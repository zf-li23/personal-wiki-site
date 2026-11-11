---
title: Inflammation and Innate Effector Mechanisms
description: How innate immunity acts once it has recognized a threat. The cascade of acute inflammation and its mediators, fever and the acute-phase response, the killing mechanisms of phagocytes (phagolysosome, respiratory burst, reactive nitrogen species, neutrophil extracellular traps), opsonization, the first line of antiviral defense, the three phases of innate immunity and the transition to adaptive immunity, resolution and dysregulation of inflammation, and a kinetic model of the race between pathogen and innate effector cells.
source_hash: fef24026d484
---

[7.15.5](/7.15.5) introduced the barriers and cells of innate immunity, and [7.15.6](/7.15.6) described how they detect pathogens with pattern recognition receptors. This chapter answers the next question on the path of knowledge: once a pathogen has been recognized, what effectors does innate immunity use to eliminate it? (This is the innate-immunity answer to the "effector" question of [7.15.1](/7.15.1).) The core of the answer is **inflammation**. Sentinel cells in the tissue raise the alarm, the blood vessels deliver fluid, complement and leukocytes to the site of infection, and phagocytes there engulf and kill the microbes. The same alarm molecules also act on the liver and the hypothalamus, producing the acute-phase response and fever.

Innate immunity acts within minutes to days after infection, and most infections are terminated at this stage. Those that are not are passed on by dendritic cells, which carry the information to the lymph node and start adaptive immunity. This chapter is therefore also the hand-over point between innate and adaptive immunity: antibodies ([7.15.9](/7.15.9)), complement ([7.15.10](/7.15.10)) and cytokines ([7.15.11](/7.15.11)) in the following chapters all return to the effector functions described here. A general physiological account of inflammation is given in [7.14.15](/7.14.15) and of thermoregulation in [7.14.31](/7.14.31); this chapter covers only the immunological mechanisms.

## 7.1. The Cascade of Acute Inflammation

### 7.1.1. From Recognition to the Vascular Response

Acute inflammation is a chain of events, each causing the next. After a barrier in the skin or a mucosa has been breached, tissue-resident **macrophages**, **mast cells** and **dendritic cells** recognize **pathogen-associated molecular patterns** and **damage-associated molecular patterns** through **pattern recognition receptors**, and within minutes to hours they release three classes of signals:

- Preformed mediators: **degranulation** of mast cells releases histamine, which acts within seconds to minutes.
- Newly synthesized lipid mediators: **prostaglandins** and leukotrienes, made from arachidonic acid released from membrane phospholipids through the cyclooxygenase (COX) and 5-lipoxygenase pathways.
- Newly transcribed proteins: the proinflammatory **cytokines** TNF-α, IL-1β and IL-6 and **chemokines** (such as CXCL8, also called IL-8). These require activation of transcription factors such as NF-κB and take tens of minutes to hours to appear.

These molecules act on the small local vessels. Dilation of arterioles increases blood flow; the endothelial cells of the postcapillary venules contract and the gaps between them widen, so plasma proteins and fluid leak into the tissue. The exudate brings **complement**, antibodies, and components of the coagulation and kinin systems, and the tissue swells. The four cardinal signs of inflammation recorded by the Roman physician Celsus (redness, swelling, heat, pain), and loss of function, added later (usually credited to Virchow), can all be explained by these vascular changes:

| Sign | Mechanism |
|---|---|
| Redness (rubor) | Arteriolar dilation increases local blood volume |
| Heat (calor) | Increased blood flow brings more heat from the body core; systemic fever is treated in §7.2.1 |
| Swelling (tumor) | Increased venular permeability lets plasma escape, forming **edema** |
| Pain (dolor) | Bradykinin and prostaglandin E2 sensitize and activate nociceptor endings; swelling stretches the tissue |
| Loss of function (functio laesa) | Pain, swelling and tissue damage together limit movement |

### 7.1.2. Recruitment of Leukocytes

Within a few hours, TNF-α and IL-1β induce the local endothelium to express E-selectin, P-selectin, ICAM-1 and VCAM-1 and to display chemokines on its surface. Leukocytes in the blood pass in turn through rolling, activation, firm adhesion and transmigration across the endothelium. This is the **leukocyte adhesion cascade** (molecules and steps in [7.15.4](/7.15.4)), and its last step is **diapedesis**. Once in the tissue, leukocytes move toward the focus of infection along concentration gradients of chemokines and of the complement fragment C5a (**chemotaxis**).

Recruitment follows a fixed order. **Neutrophils** arrive first, begin to accumulate within hours and peak at 6–24 h. **Monocytes** follow and differentiate into macrophages in the tissue, becoming the dominant population at 24–72 h. The sequence is set by chemokines: ELR⁺ CXC chemokines such as CXCL8 mainly recruit neutrophils, whereas CCL2 mainly recruits monocytes. Neutrophils are short-lived and highly destructive, and they bring the pathogen quickly under control. Macrophages are long-lived; they continue to phagocytose, clear apoptotic neutrophils and tissue debris, and initiate repair. In inflammation driven by type 2 immunity, eosinophils replace neutrophils as the main recruited cells ([7.15.26](/7.15.26)).

![The cascade of acute inflammation. A: Pathogens in the tissue are recognized by sentinel cells such as macrophages and mast cells, which release histamine, prostaglandins, TNF-α, IL-1β, IL-6 and chemokines. These mediators dilate vessels, increase permeability and activate the endothelium; plasma proteins (complement, antibodies, kinins) enter the tissue with the fluid, and leukocytes emigrate through the adhesion cascade. Neutrophils arrive first and monocytes later, differentiating into macrophages in the tissue. TNF-α, IL-1β and IL-6 also enter the blood and act on the hypothalamus (fever), the liver (acute-phase proteins) and the bone marrow (mobilization of neutrophils). B: Time course of local infiltrating cells (qualitative sketch): neutrophils peak at 6–24 h, monocytes and macrophages dominate at 1–3 d, followed by resolution and repair](./plots/inflammation-cascade.py)

### 7.1.3. Inflammatory Mediators

**Definition 7.1.1 (Inflammatory Mediator)** An **inflammatory mediator** is a soluble molecule that is released by cells, or produced by activation of a plasma precursor, during inflammation and that acts on vessels, leukocytes or nerve endings to produce the manifestations of inflammation. By origin, mediators are either cell-derived (preformed or newly synthesized) or plasma-derived (activation products of the complement, kinin and coagulation systems).

| Mediator | Source | Main actions |
|---|---|---|
| Histamine | Granules of mast cells and basophils (preformed) | Arteriolar dilation, increased venular permeability; acts within minutes and is short-lived |
| Prostaglandins (PGE2, PGI2) | Many cell types, synthesized via induced COX-2 | Vasodilation; PGE2 causes pain and fever |
| Leukotriene B4 (LTB4) | Neutrophils, macrophages, via 5-lipoxygenase | Recruits and activates neutrophils |
| Cysteinyl leukotrienes (LTC4, LTD4, LTE4) | Mast cells, eosinophils | Increased permeability, smooth-muscle contraction (bronchoconstriction, see [7.15.26](/7.15.26)) |
| Platelet-activating factor (PAF) | Many leukocytes, endothelium | Platelet aggregation, increased permeability, leukocyte activation |
| Bradykinin | Plasma kininogen cleaved by kallikrein | Increased permeability, vasodilation, intense pain |
| C3a, C5a | Complement activation ([7.15.10](/7.15.10)) | Mast-cell degranulation; C5a recruits and activates neutrophils |
| TNF-α, IL-1β, IL-6 | Macrophages, dendritic cells, mast cells and others | Endothelial activation; systemic actions in §7.2 |
| Chemokines (CXCL8, CCL2, etc.) | Macrophages, endothelium, epithelium | Selective recruitment of leukocytes |
| Nitric oxide (NO) | Endothelium (eNOS), macrophages (iNOS) | Vasodilation; used for killing by macrophages (§7.3.3) |

Prostaglandins and leukotrienes both belong to the **eicosanoids**. Aspirin and other nonsteroidal anti-inflammatory drugs inhibit COX and therefore reduce fever and pain; glucocorticoids act further upstream, inhibiting phospholipase A2 and the transcription of many proinflammatory genes.

## 7.2. Systemic Responses: Fever and the Acute-Phase Response

TNF-α, IL-1β and IL-6 produced in local inflammation enter the blood and act on distant organs, putting the whole organism into a "defensive state."

### 7.2.1. Fever

TNF-α, IL-1β and IL-6 are endogenous pyrogens. They induce COX-2 in the vascular endothelium around the hypothalamus; the PGE2 produced acts on neurons of the preoptic area and raises the thermoregulatory set point, and the body then raises its temperature to the new set point by generating heat and reducing heat loss (the thermoregulatory circuit and the physiology of [fever](/7.14.31) are treated in 7.14.31). Exogenous pyrogens such as bacterial **lipopolysaccharide** act mainly by inducing these cytokines. Fever is a beneficial defense: many pathogens replicate more slowly at higher temperatures, whereas lymphocyte proliferation and neutrophil migration are enhanced at 38–40 °C.

### 7.2.2. The Acute-Phase Response

**Definition 7.2.1 (Acute-Phase Response and Acute-Phase Proteins)** The **acute-phase response** is the systemic reaction, occurring within hours to days after infection or tissue injury, in which hepatocytes change the profile of plasma protein synthesis, driven mainly by IL-6 (and also IL-1β and TNF-α). Proteins whose plasma concentration changes by at least 25% during this period are called **acute-phase proteins**: those that increase are positive acute-phase proteins, and those that decrease (albumin, transferrin) are negative acute-phase proteins.

**Definition 7.2.2 (C-Reactive Protein)** **C-reactive protein** (CRP) is a pentameric pentraxin synthesized by the liver. It binds, in a $\mathrm{Ca^{2+}}$-dependent manner, to phosphocholine on bacterial surfaces and on apoptotic cell membranes. Once bound, it acts both as an opsonin and, by binding C1q, as an activator of the classical pathway of complement. It was named for its ability to precipitate the C polysaccharide of *Streptococcus pneumoniae* (1930).

CRP is normally below $3\ \mathrm{mg\,L^{-1}}$ in healthy plasma and can rise more than 1000-fold in severe bacterial infection. It begins to rise about 6 h after the stimulus and peaks at about 48 h. Its plasma half-life is roughly 19 h and almost constant, so its plasma concentration directly reflects its rate of synthesis and falls quickly once inflammation is controlled. This makes CRP the standard clinical marker for monitoring inflammation; the "high-sensitivity CRP" assay measures low-grade chronic inflammation in the range $1$–$10\ \mathrm{mg\,L^{-1}}$ and is used in cardiovascular risk assessment.

| Acute-phase protein | Change | Immunological function |
|---|---|---|
| CRP | Up to 1000-fold increase | Opsonization, activation of the classical pathway |
| Serum amyloid A (SAA) | Up to 1000-fold increase | Recruits leukocytes, binds and transports lipids |
| **Mannose-binding lectin** (MBL) | Moderate increase | Recognizes sugars on microbial surfaces and starts the lectin pathway ([7.15.10](/7.15.10)) |
| Fibrinogen | 2–4-fold increase | Coagulation, limits spread of infection; accelerates erythrocyte sedimentation |
| Complement C3, C4, factor B | About 1.5-fold increase | Replace consumed complement |
| Hepcidin | Increased | Retains iron in macrophages and lowers plasma iron, depriving bacteria of iron ("nutritional immunity") |
| Albumin, transferrin | Decreased | Negative acute-phase proteins: hepatic synthetic capacity is redirected to defense |

The acute-phase response also includes the release of neutrophils from the bone marrow (peripheral neutrophilia and the "left shift"), breakdown of muscle protein for fuel, and anorexia and somnolence caused by the hypothalamus. CRP and MBL are soluble pattern recognition molecules: like antibodies, they bind pathogens and activate complement, but their specificity is germline-encoded and they are present in quantity days before antibodies appear.

## 7.3. Phagocytosis and Killing

### 7.3.1. Phagocytosis and Opsonization

**Phagocytosis** is the most ancient effector function of innate immunity (Metchnikoff observed it in starfish larvae). Phagocytes (neutrophils, macrophages, dendritic cells) bind a particle with receptors, and actin-driven pseudopods surround it to form a **phagosome**. Receptors that recognize microbes directly include the mannose receptor, Dectin-1 (which binds fungal β-glucan) and scavenger receptors. But many pathogens have capsules or other structures that prevent direct binding, and they must first be "tagged."

**Definition 7.3.1 (Opsonization)** **Opsonization** is the process in which soluble host molecules (opsonins) bind to the surface of a particle so that it is bound and ingested more efficiently by phagocytes carrying the corresponding receptors. The main opsonins are **IgG** (recognized by Fc receptors), the complement fragments C3b and iC3b (recognized by the complement receptors CR1 and CR3), and acute-phase proteins such as CRP and MBL.

Opsonization raises the efficiency of phagocytosis by several orders of magnitude. The capsular polysaccharide of *S. pneumoniae* is not recognized directly by phagocytes, which is why encapsulated strains are virulent; once coated with anticapsular antibody and complement, the bacteria are quickly phagocytosed and cleared. This also explains why splenectomized patients, patients with complement C3 deficiency and patients with antibody deficiency are especially susceptible to encapsulated bacteria. Opsonization by antibody and by complement is treated in [7.15.9](/7.15.9) and [7.15.10](/7.15.10), and Fc receptors in [7.15.21](/7.15.21).

### 7.3.2. The Phagolysosome and Oxygen-Independent Killing

**Definition 7.3.2 (Phagolysosome)** A **phagolysosome** is the organelle formed by fusion of a phagosome with **lysosomes** (and, in neutrophils, with preformed granules). Its lumen is acidic (pH about 4.5–5) and contains hydrolases, antimicrobial proteins, and reactive oxygen and nitrogen species; it is the site where phagocytes kill and degrade ingested microbes.

During phagosome maturation (successive fusion with early endosomes, late endosomes and lysosomes; see [7.3.11](/7.3.11)), the vacuolar $\mathrm{H^+}$-ATPase acidifies the lumen. Oxygen-independent killing mechanisms include:

- **Antimicrobial peptides**: **defensins** and cathelicidin (LL-37 in humans) insert into and disrupt microbial membranes.
- **Lysozyme** hydrolyzes the **peptidoglycan** of the Gram-positive cell wall.
- Proteases (neutrophil elastase, cathepsin G) are activated in the acidic environment.
- Nutrient deprivation: lactoferrin chelates iron, and NRAMP1 pumps $\ce{Fe^2+}$ and $\ce{Mn^2+}$ out of the phagosome, depriving intracellular bacteria of metal cofactors.

Neutrophil granules fall into three classes: azurophilic granules (primary granules, containing myeloperoxidase, defensins and elastase), specific granules (secondary granules, containing lactoferrin, lysozyme and the membrane subunits of NADPH oxidase) and gelatinase granules. They fuse with the phagosome or are exocytosed in the order "last formed, first released."

### 7.3.3. The Respiratory Burst and Reactive Oxygen and Nitrogen Species

**Definition 7.3.3 (Respiratory Burst)** The **respiratory burst** is the sharp rise in oxygen consumption (more than 10 times the resting rate) that occurs within minutes after a phagocyte is stimulated. Almost all of the extra oxygen is reduced to superoxide by the NADPH oxidase (NOX2) in the phagosomal membrane, to generate microbicidal **reactive oxygen species**, and none is used for mitochondrial oxidative phosphorylation.

NOX2 is assembled from the membrane proteins gp91phox and p22phox, the cytosolic proteins p47phox, p67phox and p40phox, and the small G protein Rac; signals from phagocytic receptors or C5a translocate the cytosolic subunits to the membrane. It transfers electrons from cytosolic NADPH across the membrane to $\ce{O2}$ in the phagosomal lumen, and the reactions that follow generate a series of oxidants:

$$
\begin{aligned}
&\ce{NADPH + 2O2 -> NADP+ + H+ + 2O2^{.-}} &&\text{(NADPH oxidase)}\\
&\ce{2O2^{.-} + 2H+ -> H2O2 + O2} &&\text{(superoxide dismutase or spontaneous)}\\
&\ce{H2O2 + Cl- -> HOCl + OH-} &&\text{(myeloperoxidase, neutrophils)}
\end{aligned}
$$

Hypochlorous acid (HOCl, the active ingredient of bleach) is the most potent microbicide of the neutrophil; it oxidizes thiols, chlorinates amines and destroys iron–sulfur clusters. Macrophages activated by IFN-γ and TNF-α additionally express inducible **nitric oxide synthase** (iNOS), which produces NO from L-arginine:

$$
\ce{L-Arg + O2 + NADPH -> NO + L-citrulline},\qquad \ce{NO + O2^{.-} -> ONOO-}
$$

NO combines with superoxide to form peroxynitrite, which nitrates proteins and breaks DNA. Reactive nitrogen species are the main means by which macrophages control intracellular pathogens such as *Mycobacterium tuberculosis*, and iNOS-knockout mice lose control of these infections.

**Example 7.3.1 (Chronic Granulomatous Disease)** A hereditary defect in any subunit of NOX2 (most often a mutation in the X-linked gp91phox gene *CYBB*) prevents phagocytes from producing superoxide; this is **chronic granulomatous disease**. The patient's neutrophils phagocytose normally but cannot kill catalase-positive bacteria and fungi (*Staphylococcus aureus*, *Aspergillus*), because these microbes break down the $\ce{H2O2}$ they produce themselves, so the phagocyte has none to borrow. The surviving microbes are walled off by macrophages in the tissue, forming **granulomas**. The disease demonstrates that the respiratory burst is necessary for microbial killing (immunodeficiency diseases are treated in [7.15.31](/7.15.31)).

:::

### 7.3.4. Neutrophil Extracellular Traps

**Definition 7.3.4 (Neutrophil Extracellular Trap)** A **neutrophil extracellular trap** (NET) is a web-like structure released into the extracellular space by activated neutrophils. It consists of decondensed chromatin fibers studded with granule proteins (elastase, myeloperoxidase, antimicrobial peptides, histones) and can capture and kill bacteria, fungi and parasites. The process of releasing NETs and dying in the course of it is called NETosis.

NET formation requires reactive oxygen species generated by NADPH oxidase. Elastase and myeloperoxidase move from the granules into the nucleus, and peptidylarginine deiminase 4 (PAD4) converts histone arginine residues to citrulline; the chromatin decondenses, and the nuclear and plasma membranes then rupture. A NET can extend to 10–15 times the diameter of the cell, which suits it for dealing with pathogens too large to be phagocytosed (fungal hyphae). NETs are a double-edged sword: their DNA and histones are themselves **damage-associated molecular patterns**, persistent NETs promote thrombosis, and the autoantigens exposed in NETs (citrullinated proteins, DNA) are linked to the autoantibodies of **systemic lupus erythematosus** and **rheumatoid arthritis** ([7.15.28](/7.15.28)).

### 7.3.5. Inflammatory Cell Death and Autophagy

A macrophage infected with an intracellular pathogen can die actively, depriving the pathogen of its replication niche. After **inflammasome** activation of caspase-1, the enzyme cleaves pro-IL-1β and pro-IL-18 to their mature forms and also cleaves gasdermin D, whose N-terminal fragment forms pores in the membrane. This causes **pyroptosis** and the release of IL-1β, IL-18 and cell contents (molecular mechanism in [7.3.25](/7.3.25)). Pyroptosis exposes intracellular bacteria to neutrophils and amplifies local inflammation. In addition, bacteria that escape into the cytosol can be enclosed by **autophagy** and delivered to lysosomes for degradation; cytosolic receptors such as NOD2 can initiate this antibacterial autophagy ([7.15.6](/7.15.6)).

## 7.4. The First Line of Antiviral Defense

Viruses replicate inside cells, and phagocytosis is almost useless against them. Innate immunity relies on two mechanisms against viruses, which act as successive relays:

1. Type I **interferons** (IFN-α, IFN-β) are produced within hours of infection by infected cells and by plasmacytoid dendritic cells, and peak at 1–2 d. They cause neighboring cells to express hundreds of interferon-stimulated genes and enter an "antiviral state," and they upregulate MHC class I molecules (the molecular mechanisms of interferons and interferon-stimulated genes are in [7.11.27](/7.11.27)).
2. **Natural killer cells** are activated by type I interferons together with IL-12, IL-15 and IL-18 and peak on days 2–4. They kill infected cells that have downregulated MHC class I molecules (**missing self**, [7.15.5](/7.15.5)) and secrete IFN-γ to activate macrophages.

Virus-specific CTLs do not appear in large numbers until days 6–8 ([7.15.18](/7.15.18)). The task of interferons and NK cells is to hold down viral replication during this gap and so buy time for adaptive immunity. People who lack NK cells (for example, with GATA2 or MCM4 deficiency) suffer repeated severe herpesvirus infections, and people with autoantibodies against type I interferons or defects in the type I interferon pathway may develop severe viral pneumonia.

## 7.5. Phases of Innate Immunity and the Transition to Adaptive Immunity

### 7.5.1. Three Phases

| Phase | Time | Components involved | Outcome |
|---|---|---|---|
| Immediate innate response | 0–4 h | Barriers, antimicrobial peptides, preexisting complement (alternative and lectin pathways), resident macrophages, the earliest recruited neutrophils | Most infections end here |
| Early induced innate response | 4–96 h | Proinflammatory cytokines, acute-phase proteins, recruited neutrophils and monocytes, NK cells, **innate lymphoid cells**, **γδ T cells**, **NKT cells**, natural IgM produced by B-1 cells | Infection is controlled or contained; cytokines that determine the type of the subsequent response are produced |
| Initiation of the adaptive response | After about 96 h | Mature dendritic cells that have migrated to the lymph node activate naive T cells | Clonal expansion; effector T cells and antibodies appear after days 5–7 |

### 7.5.2. Migration and Maturation of Dendritic Cells

Immature **dendritic cells** in tissues are specialized for taking up antigen. When their pattern recognition receptors are activated, the cell enters a "maturation" program: it downregulates uptake, upregulates MHC molecules and the **costimulatory molecules** CD80/CD86, expresses the chemokine receptor CCR7, and migrates along lymphatic vessels to the T-cell zone of the lymph node (guided by the chemokines CCL19 and CCL21). On arrival it displays antigenic peptide–MHC complexes on its surface (signal 1), provides costimulation through CD80/CD86 (signal 2), and tells the naive T cell what kind of pathogen is present through the cytokines it secretes (signal 3, for example IL-12 or IL-6). Innate immunity is therefore more than a "first line of defense": it decides whether an adaptive response occurs and of what type. Dendritic cells activated by PAMPs elicit type 1 or type 3 responses, whereas immature dendritic cells that carry only self antigens, in the absence of PAMPs, tend to induce tolerance. Antigen presentation and T-cell activation are treated in detail in [7.15.14](/7.15.14) and [7.15.16](/7.15.16); adjuvants exploit exactly this principle to enhance the immunogenicity of vaccines ([7.15.8](/7.15.8)).

### 7.5.3. Innate and Adaptive Immune Responses Compared

| | Innate immune response | Adaptive immune response |
|---|---|---|
| Main cells | Epithelial cells, phagocytes, dendritic cells, NK cells, innate lymphoid cells, γδ T cells, NKT cells, B-1 cells | αβ T cells, B-2 cells |
| Main molecules | Complement, acute-phase proteins, cytokines, antimicrobial peptides | Antibodies, cytokines |
| Recognition receptors | Germline-encoded pattern recognition receptors of limited variety | Antigen receptors produced by somatic rearrangement, with enormous diversity ([7.15.12](/7.15.12)) |
| What is recognized | Conserved molecular structures shared by a class of microbes | A specific epitope (antibodies) or antigenic peptide–MHC complex (T cells) |
| Onset | Minutes to hours; no clonal expansion | Days; requires clonal expansion and differentiation |
| Memory | No classical immunological memory (but trained immunity, §7.6.3) | Yes |

### 7.5.4. A Model: The Race Between Pathogen and Innate Effector Cells

The success of innate immunity depends on timing: does the pathogen grow to an uncontrollable number before effector cells are recruited? The simplest model writes the pathogen load $B$ and the number of local phagocytes $N$ as

$$
\frac{\mathrm{d}B}{\mathrm{d}t} = rB\left(1 - \frac{B}{K}\right) - kNB,\qquad
\frac{\mathrm{d}N}{\mathrm{d}t} = s + \frac{aB}{h + B} - \delta N - \gamma NB .
\tag{7.1}
$$

Here $r$ is the pathogen growth rate, $K$ the maximum load the tissue can carry, and $k$ the killing rate per phagocyte. The term $s$ is the basal replenishment of resident phagocytes, $aB/(h+B)$ is saturable recruitment driven by pathogen signals, $\delta$ is phagocyte death and departure, and $\gamma NB$ represents phagocytes consumed in combat with the pathogen (neutrophils die soon after phagocytosis, and many bacteria also secrete leukocyte-killing toxins). In the absence of pathogen, $N^* = s/\delta$, so the net growth rate of the pathogen early in an invasion is $r - ks/\delta$. When resident cells are numerous enough ($ks/\delta > r$), the pathogen-free state is stable and small inocula are cleared.

Stability does not mean that every inoculum can be cleared. The consumption term $\gamma NB$ gives the model threshold behavior: with a small inoculum, the pathogen is killed before it exhausts the local phagocytes; with an inoculum above the threshold, the pathogen consumes phagocytes faster than they are replenished and recruited, and the system falls into a second stable "infected state." This corresponds to the clinical notion of an "infectious dose." If both resident cells and recruitment are reduced (neutropenia after chemotherapy), $ks/\delta$ falls below $r$, the pathogen-free state loses stability, and even an otherwise harmless inoculum can establish infection; any factor that delays recruitment (such as an adhesion-molecule defect, [7.15.4](/7.15.4)) has a similar effect. The parameters in the model are illustrative values used only to show the qualitative behavior. The tools for analyzing planar systems of this kind (equilibria, nullclines, stability) are in [2.4.11](/2.4.11), and similar models in biology are in [7.9.14](/7.9.14).

![A model of the race between pathogen and innate effector cells (Eq. (7.1), nondimensionalized: $r = K = k = 1$, $\delta = 0.2$, $s = 0.3$, $a = 0.3$, $h = 0.1$, $\gamma = 6$, all illustrative values). A: Pathogen load over time for different inocula $B_0$ (log scale). Inocula below the threshold are cleared, and those above it fall into the infected state; the dashed line is the trajectory of the smallest inoculum when both resident replenishment $s$ and recruitment $a$ are halved (neutropenia), where $ks/\delta < r$ and even it establishes infection. B: Phase plane for normal parameters. The pathogen-free state (left, $N = s/\delta$) and the infected state (lower right) are two stable equilibria, and the stable manifold of the saddle between them (gray dashed line) divides the initial conditions into two basins of attraction; the colored curves are the trajectories in A](./plots/innate-race.py)

## 7.6. Resolution and Dysregulation of Inflammation

### 7.6.1. Resolution Is an Active Process

Inflammation does not end automatically once the pathogen has been cleared; resolution requires active signals. As the stimulus fades, recruited neutrophils undergo apoptosis and macrophages engulf the apoptotic cells (efferocytosis); this engulfment itself shifts the macrophage toward a reparative phenotype that secretes IL-10 and TGF-β. Arachidonic acid metabolism switches from prostaglandins and leukotrienes to lipoxins, and ω-3 fatty acids give rise to resolvins and protectins, which stop neutrophil recruitment and promote efferocytosis. Glucocorticoids (produced when IL-1 and IL-6 activate the hypothalamic–pituitary–adrenal axis) provide systemic negative feedback. Finally, fibroblasts and new blood vessels repair the tissue.

### 7.6.2. Uncontrolled Inflammation

If inflammation is stronger than necessary, or cannot resolve, its effectors themselves become the disease:

- Systemic dysregulation. Sepsis is life-threatening organ dysfunction caused by a dysregulated host response to infection. Large amounts of TNF-α, IL-1β and IL-6 enter the circulation, causing systemic vasodilation, increased permeability and widespread activation of coagulation, which appear as hypotension, disseminated intravascular coagulation and multiple organ failure; early hyperinflammation is often followed by immunoparalysis. Massive noninfectious cytokine release is called a **cytokine storm** ([7.15.11](/7.15.11)).
- Local dysregulation. A persistent stimulus (a pathogen that cannot be cleared, a foreign body, a self antigen) turns acute inflammation into **chronic inflammation**, characterized by infiltration of macrophages and lymphocytes and by tissue fibrosis, and may form **granulomas** ([7.15.27](/7.15.27)).
- Sterile inflammation. Uric acid, cholesterol crystals, or asbestos and silica particles activate the NLRP3 inflammasome, causing gout, the inflammatory component of atherosclerosis, and pneumoconiosis.

### 7.6.3. Trained Immunity

The classical view held that innate immunity has no memory. But after exposure to certain stimuli (BCG, fungal β-glucan), monocytes and macrophages can mount a stronger cytokine response to an unrelated stimulus weeks to months later; this is **trained immunity**. It is based not on clonal selection of antigen receptors but on reprogramming at the level of **epigenetics** and metabolism: histone modifications such as H3K4me3 on the promoters of inflammatory genes are retained, and glycolysis is enhanced; reprogramming of hematopoietic progenitors in the bone marrow lets the effect persist into their short-lived monocyte progeny. Trained immunity is thought to be one explanation for the nonspecific protection that BCG vaccination gives against infections other than tuberculosis. It differs from the memory of adaptive immunity in specificity, duration and mechanism.

## Summary

| Step | Key events | Key molecules |
|---|---|---|
| Alarm (§7.1.1) | Sentinel cells recognize PAMPs and DAMPs | Histamine, prostaglandins, leukotrienes, TNF-α, IL-1β, IL-6, chemokines |
| Vascular response and recruitment (§7.1.2) | Vasodilation, increased permeability, leukocyte emigration; neutrophils before monocytes | Selectins, integrin ligands, CXCL8, CCL2, C5a |
| Systemic response (§7.2) | Fever; acute-phase response | PGE2; CRP (Definition 7.2.2), SAA, MBL, hepcidin |
| Phagocytosis and killing (§7.3) | Opsonization (Definition 7.3.1); phagolysosome (Definition 7.3.2); respiratory burst (Definition 7.3.3) and reactive nitrogen species; NETs (Definition 7.3.4); pyroptosis and autophagy | NOX2, MPO, iNOS, defensins, PAD4, gasdermin D |
| Antiviral defense (§7.4) | Type I interferons precede NK cells, and both precede CTLs | IFN-α/β, IL-12, IL-15 |
| Transition (§7.5) | Three phases: 0–4 h, 4–96 h, after 96 h; dendritic cells mature and migrate, providing signals 1, 2 and 3 | MHC, CD80/CD86, CCR7 |
| Resolution and dysregulation (§7.6) | Efferocytosis, lipoxins and resolvins, glucocorticoids; sepsis, chronic inflammation; trained immunity | IL-10, TGF-β |

The model of Eq. (7.1) shows that the success of innate immunity depends on a race between pathogen growth and effector-cell replenishment, with a threshold inoculum; a reduction in effector cells can destabilize the pathogen-free state.

## Questions

1. Why can CRP rise a thousandfold within two days of a severe bacterial infection while IgG antibody barely changes in the same time? What is the fundamental difference in how the two recognize pathogens?

   **Answer** CRP is a germline-encoded acute-phase protein; under the action of IL-6, hepatocytes transcribe and translate it in large amounts within hours, with no need for clonal expansion. The phosphocholine it recognizes is a structure shared by many bacteria and by apoptotic cells, so its specificity is low and it appears quickly. Specific IgG must wait until the few B cells that recognize epitopes of the pathogen have been activated and have undergone clonal expansion and class switching; in a primary response it usually takes 1–2 weeks to rise appreciably. The former is the "pattern recognition" of innate immunity, the latter the "clonal selection" of adaptive immunity.

2. Patients with chronic granulomatous disease are not especially susceptible to catalase-negative streptococci but are highly susceptible to catalase-positive *Staphylococcus aureus* and *Aspergillus*. Explain.

   **Answer** The patients have a defective NADPH oxidase, so their phagocytes cannot themselves produce superoxide and $\ce{H2O2}$. Catalase-negative bacteria produce and accumulate $\ce{H2O2}$ in their own metabolism; once in the phagosome it can be used by myeloperoxidase to make HOCl, so the pathogen in effect "brings its own" killing material. Catalase-positive microbes break down their own $\ce{H2O2}$, leaving the phagocyte with no oxidative killing at all and only oxygen-independent mechanisms, which are not enough to kill them.

3. In Eq. (7.1), find the condition for the pathogen-free equilibrium $(0, s/\delta)$ to be stable and explain its biological meaning. When this condition holds, why can a large inoculum still establish infection?

   **Answer** Linearizing at $(0, s/\delta)$, the Jacobian is upper triangular, with eigenvalue $r - ks/\delta$ in the $B$ direction and $-\delta$ in the $N$ direction. The condition for stability is therefore $ks/\delta > r$: the steady-state number of resident phagocytes times the killing rate of a single cell exceeds the growth rate of the pathogen. This is only local stability. With a large inoculum, the consumption term $\gamma NB$ makes the phagocyte number fall rapidly, $kN$ drops below $r(1 - B/K)$, and the pathogen instead grows faster; the system enters the other stable equilibrium (the infected state). The boundary between the two basins of attraction is the stable manifold of the saddle point, which corresponds to the threshold inoculum.

   *Hint: setting $\mathrm{d}B/\mathrm{d}t = 0$ gives $B = 0$ or $N = r(1 - B/K)/k$; substitute the latter into $\mathrm{d}N/\mathrm{d}t = 0$ to find the infected state.*
4. (Open question) Some people argue that "fever should always be suppressed with antipyretics." Comment on this view using the mechanisms of this chapter.

   **Answer** Key points: fever is a defensive response in which IL-1β, TNF-α and IL-6 actively raise the set point through PGE2. The higher body temperature inhibits replication of some pathogens and enhances lymphocyte proliferation and neutrophil function, so suppressing it routinely may weaken defense. But fever increases oxygen consumption and metabolic load, and is harmful in patients with poor cardiopulmonary function, in infants at risk of febrile seizures, and in hyperthermia (above about 41 °C). Whether to bring down a fever should therefore be decided by weighing comfort against risk rather than by suppressing it routinely; antipyretics (COX inhibitors) only lower the set point and do not treat the infection itself.
