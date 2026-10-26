---
title: Translational Control
description: Why gene expression is regulated at translation (speed, reversibility, kinetics of protein levels); bacterial control by mRNA structure, RNA thermometers, repressor proteins, ribosomal-protein autoregulation, translational coupling and ribosome rescue by tmRNA; the eIF2 cycle, eIF2α phosphorylation by HRI, PKR, PERK and GCN2 and the integrated stress response, with a model of eIF2B sequestration; mTORC1, 4E-BPs, S6K and 5′ TOP mRNAs; 5′-UTR elements (IREs, uORFs and delayed reinitiation at GCN4 and ATF4, leaky scanning, IRESs); microRNA repression of initiation; protein degradation by the ubiquitin–proteasome system, degrons and the N-degron pathways, and quality control of stalled ribosomes; ribosome profiling and codon-level rates.
---

The amount of a protein is set by four rates: the synthesis and decay of its mRNA, which were the subject of the previous chapters, and the translation of the mRNA and the degradation of the protein, which are the subject of this one. Translation is the most energy-consuming of these steps and the last one at which a cell can decide, within minutes and without new transcription, how much of a protein to make; it is also where cells respond globally to stress and nutrients by adjusting the activity of the initiation machinery described in [7.2.19](/7.2.19). The chapter begins with the reasons for and the kinetics of translational control (20.1), then treats the bacterial mechanisms, which act mostly on the ribosome-binding site (20.2), and the two hubs of eukaryotic control, the eIF2 cycle (20.3) and **mTORC1** with the cap-binding complex (20.4). Particular **mRNAs** are controlled through elements of their $5'$ leaders (20.5) and by **microRNAs** (20.6). Protein degradation, the end point of every expression program, is treated in 20.7, and the last section shows how **ribosome profiling** measures translation **codon** by codon (20.8).

## 20.1. Why Control Translation

### 20.1.1. Speed and Reversibility

Control at translation acts on mRNAs that already exist. Its first advantage is speed: a eukaryotic transcript may take tens of minutes to be transcribed, processed and exported, whereas translation of a stored mRNA can be switched on within minutes. Its second is reversibility: repression of initiation can be lifted without new synthesis, as in fertilized eggs, which live for hours on maternal mRNAs stored in a masked form, or in neurons, where synapses translate locally stored mRNAs in response to activity. Third, translational control can act on all mRNAs at once, through the general **initiation factors**, which makes it the natural target of signals that report the global state of the cell, such as amino-acid supply, energy, ER stress and viral infection.

Most control is at initiation, the rate-limiting step for most mRNAs, because blocking a ribosome before it has committed costs nothing, while stopping elongation would waste the energy already invested and sequester **ribosomes** on the mRNA. In bacteria, whose mRNAs live only a few minutes ([7.2.18](/7.2.18)), most control is transcriptional, and translational control is concentrated on the structure of the ribosome-binding site; in **eukaryotes**, whose mRNAs are longer-lived, translational control is more prominent.

### 20.1.2. The Kinetics of Protein Levels

**Formula 20.1.1 (Synthesis and decay of a protein)** If an mRNA present at $m$ copies is translated with rate constant $k_{\mathrm{tl}}$ (proteins per mRNA per unit time) and the protein is degraded with rate constant $k_{\mathrm{p}}$ and diluted by growth at rate $\mu$, the protein number $p$ obeys
$$
\frac{\mathrm{d}p}{\mathrm{d}t} = k_{\mathrm{tl}}\,m - (k_{\mathrm{p}} + \mu)\,p, \tag{20.1}
$$
with **steady state** $p^* = k_{\mathrm{tl}}m/(k_{\mathrm{p}} + \mu)$ and response time $\ln 2/(k_{\mathrm{p}} + \mu)$.

The equation has the form of Eq. (18.1) of [7.2.18](/7.2.18), and the same conclusions follow: the steady-state level is proportional to the translation rate and to the protein's lifetime, and the time to reach a new level is set by degradation and dilution, not by the speed of synthesis. In mouse fibroblasts the median protein half-life is about $46\,\mathrm{h}$ and the median **mRNA half-life** about $9\,\mathrm{h}$, and translation rate constants span about 100-fold; across genes, differences in translation explain a large part of the variation of protein levels that is not explained by mRNA levels (Schwanhäusser and colleagues, 2011). For a stable protein a change of $k_{\mathrm{tl}}$ changes the synthesis rate at once, but the level follows only slowly; fast changes of protein levels therefore require unstable proteins (20.7), and this is why many regulators, such as **cyclins**, transcription factors and signaling proteins, are both short-lived and translationally controlled.

## 20.2. Translational Control in Bacteria

### 20.2.1. Structure of the Ribosome-Binding Site

A bacterial mRNA is translated about as often as its ribosome-binding site, the **Shine–Dalgarno sequence** and the **start codon** ([7.2.19](/7.2.19)), is accessible to 30S **subunits**. A stem that sequesters either one lowers initiation by orders of magnitude, in proportion to its stability, so that changing the structure of the RBS is the common mechanism of bacterial translational control. Different cistrons of a **polycistronic mRNA** ([7.2.11](/7.2.11)) can therefore be translated at different rates: in the *lac* **operon**, several times more β-galactosidase than transacetylase is made.

**Example 20.2.1 (Translational coupling)** In the RNA phage MS2, the start codon of the replicase gene is paired with a sequence within the coat-protein gene upstream. Ribosomes translating the coat gene unfold the structure and expose the replicase start; mutations that stop coat translation early, before the paired region, abolish replicase synthesis, whereas those that stop it afterward do not. Later in infection the coat protein itself binds a **hairpin** at the replicase start and represses it, so that the phage switches from replication to packaging. Translational coupling, in which translation of an upstream cistron is required to open the start of the downstream one, also equalizes the synthesis of subunits encoded in one operon, such as TrpE and TrpD of the *trp* operon.

**Definition 20.2.1** An **RNA thermometer** is a structured element in the $5'$ untranslated region of an mRNA whose base-paired conformation, which sequesters the ribosome-binding site, melts at elevated temperature, so that translation is controlled directly by temperature.

The mRNA of $\sigma^{32}$, the heat-shock **σ factor** of *E. coli* encoded by *rpoH* ([7.2.10](/7.2.10)), is translated poorly at $30^\circ\mathrm{C}$ because its start region pairs with sequences within the coding region; at $42^\circ\mathrm{C}$ the structure melts and $\sigma^{32}$ synthesis rises within minutes, before transcription changes (Morita, Yura and colleagues, 1999). Other thermometers control heat-shock genes of rhizobia (ROSE elements) and the virulence regulator PrfA of *Listeria*, which is translated at $37^\circ\mathrm{C}$, in a host, but not at ambient temperature. In the simplest model the stem melts in a two-state transition, and the fraction of open, translatable mRNA follows a sigmoid in temperature whose steepness increases with the melting enthalpy, that is, with the length of the stem (figure).

![An RNA thermometer. A: schematic: at 30 °C the Shine–Dalgarno sequence is paired in a stem and the 30S subunit cannot bind; at 42 °C the stem melts and initiation proceeds (σ32 mRNA of E. coli, the PrfA leader of Listeria and the ROSE elements of rhizobia work this way). B: two-state melting of the stem, fraction open = 1/(1 + exp(ΔH/R·(1/T − 1/T_m))) with T_m = 42 °C and ΔH = 150, 300 and 450 kJ/mol (illustrative values); translation is taken as proportional to the open fraction, and the switch sharpens with ΔH](./plots/rna-thermometer.py)

Small metabolites and **small RNAs** change the same structures: translational **riboswitches** bind a metabolite and sequester the RBS, and **small RNAs** pair with it, both described in [7.2.18](/7.2.18).

### 20.2.2. Repressor Proteins and Ribosomal-Protein Autoregulation

Proteins can repress translation by binding at or near the RBS. The most systematic case is the regulation of ribosomal proteins, which must be made in amounts matching the rRNA.

**Example 20.2.2 (Ribosomal proteins regulate their own operons)** Nomura and colleagues found that in each of several *E. coli* operons of ribosomal proteins, one protein represses the translation of the operon's mRNA. Protein L1 represses the L11 operon (L11, L1), S4 the α operon, S8 the *spc* operon, and S7 the *str* operon. The **repressor** in each case is a protein that binds rRNA directly in ribosome assembly, and its binding site on the mRNA resembles its binding site on rRNA; it binds rRNA more tightly. As long as free rRNA is available, the protein is incorporated into ribosomes; when it is made in excess, it binds its own mRNA and stops further synthesis of all proteins of the operon, which are translationally coupled. The ratio of rRNA to ribosomal protein is thus maintained by competition between two **binding sites**, a feedback that matches protein synthesis to rRNA synthesis without measuring either. Similar logic governs threonyl-tRNA synthetase, which represses its own mRNA by binding a structure that mimics the **anticodon** arm of $\mathrm{tRNA^{Thr}}$, and the T4 proteins gp32 and RegA.

### 20.2.3. Rescue of Stalled Ribosomes and the Stringent Response

A ribosome that reaches the $3'$ end of an mRNA without a **stop codon**, for example on an mRNA cut by a nuclease, cannot terminate, and in *E. coli* this happens to a few percent of translation events.

**Definition 20.2.2** **Trans-translation** is the rescue of bacterial ribosomes stalled at the $3'$ end of an mRNA by tmRNA (SsrA RNA), a $363\,\mathrm{nt}$ RNA with a tRNA-like domain, charged with Ala, and an mRNA-like reading frame: with the protein SmpB, it enters the empty A site, accepts the nascent peptide, and replaces the broken mRNA as template, so that translation ends at its own stop codon and adds a C-terminal tag (AANDENYALAA) that directs the protein to degradation by the ClpXP and other proteases.

Keiler, Waller and Sauer (1996) discovered the tag on proteins expressed from mRNAs lacking stop codons. tmRNA thus frees the ribosome, marks the incomplete protein for destruction and, because the stalled mRNA is released, promotes its decay. Backup systems use alternative **release factors** (ArfA with RF2, and ArfB, which hydrolyses peptidyl-tRNA itself).

When amino acids run out, uncharged **tRNAs** enter the A site of translating ribosomes, which activates RelA bound to the ribosome to make the alarmone ppGpp (and pppGpp) from GTP and ATP. ppGpp binds **RNA polymerase**, together with DksA, and lowers transcription of rRNA and ribosomal-protein genes, while raising that of amino-acid **biosynthesis** genes; this stringent response adjusts the ribosome content to the nutrient supply, as required by the growth law of [7.2.19](/7.2.19) (Eq. (19.4)).

## 20.3. The eIF2 Cycle and the Integrated Stress Response

### 20.3.1. Control by Phosphorylation of eIF2α

Every eukaryotic initiation uses one ternary complex of eIF2·GTP with $\mathrm{Met\text{-}tRNA_i^{Met}}$ and releases eIF2·GDP ([7.2.19](/7.2.19)). eIF2 binds GDP about 100 times more tightly than GTP, so its recycling depends on eIF2B, its **guanine nucleotide-exchange factor**, which is present at lower concentration than eIF2 (about 15–25 % in mammalian cells). This step is the target of a family of kinases, discovered as the heme-controlled repressor (HCR) of reticulocyte lysates, now called HRI.

**Example 20.3.1 (Heme controls globin synthesis)** Lysates of rabbit reticulocytes, which make almost only globin, translate actively when **heme** is added, but shut down after a few minutes without it. The inhibitor that appears was purified as a **protein kinase** that phosphorylates the α subunit of eIF2. Phosphorylated eIF2·GDP is not a **substrate** for exchange; instead it binds eIF2B more tightly than unphosphorylated eIF2·GDP and holds it in an unproductive complex. Adding excess eIF2B relieves the inhibition. The heme dependence ensures that globin chains are made only when heme is available to bind them.

**Definition 20.3.1** The **integrated stress response** (ISR) is the eukaryotic signaling pathway in which any of four kinases phosphorylates Ser51 of eIF2α in response to a stress, inhibiting eIF2B and reducing the formation of ternary complexes; global cap-dependent translation falls, while a few mRNAs with special $5'$ leaders, such as that of the transcription factor ATF4 (GCN4 in yeast), are translated more.

| Kinase | Activated by | Physiological role |
|---|---|---|
| HRI (EIF2AK1) | heme deficiency; also oxidative, mitochondrial and proteotoxic stress | matches globin synthesis to heme in erythroid cells |
| PKR (EIF2AK2) | double-stranded RNA (viral replication); induced by interferon | antiviral defense |
| PERK (EIF2AK3) | unfolded proteins in the ER lumen (unfolded protein response) | reduces the load of new proteins entering the ER ([7.3](/7.3)) |
| GCN2 (EIF2AK4) | uncharged tRNAs (amino-acid starvation); stalled and collided ribosomes | adapts protein synthesis and amino-acid biosynthesis to supply |

The response is terminated by dephosphorylation: ATF4 induces CHOP and then GADD34, a regulatory subunit that directs **protein phosphatase** 1 to eIF2α, closing a negative feedback loop; the drug salubrinal blocks this dephosphorylation. Viruses counter PKR by making decoy RNAs (adenovirus VA RNA) or GADD34-like proteins (herpes simplex virus ICP34.5). The small molecule ISRIB, discovered in a screen for ISR inhibitors, binds and stabilizes the decameric form of eIF2B, so that it resists inhibition by phosphorylated eIF2; it restores memory formation in mice with brain injury in some studies. Mutations in any of the five eIF2B subunits cause vanishing white-matter disease, a leukodystrophy aggravated by stress.

### 20.3.2. Why a Little Phosphorylation Goes a Long Way

Because eIF2B is less abundant than eIF2, phosphorylation of a fraction of eIF2 equal to the eIF2B/eIF2 ratio is enough to sequester nearly all eIF2B.

**Formula 20.3.1 (Sequestration of eIF2B)** Let the total concentrations of eIF2 and eIF2B be $E_{\mathrm{T}}$ and $B_{\mathrm{T}}$, a fraction $\varphi$ of eIF2 be phosphorylated, and phosphorylated eIF2·GDP bind eIF2B with **dissociation constant** $K_{\mathrm{i}}$. The free eIF2B is $B_{\mathrm{free}} = B_{\mathrm{T}} - C$, where the complex $C$ is the smaller root of
$$
C^2 - (B_{\mathrm{T}} + \varphi E_{\mathrm{T}} + K_{\mathrm{i}})\,C + B_{\mathrm{T}}\,\varphi E_{\mathrm{T}} = 0, \tag{20.2}
$$
and exchange on unphosphorylated eIF2·GDP, at concentration $S = (1-\varphi)E_{\mathrm{T}}$, proceeds at the **Michaelis–Menten equation** rate $v \propto B_{\mathrm{free}}\,S/(K_{\mathrm{m}} + S)$. For tight binding ($K_{\mathrm{i}} \ll B_{\mathrm{T}}$), $B_{\mathrm{free}} \approx \max(0,\ B_{\mathrm{T}} - \varphi E_{\mathrm{T}})$, and ternary-complex formation falls linearly to nearly zero at $\varphi = B_{\mathrm{T}}/E_{\mathrm{T}}$.

This is the titration mechanism of Formula 18.9.1 ([7.2.18](/7.2.18)) applied to an enzyme: the phosphorylated substrate acts as a stoichiometric inhibitor of its own exchange factor. With $B_{\mathrm{T}}/E_{\mathrm{T}} = 0.2$, phosphorylation of 20 % of eIF2 lowers ternary-complex formation about tenfold; if eIF2B were as abundant as eIF2, the same phosphorylation would lower it by only about 20 % (figure, B). The low abundance of eIF2B is therefore an amplifier, which lets four kinases with modest activity control the protein synthesis of the whole cell.

![The eIF2 cycle. A: eIF2·GTP binds Met-tRNAi to form the ternary complex, which joins the 40S subunit; at the start codon, eIF5 triggers GTP hydrolysis, and eIF2·GDP is released and recycled by its exchange factor eIF2B. The four kinases HRI, PKR, PERK and GCN2, activated by heme deficiency, double-stranded RNA, ER stress and uncharged tRNA, phosphorylate Ser51 of eIF2α; phosphorylated eIF2·GDP binds and sequesters eIF2B. B: the sequestration model of Formula 20.3.1 (K_i = 0.002 E_T, K_m = 0.1 E_T): with eIF2B at 20 % of eIF2 (solid), ternary-complex formation falls about tenfold when 20 % of eIF2 is phosphorylated; with eIF2B as abundant as eIF2 (dashed) it would fall only slightly](./plots/eif2-cycle.py)

## 20.4. mTORC1 and the Cap-Binding Complex

The second hub of global control is the assembly of eIF4F on the cap. Its target is eIF4E, the cap-binding protein, whose availability is limited by the 4E-binding proteins.

**Definition 20.4.1** The **eIF4E-binding proteins** (4E-BPs; 4E-BP1–3 in mammals) are small proteins that bind eIF4E through the motif $\mathrm{YXXXXL\Phi}$ (Φ hydrophobic), the same motif by which eIF4G binds it, and so prevent eIF4F assembly and cap-dependent initiation; phosphorylation of 4E-BPs at several sites releases eIF4E.

The kinase that phosphorylates 4E-BPs is mTORC1, the complex of the protein kinase mTOR (mechanistic target of rapamycin) with Raptor, named after the drug rapamycin, which with its binding protein FKBP12 inhibits it. mTORC1 integrates four inputs on the surface of lysosomes (figure): growth factors and **insulin**, through PI3K and PKB (Akt), which phosphorylate and inactivate the TSC1–TSC2 complex, the **GTPase-activating protein** of the **small G protein** Rheb ([7.1.15](/7.1.15)), so that Rheb·GTP accumulates and activates mTORC1; amino acids, sensed by the Rag GTPases, which recruit mTORC1 to the lysosome; energy, through AMPK, which activates TSC2 and inhibits Raptor when ATP is low; and oxygen and DNA damage, through TSC as well. Its translational outputs are three.

1. 4E-BP1 is phosphorylated in a hierarchical order (Thr37 and Thr46 first, then Ser65 and Thr70) and releases eIF4E, which binds eIF4G. Since 4E-BPs are typically more abundant than free eIF4E, eIF4F forms only after most 4E-BP has been phosphorylated (figure, B), a threshold set by stoichiometry, as for eIF2B.
2. S6 kinase 1 (S6K1) is phosphorylated and activated. It phosphorylates ribosomal protein S6, eIF4B (which stimulates the helicase eIF4A), and PDCD4, an inhibitor of eIF4A that is then degraded; S6K also inhibits eEF2 kinase, which phosphorylates and inactivates eEF2, so that elongation speeds up as well.
3. The mRNAs with a $5'$ terminal oligopyrimidine tract (5′ TOP mRNAs: a C at the cap followed by 4–14 pyrimidines), which encode all ribosomal proteins, most elongation factors and PABP, are released from repression by the protein LARP1, which binds the cap and the TOP sequence when mTORC1 is inactive. mTORC1 therefore controls the synthesis of the translation machinery itself, matching it to growth conditions, as the stringent response does in bacteria.

Many cancers have activating mutations in this pathway (PI3K, PTEN loss, TSC), and rapamycin analogs (rapalogs) are used as immunosuppressants and anticancer drugs. Viruses also target eIF4F: the poliovirus protease 2A cleaves eIF4G ([7.2.19](/7.2.19)), and some viruses dephosphorylate 4E-BP1.

![mTORC1, the integrator of growth signals for translation. A: insulin and growth factors (through PI3K and PKB), amino acids (through the Rag GTPases) and energy (AMPK) converge on mTORC1 at the lysosome; PKB inhibits TSC1/2, the GAP of Rheb, and Rheb·GTP activates mTORC1; rapamycin·FKBP12 inhibits it. mTORC1 phosphorylates and inactivates 4E-BP1, releasing eIF4E for eIF4F assembly; activates S6K1, which acts on eIF4B, PDCD4 and rpS6; and relieves LARP1 repression of 5′ TOP mRNAs. B: competition of 4E-BP and eIF4G for eIF4E in an equilibrium model (eIF4E 1, eIF4G 0.6, 4E-BP 2; dissociation constants 0.01 and 0.002, illustrative): eIF4F assembles mostly after 4E-BP is largely phosphorylated](./plots/mtorc1.py)

## 20.5. Control by the 5′ Leader

### 20.5.1. Iron-Responsive Elements

The **iron-responsive element** in the $5'$ UTR of ferritin mRNA ([7.2.18](/7.2.18)) is the classic case of a repressor protein bound to a eukaryotic mRNA. When iron is low, iron-regulatory proteins bind the IRE and block recruitment of the 43S complex; when iron is high, they leave and ferritin is made.

**Example 20.5.1 (An IRE must be near the cap to repress)** Hentze, Klausner and colleagues fused the $5'$ leader of ferritin mRNA to a reporter (chloramphenicol acetyltransferase, CAT) and transfected cells: iron raised CAT synthesis without changing its mRNA, and the same construct with the IRE in the $3'$ UTR was not regulated at the level of translation. Goossen and Hentze (1992) then moved the IRE progressively away from the cap within an extended leader: repression was strong when the IRE lay within about $40\,\mathrm{nt}$ of the cap and was lost when it lay further downstream. Bound IRP therefore does not block scanning ribosomes; it prevents the 43S complex from binding the cap-proximal region. Similar repression is obtained by tethering other RNA-binding proteins near the cap, which shows that the mechanism is steric.

### 20.5.2. Upstream Open Reading Frames and Reinitiation

About half of human mRNAs have at least one AUG upstream of the main start codon, and ribosome profiling shows that many of these are translated.

**Definition 20.5.1** An **upstream open reading frame** (uORF) is a short **open reading frame** in the $5'$ leader of an mRNA, upstream of the main coding sequence. After translating a short uORF, a 40S subunit can remain on the mRNA, resume scanning and start again at a downstream AUG once it has rebound a ternary complex; this is **reinitiation**.

Most uORFs reduce translation of the main ORF, typically by 30–80 %, because ribosomes that translate them often dissociate; they are therefore under negative selection near the start, and mutations that create uORFs cause disease. In two famous cases, the uORFs are the sensors of the integrated stress response.

**Example 20.5.2 (GCN4 and ATF4)** Yeast *GCN4* mRNA, which encodes the transcriptional activator of amino-acid biosynthesis genes, has four short uORFs (Hinnebusch and colleagues). uORF1 allows efficient reinitiation; uORF4 does not, because ribosomes that translate it detach. After uORF1, the scanning 40S subunits need a new ternary complex. When ternary complexes are abundant, they rebind one before uORF4, translate it and are lost; when amino acids are scarce, GCN2 phosphorylates eIF2α, ternary complexes become scarce, and many 40S subunits scan past uORF4 before rebinding one, reinitiating at *GCN4*. Moving uORF4 closer to uORF1 makes *GCN4* constitutively derepressed; removing all uORFs makes it constitutive and unregulated. Mammalian *ATF4* mRNA uses the same logic with two uORFs (Vattem and Wek, 2004): a short uORF1 that permits reinitiation and an inhibitory uORF2 that overlaps the ATF4 start codon out of frame (figure). Paradoxically, a reduction of global initiation thus increases the synthesis of a transcription factor that induces amino-acid transporters, biosynthetic enzymes, chaperones and, through CHOP and GADD34, the feedback of 20.3.

**Formula 20.5.1 (Delayed reinitiation)** Suppose a 40S subunit that has translated uORF1 rebinds a ternary complex as a Poisson process along the leader with rate $a$ per nucleotide scanned, proportional to the ternary-complex concentration. With $d_2$ nucleotides from uORF1 to the start of uORF2 and $D$ from there to the main start codon, the probabilities of reinitiating at uORF2 and at the main ORF are
$$
P_{\mathrm{u2}} = 1 - \mathrm{e}^{-a d_2}, \qquad P_{\mathrm{main}} = \mathrm{e}^{-a d_2}\,\bigl(1 - \mathrm{e}^{-aD}\bigr). \tag{20.3}
$$
$P_{\mathrm{main}}$ is maximal at $a^* = \ln(1 + D/d_2)/D$: it increases as $a$ falls from high values and decreases again when $a$ becomes so small that ribosomes pass the main start codon as well.

With illustrative values ($d_2 = 90$, $D = 180$, and $a = 0.03$ per nt in unstressed cells), reducing the ternary complex to about 20 % raises ATF4 synthesis about sixfold while bulk translation falls fivefold (figure, B). The model explains why the distances between the uORFs, measured in nucleotides scanned, are conserved, and it predicts the biphasic response seen in severe stress.

![Delayed reinitiation on ATF4 mRNA. A: after the short uORF1, 40S subunits resume scanning without a ternary complex (TC); with abundant TC (top) they reacquire one before the inhibitory uORF2, which overlaps the ATF4 start codon out of frame, translate it and miss ATF4; when TC is scarce (bottom) many scan past uORF2 before rebinding and reinitiate at ATF4. B: the Poisson model of Formula 20.5.1 (d₂ = 90 nt, D = 180 nt, rebinding rate 0.03 per nt at normal TC; illustrative): ATF4 translation relative to unstressed cells rises about sixfold as TC falls to about 20 %, while bulk translation, proportional to TC, falls; at very low TC ATF4 falls again](./plots/uorf-reinitiation.py)

### 20.5.3. Leaky Scanning and Alternative Starts

When the first AUG lies in a weak Kozak context, some 40S subunits pass it and initiate at a downstream AUG (leaky scanning, [7.2.19](/7.2.19)). One mRNA then encodes two proteins with different N-termini, for example a mitochondrial and a cytosolic isoform, one with and one without a targeting presequence, or two transcription factors with opposite activities (LAP and LIP from *CEBPB* mRNA, whose ratio is controlled by mTORC1 through a uORF). Non-AUG codons (CUG, GUG, ACG) in good context also start translation at low efficiency, often with eIF2A or eIF2D rather than eIF2, and give N-terminally extended isoforms such as those of FGF2 and MYC.

### 20.5.4. Internal Ribosome Entry Sites

**Definition 20.5.2** An **internal ribosome entry site** (IRES) is an RNA structure that recruits the ribosome to an internal position of an mRNA, independently of the $5'$ cap and of scanning from the $5'$ end, by binding directly to the 40S subunit, to initiation factors or to auxiliary RNA-binding proteins.

IRESs were found in the uncapped genomic RNAs of picornaviruses (Pelletier and Sonenberg; Jang and Wimmer, 1988), whose $5'$ ends carry a small protein, VPg, and a long, structured leader with many AUGs that cannot be scanned. They were defined with bicistronic reporters, in which a second cistron is translated only if the RNA between the cistrons can recruit ribosomes. Viral IRESs form a spectrum of decreasing factor requirements.

| Type | Example | Requirements |
|---|---|---|
| I and II | poliovirus (I), encephalomyocarditis virus (II) | all eIFs except eIF4E (bind the central domain of eIF4G and eIF4A), plus IRES trans-acting proteins (PTB); type I scans from the entry site |
| III | hepatitis C virus | binds the 40S subunit directly and eIF3; needs eIF2 or eIF2D for Met-tRNA, but no eIF4F |
| IV | intergenic IRES of cricket paralysis virus | binds 80S ribosomes alone; mimics a tRNA–mRNA interaction in the P site and starts at a non-AUG codon in the A site, without any initiation factor or Met-tRNA |

The advantage for a virus is that its RNA is translated when the host's cap-dependent initiation is inhibited, which the virus itself often causes (cleavage of eIF4G, activation of PKR). Many cellular mRNAs, among them those of MYC, XIAP and VEGF, were proposed to contain IRESs that keep them translated during stress, mitosis or apoptosis. This is controversial: in bicistronic plasmid assays, cryptic promoters and splicing can create monocistronic mRNAs that look like IRES activity, and only a few cellular IRESs have passed stringent tests (direct transfection of bicistronic RNA, analysis of mRNA integrity).

## 20.6. MicroRNAs and 3′-UTR Repressors

**microRNAs** ([7.2.18](/7.2.18)) were first thought to act only on translation, because the target mRNAs of *lin-4* in *C. elegans* remained on polysomes. The evidence that they inhibit initiation came from human cells.

**Example 20.6.1 (let-7 inhibits cap-dependent initiation)** Pillai, Filipowicz and colleagues (2005) placed let-7 target sites in the $3'$ UTR of a luciferase reporter. Repression by endogenous let-7 shifted the reporter mRNA from heavy to light fractions of a sucrose gradient (fewer ribosomes per mRNA) without much change in its level. Reporters translated from an EMCV or HCV IRES, or through an eIF4E or eIF4G protein tethered to the RNA, were not repressed, whereas capped reporters were; an mRNA with a nonfunctional $\mathrm{ApppN}$ cap was not repressed either. The miRNA therefore acts at cap recognition or shortly after, and repressed mRNAs accumulated in P-bodies.

Later work explained how. Argonaute recruits GW182 (TNRC6), which recruits CCR4–NOT; this complex deadenylates the mRNA and, through the helicase DDX6 and the cap-binding protein 4E-T, represses initiation and displaces eIF4A from eIF4F. In the steady state of mammalian cells, decay accounts for most of the repression, but translational repression comes first and dominates in some contexts ([7.2.18](/7.2.18), Formula 18.6.1 and its discussion). Earlier proposals, such as direct cap binding by Argonaute, have not been confirmed.

Other $3'$-UTR repressors act on the closed loop of [7.2.19](/7.2.19). In *Xenopus* oocytes, mRNAs with a cytoplasmic polyadenylation element (CPE) have short poly(A) tails and are kept silent by CPEB with Maskin (or 4E-T), which binds eIF4E and blocks eIF4G; at oocyte maturation CPEB is phosphorylated, the tail is extended by the poly(A) polymerase GLD-2, PABP binds, and translation starts. In *Drosophila* embryos, Bicoid represses *caudal* mRNA through the cap-binding protein 4EHP, which cannot bind eIF4G; such localized repression creates protein gradients in development ([7.5](/7.5)).

## 20.7. Protein Degradation as the End Point

### 20.7.1. The Ubiquitin–Proteasome System

All proteins are eventually degraded, regulators within minutes, structural proteins in days; damaged and misfolded proteins are removed quickly. Two systems do this in eukaryotes: lysosomes, which digest proteins taken up by endocytosis and autophagy ([7.3](/7.3)), and the **proteasome**, which degrades proteins of the cytosol and nucleus that are marked with **ubiquitin** ([7.1.15](/7.1.15)). Hershko, Ciechanover and Rose discovered the system in ATP-dependent proteolysis of reticulocyte lysates (Nobel Prize in Chemistry 2004).

**Definition 20.7.1** The **ubiquitin–proteasome system** (UPS) is the eukaryotic pathway of selective protein degradation in which an E1–E2–E3 enzyme cascade attaches chains of ubiquitin to a substrate recognized by a specific E3 ubiquitin ligase, and the 26S proteasome recognizes the chain, unfolds the substrate with ATP and degrades it to short peptides, releasing ubiquitin for reuse.

- Enzymes. One or two E1s activate ubiquitin with ATP (ubiquitin adenylate, then a thioester with the active-site Cys of E1); about 40 E2s carry it as a thioester; over 600 E3s in humans give specificity. RING-type E3s (including the cullin–RING ligases such as SCF and the anaphase-promoting complex APC/C) bring E2 and substrate together and catalyze direct transfer; HECT-type E3s form a thioester with ubiquitin themselves. The isopeptide bond links the C-terminal Gly76 of ubiquitin to a Lys ε-amino group of the substrate or of the previous ubiquitin.
- The signal. A chain of at least four ubiquitins linked through Lys48 is the canonical degradation signal; Lys11-linked chains act in mitosis, whereas Lys63-linked and linear chains, and single ubiquitins, have nondegradative roles in signaling, DNA repair and endocytosis. Deubiquitinating enzymes (about 100 in humans) edit or remove chains.
- The proteasome. The 20S core particle is a barrel of four stacked heptameric rings, $\alpha_7\beta_7\beta_7\alpha_7$, with the active sites inside, on three of the β subunits: β1 (cleavage after acidic residues, caspase-like), β2 (after basic residues, trypsin-like) and β5 (after hydrophobic residues, chymotrypsin-like), all threonine proteases with the N-terminal Thr as nucleophile. The gated α rings admit only unfolded chains. The 19S regulatory particle on one or both ends contains ubiquitin receptors (Rpn1, Rpn10, Rpn13), the deubiquitinase Rpn11, which removes the chain as the substrate enters, and a ring of six AAA+ ATPases (Rpt1–6) that unfold the substrate and thread it into the core, which needs an unstructured initiation region of the substrate of about 20–30 residues. Products are peptides of 3–25 residues, further degraded by peptidases or presented by MHC class I molecules ([7.15](/7.15)).

Bacteria and archaea have proteasome-like and other ATP-dependent proteases (ClpXP, ClpAP, Lon, FtsH, and in actinobacteria a true proteasome with a ubiquitin-like tag, Pup), which recognize degrons directly or through adaptors. The proteasome inhibitor bortezomib, which blocks β5, is used against multiple myeloma, whose plasma cells, making large amounts of antibody, depend on protein quality control.

![The ubiquitin–proteasome system. A: E1 activates ubiquitin with ATP, E2 carries it, and an E3 ligase that recognizes the substrate's degron transfers it to a Lys of the substrate; repeated rounds build a Lys48-linked chain. The 26S proteasome binds the chain with its 19S regulatory particles, removes and recycles the ubiquitin, unfolds the substrate and degrades it in the 20S core (αββα rings) to peptides of 3–25 residues. B: the N-degron rule: half-lives in yeast of β-galactosidase variants with different N-terminal residues (Bachmair, Finley and Varshavsky, 1986): more than 20 h with Met, Ser, Ala, Thr, Val or Gly, 2–30 min with the other residues tested](./plots/ubiquitin-proteasome.py)

### 20.7.2. Degrons and the N-Degron Pathways

**Definition 20.7.2** A **degron** is a feature of a protein that is sufficient to target it for degradation, usually by being recognized by an E3 ubiquitin ligase or a protease adaptor; an **N-degron** is a degron whose essential part is the N-terminal residue of the protein.

Bachmair, Finley and Varshavsky (1986) expressed ubiquitin–β-galactosidase fusions in yeast, which are cleaved by deubiquitinases right after ubiquitin and so expose any chosen residue at the N-terminus of β-galactosidase: the half-life ranged from more than $20\,\mathrm{h}$ to $2\,\mathrm{min}$ depending on this residue (figure, B), the N-end rule. Its present form distinguishes several N-degron pathways.

| Pathway | N-terminal signal | Recognition |
|---|---|---|
| Arg/N-degron | primary destabilizing residues: basic (Arg, Lys, His) and bulky hydrophobic (Leu, Phe, Tyr, Trp, Ile); secondary: Asp, Glu, which are arginylated by ATE1; tertiary: Asn, Gln, which are deamidated and then arginylated, and Cys after oxidation | UBR-box E3s (UBR1, UBR2 and others) |
| Ac/N-degron | Nα-acetylated N-termini (most proteins after cotranslational acetylation, [7.2.19](/7.2.19)), exposed when the protein is misfolded or unassembled | Doa10 (MARCHF6) and others |
| Pro/N-degron | Pro at position 1 or 2 | GID/CTLH ligase in yeast (gluconeogenic enzymes) |
| fMet/N-degron (bacteria and eukaryotes) | formylated Met | Psh1 in yeast |
| Bacterial N-degron | Leu, Phe, Tyr, Trp; Arg and Lys are converted by the Leu/Phe-tRNA-protein transferase | adaptor ClpS, protease ClpAP (no ubiquitin) |

N-degrons are created by the processing of 19.9.1 of [7.2.19](/7.2.19): methionine aminopeptidases remove Met only before small residues, which are stabilizing, so a protein rarely starts with a destabilizing residue unless it is cleaved by a protease. Cleavage of a protein can therefore mark the fragment for destruction; in yeast, separase cleaves the cohesin subunit Scc1 at anaphase, and the C-terminal fragment, starting with Arg, is degraded by the Arg/N-degron pathway. The rule is often presented as identical in bacteria and eukaryotes; its hierarchical logic is shared, but the primary residues and the machinery differ (table). Internal degrons include the destruction box ($\mathrm{R}xx\mathrm{L}xx\mathrm{I}x\mathrm{N}$) and KEN box of cyclins, recognized by APC/C in mitosis ([7.3](/7.3)), phosphodegrons such as the one of β-catenin and IκB recognized by SCF ligases after phosphorylation, and the PEST sequences rich in Pro, Glu, Ser and Thr associated with short half-lives. Targeted protein degradation with small molecules that bring a substrate to an E3, such as the "molecular glues" thalidomide and lenalidomide (which redirect the E3 cereblon to transcription factors such as IKZF1/3) and the bivalent PROTACs, has become a drug design strategy.

### 20.7.3. Quality Control at the Ribosome

Eukaryotic ribosomes that stall on an mRNA, on a damaged base, a strong structure, a poly(A) stretch translated as poly-Lys, or the $3'$ end of an mRNA cut without a stop codon, are rescued by a pathway that has the same aims as trans-translation in bacteria (20.2.3): recycle the ribosome, degrade the mRNA and destroy the incomplete protein. A stalled ribosome is hit by the one behind it, and the collided pair is recognized by the E3 ZNF598 (Hel2 in yeast), which ubiquitinates ribosomal proteins of the small subunit. Pelota (Dom34) with the GTPase Hbs1, the paralogs of eRF1 and eRF3 that bind an empty A site without a stop codon, together with ABCE1, split the ribosome. On the large subunit, which still holds the peptidyl-tRNA, the ribosome-associated quality-control complex acts: the E3 listerin (Ltn1) ubiquitinates the nascent chain, which is extracted by the ATPase VCP (p97) and degraded by the proteasome, and the protein NEMF (Rqc2) adds a C-terminal tail of Ala and Thr residues without mRNA (CAT tail), which exposes Lys residues for listerin. The mRNA is cleaved near the stall (no-go decay) and degraded ([7.2.18](/7.2.18)). Collisions also activate GCN2 and the stress kinase ZAK, linking ribosome quality control to the integrated stress response. Loss of listerin causes neurodegeneration in mice.

## 20.8. Measuring Translation Codon by Codon

**Ribosome profiling** ([7.2.6](/7.2.6)) counts the ribosomes on each codon of every mRNA at the moment the cells are lysed. Its readouts address three quantities.

1. How much each mRNA is translated. The density of footprints on a coding sequence divided by the mRNA abundance from RNA-seq of the same sample is its translation efficiency, a measure of the initiation rate when elongation is uniform. Under stress, profiling shows which mRNAs escape the global shutdown (ATF4 and others with uORFs), and under mTORC1 inhibition the selective loss of 5′ TOP mRNAs.
2. Where translation starts. Drugs that arrest initiating ribosomes (harringtonine, lactimidomycin) leave footprints only at start codons, which identified thousands of translated uORFs, non-AUG starts and short ORFs in RNAs annotated as noncoding.
3. How fast each codon is read. At low ribosome density, ribosomes do not interfere with each other, and the number at a codon is the flux through it times its dwell time.

**Formula 20.8.1 (Density and dwell time)** If ribosomes pass codon $i$ with flux $J$ (ribosomes per unit time, equal to the initiation rate in steady state) and spend on average $\tau_i = 1/k_i$ there, the mean number of ribosomes on that codon is
$$
\rho_i = J\,\tau_i = \frac{J}{k_i}, \tag{20.4}
$$
so relative footprint counts along a coding sequence measure relative dwell times, independently of $J$. When initiation is fast compared with the slowest elongation steps, ribosomes queue behind slow codons, and the totally asymmetric simple exclusion process (TASEP, MacDonald and Gibbs, 1968), in which particles of size about $10$ codons hop one way with codon-specific rates, describes the resulting traffic.

Profiling found that the speed varies at particular motifs more than with codon usage in general: ribosomes pause at runs of Pro, whose peptide bonds form slowly and are accelerated by the factor eIF5A (EF-P in bacteria), at stretches of positively charged residues that interact with the negatively charged exit tunnel, and at codons whose tRNAs are depleted, as during amino-acid starvation. The footprints also show the reading frame through their three-nucleotide periodicity, which distinguishes genuine translation from other protected RNA.

![Ribosome profiling of a simulated mRNA (a model, not data). A: footprints of elongating ribosomes along an mRNA with a 120-nt leader containing a 10-codon uORF, a 300-codon coding sequence and a 3′ UTR: counts follow ribosome density J/k_i (Formula 20.8.1) with codon-specific rates (mean 6 codons per second), longer dwell times at the start and stop codons and a tenfold slower Pro-Pro-Pro motif at codon 180; reads in the reading frame dominate (inset, 75 % in frame 0), which reveals the frame. B: with harringtonine, which stops ribosomes at initiation, footprints remain only at the start codons of the uORF and of the main coding sequence](./plots/ribosome-profile.py)

## Summary

| Level | Mechanism | Key molecules | Example |
|---|---|---|---|
| Bacterial RBS | sequestration of SD/AUG by mRNA structure (Definition 20.2.1), metabolites, sRNAs, repressor proteins; translational coupling (Example 20.2.1) | 30S subunit, riboswitches, Hfq | σ32 thermometer; ribosomal-protein autoregulation (Example 20.2.2) |
| Ternary complex | eIF2α Ser51 phosphorylation sequesters eIF2B (Example 20.3.1, Formula 20.3.1) | HRI, PKR, PERK, GCN2; eIF2B; GADD34–PP1; ISRIB | integrated stress response (Definition 20.3.1) |
| Cap recognition | 4E-BPs compete with eIF4G for eIF4E (Definition 20.4.1) | mTORC1, 4E-BP1, S6K1, LARP1 | growth control; 5′ TOP mRNAs |
| 5′ leader | IREs near the cap (Example 20.5.1); uORFs and delayed reinitiation (Definition 20.5.1, Formula 20.5.1); leaky scanning; IRESs (Definition 20.5.2) | IRP1/2; ternary complex; ITAFs | ferritin; GCN4 and ATF4 (Example 20.5.2); picornaviruses, HCV |
| 3′ UTR | miRNAs (Example 20.6.1), CPEB–Maskin, 4EHP | Argonaute, GW182, CCR4–NOT, DDX6 | let-7; oocyte maturation; Bicoid–*caudal* |
| Rescue and quality control | trans-translation (Definition 20.2.2); collision sensing, splitting, RQC | tmRNA–SmpB; ZNF598, Pelota–Hbs1, listerin, NEMF | nonstop mRNAs |
| Protein degradation | E1–E2–E3 and the 26S proteasome (Definition 20.7.1); degrons and N-degrons (Definition 20.7.2) | E3 ligases (SCF, APC/C, UBR1), Lys48 chains, 19S and 20S particles | cyclins, IκB, N-end rule |

- Protein levels follow $\mathrm{d}p/\mathrm{d}t = k_{\mathrm{tl}}m - (k_{\mathrm{p}} + \mu)p$ (Eq. (20.1)): translation sets the synthesis rate at once, protein stability the response time.
- Global control works through two scarce components, eIF2B and free eIF4E, whose titration by phosphorylated eIF2 or by 4E-BPs gives switch-like responses (Eq. (20.2), mTORC1 figure).
- Lowering ternary-complex availability selectively increases translation of uORF-containing mRNAs (Eq. (20.3)).
- Ribosome profiling measures translation efficiency, start sites and codon dwell times, $\rho_i = J/k_i$ (Eq. (20.4)).

## Questions

1. A protein with a half-life of $40\,\mathrm{h}$ is made from an mRNA with a half-life of $4\,\mathrm{h}$ in cells dividing every $24\,\mathrm{h}$. Translation of its mRNA is doubled at $t = 0$. How long does it take for the protein to reach 75 % of its new excess level? Would doubling transcription instead be faster?

   **Answer** The protein's effective decay rate is $k_{\mathrm{p}} + \mu = \ln 2/40 + \ln 2/24 = 0.0173 + 0.0289 = 0.0462\,\mathrm{h^{-1}}$. After doubling $k_{\mathrm{tl}}$, the protein approaches its new level as $1 - \mathrm{e}^{-0.0462t}$; 75 % is reached at $t = \ln 4/0.0462 = 30\,\mathrm{h}$. Doubling transcription is slower, because the mRNA must first rise (with effective rate $\ln 2/4 + \ln 2/24 = 0.202\,\mathrm{h^{-1}}$, i.e. a delay of several hours) before the protein synthesis rate has doubled; the protein response is then the convolution of the two exponentials and lags the translational change by about $1/0.202 \approx 5\,\mathrm{h}$. In both cases the slow step is protein turnover.

2. In the model of Formula 20.3.1 with $B_{\mathrm{T}}/E_{\mathrm{T}} = 0.2$ and tight binding, what fraction of eIF2 must be phosphorylated to reduce ternary-complex formation by half? Why would overexpression of eIF2B make cells resistant to stress, and what is the analogous effect of ISRIB?

   **Answer** With tight binding, $B_{\mathrm{free}} \approx B_{\mathrm{T}} - \varphi E_{\mathrm{T}}$, and the substrate term $S/(K_{\mathrm{m}} + S)$ changes little for small $\varphi$ ($K_{\mathrm{m}} = 0.1E_{\mathrm{T}}$). Half of the activity is lost when $B_{\mathrm{free}} \approx 0.5B_{\mathrm{T}}$, i.e. $\varphi \approx 0.1$: phosphorylation of 10 % of eIF2 halves initiation. Overexpressing eIF2B raises $B_{\mathrm{T}}/E_{\mathrm{T}}$, so a larger phosphorylated fraction is needed before the exchange factor is titrated, and the response to the same kinase activity is weaker. ISRIB does the equivalent without changing amounts: by stabilizing the active eIF2B decamer it lowers its affinity for phosphorylated eIF2 (raises $K_{\mathrm{i}}$) and increases its activity, so phosphorylation sequesters less of it.

3. Predict the effect on *GCN4* translation in yeast, under starved and nonstarved conditions, of (a) a deletion of *GCN2*, (b) a mutation in eIF2α at Ser51 to Ala, (c) deleting uORFs 2–4 and keeping uORF1, (d) moving uORF4 far downstream from uORF1.

   **Answer** (a) and (b): eIF2α cannot be phosphorylated, ternary complexes stay abundant even in starvation, ribosomes reinitiate at uORF4 and *GCN4* is not induced (the *gcn* phenotype, inability to grow on amino-acid analogs). (c) With only uORF1, ribosomes that reinitiate always reach *GCN4* (no inhibitory uORF), so *GCN4* is translated well under both conditions (constitutive derepression). (d) A longer distance from uORF1 to uORF4 gives the 40S subunits more time to rebind a ternary complex even when it is scarce, so more ribosomes translate uORF4 and induction under starvation is reduced (Eq. (20.3) with larger $d_2$).

4. How would you distinguish experimentally whether a drug inhibits translation initiation or elongation, using polysome profiles and ribosome profiling?

   **Answer** An initiation inhibitor lets ribosomes already engaged finish their proteins ("run-off") while no new ones load: polysomes decrease and 80S monosomes and free subunits increase within minutes. An elongation inhibitor freezes ribosomes in place: polysomes are retained (or increase, as with cycloheximide, which is used precisely to stabilize them). Ribosome profiling refines this: with an initiation inhibitor, footprint density falls first at the $5'$ end of coding sequences and the depletion moves $3'$ with time at the elongation speed (as in harringtonine run-off experiments that measure elongation rates of about $5$–$6$ codons per second); with a context-specific elongation inhibitor, footprints accumulate at the specific motifs where it acts.

5. The ferritin IRE functions only near the cap, whereas the IREs of transferrin-receptor mRNA act from the $3'$ UTR. Explain both in terms of the steps they control.

   **Answer** The ferritin IRE controls translation initiation: IRP bound within about 40 nt of the cap prevents the 43S complex (with eIF3 bound to eIF4G on the cap) from binding the $5'$ end, a steric block that works only where the 43S complex must land; once bound, scanning complexes can unwind and displace downstream structures and proteins, so an IRE far from the cap is passed. The TfR IREs control mRNA stability: bound IRPs protect an endonuclease-sensitive region in the $3'$ UTR from cleavage, which requires no position relative to the ribosome ([7.2.18](/7.2.18)).

6. Why do RING E3s, but not proteasome inhibitors, offer specificity for drugs? Explain how a molecular glue such as lenalidomide degrades transcription factors that cereblon normally does not bind.

   **Answer** The proteasome degrades all ubiquitinated proteins, so inhibiting it affects every short-lived protein (useful in myeloma, whose cells are especially dependent on it, but toxic); the specificity of the system lies in the more than 600 E3s, each recognizing particular degrons. Lenalidomide binds a pocket of cereblon, the substrate receptor of a cullin-4 RING ligase, and creates a new composite surface that binds a zinc-finger degron of IKZF1 and IKZF3; these become substrates, are polyubiquitinated and degraded, which kills multiple myeloma cells that depend on them. The drug thus reprograms the substrate specificity of an E3 instead of inhibiting an enzyme.

7. (Open question) Using Formula 20.8.1, explain why the average footprint density of an mRNA is not a direct measure of its protein synthesis rate when elongation is slowed globally, for example by eEF2 phosphorylation, and propose a way to measure the synthesis rate directly.

   **Answer** Footprint density $\rho = J\bar\tau$ is proportional to the flux only if the dwell times $\bar\tau$ are unchanged. If elongation slows globally, $\bar\tau$ rises and density can stay constant or even increase while the flux $J$, the actual rate of protein synthesis, falls; translation efficiency calculated from density then overestimates synthesis. Ways to measure synthesis: run-off experiments with harringtonine to determine the elongation rate, combined with the density, give $J = \rho/\bar\tau$; metabolic labeling of nascent proteins with stable-isotope or clickable amino acids (pulsed SILAC, azidohomoalanine) or puromycin incorporation (SUnSET) measures synthesis directly; and single-molecule imaging of nascent chains (SunTag) measures initiation and elongation rates on individual mRNAs.
