---
title: Barriers and Cells of Innate Immunity
source_hash: 990a508b8e44
---

From this chapter on we enter the first link of the knowledge path, innate immunity. It answers the "fast version" of question 1 (who recognizes) and question 3 (what clears) of the five questions. This chapter introduces the executors: first the barriers that keep pathogens out (§5.1), then the phagocytes that are the first to fight once pathogens get in (§5.2–5.3), the granulocytes (§5.4), and the NK cells that recognize "abnormal self" (§5.5), and finally the innate lymphoid cells and innate-like lymphocytes that correspond one to one with T-cell subsets (§5.6–5.7). The receptors with which they recognize pathogens are the subject of the next chapter, and the processes of their recruitment, killing, and induction of inflammation are in [7.15.7](/7.15.7). The origin, numbers, and surface markers of each cell type were tabulated in [7.15.2](/7.15.2); here we describe how they work.

## 5.1. Tissue Barriers

The great majority of microbes that contact the human body are stopped at the barriers. Barriers are the most commonly overlooked yet most important part of innate immunity: a burn patient who has lost skin is highly prone to severe infection even though the immune cells are entirely normal.

### 5.1.1. Physical Barriers

The epidermis of the skin consists of multiple layers of keratinocytes, the outermost of which is a dense, continuously shed layer of dead cells, the stratum corneum, that is almost impenetrable to microbes. Mucosae have only one or a few layers of epithelium and compensate by other mechanisms: **tight junctions** between epithelial cells seal the intercellular space; mucus secreted by goblet cells forms a gel layer on the epithelial surface that keeps microbes far from the epithelium (the inner mucus layer of the colon is nearly sterile); the beating of cilia in the airway pushes mucus together with trapped particles toward the pharynx (**mucociliary clearance**); and peristalsis, urine flow, tears, coughing, and sneezing also continuously flush microbes away.

### 5.1.2. Chemical Barriers

| Site | Chemical factor | Action |
|---|---|---|
| Skin | Lactic acid in sweat gives a pH of about 5.5; unsaturated fatty acids in sebum | Inhibit the growth of most bacteria |
| Stomach | Gastric acid (pH 1–3) | Kills most ingested microbes |
| Tears, saliva, respiratory and intestinal secretions | **Lysozyme** (hydrolyzes the β-1,4 glycosidic bond of peptidoglycan); lactoferrin (chelates iron) | Dissolves bacterial cell walls; deprives bacteria of the iron needed for growth |
| Alveoli | Surfactant proteins SP-A, SP-D (collectins) | Agglutinate microbes and promote phagocytosis |
| Various epithelia | Antimicrobial peptides (§5.1.3) | Disrupt microbial membranes |

### 5.1.3. Antimicrobial Peptides

**Definition 5.1.1 (Antimicrobial Peptide)** Small cationic polypeptides produced by epithelial cells and phagocytes that can directly kill bacteria, fungi, or enveloped viruses are called **antimicrobial peptides** (also host defense peptides); a large class of them that are rich in cysteine and stabilized by three intrachain disulfide bonds are called **defensins**.

Antimicrobial peptides generally consist of 12–50 amino acids, carry a net positive charge, and are amphipathic. The outer layer of microbial membranes is rich in negatively charged phospholipids (phosphatidylglycerol and cardiolipin of bacteria, lipopolysaccharide of gram-negative bacteria, teichoic acid of gram-positive bacteria), whereas the outer layer of animal cell membranes is mainly electrically neutral phosphatidylcholine and sphingomyelin and contains cholesterol. Cationic antimicrobial peptides therefore bind preferentially to microbial membranes and, after insertion, form pores or disintegrate the membrane like detergents.

| Class | Representatives | Source | Notes |
|---|---|---|---|
| α-defensins | HNP1–4; HD5, HD6 | Azurophilic granules of neutrophils; Paneth cells at the base of small intestinal crypts | HD6 does not kill directly but polymerizes into "nanonets" that entangle bacteria |
| β-defensins | hBD1–4 | Epithelium of skin, airways, and urogenital tract | hBD2 and hBD3 are induced by IL-1, IL-17, IL-22, and bacterial products |
| Cathelicidin | LL-37 | Neutrophils, epithelium | The only human cathelicidin; also neutralizes lipopolysaccharide and is chemotactic for leukocytes |
| C-type lectin | RegIIIγ (mouse) / REG3A (human) | Intestinal epithelium, Paneth cells | Binds peptidoglycan and keeps gram-positive bacteria at a distance from the epithelium |
| Others | Histatins (saliva), dermcidin (sweat) | | |

The production of antimicrobial peptides is regulated by type 3 immunity: IL-17 and IL-22 secreted by Th17 cells and ILC3s induce epithelial expression of β-defensins and REG3 ([7.15.1](/7.15.1)). Because they attack a basic physical property of membranes, it is difficult for bacteria to acquire high-level resistance by point mutations, which makes antimicrobial peptides a subject of research for new antibacterial drugs.

### 5.1.4. Microbial Barriers

Commensal microbes on the surfaces of skin and mucosa (the **microbiome**) prevent colonization by pathogens by competing for nutrients and adhesion sites, producing bacteriocins and short-chain fatty acids, and stimulating the epithelium to produce antimicrobial peptides and mucus; this is called colonization resistance. After broad-spectrum antibiotics disrupt the gut flora, pathogens such as *Clostridioides difficile* can take advantage. Commensals also continually "train" the mucosal immune system, and the host must remain tolerant of them while confining them outside the epithelium ([7.15.23](/7.15.23)).

### 5.1.5. Internal Barriers

The **blood–brain barrier** consists of the tight junctions of brain capillary endothelium, the basement membrane, and the end-feet of astrocytes, and prevents pathogens and macromolecules in the blood from entering the central nervous system. The placental barrier consists of the maternal decidua basalis and the fetal chorionic trophoblast; it allows exchange of substances while blocking maternal pathogens, and it is not yet fully developed in early pregnancy, which is one reason infection with rubella virus, cytomegalovirus, and others in the first trimester readily causes birth defects. These sites also restrict the entry of immune cells and are related to **immune privilege** ([7.15.24](/7.15.24)).

![Components of the epithelial barrier (small intestine as example, schematic). Commensal bacteria (green) and a few pathogens (red) in the intestinal lumen are kept in the outer mucus layer; the inner mucus layer is dense and contains mucins secreted by goblet cells, antimicrobial peptides (small dots), and secretory IgA (Y shapes); epithelial cells are sealed by tight junctions; Paneth cells at the base of the crypts secrete defensins; in the subepithelial lamina propria are macrophages and dendritic cells, the latter of which can extend processes to sample luminal contents. Physical (epithelium, tight junctions, mucus), chemical (antimicrobial peptides), and microbial (colonization resistance of commensals) barriers act together at the same site](./plots/epithelial-barrier.py)

## 5.2. Phagocytes and Phagocytosis

### 5.2.1. Phagocytes

**Definition 5.2.1 (Phagocyte)** Cells that can recognize, engulf, and digest microbes and particles intracellularly are called **phagocytes**; in immunology the term mainly refers to the "professional" phagocytes: neutrophils, monocytes and macrophages, and dendritic cells.

In 1882 Metchnikoff pierced transparent starfish larvae with a rose thorn and observed motile cells gathering around the thorn, from which he proposed that phagocytes are the principal agents of defense ([7.15.1](/7.15.1)). It is now known that phagocytosis is far older in evolution than adaptive immunity: amoebae feed using the same molecular machinery, and all animals have phagocytes. The three kinds of professional phagocytes have different roles: neutrophils are the most numerous and respond fastest, killing on the spot after phagocytosis and soon dying; macrophages are long-lived and, besides killing, secrete cytokines and repair tissue; and the main purpose of phagocytosis by dendritic cells is not killing but handing antigen to T cells.

### 5.2.2. The Process of Phagocytosis

**Phagocytosis** ([7.3.11](/7.3.11)) comprises four steps:

1. Recognition and binding. Phagocytes grasp particles with two classes of receptors: pattern recognition receptors that directly recognize structures on the microbial surface (the mannose receptor CD206, scavenger receptors, dectin-1, and others, [7.15.6](/7.15.6)), and opsonic receptors that recognize antibodies and complement fragments bound to the microbial surface (Fc receptors CD64 and CD32, complement receptors CR1 and CR3). **Opsonization** raises the efficiency of phagocytosis by several orders of magnitude and is one of the most important effector actions of antibodies and **complement** ([7.15.10](/7.15.10), [7.15.21](/7.15.21)).
2. Engulfment. Receptor clustering triggers local actin polymerization, and pseudopods surround the particle to form a membrane-bound **phagosome**.
3. Phagosome maturation. The phagosome fuses successively with early endosomes, late endosomes, and lysosomes: the Rab protein marking it changes from Rab5 to Rab7, the V-type ATPase lowers the luminal pH to about 4.5, and finally fusion with lysosomes forms a **phagolysosome** that acquires hydrolytic enzymes such as proteases, lipases, and lysozyme.
4. Killing and degradation. In the phagolysosome the low pH, reactive oxygen and nitrogen species, antimicrobial peptides, and nutrient deprivation together kill the microbe ([7.15.7](/7.15.7)), and the remains are degraded; in macrophages and dendritic cells, the peptides produced by degradation are loaded onto MHC class II molecules for presentation ([7.15.14](/7.15.14)).

![Phagocytosis and phagosome maturation (schematic). A bacterium is recognized by opsonic receptors (when coated with antibody and complement) or pattern recognition receptors (1), and actin-driven pseudopods enclose it in a phagosome (2); the phagosome fuses successively with endosomes and lysosomes, the marker changes from Rab5 to Rab7, and the V-type ATPase acidifies the lumen (3); in the resulting phagolysosome, reactive oxygen species produced by NADPH oxidase, hydrolytic enzymes, and antimicrobial peptides kill and degrade the bacterium (4); the peptide fragments produced by degradation can be loaded onto MHC class II molecules and carried to the cell surface (5)](./plots/phagocytosis.py)

Phagocytes likewise engulf the large numbers of apoptotic cells produced in the body every day (**efferocytosis**). Apoptotic cells flip phosphatidylserine to the outer leaflet of the membrane as an "eat me" signal; healthy cells express CD47, which binds SIRPα on macrophages and transmits an inhibitory "don't eat me" signal. Many tumor cells overexpress CD47 to escape phagocytosis, and blocking CD47–SIRPα is a "macrophage checkpoint" therapeutic approach ([7.15.30](/7.15.30)). Macrophages that clear apoptotic cells secrete anti-inflammatory factors such as IL-10 and TGF-β and do not cause inflammation; failure to clear apoptotic cells in time releases nuclear antigens and is associated with autoimmune diseases such as systemic lupus erythematosus.

## 5.3. Monocytes and Macrophages

### 5.3.1. Tissue-Resident Macrophages

**Definition 5.3.1 (Tissue-Resident Macrophage)** Macrophages that at steady state reside long term in a tissue and perform the clearance and supportive functions specific to that tissue are called **tissue-resident macrophages**; most settle in the tissue during embryonic life from progenitors of the yolk sac or fetal liver and thereafter renew themselves in situ, while some tissues require continuous replenishment by blood monocytes.

| Tissue | Name | Main origin | Specific function |
|---|---|---|---|
| Brain | Microglia | Yolk sac, self-renewing throughout life | Pruning synapses, clearing debris and apoptotic neurons |
| Liver | Kupffer cells | Fetal liver, partly replenished by monocytes | Clearing bacteria, endotoxin, and senescent erythrocytes from portal blood |
| Lung | Alveolar macrophages | Fetal liver monocytes, self-renewing in situ | Clearing inhaled particles, degrading surfactant |
| Spleen | Red pulp macrophages, marginal zone macrophages | Embryonic origin and monocytes | Recycling iron from senescent erythrocytes; capturing blood-borne antigen |
| Bone | Osteoclasts | Fused multinucleated cells of the monocyte lineage | Bone resorption |
| Skin | Epidermal Langerhans cells; dermal macrophages | Embryonic origin (Langerhans cells); monocytes | Langerhans cells can migrate to lymph nodes to present antigen |
| Intestine | Lamina propria macrophages | Continuously replenished by monocytes | Phagocytose bacteria crossing the epithelium without causing inflammation |
| Peritoneal cavity, connective tissue | Peritoneal macrophages, histiocytes | Embryonic origin and monocytes | |

The identity of resident macrophages is "written" by the tissue environment: signals from the microenvironment induce particular transcription factors (PPARγ in alveolar macrophages, SALL1 in microglia, SPI-C in red pulp macrophages), so that cells of the same lineage behave very differently in different tissues. In infection and inflammation, classical monocytes in the blood enter tissue in large numbers via CCL2–CCR2 ([7.15.4](/7.15.4)) and differentiate into inflammatory macrophages or monocyte-derived dendritic cells, which fight together with resident macrophages.

### 5.3.2. Functions of Macrophages

Macrophages have five main functions: phagocytosing and killing pathogens (killing intracellular bacteria requires activation by IFN-γ, [7.15.17](/7.15.17)); secreting TNF, IL-1, IL-6, IL-12, chemokines, and so on to initiate and sustain inflammation; processing and presenting antigen to activate effector and memory T cells (naive T cells are activated mainly by dendritic cells); clearing apoptotic cells and debris and recycling iron; and secreting growth factors and remodeling matrix to take part in tissue repair and fibrosis.

### 5.3.3. Macrophage Polarization and Its Limits

**Definition 5.3.2 (Macrophage Polarization)** The process by which macrophages acquire different functional states under different cytokine and microbial signals is called **macrophage polarization**. The classical dichotomy calls the "classically activated" state induced by IFN-γ and lipopolysaccharide M1 and the "alternatively activated" state induced by IL-4 and IL-13 M2.

| | M1 (classical activation) | M2 (alternative activation) |
|---|---|---|
| Inducing signals | IFN-γ (Th1, NK) + TLR ligands | IL-4, IL-13 (Th2, ILC2); IL-10, glucocorticoids, and immune complexes induce other "M2-like" states |
| Corresponding effector module | Type 1 | Type 2; tissue repair |
| Typical products | iNOS (NO), reactive oxygen species, IL-12, IL-1β, TNF, CXCL9/10 | Arginase 1 (mouse), IL-10, TGF-β, chitinase-like proteins, profibrotic factors |
| Commonly used markers (human) | CD80, CD86, HLA-DR high | CD206, CD163, CD200R |
| Function | Killing intracellular pathogens, antitumor; also causes tissue damage | Encasing helminths, repairing tissue, promoting fibrosis; can promote growth in tumors |

M1/M2 is a useful starting point for understanding macrophage plasticity, but it consists of two extremes obtained in vitro by stimulating monocyte-derived macrophages with purified cytokines. Its limits should be kept in mind when reading the literature and tissue sections:

- The states of macrophages in vivo form a continuous spectrum rather than two classes; single-cell transcriptomes reveal many more states than two, and many cells express "M1" and "M2" markers simultaneously, tumor-associated macrophages in particular.
- Markers differ between species: iNOS and arginase 1 are the most commonly used M1/M2 markers in mice but are induced much more weakly in human macrophages.
- A single marker is not sufficient to judge state: CD163 and CD206 are also expressed on many resident macrophages and do not necessarily imply "alternative activation". When describing macrophages in spatial proteomics and pathology, it is therefore best to report the marker combination actually measured (such as CD68⁺CD163⁺) rather than writing "M2" directly ([7.15.35](/7.15.35)).

## 5.4. Granulocytes and Mast Cells

### 5.4.1. Neutrophils

Neutrophils are the first arrivals in acute inflammation and gather in large numbers within hours of infection ([7.15.7](/7.15.7)). Their weapons are preloaded in several classes of granules, listed in order of formation and ease of mobilization:

| Granule (order of formation) | Main contents | Mobilization |
|---|---|---|
| Azurophilic (primary) | Myeloperoxidase, elastase, cathepsin G, α-defensins | Hardest; mainly fuse with phagosomes |
| Specific (secondary) | Lactoferrin, procathelicidin, membrane subunits of NADPH oxidase | Easier |
| Gelatinase (tertiary) | Gelatinase (MMP-9) | Easy; helps cross the basement membrane |
| Secretory vesicles | Membrane stores of integrin Mac-1, complement receptors, FcγR | Easiest; first to fuse with the plasma membrane, increasing adhesion receptors |

The order of mobilization matches functional need: adhesion receptors are first delivered to the surface for adhesion and extravasation, matrix-degrading enzymes are then secreted to cross the tissue, and finally the most potent microbicidal components are used in the phagosome. The three modes of killing, killing within the phagolysosome, degranulation to the exterior, and release of **neutrophil extracellular traps** composed of DNA and granule proteins, are described in [7.15.7](/7.15.7). Neutrophils of patients with NADPH oxidase deficiency (**chronic granulomatous disease**) can engulf bacteria and fungi but cannot kill them, showing that the respiratory burst is one of their main microbicidal mechanisms ([7.15.31](/7.15.31)).

### 5.4.2. Eosinophils

The granules of eosinophils contain major basic protein, eosinophil cationic protein, eosinophil peroxidase, and eosinophil-derived neurotoxin; these strongly positively charged toxic proteins are effective against helminths too large to be phagocytosed: eosinophils adhere to the worm surface via IgE, IgG, or complement and release their granule contents onto the contact surface. Their production and survival depend on IL-5, and their recruitment depends on eotaxin (CCL11) and CCR3; they are representative effector cells of type 2 immunity, and in allergic diseases such as asthma the same toxic proteins damage the airway epithelium. At steady state large numbers of eosinophils reside in the gastrointestinal mucosa and take part in tissue maintenance.

### 5.4.3. Basophils, Mast Cells, and Degranulation

**Definition 5.4.1 (Degranulation)** The process in which, after stimulation of a granulated cell, secretory granules in the cytoplasm fuse with the plasma membrane and release their preformed contents to the exterior is called **degranulation**.

The mast cell is the typical example of degranulation: after multivalent antigen cross-links IgE bound to FcεRI, granules can be released within tens of seconds. The mediators released are of three classes according to how they are produced:

| Class | Mediators | Time of appearance | Action |
|---|---|---|---|
| Preformed (in granules) | Histamine, tryptase, chymase, heparin, some TNF | Seconds to minutes | Vasodilation and increased permeability, smooth-muscle contraction, degradation of tissue proteins |
| Newly synthesized lipid mediators | Prostaglandin D2, leukotriene C4, platelet-activating factor | Minutes | Sustained bronchoconstriction, mucus secretion, leukocyte recruitment |
| Cytokines and chemokines | IL-4, IL-5, IL-13, TNF, CCL3, and others | Hours | Sustain type 2 inflammation, recruit eosinophils |

Besides IgE cross-linking, the complement fragments C3a and C5a (**anaphylatoxins**), certain drugs and neuropeptides (via the receptor MRGPRX2), and TLR ligands of pathogens can also activate mast cells. Human mast cells are divided by protease content into the mucosal type, containing only tryptase, and the connective tissue type, containing both tryptase and chymase. Basophils circulate in the blood and, after recruitment to inflamed tissue, release histamine and large amounts of IL-4 and serve as early amplifiers of type 2 responses. In antiparasitic immunity degranulation causes the "weep and sweep" response (mucus secretion, increased intestinal motility), and in type I hypersensitivity it causes the symptoms of allergy ([7.15.26](/7.15.26)). Mast cells are also distributed around blood vessels and are among the earliest "sentinels" at a site of infection: the TNF and histamine they release begin to alter local vessels before neutrophils arrive.

## 5.5. NK Cells

### 5.5.1. Receptor Balance and "Missing Self"

NK cells do not express clonally specific antigen receptors, yet they can distinguish healthy cells from cells infected with viruses or malignantly transformed. Their judgment relies on two sets of germline-encoded receptors, and whether to kill depends on the balance of the two sets of signals.

| Class | Receptors | Ligands | Signal |
|---|---|---|---|
| Inhibitory (recognizing "self") | KIR family (KIR2DL, KIR3DL; CD158) | HLA-C, some HLA-B and HLA-A alleles | The cytoplasmic ITIM recruits the phosphatase SHP-1, which counteracts activating signals |
| | CD94/NKG2A | HLA-E (presenting signal peptides of other HLA class I molecules) | ITIM |
| | LILRB1 | Many HLA class I molecules | ITIM |
| Activating (recognizing "abnormality") | NKG2D (CD314) | MICA, MICB, ULBP, and other "stress ligands": induced by DNA damage, infection, transformation | Activates PI3K via the adaptor DAP10 |
| | Natural cytotoxicity receptors NKp30, NKp44, NKp46 | Certain viral proteins, ligands on tumor cells (B7-H6 and others) | Via ITAM-containing adaptors |
| | CD16 (FcγRIIIa) | Fc portion of IgG bound to the target cell | Via ITAM, mediates ADCC |
| | DNAM-1 (CD226), activating KIRs | CD155, CD112; some HLA | |

**Definition 5.5.1 (Missing Self)** The recognition principle in which MHC class I molecules expressed by normal cells are recognized by inhibitory receptors of NK cells so that they are not killed, whereas cells with reduced or absent MHC class I expression lose this protection and are killed by NK cells, is called **missing self**.

The missing-self hypothesis was proposed by Kärre in the 1980s: he found that NK cells preferentially kill tumor cells lacking MHC class I molecules. It is complementary to recognition by CTLs: many viruses (such as herpesviruses and HIV) and tumors downregulate MHC class I molecules to escape CTLs and thereby become targets of NK cells; and to evade both, some cytomegaloviruses even encode "decoys" that mimic MHC class I molecules to bind inhibitory receptors. Alongside "missing self" is "induced self": when cells are stressed they express activating ligands such as NKG2D ligands, and even if MHC class I molecules are normal the activating signal may overcome the inhibitory signal.

During development NK cells must also undergo "education" (licensing): only NK cells whose inhibitory receptors can recognize self MHC class I molecules acquire full killing capacity. This ensures that the reactivity of mature NK cells matches the host's own MHC and is the self-tolerance mechanism of NK cells.

### 5.5.2. Killing Mechanisms

NK cells and CTLs share one contact-dependent killing mechanism. After deciding to kill, the NK cell forms a cytolytic **immunological synapse** at the contact surface and transports cytotoxic granules along microtubules to the contact surface for release.

**Definition 5.5.2** The cytotoxic granules of NK cells and CTLs contain two classes of key molecules: **perforin**, which in the presence of $\ce{Ca^2+}$ inserts into the target cell membrane and polymerizes into transmembrane pores, and **granzymes**, serine proteases that enter the target cell through the perforin pores and cleave substrates to induce apoptosis.

Granzyme B cleaves after aspartate residues and directly activates caspase-3 or cleaves BID to trigger the mitochondrial pathway (the **intrinsic pathway** of apoptosis), causing the target cell to undergo apoptosis within minutes ([7.3.25](/7.3.25)); the proteoglycan serglycin and the lysosomal membrane protein CD107a in the granules protect the NK cell itself (the appearance of CD107a on the cell surface is also used as a flow cytometry marker of degranulation). Besides the granule pathway, NK cells also use FasL and TRAIL expressed on their surface to bind **death receptors** on the target cell and initiate the **extrinsic pathway** of apoptosis; they recognize IgG coating target cells through CD16 and carry out **antibody-dependent cell-mediated cytotoxicity** (ADCC); and they secrete IFN-γ to activate macrophages and promote Th1 responses, their innate role in type 1 immunity.

Puncturing the cell membrane is a recurrent means of killing in the immune system; the three modes are compared below:

| Pore | Direction of assembly | Formed by | Consequence |
|---|---|---|---|
| Perforin pore | Inserted into the target cell membrane from outside to inside | NK cells, CTLs | Granzymes enter, target cell undergoes apoptosis |
| Membrane attack complex (C5b–C9) | From outside to inside | Complement ([7.15.10](/7.15.10)) | Lysis of cells (especially gram-negative bacteria) |
| Gasdermin D pore | From inside to outside | Caspase-1 activated by inflammasomes cleaves gasdermin D | Release of IL-1β and IL-18, pyroptosis ([7.15.6](/7.15.6)) |

### 5.5.3. A Threshold Model of the Killing Decision

The decision of an NK cell can be illustrated by a simple model. Let the activating signal strength provided by the target cell be $S_{\mathrm{a}}$ (increasing with stress ligands) and the inhibitory signal strength be $S_{\mathrm{i}}$ (increasing with MHC class I molecules); the NK cell integrates the two and kills when the net signal exceeds the threshold $\theta$:

$$
p_{\mathrm{kill}} = \frac{1}{1 + \exp\!\big(-\beta\,(S_{\mathrm{a}} - S_{\mathrm{i}} - \theta)\big)},
$$

where $\beta$ characterizes the steepness of the decision. This model is only illustrative, but it makes three points: (1) healthy cells have a strong inhibitory signal and a weak activating signal and fall in the non-killing region; (2) loss of MHC class I molecules (decreased $S_{\mathrm{i}}$) or expression of stress ligands (increased $S_{\mathrm{a}}$) can push a cell across the threshold; (3) because of the threshold, cells with only partial downregulation of MHC class I molecules are not necessarily killed, which is also why tumors can "partially escape". NK cell education corresponds to adjusting $\theta$: unlicensed cells have a higher threshold.

![Threshold model of the NK cell killing decision (schematic, parameters without units). A: heat map of the killing probability $p_{\mathrm{kill}}$ as a function of the activating signal $S_{\mathrm{a}}$ (horizontal axis, stress ligands) and the inhibitory signal $S_{\mathrm{i}}$ (vertical axis, MHC class I molecules); the white dashed line is the decision boundary $p_{\mathrm{kill}} = 1/2$. A healthy cell (high MHC I, low stress ligands) lies in the non-killing region; a virus-infected cell with downregulated MHC class I molecules ("missing self") and a tumor cell expressing stress ligands ("induced self") cross the boundary downward along the vertical axis and rightward along the horizontal axis, respectively. B: curves of the killing probability rising as the MHC class I level of the target cell falls, for a given activating signal; when the threshold $\theta$ is higher (unlicensed NK cells), more complete MHC loss is required](./plots/nk-decision.py)

## 5.6. Innate Lymphoid Cells

**Definition 5.6.1 (Innate Lymphoid Cell)** **Innate lymphoid cells** (ILCs) are lymphocytes with lymphocyte morphology that depend on the transcriptional regulator Id2 for development, express neither rearranged antigen receptors nor markers of other lineages, reside mainly in barrier tissues, and are rapidly activated by cytokines secreted by epithelial and myeloid cells.

ILCs were systematically recognized only around 2010, but they provide a key to understanding immunology: the subsets of ILCs correspond one to one with the subsets of CD4⁺ T cells, use the same master transcription factors, and secrete the same effector cytokines. The difference lies in the mode of initiation: T-cell subsets must first undergo antigen selection, clonal expansion, and differentiation, which takes days, whereas ILCs already reside in tissues and are activated directly by cytokines within hours. ILCs are therefore the "innate vanguard" of type 1, 2, and 3 immunity.

| Group | Master regulators | Activating signals | Effector molecules | Corresponding T cell | Main role |
|---|---|---|---|---|---|
| NK cells | T-bet, EOMES | IL-12, IL-15, IL-18; target cells | Perforin, granzymes, IFN-γ | CD8⁺ CTL | Killing (§5.5) |
| ILC1 | T-bet | IL-12, IL-15, IL-18 | IFN-γ, TNF | Th1 | Type 1: intracellular pathogens |
| ILC2 | GATA3 | IL-25, IL-33, TSLP (epithelial "alarmins") | IL-5, IL-13, amphiregulin | Th2 | Type 2: helminths, tissue repair; allergy and asthma |
| ILC3 | RORγt | IL-1β, IL-23 | IL-17, IL-22, GM-CSF | Th17 | Type 3: extracellular bacteria and fungi; epithelial barrier |
| Lymphoid tissue inducer cells (LTi) | RORγt | | Lymphotoxin | — | Induce formation of lymph nodes and Peyer's patches in the embryo |

ILCs are far fewer than T cells in tissues, but their role in the first hours of a response is great: for example, IL-22 secreted by intestinal ILC3s induces the epithelium to produce REG3 antimicrobial peptides and maintains the barrier, and in its absence commensals cross the epithelium and cause systemic inflammation; lung ILC2s rapidly secrete IL-5 and IL-13 after viral damage to the epithelium releases IL-33 and play an important role in acute asthma attacks. Because ILCs have no specific marker, they are usually identified as "lineage-negative, CD127⁺" together with the master regulators.

## 5.7. Innate-Like Lymphocytes

Among T cells and B cells there are also some "unconventional" subsets: they have rearranged antigen receptors, but the diversity of the receptors is very limited, they recognize highly conserved nonpeptide antigens, and they have acquired effector functions in advance during development, so that they can respond rapidly on stimulation without clonal expansion. They lie between innate and adaptive immunity and are collectively called innate-like lymphocytes.

**Definition 5.7.1 (γδ T Cell)** **γδ T cells** are T cells that express a TCR composed of a γ chain and a δ chain; most are not restricted by classical MHC and recognize phosphoantigens (intermediates of the isoprenoid synthesis pathway, presented via butyrophilin molecules), stress-induced molecules, or lipids, and are found mainly in epithelia such as skin and gut.

γδ T cells make up only 1%–5% of T cells in human peripheral blood, but in some epithelia they are the main T cells. The most abundant in human peripheral blood are Vγ9Vδ2 cells, which recognize phosphoantigens accumulated in bacteria and infected cells (such as HMB-PP) and respond rapidly to many bacterial and protozoan infections. The dendritic epidermal T cells of mouse skin all use the same γδ TCR and, like "sensors", monitor keratinocytes for stress. γδ T cells can secrete IFN-γ or IL-17 and can also kill target cells.

**Definition 5.7.2 (NKT Cell)** **NKT cells** (natural killer T cells) are T cells that express both an αβ TCR and NK cell receptors (such as NK1.1 and CD161); their main subset, invariant NKT cells (iNKT), expresses a nearly invariant TCR α chain (Vα24–Jα18 in humans, Vα14–Jα18 in mice) and recognizes glycolipid antigens presented by the nonclassical MHC molecule CD1d.

After activation by glycolipids (in experiments, α-galactosylceramide derived from sponges is often used), iNKT cells secrete large amounts of both IFN-γ and IL-4 within minutes to hours and can rapidly influence the direction of the subsequent adaptive response. Similar are the *mucosal-associated invariant T cells* (MAIT cells), which use an invariant TCR α chain to recognize bacterial riboflavin-synthesis intermediates presented by the MR1 molecule and are abundant in human blood and liver.

The **B-1 cell** among B cells is the corresponding innate-like B cell: found mainly in the peritoneal and pleural cavities, with limited receptor diversity biased toward recognizing conserved structures such as bacterial polysaccharides and phosphorylcholine, they produce "natural IgM" without T-cell help, antibodies that are present in serum even without infection and form an early line of defense against bacteria ([7.15.19](/7.15.19)).

| | Receptor | Recognizes | Presenting molecule | Main effector action |
|---|---|---|---|---|
| γδ T cells | γδ TCR, limited diversity | Phosphoantigens, stress molecules, lipids | Butyrophilin; not restricted to MHC | IFN-γ or IL-17; killing |
| iNKT cells | αβ TCR with invariant α chain | Glycolipids | CD1d | Rapid secretion of IFN-γ and IL-4 |
| MAIT cells | αβ TCR with invariant α chain | Riboflavin metabolic intermediates | MR1 | IFN-γ, IL-17; killing |
| B-1 cells | BCR of limited diversity | Polysaccharides, phosphorylcholine | Not required | Natural IgM |

## Summary

- Barriers are of three kinds, physical (skin, tight junctions, mucus and mucociliary clearance), chemical (pH, **lysozyme**, lactoferrin, **antimicrobial peptides** and **defensins**, Definition 5.1.1), and microbial (colonization resistance by commensals), plus internal barriers such as the blood–brain barrier and the placental barrier.
- **Phagocytes** (Definition 5.2.1) clear microbes by recognition (PRRs or opsonic receptors) → engulfment → phagosome maturation (Rab5→Rab7, acidification, fusion with lysosomes) → killing and degradation; the clearance of apoptotic cells is controlled by "eat me" (phosphatidylserine) and "don't eat me" (CD47–SIRPα) signals.
- **Tissue-resident macrophages** (Definition 5.3.1) are mostly of embryonic origin and self-renew in situ, with identity determined by the tissue environment; M1/M2 of **macrophage polarization** (Definition 5.3.2) are two extremes in vitro, in vivo there is a continuous spectrum, and the marker combination actually measured should be reported.
- The weapons of granulated cells are stored in advance: the four classes of neutrophil granules are mobilized in order of need; the cationic toxic proteins of eosinophils deal with helminths; **degranulation** (Definition 5.4.1) of mast cells and basophils releases preformed mediators, newly synthesized lipid mediators, and cytokines and is the effector of type 2 immunity and allergy.
- **NK cells** decide whether to kill by the balance of inhibitory receptors (KIR, CD94/NKG2A: recognizing MHC I) and activating receptors (NKG2D, NCRs, CD16: recognizing stress ligands and IgG); **missing self** (Definition 5.5.1) is complementary to recognition by CTLs. Killing uses **perforin** and **granzymes** (Definition 5.5.2), death receptors, and ADCC; the threshold model $p_{\mathrm{kill}} = \sigma(\beta(S_{\mathrm{a}} - S_{\mathrm{i}} - \theta))$ summarizes this decision.
- **Innate lymphoid cells** (Definition 5.6.1) correspond one to one with T-cell subsets:

  | Innate | NK | ILC1 | ILC2 | ILC3 |
  |---|---|---|---|---|
  | Adaptive | CTL | Th1 | Th2 | Th17 |
  | Master regulators | T-bet, EOMES | T-bet | GATA3 | RORγt |
  | Effector module | Type 1 | Type 1 | Type 2 | Type 3 |

- Innate-like lymphocytes (**γδ T cells**, **NKT cells**, MAIT cells, B-1 cells) have rearranged receptors of limited diversity, recognize conserved nonpeptide antigens, and have effector functions preformed.

## Questions

1. Why can cationic antimicrobial peptides selectively disrupt microbial membranes while largely sparing host cells? Under what circumstances does this selectivity fail?

   **Answer** The outer layer of microbial membranes is rich in negatively charged phospholipids, lipopolysaccharide, and teichoic acid, and positively charged amphipathic antimicrobial peptides bind and insert preferentially through electrostatic interaction; the outer layer of host cell membranes is mainly electrically neutral phosphatidylcholine and sphingomyelin and contains cholesterol, so binding is weak and the membrane more stable. When the concentration of antimicrobial peptide is very high (such as LL-37 at some sites of inflammation) or when the outer leaflet of host cell membranes exposes negatively charged phosphatidylserine (apoptotic or damaged cells), the selectivity falls and the antimicrobial peptides also damage host cells.

2. A tumor cell line completely lacks β2-microglobulin and therefore has no MHC class I molecules on its surface. Predict its sensitivity to CTLs and NK cells and explain why.

   **Answer** Without MHC class I molecules, CTLs cannot recognize any peptide it would present, so it is insensitive to CTLs; but the inhibitory receptors of NK cells, such as KIR and CD94/NKG2A, lose their ligands (surface expression of HLA-E also depends on β2-microglobulin), and by the "missing self" principle, as long as the cell expresses some activating ligands it will be killed by NK cells. This is also the rationale for using NK cells (or enhancing NK activity) against tumors that have become resistant to CTLs.

3. In a tumor section, many CD68⁺ cells express both CD163 and HLA-DR. Can they be called "M2 macrophages" on this basis? How should they be described?

   **Answer** They should not. CD163 is often treated as an "M2" marker, but it is also expressed on many tissue-resident macrophages; high HLA-DR is often treated as a marker of "M1" or of activation; their coexpression shows that the states in vivo are continuous and mixed and that the dichotomy does not apply. The actual phenotype (such as CD68⁺CD163⁺HLA-DR⁺ macrophages) and its spatial location should be reported, and where necessary the functional state should be described using more markers (CD206, CD86, PD-L1, proliferation markers) or transcriptomic data.

4. Use the model of §5.5.3 to explain why a virus that partially downregulates MHC class I molecules may escape both CTLs and NK cells.

   **Answer** Recognition by CTLs requires a sufficient number of viral peptide–MHC I complexes, and downregulating MHC class I molecules reduces these complexes and can lower recognition by CTLs; for NK cells to kill, $S_{\mathrm{a}} - S_{\mathrm{i}}$ must exceed the threshold $\theta$. If MHC class I molecules are only partially downregulated, the remaining inhibitory signal may still keep the net signal below threshold, and the cell falls on the non-killing side of the decision boundary. Many viruses selectively downregulate HLA-A and HLA-B, which present peptides, while retaining HLA-C and HLA-E, the main inhibitory ligands of NK cells, and thus find a "window" between the two.

5. (Open question) ILC2s and Th2 cells secrete the same cytokines. Devise an experiment to distinguish their contributions in the early and late phases of a helminth infection in mice.

   **Answer** Idea: exploit the difference between them, that ILC2s have no rearranged antigen receptor. Compare *Rag*-deficient mice (no T or B cells but ILC2s present), mice in which ILC2s are removed on top of *Rag* deficiency (for example conditional deletion of *Il7ra* or *Rora*, or *Il2rg* deletion to remove all ILCs), and wild-type mice; measure intestinal IL-13, eosinophil recruitment, goblet cell hyperplasia, and worm expulsion at various times after infection. If the early (within days) type 2 response is still present in *Rag*-deficient mice but absent in mice lacking ILCs, the early response is driven mainly by ILC2s; late worm expulsion and IgE depend on T cells. Cytokine reporter mice combined with flow cytometry can also be used to distinguish the cellular source of IL-13. Note that genetic deletions may have other effects, and several models should be used to corroborate one another.
