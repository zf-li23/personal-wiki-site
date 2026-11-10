---
title: Principles of Vaccination and Immune Intervention
description: Active and passive immunity; correlates of protection and the immunological goals of a vaccine; antigen, adjuvant and T dependence determine the type of response induced by each class of vaccine (toxoid, subunit, polysaccharide and conjugate, live, nucleic acid); antibody kinetics of primary and booster immunization; the herd immunity threshold and vaccine efficacy; principles of antibody drugs, cytokine therapy, immunosuppression and immune enhancement.
source_hash: c89d41a951bb
---

The last question on the knowledge pathway is "how is the threat remembered after clearance", and vaccination is humanity's most successful use of the answer: before the real pathogen is ever encountered, the immune system is made to "rehearse" and leaves memory behind. Once the earlier chapters are understood (how antigen is presented ([7.15.14](/7.15.14)), how T cells are activated and differentiate ([7.15.16](/7.15.16), [7.15.17](/7.15.17)), how B cells produce high-affinity antibody and memory through the germinal center ([7.15.20](/7.15.20)), and how memory is maintained ([7.15.18](/7.15.18))), vaccinology is almost entirely a combined application of them: which antigen to choose, what innate signals are needed, which class of response is to be induced, and which kind of memory protection requires. Following this thread, the chapter presents the immunological principles of vaccines, asking only "why can protection be induced" and not touching preparation or production. The definitions of vaccine platforms and virological details are in [7.11.28](/7.11.28), herd immunity and epidemiology in [7.11.35](/7.11.35), and which response the host needs in [7.15.32](/7.15.32). The second half of the chapter brings together the methods of "deliberately altering the immune response": antibody drugs, cytokine therapy, immunosuppression and immune enhancement, which act on different links of the knowledge pathway; most have appeared in earlier chapters, and a unified picture is given here.

## 33.1. Active and Passive Immunity

**Definition 33.1.1 (Active Immunity)** The protection established when the body's own immune system is activated by antigen (infection or vaccine) to produce effector cells, antibodies and memory cells is called **active immunity**.

**Definition 33.1.2 (Passive Immunity)** The protection obtained by transferring preformed antibody (or sensitized cells) to a recipient is called **passive immunity**.

The two differ in whether the recipient's own response is involved, and therefore in whether there is memory:

| Comparison | Active immunity | Passive immunity |
|---|---|---|
| Onset | Days to weeks (the primary response requires expansion, [7.15.18](/7.15.18)) | Immediate |
| Duration | Years to lifelong (memory) | Short, declining with antibody (IgG half-life about 3 weeks) |
| Memory | Yes | No; may even suppress the recipient's own response |
| Source | Natural infection; vaccines | Maternal IgG across the placenta and IgA in breast milk; antisera and antitoxins; pooled human immunoglobulin; monoclonal antibodies |
| Risks | Adverse vaccine reactions; danger of live vaccines for the immunodeficient | Allergy and serum sickness caused by heterologous serum ([7.15.27](/7.15.27)); development of anti-xenogeneic or anti-allotypic antibodies |
| Use | Prevention | Antibody deficiency ([7.15.31](/7.15.31)); toxin or venom exposure; situations needing immediate protection after exposure when active immunization comes too late (rabies, tetanus, hepatitis B and others); temporary protection of infants |

Natural passive immunity is maternal antibody: in late pregnancy maternal IgG is actively transported across the placenta by FcRn, so for several months after birth the newborn has antibodies to the pathogens the mother has encountered; secretory IgA in breast milk protects the infant gut ([7.15.21](/7.15.21), [7.15.23](/7.15.23)). Artificial passive immunization uses antitoxins (originally horse serum), pooled immunoglobulin from many donors, highly specific hyperimmune globulin, and monoclonal antibodies; the last can be Fc-engineered to extend half-life (strengthening pH-dependent binding to FcRn), lengthening the period of protection from weeks to months. Passively administered antibody produces no immunological memory, and maternal antibody can also bind vaccine antigen and mask it, which is one reason infant vaccines are given only some time after birth (§33.4).

## 33.2. What a Vaccine Must Induce: Correlates of Protection

**Definition 33.2.1 (Correlate of Protection)** An immune response that is statistically associated with protection, can be measured, and can serve as an immunological indicator of whether a vaccine is effective is called a **correlate of protection**.

The first question in designing a vaccine is: to prevent this infection, what immune memory must the body already have? The answer depends on the location–effector matching described in the previous chapter ([7.15.32](/7.15.32)): where an extracellular toxin must be neutralized, circulating antitoxin is needed; where viral entry into the mucosa must be prevented, mucosal IgA is needed; where intracellular pathogens must be killed, Th1 and CTL memory are needed. A correlate of protection is the measurable form of this goal:

| Vaccine target | Correlate of protection (commonly used reference values, varying with the assay) | Notes |
|---|---|---|
| Tetanus, diphtheria | Serum antitoxin concentration (above about 0.01 IU/ml) | The toxin acts rapidly, leaving no time for a memory response, so circulating antibody is needed (periodic boosting) |
| Hepatitis B | Anti-HBs antibody (above about 10 mIU/ml) | People whose antibody has fallen below the threshold are still protected by memory, and boosting is often unnecessary |
| Influenza | Hemagglutination inhibition titer (about 1:40 corresponds to about 50% protection) | The incubation period is only 1–2 days, so preexisting antibody is required |
| Measles | Neutralizing antibody (about 120 mIU/ml) | The antibody threshold is linked to estimates of herd immunity |
| Tuberculosis, HIV, malaria | No generally accepted correlate of protection to date | This is one reason vaccine development is difficult |

Correlates of protection also determine the vaccination strategy. If the incubation period of the pathogen is long (hepatitis B, rabies, measles: weeks), a memory response has time to be activated and memory alone is sufficient; if the incubation period is short or the toxin acts rapidly (influenza, tetanus), memory comes too late, preexisting circulating antibody is needed, and the vaccine must maintain antibody levels, hence booster immunization. Conversely, for some infections protection requires cellular immunity, and antibody level is not a good indicator (protection against tuberculosis is related to Th1 cells, but IFN-γ levels alone do not predict protection). Correlates of protection are determined empirically in late clinical trials, and finding one is the most time-consuming step in vaccine research; there are also cases of "targeting a correlate of protection yet not protecting", so phase III trials must still look at real protective effect.

## 33.3. How Vaccines Induce Responses

### 33.3.1. Antigen, Adjuvant and Innate Signals

What a vaccine must induce is adaptive immunity, and starting adaptive immunity requires two signals ([7.15.16](/7.15.16)): antigen (signal 1, what antibodies and T cells recognize specifically) and the innate "alarm" (costimulatory molecules and cytokines). Purified antigens (proteins, polysaccharides) carry no alarm signal and cause only weak responses or even tolerance, so a vaccine either retains the alarm molecules of the pathogen itself or adds an **adjuvant** ([7.15.8](/7.15.8)). Adjuvants provide stimulation of pattern recognition receptors ([7.15.6](/7.15.6)): aluminum salts, through the depot effect of antigen and activation of the inflammasome, promote antigen uptake and recruit cells, favoring humoral immunity; TLR4 agonists (low-toxicity derivatives of lipid A), TLR9 agonists (CpG oligonucleotides) and saponins mature dendritic cells and enhance Th1 and antibody responses; oil-in-water emulsions enhance local cell recruitment. Choosing an adjuvant is choosing the desired type of response, consistent with the principle in [7.15.17](/7.15.17) that innate signals determine the Th subset.

### 33.3.2. T Dependence and Conjugate Vaccines

The chemical nature of an antigen determines whether it obtains T cell help ([7.15.8](/7.15.8), [7.15.20](/7.15.20)). Protein antigens are thymus-dependent antigens: B cells internalize them and present them as peptide–MHC II to Tfh cells, which gives class switching, germinal centers and memory. Capsular polysaccharides are thymus-independent antigens with repeating epitopes that can directly cross-link the BCR and activate B cells, but without T cell help the antibody is mainly IgM, with weak class switching and memory, and the B cells of infants and children under 2 years respond especially poorly to polysaccharides. This makes pure polysaccharide vaccines essentially ineffective in infants and young children, precisely the age at which encapsulated bacteria are most dangerous.

**Definition 33.3.1 (Conjugate Vaccine)** A vaccine made by covalently linking a polysaccharide antigen to a protein carrier, which converts the immune response to the polysaccharide into a T-dependent one, is called a **conjugate vaccine**.

The principle is "linked recognition" (the hapten–carrier effect): a B cell binds the polysaccharide specifically through its BCR and internalizes the whole conjugate, presenting peptides of the carrier protein on MHC II to carrier-specific Th cells; the Th cells then give help to this B cell, which recognizes only the polysaccharide, so that it enters the germinal center, undergoes class switching, and produces high-affinity antibody and memory B cells. Conjugate vaccines are therefore effective in infants and young children and can be boosted. Conjugate vaccines against *Streptococcus pneumoniae*, *Neisseria meningitidis* and *Haemophilus influenzae* type b have greatly reduced invasive disease in children and are among the most successful applications of immunological principles in vaccinology.

### 33.3.3. Toxoids and Subunit Vaccines

**Definition 33.3.2 (Toxoid)** A bacterial exotoxin that has lost toxicity by denaturation or genetic means while retaining antigenicity is called a **toxoid**.

Toxoids induce antibodies that neutralize the toxin (antitoxin), because the symptoms of tetanus and diphtheria come entirely from the toxin and not from bacterial growth ([7.11.33](/7.11.33)): antibody binds the toxin so that it cannot bind receptors on target cells, and it is then cleared by phagocytosis. Because the toxin acts rapidly and circulating antibody is needed rather than waiting for a memory response (§33.2), regular boosting is required, for example tetanus toxoid every ten years in adults.

**Definition 33.3.3 (Subunit Vaccine)** A vaccine that contains only one or several purified or recombinant antigenic components of the pathogen (proteins, polysaccharides, virus-like particles) and not the whole pathogen is called a **subunit vaccine**.

The advantage of subunit vaccines is safety: they contain no replicating pathogen and carry no danger of reversion to virulence; the cost is that purified antigen has almost no innate signal, so immunogenicity is weak and adjuvants and multiple doses are needed ([7.15.8](/7.15.8)), and the response induced is mainly antibody and CD4⁺ T cell, because exogenous protein is presented through the MHC II pathway and rarely enters cross-presentation ([7.15.14](/7.15.14)). **Virus-like particles** ([7.11.28](/7.11.28)) are an interesting exception: they consist of many copies of surface protein arranged in an ordered repeating array, similar to the structure of the virion, and this dense repeating epitope array can cross-link many BCRs at once, greatly lowering the activation threshold of B cells, so immunogenicity is far higher than that of the same protein in solution.

### 33.3.4. Live, Inactivated and Nucleic Acid Vaccines: Comparison of Response Types

The immunological differences between vaccine platforms depend mainly on two things: whether the antigen is produced inside cells (presented on MHC I, inducing CTLs) or comes from outside (on MHC II, inducing antibody and CD4⁺ T cells); and whether the innate signal comes with the vaccine or must be added.

| Platform | Location and source of antigen | Main response induced | Innate signal and adjuvant | Immunological features and limitations |
|---|---|---|---|---|
| **Live attenuated vaccine** | The pathogen replicates to a limited extent in the body; antigen is produced inside cells | Antibody, CD4⁺ and CD8⁺ T cells; the mucosal route can induce IgA | Carries a complete set of PAMPs | Response closest to natural infection, often long-term memory after a single dose; may revert to virulence, contraindicated in the immunodeficient ([7.15.31](/7.15.31)); preexisting antibody (such as maternal antibody) can stop it replicating and render it ineffective |
| **Inactivated vaccine** | Exogenous, particulate | Antibody and CD4⁺ T cells; weak CTL | Partly retains PAMPs, adjuvant often needed | Safe, requires multiple doses; if inactivation destroys neutralizing epitopes, it does not protect and may even worsen disease ([7.11.28](/7.11.28)) |
| Toxoid | Exogenous protein | Antitoxin antibody | Adjuvant needed | Regular boosting needed (§33.3.3) |
| Subunit and recombinant protein | Exogenous protein | Antibody, CD4⁺ T cells | Adjuvant needed | Safe, weakly immunogenic; conformational epitopes must be preserved |
| Polysaccharide | Thymus-independent | IgM; weak class switching and memory | No T help | Ineffective in infants and young children; no memory |
| **Conjugate vaccine** | Polysaccharide plus carrier protein | T-dependent IgG, memory B cells | Adjuvant often needed | Effective in infants and young children; can be boosted |
| **mRNA vaccine** | Synthesized by the recipient's own cells, native conformation | Antibody (strong Tfh and germinal center response), CD4⁺ and CD8⁺ T cells | The carrier and the RNA supply innate signals, high immunogenicity; nucleoside modification dampens unwanted interferon responses ([7.11.28](/7.11.28)) | Versatile platform, relatively high reactogenicity; duration of memory and need for boosters depend on the antigen |
| Viral vector and DNA vaccines | Expressed inside cells | Strong CD8⁺ T cells and antibody | The vector supplies signals | Immunity to the vector itself (preexisting or generated after vaccination) limits repeated use |

This table shows that vaccine design works backward from the correlate of protection: to induce antibody and Tfh cells, a subunit vaccine with a good adjuvant suffices; to induce CTLs, antigen must be synthesized inside cells or cross-presented, which live vaccines, vectors and nucleic acid vaccines can do; and to protect infants and young children from encapsulated bacteria, the polysaccharide must be made T-dependent by conjugation.

## 33.4. Priming, Boosting and Antibody Kinetics

**Definition 33.4.1 (Booster Immunization)** Vaccination in which the same antigen is given again at an interval after the primary immunization, to recall memory cells and raise and prolong the level of protection, is called **booster immunization**.

Booster immunization is necessary because the response to a single vaccination is often insufficient: the primary response has lower affinity and the memory pool is small ([7.15.18](/7.15.18)); a booster recalls memory B cells and Th cells, which reenter germinal centers and, through another round of somatic hypermutation and selection ([7.15.20](/7.15.20)), yield antibody of higher affinity and produce new long-lived plasma cells. The interval between doses also matters immunologically: if too short, antibody from the previous response is still high and binds and masks the antigen, suppressing the secondary response, and affinity maturation in the germinal center is not yet complete; with a longer interval, memory is more fully developed, so antibody after the booster is usually higher and lasts longer. The antibody response consists of two kinds of plasma cells: antibody from short-lived plasma cells (half-life of weeks) falls rapidly within weeks to months, whereas long-lived plasma cells survive in bone marrow niches for years to decades and maintain a stable low level.

**Example 33.4.1** A phenomenological model illustrates this. The antibody produced by the $k$-th antigen exposure at time $t_k$ is

$$
A_k(t) = a_k\bigl(1 - \mathrm{e}^{-(t - t_k)/\tau}\bigr)\Bigl[(1 - \varphi_k)\,\mathrm{e}^{-\ln 2\,(t - t_k)/T_{\mathrm{s}}} + \varphi_k\,\mathrm{e}^{-\ln 2\,(t - t_k)/T_{\mathrm{l}}}\Bigr],\quad t \ge t_k,
$$

and the total titer is the sum over exposures. Here $\tau = 4\,\mathrm{d}$ describes the rise, $T_{\mathrm{s}} = 30\,\mathrm{d}$ and $T_{\mathrm{l}} = 730\,\mathrm{d}$ are the half-lives of antibody from short-lived and long-lived plasma cells, and $\varphi_k$ is the fraction of the long-lived component; passively administered IgG decays only with a half-life of $21\,\mathrm{d}$ (FcRn recycling, [7.15.21](/7.15.21)). Take illustrative parameters: primary vaccination $a_1 = 100$, $\varphi_1 = 0.10$; a booster 4 weeks later with $a_2 = 600$, $\varphi_2 = 0.25$; alternatively, a booster after 6 months with $a_2 = 2500$, $\varphi_2 = 0.35$ (relative units, protection threshold set at 10). The results are shown in the figure:

- Passive immunization giving a titer of 100 lasts only about $21\log_2(100/10)\approx 70$ days and leaves no memory;
- A single active immunization peaks on day 10 (about 75), the short-lived component decays within weeks, and the titer falls below the threshold at about day 176;
- A booster after 4 weeks raises the peak to about 510 and leaves a higher long-lived component, still about 83 after 2 years, above the threshold;
- A booster after 6 months gives a peak of about 2000 and about 530 after 2 years, about 6 times that of the 4-week interval.

These numbers are outputs of the model's assumptions, not measurements, but they agree qualitatively with observation: a booster raises the titer by more than an order of magnitude, greatly prolongs the time above the protective threshold, and a longer interval gives a higher long-term titer. The model also shows that the duration of protection depends on the fraction of the long-lived component rather than on the height of the peak: a vaccine with a high peak but little long-lived component loses protection quickly (such as polysaccharide vaccines and some inactivated vaccines), whereas a vaccine with a modest peak but much long-lived component (such as live vaccines) protects durably.

:::

![Antibody titer after active and passive immunization (illustrative model, see Example 33.4.1; vertical axis in relative units on a logarithmic scale, dashed line the assumed protective threshold). A: passively transferred IgG decays with a half-life of 21 days, whereas the antibody of a single active immunization first rises and then falls to a plateau of the long-lived component. B: comparison of boosters after 4 weeks and 6 months; boosting greatly raises the peak and the long-term titer, which is higher with the longer interval](./plots/antibody-timecourse.py)

## 33.5. Herd Immunity and Vaccine Efficacy

The protection of a vaccine is not confined to the individual: when a sufficiently high fraction of the population is immune, transmission chains are broken and individuals without immunity are also protected (for the definition of herd immunity and the epidemiology of $R_0$ see [7.11.28](/7.11.28) and [7.11.35](/7.11.35)). This section adds only one point: vaccines are not 100% effective. Let $p$ be the vaccination coverage and $E$ the probability (efficacy) that the vaccine protects a vaccinated person from infection; then the effective reproduction number is

$$
R = R_0\,(1 - Ep),
$$

and for $R<1$ the coverage must exceed

$$
p_{\mathrm{c}} = \frac{1 - 1/R_0}{E}.
$$

When $E = 1$ this returns to the threshold $1 - 1/R_0$ of [7.11.28](/7.11.28); when $E < 1 - 1/R_0$, even vaccinating the whole population cannot interrupt transmission and can only lower the incidence of disease.

**Example 33.5.1** Take $R_0 = 15$ for measles: a fully effective vaccine requires a coverage of $93.3\%$; if the efficacy of two doses is $97\%$, $96.2\%$ is needed; if the efficacy is only $90\%$, then $p_{\mathrm{c}} = 103.7\% > 1$ and vaccination alone cannot interrupt transmission. Take also $R_0 = 6$ (the order of poliomyelitis): efficacy $95\%$ requires coverage of $87.7\%$. This simple relation illustrates three points: the more infectious the pathogen, the more demanding the requirements for vaccine efficacy and coverage; the efficacy of a single dose is insufficient and boosters are needed to raise $E$ (§33.4); and vaccines with low efficacy and short duration (such as vaccines against mucosal viruses with limited protection) can hardly eliminate disease through herd immunity and can only reduce severe disease.

:::

![Vaccine efficacy and the herd immunity threshold (see Example 33.5.1). A: coverage $p_c = (1 - 1/R_0)/E$ needed to interrupt transmission as a function of $R_0$ at different efficacies; the gray bands are typical $R_0$ ranges from the literature (influenza, poliomyelitis, measles) and crosses mark positions where the efficacy is insufficient to reach the threshold. B: effective reproduction number $R$ as a function of coverage at $R_0=15$; the threshold is at R = 1](./plots/herd-threshold.py)

## 33.6. Immune Intervention: Antibody Drugs, Cytokines and Immune Modulation

Deliberately altering the immune response means intervening in one link of the knowledge pathway: either supplementing or amplifying it, or removing or blocking it. The table below arranges interventions by direction and target, and almost every entry corresponds to an earlier chapter.

| Strategy | Principle | Examples | Position on the pathway |
|---|---|---|---|
| Neutralizing antibody drugs | Bind and block a soluble factor or its receptor | Anti-TNF-α, anti-IL-6 receptor, anti-IL-5, anti-IgE ([7.15.26](/7.15.26)) | Effector and inflammation |
| Cell-depleting antibodies | Remove cells expressing the target antigen through ADCC, complement and apoptosis ([7.15.21](/7.15.21)) | Anti-CD20 depletes B cells (autoimmune disease and B cell tumors) | Recognition and effector |
| Checkpoint blockade | Release inhibition of T cells ([7.15.25](/7.15.25), [7.15.30](/7.15.30)) | Anti-PD-1, anti-CTLA-4 | Regulation |
| Bispecific antibodies and T cell engagers | One arm against a tumor antigen and the other against CD3, pulling T cells next to tumor cells and bypassing MHC | CD3×CD19 | Decision and effector |
| Cytokine therapy | Supplement or block cytokine signals ([7.15.11](/7.15.11)) | IFN-γ (chronic granulomatous disease, [7.15.31](/7.15.31)); low-dose IL-2 to expand Tregs; colony-stimulating factors for neutropenia | Decision |
| Immunosuppression | Inhibit T cell activation or proliferation ([7.15.16](/7.15.16), [7.15.29](/7.15.29)) | Glucocorticoids (inhibit transcription factors such as NF-κB); calcineurin inhibitors (block NFAT); mTOR inhibitors; antimetabolites; JAK inhibitors; costimulation blockade (CTLA4-Ig) | Decision |
| Immune enhancement | Strengthen the response | Vaccines and adjuvants; checkpoint blockade; adoptive cell therapy (CAR-T, [7.15.30](/7.15.30)); TLR agonists | Recognition and decision |
| Tolerance induction | Steer the response toward tolerance or suppression | Allergen immunotherapy ([7.15.26](/7.15.26)); exploration of Treg therapy | Regulation |

There are three immunological points about antibody drugs. First, **monoclonal antibodies** derived from mice are immunogenic and provoke antidrug antibodies, so this has been progressively reduced by chimerization (keeping the mouse variable region and replacing the constant region with a human one) and humanization (keeping only the CDRs), and later fully human antibodies went further ([7.15.9](/7.15.9)); the suffixes of drug names (-ximab, -zumab, -umab) record this evolution. Second, Fc function can be tuned as needed: to deplete target cells, enhance binding to FcγR and complement; to block without depleting, weaken it; to prolong half-life, engineer binding to FcRn ([7.15.21](/7.15.21)). Third, **bispecific antibodies** put two specificities in one molecule, used to redirect effector cells. The price of immunosuppressive therapy is secondary immunodeficiency ([7.15.31](/7.15.31)): it suppresses the pathological response but also the protective response, so the more specific the targeting, the smaller the side effects.

## 33.7. Immunosenescence and the Limits of Vaccines

The elderly respond poorly to vaccines for reasons already described in [7.15.18](/7.15.18): thymic involution reduces the output of naive T cells and the diversity of the repertoire, and weakened germinal center reactions impair antibody affinity maturation, so responses to new antigens are especially affected. The immunological countermeasures are to strengthen antigen, adjuvant and number of doses to raise immunogenicity, and to concentrate on preexisting memory (boosting) rather than on the primary response.

Vaccines also have immunological limits, each a consequence of principles that appeared in earlier chapters:

- Pathogens without a correlate of protection (tuberculosis, HIV, malaria) are hard to design vaccines for, because it is not known what to induce; the envelope glycan shield and high mutation rate of HIV make broadly neutralizing antibodies rare ([7.15.31](/7.15.31)), and antigenic variation of *Plasmodium* limits the protection of single-antigen vaccines ([7.15.32](/7.15.32)).
- Antigenic variation and original antigenic sin: influenza vaccines must be updated every year, and preexisting memory can be biased toward old epitopes; the idea of universal vaccines is to target conserved epitopes (such as the stem of influenza HA) to induce responses effective against several subtypes ([7.15.32](/7.15.32)).
- Antibody-dependent enhancement and disease worsening: sub-neutralizing antibody can worsen dengue virus infection, and historically an inactivated respiratory syncytial virus vaccine worsened subsequent infection ([7.11.28](/7.11.28)), so the safety assessment of vaccines must look at the type of response and not only at the amount of antibody.
- Mucosal protection: injection mainly produces serum IgG and circulating memory cells, with limited protection against pathogens at mucosal surfaces; inducing IgA and tissue-resident memory T cells at mucosae requires mucosal vaccination or a "systemic priming, mucosal boosting" strategy ([7.15.18](/7.15.18), [7.15.23](/7.15.23)).
- Timing of vaccination: maternal antibody in infants can bind vaccine antigen and lower the response, so many vaccines are given only after maternal antibody is exhausted or in multiple doses; live vaccines cannot be given to the immunodeficient.

## Summary

- Active immunity (Definition 33.1.1) arises from one's own response, with slow onset, memory and durability; passive immunity (Definition 33.1.2) transfers antibody, with immediate onset, brief duration and no memory; natural examples are maternal IgG and milk IgA.
- A vaccine must induce the correlate of protection (Definition 33.2.1), which depends on the location of the pathogen and the incubation period: toxins require circulating antibody, long-incubation infections can rely on memory, and intracellular infections need T cells; for some pathogens there is no correlate of protection to date.
- Antigen plus an innate signal (adjuvant) is needed to activate adaptive immunity; protein antigens are T-dependent and polysaccharides T-independent; the conjugate vaccine (Definition 33.3.1) makes the response to polysaccharide T-dependent through linked recognition and is effective in infants and young children; the toxoid (Definition 33.3.2) induces antitoxin; the subunit vaccine (Definition 33.3.3) is safe but weakly immunogenic and needs an adjuvant, and the repeating array of virus-like particles enhances B cell activation.
- Platforms in which antigen is produced inside cells (live vaccines, vectors, nucleic acids) induce CTLs, whereas exogenous antigen induces antibody and CD4⁺ T cells; the response type of each platform is in the table of §33.3.4.
- Booster immunization (Definition 33.4.1) recalls memory and carries out affinity maturation once more; the duration of protection is determined by the fraction of long-lived plasma cells (Example 33.4.1: a booster raises the titer by an order of magnitude, and a longer interval gives a higher long-term titer).
- When vaccine efficacy is incomplete, the coverage needed to interrupt transmission is $p_{\mathrm{c}} = (1-1/R_0)/E$, and transmission cannot be interrupted when $E < 1 - 1/R_0$ (Example 33.5.1).
- Immune interventions are arranged by link on the knowledge pathway: neutralizing or depleting antibodies, checkpoint blockade, bispecific antibodies, cytokines, immunosuppression, immune enhancement and tolerance induction; humanization and Fc engineering of antibody drugs tune function as needed.
- The limits of vaccines come from immunological principles themselves: lack of correlates of protection, antigenic variation and original antigenic sin, antibody-dependent enhancement, mucosal protection, interference by maternal antibody, and immunosenescence.

## Questions

1. Why does tetanus vaccine need a booster every ten years, whereas hepatitis B vaccine usually needs no booster after antibody has fallen below the threshold?

   **Answer** Tetanus is caused by a toxin that acts rapidly, so enough antitoxin must already be circulating to neutralize it, and a memory response comes too late; protection therefore depends on the serum antibody level, and as antibody declines over time a booster is needed. Hepatitis B has a long incubation period (weeks to months), and the virus needs time to reach the liver and replicate, during which memory B and T cells can be reactivated to produce a protective response; so even when anti-HBs antibody has fallen below the threshold, memory still protects and routine boosting is usually unnecessary (except in the immunodeficient).

2. A purified bacterial capsular polysaccharide is effective in 5-year-old children and almost ineffective in 1-year-old infants; after it is covalently linked to tetanus toxoid, infants also produce antibody and form memory. Explain this using T dependence and linked recognition.

   **Answer** The polysaccharide is a thymus-independent antigen that can activate mature B cells by cross-linking the BCR, but without T cell help there is only IgM, with no class switching or memory, and the B cells of infants respond weakly to polysaccharide anyway, so it is ineffective. In the conjugate vaccine, the B cell binds the polysaccharide through the BCR and internalizes the whole conjugate, presenting peptides of tetanus toxoid on MHC II to carrier-specific Th cells, which then help the B cell (CD40L and cytokines), so that it enters the germinal center, undergoes class switching and produces memory B cells. The T cells of infants respond well to protein, so the T-dependent response can make up for the deficiency of the polysaccharide response.

3. Using the formula of Example 33.5.1, answer: for a pathogen with $R_0 = 4$ and vaccine efficacy $E = 70\%$, can transmission be interrupted by vaccination? What about $E=90\%$? What coverage is needed in each case?

   **Answer** $1 - 1/R_0 = 0.75$. With $E=70\%<75\%$, $p_{\mathrm{c}} = 0.75/0.7 = 107\%>1$, so even vaccinating the entire population cannot interrupt transmission completely, and only lowers $R$ to $4\times(1-0.7)=1.2>1$. With $E=90\%$, $p_{\mathrm{c}} = 0.75/0.9 \approx 83.3\%$, and coverage above about 83% suffices to interrupt transmission. This shows that vaccine efficacy and coverage are equally important.

4. According to Example 33.4.1, how would the duration of protection change if a vaccine raised only the fraction $\varphi$ of the long-lived component from 0.1 to 0.3 with the peak unchanged? Why is this important in vaccine design?

   **Answer** With the same peak, the short-lived component decays quickly with its 30-day half-life, and the later titer is determined mainly by the long-lived component $\varphi a$, so a 3-fold increase in $\varphi$ raises the plateau about 3-fold, and the time at which the titer falls to the protective threshold is markedly delayed. For the single vaccination of Example 33.4.1, the plateau is about $\varphi\times a$, rising from $10$ to $30$, above the threshold of 10, so protection can be maintained for a long time. This shows that the aim of vaccine design is not simply to raise the peak but to raise the formation of long-lived plasma cells and memory cells, which depends on the germinal center reaction, Tfh help and adjuvant ([7.15.20](/7.15.20)).

5. (Open question) A vaccine is to be designed for a virus with a very short incubation period, infection at the upper respiratory mucosa and a variable surface antigen. Propose a design approach in terms of correlate of protection, response type, route of vaccination and antigen choice, and point out possible limitations.

   **Answer** Outline: with a short incubation period, preexisting antibody is needed rather than reliance on memory, so the correlate of protection should be neutralizing antibody (mucosal IgA and serum IgG) and rapid tissue-resident memory T cells; the response type should be antibody plus CD4⁺ and CD8⁺ T cells, with induction of tissue-resident memory; as route, consider mucosal (intranasal) vaccination or a systemic-then-mucosal strategy to induce mucosal IgA and tissue-resident memory T cells; for antigen choice, variable surface antigens are easily escaped, so prefer conserved epitopes (the stem, T cell epitopes of internal proteins) or a multivalent design, and choose adjuvant and platform to balance antibody and T cell responses. Limitations include: original antigenic sin biasing the response toward old epitopes, short duration of mucosal immunity requiring repeated boosting, the need for large trials to validate protection when there is no reliable correlate of protection, and the fact that epitopes giving broad protection are often not immunodominant and are hard to induce.
