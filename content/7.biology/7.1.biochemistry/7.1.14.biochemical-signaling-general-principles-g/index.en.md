---
title: "Biochemical Signaling I: General Principles, G Protein–Coupled Receptors, and Second Messengers"
description: The general features of signal transduction and the types of receptors; occupancy, efficacy, agonists and antagonists; G protein–coupled receptors, the G-protein switch and the β-adrenergic cAMP–PKA pathway, its amplification, termination and desensitization; G-protein classes and bacterial toxins; DAG, IP₃, Ca²⁺ and calmodulin; cGMP and NO; vision, olfaction and taste; gated ion channels, the nicotinic acetylcholine receptor and toxins.
---

Cells constantly sense their surroundings. A bacterium measures the pH, osmotic strength, nutrients, oxygen and light around it; in a multicellular organism cells exchange hundreds of signals, **hormones**, neurotransmitters, growth factors and metabolites, that coordinate **metabolism**, division, development, movement and defense. In every case a signal carries information that is detected by a specific receptor and converted into a chemical change in the cell. This chapter and the next describe the molecular machinery of that conversion. It is built from parts met earlier in the course: receptors are binding **proteins** whose occupancy follows the **dissociation constant** of [7.1.7](/7.1.7#sec-7.1.2); they change conformation as **allosteric proteins** do ([7.1.7](/7.1.7#sec-7.3.4)); and the signals they start are carried by **protein kinases** and **protein phosphatases** and amplified by **regulatory cascades** ([7.1.9](/7.1.9#sec-9.5.3)). Remarkably few mechanisms serve thousands of signals. This chapter covers the general features of signaling and the largest receptor family, the G protein–coupled receptors, with the second messengers they produce, their role in the senses, and the gated **ion channels**; receptor kinases, **nuclear receptors**, signaling in bacteria and plants, the cell cycle and **apoptosis** follow in [7.1.15](/7.1.15). The use of these pathways by hormones to integrate the metabolism of the whole body is the subject of [7.1.29](/7.1.29), their network dynamics that of systems biology ([7.9](/7.9)), and the electrical signaling of neurons that of [7.16](/7.16).

## 14.1. General Features of Signal Transduction

### 14.1.1. Signals, Receptors and Responses

**Definition 14.1.1 (Signal Transduction)** **Signal transduction** is the process by which a signal, a chemical or physical stimulus that carries information, is detected by a specific receptor and converted into a change in the activity of the cell. A **receptor** is a protein that binds a specific signal molecule (its ligand) or absorbs a specific stimulus and, in doing so, changes its own conformation or activity so that it transmits the signal to other molecules of the cell.

The general scheme is the same in all cases: the signal (the first messenger) binds the receptor; the activated receptor changes the activity of an enzyme or channel, producing an intracellular signal (a second messenger, or a protein modification); this signal changes the activity of target proteins, either existing **enzymes**, **transporters** and cytoskeletal proteins (a fast response, in seconds to minutes) or **transcription** factors (a slow response through changes in **gene** expression, in hours); and finally the signal is turned off.

### 14.1.2. Eight Features of Signaling Systems

| Feature | Meaning | Molecular basis |
|---|---|---|
| Specificity | only the right signal elicits the response, and only in the right cells | molecular complementarity of **ligand** and receptor; receptors and targets expressed only in certain cell types |
| Sensitivity | very low signal concentrations are detected | high affinity ($K_{\mathrm{d}} \le 10^{-7}\,\mathrm{M}$, often nanomolar); **cooperativity**; amplification by **enzyme cascades** |
| Amplification | one signal molecule changes very many target molecules | catalysts activating catalysts (14.2.3) |
| Modularity | the same parts are combined into many pathways | signaling proteins with several **domains** that bind phosphorylated **residues**, **lipids** or other proteins ([7.1.15](/7.1.15)) |
| Desensitization (adaptation) | a persistent signal loses its effect; sensitivity returns when the signal is removed | feedback on the receptor (phosphorylation, arrestin, endocytosis) |
| Integration | several signals give one appropriate response | pathways converge on shared components; synergism (more than additive), antagonism (opposite effects), cross talk |
| Divergence | one signal starts several branches with different outputs | branched pathways ([7.1.15](/7.1.15)) |
| Localization | the response is confined to part of a cell | **scaffold proteins**, rafts ([7.1.13](/7.1.13#sec-13.2.4)) |

Specificity arises at two levels. Thyrotropin-releasing hormone acts on cells of the anterior pituitary but not on hepatocytes, which lack its receptor; **epinephrine** has receptors on both hepatocytes and adipocytes but mobilizes **glycogen** only in the liver, because only hepatocytes contain glycogen and the enzymes that respond. Integration is just as important. Whether a plant flowers, for example, depends on day length, temperature, the age of the plant and hormones, whose pathways converge on a few integrator proteins; and a typical animal cell needs a combination of survival, growth and division signals, without which it dies by apoptosis ([7.1.15](/7.1.15)). When signaling fails, development fails visibly: plants with defective brassinosteroid receptors are dwarfs, and mutants defective in the perception of gravity grow their roots in random directions.

### 14.1.3. Types of Receptors

Several hundred human receptors fall into a few structural classes, which are also the mechanisms of transduction.

| Receptor type | Structure and mechanism | Examples | Section |
|---|---|---|---|
| G protein–coupled receptors (GPCRs) | seven transmembrane helices; activate a heterotrimeric G protein, which regulates an enzyme or channel that changes a second messenger | β-adrenergic receptor, rhodopsin, olfactory receptors | 14.2–14.4 |
| Receptor enzymes | one transmembrane helix; ligand binding activates a cytoplasmic enzyme domain | **receptor tyrosine kinases** (**insulin**, EGF), receptor guanylyl cyclases (ANF), plant receptor Ser/Thr kinases | [7.1.15](/7.1.15), 14.3.3 |
| Receptors without enzyme activity | ligand binding activates an associated soluble kinase | cytokine receptors with JAK | [7.1.15](/7.1.15) |
| Gated ion channels | open or close in response to a ligand or to the membrane potential | nicotinic acetylcholine receptor, voltage-gated Na⁺ channel | 14.5 |
| Adhesion receptors | bind the extracellular matrix and the cytoskeleton, signal in both directions | **integrins** | [7.1.15](/7.1.15) |
| Nuclear receptors | intracellular; the hormone–receptor complex binds **DNA** and regulates transcription | steroid, thyroid and retinoid receptors | [7.1.15](/7.1.15) |

Bacteria rely mainly on **two-component systems** of histidine kinases ([7.1.15](/7.1.15)); plants have hundreds of receptor kinases but very few GPCRs.

### 14.1.4. Occupancy, Efficacy, Agonists and Antagonists

The first quantitative step of signaling is binding. A receptor R binds its ligand L reversibly, and at equilibrium the fraction of receptors occupied is

$$
\theta = \frac{[\mathrm{L}]}{K_{\mathrm{d}} + [\mathrm{L}]},
$$
the hyperbolic binding curve of [7.1.7](/7.1.7#sec-7.1.2). The response, however, is not simply proportional to occupancy, and drugs that act on receptors are classified by how occupancy is turned into response.

**Definition 14.1.2 (Agonist and Antagonist)** An **agonist** is a molecule (the natural ligand or a structural analog) that binds a receptor and produces the effect of the natural ligand; a partial agonist produces only part of the maximal effect even when it occupies all receptors. An **antagonist** binds the receptor without producing the effect and thereby blocks the action of agonists; a competitive antagonist binds reversibly to the same site as the agonist.

**Formula 14.1.1 (Operational Model)** If the response is a hyperbolic function of the concentration of agonist–receptor complexes (Black and Leff, 1983), then

$$
\frac{E}{E_{\max}} = \frac{\tau[\mathrm{A}]}{K_{\mathrm{A}} + (1 + \tau)[\mathrm{A}]}, \qquad \mathrm{EC}_{50} = \frac{K_{\mathrm{A}}}{1 + \tau}, \qquad \frac{E(\infty)}{E_{\max}} = \frac{\tau}{1 + \tau},
$$
where $K_{\mathrm{A}}$ is the **dissociation constant** of the agonist, $E_{\max}$ the maximal response of the system, and the efficacy $\tau$ is the number of receptors divided by the number of agonist–receptor complexes needed for half-maximal response. In the presence of a competitive antagonist B (dissociation constant $K_{\mathrm{B}}$), $[\mathrm{A}]$ is replaced by $[\mathrm{A}]/(1 + [\mathrm{B}]/K_{\mathrm{B}})$, so the curve shifts to the right by the dose ratio $r = 1 + [\mathrm{B}]/K_{\mathrm{B}}$ without a change in maximum (the Schild relation, $\log(r - 1) = \log[\mathrm{B}] - \log K_{\mathrm{B}}$).

The model makes three practical points. First, a high-efficacy agonist ($\tau \gg 1$) gives a half-maximal response at a concentration far below $K_{\mathrm{A}}$, when only a small fraction of the receptors is occupied: the cell has spare receptors, and the potency of a drug ($\mathrm{EC}_{50}$) differs from its affinity ($K_{\mathrm{A}}$). Second, the same molecule can be a full agonist in a tissue rich in receptors and a partial agonist in a tissue with few, because $\tau$ depends on receptor number. Third, measuring the shift produced by several antagonist concentrations gives $K_{\mathrm{B}}$ independently of the agonist used, which is how receptor subtypes were first classified. Synthetic ligands can bind more tightly than the natural one: for the β-adrenergic receptor, the agonist isoproterenol and the antagonist propranolol (a "beta blocker") both have a higher affinity than epinephrine. Many drugs act this way; the active component of cannabis, Δ⁹-tetrahydrocannabinol (THC), is an agonist of the cannabinoid receptor CB1, a GPCR of the brain whose natural ligands are lipid-derived endocannabinoids such as anandamide.

![Receptor occupancy and response in the operational model (Formula 14.1.1), with concentrations in units of K_A. A: an agonist of high efficacy (τ = 30) gives a half-maximal response (dot) at one thirtieth of K_A, when only 3% of the receptors are occupied (spare receptors); with τ = 3 the maximum is still 75%; a partial agonist (τ = 0.5) reaches only a third of the maximal response at full occupancy (dashed: occupancy θ). B: a competitive antagonist at [B]/K_B = 3, 30 and 300 shifts the curve of the full agonist to the right in parallel, by the dose ratio r = 1 + [B]/K_B, without lowering its maximum](./plots/dose-response.py)

## 14.2. G Protein–Coupled Receptors and cAMP

### 14.2.1. GPCRs and Heterotrimeric G Proteins

**Definition 14.2.1 (G Protein–Coupled Receptor)** A **G protein–coupled receptor** (GPCR; seven-transmembrane or heptahelical receptor) is an integral membrane protein with seven transmembrane α helices that, when it binds its ligand (or, for rhodopsin, absorbs a photon), activates a heterotrimeric G protein on the cytoplasmic side of the membrane.

**Definition 14.2.2 (Heterotrimeric G Protein)** A **heterotrimeric G protein** consists of an α subunit, which binds GDP or GTP and has a GTPase activity, and a tightly associated βγ dimer. With GDP bound, the trimer $\mathrm{G\alpha\beta\gamma}{\cdot}\mathrm{GDP}$ is inactive; exchange of GDP for GTP activates it and separates $\mathrm{G\alpha}{\cdot}\mathrm{GTP}$ from $\mathrm{G\beta\gamma}$, and each part then regulates effector proteins until the α subunit hydrolyzes its GTP.

The α **subunit** is anchored to the membrane by an N-terminal palmitoyl (and in some classes myristoyl) group and the γ subunit by a C-terminal prenyl group ([7.1.13](/7.1.13#sec-13.1.6)), so the G protein moves only in the plane of the membrane. The human **genome** encodes about 800 GPCRs, the largest **protein family** of the genome: roughly 350 respond to hormones, neurotransmitters and other endogenous ligands and about 400 are olfactory receptors, the rest taste and other sensory receptors, and more than a hundred are still "orphans" whose ligands are unknown. GPCRs are the targets of about a third of all approved drugs, among them the beta blockers, antihistamines, opioids, many antipsychotics and the GLP-1 receptor agonists used against **diabetes** and obesity. Their **mutations** are found in many diseases and in about a fifth of cancers.

The G protein is a switch with a built-in timer, and the receptor turns it on by catalyzing nucleotide exchange.

**Definition 14.2.3 (GEF and GAP)** A **guanine nucleotide-exchange factor** (GEF) is a protein that catalyzes the release of GDP from a G protein, allowing GTP, about ten times more concentrated than GDP in the cytosol, to bind; a ligand-bound GPCR is the GEF of its heterotrimeric G protein. A **GTPase-activating protein** (GAP) accelerates the hydrolysis of GTP by a G protein and so shortens its active period; the GAPs of heterotrimeric G proteins are called **regulators of G-protein signaling** (RGS proteins).

Because the GTPase of most α subunits is slow (a few GTP per minute) and an RGS protein can raise it a hundredfold or more, the balance of exchange and hydrolysis, rather than a single event, sets the fraction of active G protein and thus the strength of the response. Small monomeric G proteins such as **Ras** ([7.1.15](/7.1.15)) work by the same mechanism.

![The G-protein switch in β-adrenergic signaling. 1: the receptor (seven transmembrane helices) and the heterotrimeric G protein Gs (α with GDP; β and γ) are inactive. 2: epinephrine (Epi) binds; the occupied receptor acts as a GEF: GDP leaves the α subunit and GTP binds. 3: Gsα·GTP separates from βγ and stimulates adenylyl cyclase (AC), which converts ATP to cAMP. 4: the GTPase of α, accelerated by RGS proteins, hydrolyzes GTP to GDP and Pᵢ; α·GDP leaves the cyclase and reassociates with βγ (dashed arrow), returning to state 1](./plots/g-protein-cycle.py)

### 14.2.2. The β-Adrenergic System Acts through cAMP

Epinephrine (adrenaline), secreted by the adrenal medulla in response to fear, anger or exercise, prepares the body for "fight or flight": it raises the heart rate and mobilizes glucose and **fatty acids**. It acts through four types of adrenergic receptors, $\alpha_1$, $\alpha_2$, $\beta_1$ and $\beta_2$, distinguished by their responses to agonists and antagonists and present in different tissues. The β receptors of muscle, liver and adipose tissue act through the following sequence, which has become the prototype of all GPCR signaling.

1. Epinephrine binds its receptor on the outer face of the plasma membrane; an allosteric change in the receptor exposes a site for the G protein.
2. The occupied receptor catalyzes GDP/GTP exchange on the stimulatory G protein Gs.
3. $\mathrm{G_{s\alpha}}{\cdot}\mathrm{GTP}$ separates from $\mathrm{G\beta\gamma}$ and binds adenylyl cyclase.
4. Adenylyl cyclase converts ATP into the second messenger cAMP.
5. cAMP activates **protein kinase** A.
6. PKA phosphorylates target enzymes, among them **phosphorylase kinase**, which phosphorylates and activates **glycogen phosphorylase** ([7.1.19](/7.1.19)), and **glycogen synthase**, which phosphorylation inactivates.
7. cAMP phosphodiesterase degrades cAMP, ending its action.

**Definition 14.2.4 (Second Messenger)** A **second messenger** is a small molecule or ion whose concentration in the cytosol changes when a signal (the first messenger) binds its receptor at the cell surface, and which carries the signal to intracellular targets: cAMP, cGMP, inositol 1,4,5-trisphosphate, diacylglycerol and $\ce{Ca^2+}$ are the main ones.

**Definition 14.2.5 (Adenylyl Cyclase and cAMP)** **Adenylyl cyclase** is an integral membrane enzyme, with its catalytic site on the cytoplasmic face, that converts ATP into **cyclic AMP** (adenosine 3′,5′-cyclic monophosphate, cAMP) and pyrophosphate; in animals its isoforms are stimulated by $\mathrm{G_{s\alpha}}$ and inhibited by $\mathrm{G_{i\alpha}}$, and some are regulated by $\ce{Ca^2+}$–calmodulin or $\mathrm{G\beta\gamma}$. A **cyclic nucleotide phosphodiesterase** (PDE) hydrolyzes the 3′ ester of cAMP (or cGMP), giving 5′-AMP (or 5′-GMP), which is not a messenger.

```smiles
Nc1ncnc2c1ncn2[C@@H]1O[C@@H]2COP(=O)(O)O[C@H]2[C@H]1O cAMP
```

**Definition 14.2.6 (Protein Kinase A)** **Protein kinase A** (PKA, cAMP-dependent protein kinase) is an $\mathrm{R_2C_2}$ tetramer of two regulatory and two catalytic subunits. In the tetramer an autoinhibitory (pseudosubstrate) sequence of each R subunit occupies the substrate-binding cleft of a C subunit; when each R subunit binds two cAMP, the complex dissociates into $\mathrm{R_2(cAMP)_4}$ and two active C subunits, which phosphorylate Ser or Thr residues in the **consensus sequence** Arg–Arg–X–Ser/Thr–hydrophobic.

The structure of the catalytic subunit of PKA, a small N-terminal lobe that binds ATP and a large C-terminal lobe that binds the protein **substrate**, is the prototype of the more than 500 protein kinases of the human genome, and displacement of an autoinhibitory segment by a second messenger is the activation mechanism of many of them (PKC, PKG and the CaM kinases below). Because four cAMP are bound cooperatively, PKA responds steeply to [cAMP]. Its catalytic subunit can also enter the nucleus and phosphorylate the transcription factor CREB (cAMP response element binding protein), which then activates genes with a cAMP response element (CRE) in their **promoters**; this is how cAMP changes gene expression over hours, in the liver, for example, the expression of gluconeogenic enzymes ([7.1.19](/7.1.19)).

![The β-adrenergic cascade of a hepatocyte in SBGN process description notation. Epinephrine (Epi) binds the β-adrenergic receptor (association, filled disc); the complex catalyzes (open circle) the exchange of GDP for GTP on Gsα; Gsα·GTP stimulates (open arrow) adenylyl cyclase (AC), which converts ATP to cAMP; phosphodiesterase (PDE) converts cAMP to 5′-AMP. Four cAMP dissociate the inactive PKA tetramer (dissociation, double circle) into R₂(cAMP)₄ and two active C subunits. PKA phosphorylates phosphorylase kinase (PhK), which is further stimulated by Ca²⁺, and glycogen synthase (GS), inactivating it. PhK phosphorylates phosphorylase b to the active a form, which cleaves glycogen to glucose 1-phosphate; glucose is formed in further steps (omitted process, //) and leaves the hepatocyte through GLUT2](./plots/beta-adrenergic-cascade.py)

**Remark 14.2.1** Two enzyme names that recur here are easily confused. A kinase transfers a phosphoryl group from a nucleoside triphosphate (usually ATP) to an acceptor, a sugar, a protein, a nucleotide or another metabolite: hexokinase phosphorylates glucose, phosphorylase kinase phosphorylates a protein. A phosphorylase catalyzes phosphorolysis, the cleavage of a bond by inorganic phosphate, which becomes attached at the point of cleavage: glycogen phosphorylase cleaves glycogen to glucose 1-phosphate.

The pathway was discovered in steps, each of which gave a principle of the field. Carl and Gerty Cori showed in the 1930s and 1940s that glycogen phosphorylase exists in a less active b and an active a form (Nobel Prize 1947). Earl Sutherland found in the 1950s that epinephrine converts phosphorylase b to a in a liver homogenate only if the particulate (membrane) fraction is present, and that the membranes, treated with hormone, release a heat-stable factor that activates phosphorylase in the soluble fraction: the factor was cAMP, the first second messenger (Nobel Prize 1971). Edwin Krebs and Edmond Fischer showed that the conversion of phosphorylase b to a is a phosphorylation catalyzed by a protein kinase, phosphorylase kinase, which itself requires $\ce{Ca^2+}$ and ATP, establishing reversible phosphorylation as a regulatory mechanism (Nobel Prize 1992); Krebs then purified PKA (1968). Alfred Gilman and Martin Rodbell discovered that a GTP-binding protein links the receptor to adenylyl cyclase (Nobel Prize 1994), and Robert Lefkowitz and Brian Kobilka described the receptors themselves, their desensitization and, in 2011, the structure of the β₂-adrenergic receptor in complex with Gs (Nobel Prize 2012).

### 14.2.3. Amplification

Each step of the β-adrenergic pathway after hormone binding is catalytic, so the signal grows from step to step: one occupied receptor activates many Gs molecules in succession, each activated adenylyl cyclase makes many cAMP molecules, each PKA phosphorylates many phosphorylase kinase molecules, each of which activates many phosphorylase molecules, each of which releases many glucose 1-phosphate from glycogen. If step $i$ has gain $g_i$ (product molecules per activated input molecule), the overall gain of the **regulatory cascade** is the product

$$
G = \prod_i g_i ,
$$
which can reach $10^8$ or more with gains of 10–100 per stage (Lehninger estimates "several orders of magnitude within milliseconds"). One step does not amplify: four cAMP are needed to free two catalytic subunits of PKA. Amplification explains why hormones act at nanomolar concentrations, and its dynamics, a growing delay and the need for fast shutoff at every stage, are those of the cascades of [7.1.9](/7.1.9#sec-9.6.2).

![Amplification in the epinephrine cascade, an order-of-magnitude illustration: molecules activated (or, for cAMP and glucose 1-phosphate, produced) per occupied receptor at each stage, with the gain of each step above the arrows (values chosen within the ranges discussed in the text; actual numbers depend on cell type). The gains multiply to about 5 × 10⁸; the step from cAMP to the catalytic subunits of PKA is a loss (factor 0.5), because four cAMP free two subunits](./plots/cascade-amplification.py)

### 14.2.4. Termination and Desensitization

A signaling system must stop when the stimulus ends, so that the response stays proportional to the signal. The β-adrenergic system has a mechanism at every level:

- when the epinephrine concentration falls below $K_{\mathrm{d}}$, the hormone dissociates and the receptor stops catalyzing exchange;
- $\mathrm{G_{s\alpha}}$ hydrolyzes its GTP, accelerated by RGS proteins, and returns to the inactive trimer;
- phosphodiesterases hydrolyze cAMP, which has a lifetime of seconds in the cell;
- **protein phosphatases** remove the phosphoryl groups added by PKA. About 190 human genes encode protein phosphatases, against about 540 encoding protein kinases, and a single phosphatase such as PP1 acts on some 200 substrates.

**Formula 14.2.1 (cAMP Dynamics)** If adenylyl cyclase is activated in proportion to the active receptor fraction $a(t)$ and PDE acts below saturation, $\dfrac{\mathrm{d}[\mathrm{cAMP}]}{\mathrm{d}t} = k_{\mathrm{AC}}\,a(t) - k_{\mathrm{PDE}}[\mathrm{cAMP}]$, so a steady stimulus gives the level $k_{\mathrm{AC}}a/k_{\mathrm{PDE}}$, reached with the time constant $1/k_{\mathrm{PDE}}$.

The phosphodiesterase therefore sets both the level and the speed of the response, and inhibiting it (caffeine and theophylline, weak PDE inhibitors, or the experimental inhibitor IBMX) raises the level and slows the decay. A different mechanism, desensitization, damps the response while the signal persists.

**Definition 14.2.7 (Desensitization and Arrestin)** **Desensitization** is the reduction of a receptor system's response during continued exposure to its signal. In GPCRs it is brought about by **G protein–coupled receptor kinases** (GRKs, such as β-adrenergic receptor kinase, βARK or GRK2), which phosphorylate Ser and Thr residues in the cytoplasmic C-terminal region of the occupied receptor, and by **arrestins**, which bind the phosphorylated receptor, block its interaction with the G protein and recruit clathrin and its adaptors for endocytosis.

βARK is recruited to the membrane by the free $\mathrm{G\beta\gamma}$ released when the receptor is active, so it phosphorylates mainly occupied receptors: desensitization is a negative feedback triggered by the response itself. The internalized receptors are later dephosphorylated and returned to the membrane (resensitization) or degraded. Seven GRKs and four arrestins serve all GPCRs. Arrestin is also a scaffold that starts signaling of its own, through **MAP kinase cascades** ([7.1.15](/7.1.15)). Ligands that favor one of the two branches, G protein or arrestin, are called biased agonists; they are of great interest in pharmacology (for example, opioids that relieve pain with fewer side effects), although which effects are carried by which branch is still debated.

![A minimal model of receptor desensitization (Formula 14.2.1 coupled to dd/dt = k_des θ(1 − d) − k_rec d for the desensitized fraction d; k_des = 0.3, k_rec = 0.05, k_AC = k_PDE = 2 min⁻¹). A: during 30 min of agonist at 10 K_d (shaded) cAMP peaks and then adapts to about a fifth of its peak while the receptor remains occupied; after 15 min of washout only part of the receptors has resensitized (time constant 1/k_rec = 20 min), so a second stimulus gives a smaller response. B: partial inhibition of phosphodiesterase (k_PDE = 0.5 min⁻¹) raises the peak and the plateau of cAMP and slows its decay after washout](./plots/adaptation-model.py)

### 14.2.5. G-Protein Classes and Bacterial Toxins

Humans have 16 genes for Gα subunits (giving about 21 proteins by **alternative splicing**), 5 for Gβ and 12 for Gγ, which form four main families defined by their α subunits.

| Family | α subunits | Main effectors | Examples of receptors |
|---|---|---|---|
| $\mathrm{G_s}$ | $\mathrm{G_{s\alpha}}$, $\mathrm{G_{olf}}$ | adenylyl cyclase ↑ | β-adrenergic, **glucagon**, ACTH, TSH, dopamine D₁, odorant receptors |
| $\mathrm{G_{i/o}}$ | $\mathrm{G_{i}}$, $\mathrm{G_{o}}$, $\mathrm{G_t}$ (transducin), $\mathrm{G_{gust}}$ (gustducin) | adenylyl cyclase ↓; βγ opens K⁺ channels; cGMP PDE (transducin) | α₂-adrenergic, somatostatin, opioid, muscarinic M₂, rhodopsin |
| $\mathrm{G_{q/11}}$ | $\mathrm{G_q}$, $\mathrm{G_{11}}$ | phospholipase Cβ ↑ | α₁-adrenergic, muscarinic M₁, vasopressin V₁, histamine H₁, angiotensin II |
| $\mathrm{G_{12/13}}$ | $\mathrm{G_{12}}$, $\mathrm{G_{13}}$ | Rho GEFs (cytoskeleton) | thrombin (PAR), lysophosphatidic acid |

Because different receptors for the same hormone can couple to different G proteins, one signal can have opposite effects in different tissues: epinephrine raises cAMP through β receptors (Gs) but lowers it through α₂ receptors (Gi), and **prostaglandin** E₂ lowers cAMP in adipocytes while raising it in other tissues. A cell integrates its Gs and Gi inputs at the adenylyl cyclase.

Two bacterial toxins exploit the switch. Cholera toxin (from *Vibrio cholerae*) binds **ganglioside** GM1 on intestinal epithelial cells; its A1 fragment, activated by the host's small G protein ARF6, transfers ADP-ribose from $\ce{NAD+}$ to an Arg residue of $\mathrm{G_{s\alpha}}$ that is required for GTP hydrolysis. $\mathrm{G_{s\alpha}}$ is then locked in its active state, cAMP stays high, and PKA keeps the CFTR chloride channel open ([7.1.13](/7.1.13#sec-13.5.4)); $\ce{NaCl}$ and water pour into the intestine, and the patient can lose more than ten liters of fluid a day. Oral rehydration with glucose and salt, which uses the intestinal Na⁺–glucose **symporter** ([7.1.13](/7.1.13#sec-13.5.5)), saves most patients. Pertussis toxin (from *Bordetella pertussis*, whooping cough) ADP-ribosylates a Cys residue near the C-terminus of $\mathrm{G_{i\alpha}}$, which prevents its activation by receptors; the inhibitory input to adenylyl cyclase is lost and cAMP rises.

Mutations in G proteins cause disease too: activating mutations of $\mathrm{G_{s\alpha}}$, which eliminate its GTPase, occur in about 40% of growth hormone–secreting pituitary tumors, and inactivating ones make tissues unresponsive to hormones that act through cAMP.

Plants use the switch differently. *Arabidopsis* has one canonical Gα, one Gβ, three Gγ subunits and three extra-large Gα proteins (XLGs), but probably no true GPCR (whether the candidate GCR1 is one is still disputed). Its Gα exchanges GDP for GTP spontaneously and quickly, so it does not need a GEF; it is instead kept inactive by RGS1, a seven-transmembrane protein with an RGS domain, and activated when receptor-like kinases at the cell surface (7.1.15) phosphorylate RGS1 and cause its endocytosis. The few G-protein subunits of plants thus serve many signals through combinations with the large family of receptor kinases, rather than with GPCRs.

### 14.2.6. Many Signals Use cAMP; Localization by AKAPs

Glucagon, ACTH, TSH, FSH and LH, parathyroid hormone, histamine (H₂ receptors), serotonin (5-HT₁ and 5-HT₄), dopamine (D₁), prostaglandins E, many odorants and the sweet and bitter tastes act through changes in cAMP. Glucagon in adipocytes and epinephrine in muscle use the same second messenger and the same kinase for different purposes, because the set of PKA substrates differs between cells. How can one diffusible messenger carry different messages even within one cell? Part of the answer is confinement.

**Definition 14.2.8 (AKAP)** An **A kinase anchoring protein** (AKAP) is a scaffold protein that binds the regulatory subunits of PKA and also a specific subcellular structure (the plasma membrane, microtubules, actin, mitochondria, ion channels or the nucleus), confining PKA to that location; many AKAPs also bind the adenylyl cyclase, phosphodiesterase or phosphatase that start and end the signal.

AKAP5, for example, is held in rafts of the plasma membrane by two palmitoyl groups and a PIP₃-binding site and binds the β-adrenergic receptor, adenylyl cyclase, PKA and the phosphatase PP2A. cAMP made by the cyclase reaches the nearby PKA at high concentration before it is degraded or diluted, and the phosphatase reverses the phosphorylation quickly, so the signal is a brief, local "puff". Different cell types express different AKAPs, so cAMP can stimulate the phosphorylation of mitochondrial proteins in one cell and of cytoskeletal proteins in another. FRET-based sensors that make such cAMP gradients visible in living cells are described in [7.1.15](/7.1.15).

## 14.3. Diacylglycerol, IP₃ and Ca²⁺

### 14.3.1. Phospholipase C

A second large class of GPCRs couples through $\mathrm{G_q}$ to a phospholipase C that cleaves a minor lipid of the cytoplasmic leaflet, phosphatidylinositol 4,5-bisphosphate (PIP₂; [7.1.12](/7.1.12#sec-12.5.1)), into two messengers.

**Definition 14.3.1 (Phospholipase C, IP₃ and DAG)** **Phospholipase C** (PLC) hydrolyzes the phosphodiester bond between glycerol and inositol in PIP₂, releasing the water-soluble **inositol 1,4,5-trisphosphate** (IP₃) into the cytosol and leaving **diacylglycerol** (DAG) in the membrane. PLCβ is activated by $\mathrm{G_{q\alpha}}$ (and by Gβγ), PLCγ by receptor tyrosine kinases ([7.1.15](/7.1.15)).

The sequence is: an agonist (acetylcholine on M₁ receptors, vasopressin, α₁-adrenergic agonists, histamine on H₁ receptors, angiotensin II, thrombin and others) binds its receptor; $\mathrm{G_q}$ is activated; PLCβ cleaves PIP₂; IP₃ diffuses to the endoplasmic reticulum and opens the IP₃ receptor, a $\ce{Ca^2+}$ channel; $\ce{Ca^2+}$, held in the ER at concentrations thousands of times higher than in the cytosol by the SERCA pump ([7.1.13](/7.1.13#sec-13.5.2)), rushes out, and cytosolic $[\ce{Ca^2+}]$ rises from about $10^{-7}$ to $10^{-6}\,\mathrm{M}$; $\ce{Ca^2+}$ and DAG together activate protein kinase C.

**Definition 14.3.2 (Protein Kinase C)** **Protein kinase C** (PKC) is a family of Ser/Thr protein kinases whose conventional members are activated by DAG and $\ce{Ca^2+}$ together with the membrane lipid phosphatidylserine, which pull the enzyme to the membrane and displace its pseudosubstrate domain from the active site.

The IP₃ receptor is a tetramer of 1.3 MDa with 24 transmembrane helices around a central pore; IP₃ binds near the N-terminal end of each subunit, far from the pore in the ER membrane, and opens it allosterically. Phorbol esters, plant compounds that mimic DAG but are not degraded, activate PKC permanently and are powerful tumor promoters, an early clue that PKC regulates cell division. The signal ends when IP₃ is dephosphorylated (or phosphorylated further) and DAG is phosphorylated to **phosphatidic acid**, and when $\ce{Ca^2+}$ is pumped back into the ER and out of the cell.

### 14.3.2. Ca²⁺ as a Second Messenger

$\ce{Ca^2+}$ triggers exocytosis in neurons and **endocrine** cells, contraction of muscle, cytoskeletal rearrangements in moving cells and fertilization, among many other responses. Its signaling depends on the extreme gradient that cells maintain: the cytosolic concentration is about $0.1\,\mu\mathrm{M}$, the extracellular one 1–2 mM and that in the ER 0.1–1 mM, so opening a few channels in the plasma membrane or the ER raises cytosolic $\ce{Ca^2+}$ tenfold within milliseconds. Unlike $\ce{Na+}$ and $\ce{K+}$, whose concentrations hardly change when channels open, $\ce{Ca^2+}$ changes enough to serve as a messenger ([7.1.13](/7.1.13#sec-13.3.1)).

**Definition 14.3.3 (Calmodulin)** **Calmodulin** (CaM) is a small acidic protein ($M_{\mathrm{r}} \approx 17\,000$) with four $\ce{Ca^2+}$-binding sites, each an EF hand (a helix–loop–helix motif), with dissociation constants near $1\,\mu\mathrm{M}$. When cytosolic $[\ce{Ca^2+}]$ rises to about $1\,\mu\mathrm{M}$, $\ce{Ca^2+}$ binds, calmodulin exposes hydrophobic patches on its two lobes, and its flexible central helix wraps around helical segments of target proteins, changing their activity.

Calmodulin is the regulatory subunit of phosphorylase kinase of muscle, so the $\ce{Ca^2+}$ that triggers contraction also mobilizes glycogen to fuel it; and it regulates the $\ce{Ca^2+}$/calmodulin-dependent protein kinases (CaM kinases I–IV), adenylyl cyclase (brain) and cAMP phosphodiesterase, calcineurin (protein phosphatase 2B), myosin light-chain kinase of smooth muscle, NO synthase, **PI 3-kinase**, the plasma membrane $\ce{Ca^2+}$ pump and several ion channels. It belongs to a family of EF-hand proteins that includes troponin C, which triggers contraction of skeletal muscle ([7.1.7](/7.1.7#sec-7.5)). CaMKII, a dodecamer, phosphorylates itself when it is activated, which keeps it active after $[\ce{Ca^2+}]$ falls; this molecular memory is central to synaptic plasticity.

$\ce{Ca^2+}$ signals are limited in space and time. Cytosolic buffers bind most entering $\ce{Ca^2+}$, so a free ion travels only a short distance from a channel before it is captured, and local "puffs" and "sparks" can act on nearby targets without affecting the rest of the cell. With a steady hormone concentration, cytosolic $\ce{Ca^2+}$ often oscillates with a period of seconds to minutes: in a hepatocyte stimulated with norepinephrine it swings between about 200 and 500 nM. The oscillations arise because $\ce{Ca^2+}$ itself first stimulates and then inhibits the IP₃ receptor (a fast positive and a slower negative feedback, [7.9](/7.9)), and they convert the concentration of a hormone into the frequency of $\ce{Ca^2+}$ spikes, which targets such as CaMKII can decode. A growing pollen tube shows oscillations of a steep tip-focused $\ce{Ca^2+}$ gradient that are coupled to its pulses of growth. There is extensive cross talk between the $\ce{Ca^2+}$ and cAMP systems: in some tissues both the cyclase that makes cAMP and the phosphodiesterase that degrades it are $\ce{Ca^2+}$/calmodulin-dependent.

### 14.3.3. cGMP and Protein Kinase G

Guanosine 3′,5′-cyclic monophosphate is a second messenger made by guanylyl cyclases, which come in two forms.

**Definition 14.3.4 (Guanylyl Cyclase and Protein Kinase G)** **Guanylyl cyclases** convert GTP into cyclic GMP (cGMP). Receptor guanylyl cyclases are homodimeric receptor enzymes with an extracellular ligand-binding domain, one transmembrane helix and a cytoplasmic cyclase domain; soluble guanylyl cyclase is a cytosolic heme protein activated by nitric oxide. Most effects of cGMP in animals are mediated by **protein kinase G** (PKG, cGMP-dependent protein kinase), a Ser/Thr kinase whose regulatory and catalytic domains are in one polypeptide; cGMP also opens cyclic nucleotide-gated channels (14.4.1).

Atrial natriuretic factor (ANF), released by the heart when it is stretched by a high blood volume, activates a receptor guanylyl cyclase in the kidney and in vascular smooth muscle; the resulting cGMP increases renal excretion of $\ce{Na+}$ and water and relaxes the blood vessels, lowering blood volume and pressure. The **peptide** guanylin activates another receptor guanylyl cyclase in the intestinal epithelium that controls $\ce{Cl-}$ secretion; the heat-stable enterotoxin of pathogenic *E. coli* activates the same receptor and causes diarrhea.

Nitric oxide (NO), made from arginine by the $\ce{Ca^2+}$/calmodulin-dependent NO synthase ([7.1.27](/7.1.27)), is a gas that diffuses from its cell of origin into neighboring cells, where it binds the **heme** of soluble guanylyl cyclase. In blood vessels, acetylcholine or shear stress makes endothelial cells produce NO, which relaxes the surrounding smooth muscle through cGMP and PKG (PKG lowers cytosolic $\ce{Ca^2+}$ and the $\ce{Ca^2+}$ sensitivity of the contractile apparatus). NO lasts only seconds before it is oxidized to nitrite and nitrate, but nitroglycerin and other nitrovasodilators release it slowly over hours; they relieve angina pectoris mainly by dilating veins, which lowers the load on the heart and its oxygen demand, and by dilating coronary arteries. (The use of nitroglycerin was discovered in explosives factories of the nineteenth century, where workers with angina felt better on working days than at weekends.) cGMP is degraded by cGMP phosphodiesterases; sildenafil and tadalafil inhibit the isoform PDE5 of the smooth muscle of the corpora cavernosa and of the pulmonary vessels, which prolongs the cGMP signal and is used against erectile dysfunction and pulmonary hypertension ([7.1.9](/7.1.9#sec-9.4.3)).

## 14.4. GPCRs in Vision, Olfaction and Taste

### 14.4.1. Vision: Rhodopsin and Transducin

The senses of vision, smell and taste use GPCR mechanisms in specialized sensory cells, with amplification, adaptation and integration at every step.

**Definition 14.4.1 (Rhodopsin)** **Rhodopsin** is the photoreceptor GPCR of the rod cells of the vertebrate retina: the protein opsin with the chromophore 11-cis-retinal attached as a protonated Schiff base to a Lys residue of its seventh transmembrane helix. Absorption of a photon isomerizes the retinal to all-trans; the change in shape of the chromophore drives the receptor into its active conformation (metarhodopsin II, R*), which activates the G protein **transducin**.

Rods are specialized for dim light and contain about $10^8$ rhodopsin molecules in the stacked disk membranes of their outer segment. In the dark, a high concentration of cGMP keeps cyclic nucleotide-gated (CNG) cation channels in the plasma membrane open, and $\ce{Na+}$ and $\ce{Ca^2+}$ flow in (the dark current), so the dark membrane potential is only about $-40\,\mathrm{mV}$. Light starts a cascade:

1. R* catalyzes GDP/GTP exchange on transducin ($\mathrm{G_t}$), activating tens to hundreds of transducin molecules in its active lifetime;
2. $\mathrm{T_\alpha}{\cdot}\mathrm{GTP}$ binds the inhibitory γ subunits of the cGMP phosphodiesterase PDE6 and relieves the inhibition;
3. PDE6, one of the fastest enzymes known (each catalytic subunit hydrolyzes thousands of cGMP per second, near the diffusion limit), lowers [cGMP];
4. cGMP dissociates from the CNG channels, which bind it cooperatively (**Hill coefficient** about 3), and they close;
5. the $\ce{Na+}$/$\ce{Ca^2+}$,$\ce{K+}$ exchanger continues to export $\ce{Ca^2+}$, so $[\ce{Ca^2+}]$ falls, and the cell hyperpolarizes; it releases less glutamate at its synapse, and the signal passes through the neurons of the retina to the brain.

A single photon closes a few percent of the open channels and changes the current by about 1 pA, enough to be detected: rods can register single photons. Recovery is just as fast. Rhodopsin kinase (GRK1) phosphorylates R* and arrestin 1 binds it, ending its catalytic activity; transducin hydrolyzes its GTP, accelerated by the GAP complex RGS9–Gβ5, and PDE6 is inhibited again; and the fall in $[\ce{Ca^2+}]$ releases $\ce{Ca^2+}$ from guanylyl cyclase-activating proteins (GCAPs), which then stimulate guanylyl cyclase to restore cGMP. This $\ce{Ca^2+}$ feedback is also the basis of light adaptation, the reduced sensitivity in bright light. All-trans-retinal is released from the bleached opsin, carried out of the disks by the **ABC transporter** ABCA4 ([7.1.13](/7.1.13#sec-13.5.4)) and regenerated to 11-cis-retinal in the retinal pigment epithelium, a process that takes minutes and underlies dark adaptation.

![Phototransduction in a rod outer segment. A photon (hν) isomerizes 11-cis-retinal in rhodopsin in the disk membrane; activated rhodopsin (R*) catalyzes GDP/GTP exchange on many transducin α subunits (Tα); Tα·GTP removes the inhibitory γ subunits of the cGMP phosphodiesterase PDE6, which hydrolyzes cGMP to 5′-GMP. In the plasma membrane, cGMP-gated (CNG) channels close as [cGMP] falls, blocking the dark current of Na⁺ and Ca²⁺, while the exchanger NCKX (4 Na⁺ in, 1 Ca²⁺ and 1 K⁺ out) continues to export Ca²⁺. Recovery: rhodopsin kinase (GRK1) and arrestin shut off R*; the fall in [Ca²⁺] lets GCAPs activate guanylyl cyclase (GC), restoring cGMP](./plots/phototransduction.py)

Color vision uses three types of cone cells, each with one of three opsins whose absorption maxima, near 420 nm (blue, S), 530 nm (green, M) and 560 nm (red, L), are tuned by the amino acids around the same chromophore; rhodopsin absorbs maximally near 500 nm. The brain compares the outputs of the three cones. The genes for the red and green opsins lie side by side on the X chromosome and recombine unequally, which is why red–green color blindness is common in men: loss of the red pigment gives a red dichromat (protanope), loss of the green pigment a green dichromat (deuteranope), and altered pigments give anomalous trichromats. John Dalton, who described his own color blindness in 1794, asked that his eyes be examined after his death; DNA from his preserved retina, analyzed in the 1990s, showed that he lacked the gene for the green pigment and was a deuteranope. Mutations in the transducin α subunit cause a form of congenital night blindness.

### 14.4.2. Olfaction and Taste

Each olfactory sensory neuron of the nose expresses one of about 400 functional odorant receptor genes in humans (about 1100 in mice, the largest gene family of mammals). Odorants bind their GPCRs in the cilia of these neurons; the receptor activates $\mathrm{G_{olf}}$, which stimulates adenylyl cyclase III; cAMP opens CNG cation channels, and the entering $\ce{Ca^2+}$ opens $\ce{Ca^2+}$-activated $\ce{Cl-}$ channels, whose outward $\ce{Cl-}$ current (olfactory neurons keep a high internal $\ce{Cl-}$) amplifies the depolarization (the receptor potential). If it is large enough, the neuron fires action potentials to the olfactory bulb, all within 100–200 ms. Since each odorant activates a characteristic combination of receptors and each receptor responds to several odorants, a few hundred receptors can distinguish a very large number of odors. Shutoff uses the same set of mechanisms as before: PDE, GTP hydrolysis by $\mathrm{G_{olf}}$, phosphorylation of the receptor, and $\ce{Ca^2+}$/calmodulin, which lowers the cAMP sensitivity of the channel (adaptation).

Taste buds on the tongue contain cells specialized for five tastes. Sweet, umami and bitter are detected by GPCRs: sweet by the heterodimer T1R2–T1R3 ([7.1.10](/7.1.10)), umami (the taste of glutamate and other amino acids) by T1R1–T1R3, and bitter by about 25 T2R receptors, each recognizing many bitter compounds. All three activate the G protein gustducin, whose βγ subunits stimulate PLCβ2; IP₃ releases $\ce{Ca^2+}$ from the ER, which opens the cation channel TRPM5, depolarizes the cell and releases ATP as a transmitter onto the nerve fibers. Salty taste is mediated by the epithelial $\ce{Na+}$ channel ENaC and sour taste by the proton channel otopetrin-1, both ion channels rather than GPCRs. (Older textbooks, and Lehninger, describe taste transduction through cAMP and PKA closing $\ce{K+}$ channels; that model has been superseded by the PLCβ2–TRPM5 pathway.)

### 14.4.3. Common Features of GPCR Systems

Genome sequences reveal hundreds of GPCR genes in vertebrates, insects and nematodes, and even budding yeast detects the pheromone of the opposite mating type with a GPCR and a heterotrimeric G protein: the system is ancient and conserved.

| System | Receptor | G protein | Effector | Second messenger | Output |
|---|---|---|---|---|---|
| Hormone (epinephrine, liver) | β-adrenergic receptor | $\mathrm{G_s}$ | adenylyl cyclase ↑ | cAMP ↑ | PKA phosphorylates enzymes |
| Hormone (vasopressin, smooth muscle) | V₁ receptor | $\mathrm{G_q}$ | PLCβ ↑ | IP₃, DAG, Ca²⁺ ↑ | PKC, CaM kinases, contraction |
| Vision (rod) | rhodopsin | $\mathrm{G_t}$ | cGMP PDE ↑ | cGMP ↓ | CNG channels close: hyperpolarization |
| Olfaction | odorant receptor | $\mathrm{G_{olf}}$ | adenylyl cyclase ↑ | cAMP ↑ | CNG channels open: depolarization |
| Taste (sweet, umami, bitter) | T1R or T2R | gustducin (βγ) | PLCβ2 ↑ | IP₃, Ca²⁺ ↑ | TRPM5 opens: depolarization |

In all these systems the ligand-binding site (or the chromophore) lies within the seven-helix bundle; ligand binding moves the cytoplasmic ends of the helices, especially helix 6, opening a site for the G protein; the G protein changes an effector enzyme and a second messenger; the output is a protein kinase in hormone signaling and a change in membrane potential in sensory cells; the GTPase of the G protein, often with an RGS protein, ends the signal; and phosphorylation of the receptor's C-terminal tail followed by arrestin binding desensitizes it.

## 14.5. Gated Ion Channels

### 14.5.1. Ion Channels Change the Membrane Potential

Excitable cells, neurons, muscle cells, many endocrine and sensory cells, detect a signal, convert it into a change of the membrane potential and pass it on. The changes are produced by gated ion channels ([7.1.13](/7.1.13#sec-13.6.2)).

**Definition 14.5.1 (Gated Ion Channel)** A **gated ion channel** is an ion channel that opens or closes in response to a signal: a **ligand-gated channel** to the binding of an extracellular ligand (a neurotransmitter) or an intracellular one (cAMP, cGMP, IP₃, $\ce{Ca^2+}$, ATP), a **voltage-gated channel** to a change in membrane potential, and others to mechanical force or temperature. A receptor that is itself an ion channel is called **ionotropic**; one that acts through a G protein and second messengers is **metabotropic**.

The **Na⁺/K⁺-ATPase** keeps $\ce{K+}$ high and $\ce{Na+}$ low inside the cell, and the resting membrane is dominated by $\ce{K+}$ channels, so the resting potential is about $-60$ to $-70\,\mathrm{mV}$. By Formula 13.3.1 the direction of spontaneous flow through an open channel follows from the electrochemical gradient of each ion: opening $\ce{Na+}$ or $\ce{Ca^2+}$ channels lets these ions in and depolarizes the cell; opening $\ce{K+}$ channels lets $\ce{K+}$ out, against the electrical gradient but down its much larger concentration gradient, and hyperpolarizes it. For $\ce{Cl-}$ the outcome depends on its internal concentration: in mature neurons its Nernst potential is near or below the resting potential, so opening $\ce{Cl-}$ channels holds the membrane near rest or hyperpolarizes it (inhibition), whereas in immature neurons and in olfactory neurons, which keep more $\ce{Cl-}$ inside, $\ce{Cl-}$ leaves and the cell depolarizes. The number of ions that must cross to change the potential by tens of millivolts is tiny compared with the ions present ([6.3.13](/6.3.13#sec-13.9.1)), so signaling hardly changes the concentrations of $\ce{Na+}$, $\ce{K+}$ and $\ce{Cl-}$; only for $\ce{Ca^2+}$, at $10^{-7}\,\mathrm{M}$ inside, does a brief influx change the concentration enough to act as a messenger.

### 14.5.2. Voltage-Gated Channels and the Action Potential

**Definition 14.5.2 (Voltage-Gated Na⁺ Channel)** The **voltage-gated Na⁺ channel** of neurons and muscle is a single polypeptide of about 2000 residues with four homologous domains (I–IV) arranged around a central pore; each domain has six transmembrane helices (S1–S6). S5, S6 and the loop between them line the pore and form the selectivity filter; S1–S4 form a voltage sensor, in which helix S4 carries a positively charged Arg or Lys at every third position and moves outward when the membrane depolarizes, opening the pore. Within a millisecond a cytoplasmic loop between domains III and IV (the inactivation gate, with the motif Ile–Phe–Met) closes the open pore.

Voltage-gated $\ce{K+}$ channels are tetramers of four separate subunits, each like one domain of the $\ce{Na+}$ channel, with the **selectivity filter** of 13.6.2 of [7.1.13](/7.1.13#sec-13.6.2); voltage-gated $\ce{Ca^2+}$ channels resemble the $\ce{Na+}$ channel. The steep voltage dependence of opening follows from the charge that the sensors move across the field.

**Formula 14.5.1 (Two-State Voltage Gating)** If a channel has a closed and an open state that differ in the gating charge $z_{\mathrm{g}}e$ moved across the membrane, the fraction of open channels at equilibrium follows the **Boltzmann distribution** ([5.2.1](/5.2.1)):

$$
P_{\text{open}}(V) = \frac{1}{1 + \exp\left[-z_{\mathrm{g}}F\left(V - V_{1/2}\right)/RT\right]},
$$
where $V_{1/2}$ is the potential at which half the channels are open.

With about 12–13 elementary charges per channel (the measured gating charge of the Shaker $\ce{K+}$ channel, three to four per voltage sensor), $P_{\text{open}}$ changes e-fold for every $RT/(z_{\mathrm{g}}F) \approx 2\,\mathrm{mV}$, so a depolarization of 10–20 mV switches most channels from closed to open; with a single charge the same change would need about 100 mV. Real channels pass through several closed states, and the steepness and kinetics of their transitions are described by the Hodgkin–Huxley model ([7.16](/7.16)).

The action potential is a wave of such events. A depolarization opens voltage-gated $\ce{Na+}$ channels; $\ce{Na+}$ enters and depolarizes the membrane further, which opens neighboring $\ce{Na+}$ channels, so the depolarization spreads along the axon; the inactivation of $\ce{Na+}$ channels (the refractory period) makes it travel in one direction only; slightly later, voltage-gated $\ce{K+}$ channels open and repolarize the membrane. At the axon terminal the depolarization opens voltage-gated $\ce{Ca^2+}$ channels; the entering $\ce{Ca^2+}$, sensed by the protein synaptotagmin, triggers fusion of synaptic vesicles with the plasma membrane by the **SNARE** machinery ([7.1.13](/7.1.13#sec-13.2.5)), and the neurotransmitter is released into the synaptic cleft.

### 14.5.3. Ligand-Gated Channels: The Nicotinic Acetylcholine Receptor

**Definition 14.5.3 (Nicotinic Acetylcholine Receptor)** The **nicotinic acetylcholine receptor** of the neuromuscular junction is a ligand-gated cation channel, a pentamer of four kinds of subunits ($\alpha_2\beta\gamma\delta$ in the fetus, $\alpha_2\beta\varepsilon\delta$ in the adult) arranged around a central pore lined by one helix (M2) from each subunit. Binding of two acetylcholine molecules, at the interfaces of the α subunits with their neighbors, rotates the subunits and widens the gate formed by a ring of Leu side chains, opening the pore to $\ce{Na+}$, $\ce{K+}$ and $\ce{Ca^2+}$.

Acetylcholine released from a motor neuron opens about a million such channels, each for about a millisecond; the influx of $\ce{Na+}$ depolarizes the muscle membrane, starts an action potential and leads to contraction. Acetylcholinesterase in the cleft, a catalytically perfect enzyme ([7.1.9](/7.1.9#sec-9.1.2)), hydrolyzes the transmitter within milliseconds, so the signal is brief. Related pentameric (Cys-loop) receptors are the serotonin 5-HT₃ receptor, a cation channel, and the glycine and GABA_A receptors, $\ce{Cl-}$ channels that mediate inhibition in the spinal cord and brain (the targets of benzodiazepines and many anesthetics). The ionotropic glutamate receptors (AMPA, NMDA and kainate receptors), which carry most excitatory transmission in the brain, belong to a different, tetrameric family. A neuron receives inputs from many others, some depolarizing and some hyperpolarizing, and fires an action potential only when their sum depolarizes it beyond a threshold: its membrane potential is an integrator in the sense of 14.1.2.

### 14.5.4. Toxins Target Ion Channels

Many of the most potent natural toxins act on ion channels: tetrodotoxin of the puffer fish and saxitoxin of dinoflagellates block voltage-gated $\ce{Na+}$ channels; dendrotoxin of the black mamba blocks voltage-gated $\ce{K+}$ channels; α-bungarotoxin and cobratoxin of snake venoms, and curare, the arrow poison, block the nicotinic acetylcholine receptor; ω-conotoxins of cone snails block $\ce{Ca^2+}$ channels. Channels are the preferred targets because they are amplifiers: a single open channel passes about $10^7$ ions per second, so a neuron needs relatively few channels, and a small number of toxin molecules binding them from outside the cell silences signaling throughout the body, whereas inhibiting a metabolic enzyme, present in far larger amounts, would require many more toxin molecules. Purified toxins became tools: α-bungarotoxin labeled the acetylcholine receptor for its purification, and tetrodotoxin is used to count and silence $\ce{Na+}$ channels.

## Summary

| Structural feature | Chemical property | Biological function |
|---|---|---|
| Receptor **binding site** (Definition 14.1.1) | high affinity, $\theta = [\mathrm{L}]/(K_{\mathrm{d}} + [\mathrm{L}])$; efficacy $\tau$ (Formula 14.1.1) | specificity and sensitivity; agonists, partial agonists, competitive antagonists (Definition 14.1.2); spare receptors, $\mathrm{EC}_{50} = K_{\mathrm{A}}/(1 + \tau)$ |
| Seven transmembrane helices (Definition 14.2.1) | ligand binding moves helix 6, exposing the G-protein site; the receptor is a GEF (Definition 14.2.3) | ~800 human GPCRs; about a third of drugs |
| Heterotrimeric G protein (Definition 14.2.2) | Gα·GDP inactive, Gα·GTP active; intrinsic GTPase, accelerated by RGS (GAP) | self-limiting switch; classes Gs, Gi/o, Gq, G12/13 (14.2.5); cholera and pertussis toxins |
| Adenylyl cyclase, PDE (Definition 14.2.5) | ATP → cAMP; cAMP → 5′-AMP; $\mathrm{d[cAMP]/d}t = k_{\mathrm{AC}}a - k_{\mathrm{PDE}}[\mathrm{cAMP}]$ (Formula 14.2.1) | second messenger (Definition 14.2.4); PDE sets level and speed |
| PKA $\mathrm{R_2C_2}$ (Definition 14.2.6) | 4 cAMP release 2 C; consensus RRXS/T; CREB in the nucleus | glycogen breakdown (phosphorylase kinase → phosphorylase), gene expression |
| Catalytic cascade | gains multiply, $G = \prod g_i$ | amplification by up to $10^8$ (14.2.3) |
| GRK and arrestin (Definition 14.2.7) | phosphorylation of the receptor tail, arrestin binding, endocytosis | desensitization; arrestin signaling, biased agonism |
| AKAPs (Definition 14.2.8), rafts | scaffolds holding PKA, AC, PDE, phosphatases | local, brief cAMP signals |
| PLC, IP₃, DAG (Definition 14.3.1); PKC (Definition 14.3.2) | PIP₂ → IP₃ (opens ER Ca²⁺ channel) + DAG; DAG + Ca²⁺ + PS activate PKC | Gq signaling; phorbol esters as tumor promoters |
| Ca²⁺ gradient; calmodulin (Definition 14.3.3) | cytosol 0.1 µM vs 1 mM outside; four EF hands, $K_{\mathrm{d}} \approx 1\,\mu\mathrm{M}$ | contraction, secretion, CaM kinases; oscillations encode frequency |
| Guanylyl cyclases, PKG (Definition 14.3.4) | receptor GC (ANF, guanylin) and NO-activated soluble GC; PDE5 | vasodilation, natriuresis; nitroglycerin, sildenafil |
| Rhodopsin and transducin (Definition 14.4.1) | 11-cis → all-trans retinal; PDE6 lowers cGMP; CNG channels close | single-photon detection, Ca²⁺ feedback (GCAPs), color vision |
| Odorant and taste receptors | Golf–cAMP–CNG; gustducin–PLCβ2–TRPM5 | combinatorial coding of smell; sweet, umami, bitter |
| Gated channels (Definition 14.5.1); Na⁺ channel (Definition 14.5.2) | S4 voltage sensor, $P_{\text{open}}$ Boltzmann in $V$ with $z_{\mathrm{g}} \approx 12$ (Formula 14.5.1); inactivation gate | action potential; Ca²⁺-triggered transmitter release |
| Nicotinic ACh receptor (Definition 14.5.3) | pentamer, two ACh open a cation pore | neuromuscular transmission; toxins (bungarotoxin, curare, TTX) |

| Quantity | Value |
|---|---|
| Receptor $K_{\mathrm{d}}$ for hormones | ≤ 10⁻⁷ M (often nM) |
| Human GPCRs; olfactory receptors | ~800; ~400 functional |
| Protein kinases / phosphatases in the human genome | ~540 / ~190 |
| Cytosolic [Ca²⁺] at rest / stimulated | ~0.1 / ~1 µM |
| Resting potential; rod in the dark | −60 to −70 mV; about −40 mV |
| Rhodopsin absorption maximum; cones S, M, L | 500 nm; 420, 530, 560 nm |
| Gating charge of a voltage-gated K⁺ channel | about 12–13 e |
| Ion flux through one open channel | ~10⁷ s⁻¹ |

## Questions

1. In Sutherland's experiments, epinephrine added to a liver homogenate activated glycogen phosphorylase, but not when it was added to the supernatant after high-speed centrifugation. The particulate fraction treated with epinephrine produced a substance X that activated phosphorylase in the supernatant; X was heat-stable and identical to a compound obtained by treating ATP with barium hydroxide. Interpret these observations.

   **Answer** The receptor and adenylyl cyclase are in the plasma membrane, which sediments with the particulate fraction; the supernatant contains PKA, phosphorylase kinase and phosphorylase but no receptor, so epinephrine alone does nothing to it. The membranes, stimulated by epinephrine, make the second messenger X, which then activates the soluble cascade. A heat-stable small molecule identical to a product of ATP is cAMP (barium hydroxide cyclizes ATP to the 3′,5′-cyclic phosphate); heat stability rules out a protein.

2. Adding cAMP to intact cells has little effect, but its derivative dibutyryl cAMP mimics the effects of epinephrine. Why?

   **Answer** cAMP is charged (a phosphodiester anion) and polar, so it crosses the plasma membrane very poorly ([7.1.13](/7.1.13#sec-13.3.2)); in addition it is quickly hydrolyzed by phosphodiesterases. The two butyryl groups (on the N⁶ amino group and the 2′-OH) make dibutyryl cAMP more hydrophobic, so it enters cells, where esterases remove the butyryl groups (giving active cAMP or N⁶-butyryl-cAMP, which also activates PKA), and the analog resists PDE.

3. An agonist binds its receptor with $K_{\mathrm{A}} = 100\,\mathrm{nM}$ and produces a half-maximal response at 2 nM. Estimate its efficacy $\tau$, the fraction of receptors occupied at the $\mathrm{EC}_{50}$, and the maximal response relative to the system maximum. If a competitive antagonist with $K_{\mathrm{B}} = 1\,\mathrm{nM}$ is present at 9 nM, what $\mathrm{EC}_{50}$ will be measured?

   **Answer** By Formula 14.1.1, $\mathrm{EC}_{50} = K_{\mathrm{A}}/(1 + \tau)$, so $1 + \tau = 50$, $\tau = 49$. At 2 nM the occupancy is $2/(100 + 2) \approx 2\%$: there are many spare receptors. The maximal response is $\tau/(1 + \tau) = 98\%$ of the system maximum. The antagonist multiplies the effective $K_{\mathrm{A}}$ by $r = 1 + 9/1 = 10$, so $\mathrm{EC}_{50} = 20\,\mathrm{nM}$, and the maximum is unchanged.

4. Which steps of the β-adrenergic pathway amplify the signal, which terminate it, and which do both? (a) One Gsα activates one adenylyl cyclase; (b) one PKA catalytic subunit phosphorylates many targets; (c) the GTPase of Gα; (d) phosphodiesterase acts on many cAMP; (e) one epinephrine molecule activates one receptor, which activates many Gs.

   **Answer** Amplification: (b) and (e) (many substrate molecules per catalyst); (a) does not amplify (1:1), although the cyclase it activates does, by making many cAMP. Termination: (c) and (d). The GTPase also sets the amplification, because the longer Gα·GTP lives, the more cAMP each cyclase makes; it thus both limits and shapes the signal. Phosphodiesterase terminates it; by setting $k_{\mathrm{PDE}}$ it also determines the steady level (Formula 14.2.1).

5. Cholera toxin and pertussis toxin both raise cAMP in their target cells. Explain the two mechanisms. Why do cholera patients survive with oral glucose–salt solutions?

   **Answer** Cholera toxin ADP-ribosylates an Arg residue of $\mathrm{G_{s\alpha}}$ required for GTP hydrolysis, so the stimulatory G protein stays active and adenylyl cyclase is continuously stimulated. Pertussis toxin ADP-ribosylates a Cys residue near the C-terminus of $\mathrm{G_{i\alpha}}$, preventing its activation by receptors, so the inhibition of adenylyl cyclase is lost. In cholera, high cAMP opens CFTR and causes massive secretion of $\ce{Cl-}$, $\ce{Na+}$ and water; the Na⁺–glucose symporter SGLT1 of the intestinal epithelium is not affected, so glucose given with salt is absorbed together with $\ce{Na+}$, and water follows osmotically, replacing the losses.

6. A person with Oguchi disease, an inherited night blindness, recovers vision only slowly after a bright flash. Suggest a molecular defect, and explain the symptom. What would you expect in a rod treated with a membrane-permeant, PDE-resistant cGMP analog?

   **Answer** Recovery of the rod requires shutoff of R*, which depends on phosphorylation by rhodopsin kinase (GRK1) and binding of arrestin 1; Oguchi disease is indeed caused by mutations in the genes for arrestin (SAG) or rhodopsin kinase (GRK1). R* then stays active for a long time after a flash, keeping PDE6 active and the channels closed, so the rods remain saturated and dark adaptation is very slow. With a permeant, PDE-resistant cGMP analog the CNG channels stay open whatever PDE does: the rod stays depolarized and does not respond to light.

7. Ca²⁺ in the cytosol is about 0.1 µM, extracellular Ca²⁺ is 1.5 mM, and the resting potential is −70 mV. Calculate the free energy available per mole of Ca²⁺ entering through a channel at 37 °C, and explain why a brief influx raises cytosolic Ca²⁺ several-fold while Na⁺ influx through Na⁺ channels changes [Na⁺] negligibly.

   **Answer** $\Delta G_{\mathrm{t}}$ for entry $= RT\ln(10^{-7}/1.5\times10^{-3}) + 2F(-0.070\,\mathrm{V}) = 2.58\times(-9.6) - 13.5 = -24.8 - 13.5 \approx -38\,\mathrm{kJ\,mol^{-1}}$, a very large driving force. Because cytosolic $\ce{Ca^2+}$ is only $10^{-7}\,\mathrm{M}$, the entry of even a tiny amount (a few micromolar, mostly captured by buffers) changes the free concentration several-fold, whereas the $10\,\mathrm{mM}$ of $\ce{Na+}$ inside a cell is hardly changed by the number of ions needed to depolarize the membrane by 100 mV (of the order of $10^{-6}$ of the ions present, [6.3.13](/6.3.13#sec-13.9.1)).

8. (Open question) Using Formula 14.5.1, estimate by how much the open probability of a voltage-gated channel with $z_{\mathrm{g}} = 12$ and $V_{1/2} = -40\,\mathrm{mV}$ changes between −70 mV and −50 mV at 37 °C, and compare a hypothetical channel with $z_{\mathrm{g}} = 1$. What does this imply for the threshold behavior of the action potential?

   **Answer** $F/RT = 1/(26.7\,\mathrm{mV})$. For $z_{\mathrm{g}} = 12$: at −70 mV, $P = 1/(1 + \mathrm{e}^{12\times30/26.7}) = 1/(1 + \mathrm{e}^{13.5}) \approx 1.4\times10^{-6}$; at −50 mV, $P = 1/(1 + \mathrm{e}^{12\times10/26.7}) = 1/(1 + \mathrm{e}^{4.5}) \approx 0.011$, an increase of almost $10^4$-fold for 20 mV. For $z_{\mathrm{g}} = 1$: $P$ goes from $1/(1 + \mathrm{e}^{1.12}) = 0.25$ to $1/(1 + \mathrm{e}^{0.37}) = 0.41$, less than twofold. The steep voltage dependence means that the $\ce{Na+}$ current is negligible at rest but grows explosively once a small depolarization opens a few channels whose current depolarizes the membrane further: a positive feedback with a sharp threshold, which the Hodgkin–Huxley model ([7.16](/7.16)) analyzes quantitatively.
