---
title: Pattern Recognition and Innate Immune Signaling
source_hash: 982993f142d1
---

The previous chapter introduced the cells of innate immunity; this chapter answers how they "see" pathogens, the innate part of question 1 on the knowledge path and also the starting point of question 2 (how the decision is made): what activates the pattern recognition receptors determines which cytokines are produced and thereby whether the subsequent adaptive response goes toward type 1, 2, or 3. The **pattern recognition receptors** and **interferon** response within virus-infected cells were covered in [7.11.27](/7.11.27); here we build on that, putting all receptor families together to compare their localization, ligands, and signaling and to discuss their common downstream. The cell biology of the **inflammasome** and **pyroptosis** is in [7.3.25](/7.3.25), and the **NF-κB** pathway and its oscillations are in [7.3.19](/7.3.19) and [7.9.16](/7.9.16). The next chapter describes the inflammation and effector functions that these signals trigger.

## 6.1. The Logic of Innate Recognition

### 6.1.1. What Is Recognized: PAMPs and DAMPs

In 1989 Janeway proposed that because the receptors of adaptive immunity are generated at random and cannot by themselves judge whether an antigen comes from a pathogen, there must be a set of germline-encoded receptors specialized to recognize molecular structures unique to microbes and absent from the host, thereby "licensing" the adaptive response. He called these structures **pathogen-associated molecular patterns** (PAMPs) and the receptors that recognize them pattern recognition receptors (PRRs). The molecules chosen as "patterns" share common features: they are shared by a large class of microbes, are essential for microbial survival and therefore hard to remove by mutation, and are absent from the host or present in a different form or in a different place.

| PAMP | Microbe | Main receptors |
|---|---|---|
| **Lipopolysaccharide** (lipid A portion) | Outer membrane of gram-negative bacteria | TLR4–MD-2; cytosolic caspase-4/5/11 |
| Lipoproteins, lipopeptides | Bacteria, mycoplasma | TLR2–TLR1 (triacylated), TLR2–TLR6 (diacylated) |
| **Peptidoglycan** fragments | Bacterial cell wall | NOD1 (fragments containing meso-DAP), NOD2 (muramyl dipeptide) |
| Lipoteichoic acid | Gram-positive bacteria | TLR2 |
| *Flagellin* | Flagellated bacteria | TLR5; cytosolic NAIP–NLRC4 |
| Unmethylated CpG DNA | Bacterial and viral DNA | TLR9 (endosome) |
| Double-stranded RNA | Replication intermediate of most viruses | TLR3 (endosome), MDA5 (cytosol) |
| Single-stranded RNA (GU-rich) | RNA viruses | TLR7, TLR8 (endosome) |
| Short double-stranded RNA with 5′-triphosphate | RNA viruses | RIG-I (cytosol) |
| Cytosolic double-stranded DNA | DNA viruses, retroviruses, intracellular bacteria | cGAS; AIM2 |
| β-Glucan, mannan | Fungi | Dectin-1, dectin-2, mannose receptor |

How does the host avoid recognizing its own nucleic acids? The key lies not in the molecules themselves but in their location and modification: TLR3, 7, 8, and 9 are found only in endosomes, which self nucleic acid does not normally reach; host mRNA has a 5′ cap and 2′-O-methylation, and there is normally no free DNA in the cytosol; CpG in bacterial DNA is unmethylated whereas most CpG in mammalian DNA is methylated.

The "danger model" proposed by Matzinger in 1994 emphasized the other side: the immune system distinguishes not only self from nonself but also "safe" from "dangerous". Endogenous molecules released by damaged or necrotic cells, **damage-associated molecular patterns** (DAMPs), can likewise activate PRRs and cause sterile inflammation.

| DAMP | Source | Receptor |
|---|---|---|
| HMGB1 | Nuclear protein of necrotic cells | TLR2, TLR4, RAGE |
| Extracellular ATP | Damaged cells | P2X7 (activates NLRP3) |
| Uric acid crystals, cholesterol crystals | Gout, atherosclerosis | NLRP3 |
| Mitochondrial DNA, N-formyl peptides | Released mitochondrial components (of bacterial origin) | TLR9, cGAS; formyl peptide receptors |
| Heat shock proteins, S100 proteins | Stressed cells | TLR2, TLR4 |
| IL-33, IL-1α ("alarmins") | Necrotic epithelial and endothelial cells | ST2, IL-1R1 |

### 6.1.2. Who Recognizes: Localization of Receptors

The distribution of PRRs corresponds one to one with the places where pathogens may appear, forming a "surveillance map":

| Location | Receptors | What is monitored |
|---|---|---|
| Plasma membrane | TLR1, 2, 4, 5, 6; C-type lectin receptors; scavenger receptors | Surface components of extracellular bacteria and fungi |
| Endosomes and lysosomes | TLR3, 7, 8, 9 | Nucleic acids released by engulfed pathogens |
| Cytosol | RIG-I-like receptors (RNA); cGAS, AIM2 (DNA); NOD-like receptors (bacterial components, cell stress) | Viruses and intracellular bacteria that enter the cytosol to replicate |
| Extracellular fluid | Mannose-binding lectin, ficolins, C-reactive protein, surfactant proteins | Microbes in blood and body fluids (activate complement, opsonize) |

Compared with the antigen receptors of adaptive immunity, PRRs have four characteristics: they are encoded by germline genes and need no rearrangement; they are constitutively expressed on many cell types (not only immune cells but also epithelial cells and fibroblasts) and need no clonal expansion; signaling begins within minutes of binding; and each receptor recognizes a large class of microbes, and their number is limited (about a hundred PRRs are known in humans).

![Localization and signaling of pattern recognition receptors (schematic). Plasma membrane TLRs (TLR4 as example) activate NF-κB via MyD88; internalized TLR4 and endosomal TLR3 activate IRF3 via TRIF; endosomal TLR7 and TLR9 activate IRF7 via MyD88 (especially prominent in plasmacytoid dendritic cells); cytosolic RIG-I and MDA5, after binding viral RNA, signal via MAVS on mitochondria, and cGAS, after binding DNA and producing cGAMP, signals via STING on the endoplasmic reticulum, both activating TBK1 and IRF3; NOD1 and NOD2 activate NF-κB via RIPK2; NLRP3 and others assemble inflammasomes that activate caspase-1. NF-κB in the nucleus induces inflammatory cytokines, and IRF3 and IRF7 induce type I interferons. Arrows are SBGN stimulation arrows: open arrowheads indicate activation](./plots/prr-map.py)

## 6.2. Toll-Like Receptors

### 6.2.1. Discovery and Structure

The *Toll* gene was first discovered in studies of the dorsoventral axis of the *Drosophila* embryo. In 1996 Lemaitre and Hoffmann found that *Toll* mutant flies die rapidly after fungal infection because they cannot induce the antifungal peptide drosomycin. The next year Medzhitov and Janeway cloned the human homolog and showed that it can activate NF-κB and the expression of costimulatory molecules; in 1998 Beutler's laboratory found that the mutation in the C3H/HeJ mouse, which does not respond to lipopolysaccharide, lies precisely in the *Tlr4* gene, for the first time identifying the ligand of a mammalian PRR.

**Definition 6.2.1 (Toll-Like Receptor)** **Toll-like receptors** (TLRs) are type I transmembrane pattern recognition receptors: the extracellular region consists of leucine-rich repeats forming a horseshoe-shaped ligand-binding domain, and the cytoplasmic region is the Toll/IL-1 receptor homology domain (TIR domain); ligand binding causes two receptors to form a dimer, and the cytoplasmic TIR domains come together and recruit TIR-containing adaptor proteins, initiating signaling.

Humans have 10 functional TLRs (TLR1–10; TLR10 is specific to humans, and mice have TLR11–13 in addition). Their TIR domains are the same as those of the IL-1 receptor and IL-18 receptor, so these two classes of receptors share most of the signaling machinery ([7.15.11](/7.15.11)).

### 6.2.2. Localization, Ligands, and Adaptors

| TLR | Localization | Ligands | Adaptor | Main output |
|---|---|---|---|---|
| TLR2/TLR1, TLR2/TLR6 | Plasma membrane | Triacylated / diacylated lipopeptides, lipoteichoic acid, zymosan | TIRAP–MyD88 | Inflammatory cytokines |
| TLR4 (with MD-2, aided by CD14) | Plasma membrane, then endosome | Lipopolysaccharide | Plasma membrane: TIRAP–MyD88; endosome: TRAM–TRIF | Inflammatory cytokines; type I interferons |
| TLR5 | Plasma membrane | Flagellin | MyD88 | Inflammatory cytokines |
| TLR3 | Endosome | Double-stranded RNA | TRIF | Type I interferons, inflammatory cytokines |
| TLR7, TLR8 | Endosome | Single-stranded RNA; imidazoquinoline drugs | MyD88 | Type I interferons (pDC), inflammatory cytokines |
| TLR9 | Endosome | Unmethylated CpG DNA | MyD88 | Type I interferons (pDC), inflammatory cytokines |

Endosomal TLRs need the chaperone UNC93B1 for transport and become active only after being cleaved by proteases in the endosome, which ensures that they work only where endocytosed material has been degraded and nucleic acids are exposed.

### 6.2.3. Signaling: MyD88 and TRIF

**Definition 6.2.2 (MyD88)** **MyD88** is a cytoplasmic adaptor protein containing a TIR domain and a death domain; it is recruited by all TLRs except TLR3 and by the IL-1 receptor and IL-18 receptor, and through its death domain it aggregates IRAK family kinases, forming the common pathway by which these receptors activate NF-κB.

The MyD88 branch: the activated receptor recruits MyD88, which assembles with IRAK4 and IRAK1/2 into a helical oligomeric complex (the Myddosome); IRAK activates the ubiquitin ligase TRAF6, which synthesizes K63-linked polyubiquitin chains that serve as a scaffold to recruit and activate the kinase TAK1; TAK1 phosphorylates the IKK complex (IKKα, IKKβ, and the regulatory subunit NEMO), and IKK phosphorylates **IκB**, which is ubiquitinated and degraded by the **proteasome**, releasing NF-κB to enter the nucleus; TAK1 simultaneously activates MAPKs such as p38 and JNK, which in turn activate the transcription factor AP-1. Together they induce TNF, pro-IL-1β, IL-6, IL-12, and chemokines.

The TRIF branch: TLR3 directly, and TLR4 (after endocytosis, via the adaptor TRAM), recruit TRIF; TRIF activates the kinases TBK1 and IKKε via TRAF3, and these phosphorylate the transcription factor IRF3, which dimerizes and enters the nucleus to induce IFN-β; TRIF also activates NF-κB somewhat later via RIPK1.

**Definition 6.2.3 (Interferon Regulatory Factor)** **Interferon regulatory factors** (IRFs) are a family of transcription factors (IRF1–9 in humans) with a conserved DNA-binding domain that bind interferon-stimulated response elements; among them IRF3 and IRF7, after being phosphorylated by TBK1, IKKε, or IRAK1 in PRR signaling, induce type I interferons, IRF9 is a component of the transcription complex downstream of the type I interferon receptor, and IRF4, IRF5, and IRF8 take part in the differentiation of immune cells and the expression of inflammatory cytokines.

TLR4 is the only receptor that uses both branches: it first rapidly activates NF-κB via MyD88 at the plasma membrane and, after being endocytosed with the help of CD14, activates IRF3 via TRIF, so lipopolysaccharide both causes strong inflammation and induces IFN-β. TLR7 and TLR9 in plasmacytoid dendritic cells take a third route: MyD88–IRAK4–IRAK1 directly phosphorylates the constitutively highly expressed IRF7, making pDCs the main source of IFN-α in viral infection, with a yield up to a thousand times that of ordinary cells.

## 6.3. Cytosolic Nucleic Acid Sensors

TLRs monitor the extracellular space and endosomes; viruses replicating in the cytosol must be detected by two other sets of receptors.

### 6.3.1. RIG-I-Like Receptors

**Definition 6.3.1 (RIG-I-Like Receptor)** **RIG-I-like receptors** (RLRs) are cytosolic RNA helicases comprising RIG-I, MDA5, and LGP2; after RIG-I and MDA5 bind viral RNA, their two N-terminal CARD domains bind the adaptor protein MAVS on the outer mitochondrial membrane, activating TBK1–IRF3 and NF-κB and inducing type I and type III interferons.

RIG-I recognizes short RNA bearing a 5′-triphosphate (or diphosphate) and a double-stranded end, a feature of the genomes of many negative-strand RNA viruses (influenza virus, paramyxoviruses), whereas host mRNA is capped; MDA5 forms filamentous polymers along long double-stranded RNA and mainly recognizes the long double-stranded RNA produced during the replication of positive-strand viruses such as picornaviruses. Once activated, MAVS likewise polymerizes into prion-like fibers that amplify the signal. LGP2 lacks CARD domains and regulates the other two.

### 6.3.2. The cGAS–STING Pathway

**Definition 6.3.2 (cGAS–STING Pathway)** Cytosolic cyclic GMP–AMP synthase (cGAS) is activated on binding double-stranded DNA and synthesizes the second messenger 2′3′-cyclic GMP–AMP (cGAMP) from ATP and GTP; cGAMP binds the endoplasmic reticulum membrane protein STING, which then moves from the endoplasmic reticulum to the Golgi apparatus and recruits TBK1 to phosphorylate IRF3, inducing type I interferons. This pathway sensing cytosolic DNA is called the **cGAS–STING pathway**.

STING was discovered in 2008, and cGAS was identified by Zhijian Chen's laboratory in 2013. The recognition of DNA by cGAS depends not on sequence but on length: longer DNA lets multiple cGAS dimers line up along the DNA in a ladder, sharply raising activity, so short DNA fragments do not readily cause a response. cGAMP can also be passed to neighboring cells through gap junctions or packaged into virus particles, bringing uninfected cells into an antiviral state as well.

The cell's own DNA is normally confined to the nucleus and mitochondria but appears in the cytosol in several situations: mitochondrial DNA released when mitochondria are damaged, rupture of micronuclei formed by chromosome missegregation, and cDNA of retroelements. This makes cGAS–STING a sensor of both cell damage and genomic instability: micronuclei of tumor cells can cause an interferon response via cGAS–STING and take part in antitumor immunity ([7.15.30](/7.15.30)); the inflammatory secretory phenotype of senescent cells also arises partly from this pathway ([7.3.25](/7.3.25)). When the exonuclease TREX1, which degrades cytosolic DNA, is deficient, self DNA accumulates and continuously activates cGAS–STING, causing Aicardi–Goutières syndrome, characterized by excessive type I interferon.

## 6.4. NOD-Like Receptors and Inflammasomes

**Definition 6.4.1 (NOD-Like Receptor)** The family of cytosolic pattern recognition receptors characterized by a central nucleotide-binding oligomerization domain (NOD, also called the NACHT domain) and C-terminal leucine-rich repeats is called **NOD-like receptors** (often abbreviated NLR; there are 22 in humans), and their N-terminal effector domains (CARD, pyrin domain, and others) determine downstream signaling.

NOD-like receptors resemble plant disease resistance proteins in structure (both have a nucleotide-binding domain and LRRs), but the two arose by convergent evolution. Animal NOD-like receptors fall into two functional classes:

- NOD1 and NOD2 recognize **peptidoglycan** fragments released from the bacterial cell wall, recruit the kinase RIPK2 via their CARD domains, and activate NF-κB and MAPKs, inducing inflammatory cytokines and antimicrobial peptides. Loss-of-function mutations in NOD2 are among the most important genetic risk factors for Crohn's disease, suggesting its role in maintaining the intestinal barrier and the balance of the flora.
- NLRP3, NLRC4, and others, when activated, assemble into **inflammasomes**: the receptor oligomerizes and recruits and activates caspase-1 through the adaptor protein ASC.

The inflammasome has two outputs: caspase-1 cleaves inactive pro-IL-1β and pro-IL-18 into mature cytokines; it also cleaves gasdermin D, whose N-terminal fragment forms pores in the plasma membrane through which mature IL-1β is released, and the cell then swells and bursts, which is **pyroptosis** (compare perforin and the membrane attack complex in [7.15.5](/7.15.5)).

Activation of NLRP3 requires two signals, a "double confirmation" that prevents false activation:

1. Priming signal: TLRs or TNF receptors induce the expression of NLRP3 and pro-IL-1β through NF-κB.
2. Activation signal: a variety of seemingly unrelated stimuli, including extracellular ATP (via the P2X7 channel), pore-forming toxins, and particles such as uric acid crystals and silica (which rupture lysosomes), have in common the efflux of intracellular $\ce{K+}$, which triggers NLRP3 oligomerization.

Other inflammasomes have their own specialized ligands: NAIP–NLRC4 recognizes bacterial flagellin and type III secretion system proteins, AIM2 recognizes cytosolic double-stranded DNA, and pyrin senses the "consequence" of bacterial toxins inactivating RhoA rather than the toxins themselves. Human caspase-4 and caspase-5 (caspase-11 in mice) directly bind lipopolysaccharide that has entered the cytosol and cause "noncanonical" pyroptosis. Gain-of-function mutations of NLRP3 cause periodic fever and systemic inflammation (cryopyrin-associated periodic syndromes), and gout attacks result from the activation of NLRP3 by uric acid crystals; both can be treated with drugs that block IL-1.

## 6.5. Other Pattern Recognition Receptors

| Class | Representatives | Ligands | Signaling and function |
|---|---|---|---|
| C-type lectin receptors | Dectin-1 | β-1,3-Glucan of the fungal cell wall | Activates NF-κB via Syk–CARD9, induces IL-23 and IL-6, and drives antifungal Th17 responses; individuals with *CARD9* deficiency are prone to severe fungal infection |
| | Dectin-2, mincle | Mannan; trehalose dimycolate of mycobacteria | Signal via FcRγ–Syk |
| | Mannose receptor (CD206), DC-SIGN (CD209) | Glycans terminating in mannose or fucose | Endocytosis and antigen uptake |
| Scavenger receptors | SR-A, MARCO, CD36 | Modified lipoproteins, bacterial components, apoptotic cells | Phagocytosis and clearance; assist TLRs |
| Soluble PRRs | Mannose-binding lectin, ficolins | Sugars on microbial surfaces | Activate the lectin pathway of complement ([7.15.10](/7.15.10)) |
| | Pentraxins: C-reactive protein, serum amyloid P, PTX3 | Phosphorylcholine, microbial surfaces | Opsonization, activation of the classical pathway; CRP is an acute-phase protein ([7.15.7](/7.15.7)) |
| | Collectins: SP-A, SP-D | Microbes in the lung | Agglutination and opsonization |

Soluble PRRs are the "innate immunity of the body fluids": like antibodies they bind pathogen surfaces, activate complement, and promote phagocytosis, except that they recognize conserved sugars and lipids rather than specific epitopes.

## 6.6. The Common Downstream: From Receptor to Gene

### 6.6.1. Three Classes of Transcription Factors and Three Classes of Output

Despite the diversity of receptors, signals finally converge on a few transcription factors:

| Transcription factor | Upstream | Main output | Function |
|---|---|---|---|
| NF-κB | MyD88–IRAK–TRAF6 (TLR, IL-1R), RIPK2 (NOD1/2), TNF receptors, C-type lectin receptors | TNF, pro-IL-1β, IL-6, IL-12, chemokines; NLRP3; costimulatory molecules | Inflammation and activation of immune cells |
| AP-1 (via MAPK) | Same | Cooperates with NF-κB | |
| IRF3, IRF7 | TRIF, MAVS, STING (via TBK1); MyD88–IRF7 (pDC) | IFN-β, IFN-α, IFN-λ; some chemokines | Antiviral state |

After secretion, type I interferons act on the interferon receptor (IFNAR) of the cell itself and of neighboring cells and, through the **JAK–STAT pathway** (JAK1 and TYK2 phosphorylate STAT1 and STAT2, which together with IRF9 form ISGF3), induce hundreds of **interferon-stimulated genes** that bring the cell into an antiviral state ([7.11.27](/7.11.27)). Type I interferons also enhance the expression of MHC class I molecules and the activity of NK cells and promote the maturation and cross-presentation of dendritic cells, linking innate recognition to adaptive immunity.

### 6.6.2. Receptor Combinations Determine the Type of Response

When different combinations of receptors on the same dendritic cell are activated, the cytokine profile produced differs, which is how innate immunity "determines" the direction of the adaptive response ([7.15.1](/7.15.1)):

| Pathogen recognized | Main PRRs activated | Output of the dendritic cell | T-cell tendency |
|---|---|---|---|
| Viruses, intracellular bacteria | TLR3, 7, 9; RLR; cGAS–STING | IL-12, type I interferons | Th1, CTL (type 1) |
| Extracellular bacteria, fungi | TLR2, TLR4, TLR5; dectin-1; NOD2; NLRP3 | IL-6, IL-1β, IL-23, TGF-β | Th17 (type 3) |
| Helminths, allergens | IL-25, IL-33, TSLP released by epithelium; a few C-type lectin receptors | Low IL-12; OX40L | Th2 (type 2) |

The strength and duration of signals are also under negative feedback control: NF-κB induces its inhibitors IκBα and the deubiquitinase A20, so that signaling subsides or oscillates within tens of minutes to hours ([7.9.16](/7.9.16)); interferon signaling induces SOCS proteins and USP18, limiting the duration of the interferon response. Defects in these negative feedbacks lead to persistent inflammation or "interferonopathies".

### 6.6.3. A Model: Positive Feedback and Bistability of Interferon

The interferon response has an important positive feedback: viral infection first induces a small amount of IFN-β via IRF3; IFN-β induces IRF7 via IFNAR (IRF7 is itself an interferon-stimulated gene); IRF7 is in turn activated by viral signals and induces large amounts of IFN-α and IFN-β. The positive feedback gives the response an "all-or-none" character.

**Example 6.6.1** A dimensionless single-variable model summarizes this circuit: let $x$ be the interferon output driven by IRF7 in a cell and $s$ the input produced by viral sensing (the IRF3 pathway),

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = s + \alpha\,\frac{x^{n}}{K^{n} + x^{n}} - \delta x ,
$$

where the second term is the positive feedback via IFNAR–IRF7 (the Hill coefficient $n$ expresses cooperativity, since both the induction and activation of IRF7 require several steps) and $\delta x$ is the degradation of interferon and the decay of signaling. The steady states are given by the intersections of the production curve $s + \alpha x^n/(K^n + x^n)$ with the degradation line $\delta x$ ([2.4.11](/2.4.11)). Take $n = 2$, $\alpha = 1$, $K = 0.4$, $\delta = 1$: when $s = 0$ there are three intersections, $x = 0$ (stable, resting), $x = 0.2$ (an unstable threshold), and $x = 0.8$ (stable, high), that is, the system is **bistable**. If a brief viral stimulus pushes $x$ past the middle threshold, $x$ remains at the high value after the stimulus is withdrawn, and the cell "remembers" the infection and maintains the antiviral state; if the stimulus is too weak, the system returns to rest. As $s$ increases, the low steady state disappears at $s \approx 0.04$ (a saddle-node bifurcation), so the transition from rest to activation is abrupt and shows hysteresis.

:::

![Bistable model of interferon positive feedback (Example 6.6.1, dimensionless illustrative parameters $n = 2$, $\alpha = 1$, $K = 0.4$, $\delta = 1$). A: rate-balance plot at $s = 0$; the sigmoidal production curve and the degradation line $\delta x$ have three intersections: two stable states (filled circles) and the unstable threshold between them (open circle). B: viral input $s$ of different strengths (0.05, 0.12, 0.15) applied from $t = 2$ to $t = 4$; after a weaker stimulus is withdrawn $x$ returns to rest, whereas a strong stimulus drives $x$ across the threshold and it stays in the high state after the stimulus is withdrawn. C: the steady state $x^*$ as a function of the input $s$ (bifurcation diagram), with solid lines for stable and dashed lines for unstable steady states; as $s$ increases, the low state disappears at the saddle-node bifurcation at $s \approx 0.04$ and the system jumps to the high state. In real cells negative feedbacks such as SOCS and USP18 eventually bring the high state back down, so this "memory" is temporary](./plots/ifn-bistability.py)

The form of this model is the same as that of the general model of positive-feedback switches in [7.9.16](/7.9.16), and it helps to understand two phenomena: the interferon response is often "on or off" at the single-cell level (in single-cell measurements only some infected cells produce interferon); and a sufficiently strong signal can keep the cell in a defensive state before the pathogen is cleared.

## 6.7. Trained Immunity

The traditional view held that innate immunity has no memory. But epidemiological observations of BCG vaccination and animal experiments both show that certain stimuli can cause innate immune cells to respond more strongly to unrelated pathogens over the following weeks to months.

**Definition 6.7.1 (Trained Immunity)** The non-specific "innate immune memory" in which innate immune cells (monocytes, macrophages, NK cells) and their progenitors in the bone marrow, after an initial exposure to certain stimuli (such as fungal β-glucan or BCG), undergo epigenetic and metabolic reprogramming and respond more strongly when later exposed to the same or different stimuli is called **trained immunity**.

| | Trained immunity | Adaptive immune memory |
|---|---|---|
| Cells | Monocytes, macrophages, NK cells; hematopoietic progenitors in the bone marrow | T and B cells |
| Specificity | None: enhances responses to many pathogens | High: directed against the same antigen |
| Mechanism | Histone modifications (H3K4me3, H3K27ac) at promoters and enhancers place inflammatory genes in a "poised" state; metabolic reprogramming with aerobic glycolysis (mTOR–HIF-1α), glutamine replenishment, and the mevalonate pathway | Clonal expansion; rearrangement and somatic mutation of receptor genes |
| Duration | Weeks to months; more than a year when acting on bone marrow progenitors | Years to lifelong |

The converse of trained immunity is "tolerance": after macrophages receive a high dose of lipopolysaccharide, their response to restimulation is weakened for a period (endotoxin tolerance), which is associated with the immunosuppression of the late phase of sepsis. The two show that the state of innate immune cells is likewise shaped by "experience".

## 6.8. Tolerance of Self Nucleic Acids and Pathogen Evasion

The precision of pattern recognition derives from three safeguards, "location, modification, and clearance": endosomal TLRs can contact only nucleic acids exposed after degradation, and there is normally no DNA in the cytosol; host RNA carries modifications such as the cap structure, 2′-O-methylation, and N6-methyladenosine and is not recognized by RIG-I and TLR7 (which is also why **mRNA vaccines** substitute pseudouridine for uridine to reduce innate immune stimulation); and the nucleases TREX1, DNase II, and RNase H2 promptly degrade surplus nucleic acid. Failure of any one safeguard leads to recognition of self nucleic acids: besides Aicardi–Goutières syndrome, in systemic lupus erythematosus immune complexes carry self nucleic acids into the endosomes of pDCs, where TLR7 and TLR9 cause sustained type I interferon production, one of the core mechanisms of the disease ([7.15.28](/7.15.28)).

Pathogens in turn have evolved countermeasures against each of these receptors and their signaling: NS1 of influenza virus blocks RIG-I activation, proteases of many viruses cleave MAVS or STING, proteins of herpesviruses inhibit cGAS, and some bacteria modify lipid A to evade recognition by TLR4. These strategies of **pathogen immune evasion** are covered in [7.11.27](/7.11.27), [7.11.34](/7.11.34), and [7.15.32](/7.15.32).

## Summary

- Innate recognition targets **pathogen-associated molecular patterns** (shared by microbes, essential, absent from the host or in a different place) and **damage-associated molecular patterns** (endogenous molecules released by damaged cells); the recognizers are germline-encoded, constitutively expressed, rapidly responding, limited-in-number **pattern recognition receptors**.
- PRRs divide the labor by location:

  | Location | Receptors | Adaptor / second messenger | Main transcription factor |
  |---|---|---|---|
  | Plasma membrane | TLR1/2/4/5/6; C-type lectin receptors | MyD88 (TIRAP); Syk–CARD9 | NF-κB |
  | Endosome | TLR3; TLR7/8/9; endocytosed TLR4 | TRIF; MyD88 | IRF3; IRF7 (pDC) |
  | Cytosol | **RIG-I-like receptors**; **cGAS–STING pathway**; **NOD-like receptors** | MAVS; cGAMP–STING; RIPK2 | IRF3, NF-κB |
  | Cytosol (inflammasomes) | NLRP3, NLRC4, AIM2, pyrin | ASC–caspase-1 | Maturation of IL-1β, IL-18; pyroptosis |
  | Body fluids | MBL, ficolins, CRP | Complement | — |

- **Toll-like receptors** (Definition 6.2.1): LRR extracellular region + TIR cytoplasmic region; the **MyD88** (Definition 6.2.2) branch activates NF-κB via IRAK–TRAF6–TAK1–IKK, and the TRIF branch activates **interferon regulatory factor** IRF3 (Definition 6.2.3) via TBK1; TLR4 uses both.
- The NLRP3 inflammasome requires two signals, priming (NF-κB) and activation ($\ce{K+}$ efflux), and outputs IL-1β, IL-18, and gasdermin D-mediated pyroptosis.
- Outputs converge on inflammatory cytokines (NF-κB, AP-1) and type I interferons (IRF3/7 → IFNAR → JAK–STAT → ISG); different PRR combinations let dendritic cells steer the response toward type 1, 2, or 3.
- Positive feedback of interferon (IFN → IRF7 → IFN) can make the response bistable (Example 6.6.1): there are a threshold, a saddle-node bifurcation, and hysteresis, and negative feedback eventually brings the high state back down.
- **Trained immunity** (Definition 6.7.1) is the nonspecific enhancement acquired by innate immune cells through epigenetic and metabolic reprogramming; self nucleic acids avoid recognition through location, modification, and nucleases, and failure leads to interferonopathies and lupus.

## Questions

1. Why are TLR3, 7, 8, and 9 located in endosomes rather than at the plasma membrane? What consequence might arise if the extracellular domain of TLR9 were artificially placed at the plasma membrane?

   **Answer** Nucleic acids are molecules shared by pathogens and the host, and distinguishing them depends mainly on location: host nucleic acids are in the nucleus, mitochondria, and cytosol and do not normally enter endosomes; the nucleic acids of an engulfed pathogen are exposed only after degradation in the endosome, so endosomal TLRs "see" only foreign nucleic acid. If TLR9 were at the plasma membrane, it would contact self DNA released by dead cells into the extracellular space, the distinction by location would be lost, and the result would be a sustained response to self DNA. Indeed, mice engineered to have TLR9 at the cell surface respond to self DNA and develop fatal inflammation.

2. C3H/HeJ mice barely respond to injected lipopolysaccharide yet are very susceptible to gram-negative bacterial infection. Explain both points using what you have learned in this chapter.

   **Answer** The *Tlr4* of C3H/HeJ mice carries a point mutation, so TLR4 cannot transmit signals, and injection of purified lipopolysaccharide therefore fails to cause the release of inflammatory cytokines and endotoxic shock; for the same reason, in the early phase of gram-negative infection they cannot promptly produce TNF, IL-1, IL-6, and chemokines, neutrophil recruitment and macrophage activation are delayed, and the bacteria multiply. This example shows that the same recognition by TLR4 is both necessary for defense and responsible for the toxicity of lipopolysaccharide (septic shock).

3. A patient has recurrent fever, urticaria-like rash, and joint pain, and genetic testing finds a gain-of-function mutation in NLRP3. Why does blocking IL-1β effectively control the symptoms while blocking TNF has limited effect?

   **Answer** The gain-of-function mutation of NLRP3 lets the inflammasome assemble with no (or only a weak) activation signal, continuously activating caspase-1 and cleaving pro-IL-1β and pro-IL-18; the symptoms are caused mainly by excess mature IL-1β (fever, acute-phase response, neutrophilic inflammation). Blocking IL-1β or its receptor directly targets the pathological output; TNF is not a direct product of the inflammasome but only part of the downstream inflammatory network, and blocking it cannot abolish the action of IL-1β.

4. In the model of Example 6.6.1, how does the bistability change if $\delta$ increases (for example if interferon is degraded faster or negative feedback such as SOCS is stronger)? Explain the biological significance.

   **Answer** The degradation line $\delta x$ becomes steeper and the number of intersections with the sigmoidal production curve decreases: when $\delta$ exceeds a critical value, only the low intersection remains, the bistability disappears, and the system becomes monostable; the interferon response subsides when the stimulus is withdrawn and cannot "remember" the infection. Biologically, the strength of negative feedback determines whether the interferon response is a sustained switch or a reversible graded response; defects in negative feedback (such as USP18 deficiency) make the response persistent and cause interferonopathies, whereas excessive negative feedback weakens antiviral defense.

5. (Open question) Why might trained immunity explain the protective effect of BCG vaccine against infections other than tuberculosis? What evidence would distinguish trained immunity from cross-reactive adaptive immunity?

   **Answer** Key points: BCG can induce epigenetic and metabolic reprogramming of monocytes and bone marrow progenitors, so that they later produce stronger responses such as IL-1β and TNF to many unrelated pathogens, and this nonspecific enhancement can lower the incidence and severity of other infections. To distinguish them: (1) protection is still observed in animals lacking T and B cells (*Rag* deficiency), showing independence from adaptive immunity; (2) protection can be transferred by monocytes or bone marrow progenitors and is accompanied by the corresponding histone modifications and metabolic changes; (3) drugs inhibiting glycolysis or histone modification abolish protection; (4) the breadth of protection (against structurally unrelated pathogens) and its duration (months) also differ from those of cross-reactive antibodies or T cells.
