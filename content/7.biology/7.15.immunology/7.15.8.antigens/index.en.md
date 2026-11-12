---
title: Antigens
description: What adaptive immunity recognizes. Immunogenicity and antigenicity, the hapten–carrier effect, linear and conformational epitopes, T-cell and B-cell epitopes, shared epitopes and cross-reactivity, factors that affect immunogenicity, thymus-dependent and thymus-independent antigens and other classifications, and the nonspecific immune stimulators (superantigens, adjuvants and mitogens); with a simple model of BCR cross-linking.
source_hash: 025dd24bcb5f
---

Innate immunity recognizes molecular patterns shared by whole classes of microbes ([7.15.6](/7.15.6)); adaptive immunity recognizes specific molecular structures, and can recognize almost any structure. This chapter gives the adaptive-immunity answer to the question "what is recognized?" on the path of knowledge ([7.15.1](/7.15.1)): what kinds of substances can be recognized by T and B lymphocytes, what kinds can elicit a response, and why these are not the same thing.

The basic definitions of **antigen**, **epitope** and **hapten** were given in [7.1.7](/7.1.7) from the standpoint of protein–ligand interactions and are not repeated here; this chapter discusses their immunological meaning. Several distinctions made here run through the whole course: B cells recognize the shape of the surface of an intact molecule, whereas T cells recognize peptides that have been processed and are presented by MHC molecules ([7.15.13](/7.15.13), [7.15.14](/7.15.14)); most antibody responses require T-cell help, but a few do not ([7.15.20](/7.15.20)); and whether a molecule elicits a response depends not only on the molecule itself but also on whether innate immunity simultaneously supplies a "danger" signal, which is the principle behind adjuvants ([7.15.33](/7.15.33)). The molecules that bind antigens, antibodies, are the subject of the next chapter ([7.15.9](/7.15.9)).

## 8.1. Two Basic Properties of Antigens

### 8.1.1. Immunogenicity and Antigenicity

That a molecule is "recognized by the immune system" can mean two things: it can be bound by existing antibodies or lymphocytes, or it can elicit a new response. The two require different conditions.

**Definition 8.1.1 (Immunogenicity and Antigenicity)** The ability of a substance to stimulate an adaptive immune response (activation, proliferation and differentiation of specific lymphocytes, with production of antibodies or effector T cells) is called **immunogenicity**; the ability of a substance to bind specifically to the products of a response (antibodies, TCRs or BCRs) is called **antigenicity** (also called immunoreactivity). A substance with both properties is a complete antigen (an immunogen); a substance with antigenicity but no immunogenicity is an incomplete antigen, that is, a hapten.

Every substance that is immunogenic is also antigenic, but not the reverse. A small molecule such as dinitrophenyl (DNP) can be bound by antibodies but does not elicit antibodies when injected alone; when it is covalently attached to a protein such as bovine serum albumin, it induces antibodies against itself, and these antibodies also bind the free small molecule. In the literature the substance that elicits a response is often called an immunogen and the substance that is bound is called an antigen; in everyday use the two terms are frequently interchanged, and where the distinction is needed this course writes immunogen and antigen.

### 8.1.2. The Hapten–Carrier Effect

Why does a hapten need a carrier? The answer is that B-cell activation requires T-cell help, and T cells recognize only peptides.

**Definition 8.1.2 (Hapten–Carrier Effect)** The **hapten–carrier effect** is the requirement that an antibody response to a hapten (especially a secondary response) needs the hapten to be linked to a carrier protein to which the organism has previously been primed. The B cell that recognizes the hapten binds and internalizes the hapten–carrier conjugate through its BCR and presents peptides of the carrier on MHC class II molecules, and helper T cells that recognize the carrier peptide provide the help.

This mechanism is called linked recognition: the epitopes recognized by the B cell and by the T cell may differ, but they must lie on the same molecule (or the same particle), so that the help is delivered to the very B cell that recognized the antigen. The classical carrier-priming experiment shows this. In mice primed with DNP–ovalbumin and boosted with DNP–bovine serum albumin, the secondary anti-DNP response is weak; the secondary response appears only if the carrier used for the boost is the same as for priming, or if T cells primed to the new carrier are transferred in addition.

![Units of antigen recognition. A: Two kinds of B-cell epitopes on a protein formed by folding of one polypeptide chain. A linear epitope consists of residues contiguous in sequence (red) and can still be recognized by antibodies after denaturation; a conformational epitope consists of residues that are distant in sequence but close together in the folded structure (blue) and disappears on denaturation. A T-cell epitope (yellow) can lie inside the molecule and is presented by MHC molecules after processing into a short peptide. B: The hapten–carrier effect. The B cell binds the hapten (diamond) with its BCR, internalizes the whole conjugate, and presents peptides of the carrier protein on MHC class II molecules; a helper T cell that recognizes the carrier peptide provides help through CD40L and cytokines, and the B cell then produces anti-hapten antibodies](./plots/epitopes.py)

The hapten–carrier effect has two corollaries. One is drug allergy: certain drugs or their metabolites bind covalently to self proteins, which become carriers and so elicit antibodies against the drug ([7.15.26](/7.15.26), [7.15.27](/7.15.27)). The other is the principle of the **conjugate vaccine**: a polysaccharide antigen cannot by itself obtain T-cell help (§8.4.1), but once it is covalently attached to a protein carrier, polysaccharide-specific B cells can obtain help from carrier-specific T cells through linked recognition and produce class-switched antibodies and memory ([7.15.33](/7.15.33)).

## 8.2. Epitopes

### 8.2.1. Size and Number of Epitopes

An **epitope** is the smallest structural unit of an antigen that is recognized by one antibody or one TCR. A protein antigen usually has many epitopes, and a hapten corresponds to one. A B-cell epitope typically consists of 5–15 amino acid residues (or 5–7 monosaccharide residues), and the area of contact with the antibody combining site is about $7$–$9\ \mathrm{nm^2}$ ([7.1.7](/7.1.7)). A T-cell epitope is a peptide of 8–10 residues presented by MHC class I molecules or of 13–25 residues presented by MHC class II molecules (a core of about 9 residues lies in the binding groove).

Although an antigen has many potential epitopes, the response is often concentrated on a few of them, called immunodominant epitopes. For T cells, immunodominance depends on whether the peptide is efficiently generated by cleavage, whether it binds the MHC alleles the individual carries, and whether corresponding T cells are present in the periphery; for B cells it depends on the accessibility and flexibility of the epitope and on its difference from self molecules.

### 8.2.2. Linear and Conformational Epitopes

**Definition 8.2.1 (Linear and Conformational Epitopes)** An epitope made up of amino acid residues that are contiguous in the sequence of a polypeptide chain is called a **linear epitope** (sequential epitope); an epitope made up of residues that are discontiguous in sequence but close together in the folded three-dimensional structure is called a **conformational epitope**.

The two can be distinguished by denaturation: a conformational epitope disappears when the protein is denatured, whereas a linear epitope is unaffected and may even bind more readily once exposed. Most B-cell epitopes of native proteins are conformational (structural analyses estimate about 90%), so antibodies raised against denatured protein (for example, the bands on a **Western blot**) often do not bind the native protein, and vice versa. This matters in practice in pathology and spatial proteomics: formaldehyde fixation and paraffin embedding alter protein conformation, and whether an antibody can be used for **immunohistochemistry** depends on whether its epitope is still present after fixation and antigen retrieval ([7.15.34](/7.15.34)).

### 8.2.3. T-Cell Epitopes and B-Cell Epitopes

**Definition 8.2.2 (T-Cell Epitopes and B-Cell Epitopes)** An epitope recognized by a TCR is called a **T-cell epitope**: it is a linear peptide produced by processing of the antigen in an antigen-presenting cell and bound in the peptide-binding groove of an MHC molecule, and the TCR recognizes the peptide and the MHC together. An epitope recognized directly by a BCR or antibody is called a **B-cell epitope**: it lies on the surface of the intact antigen molecule, needs neither processing nor MHC, may be conformational or linear, and may be chemically a protein, polysaccharide, lipid or nucleic acid.

| | T-cell epitope | B-cell epitope |
|---|---|---|
| Recognition receptor | TCR (with the CD4 or CD8 coreceptor) | BCR, antibody |
| MHC molecule | Required (MHC restriction) | Not required |
| Chemical nature | Almost always peptides (lipids presented by CD1 are the exception) | Proteins, polysaccharides, lipopolysaccharides, nucleic acids, small molecules |
| Size | MHC I: 8–10 residues (CD8⁺ T cells); MHC II: 13–25 residues (CD4⁺ T cells) | 5–15 residues |
| Type | Linear | Mostly conformational, may be linear |
| Location | Anywhere in the molecule, including the interior | On the surface, accessible |
| Processing needed | Yes ([7.15.14](/7.15.14)) | No |

T-cell epitopes must be presented by MHC because of what T cells do: they must judge the state of a cell, not whether a certain molecule is present in solution. MHC displays protein fragments from inside the cell (class I) or from what the cell has taken up (class II) on the surface, and the T cell thereby "sees" the inside of the cell; the price is that the T cell cannot see the shape of the intact molecule or most non-protein antigens. On the same protein, B cells and T cells therefore often recognize entirely different sites, which is the premise that makes linked recognition (§8.1.2) possible.

### 8.2.4. Shared Epitopes and Cross-Reactivity

**Definition 8.2.3 (Cross-Reactivity)** Identical or similar epitopes on different antigens are called shared epitopes (common antigens), and different antigens bearing a shared epitope are called cross-reacting antigens. The binding of antibodies or sensitized lymphocytes raised against one antigen to another antigen bearing a shared epitope is called **cross-reactivity**.

Cross-reactivity is a matter of degree: binding of an antibody to a similar epitope is usually weaker, and affinity declines progressively as the structures diverge. It matters in three ways:

- Protection: immunity to one antigen can protect against another antigen bearing a shared epitope, which was the historical basis for immunizing with related antigens.
- Damage: when a foreign antigen shares an epitope with a self molecule, the response to the foreign antigen may attack self tissue, which is called **molecular mimicry** and is one cause of autoimmune disease ([7.15.28](/7.15.28)).
- Detection: in immunological assays, cross-reactivity causes false positives, and diagnostic antigens and antibodies should be chosen to use specific epitopes; in experiments, cross-reaction of an antibody with homologous proteins of the same family is a problem that **antibody validation** must exclude ([7.15.34](/7.15.34)).

Common antigens that are widespread among different species are called heterophile antigens (Forssman antigens); for example, certain glycolipid epitopes are present both in the tissues of many animals and on the surface of microbes. The antibodies against ABO blood-group antigens that occur naturally in humans are generally believed to be cross-reactive antibodies induced by carbohydrates of gut bacteria that resemble the blood-group carbohydrate structures.

## 8.3. Factors Affecting Immunogenicity

Immunogenicity is not an intrinsic property of a molecule; it is determined jointly by the molecule, the host and the manner of exposure.

| Category | Factor | Rule |
|---|---|---|
| Antigen molecule | Foreignness | The more distant the relationship to the host and the greater the structural difference, the stronger the immunogenicity; self components that the immune system never encountered during development (sequestered antigens) also count as foreign |
| | Chemical nature | Proteins are strongest, then polysaccharides; lipids and nucleic acids are weak alone and strengthened when bound to proteins |
| | Molecular weight | Molecules larger than about $10\ \mathrm{kDa}$ are usually strongly immunogenic, and those smaller than $5\ \mathrm{kDa}$ are often haptens |
| | Structural complexity | Molecules containing aromatic amino acids and of complex structure are stronger; homopolymers of a single amino acid are very weak |
| | Conformation and accessibility | The epitope must lie on the surface where the BCR can reach it |
| | Degradability | The molecule must be processable by proteases to yield T-cell epitopes: polypeptides made of D-amino acids cannot be degraded and are poorly immunogenic |
| | Physical state | Aggregated, particulate antigens are stronger than soluble monomers because they are taken up more readily by phagocytes and can cross-link BCRs |
| Host | Genetic background | The MHC alleles an individual carries determine whether peptides of a given antigen can be presented ([7.15.13](/7.15.13)); the same antigen can be a high or low responder in different strains of animals |
| | Age, sex and health | Newborns and the elderly respond more weakly; females generally mount stronger antibody responses and also suffer more autoimmune disease |
| Manner of exposure | Dose | A moderate dose elicits a response; doses that are too low or too high can induce **immune tolerance** (low-zone and high-zone tolerance) |
| | Route | Intradermal and subcutaneous routes are stronger than intramuscular, and intramuscular stronger than intraperitoneal and intravenous; oral exposure often induces **oral tolerance** |
| | Frequency | Repeated exposure at suitable intervals (weeks) enhances the response (**booster immunization**); too frequent exposure can cause tolerance |
| | Adjuvant | An adjuvant given with the antigen markedly enhances the response (§8.5.2) |

## 8.4. Classification of Antigens

### 8.4.1. Thymus-Dependent and Thymus-Independent Antigens

According to whether helper T cells are needed to stimulate B cells to produce antibody, antigens fall into two classes. This classification is the most useful, because it determines the quality of the antibody response.

**Definition 8.4.1 (Thymus-Dependent and Thymus-Independent Antigens)** An antigen that requires the participation of helper T cells to stimulate B cells to produce antibody is called a **thymus-dependent antigen** (TD antigen); most protein antigens belong to this class. An antigen that can stimulate B cells to produce antibody without T-cell help is called a **thymus-independent antigen** (TI antigen). TI antigens are further divided into two types: TI-1 antigens (such as **lipopolysaccharide**) activate polyclonal B cells nonspecifically at high concentrations, through **Toll-like receptors** and other receptors; TI-2 antigens (such as polysaccharides and polymeric flagellin) carry many identical epitopes in a repetitive array and activate B cells by extensively cross-linking BCRs.

The name "thymus-dependent" comes from congenitally athymic nude mice: they lack T cells and cannot make antibodies against most proteins, yet can still respond to certain polysaccharides.

| | TD antigen | TI antigen |
|---|---|---|
| Chemical nature | Mainly proteins | Polysaccharides, lipopolysaccharides, polymeric proteins, etc. |
| Epitopes | Both B-cell and T-cell epitopes | Repeated B-cell epitopes, no T-cell epitopes |
| T-cell help | Required (linked recognition) | Not required |
| Main responding B cells | **Follicular B cells** (B-2) | **Marginal zone B cells**, **B-1 cells** |
| Germinal center | Formed | Essentially not formed |
| Antibody class | IgM, then class switching to IgG, IgA, IgE | Mainly IgM, little IgG |
| Affinity maturation | Yes | Very weak |
| Immunological memory | Yes | Very weak or absent |
| Type of immunity elicited | Humoral immunity, accompanied by cell-mediated immunity | Humoral immunity |

The TI-2 response depends on marginal zone B cells, and the human splenic marginal zone does not mature until about 2 years of age, so infants and young children respond poorly to pure polysaccharide antigens; this is why conjugate vaccines (§8.1.2) turn a TI-2 antigen into a TD antigen.

### 8.4.2. Classification by Relationship Between Antigen and Host

| Category | Meaning | Examples |
|---|---|---|
| Xenogeneic antigen | Antigen from another species | Microbial antigens, heterologous animal serum, xenografts |
| Alloantigen | Antigen that differs between individuals of the same species | Blood-group antigens, HLA |
| Autoantigen | Self component that can elicit an autoimmune response | Sequestered antigens, modified self molecules |
| Heterophile antigen | Common antigen shared among different species | Forssman antigen |
| Idiotypic antigen | Structure peculiar to the variable region of an antibody, TCR or BCR | Epitopes recognized by anti-idiotypic antibodies ([7.15.9](/7.15.9)) |

**Definition 8.4.2 (Alloantigens and Autoantigens)** An antigen that differs between individuals of the same species because of genetic polymorphism is called an **alloantigen** (allogeneic antigen); a self component that can be recognized by the individual's own immune system and elicit a response is called an **autoantigen**.

Alloantigens are the targets of immune reactions in transfusion and transplantation: the ABO and Rh **blood groups** determine transfusion compatibility, and HLA determines histocompatibility in organ transplantation ([7.15.13](/7.15.13), [7.15.29](/7.15.29)). Normally self components elicit no response, as a result of **immune tolerance** ([7.15.24](/7.15.24)). Self components become autoantigens by several routes: components sequestered from the immune system during development (such as lens protein of the eye, and sperm) are released by trauma; self molecules are chemically modified, undergo altered posttranslational modification (such as citrullination) or change conformation, creating new epitopes; or they are cross-recognized through molecular mimicry ([7.15.28](/7.15.28)).

### 8.4.3. Other Classifications

- By origin within the antigen-presenting cell: **endogenous antigens**, synthesized within the cell, are presented mainly on MHC class I molecules to CD8⁺ T cells, and **exogenous antigens**, taken up from outside, are presented mainly on MHC class II molecules to CD4⁺ T cells ([7.15.14](/7.15.14)).
- By relation to disease: transplantation antigens, **tumor-associated antigens** and **tumor-specific antigens** ([7.15.30](/7.15.30)), autoantigens, **allergens** that can cause hypersensitivity, and tolerogens that can induce tolerance.
- By physical form and source: particulate and soluble antigens, natural and synthetic antigens.

## 8.5. Nonspecific Immune Stimulators

An antigen activates only the few clones that carry the corresponding receptor. Other substances, without specific recognition or by bypassing recognition of epitopes, can activate large numbers of lymphocyte clones or amplify specific responses. They act in different ways but share independence from antigen specificity: superantigens and mitogens directly activate large numbers of clones, whereas adjuvants amplify the response to other antigens.

### 8.5.1. Superantigens and Mitogens

**Superantigens** are microbial products (such as the enterotoxins and toxic shock syndrome toxin-1 of *Staphylococcus aureus* and the pyrogenic exotoxins of *Streptococcus pyogenes*) that, without processing, bind as intact molecules to a region outside the peptide-binding groove of MHC class II molecules and to the framework of the V region of the TCR β chain, bridging the two cells. This binding depends neither on the peptide nor on the CDR3 of the TCR, so one superantigen can activate all T cells bearing a given Vβ family, about 2%–20% of peripheral T cells, whereas an ordinary peptide antigen activates only about $10^{-5}$–$10^{-4}$. The result is that large numbers of CD4⁺ T cells simultaneously release IFN-γ, TNF-α and IL-2, triggering a systemic inflammatory reaction such as toxic shock syndrome and the vomiting of food poisoning (the **cytokine storm** of [7.15.11](/7.15.11)); the T cells activated at the same time later undergo apoptosis or become anergic, causing immunosuppression.

**Mitogens** are substances that stimulate mitosis in lymphocytes, independently of antigen specificity. Concanavalin A (ConA) and phytohemagglutinin (PHA) activate T cells, lipopolysaccharide and pokeweed mitogen act on B cells, and anti-CD3 antibody directly cross-links the TCR complex. Mitogens mimic the antigen signal by cross-linking glycoproteins (or receptors) on the cell surface and act on the whole lymphocyte population rather than on a single clone; they are used to stimulate T cells when testing the proliferative capacity of lymphocytes and in karyotype analysis.

### 8.5.2. Adjuvants

**Definition 8.5.1 (Adjuvant)** An **adjuvant** is a substance given together with, or before, an antigen that enhances the strength of the organism's response to that antigen or changes its type.

An adjuvant has no immunogenicity of its own (or only a very weak one), and its mechanisms fall into four classes:

- Altering the physical state of the antigen to form an antigen depot: aluminum salts adsorb antigen and are retained at the injection site, releasing it slowly; oil emulsions act similarly. The prolonged residence of the antigen gives lymphocytes more opportunity to encounter it.
- Activating innate immunity: many adjuvants contain ligands of **pattern recognition receptors**, such as nontoxic derivatives of lipopolysaccharide (TLR4), CpG oligonucleotides (TLR9) and mycobacterial cell-wall components (TLR2, NOD2); aluminum salts and certain particles activate the **inflammasome** (NLRP3) and cause local tissue injury, releasing **damage-associated molecular patterns**.
- Promoting uptake, maturation and migration of antigen-presenting cells: once innate immunity is activated, dendritic cells upregulate MHC and costimulatory molecules (CD80, CD86) and secrete cytokines, which are the second and third signals needed for T-cell activation ([7.15.16](/7.15.16)).
- Recruiting and activating antigen-presenting cells and lymphocytes: local inflammation releases chemokines, so more monocytes and dendritic cells reach the injection site and enter the draining lymph node.

The principle of adjuvants answers a fundamental question: why is a purified protein often weakly immunogenic, whereas the same protein given together with a "danger signal" elicits a strong response? The initiation of adaptive immunity requires the second signal supplied by innate immunity, which a pure protein lacks. This is the link between the pattern recognition of [7.15.6](/7.15.6) and adaptive immunity, and it is also the focus of modern vaccine design: recombinant protein vaccines depend on adjuvants ([7.15.33](/7.15.33)), whereas inactivated or attenuated whole pathogens carry their own patterns. Adjuvants change not only the strength of the response but also its type: aluminum salts favor Th2 and antibody responses, and adjuvants containing TLR agonists favor Th1 responses, which is related to the cytokines secreted by the activated innate cells ([7.15.17](/7.15.17)).

| | Superantigen | Mitogen | Adjuvant |
|---|---|---|---|
| Target | T cells (Vβ families) | T cells or B cells | Antigen-presenting cells, innate cells |
| Antigen specificity required | No | No | No, but amplifies the specific response to the antigen |
| MHC restriction | None (binds conserved regions of MHC II) | None | None |
| Proportion of clones activated | About 2%–20% | Very high (polyclonal) | Does not directly activate lymphocytes |
| Result | Massive cytokines, immunopathology, then anergy | Polyclonal proliferation | Enhanced response, altered type |

## 8.6. A Model: Epitope Occupancy and Cross-Linking

Activation of a B cell requires BCRs to be cross-linked: signaling begins only when one antigen molecule binds two or more receptors and pulls them together. This section uses a simple model to answer the question: how many epitopes must an antigen have, and at what receptor concentration, to cross-link effectively? It prepares for the avidity of [7.15.9](/7.15.9).

Let the antigen have $n$ identical and mutually independent epitopes, each binding free receptor (concentration $c$, much greater than the antigen concentration and therefore not depleted) with dissociation constant $K_\mathrm{D}$. By the binding isotherm of [7.1.7](/7.1.7), the probability that each epitope is occupied is $\theta = c/(K_\mathrm{D} + c)$. For one antigen molecule to bridge two receptors, at least two epitopes must be occupied, with probability

$$
p(n, \theta) = 1 - (1 - \theta)^n - n\theta(1 - \theta)^{n-1}. \tag{8.1}
$$

For $n = 1$ (a hapten), $p = 0$: a monovalent antigen cannot cross-link at any concentration, which explains why haptens do not elicit a response (Definition 8.1.1).

**Example 8.6.1** Take $\theta = 0.1$, that is, a receptor concentration of $1/9$ of $K_\mathrm{D}$. For $n = 2$, $p = 0.01$; for $n = 10$, $p = 1 - 0.9^{10} - 10 \times 0.1 \times 0.9^{9} \approx 0.26$. That is, at the same receptor occupancy, the fraction of molecules that can cross-link is 26 times as great for a 10-valent antigen as for a bivalent one.

For larger $n$, $p \approx 1 - \mathrm{e}^{-n\theta}(1 + n\theta)$, which depends only on $n\theta$ (the mean number of occupied epitopes). Setting $p = 1/2$, the numerical solution is $n\theta \approx 1.7$, so the $c/K_\mathrm{D} \approx \theta \approx 1.7/n$ required for half-maximal cross-linking falls as valency rises: the higher the valency, the lower the concentration required.

![Epitope occupancy and cross-linking (Eq. (8.1)). A: For an antigen with $n$ identical epitopes, the fraction $p$ of molecules with at least two occupied epitopes (able to bridge two receptors) as a function of free receptor concentration (in units of $K_\mathrm{D}$): the larger $n$, the further left the curve shifts; for the hapten with $n = 1$ it is always 0. B: The $c/K_\mathrm{D}$ required to reach $p = 1/2$ versus $n$ (log–log scale); the dashed line is the asymptotic form $1.7/n$, and for $n = 2$, 10 and 30 the values are 2.4, 0.19 and 0.059](./plots/crosslinking.py)

The conclusion of the model agrees with the properties of TI-2 antigens: polysaccharides and polymeric proteins carry tens to hundreds of repetitively arrayed epitopes and can cross-link BCRs extensively at very low receptor occupancy, without T-cell help (§8.4.1); monomeric proteins have only a few epitopes, cross-link weakly, and rely on T cells to make up the difference. The model is only a first-order approximation: it assumes that epitopes are independent and suitably spaced and ignores receptor mobility and signaling thresholds; real BCR clustering also depends on epitope spacing (about $5$–$10\ \mathrm{nm}$ is most effective) and on receptor fluidity. The avidity treated later ([7.15.9](/7.15.9)) is the same idea on the antibody side: a bivalent antibody binds two epitopes at once, which greatly strengthens the effective binding.

## Summary

| Topic | Key points |
|---|---|
| Two properties (§8.1) | Immunogenicity is the ability to elicit a response and antigenicity the ability to bind its products (Definition 8.1.1); a hapten has only antigenicity and becomes immunogenic when attached to a carrier (Definition 8.1.2) |
| Epitopes (§8.2) | An epitope is the smallest unit of an antigen that is recognized; linear and conformational epitopes (Definition 8.2.1); T-cell versus B-cell epitopes (Definition 8.2.2); shared epitopes cause cross-reactivity (Definition 8.2.3) |
| Determinants of immunogenicity (§8.3) | Foreignness, molecular weight and chemical nature, structural complexity, physical state; host MHC and age; dose, route, frequency and adjuvant |
| Classification (§8.4) | TD and TI antigens (Definition 8.4.1): TD requires T-cell help and yields class switching, affinity maturation and memory; alloantigens and autoantigens (Definition 8.4.2) |
| Nonspecific stimulators (§8.5) | Superantigens and mitogens directly activate large numbers of clones; adjuvants (Definition 8.5.1) enhance the response through an antigen depot, activation of innate immunity and maturation of antigen-presenting cells |
| Model (§8.6) | The fraction of antigens bridging two receptors is given by Eq. (8.1); the concentration needed for cross-linking is roughly inversely proportional to the number of epitopes |

Two threads run through the whole course: B cells see the shape of the molecule, T cells see the peptide presented by MHC, and the two meet on the same antigen through linked recognition; and whether a response begins depends both on the antigen and on whether innate immunity simultaneously supplies signals.

## Questions

1. Why is no antibody produced against a hapten (such as dinitrophenyl) by itself, whereas antibody is produced when it is coupled to a carrier, and why can the antibody produced bind the free hapten?

   **Answer** A hapten has a small molecular weight and cannot be processed into a peptide that binds MHC, so even if a B cell binds the hapten, it receives no help from CD4⁺ T cells. After coupling to a carrier protein, the B cell binds the hapten through its BCR, internalizes the whole conjugate, and presents the carrier peptide on MHC class II molecules, where carrier-specific T cells provide help (linked recognition). The antibody response is directed against the hapten as a B-cell epitope, so the specificity of the antibodies produced is still for the hapten, and they can of course bind the free hapten.

2. After a protein is denatured by heating, a monoclonal antibody that bound it no longer does. Another antibody binds only the denatured protein. How can this be explained? What does it suggest for using antibodies in immunohistochemistry?

   **Answer** The first antibody recognizes a conformational epitope; denaturation separates residues that are far apart in sequence, and the epitope disappears. The second antibody recognizes a linear epitope, which in the native protein is buried or masked and is exposed after denaturation. Formaldehyde fixation and paraffin embedding alter protein conformation and also cross-link neighboring residues, so one should choose antibodies validated on fixed tissue (mostly antibodies that recognize linear epitopes) and use antigen retrieval; for the same target protein, different antibody clones can behave completely differently on fixed tissue.

3. Pure polysaccharide vaccines work poorly in infants, whereas attaching the polysaccharide to a protein carrier produces a durable IgG response. Explain the difference, and explain why this is the same principle as the hapten–carrier effect.

   **Answer** A polysaccharide is a TI-2 antigen: it activates marginal zone B cells by cross-linking BCRs, has no T-cell epitope, and cannot obtain T-cell help, so the response is mainly IgM, without affinity maturation or memory; in infants and young children the marginal zone is underdeveloped and the response is poorer still. When the polysaccharide is covalently attached to a protein carrier, polysaccharide-specific B cells internalize the conjugate through the BCR and present the carrier peptide to carrier-specific T cells, receive help, undergo class switching, and form germinal centers and memory. Here the polysaccharide plays the part of the hapten and the protein the part of the carrier; both are the same kind of linked recognition.

4. In the model of Eq. (8.1), what free receptor concentration is needed for an antigen with $n = 5$ epitopes to reach $p = 1/2$? How does the required concentration change if the $K_\mathrm{D}$ of the receptor increases 10-fold (lower affinity)?

   **Answer** Solving $p(5, \theta) = 1/2$ gives $\theta \approx 0.314$, that is, $c/K_\mathrm{D} = \theta/(1 - \theta) \approx 0.46$, so the required $c \approx 0.46K_\mathrm{D}$. The concentration is proportional to $K_\mathrm{D}$, so a 10-fold increase in $K_\mathrm{D}$ increases the required concentration 10-fold. An increase in valency can compensate for a loss of affinity: raising $n$ from 5 to 30 lowers the required $c/K_\mathrm{D}$ from 0.46 to 0.059.

   *Hint: find the root of Eq. (8.1) numerically, for example with `scipy.optimize.brentq`.*
5. (Open question) In vaccine development it is often found that immunization with a purified recombinant protein alone is far less effective than with an inactivated whole pathogen. Using the concepts of this chapter, design approaches to close this gap.

   **Answer** Ideas: a recombinant protein lacks the second signal of innate immunity, so one can add an adjuvant containing pattern recognition receptor ligands (TLR agonists, aluminum salts, etc.); through slow release, particle formation or multivalent display (such as repetitive antigens arrayed on virus-like particles or nanoparticles), one increases both uptake and BCR cross-linking (larger $n$ in Eq. (8.1)); one can link the antigen to a helper T-cell epitope or carrier protein that can be presented by the MHC of most individuals, ensuring T-cell help; and one can select immunodominant epitopes and preserve their native conformation, to induce neutralizing antibodies against conformational epitopes.
