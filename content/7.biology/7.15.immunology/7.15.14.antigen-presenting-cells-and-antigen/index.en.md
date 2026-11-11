---
title: Antigen-Presenting Cells and Antigen Processing and Presentation
source_hash: b1e252e01dfa
---

The previous chapter ([7.15.13](/7.15.13)) described what kinds of peptides MHC molecules can bind. This chapter answers the second half of the second question on the knowledge path, "what is recognized?": how a protein antigen becomes a peptide–MHC complex (pMHC) that a T cell can see, and which cells display it. The answer has two parts. All nucleated cells cut the proteins they synthesize themselves into peptides and load them onto MHC class I molecules for surveillance by CD8⁺ T cells. A few professional antigen-presenting cells take up proteins from the outside and load them onto MHC class II molecules for recognition by CD4⁺ T cells, and among them dendritic cells can also load exogenous antigen "across" onto MHC class I molecules to initiate CD8⁺ T-cell responses. Dendritic cells are at once sensors of innate immunity and initiators of adaptive immunity: they sense pathogens in the tissues (through **pattern recognition receptors**, [7.15.6](/7.15.6)) and then carry the antigen, together with "danger" signals, to the lymph node. How T cells read these signals is covered in [7.15.16](/7.15.16).

## 14.1. Antigen-Presenting Cells

**Definition 14.1.1 (Antigen-Presenting Cell)** A cell that can take up or produce antigen, process it into peptides and present it to T cells as peptide–MHC complexes is called an **antigen-presenting cell** (APC).

T cells cannot recognize free protein antigen; they recognize only pMHC, through the TCR. According to the route and capacity of presentation, APCs fall into three groups:

- Professional APCs: dendritic cells, monocytes/macrophages and B cells (Definition 14.1.2);
- Nonprofessional APCs: endothelial cells, epithelial cells, fibroblasts and others, which are induced to express MHC class II molecules by inflammation and IFN-γ and can present to effector or memory CD4⁺ T cells but usually cannot prime naive T cells;
- Target cells: almost all nucleated cells present endogenous antigen through MHC class I molecules to be recognized by CD8⁺ T cells; by convention these are called target cells and not APCs.

**Definition 14.1.2 (Professional Antigen-Presenting Cell)** Cells that constitutively express MHC class II molecules, take up and process antigen efficiently, and express costimulatory molecules after activation are called **professional antigen-presenting cells**: dendritic cells, monocytes/macrophages and B cells.

The three kinds of professional APC divide the work differently:

| | Dendritic cell | Macrophage | B cell |
|---|---|---|---|
| Mode of uptake | Macropinocytosis, receptor-mediated endocytosis, phagocytosis | Mainly phagocytosis | Specific binding and internalization via the BCR |
| Antigen specificity | None | None | Takes up only antigen recognized by the BCR; can concentrate it from very low concentrations |
| MHC II and costimulatory molecules | Very high after maturation | Low; upregulated after IFN-γ activation | Constitutive MHC II; CD80/86 upregulated after activation |
| Cross-presentation | Strong (cDC1) | Weak | Very weak |
| Main location | Tissues → T-cell zone of the lymph node | Tissues, sites of inflammation | Lymphoid follicles, T–B border |
| Main targets | Naive T cells (the only cells that can prime them effectively) | Effector and memory Th1 cells | Activated Th cells, especially Tfh |
| Purpose of presentation | To initiate adaptive responses | To receive T-cell help in killing ingested microbes | To receive T-cell help in producing antibody |

The last row of the table is the key point: dendritic cells present in order to initiate a response; macrophages and B cells present in order to "ask for help," so that CD4⁺ T cells recognizing the same antigen come back to activate them ([7.15.17](/7.15.17), [7.15.20](/7.15.20)).

## 14.2. Dendritic Cells

**Dendritic cells** are named for the many dendrite-like processes they extend when mature; they were discovered in the mouse spleen by Steinman and Cohn in 1973. Steinman received the 2011 Nobel Prize in Physiology or Medicine for the discovery of dendritic cells and their role in adaptive immunity (Beutler and Hoffmann shared the prize that year for the discovery of innate immune activation). The dendritic cell is the only APC that can effectively prime naive T cells and is the initiator of adaptive immune responses.

### 14.2.1. Subsets

Modern classification is based on developmental lineage and transcription factors, and no longer on location (the old names "interdigitating DC" and "interstitial DC" are descriptions of position).

**Definition 14.2.1 (Dendritic Cell Subsets)** Dendritic cells that differentiate from a common DC precursor in the bone marrow, depend on FLT3 ligand, and serve as antigen presenters in tissues and lymphoid organs are called **classical dendritic cells** (cDCs) and are divided into two subsets, cDC1 and cDC2; dendritic cells that secrete large amounts of type I interferon in response to viral nucleic acids are called **plasmacytoid dendritic cells** (pDCs).

| Subset | Transcription factors required | Human markers | Mouse markers | Main functions |
|---|---|---|---|---|
| cDC1 | IRF8, BATF3 | CD141 (BDCA3), XCR1, CLEC9A | CD8α (lymphoid organs), CD103 (tissues), XCR1 | Cross-presentation, IL-12 secretion; prime CD8⁺ T-cell and Th1 responses |
| cDC2 | IRF4, KLF4, NOTCH2 | CD1c (BDCA1), CD172a (SIRPα), CD11b | CD11b, SIRPα | MHC II presentation, priming of CD4⁺ T cells, biased toward Th2 and Th17 |
| pDC | E2-2 (TCF4), IRF7 | CD123, CD303 (BDCA2), CD304 (BDCA4) | SiglecH, BST2 | Sense nucleic acids through TLR7 and TLR9 and secrete large amounts of IFN-α; weak presenting capacity |
| Monocyte-derived DC | Inflammation-induced | CD14⁺CD1c⁺ and others | Derived from Ly6C⁺ monocytes | Generated locally at sites of inflammation; supplementary presentation and cytokine production |
| Langerhans cell | Embryonic origin, self-renewing | CD1a, CD207 (langerin) | CD207 | Resident cells of the epidermis, close to macrophages in lineage but able functionally to migrate to lymph nodes to present |

**Remark 14.2.1** The **follicular dendritic cell** (FDC) of the lymphoid follicle is not a dendritic cell. It is a stromal cell of mesenchymal origin that does not express MHC class II molecules and does not process antigen; instead it uses complement receptors and Fc receptors to retain intact antigen–antibody complexes on its surface for a long time, so that germinal center B cells can test their affinity ([7.15.20](/7.15.20)). The name reflects only a similar morphology; listing FDCs as a kind of DC is a common mistake.

:::

### 14.2.2. Maturation and Migration

Classical DCs exist in two states with sharply different functions:

| | Immature DC | Mature DC |
|---|---|---|
| Location | Peripheral tissues (skin, mucosa, interstitium) | T-cell zone of the lymph node |
| Uptake and processing | Very strong: macropinocytosis, Fc receptors, mannose receptor, DEC-205 | Weak; uptake essentially stops |
| MHC class II molecules | Mainly intracellular; surface half-life about 10 h | Moved in large numbers to the surface; half-life over 100 h |
| Costimulatory molecules (CD80, CD86, CD40) | Low or absent | High |
| Chemokine receptors | Inflammatory receptors such as CCR1 and CCR5 | CCR7 |
| Cytokines | Few | IL-12, IL-6, IL-23 and others (depending on the stimulus) |
| Function | Sampling | Presenting and priming T cells |

The transition is triggered by danger signals: pattern recognition receptors such as **Toll-like receptors** recognize pathogen components, or cytokines (TNF, IL-1) and CD40 signals act on the DC. On maturation the DC upregulates CCR7, enters lymphatic vessels along the CCL21 gradient, reaches the T-cell zone of the lymph node through the afferent lymphatics, and, guided by CCL19 and CCL21, meets the recirculating naive T cells ([7.15.3](/7.15.3), [7.15.4](/7.15.4)). The whole process usually takes a day or two. Maturation also "freezes" the antigen repertoire of the DC: uptake stops and the loaded pMHC is stabilized for a long time, so the DC in the lymph node displays the antigens it saw in the tissue during its last period there.

The functions of DCs can be summarized in four points:

1. Recognizing and taking up antigen, and participating in innate immunity through pattern recognition receptors;
2. Processing and presenting antigen to initiate adaptive immunity: pMHC provides signal 1, costimulatory molecules provide signal 2, and cytokines (IL-12 and others) induce T-cell differentiation ([7.15.16](/7.15.16));
3. Immune regulation: the pathogen signals the DC receives determine which effector subset T cells differentiate into, that is, the choice among type 1, 2 and 3 immunity;
4. Maintaining immune tolerance: thymic DCs take part in negative selection ([7.15.15](/7.15.15)); in the steady state, DCs without danger signals also carry antigens of self tissues to lymph nodes and present them under insufficient costimulation, inducing T-cell anergy or regulatory T cells ([7.15.24](/7.15.24)).

**Remark 14.2.2** Priming of naive CD4⁺ T cells by a DC is sufficient for their full activation, proliferation and differentiation; priming of naive CD8⁺ T cells in many situations also requires help from CD4⁺ T cells: CD40L on the CD4⁺ T cell binds CD40 on the DC, causing the DC to upregulate costimulatory molecules and IL-12 further. This process is called DC "licensing"; details are in [7.15.16](/7.15.16).

:::

### 14.2.3. Macrophages and B Cells

**Macrophages** take up particulate antigen by phagocytosis and through a variety of receptors (Fc receptors, complement receptors, scavenger receptors, the mannose receptor) and degrade it in the **phagolysosome**. Resting macrophages have low MHC class II molecules and costimulatory molecules, which are markedly upregulated after IFN-γ activation. Macrophages present mainly to already activated T cells and to memory T cells, providing them with targets for recognition, and the T cells in turn activate the macrophages to kill the microbes they have ingested.

**B cells** bind and internalize antigen specifically through the BCR and can present effectively at antigen concentrations several orders of magnitude lower than DCs; they can also take up soluble antigen by pinocytosis. A B cell presents a T-cell epitope from the antigen recognized by its BCR to Th cells and so obtains help directed against the same antigen; this is the cellular basis of the **hapten–carrier effect** and of **conjugate vaccines** ([7.15.8](/7.15.8), [7.15.20](/7.15.20)).

## 14.3. Concepts of Antigen Processing and Presentation

**Definition 14.3.1 (Antigen Processing and Antigen Presentation)** **Antigen processing** is the process by which an APC degrades ingested exogenous antigen or endogenously produced antigen into peptides of a certain length, allows them to bind MHC molecules, and transports the pMHC to the cell surface. **Antigen presentation** is the process by which the pMHC at the cell surface is recognized by the TCR of a T cell, so that the antigenic peptide is displayed to the T cell.

**Definition 14.3.2 (Endogenous and Exogenous Antigens)** Antigens synthesized inside the cell are called **endogenous antigens** (viral proteins, tumor proteins, the cell's own proteins); antigens taken in from outside the cell are called **exogenous antigens** (bacteria, debris of apoptotic cells, soluble proteins).

The basic rule is that endogenous antigens are presented through the MHC class I pathway to CD8⁺ T cells, and exogenous antigens through the MHC class II pathway to CD4⁺ T cells. This division of labor matches the needs of the effector response: intracellular pathogens can be cleared only by killing the infected cell, which is the task of CTLs, whereas extracellular pathogens require antibodies and activated phagocytes, which are what Th cells help. The rule has two important exceptions: cross-presentation (§14.6), and autophagy, which delivers cytosolic proteins into the class II pathway (§14.5).

![The two antigen presentation pathways. Left: the MHC class I pathway. Viral proteins in the cytosol are ubiquitinated and degraded by the proteasome into peptides; the peptides enter the endoplasmic reticulum through TAP, where they are loaded onto newly synthesized MHC class I molecules, travel through the secretory pathway to the cell surface, and are recognized by the TCR of CD8⁺ T cells, with CD8 binding the α3 domain of MHC I. Right: the MHC class II pathway. Exogenous antigens such as bacteria are endocytosed and degraded by proteases in endosomes and lysosomes; MHC class II molecules associate with the invariant chain (Ii) in the endoplasmic reticulum and are sent through the Golgi apparatus to the MHC class II compartment (MIIC), where the invariant chain is degraded and the remaining CLIP fragment is exchanged for antigenic peptide catalyzed by HLA-DM; pMHC II reaches the cell surface and is recognized by CD4⁺ T cells, with CD4 binding the β2 domain of MHC II](./plots/processing-pathways.py)

## 14.4. The MHC Class I Pathway

### 14.4.1. Generation of Peptides: Proteasome and Immunoproteasome

The peptides of the MHC class I pathway come mainly from proteins being degraded in the cytosol and nucleus. Proteins tagged with **ubiquitin** are degraded by the 26S **proteasome** ([7.3.7](/7.3.7)), and a considerable fraction of them are "defective ribosomal products" (DRiPs: misfolded or prematurely terminated polypeptides) degraded soon after synthesis. This is why viral peptides can appear at the cell surface within hours of infection, before viral proteins have accumulated.

**Definition 14.4.1 (Immunoproteasome)** Inflammatory signals such as IFN-γ induce three catalytic subunits, β1i (LMP2, *PSMB9*), β2i (MECL-1, *PSMB10*) and β5i (LMP7, *PSMB8*), which replace β1, β2 and β5 in the 20S core of the constitutive proteasome to form the **immunoproteasome**. It cleaves more often after hydrophobic and basic residues, producing peptides whose C termini match the F pocket of MHC class I molecules; it is constitutively expressed in immune cells.

Thymic cortical epithelial cells also express a specialized "thymoproteasome" (β5t, *PSMB11*), which produces a distinctive set of self peptides for positive selection ([7.15.15](/7.15.15)). Most peptides generated by the proteasome are cut further into amino acids by cytosolic aminopeptidases and recycled, and only a small fraction enters the endoplasmic reticulum.

### 14.4.2. Transport and Loading

**Definition 14.4.2 (Transporter Associated with Antigen Processing)** The **transporter associated with antigen processing** (TAP) is an ATP-binding cassette (ABC) transporter in the membrane of the endoplasmic reticulum, composed of TAP1 and TAP2, that uses ATP to pump peptides from the cytosol into the lumen of the endoplasmic reticulum; it prefers peptides of 8–16 residues with hydrophobic or basic C-terminal residues.

Newly synthesized class I heavy chains first bind calnexin and fold in the endoplasmic reticulum (the **calnexin cycle**) and, after binding β2m, enter the peptide-loading complex: TAP, tapasin (which tethers the empty class I molecule next to TAP), calreticulin and ERp57 (a thiol oxidoreductase). Peptides that enter the endoplasmic reticulum and are too long are trimmed from the N terminus to 8–9 residues by the endoplasmic reticulum aminopeptidases ERAP1/2. Tapasin and its homolog TAPBPR also act as "editors": they cause peptides of low affinity to dissociate faster, so that the class I molecule ends up loaded with a stably bound peptide. After loading, the class I molecule leaves the complex and travels through the Golgi apparatus to the cell surface; class I molecules that never acquire a peptide are removed by **ER-associated degradation**. Cells deficient in TAP or tapasin have greatly reduced class I molecules at the surface, showing that surface class I molecules almost all need a peptide for stabilization ([7.15.13](/7.15.13)).

## 14.5. The MHC Class II Pathway

Exogenous antigens enter the cell by **phagocytosis**, **macropinocytosis** and receptor-mediated endocytosis (Fc receptors, complement receptors, C-type lectin receptors such as DEC-205 and the mannose receptor, and the BCR of B cells) and move along the **endosome** toward the **lysosome**. The pH falls gradually to 4.5–5, and cathepsins (cathepsin S, L, B, D) and asparagine endopeptidase are activated under the acidic conditions; the thiol reductase GILT in the lysosome opens disulfide bonds and helps proteins unfold. The endosomal protease activity of DCs is weaker than that of macrophages and acidification is milder, so antigen is not degraded completely and presentable peptides are retained.

**Definition 14.5.1 (Invariant Chain)** The **invariant chain** (Ii, CD74) is a nonpolymorphic transmembrane protein that associates with newly synthesized MHC class II αβ dimers in the endoplasmic reticulum. It binds three αβ dimers as a trimer, occupies the binding groove with a stretch of its sequence to prevent peptides in the endoplasmic reticulum from binding the class II molecule, and uses a sorting signal in its cytosolic tail to send the class II molecule to the endosomal system.

In the endosome, the invariant chain is degraded step by step, leaving only a fragment of about 20 residues bound in the groove, called CLIP (class II–associated invariant chain peptide). The late endosomal or lysosome-like compartment rich in class II molecules is called the MHC class II compartment (MIIC). In the MIIC, the nonclassical molecule HLA-DM binds the class II molecule, loosening its conformation and catalyzing the dissociation of CLIP so that a more stably binding antigenic peptide takes its place; DM also acts as an editor, favoring retention of peptides of high stability. HLA-DO inhibits DM in B cells and thymic epithelial cells and regulates the repertoire of peptides these cells present. Peptide-loaded class II molecules are transported to the cell surface.

**Autophagy** also delivers proteins from the cytosol and nucleus to lysosomes and the MIIC ([7.3.25](/7.3.25)), so class II molecules also present some endogenous antigens: thymic epithelial cells use this to present self proteins to developing CD4⁺ T cells.

| | MHC class I pathway | MHC class II pathway |
|---|---|---|
| Source of antigen | Endogenous (cytosol, nucleus, including DRiPs) | Exogenous (endocytosed); some intracellular via autophagy |
| Degradation | Proteasome, immunoproteasome; ERAP trimming | Cathepsins in endosomes and lysosomes |
| Site of peptide–MHC binding | Endoplasmic reticulum | MIIC (late endosome) |
| Mechanism preventing premature binding | Empty class I molecules wait in the peptide-loading complex | Invariant chain and CLIP occupy the binding groove |
| Chaperones and accessory molecules | Calnexin, calreticulin, ERp57, tapasin, TAP | Ii (CD74), HLA-DM, HLA-DO |
| Presenting cells | All nucleated cells | Professional APCs, thymic epithelial cells (inducible on nonprofessional APCs) |
| Recognizing cells | CD8⁺ T cells (CTLs) | CD4⁺ T cells (Th, Treg) |

## 14.6. Cross-Presentation

**Definition 14.6.1 (Cross-Presentation)** The phenomenon in which an APC processes exogenous antigen and presents it through MHC class I molecules to CD8⁺ T cells is called **cross-presentation**; the resulting initiation of CD8⁺ T-cell responses is called cross-priming, and the induction of their tolerance is called cross-tolerance.

Cross-presentation solves a difficulty: if CD8⁺ T cells could be primed only by DCs that were themselves infected, then viruses that do not infect DCs, and tumors, would never provoke a CTL response. cDC1 are the main workhorses of cross-presentation: through CLEC9A (DNGR-1) they recognize F-actin exposed by dead cells and engulf debris from infected cells or tumor cells. Two mechanisms are known:

- Cytosolic pathway: antigen in the phagosome is exported to the cytosol, degraded by the proteasome, and returned by TAP to the endoplasmic reticulum or the phagosome for loading; sensitive to proteasome inhibitors.
- Vacuolar pathway: antigen is degraded within the phagosome by cathepsin S and loaded directly onto class I molecules recycling to the phagosome; independent of TAP.

Mice deficient in BATF3 lack cDC1, cross-priming is severely impaired, and both the CTL responses to a variety of viruses and the rejection of transplanted tumors are markedly weakened, which is direct evidence of the physiological importance of cross-presentation. Infiltration of tumors by cDC1 is also correlated with the efficacy of immunotherapy ([7.15.30](/7.15.30)).

## 14.7. Presentation of Nonpeptide Antigens

**Definition 14.7.1 (CD1 Molecule)** **CD1 molecules** are antigen-presenting molecules encoded on chromosome 1, structurally similar to MHC class I molecules and associated with β2m; their deep, hydrophobic binding groove accommodates the alkyl chains of lipid and glycolipid antigens and exposes the hydrophilic head to T cells. Humans have five, CD1a, b, c, d and e: CD1a–c (group 1) present lipids such as the mycolic acids of mycobacteria to diverse αβ T cells; CD1d (group 2, the only CD1 of mice) presents glycolipids to **NKT cells**; CD1e does not present at the surface but assists lipid loading in the lysosome.

CD1 molecules load lipids in endosomes and have almost no polymorphism, so everyone presents the same lipid in the same way. Other modes of recognition of nonpeptide antigens:

| Presenting molecule | Antigen | Recognizing cell | Significance |
|---|---|---|---|
| CD1a–c | Mycobacterial lipids, self lipids | Some αβ T cells, γδ T cells | Antimycobacterial immunity |
| CD1d | Glycolipids (such as α-galactosylceramide, self lipids) | iNKT cells (invariant Vα24-Jα18 TCR; Vα14-Jα18 in mice) | Rapidly secrete large amounts of IFN-γ and IL-4, linking innate and adaptive immunity |
| MR1 | Metabolites of the microbial riboflavin synthesis pathway (such as 5-OP-RU) | MAIT cells (Vα7.2-Jα33) | Abundant in mucosa and liver; sense most bacteria and fungi |
| Butyrophilins BTN3A1/BTN2A1 | Phosphoantigens (HMBPP, IPP) | Human Vγ9Vδ2 T cells | Sense isoprenoid metabolism of microbes and transformed cells |

What these molecules have in common is that the ligands are metabolites specific to microbes or stressed cells, the presenting molecules are almost nonpolymorphic, and the repertoire of T cells recognizing them is also limited. They lie between innate and adaptive immunity and are often called "innate-like T cells" ([7.15.17](/7.15.17)).

Many pathogens interfere with certain steps of these two pathways to escape T-cell recognition, and the host has NK-cell recognition of the loss of MHC class I molecules (**missing self**) as a backup; such interactions belong to microbiology and are covered in [7.11.27](/7.11.27) and [7.11.34](/7.11.34).

## 14.8. A Quantitative Model of Surface pMHC Numbers

A cell has about $10^5$ MHC class I molecules at its surface, belonging to thousands of different peptides, and a T cell needs to recognize only one of them. How many copies a particular peptide has is determined by two quantities: the rate at which this pMHC reaches the surface and its lifetime there.

**Example 14.8.1** Suppose a pMHC appears at rate $\sigma(t)$ (the number of complexes reaching the surface per hour) and disappears from the surface by first-order kinetics with half-life $t_{1/2}$ (the combined effect of peptide dissociation, internalization and degradation). Its number $P$ then satisfies

$$
\frac{\mathrm{d}P}{\mathrm{d}t} = \sigma(t) - \frac{\ln 2}{t_{1/2}}\,P,
\qquad
P^* = \frac{\sigma\, t_{1/2}}{\ln 2}.
$$

This is the simplest production–degradation balance ([7.9.14](/7.9.14)), with relaxation time $t_{1/2}/\ln 2$. Take the illustrative values $\sigma = 20\,\mathrm{h^{-1}}$ with supply lasting 24 h:

- With $t_{1/2} = 2\,\mathrm{h}$, $P^* \approx 58$ is reached quickly; after the supply stops the number halves every 2 h and falls below the level detectable by a T cell (about 10 complexes, an order of magnitude from single-molecule imaging studies) after about 5 h;
- With $t_{1/2} = 48\,\mathrm{h}$, the steady state is far from reached within 24 h ($P^* \approx 1400$), and only about $1400 \times (1 - 2^{-1/2}) \approx 400$ accumulate; after the supply stops, about 100 remain four days later.

There are three conclusions. First, stably binding peptides (with matching anchor residues, or peptides left after editing by tapasin or HLA-DM) have high copy numbers and stay at the surface longer, and are more likely to become dominant epitopes; this is one of the main determinants of "immunodominance." Second, mature DCs stabilize their pMHC, so that antigen can still be displayed in the lymph node for several days after it has disappeared from the tissue. Third, supply and lifetime enter as a product, so a reduction of either by an order of magnitude can push an epitope below the detection threshold.

:::

![A production–degradation model of surface pMHC numbers (illustrative parameters). A: Complexes of one peptide reach the surface at $\sigma = 20\,\mathrm{h^{-1}}$ with supply lasting 24 h (shaded); four curves for surface half-lives of 2, 8, 24 and 48 h (logarithmic vertical axis). Complexes with a short half-life quickly reach a low plateau and disappear rapidly once supply stops; complexes with a long half-life accumulate more and persist for days. The dashed line is the order of magnitude of the T-cell detection threshold (about 10 complexes per cell). B: Steady-state number $P^* = \sigma t_{1/2}/\ln 2$ as a function of the supply rate; the dotted line is the order of magnitude of the total number of MHC class I molecules at the cell surface](./plots/pmhc-kinetics.py)

## Summary

- **Antigen-presenting cells** (Definition 14.1.1) comprise professional APCs (DCs, macrophages, B cells; Definition 14.1.2), nonprofessional APCs induced to express MHC II, and target cells recognized by CTLs through MHC I. DCs present in order to initiate a response; macrophages and B cells present in order to receive help.
- DC subsets (Definition 14.2.1): cDC1 (IRF8, BATF3; cross-presentation, IL-12, CD8⁺ and Th1), cDC2 (IRF4; CD4⁺, Th2 and Th17), pDC (IFN-α); FDCs are not DCs (Remark 14.2.1).
- Immature DCs sample in the tissues, and danger signals cause them to mature: they upregulate CCR7, MHC II and costimulatory molecules and migrate to the lymph node to prime naive T cells; presentation in the absence of danger signals induces tolerance.
- The two pathways (Definition 14.3.1, Definition 14.3.2):

| | Class I pathway | Class II pathway |
|---|---|---|
| Antigen | Endogenous | Exogenous (and autophagy substrates) |
| Key steps | Ubiquitin–(immuno)proteasome (Definition 14.4.1) → TAP (Definition 14.4.2) → peptide-loading complex in the endoplasmic reticulum (tapasin, ERAP trimming) | Endocytosis → cathepsins → invariant chain (Definition 14.5.1) → CLIP → peptide exchange by HLA-DM (MIIC) |
| Target | CD8⁺ T cells | CD4⁺ T cells |

- **Cross-presentation** (Definition 14.6.1): cDC1 load exogenous antigen onto MHC I, so that CTLs can respond to viruses that do not infect DCs and to tumors.
- Nonpeptide antigens: **CD1 molecules** (Definition 14.7.1) present lipids, MR1 presents riboflavin metabolites, and butyrophilins mediate recognition of phosphoantigens; the recognizing cells are innate-like T cells.
- The number of a given pMHC at the surface is roughly "supply rate × lifetime" (Example 14.8.1): stable complexes determine immunodominant epitopes, and mature DCs can keep displaying antigen for several days after it has disappeared.

## Questions

1. Why can only dendritic cells effectively prime naive T cells, whereas macrophages and B cells usually cannot?

   **Answer** Priming a naive T cell requires meeting, simultaneously, three conditions: encountering the rare specific T cell in the T-cell zone of the lymph node; having enough sufficiently stable pMHC at the surface; and high levels of costimulatory molecules and polarizing cytokines. Mature DCs satisfy all three: they carry antigen from the tissue into the T-cell zone via CCR7, stabilize pMHC on maturation, and express large amounts of CD80/86, CD40 and IL-12. Macrophages mostly stay in the tissues, have low costimulatory molecules at rest, and degrade antigen too thoroughly in their lysosomes; B cells present only antigen recognized by their own BCR and also have low costimulatory molecules at rest. Their presentation serves mainly to obtain help from already activated T cells.

2. A virus infects only neurons and no APC. The host can still generate CTLs against it. By what mechanism? What would happen if the host lacked BATF3?

   **Answer** Through cross-presentation: cDC1 engulf debris of infected neurons that have died, load the viral proteins onto MHC class I molecules through the cytosolic or vacuolar pathway, and prime CD8⁺ T cells in the lymph node. With BATF3 deficiency, cDC1 are absent, cross-priming is severely impaired, and the CTL response to this virus would be markedly weakened or absent (a small amount of cross-presentation by other DCs may remain).

3. What problems would arise in the class II pathway if the invariant chain were absent?

   **Answer** The invariant chain has three functions: helping αβ dimers fold and assemble correctly in the endoplasmic reticulum; occupying the binding groove to prevent peptides in the endoplasmic reticulum from binding class II molecules prematurely; and directing class II molecules to the endosomal system. When it is absent, the efficiency of class II assembly falls, some molecules bind peptides they should not or aggregate in the endoplasmic reticulum, far fewer class II molecules reach the endosome, and presentation of exogenous antigen is markedly impaired; Ii-deficient mice have fewer class II molecules at the surface and fewer CD4⁺ T cells.

4. In the model of Example 14.8.1, if antigen supply is continuous, what are the effects on the steady-state copy number and on the "duration after supply stops" of lengthening the pMHC half-life 4-fold versus raising the supply rate 4-fold?

   **Answer** The steady-state number $P^* = \sigma t_{1/2}/\ln 2$ is symmetric in the two, and both raise it 4-fold. After the supply stops, the time during which the number stays above the detection threshold $\vartheta$ is $T = t_{1/2}\log_2(P^*/\vartheta)$. Raising the supply 4-fold increases $T$ by only $2t_{1/2}$; lengthening the half-life 4-fold gives $4t_{1/2}\left(\log_2(P^*/\vartheta) + 2\right) = 4T + 8t_{1/2}$, a duration more than 4 times longer. This is the significance of the stabilization of pMHC by mature DCs: after leaving the tissue and no longer taking up antigen, they must still display antigen in the lymph node for several days.
