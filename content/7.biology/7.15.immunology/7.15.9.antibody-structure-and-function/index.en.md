---
title: Antibody Structure and Function
description: How antibodies recognize and act. The heavy chain, light chain, variable and constant regions, CDRs, Fab, Fc and hinge region of immunoglobulins; isotype, allotype and idiotype; the properties of the five classes; the functions of the V and C regions; quantitation of antigen–antibody binding (affinity, avidity, Scatchard plot, immune complexes and the zone of equivalence); and the principles of polyclonal, monoclonal and engineered antibodies and therapeutic antibodies.
source_hash: 7e6c08dfd3d0
---

[7.15.8](/7.15.8) answered what adaptive immunity recognizes; this chapter answers what the B cell uses to recognize it and what it uses to eliminate it afterward. An antibody is one molecule in two forms: the membrane form is the antigen receptor of the B cell, and the secreted form is the effector molecule of humoral immunity. Its structure separates the two tasks: the N-terminal variable region is responsible for specific recognition, and the C-terminal constant region determines which effector function is used for elimination. Understanding this division of labor is understanding the whole biology of antibodies.

The general rules of protein–ligand binding and the basic structure of IgG were given in [7.1.7](/7.1.7) and are not repeated here; this chapter develops the immunological content: the functions of each of the five classes, the quantitation of antigen–antibody binding (affinity and avidity are the two limits of one model), and how engineered antibodies turn these principles into tools and drugs. Where antibody diversity comes from is the subject of [7.15.12](/7.15.12); how B cells produce antibodies is in [7.15.19](/7.15.19) and [7.15.20](/7.15.20); the details of antibody effector functions are in [7.15.21](/7.15.21), and complement in [7.15.10](/7.15.10).

## 9.1. Basic Structure of Immunoglobulins

### 9.1.1. Four Polypeptide Chains and the Ig Domain

All **antibodies** (immunoglobulins) consist of four polypeptide chains, two long and two short, joined by interchain disulfide bonds and noncovalent interactions into a symmetric Y-shaped molecule.

**Definition 9.1.1 (Heavy Chain, Light Chain, Variable Region and Constant Region)** The two identical, larger chains of an antibody molecule (about $50$–$75\ \mathrm{kDa}$) are called the **heavy chains**, and the two identical, smaller chains (about $25\ \mathrm{kDa}$) are called the **light chains**. The roughly 110 amino acids of each chain nearest the N terminus, whose sequence differs greatly from one antibody to another, are called the **variable region** (V region, $\mathrm{V_H}$ and $\mathrm{V_L}$); the rest, whose sequence is essentially the same within a class, is called the **constant region** (C region: $\mathrm{C_H}$ in the heavy chain and $\mathrm{C_L}$ in the light chain).

There are two kinds of light chain, κ and λ, and the two light chains of one antibody molecule are always of the same type. In human antibodies about 60% of light chains are κ and about 40% are λ; in the mouse about 95% are κ. There are five kinds of heavy chain (γ, μ, α, δ, ε), which determine the class of the antibody (§9.2).

Each chain is built from a series of immunoglobulin domains (Ig folds) of about 110 residues each: each domain is a "sandwich" of two antiparallel β sheets stabilized by one intrachain disulfide bond. The light chain has two domains ($\mathrm{V_L}$, $\mathrm{C_L}$); the heavy chain has four ($\mathrm{V_H}$, $\mathrm{C_H1}$, $\mathrm{C_H2}$, $\mathrm{C_H3}$), and the heavy chains of IgM and IgE have one more ($\mathrm{C_H4}$). $\mathrm{V_H}$ and $\mathrm{V_L}$ pair to form the antigen-binding site, $\mathrm{C_H1}$ pairs with $\mathrm{C_L}$, and the $\mathrm{C_H3}$ domains of the two heavy chains pair with each other. The Ig fold is the hallmark of a large protein superfamily: the TCR, MHC, CD4, CD8 and many adhesion molecules all contain this kind of domain ([7.15.4](/7.15.4)).

### 9.1.2. The Variable Region and the Complementarity-Determining Regions

When the V-region sequences of many antibodies are aligned, the variability is not evenly distributed but is concentrated in three very short segments, called the **complementarity-determining regions** (CDRs, also called hypervariable regions), which lie between four relatively conserved framework regions.

**Definition 9.1.2 (Complementarity-Determining Region)** The three highly variable loops of the variable region of an antibody or TCR that directly contact antigen (CDR1, CDR2, CDR3) are called the **complementarity-determining regions**; the relatively conserved segments between them, which form the β-sheet scaffold, are called framework regions.

$\mathrm{V_H}$ and $\mathrm{V_L}$ each have three CDRs, so one binding site of an antibody molecule is assembled from six loops. In the folded structure they cluster at the top of the $\mathrm{V_H}$/$\mathrm{V_L}$ interface and form a binding surface of about $6$–$9\ \mathrm{nm^2}$ complementary to the epitope ([7.15.8](/7.15.8), [7.1.7](/7.1.7)). Of the six loops, the heavy-chain CDR3 is the longest and most variable; it is encoded at the junction of the V, D and J gene segments, lies at the center of the binding surface, and contributes most to specificity ([7.15.12](/7.15.12)). The shape of the binding surface varies with the antigen: a deep pocket for a hapten, a groove for a polysaccharide, and a larger, flatter interface for a protein; binding of an epitope to the CDRs is often accompanied by local conformational adjustments on both sides (induced fit).

### 9.1.3. Fab, Fc and the Hinge Region

Long before the amino acid sequences of antibodies were determined, proteolysis had already revealed their domain organization: papain cuts IgG in the hinge region into three pieces, two identical antigen-binding fragments and one crystallizable fragment; pepsin cuts below the disulfide bonds of the hinge region, giving an $\mathrm{F(ab')_2}$ fragment that remains bivalent and some small fragments.

**Definition 9.1.3 (Fab and Fc Fragments and the Hinge Region)** The N-terminal portion of an antibody, comprising one complete light chain and the $\mathrm{V_H}$ and $\mathrm{C_H1}$ of the heavy chain, is called the **Fab fragment** (fragment antigen binding); it contains one antigen-binding site. The C-terminal portion of the two heavy chains, comprising $\mathrm{C_H2}$ and $\mathrm{C_H3}$ (and $\mathrm{C_H4}$ in IgM and IgE), is called the **Fc fragment** (fragment crystallizable); it does not bind antigen but determines the effector functions of the antibody. The flexible, proline- and cysteine-rich sequence between $\mathrm{C_H1}$ and $\mathrm{C_H2}$ is called the **hinge region**.

The hinge region has two functions: the disulfide bonds between the two heavy chains lock them into a symmetric dimer; and its flexibility lets the two Fab arms open or close through a wide range of angles, so that a bivalent antibody can bind two epitopes at different spacings simultaneously (§9.5.2). IgG, IgA and IgD have a hinge region; IgM and IgE do not, and instead have an extra $\mathrm{C_H}$ domain, their flexibility coming from flexibility between domains. The hinge of IgG3 is especially long, up to 62 residues, which makes it the most accessible to antigen but also the most easily cut by proteases, so its half-life is shorter.

![The structure of antibodies. A: IgG drawn domain by domain: two heavy chains (yellow; $\mathrm{V_H}$, $\mathrm{C_H1}$, hinge, $\mathrm{C_H2}$, $\mathrm{C_H3}$) and two light chains (purple; $\mathrm{V_L}$, $\mathrm{C_L}$); the red arcs at the tips of the variable regions mark the complementarity-determining regions; each of the two Fab arms contains one antigen-binding site, the Fc consists of the $\mathrm{C_H2}$ and $\mathrm{C_H3}$ domains of the two heavy chains, and the interchain disulfide bonds of the hinge region lock the two heavy chains together. B: Schematic of the five classes (heavy-chain color indicates class, light chains gray): IgG, IgD and IgE are monomers; secretory IgA is a dimer joined by the J chain (small yellow circle) and wrapped by the secretory component (dashed ellipse); IgM is a pentamer joined by the J chain and has 10 antigen-binding sites](./plots/structure.py)

## 9.2. Serotypes of Immunoglobulins

Antibody molecules can themselves be recognized by antibodies: when the immunoglobulins of one animal are used to immunize another, the antibodies obtained distinguish different antigenic differences, which fall into three classes according to their distribution in the population, called serotypes.

**Definition 9.2.1 (Isotype)** The antigenic differences shared by the antibodies of all individuals of a species and encoded by different constant-region genes are called **isotypes**; they include the class of the heavy chain (γ, μ, α, δ, ε), its subclass (human IgG1–4, IgA1–2) and the type of the light chain (κ, λ).

Isotype is a difference at the species level: one person has antibodies of all isotypes at the same time, and anti-human IgG antibody obtained by immunizing a rabbit with human IgG recognizes the IgG of all humans. Isotype determines the class of an antibody and also its effector functions; a B cell can change the isotype of the antibody it produces while keeping the V region unchanged, and this is **class switch recombination** ([7.15.12](/7.15.12)).

**Definition 9.2.2 (Allotype)** The antigenic differences between individuals of a species that arise from allelic polymorphism of constant-region genes are called **allotypes**.

Allotype is a difference at the level of the individual, generally caused by a difference of one or two amino acids in the constant region, as in the Gm system of the human IgG heavy chain, the Km system of the κ chain and the Am system of IgA2. The genes encoding them are tightly linked and inherited as haplotypes; they were once used in paternity testing and in studies of population genetics. Medically, infusion of immunoglobulin that contains an allotype the recipient lacks can occasionally elicit anti-allotype antibodies.

**Definition 9.2.3 (Idiotype)** The unique antigenicity of the variable region of an antibody (or TCR or BCR) conferred by the sequences of the CDRs and framework regions is called the **idiotype**; each antigenic determinant on an idiotype is called an idiotope.

The antibodies of each B-cell clone have an idiotype of their own. Antibodies directed against an idiotype (anti-idiotypic antibodies) can recognize one clone; some of them have a binding site whose shape resembles the original antigen and are called the "internal image." On this basis Jerne proposed the immune network theory: antibodies and anti-idiotypic antibodies form a mutually regulating network. Experiments have not supported this theory as the main regulatory mechanism of the immune response, but the concept of the idiotype remains useful: it is a marker of a tumor B-cell clone and is also one source of the immunogenicity of antibody drugs.

| | Isotype | Allotype | Idiotype |
|---|---|---|---|
| Location | Constant region (C) | Individual positions in the constant region (C) | Variable region (V) and CDRs |
| Distribution | Shared by all individuals of the species | Differs between individuals | Differs between clones |
| Determined by | Different C genes | Alleles of C genes | V(D)J rearrangement and somatic mutation |
| Examples | μ, γ, α, δ, ε; κ, λ | Gm, Km, Am | Epitopes recognized by anti-idiotypic antibodies |

## 9.3. The Five Classes of Antibodies

### 9.3.1. Classes and Summary Table

**Definition 9.3.1 (The Five Classes of Antibodies)** By the type of the heavy-chain constant region, human antibodies fall into five classes: **IgG**, containing γ chains; **IgM**, containing μ chains; **IgA**, containing α chains; **IgD**, containing δ chains; and **IgE**, containing ε chains.

| | IgG | IgM | IgA | IgD | IgE |
|---|---|---|---|---|---|
| Heavy chain | γ (γ1–γ4) | μ | α (α1, α2) | δ | ε |
| Structure | Monomer | Pentamer (J chain); membrane form is a monomer | Mostly monomer in serum; secretory form is a dimer (J chain + secretory component) | Monomer | Monomer |
| Relative molecular mass | 150 kDa | 970 kDa | 160 kDa (monomer); secretory form about 400 kDa | 180 kDa | 190 kDa |
| Serum concentration / mg·mL⁻¹ | 7–16 (about 75%) | 0.4–2.3 | 0.7–4 | about 0.03 | about $10^{-4}$ |
| Serum half-life | About 21 d (IgG3 about 7 d) | About 5 d | About 6 d | About 3 d | About 2 d (weeks when bound to mast cells) |
| Complement activation (classical pathway) | IgG3 > IgG1 > IgG2; IgG4 barely | Strongest | No | No | No |
| Fc receptor binding | Phagocytes, NK cells (FcγR) | Yes (FcμR), weak | Phagocytes and neutrophils (FcαR) | — | Mast cells, basophils, eosinophils (FcεRI) |
| Crosses placenta | Yes (FcRn) | No | No | No | No |
| Main functions | Main antibody of serum and tissues: neutralization, opsonization, complement activation, ADCC, passive immunity of the newborn | Earliest in a primary response; intravascular; complement activation | Defense of mucosal surfaces; maternal antibody in milk | BCR on the surface of mature B cells | Antiparasitic; allergic reactions |

### 9.3.2. Characteristics of Each Class

IgG is the most abundant antibody in serum and tissue fluid and is the main antibody of the secondary response. It diffuses freely into tissues and is therefore the mainstay of defense against infection within tissues. It is the only antibody that crosses the placenta, being actively transported by transcytosis by the **neonatal Fc receptor** on placental syncytiotrophoblast cells, so that the newborn has its mother's protection for several months after birth. The half-life of IgG (about 3 weeks) is much longer than that of the other classes and is likewise determined by FcRn: after IgG is taken up by pinocytosis in endothelial cells and phagocytes, it binds FcRn in the acidic endosome, escapes lysosomal degradation, and is returned to the cell surface and released ([7.15.21](/7.15.21)). The Fc regions of the four subclasses differ in their affinities for complement and Fc receptors, so their effector functions differ in emphasis: IgG1 and IgG3 are strong in activating complement and binding FcγR, IgG2 is directed preferentially against polysaccharide antigens, and the effector functions of IgG4 are very weak.

IgM is the earliest antibody to appear in a response and also the oldest antibody class phylogenetically. Secretory IgM is a pentamer of five Y-shaped monomers joined by one J chain, with 10 antigen-binding sites. The affinity of a single binding site is often low (affinity maturation has not yet occurred at this stage of the response), but the avidity of ten valencies makes up for it (§9.5.2), so IgM is especially suited to binding multivalent repetitive antigens such as bacterial polysaccharides and the blood-group antigens on erythrocytes. IgM is the strongest of the five classes in activating the classical pathway: a pentamer bound to an antigen surface can offer several Fc regions close enough together to bind C1q ([7.15.10](/7.15.10)). Because the molecule is large, it is largely confined to the blood vessels. Membrane IgM is a monomer and, together with IgD, forms the **B-cell receptor** of the mature naive B cell.

**Definition 9.3.2 (J Chain and Secretory IgA)** The **J chain** is a short polypeptide synthesized by plasma cells that joins IgM monomers into a pentamer and IgA monomers into a dimer. **Secretory IgA** (sIgA) is the dimeric IgA of mucosal surfaces: the J-chain-linked dimer first binds the polymeric immunoglobulin receptor on the basolateral side of epithelial cells and is transported by transcytosis to the luminal surface, where the extracellular part of the receptor is cleaved off and remains on the IgA as the secretory component.

IgA is the most abundantly produced antibody (about $3$–$5\ \mathrm{g}$ per day in humans), and the great majority of it is present in secretory form in the mucosae of the intestinal, respiratory and urogenital tracts and in milk, saliva and tears. The secretory component protects IgA from degradation by digestive enzymes. sIgA acts by neutralization and "immune exclusion": it binds pathogens and toxins, preventing them from adhering to the epithelium and causing them to be expelled with the mucus, without causing inflammation ([7.15.23](/7.15.23)). IgA does not activate the classical pathway and rarely causes inflammation, which suits the environment in which it works, with its large numbers of commensal microbes and food antigens.

IgD is present at very low concentrations in serum; its main function is as the surface receptor of mature B cells, co-expressed with IgM. It is related to B-cell maturation and to the threshold of response to antigen, but the role of secreted IgD is still unclear.

IgE has the lowest serum concentration but a very high affinity: the Fc of IgE binds the high-affinity receptor FcεRI on the surface of mast cells and basophils with $K_\mathrm{D}$ of about $10^{-10}\ \mathrm{M}$, so IgE on the cell surface persists for weeks. Antigen cross-links the IgE on the cell surface and causes degranulation ([7.15.26](/7.15.26)). The normal function of this mechanism is defense against helminth parasites and against insect venoms and toxins; in an environment without parasites it mainly causes allergy.

## 9.4. Functions of the V Region and the C Region

The two parts of an antibody each have their own task:

- The V region recognizes and specifically binds antigen. This alone suffices for neutralization: antibody binds a toxin and prevents it from binding its cell receptor; binds an adhesion molecule on the surface of a virus or bacterium and prevents infection or colonization; or binds the active site of an enzyme and inhibits its activity. Neutralization does not need the Fc and can be carried out by the Fab fragment alone, which is why Fab and scFv can be used as drugs.
- The C region, specifically the Fc, determines what happens after binding:

| Effect | Antibody and site on Fc | Result |
|---|---|---|
| Complement activation | IgM, IgG ($\mathrm{C_H2}$ or $\mathrm{C_H3}$ binds C1q) | Lysis, opsonization and inflammation ([7.15.10](/7.15.10)) |
| Opsonization | The Fc of IgG binds the **Fc receptor** (FcγR) of phagocytes; acts together with C3b | Enhanced phagocytosis and killing ([7.15.7](/7.15.7)) |
| ADCC | The Fc of IgG binds FcγRIII (CD16) of NK cells | NK cells kill antibody-coated target cells ([7.15.21](/7.15.21)) |
| Mast-cell degranulation | The Fc of IgE binds FcεRI | Immediate hypersensitivity, antiparasitic defense ([7.15.26](/7.15.26)) |
| Transepithelial transport | IgA and IgM via the polymeric immunoglobulin receptor; IgG via FcRn | Mucosal secretion; transfer of maternal antibody |
| Half-life | Recycling of IgG via FcRn | Serum persistence of weeks |

This separation of V and C regions is why antibodies can meet the demand for "unlimited specificity" together with "limited effector functions": there are only a few effector functions, but they can be called up through any specificity. **Class switch recombination** ([7.15.12](/7.15.12)) replaces only the C region and keeps the V region, so that the same specificity can be carried out in turn by IgM, IgG, IgA or IgE, the choice being determined by the cytokines secreted by T cells ([7.15.20](/7.15.20)).

## 9.5. Quantitation of Antigen–Antibody Binding

### 9.5.1. Affinity of a Single Binding Site

Binding of an antibody to an antigen, like the binding of any protein to a ligand, is maintained by noncovalent interactions (hydrogen bonds, electrostatic interactions, van der Waals forces and hydrophobic interactions), is reversible, and obeys the law of mass action ([7.1.7](/7.1.7)).

**Definition 9.5.1 (Affinity)** The strength of binding between **one** antigen-binding site of an antibody and **one** epitope is called its **affinity**, measured by the dissociation constant $K_\mathrm{D}$: the smaller $K_\mathrm{D}$, the higher the affinity.

Let the free antibody concentration be $c$ (the amount of antigen is much smaller than that of antibody, so the free concentration is essentially constant); the fraction of epitopes occupied is

$$
\theta = \frac{c}{K_\mathrm{D} + c}, \tag{9.1}
$$

and exactly half the epitopes are occupied when $c = K_\mathrm{D}$. Kinetically, $K_\mathrm{D} = k_\mathrm{off}/k_\mathrm{on}$. The $k_\mathrm{on}$ of antigen–antibody binding usually lies between $10^{5}$ and $10^{6}\ \mathrm{M^{-1}\,s^{-1}}$ and does not vary much, so differences in affinity come mainly from $k_\mathrm{off}$: high-affinity complexes dissociate slowly (the half-life $\ln 2/k_\mathrm{off}$ can reach hours to days). The $K_\mathrm{D}$ of antibodies produced in a primary response is about $10^{-6}$–$10^{-7}\ \mathrm{M}$; after the **affinity maturation** produced by **somatic hypermutation** and selection, it can reach $10^{-9}$–$10^{-11}\ \mathrm{M}$ ([7.15.20](/7.15.20)).

Experimentally, Scatchard plots are often used to determine the number of binding sites and the affinity. Suppose an antibody molecule has $n$ identical and independent binding sites and binds on average $r$ antigens per antibody; then $r = nc/(K_\mathrm{D} + c)$, which can be rewritten as

$$
\frac{r}{c} = \frac{n - r}{K_\mathrm{D}}. \tag{9.2}
$$

A plot of $r/c$ against $r$ should give a straight line with slope $-1/K_\mathrm{D}$ and an intercept on the horizontal axis of $n$. A polyclonal antibody is a mixture of antibodies of many different affinities, and its Scatchard plot is concave upward (panel B): high-affinity antibodies dominate at low $r$, and low-affinity antibodies show themselves only at high $r$.

### 9.5.2. Avidity of a Bivalent Antibody

Natural antibodies are almost always multivalent (IgG has 2 binding sites, IgM has 10), and the antigens on the surfaces of bacteria and cells are also often arranged in multiple copies. The overall strength of binding when a multivalent antibody binds several epitopes simultaneously is much greater than that of a single binding site.

**Definition 9.5.2 (Avidity)** The total strength of binding between a multivalent antibody and a multivalent antigen is called its **avidity**; it depends both on the affinity of each binding site and on the valency and geometric fit.

Affinity and avidity are easily confused and must be distinguished carefully: the former is one site for one epitope, the latter the whole molecule for the whole antigen. A simple model shows how avidity arises. Suppose one arm of a bivalent antibody has already bound an epitope on the antigen surface; the other arm is then tethered near the surface, and its chance of meeting a second epitope is equivalent to a very high "effective concentration" $c_\mathrm{eff}$ around that arm, whose magnitude depends on the density and spacing of epitopes and the length of the hinge and is generally on the order of millimolar. The binding equilibrium of the second arm is $[\text{both arms}]/[\text{one arm}] = c_\mathrm{eff}/K_\mathrm{D}$, so the ratio of total bound to free is increased by a factor of $1 + c_\mathrm{eff}/K_\mathrm{D}$, and the apparent dissociation constant is

$$
K_\mathrm{D}^\text{app} = \frac{K_\mathrm{D}}{1 + c_\mathrm{eff}/K_\mathrm{D}} \approx \frac{K_\mathrm{D}^2}{c_\mathrm{eff}} \qquad (c_\mathrm{eff} \gg K_\mathrm{D}). \tag{9.3}
$$

**Example 9.5.1** Take $K_\mathrm{D} = 10^{-7}\ \mathrm{M}$ and $c_\mathrm{eff} = 10^{-3}\ \mathrm{M}$. The enhancement factor is $1 + 10^{4}$ and $K_\mathrm{D}^\text{app} \approx 10^{-11}\ \mathrm{M}$: the avidity is four orders of magnitude higher than the affinity of a single site. If the affinity of the site is 100 times lower ($K_\mathrm{D} = 10^{-5}\ \mathrm{M}$), then $K_\mathrm{D}^\text{app} = 10^{-5}/101 \approx 10^{-7}\ \mathrm{M}$, equal to a high-affinity monovalent site.

Two conclusions follow. (1) $K_\mathrm{D}^\text{app}$ is proportional to $K_\mathrm{D}^2$, so avidity "squares" the effect of affinity: two antibodies whose affinities differ 10-fold differ 100-fold apparently after bivalent binding. (2) Valency can compensate for affinity: in a primary response, low-affinity IgM binds repetitive antigens effectively through the avidity of ten valencies. The latter also explains a common observation: a Fab fragment (monovalent) is much weaker than whole IgG (bivalent) at binding cell-surface antigens, whereas the two are similar in binding monovalent antigen in solution. Avidity also lets antibodies discriminate the density of epitopes: only a surface with epitopes dense enough and suitably spaced can be "pulled taut" by a bivalent antibody.

![Quantitation of antigen–antibody binding. A: The monovalent binding isotherm (Eq. (9.1), dashed, $K_\mathrm{D} = 10^{-7}\ \mathrm{M}$) and the apparent isotherm of a bivalent antibody (Eq. (9.3), $c_\mathrm{eff} = 1\ \mathrm{mM}$): bivalent binding of the same site shifts the curve left by four orders of magnitude (red); a site with $K_\mathrm{D}$ 100 times larger coincides after bivalent binding with a high-affinity monovalent site (blue). B: Scatchard plot (Eq. (9.2)) of an antibody with $n = 2$ sites: a single affinity gives a straight line with slope $-K$; a mixture of two affinities ($5\times10^9$ and $10^8\ \mathrm{M^{-1}}$ in equal amounts) gives a curve concave upward. C: Precipitation curve (Eq. (9.4)) of a bivalent antibody with an $n$-valent antigen: when the network index $(n-1)p_\mathrm{A}p_\mathrm{B}$ exceeds 1, a large cross-linked network forms, which occurs only within the zone of equivalence where the numbers of binding sites of antibody and antigen are similar; for $n \le 2$ it never exceeds 1](./plots/binding.py)

### 9.5.3. Immune Complexes and the Zone of Equivalence

**Definition 9.5.3 (Immune Complex)** The complex formed by binding of antigen and antibody is called an **immune complex**.

When antibody and antigen are both multivalent, immune complexes can grow into large cross-linked networks. As early as the 1930s, Heidelberger and Kendall found that, with the amount of antibody fixed and the amount of antigen gradually increased, the precipitate first increases and then decreases; the maximum is called the zone of equivalence, flanked by the zone of antibody excess and the zone of antigen excess. A model helps to understand this precipitation curve. Suppose a bivalent antibody binds an $n$-valent antigen very tightly, and let $\rho$ be the ratio of numbers of binding sites (antibody sites / antigen epitopes). With antigen excess ($\rho < 1$), all antibody sites are occupied, so the fraction of epitopes occupied is $p_\mathrm{B} = \rho$ and $p_\mathrm{A} = 1$; with antibody excess ($\rho > 1$) the reverse holds, $p_\mathrm{A} = 1/\rho$ and $p_\mathrm{B} = 1$. According to the Flory–Stockmayer theory of polymer gels, when

$$
(n-1)\,p_\mathrm{A}\,p_\mathrm{B} > 1 \tag{9.4}
$$

the network can extend without limit and a precipitate forms. It follows that with antigen excess $\rho > 1/(n-1)$ is required, with antibody excess $\rho < n-1$ is required, and the maximum is at $\rho = 1$. The precipitation region is therefore a stretch centered on $\rho = 1$ that is wider the larger $n$ is; an antigen with $n \le 2$ (such as a hapten, or a molecule with only two epitopes) cannot be precipitated into a network by a bivalent antibody at any ratio and can form only short chains. Real curves are smoother than this model, because intramolecular ring formation, conformational restrictions and finite affinity all impair the network, but the qualitative features, the zone of equivalence and the flanking zones on either side, are robust.

The zone of equivalence has important biological and medical significance:

- Large complexes in the zone of antibody excess and the zone of equivalence are readily cleared by complement and phagocytes; complexes in the zone of antigen excess are small and soluble, are not readily cleared, remain in the circulation for a long time, and deposit in vessel walls and the glomerular basement membrane, causing serum sickness, immune-complex nephritis and tissue damage in some autoimmune diseases ([7.15.27](/7.15.27)).
- In immunological assays, a great excess of antigen weakens the precipitation or agglutination reaction instead, known as the postzone (hook) effect, which can cause false negatives ([7.15.34](/7.15.34)).

## 9.6. Engineered Antibodies and Therapeutic Antibodies

### 9.6.1. Polyclonal and Monoclonal Antibodies

When an animal is immunized with an antigen, the antibodies in its serum are a mixture produced by many B-cell clones, recognizing different epitopes of the same antigen; these are **polyclonal antibodies**. They bind native antigen strongly but vary from batch to batch and are difficult to reproduce in quantity. Köhler and Milstein (1975; Nobel Prize 1984) solved this problem: fusing B cells from an immunized animal with myeloma cells gives **hybridomas**, which both produce antibody and proliferate indefinitely in vitro ([7.3.3](/7.3.3)); selecting a single clone that produces the desired antibody gives a **monoclonal antibody** that recognizes only one epitope ([7.1.7](/7.1.7)). The principle of selection is a metabolic defect: the myeloma cells lack an enzyme of the salvage pathway, and in a medium that blocks the de novo pathway only cells fused with B cells survive, while unfused B cells cannot proliferate for long on their own.

Monoclonal antibodies have a single specificity, are homogeneous and can be supplied without limit, and have become basic tools of immunological assays, immunohistochemistry and flow cytometry ([7.15.34](/7.15.34)). As drugs they have a problem: a mouse antibody is a foreign protein to humans and elicits an anti-mouse antibody response, which both neutralizes the drug and readily causes allergic reactions, and in addition the mouse Fc cannot activate effector functions effectively in humans and has a short half-life.

### 9.6.2. Engineered Antibodies

The way to overcome this problem is to "humanize" the antibody step by step with recombinant DNA technology. The modular structure of antibodies (V region separate from C region, CDRs separate from framework regions) is what allows them to be remodeled in this way.

**Definition 9.6.1 (Chimeric and Humanized Antibodies)** An antibody obtained by joining the V region of a mouse antibody to the C region of a human antibody is called a **chimeric antibody**; an antibody obtained by going further and grafting the CDRs of a mouse antibody into the framework regions of a human antibody, retaining only the portion of the mouse sequence that directly contacts antigen, is called a **humanized antibody**.

The mouse sequence accounts for only 5%–10% of a humanized antibody, and its immunogenicity is greatly reduced. Going further, fully human antibodies can be obtained by immunizing transgenic mice carrying human immunoglobulin genes, or by screening human antibody gene libraries for binding ability with in vitro methods such as phage display. The suffix of a therapeutic antibody's name reflects its origin: -omab for mouse, -ximab for chimeric, -zumab for humanized and -umab for fully human.

**Definition 9.6.2 (Bispecific Antibody)** An engineered antibody whose two binding sites recognize different antigens (or different epitopes on the same antigen) is called a **bispecific antibody**.

The two arms of a natural antibody are identical; a bispecific antibody is engineered so that the two arms differ. One use is to bridge two cells: one arm binds a surface antigen of a tumor cell and the other binds CD3 on a T cell, bringing the T cell close to the tumor cell and causing it to kill, without the TCR of that T cell having to recognize a tumor antigen ([7.15.30](/7.15.30)). Another use is to mimic on a single molecule the joint action of two proteins (for example, an antibody that binds coagulation factors FIXa and FX at the same time, replacing the bridging function of the missing FVIIIa in hemophilia A).

**Definition 9.6.3 (Nanobody)** In camelids (and sharks) heavy-chain-only antibodies occur naturally, and their single variable domain (VHH) can bind antigen independently; the fragment of about $15\ \mathrm{kDa}$ obtained by expressing it alone is called a **nanobody** (single-domain antibody).

Nanobodies are small and stable, can bind recesses that the CDRs of IgG have difficulty entering (such as the active site of an enzyme), and are easily fused to other domains. There are also single-chain antibody fragments (scFv, in which $\mathrm{V_H}$ and $\mathrm{V_L}$ are joined by a flexible peptide), Fab, $\mathrm{F(ab')_2}$ and other fragments, used as drugs, imaging probes, or the recognition modules of chimeric antigen receptors ([7.15.30](/7.15.30)).

| Type | Composition | Features and uses |
|---|---|---|
| Polyclonal antibody | Mixture of many clones | Binds native antigen well; batch-to-batch variation; mostly used for detection and passive immunization |
| Monoclonal antibody (mouse) | A single clone of a hybridoma | Homogeneous specificity; immunogenic in humans |
| Chimeric antibody | Mouse V + human C | Retains Fc effector functions; lower immunogenicity |
| Humanized antibody | Mouse CDRs + human framework and C | Still lower immunogenicity |
| Fully human antibody | Transgenic mice or in vitro display | Lowest immunogenicity |
| Bispecific antibody | Two different binding sites | Bridges two cells or two molecules |
| Nanobody, scFv, Fab | One or a few domains | Small, good penetration; short half-life, no Fc effector function |

### 9.6.3. Mechanisms of Therapeutic Antibodies

The mechanisms of antibody drugs can be summarized by the division of labor of §9.4:

- Binding alone (V region): neutralizing a cytokine or its receptor (anti-TNF, anti-IL-6 receptor, anti-IgE), or blocking a receptor–ligand interaction, as in blockade of **immune checkpoints** (anti-PD-1, anti-CTLA-4, [7.15.25](/7.15.25)) and of growth-factor signaling (anti-VEGF, anti-HER2).
- Elimination of target cells (Fc): binding an antigen on the surface of tumor cells or B cells (such as CD20 or HER2) and eliminating the cells through ADCC, complement-dependent cytotoxicity and antibody-dependent phagocytic killing ([7.15.21](/7.15.21)); the glycosylation of Fc can be engineered to strengthen its binding to FcγRIII.
- As a carrier: antibodies conjugated to cytotoxic drugs deliver the drug to cells expressing the target antigen, or are conjugated to radionuclides.
- Bridging immune cells: bispecific antibodies (see above).
- Passive immunization: directly administering antibody against a pathogen or toxin gives immediate protection without depending on a response made by the recipient ([7.11.28](/7.11.28)); examples are antivenom, anti-tetanus immunoglobulin and the monoclonal antibody against respiratory syncytial virus.
- Extending half-life: engineering the binding of Fc to FcRn prolongs the half-life of the antibody.

## Summary

| Topic | Key points |
|---|---|
| Structure (§9.1) | Two heavy chains and two light chains, built of Ig domains; the V region contains 3 CDRs, and $\mathrm{V_H}$ and $\mathrm{V_L}$ together form the antigen-binding site (Definitions 9.1.1, 9.1.2); Fab binds antigen, Fc determines effector function, and the hinge region makes the two arms flexible (Definition 9.1.3) |
| Serotypes (§9.2) | Isotype (shared within the species, Definition 9.2.1), allotype (individual differences, Definition 9.2.2), idiotype (clone-specific, Definition 9.2.3) |
| Five classes (§9.3) | IgG (main one, crosses the placenta, long half-life), IgM (earliest, pentamer, strongest complement activation), IgA (secretory, mucosal), IgD (BCR), IgE (mast cells, allergy and antiparasitic defense) (Definitions 9.3.1, 9.3.2) |
| Division of function (§9.4) | The V region recognizes and neutralizes; the C region calls up complement, Fc receptors and transepithelial transport |
| Quantitation (§9.5) | Affinity: a single site, $K_\mathrm{D}$ (Eq. (9.1)); avidity: multivalent, bivalent binding gives $K_\mathrm{D}^\text{app} \approx K_\mathrm{D}^2/c_\mathrm{eff}$ (Eq. (9.3)); immune-complex size is determined by the antibody-to-antigen ratio, with precipitation when $(n-1)p_\mathrm{A}p_\mathrm{B}>1$ (Eq. (9.4)) |
| Engineered antibodies (§9.6) | Polyclonal, monoclonal (hybridoma), chimeric, humanized, fully human, bispecific and nanobodies; therapeutic mechanisms: neutralization, elimination, drug delivery, bridging |

## Questions

1. Why can the antibody of one B-cell clone change from IgM to IgG or IgA while the V region stays unchanged? What is the advantage for the antibody response?

   **Answer** The structure of the antibody separates the V region from the C region, which are encoded by different gene segments; class switch recombination joins the rearranged V(D)J exon to a different C gene at the DNA level ([7.15.12](/7.15.12)), so the antigen-binding site is unchanged and the effector function is changed. The advantage is that the same specificity can call up the most suitable effector function as needed: IgM to activate complement within vessels, IgG to opsonize in tissues, IgA on mucosae, IgE against parasites; which class is chosen is determined by the cytokines of T cells.

2. When IgG is treated with papain and with pepsin, how do the fragments obtained differ in their ability to bind antigen? Why can $\mathrm{F(ab')_2}$ precipitate antigen while Fab cannot?

   **Answer** Papain cuts on the N-terminal side of the interheavy-chain disulfide bonds of the hinge, giving two monovalent Fab fragments and one Fc; pepsin cuts on the C-terminal side of the disulfide bonds, so the two Fab arms remain joined by disulfide bonds, giving the bivalent $\mathrm{F(ab')_2}$, which retains the ability to cross-link; neither has the effector functions of Fc. Precipitation requires the formation of a cross-linked network, and each antibody must have at least two binding sites (Eq. (9.4) presupposes a bivalent antibody). Fab is monovalent and cannot cross-link, so it does not precipitate.

3. A single site of an antibody has $K_\mathrm{D} = 10^{-8}\ \mathrm{M}$. Suppose $c_\mathrm{eff} = 10^{-3}\ \mathrm{M}$ for bivalent binding; estimate $K_\mathrm{D}^\text{app}$ for bivalent binding with Eq. (9.3). What happens if $c_\mathrm{eff}$ falls to $10^{-6}\ \mathrm{M}$ because the epitopes on the antigen are sparse?

   **Answer** In the first case, $c_\mathrm{eff}/K_\mathrm{D} = 10^5$ and $K_\mathrm{D}^\text{app} = 10^{-8}/(1 + 10^5) \approx 10^{-13}\ \mathrm{M}$. In the second, $c_\mathrm{eff}/K_\mathrm{D} = 100$ and $K_\mathrm{D}^\text{app} = 10^{-8}/101 \approx 10^{-10}\ \mathrm{M}$. With sparse epitopes there is still a gain, but three orders of magnitude smaller. In the extreme case the spacing of the epitopes exceeds the distance the two arms can span, $c_\mathrm{eff} \to 0$, bivalent binding is impossible, and avidity falls back to the affinity of a single valency.

4. Why, in an immunological assay, does the precipitation reaction become weaker when antigen is in great excess? How can the resulting false negative be avoided?

   **Answer** With antigen excess, the two sites of each antibody bind different antigen molecules, the epitopes of the antigen are saturated, and no spare antibody is left to form bridges, so only small soluble complexes form ($\rho \ll 1$, and the left side of Eq. (9.4) is less than 1). Diluting the sample before measuring brings the amount of antigen back near the zone of equivalence; measuring several dilutions at once can reveal this postzone effect.

5. (Open question) Compare the possible applications of IgG and IgM as therapeutic antibodies, and state the advantages and limitations of each.

   **Answer** Ideas: IgG has a long half-life (FcRn recycling), can enter tissues, and has mature platforms for humanization and engineering; its effector functions (ADCC, complement, opsonization) can be adjusted by Fc engineering, so it is the format of the great majority of antibody drugs at present. IgM has 10 valencies, high avidity and strong complement activation, and is suited to binding low-affinity, densely repetitive antigens (such as glycans), but it is a large molecule ($970\ \mathrm{kDa}$), penetrates tissue poorly, has a short half-life, and is hard to produce and to formulate stably, so it is little used at present. In design, a compromise can use the Fc of IgG together with a multivalent (for example tetravalent) binding module.
