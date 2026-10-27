---
title: Control of Proliferation, Growth and Cell Size
description: How the cells of a multicellular organism decide whether to divide; mitogens, growth factors and survival factors; the restriction point and the Rb–E2F bistable switch with a model; cell-cycle checkpoints, the DNA damage response through ATM, ATR, Chk1/2 and p53, and the digital pulses of p53 from the p53–Mdm2 feedback; coordinating growth and division; cell size homeostasis by sizers, timers and adders; contact inhibition, telomeres, oncogene-induced senescence and p53 as the guardian against excess proliferation.
---

A yeast cell divides whenever it has enough nutrients; the cells of an animal divide only when the body needs more cells. The size of an organ, and of the organism, is the product of how many cells it has and how large they are, so it is set by three processes, cell growth, cell division and cell death, each controlled by signals from other cells and by the internal state of the cell. This chapter connects the engine of [7.3.20](/7.3.20) to these controls. Mitogens act on the decision taken in G1, at the restriction point, through the Rb–E2F switch; checkpoints halt the cycle when the DNA is damaged or incompletely replicated, with p53 as the central integrator; growth and division are coordinated so that cells keep their size; and several layers of safeguards, from contact inhibition to oncogene-induced senescence, make sure that a cell that receives too much stimulation stops or dies rather than proliferating. The signaling pathways themselves (receptor tyrosine kinases, Ras–MAPK, PI3K–PKB, mTORC1, Hippo) are described in [7.1.15](/7.1.15), [7.3.18](/7.3.18) and [7.3.19](/7.3.19); apoptosis and senescence in [7.3.25](/7.3.25); the breakdown of all these controls in cancer in [7.3.26](/7.3.26).

## 22.1. Signals That Control Proliferation

### 22.1.1. Mitogens, Growth Factors and Survival Factors

**Definition 22.1.1 (Mitogen, Growth Factor and Survival Factor)** Extracellular signals that promote cell proliferation fall into three operational classes. A **mitogen** stimulates cell division, mainly by triggering a wave of G1/S-Cdk activity that relieves the intracellular brakes on cell-cycle entry. A **growth factor** (in the strict sense) stimulates cell growth, an increase in cell mass, by promoting the synthesis and inhibiting the degradation of proteins and other macromolecules. A **survival factor** promotes cell survival by suppressing apoptosis.

The distinction is functional: a single protein often has all three activities (PDGF, EGF and IGF-1 stimulate division, growth and survival), and the name "growth factor" is commonly applied to any of them. More than 50 mitogens are known. Most have a broad specificity (PDGF for fibroblasts, smooth muscle cells and glia; EGF for epithelial and many other cells); some are narrow (erythropoietin for red-cell precursors). Mitogens act mostly through **receptor tyrosine kinases** on the Ras–MAPK and PI3K–PKB pathways, whose effect on the cell-cycle machinery, two waves of gene expression culminating in cyclin D, is traced in [7.3.19](/7.3.19#sec-19.2.1).

Inhibitory signals oppose them. TGF-β arrests many epithelial cells in G1 by inducing the CKIs p15INK4b and p21 and repressing Myc ([7.3.19](/7.3.19#sec-19.4.1)); myostatin (GDF8), a TGF-β family member made by muscle, limits muscle growth, and cattle and dogs with inactivating mutations of its gene are "double-muscled". Signals that activate apoptosis (death ligands, [7.3.25](/7.3.25)) remove cells. Raff proposed (1992) that most animal cells depend on survival signals from other cells and die by default without them, a social control that matches cell numbers to the available supply of signals, as in the matching of developing neurons to their targets through limiting amounts of NGF.

### 22.1.2. Cells Can Enter a Nondividing State

Without mitogens a cell in G1 keeps its Cdk activity low by the three brakes of the stable G1 state ([7.3.20](/7.3.20#sec-20.3.7): APC/C–Cdh1, CKIs and low cyclin transcription) and may withdraw into G0 (Definition 20.1.2). Quiescence is an actively maintained program: quiescent fibroblasts keep transcribing genes that prevent differentiation and senescence, accumulate p27 and the Rb relative p130, and can re-enter the cycle within a day when mitogens return. The time from mitogen addition to S phase (about 12–16 h for a serum-starved fibroblast) is longer than the G1 of a cycling cell, because the cell must first rebuild its cell-cycle machinery. Almost all variation in cycle length in the adult body lies in G1 and G0.

## 22.2. G1 and the Restriction Point

### 22.2.1. A Point of No Return

**Definition 22.2.1 (Restriction Point and Start)** The **restriction point** is the point in late G1 of animal cells after which a cell is committed to complete S phase and the cycle without further mitogen stimulation; before it, withdrawal of mitogens or inhibition of protein synthesis returns the cell to G0. The corresponding commitment point of yeast cells, which depends on nutrients and cell size rather than mitogens, is **Start**.

Pardee (1974) defined the restriction point in fibroblasts by withdrawing serum at different times: cells deprived of serum early in G1 returned to quiescence, cells deprived later went on into S phase. Zetterberg and Larsson (1985), following single cells by time-lapse microscopy, found that it lies 3–4 hours after mitosis, after which serum withdrawal no longer stopped them, and that the variable part of G1 lies after it. Live-cell reporters of Cdk2 activity later showed that cells emerging from mitosis bifurcate: some keep a low, rising Cdk2 activity and continue into the next cycle directly, others drop to zero and enter a quiescent state from which they must be restarted by mitogens (Spencer et al. 2013). Mitogen and stress signals received in the previous cycle, as well as in G1, therefore influence the decision.

### 22.2.2. Rb and E2F

**Definition 22.2.2 (Rb Protein and E2F)** The **retinoblastoma protein** (Rb, pRb) is a tumor suppressor, with its relatives p107 and p130 (the pocket proteins), that binds and inhibits the **E2F** transcription factors and recruits histone deacetylases and other corepressors to their target promoters. E2F proteins (E2F1–3 as activators, E2F4–8 mostly as repressors), with their partners DP1 and DP2, control genes needed for S phase: cyclins E and A, Cdc25A, Cdc6, MCM proteins, DNA polymerase α, thymidine kinase, ribonucleotide reductase and the E2F genes themselves. Phosphorylation of Rb by cyclin–Cdk complexes releases E2F.

Rb was identified through retinoblastoma, the childhood eye tumor that requires the loss of both copies of *RB1* (Knudson's two hits, [7.1.15](/7.1.15#sec-15.6.2)). It has 14 or more Cdk sites. In current models, cyclin D–Cdk4/6 in early G1 puts a single phosphate on any one of these sites, which leaves Rb able to bind E2F; hyperphosphorylation of Rb, which releases E2F, is the work of cyclin E–Cdk2 at the restriction point (Narasimha et al. 2014). The circuit therefore contains three positive loops: E2F induces cyclin E, which phosphorylates more Rb; E2F induces its own genes; and cyclin E–Cdk2 inactivates the brakes that limit it (it phosphorylates p27, marking it for SCF–Skp2, and inactivates Cdh1, so that cyclin A can accumulate). Once the loops have been engaged the cell no longer needs cyclin D: Rb is held phosphorylated by Cdk2 and later by cyclin A– and cyclin B–Cdks until mitotic exit, when phosphatases reset it.

Cyclin D, the input to the switch, integrates many signals: its transcription depends on Ras–MAPK, AP-1, Myc, β-catenin and STATs; its translation on mTORC1; its stability on GSK3, which phosphorylates Thr286 and targets it for degradation by the ubiquitin ligase CRL4–AMBRA1; its activity is blocked by INK4 proteins and helped by Cip/Kip proteins as assembly factors. Cyclin D falls within an hour of mitogen withdrawal, which explains why cells before the restriction point need continuous stimulation. Overexpression or amplification of cyclin D1 or Cdk4, loss of p16INK4a and loss of Rb all bypass the restriction point, and at least one of them is found in most human cancers ([7.3.26](/7.3.26)); the Cdk4/6 inhibitors palbociclib, ribociclib and abemaciclib exploit this dependence in breast cancer.

### 22.2.3. The Rb–E2F Switch Is Bistable

The restriction point is the behavior expected of a bistable switch with hysteresis (Definitions 18.4.2 and 18.4.3 of [7.3.18](/7.3.18#sec-18.4.3)): the input needed to turn E2F on is larger than the input that keeps it on, so a transient mitogen signal can produce lasting commitment. Yao and colleagues (2008) tested this in rat fibroblasts with a destabilized GFP reporter driven by an E2F-responsive promoter, measured in single cells. Cells brought from quiescence to a given serum level had either E2F on or off, not intermediate values; the serum level needed to switch E2F on was several times higher than the level at which cells already on stayed on; and the dependence on history was abolished by mutations that broke the feedback loops. Their model has seven variables (figure below):

$$
\begin{aligned}
\frac{\mathrm{d}E}{\mathrm{d}t} &= k_{\mathrm{E}}\,f_{\mathrm{M}}f_{\mathrm{E}} + k_{\mathrm{b}}f_{\mathrm{M}} + \text{(release of E2F by phosphorylation of RE)} - d_{\mathrm{E}}E - k_{\mathrm{RE}}RE, \\
\frac{\mathrm{d}C_{\mathrm{E}}}{\mathrm{d}t} &= k_{\mathrm{CE}}\,f_{\mathrm{M}}f_{\mathrm{E}} - d_{\mathrm{CE}}C_{\mathrm{E}}, \qquad f_{\mathrm{M}} = \frac{M}{K_{\mathrm{M}} + M}, \quad f_{\mathrm{E}} = \frac{E}{K_{\mathrm{E}} + E},
\end{aligned}
\tag{22.1}
$$
with Myc $M$ and cyclin D–Cdk4/6 $C_{\mathrm{D}}$ driven by the serum level $S$, free and E2F-bound Rb ($R$ and $RE$) phosphorylated by $C_{\mathrm{D}}$ and the cyclin E–Cdk2 activity $C_{\mathrm{E}}$, and phosphorylated Rb dephosphorylated by a phosphatase. The feedback lies in the terms $f_{\mathrm{E}}$: E2F induces itself and cyclin E, and cyclin E releases more E2F. Because Rb binds E2F tightly ($k_{\mathrm{RE}}$ large), free E2F stays near zero until phosphorylation of Rb outpaces its synthesis, after which it jumps to a high level; this titration makes the response steep, and the positive loops make it bistable.

In the model, E2F switches on above a serum level of about 0.45 (in its arbitrary units) when the cells start from quiescence and switches off only below about 0.15 when they start from the on state. A pulse of high serum commits the cell only if it lasts long enough for E2F to pass the unstable intermediate state (about 21 h from deep quiescence in the model); after a shorter pulse the system falls back. The restriction point is thus not a molecular event but a threshold in the state space of a network: the moment at which the trajectory crosses the separatrix between the basins of the two stable states.

![The Rb–E2F bistable switch, model of Yao et al. (2008), Eq. (22.1). A: steady-state free E2F against the mitogen (serum) level, approached from quiescence with rising serum (blue) or from the E2F-on state with falling serum (red): over a range of serum levels both states are stable, and the response depends on history (hysteresis). B: quiescent cells given a high serum level (S = 5) for 12–26 h, after which serum is lowered to S = 0.2, inside the bistable range (dots mark the end of each pulse). Pulses of 20 h or less leave E2F to fall back; pulses that carry E2F past the unstable threshold commit the cells, and E2F stays on without further stimulation: the restriction point](./plots/rb-e2f-switch.py)

## 22.3. Checkpoints

### 22.3.1. Four Checkpoints

**Definition 22.3.1 (Cell-Cycle Checkpoint)** A **cell-cycle checkpoint** is a control mechanism that monitors the completion or the quality of a cell-cycle event, or the conditions inside and outside the cell, and blocks progression through a later transition until the event is complete or the problem is solved.

Every checkpoint has three parts: sensors that detect the problem (unattached kinetochores, DNA ends, single-stranded DNA), transducers that amplify and relay the signal (usually protein kinases such as ATM, ATR, Chk1, Chk2 and Mps1), and effectors that act on the cell-cycle machinery (Cdc25, p21, APC/C–Cdc20). Checkpoints act on the three transitions of the control system ([7.3.20](/7.3.20#sec-20.3.1)):

| Checkpoint | Monitors | Sensor and signal | Target | Effect |
|---|---|---|---|---|
| G1/S (restriction point, Start) | mitogens, nutrients, cell size, DNA damage | Rb–E2F; ATM/ATR–p53–p21 | G1/S-Cdk, S-Cdk | no entry into S |
| Intra-S (replication) | stalled forks, damage during replication | ATR–Chk1 | Cdc25A, origin firing | slows S, protects forks, blocks late origins |
| G2/M | unreplicated or damaged DNA, cell size | ATR–Chk1, ATM–Chk2; p53–p21, 14-3-3σ | Cdc25, M-Cdk | no entry into mitosis |
| Metaphase-to-anaphase (spindle assembly) | kinetochore attachment | Mad2 and MCC ([7.3.21](/7.3.21#sec-21.3.3)) | APC/C–Cdc20 | no anaphase |

Hartwell and Weinert, who introduced the idea (1989), emphasized that checkpoints are separate from the processes they monitor: mutants lacking a checkpoint (yeast *rad9*) divide normally in good conditions but die after DNA damage, because they enter mitosis with broken chromosomes. In this sense a checkpoint is a brake added to the engine, not part of it.

### 22.3.2. The DNA Damage Response

A human cell suffers tens of thousands of DNA lesions a day ([7.2.8](/7.2.8)) and at least tens of double-strand breaks. The DNA damage response detects breaks and replication problems, arrests the cycle, activates repair and, if the damage is too severe, triggers senescence or apoptosis.

**Definition 22.3.2 (ATM and ATR)** **ATM** (ataxia telangiectasia mutated) and **ATR** (ATM and Rad3-related) are large protein kinases of the PI3K-related kinase family that initiate the DNA damage response. ATM is activated by double-strand breaks, recruited by the MRN complex; ATR is activated by single-stranded DNA coated with RPA at resected breaks and stalled replication forks, recruited by ATRIP and activated by TopBP1. They phosphorylate hundreds of substrates on Ser/Thr–Gln motifs, among them histone H2A.X, the checkpoint kinases Chk2 (mainly by ATM) and Chk1 (by ATR), and p53.

Two arms of the response act on different time scales (figure below):

1. Fast arrest, within minutes, without new transcription. Chk1 and Chk2 phosphorylate Cdc25A, marking it for destruction by SCF–βTrCP, and phosphorylate Cdc25C on Ser216, which creates a binding site for 14-3-3 proteins that hold it in the cytoplasm. Both kinases act on Cdc25 and on p53: ATM acts mainly through Chk2 and ATR through Chk1, and the scheme of some textbooks in which ATM activates Chk1 toward Cdc25 and Chk2 toward p53 is a simplification. Cdk2 and Cdk1 remain phosphorylated on Tyr15 and the cell stops in G1, S or G2.
2. Sustained arrest, over hours, through p53.

**Definition 22.3.3 (p53, Mdm2 and p21)** **p53** is a tetrameric transcription factor, encoded by the tumor suppressor gene *TP53*, that is activated by DNA damage and other stresses and induces genes for cell-cycle arrest, DNA repair, senescence and apoptosis. In unstressed cells it is kept at low levels by **Mdm2** (HDM2 in humans), a RING ubiquitin ligase that binds the transactivation domain of p53, blocks it and marks it for proteasomal destruction (half-life about 20 minutes); *MDM2* is itself a p53 target gene. **p21** (p21Cip1/Waf1), the first p53 target identified, is a Cip/Kip CKI that inhibits cyclin E– and cyclin A–Cdk2 (and, with 14-3-3σ and other targets, cyclin B–Cdk1), arresting the cell in G1 or G2.

Phosphorylation of p53 near its Mdm2-binding site (Ser15 by ATM and ATR, Ser20 by Chk1 and Chk2) and of Mdm2 itself by ATM weakens their interaction, so p53 escapes degradation, accumulates within an hour and is acetylated by p300/CBP, which increases its binding to DNA. The evidence that Mdm2 exists to restrain p53 is genetic: mice lacking *Mdm2* die as early embryos, and mice lacking both *Mdm2* and *Trp53* are viable (Jones et al. 1995; Montes de Oca Luna et al. 1995). p53 responds to many other stresses besides DNA damage: oncogenic signaling (22.5.3), hypoxia, nucleotide depletion and disruption of ribosome biogenesis, in which free ribosomal proteins RPL5 and RPL11 with 5S rRNA bind and inhibit Mdm2 (**nucleolar stress**, Definition 17.8.3 of [7.3.17](/7.3.17#sec-17.8.2)).

Severe or persistent damage turns the arrest into an exit: p53 then induces the BH3-only proteins Puma and Noxa and other mediators of apoptosis ([7.3.25](/7.3.25)), or a permanent arrest (senescence). Single-celled organisms do otherwise: a budding yeast cell that cannot repair a break eventually adapts to the checkpoint and resumes division with the damage. For a unicellular organism, life with a mutation is better than no life; for a metazoan, a dead cell is better than a cancer cell. *TP53* is mutated in about half of all human cancers, mostly by missense mutations in its DNA-binding domain, and people who inherit one mutant copy (Li–Fraumeni syndrome) develop multiple cancers early; ataxia telangiectasia, caused by loss of ATM, combines neurodegeneration (cerebellar ataxia), dilated blood vessels of the eye and skin (telangiectasia), immunodeficiency, extreme sensitivity to ionizing radiation and a high risk of lymphoma and leukemia. Cells from patients fail to arrest after irradiation and go on replicating damaged DNA (radioresistant DNA synthesis). Heterozygous carriers, about 0.5–1% of the population, are healthy but have an increased risk of breast cancer.

![The p53 hub of the DNA damage response (SBGN activity flow; open arrows activate, bars inhibit). DNA double-strand breaks, including unprotected telomeres, activate ATM and Chk2; stalled replication forks activate ATR and Chk1. The checkpoint kinases inhibit Cdc25A and Cdc25C, so that Cdk2 and Cdk1 remain inhibited (rapid arrest), and stabilize p53. Oncogenic signals induce ARF, and ribosomal proteins RPL5 and RPL11 released by nucleolar stress bind Mdm2; both inhibit Mdm2, the ubiquitin ligase that keeps p53 low, while p53 induces Mdm2 (negative feedback). p53 induces p21, which inhibits Cdk2 and Cdk1 (sustained arrest), and the pro-apoptotic Puma and Noxa; the outcome is arrest and repair, senescence or apoptosis](./plots/checkpoint-network.py)

### 22.3.3. p53 Pulses

The p53–Mdm2 pair is a negative feedback loop with a delay: p53 induces Mdm2, which takes about an hour to be transcribed, translated and imported, and Mdm2 then destroys p53. Such a loop can oscillate (compare the delayed feedback of [7.3.18](/7.3.18#sec-18.4.5)). Lahav and colleagues (2004) imaged fluorescently tagged p53 and Mdm2 in single human cells after γ-irradiation. Population averages, as in Western blots, had shown a single damped wave; single cells instead showed a series of pulses of p53 with a nearly fixed amplitude and duration, about 5.5 hours apart, and a higher dose increased the fraction of cells that pulsed and the number of pulses, not their height: a digital response. The pulses persist because the upstream kinase also pulses: p53 induces the phosphatase Wip1, which dephosphorylates and inactivates ATM and Chk2, so that ATM activity falls after each pulse and is re-activated while breaks persist (Batchelor et al. 2008). The dynamics carry information: when p53 is forced to stay high instead of pulsing, cells enter senescence, whereas pulses allow them to recover (Purvis et al. 2012).

A delay model reproduces these features. Let $D$ be the number of unrepaired breaks (each repaired at random at rate $0.1\,\mathrm{h^{-1}}$), $A$ the activity of ATM, $P$ p53, $M$ Mdm2 and $W$ Wip1:

$$
\begin{aligned}
\frac{\mathrm{d}A}{\mathrm{d}t} &= g(D)\left(k_{\mathrm{a}} + k_{\mathrm{au}}\frac{A^2}{K_{\mathrm{a}}^2 + A^2}\right)(1 - A) - k_{\mathrm{w}}\frac{WA}{0.1 + A}, \qquad g(D) = \frac{D}{D + 8}, \\
\frac{\mathrm{d}P}{\mathrm{d}t} &= \beta_{\mathrm{p}} - \left(\alpha_{\mathrm{m}}M\,(1 - 0.9A) + \alpha_{\mathrm{p}}\right)P, \\
\frac{\mathrm{d}M}{\mathrm{d}t} &= \beta_{\mathrm{m}}P(t - \tau_1) - \delta_{\mathrm{m}}M, \qquad \frac{\mathrm{d}W}{\mathrm{d}t} = \beta_{\mathrm{w}}\frac{P(t - \tau_2)^4}{K_{\mathrm{w}}^4 + P(t - \tau_2)^4} - \delta_{\mathrm{w}}W,
\end{aligned}
\tag{22.2}
$$
with delays $\tau_1 = 0.8\,\mathrm{h}$ (Mdm2) and $\tau_2 = 1.5\,\mathrm{h}$ (Wip1). ATM protects p53 from Mdm2 (the factor $1 - 0.9A$), and positive feedback (autophosphorylation) makes ATM activation switchlike. Each pulse of ATM releases a pulse of p53, which induces Mdm2 (ending the p53 pulse) and Wip1 (ending the ATM pulse); as long as breaks remain, ATM fires again. The number of pulses therefore measures how long the damage persists, and so, on average, how much damage there was.

![Digital pulses of p53, delay model Eq. (22.2). A: p53 in single simulated cells after damage that creates 5 (blue) or 40 (red) double-strand breaks; dotted steps show the unrepaired breaks (right axis). p53 rises in pulses about 6 h apart, of similar height whatever the dose; more damage gives more pulses, and the pulses stop when the breaks are repaired. B: number of p53 pulses in 40 simulated cells per dose (mean and range) rises with the number of breaks. C: the average over 100 cells after 20 breaks (red) looks like a damped oscillation, although single cells (grey) pulse with undamped amplitude and different timing: averaging over a population hides the single-cell dynamics](./plots/p53-pulses.py)

## 22.4. Coordinating Growth and Division

### 22.4.1. Growth and Division Can Be Coupled or Uncoupled

**Definition 22.4.1 (Cell Growth)** **Cell growth** is the increase in the mass (or volume) of a cell, by synthesis of proteins, lipids, nucleic acids and other components in excess of their degradation and by uptake of water and solutes; it is distinct from cell proliferation, the increase in cell number.

If cells divided without growing they would get smaller with each cycle; if they grew without dividing they would get larger. Proliferating cells keep their size by coupling the two, but the coupling is not obligatory:

- Neurons and skeletal muscle fibers grow enormously after they have stopped dividing: the size of a sympathetic neuron depends on the amount of NGF it receives from its targets, and muscle fibers grow by fusion and hypertrophy.
- Oocytes grow for months to a diameter of 0.1–1 mm without dividing; after fertilization, the cleavage divisions divide them without growth.
- In the *Drosophila* wing, cells with a mutation that speeds the cycle without speeding growth become smaller but the compartment keeps its size; cells with more Myc grow faster and outcompete their neighbors (cell competition), which are eliminated by apoptosis.

Growth is controlled by mTORC1, which integrates growth factors (through PI3K–PKB), amino acids, energy (AMPK) and oxygen ([7.3.18](/7.3.18#sec-18.6.2)). mTORC1 promotes translation (through S6 kinase and 4E-BP), ribosome biogenesis, lipid and nucleotide synthesis, and inhibits autophagy ([7.3.11](/7.3.11)). Ribosomes are the main product of a growing cell: a mammalian cell makes several thousand ribosomes per minute, and the growth rate of a cell is proportional to the fraction of its proteome invested in active ribosomes ([7.2.19](/7.2.19#sec-19.8.5)). Myc couples the two programs: it induces both the genes for ribosome biogenesis and those of the cell-cycle machinery. Many growth factors also induce cyclin D, so in most animal cells the same signals drive both growth and division, but with separate inputs (growth factors acting on mTORC1, mitogens on cyclin D) that let cell size depend on their ratio.

### 22.4.2. Cell Size Homeostasis

Within one cell type, cell size is remarkably uniform: the coefficient of variation of volume at birth is typically about 0.1–0.2. Since growth is roughly exponential (a large cell grows faster than a small one), this uniformity cannot arise passively; a deviation must be corrected.

**Definition 22.4.2 (Sizer, Timer and Adder)** **Cell size homeostasis** is the maintenance of a narrow distribution of cell sizes in a proliferating population by coupling division to growth. In a **sizer**, cells divide (or pass a cell-cycle transition) when they reach a set size, regardless of their size at birth; in a **timer**, they divide a set time after birth; in an **adder**, they divide after adding a set volume (or mass) since birth.

The three rules are special cases of the linear relation between the volume at division $V_{\mathrm{d}}$ and at birth $V_{\mathrm{b}}$,

$$
V_{\mathrm{d}} = a V_{\mathrm{b}} + b,
\tag{22.3}
$$
with $a = 0$ (sizer), $a = 1$ (adder) and, for exponential growth, $a = 2$ (timer). They are distinguished experimentally by the slope $a - 1$ of the added volume $V_{\mathrm{d}} - V_{\mathrm{b}}$ against $V_{\mathrm{b}}$, measured in single cells followed through divisions.

**Proposition 22.4.1 (Correction of Size Deviations)** Suppose cells obey Eq. (22.3) with $0 \le a < 2$ and divide exactly in half. Then the birth volume converges to $V^* = b/(2 - a)$, and a deviation $\delta_n = V_{\mathrm{b},n} - V^*$ in generation $n$ becomes $\delta_{n+1} = (a/2)\,\delta_n$ in the next. A sizer removes a deviation in one generation, an adder halves it in each generation, and a timer ($a = 2$) does not correct it at all.

**Proof** The daughter's birth volume is $V_{\mathrm{b},n+1} = V_{\mathrm{d},n}/2 = (aV_{\mathrm{b},n} + b)/2$. Its fixed point satisfies $V^* = (aV^* + b)/2$, so $V^* = b/(2 - a)$. Subtracting, $\delta_{n+1} = (a/2)\,\delta_n$, which tends to zero for $0 \le a < 2$; for $a = 2$, $b = 0$ and every birth volume is a fixed point. $\square$

With noise in the division rule, the variance of birth size is stationary for $a < 2$ and grows without bound for a timer, as in a random walk (figure below): a pure timer cannot maintain size, so cells need some form of size sensing. Single-cell measurements in microfluidic devices showed that *Escherichia coli*, *Bacillus subtilis*, *Caulobacter* and the daughter cells of budding yeast behave as adders over a wide range of growth conditions (Campos et al. 2014; Taheri-Araghi et al. 2015). Fission yeast is closer to a sizer, and many mammalian cell lines are adder-like overall, with a sizer-like correction in G1. An adder is the expected behavior when a protein needed for division accumulates at a rate proportional to growth from birth and division occurs when its number reaches a threshold, then is reset.

How cells measure size is still debated, and the proposed mechanisms convert a size into a concentration:

- Dilution of an inhibitor. In budding yeast the G1 inhibitor Whi5, an Rb analog that represses SBF, is made mostly in S and G2 and partitioned to daughters in amounts independent of their size; as a small daughter grows, Whi5 is diluted until its concentration falls below a threshold and Start occurs (Schmoller et al. 2015). In human cells Rb itself is diluted as cells grow in G1, and its concentration correlates with the probability of entering S (Zatulovskiy et al. 2020). Later measurements showed that dilution explains only part of size control in yeast, and that the activators (Cln3) and their nuclear concentrations matter too.
- Accumulation of an activator scaled to size. In fission yeast the mitotic inducer Cdc25 and cyclin B (Cdc13) accumulate in the nucleus in proportion to cell size, so Cdk1 activation is reached at a set size (Facchetti et al. 2019); the kinase Pom1, concentrated at the cell tips and forming a gradient toward the middle, inhibits the Cdk1 activator Cdr2 in cortical nodes in small cells (Martin and Berthelot-Grosjean 2009; Moseley et al. 2009), and Cdr2 nodes report cell surface area (Pan et al. 2014).
- Growth rate feedback. In mammalian cells, small cells extend G1 and large cells grow more slowly, through p38 MAPK and mTORC1, so both division timing and growth rate contribute to homeostasis.

![Sizer, adder and timer, Eq. (22.3), in simulations with exponential growth, noisy division rules and slightly unequal division (daughters receive 0.5 ± 0.03 of the mother's volume). A: added volume against volume at birth for 600 cells of each rule (units of the mean birth volume); the slope is −1 for a sizer, 0 for an adder and +1 for a timer. B: correction of a size deviation at birth over generations, the factor a/2 per generation (Proposition 22.4.1): a sizer corrects it in one generation, an adder halves it each generation, a timer keeps it. C: the coefficient of variation of birth volume in 200 lineages over 60 generations: sizer and adder keep it constant, whereas under a pure timer the noise accumulates and the distribution spreads without limit](./plots/size-control.py)

### 22.4.3. From Cells to Organs

Organ size is regulated beyond the size of single cells. A mouse liver regenerates to its original mass after two thirds has been removed, and stops; a *Drosophila* wing reaches the same size whether it is made of fewer large cells or more small ones. The signals that sense the size of a whole tissue include morphogen gradients (Dpp in the fly wing, [7.5](/7.5)), mechanical tension and cell density, read in large part by the Hippo pathway and its effectors YAP and TAZ ([7.3.19](/7.3.19#sec-19.4.2)): mutations in the Hippo kinases cause massive overgrowth of fly imaginal discs, and activated YAP enlarges the mouse liver several-fold. How these signals are integrated into a stopping rule for organ growth remains largely unknown.

## 22.5. Preventing Excessive Proliferation

### 22.5.1. Contact Inhibition

**Definition 22.5.1 (Contact Inhibition)** **Contact inhibition** of proliferation is the arrest of division of normal cells in culture when they become confluent and touch their neighbors, even in the presence of mitogens, so that they form a monolayer; it is distinct from contact inhibition of locomotion, the stopping of movement on contact.

Crowding acts through cadherin-based junctions ([7.3.23](/7.3.23)), the Hippo pathway (high density and low tension keep YAP and TAZ phosphorylated and cytoplasmic), reduced cell spreading, and the induction of p27; it also lowers the response of cells to mitogens, partly because the area of membrane per cell, and so the number of receptors exposed, falls. Loss of contact inhibition, the formation of multilayered foci, was the first assay for cell transformation by oncogenes ([7.3.26](/7.3.26)).

### 22.5.2. Telomeres as a Built-In Limit

Normal human fibroblasts divide only 25–60 times in culture before they stop permanently (Hayflick and Moorhead 1961), because most human somatic cells lack enough **telomerase** and their **telomeres** shorten with each division ([7.2.7](/7.2.7#sec-7.6.3)). When some telomeres become too short to be protected by shelterin, they are recognized as double-strand breaks and activate ATM–p53–p21 and p16–Rb: the cells enter replicative senescence. Mouse cells, which express telomerase and have long telomeres, lack this limit, and expression of telomerase reverse transcriptase in human fibroblasts makes them divide indefinitely. Replicative senescence is thus a mechanism that counts divisions through the DNA damage response; its role in tumor suppression and aging is discussed in [7.3.25](/7.3.25).

### 22.5.3. Too Much Mitogenic Signaling Stops Cells

**Definition 22.5.2 (Oncogene-Induced Senescence)** **Oncogene-induced senescence** is a stable proliferative arrest triggered in normal cells by the expression of an activated oncogene, such as mutant Ras, BRAF or excess Myc, mediated by the p16–Rb and ARF–p53 pathways and by the DNA damage response to replication stress caused by the oncogene.

The paradox that a growth-promoting oncogene can stop growth was found when activated Ras was expressed in normal human and rodent fibroblasts: instead of transforming them, it arrested them permanently with features of senescence (Serrano et al. 1997). Two mechanisms act. Excessive E2F and Myc activity induce ARF (p14ARF in humans, p19Arf in mice), the second product of the *CDKN2A* locus that also encodes p16INK4a, read in an alternative reading frame; ARF binds Mdm2 and sequesters it in the nucleolus, so p53 is stabilized. And oncogene-driven over-firing of replication origins causes fork collapse and DNA breaks, activating ATM and ATR. If the signal is strong enough, as with high Myc in the absence of survival signals, the cell dies by apoptosis instead. Benign human nevi (moles), which carry activating *BRAF* mutations yet stop growing, are made of senescent melanocytes. Tumors must therefore inactivate these safeguards, which is why mutations in *TP53*, *CDKN2A* or the components between them are so common in cancer.

### 22.5.4. p53 at the Center

The controls of this chapter converge on two hubs (figure in 22.3.2): Rb, which integrates mitogenic signals at the restriction point, and p53, which integrates stresses (DNA damage, telomere erosion, oncogenic signaling, nucleolar stress, hypoxia). Together they form the "two pathways" whose inactivation is almost universal in human cancer, either directly or through their regulators (cyclin D, Cdk4, p16, Mdm2, ARF), and tumor viruses attack both: the E7 protein of human papillomavirus binds Rb, and E6 targets p53 for degradation ([7.3.26](/7.3.26)). In a systems view, a cell in a tissue proliferates only when positive signals pass a bistable threshold (Rb–E2F) and no stress sensor (p53) vetoes the decision; each control has a backup, and only a cell that has lost several of them escapes the social control of proliferation.

## Summary

| Topic | Key points |
|---|---|
| Extracellular signals (Definition 22.1.1) | mitogens (division), growth factors (growth), survival factors (survival); TGF-β, myostatin inhibit; survival depends on signals from other cells |
| Restriction point (Definition 22.2.1) | late G1 commitment, mitogen-independent afterwards; Start in yeast; Cdk2 bifurcation after mitosis |
| Rb–E2F (Definition 22.2.2) | cyclin D–Cdk4/6 starts, cyclin E–Cdk2 completes Rb phosphorylation; E2F induces cyclin E and itself; bistable switch with hysteresis, Eq. (22.1) |
| Checkpoints (Definition 22.3.1) | G1/S, intra-S, G2/M, spindle assembly; separate from the events they monitor |
| DNA damage response (Definitions 22.3.2, 22.3.3) | ATM–Chk2 (breaks), ATR–Chk1 (forks, ssDNA); fast arrest via Cdc25 inhibition; sustained arrest via p53–p21; Mdm2 keeps p53 low; apoptosis or senescence if severe |
| p53 dynamics | delayed negative feedback with Mdm2 and Wip1 gives digital pulses; dose sets pulse number, Eq. (22.2) |
| Growth (Definition 22.4.1) | mTORC1, ribosome biogenesis, Myc; can be uncoupled from division (neurons, oocytes, cleavage) |
| Size homeostasis (Definition 22.4.2) | $V_{\mathrm{d}} = aV_{\mathrm{b}} + b$, Eq. (22.3): sizer $a = 0$, adder $a = 1$, timer $a = 2$; deviations shrink by $a/2$ per generation (Proposition 22.4.1); bacteria and yeast daughters behave as adders; inhibitor dilution and activator accumulation; organ size via Hippo–YAP |
| Safeguards | contact inhibition (Definition 22.5.1); telomere-limited replicative senescence; oncogene-induced senescence via ARF–p53 and p16–Rb (Definition 22.5.2); Rb and p53 as the two hubs |

## Questions

1. Fibroblasts are serum-starved, then given serum. Serum is removed at 2, 6, 10 and 14 h; only cells from which it was removed at 14 h or later replicate their DNA. Where is the restriction point, and which molecular event does it correspond to? How would adding a Cdk4/6 inhibitor at 16 h, or a Cdk2 inhibitor at 16 h, affect S-phase entry?

   **Answer** The restriction point lies between 10 and 14 h after serum addition: before it cyclin D–Cdk4/6 activity depends on continuous mitogen signaling, after it the Rb–E2F loop (E2F → cyclin E–Cdk2 → Rb hyperphosphorylation) sustains itself. A Cdk4/6 inhibitor added after the restriction point has little effect, because Rb is held phosphorylated by cyclin E–Cdk2 and E2F is already on. A Cdk2 inhibitor at that time may still delay or block entry in many cells, because the positive loop through cyclin E–Cdk2 is what maintains commitment; in the model, removing it moves the system back toward the off state.

2. Using Proposition 22.4.1, show that for an adder the mean birth size is $b$ (the added volume). A mutant bacterium adds 20% more volume per cycle than the wild type at the same growth rate. What happens to its steady-state size, and how many generations does it take to get within 10% of the new size after the switch?

   **Answer** With $a = 1$, $V^* = b/(2 - 1) = b$. If $b$ increases by 20%, the new birth size is $1.2b$. The deviation from the new steady state halves each generation: starting at $-0.2b$ (−16.7% of the new size), after one generation it is −8.3%, so one generation suffices to come within 10%, and after four generations the deviation is about 1%.

3. Why does a pure timer fail to maintain cell size when growth is exponential, whereas it would work if growth were linear (constant rate independent of size)?

   **Answer** With exponential growth $V_{\mathrm{d}} = V_{\mathrm{b}}\mathrm{e}^{\lambda T}$; with $\lambda T = \ln 2$ every birth volume is reproduced exactly, so deviations are never corrected and noise accumulates as a random walk in $\ln V$. With linear growth $V_{\mathrm{d}} = V_{\mathrm{b}} + kT$, a fixed time adds a fixed volume, so a timer becomes an adder ($a = 1$) and corrects deviations by half each generation.

4. In a population of irradiated cells, Western blots show a single wave of p53 that rises and then falls with damped oscillations. Single-cell imaging shows undamped pulses. Explain the discrepancy, and state what information the number of pulses carries.

   **Answer** Each cell pulses with similar amplitude, but the timing of the pulses (especially after the first) varies between cells, and different cells stop pulsing at different times as they finish repair. Averaging signals with dispersed phases produces a damped oscillation (panel C of the figure in 22.3.3), even though no single cell is damped. The number of pulses reflects how long breaks persist, so it is a digital readout of the amount of damage; the shape of the p53 signal (pulses versus sustained) influences the cell's fate.

5. Mice lacking *Mdm2* die early in development, but mice lacking both *Mdm2* and *Trp53* are viable. What does this tell you about the function of Mdm2? Why are small-molecule inhibitors of the Mdm2–p53 interaction (nutlins) of interest in cancers with wild-type *TP53*?

   **Answer** The lethality of *Mdm2* loss is caused entirely by unchecked p53 activity (arrest and apoptosis of embryonic cells); Mdm2's essential function is to keep p53 in check. In tumors that retain wild-type p53 but have amplified *MDM2* or lost *ARF*, blocking the Mdm2–p53 interaction stabilizes p53 and can re-activate arrest or apoptosis; tumors with mutant p53 do not respond.

6. Explain why expression of activated Ras transforms immortalized rodent cell lines but arrests normal human fibroblasts. What additional changes would allow Ras to transform the human cells?

   **Answer** In normal cells oncogenic Ras causes excess mitogenic signaling, which induces ARF and p16 and causes replication stress; p53 and Rb then impose oncogene-induced senescence. Immortalized cell lines have usually lost these safeguards (for example *Arf* or *Cdkn2a* deletion or p53 mutation). Human cells additionally need the loss of p53 and Rb pathway functions (for example by SV40 large T antigen or HPV E6/E7) and telomerase expression to avoid replicative senescence (Hahn et al. 1999 transformed human cells with large T, hTERT and Ras).

7. In the Rb–E2F model, why does tight binding of E2F by Rb (large $k_{\mathrm{RE}}$) help to make the switch sharp?

   **Answer** When Rb is in excess and binds E2F tightly, almost all E2F is sequestered and free E2F stays near zero, however much E2F is made, as long as free Rb exceeds total E2F. Free E2F appears only when E2F synthesis and Rb phosphorylation together exceed the remaining free Rb, and then rises steeply. This molecular titration creates an ultrasensitive threshold, and the positive loops (E2F → E2F, E2F → cyclin E → Rb phosphorylation) convert it into bistability.

8. (Open question) A tissue maintains a constant number of cells despite continuous division of its stem cells. List the cellular mechanisms of this chapter and of [7.3.25](/7.3.25) that could keep the number constant, and propose an experiment to distinguish whether division or death is regulated.

   **Answer** Mechanisms: regulated division (limited mitogens and survival factors, contact inhibition and Hippo–YAP, niche-restricted asymmetric divisions), regulated death (survival factor dependence, apoptosis of excess cells, shedding at the tissue surface), differentiation into nondividing cells, and senescence. To distinguish them, one can measure division (EdU or Ki-67 labeling, lineage tracing) and death (cleaved caspase-3, TUNEL, extrusion) after perturbing tissue size, for example after partial removal or after increasing cell number genetically: if the tissue returns to its size mainly by changing the labeling index, division is regulated; if mainly by apoptosis or extrusion, death is. Live imaging of clone sizes (neutral drift, [7.3.24](/7.3.24)) gives the balance in individual stem-cell lineages.
