---
title: The Major Histocompatibility Complex
source_hash: 9186f2ca8275
---

The second question on the knowledge path is "what is recognized?" A B-cell receptor binds the intact antigen directly, but a T cell always sees a complex of a peptide and a host molecule, and that host molecule is the MHC molecule encoded by the major histocompatibility complex. The previous chapter ([7.15.12](/7.15.12)) explained where the diversity of the **T-cell receptor** comes from. This chapter covers the other half of what the receptor recognizes, the MHC molecule itself: how its genes are organized, how the molecule binds peptides, why it is so polymorphic in human populations, how natural selection maintains that polymorphism, and why it determines whether a transplant succeeds and why it is associated with so many diseases. How antigens are cut into peptides and loaded onto MHC molecules is the subject of the next chapter ([7.15.14](/7.15.14)); how T cells learn in the thymus to recognize only self MHC is covered in [7.15.15](/7.15.15).

The MHC is also the best example linking immunology to population genetics: haplotypes, linkage disequilibrium and Hardy–Weinberg calculations ([7.4.22](/7.4.22)), and the genomic signatures of balancing selection ([7.10.8](/7.10.8)) all have direct immunological meaning here.

## 13.1. The Concept and Discovery of the MHC

In the 1930s and 1940s, Gorer and Snell carried out tumor and skin transplants between inbred mouse strains and found that the antigens deciding whether a graft survives are encoded mainly by a single genetic region, which they called H-2 (histocompatibility-2). In the 1950s, Dausset and colleagues found that the sera of people who had received multiple transfusions or had multiple pregnancies contained antibodies that agglutinate other people's leukocytes, which led to the identification of alloantigens on human leukocytes. The two lines of work ultimately pointed to the same family of genes: the molecules they encode determine not only the compatibility of transplants but also whether T cells can respond to a given antigen (Benacerraf's immune response genes). Benacerraf, Dausset and Snell shared the 1980 Nobel Prize in Physiology or Medicine for this work.

**Definition 13.1.1 (Major Histocompatibility Complex)** The **major histocompatibility complex** (MHC) is a group of tightly linked genes in vertebrate genomes. It encodes the MHC molecules that present antigenic peptides to T cells, together with several molecules involved in antigen processing, complement and inflammation, and it is the strongest genetic region provoking allograft rejection. The human MHC is called the **human leukocyte antigen** (HLA) complex, and the mouse MHC is called the H-2 complex.

**Remark 13.1.1** The names carry two meanings: MHC and HLA complex refer to the genes (the locus), whereas MHC molecule and HLA molecule (or HLA antigen) refer to the gene products. "Histocompatibility" is the way the complex was discovered, but presenting antigenic peptides is its physiological function; graft rejection is only the result of T cells mistaking another person's MHC for "self MHC plus foreign peptide" (§13.6). Besides the MHC, the genome contains many polymorphic genes encoding minor histocompatibility antigens, each of which causes only weak rejection on its own.

## 13.2. Genomic Organization of the HLA Complex

The HLA complex lies on the short arm of chromosome 6 at 6p21.3. It spans about 3.6 Mb and is one of the most gene-dense regions of the human genome. Its complete sequence, finished in 1999, annotated 224 loci, of which about 128 were predicted to be expressed, and about 40% of the expressed genes are related to immunity. Details of the annotation have been updated since, but the picture of "two hundred or so loci, about half of them functional" has not changed. By function and position, the complex is divided from centromere to telomere into three regions (Figure 13.2).

| Region | Position | Main genes | Products and functions |
|---|---|---|---|
| Class I region | Far from the centromere (telomeric side) | Classical: HLA-A, -B, -C; nonclassical: HLA-E, -F, -G; MICA, MICB | Heavy chain (α chain) of classical class I molecules; nonclassical molecules regulate NK cells; MIC proteins are stress ligands of NKG2D |
| Class III region | Between the class I and class II regions | C2, C4A, C4B, CFB (Bf); TNF, LTA, LTB; HSPA1A/B; CYP21A2 | Complement components, inflammatory cytokines, heat shock proteins; no antigen presentation |
| Class II region | Close to the centromere | Classical: HLA-DR (DRA, DRB1, and one of DRB3/4/5), -DQ (DQA1, DQB1), -DP (DPA1, DPB1); nonclassical: HLA-DM (DMA, DMB), HLA-DO (DOA, DOB); antigen-processing genes TAP1, TAP2, PSMB8, PSMB9 | α and β chains of classical class II molecules; DM catalyzes peptide exchange on class II molecules; TAP transports peptides, and PSMB8/9 are immunoproteasome subunits ([7.15.14](/7.15.14)) |

![The human HLA complex and the mouse H-2 complex. Top: the roughly 3.6 Mb segment at 6p21.3, approximately to scale in GRCh37 coordinates, with the telomeric direction at left and the centromeric direction at right. The class I region (purple) contains the classical class I genes HLA-A, -C and -B (bold) and the nonclassical HLA-E, -F, -G, as well as MICA and MICB; the class III region (yellow) contains the complement genes C2, CFB, C4A and C4B, together with TNF, LTA, HSPA1A and others; the class II region (green) contains the α- and β-chain genes of the classical class II molecules DR, DQ and DP (bold), as well as HLA-DM, HLA-DO and the antigen-processing genes TAP1, TAP2, PSMB8 and PSMB9. Bottom: the order of regions of mouse H-2 on chromosome 17 (order only, not to scale). The class I gene K lies on the centromeric side of the class II region (I-A, I-E), and D and L lie on the other side of the class III region (S)](./plots/hla-map.py)

Several details are worth remembering:

- The light chain of class I molecules, **β2-microglobulin**, is encoded by the *B2M* gene on chromosome 15, outside the MHC; both chains of class II molecules are encoded within the MHC.
- Each classical class II subregion contains A and B loci, which encode the α chain and the β chain, respectively (for example, *HLA-DPA1* encodes the α chain of DP and *HLA-DPB1* the β chain). *HLA-DRA* has almost no polymorphism, so all of the polymorphism of DR molecules comes from the β chain.
- Mouse H-2 consists of the class I genes K, D and L and the class II genes I-A (Aa, Ab) and I-E (Ea, Eb), with K separated from the others by the class II region. Many inbred strains (such as C57BL/6) have a defective *Ea* and do not express I-E. The classical mouse haplotypes are written $H\text{-}2^b$, $H\text{-}2^k$ and $H\text{-}2^d$.
- That the MHC clusters genes for antigen processing, complement and inflammation may be because these functions require coordinated evolution and coordinated regulation, but the evolutionary reason for the clustering itself is still debated.

## 13.3. Structure of MHC Molecules

The three-dimensional structures of the two classes of classical MHC molecules are strikingly similar: the end distal to the cell membrane is a "platform" formed by two domains, with a groove on the platform that accommodates the antigenic peptide, and the membrane-proximal part consists of two immunoglobulin-like domains. This design was first seen in the crystal structure of HLA-A2 solved by Bjorkman, Wiley and Strominger in 1987, in which the groove contained a patch of electron density that could not be assigned; it later proved to be a mixture of endogenous peptides.

**Definition 13.3.1 (MHC Class I Molecule)** An **MHC class I molecule** consists of a transmembrane heavy chain encoded in the MHC (the α chain, about $45\,\mathrm{kDa}$, with three extracellular domains α1, α2 and α3) and a noncovalently associated **β2-microglobulin** (β2m, about $12\,\mathrm{kDa}$). The α1 and α2 domains form the peptide-binding groove, and α3 and β2m are immunoglobulin-like domains; CD8 binds α3.

**Definition 13.3.2 (MHC Class II Molecule)** An **MHC class II molecule** consists of two transmembrane chains encoded in the MHC: an α chain (about $34\,\mathrm{kDa}$, with domains α1 and α2) and a β chain (about $29\,\mathrm{kDa}$, with domains β1 and β2). The α1 and β1 domains together form the peptide-binding groove, and α2 and β2 are immunoglobulin-like domains; CD4 binds β2.

**Definition 13.3.3 (Peptide-Binding Groove)** The **peptide-binding groove** is the groove at the membrane-distal end of an MHC molecule. Its floor is a β sheet made of eight antiparallel β strands, and its two walls are two α helices. The peptide lies in the groove in an extended conformation: some side chains insert into pockets in the floor, while other side chains and the backbone point upward, where they can be contacted by the T-cell receptor.

The key difference between the two classes of groove lies at the ends:

- The groove of a class I molecule is closed at both ends. The free N and C termini of the peptide are fixed by hydrogen bonds to conserved residues at the two ends of the groove (pockets A and F), so peptide length is tightly restricted, usually 8–10 residues, with 9-mers the most common; longer peptides can only bulge out in the middle.
- The groove of a class II molecule is open at both ends. The peptide can extend out of either end, and its length is 13–25 residues. What actually lies in the groove is a "core" of about 9 residues, and binding relies mainly on hydrogen bonds along the peptide backbone and on pockets such as P1, P4, P6 and P9.

**Definition 13.3.4 (Anchor Residue)** The residues at the few positions of a peptide whose side chains insert into pockets of the MHC groove and that are decisive for binding are called **anchor residues**. The pocket shapes of an MHC allele determine its preferred anchor residues, so what it binds is a family of peptides sharing a common **binding motif**, rather than one particular peptide.

**Example 13.3.1** HLA-A\*02:01 prefers 9-mers with mainly Leu or Met at position 2 and mainly Val or Leu at position 9 (the C terminus). GILGFVFTL from influenza matrix protein (M1 58–66) and SLYNTVATL from HIV-1 Gag are both classical epitopes it presents, and in both P2 and P9 are hydrophobic residues. Figure 13.3B draws this motif as a schematic probability matrix: the information is concentrated at the two anchor positions and the other positions are nearly random, so the same HLA molecule can bind thousands of different peptides. HLA-B\*27:05, by contrast, requires Arg at P2. Different alleles have different anchor preferences, which is the molecular basis for "different people present different fragments of a pathogen."

:::

![MHC class I and class II molecules. A: Schematic of the domains at the cell membrane. A class I molecule consists of the heavy-chain domains α1, α2 and α3 and β2-microglobulin; α1 and α2 form a groove closed at both ends that accommodates a peptide of 8–10 residues, and CD8 binds α3. A class II molecule consists of an α chain (α1, α2) and a β chain (β1, β2); α1 and β1 form a groove open at both ends from which the peptide ends protrude, and CD4 binds β2. The membrane-proximal domains of both are immunoglobulin-like domains. B: Schematic sequence logo of a 9-mer bound by HLA-A\*02:01 (the probability matrix was set by hand from published motifs and is not data): the information is concentrated at the anchor residues P2 (Leu > Met) and P9 (Val > Leu), and the other positions are close to random](./plots/mhc-structures.py)

| Feature | MHC class I molecule | MHC class II molecule |
|---|---|---|
| Chain composition | α chain (MHC-encoded) + β2m (chromosome 15) | α chain + β chain (both MHC-encoded) |
| Binding groove | α1 + α2, closed at both ends | α1 + β1, open at both ends |
| Peptide length | 8–10 residues | 13–25 residues (core about 9) |
| Coreceptor-binding site | α3 binds CD8 | β2 binds CD4 |
| Main source of peptides | Cytosolic and nuclear proteins (endogenous) | Endocytosed and extracellular proteins (exogenous) |
| Distribution | Almost all nucleated cells | Professional antigen-presenting cells, thymic epithelial cells; human activated T cells; inducible |
| Responding cell | CD8⁺ T cell | CD4⁺ T cell |

The domains α3, β2m, α2 and β2 all belong to the **immunoglobulin superfamily**. An MHC molecule without a bound peptide is unstable: an empty class I molecule dissociates rapidly at the cell surface and loses β2m, whereas a molecule bound to a high-affinity peptide can remain at the surface for more than a day. This "peptide-stabilized MHC" property ensures that the great majority of MHC molecules at the surface carry a peptide, so that what is read out is what is happening inside the cell ([7.15.14](/7.15.14)).

## 13.4. Genetic Features of the MHC

Three genetic features of the MHC, namely polygeny, polymorphism and codominant expression, together determine how many different peptides an individual can present and how different the MHC of two individuals is.

Polygeny: each person has several classical loci with similar functions (class I: A, B, C; class II: DR, DQ, DP), which are products of ancient gene duplications. Even if each locus had only one allele, a person would still have several MHC molecules with different binding preferences.

**Definition 13.4.1 (MHC Polymorphism)** The existence of a large number of alleles at the same MHC locus in a population is called **MHC polymorphism**. Polymorphism is a population-level concept: an individual has at most two alleles at each locus (one from each parent), but the number of alleles in the population can reach thousands.

The classical HLA genes are the most polymorphic genes in the human genome. As of 2025, the IPD-IMGT/HLA database lists more than 40,000 HLA alleles, with HLA-B having the most, HLA-A, HLA-C and HLA-DRB1 following with several thousand each; *HLA-DRA* has only a handful and they encode nearly identical proteins. The number grows every year as sequencing becomes more widespread, so figures in textbooks (such as about 17,000 in 2017) are only a snapshot at one moment. Allele names such as HLA-A\*02:01:01:01 are read as follows: the first field is the allele group (roughly corresponding to the serological specificity A2), the second field is the subtype encoding a distinct protein, the third field distinguishes synonymous mutations, and the fourth field distinguishes differences in noncoding regions; clinical reports usually give only the first two fields.

Polymorphism is not distributed uniformly: the amino acid differences between alleles are concentrated in the floor and walls of the binding groove, that is, in the pockets that determine anchor preferences and in the helices contacted by the TCR. The direct consequence of MHC polymorphism is therefore that different people bind and present different peptides.

**Definition 13.4.2 (Codominant Expression)** When both alleles at a locus, one from each parent, are expressed, this is called **codominant expression**. MHC genes are expressed codominantly.

Because of codominance, a person heterozygous at every classical HLA locus expresses 6 classical class I molecules (two each of A, B and C). Class II molecules are more numerous: both the α and β chains of DQ and DP are polymorphic, and chains from the two haplotypes can pair in cis or in trans, so each subregion can form up to 4 heterodimers; the α chain of DR is invariant, but many haplotypes carry a DRB3, DRB4 or DRB5 gene in addition to DRB1. The cell surface of an individual therefore carries at least 12 and usually a dozen to twenty different classical MHC molecules (whether particular α–β combinations can pair stably is restricted by isotype).

Haplotype inheritance: the recombination rate within the MHC is low (about 1%–3% per meiosis from HLA-A to HLA-DP), so the whole set of HLA alleles on one chromosome is usually transmitted to the offspring as a unit, a **haplotype** ([7.4.8](/7.4.8)). A person's HLA type is determined by the one haplotype contributed by each parent.

**Example 13.4.1** Suppose the father's haplotypes are $a/b$ and the mother's are $c/d$. The genotype of a child is one of $ac$, $ad$, $bc$, $bd$, each with probability $1/4$ (ignoring recombination). Two siblings are therefore fully HLA-identical with probability $1/4$, share exactly one haplotype (haploidentical) with probability $1/2$, and share none with probability $1/4$. If a patient has $n$ siblings, the probability that at least one is fully matched is $1 - (3/4)^n$: $25\%$ for $n = 1$ and $58\%$ for $n = 3$. The more common one-child families become, the more reliance there is on unrelated donor registries and haploidentical transplantation ([7.15.29](/7.15.29)).

**Linkage disequilibrium**: in a population, certain combinations of alleles occur together on the same haplotype more often than the product of their individual frequencies. It is measured by $D = p_{AB} - p_A p_B$ ([7.4.22](/7.4.22)).

**Example 13.4.2** Suppose in some population an allele $A$ of DRB1 has frequency $p_A = 0.156$ and an allele $B$ of DQB1 has frequency $p_B = 0.219$. If the two were independent, the frequency of the haplotype carrying $A$–$B$ would be $0.156 \times 0.219 \approx 0.034$; the observed value is $0.113$. Then

$$
D = 0.113 - 0.034 = 0.079,\qquad D' = \frac{D}{\min\{p_A(1-p_B),\,(1-p_A)p_B\}} = \frac{0.079}{0.122} \approx 0.65.
$$

DR and DQ are less than $100\,\mathrm{kb}$ apart, and linkage disequilibrium between them is generally strong. Some long haplotypes (such as A1–B8–DR3 in European populations, the "ancestral haplotype 8.1") span several Mb and are scarcely broken up by recombination. This makes it hard for disease association studies to tell which locus is actually responsible, and it also makes matching unrelated donors easier than a calculation assuming independence of allele frequencies would suggest.

:::

Neutral alleles in a finite population are eliminated one by one by genetic drift, so several thousand alleles cannot be maintained by neutral processes. MHC polymorphism is maintained by **balancing selection**, and three kinds of mechanism have been proposed, with varying degrees of support ([7.10.8](/7.10.8)):

1. **Heterozygote advantage**: heterozygotes can present a greater variety of pathogen peptides and are more resistant to multiple pathogens (proposed by Doherty and Zinkernagel in 1975). In HIV infection, people heterozygous at all HLA class I loci progress to AIDS more slowly, which is fairly direct evidence in humans.
2. **Negative frequency-dependent selection**: pathogens adapt to the most common MHC types in the population (escaping the epitopes they present), giving rare alleles an advantage.
3. Mating preference and maternal–fetal interaction: mice can prefer mates with a different MHC by smell, and whether this operates in humans is still controversial.

The signatures left by balancing selection are clear: the rate of nonsynonymous substitution at sites encoding the binding groove is much higher than the rate of synonymous substitution ($d_N/d_S > 1$); and allelic lineages are older than species, so some HLA alleles of humans and chimpanzees are more similar to each other than some alleles within humans are (trans-species polymorphism).

**Example 13.4.3 (Wright–Fisher Model of Balancing Selection)** Consider one MHC locus in $N$ diploid individuals ($2N$ gene copies), in which each copy mutates every generation with probability $u$ to an entirely new allele (infinite-alleles model). Under symmetric heterozygote advantage, the fitness of homozygotes is $1 - s$ and that of heterozygotes is $1$; the marginal fitness of an allele with frequency $p_i$ is

$$
w_i = 1 - s\,p_i,
$$

so rare alleles benefit automatically. Negative frequency-dependent selection in its simplest form gives the same $w_i = 1 - c\,p_i$. Under neutrality ($s = 0$), the expected steady-state heterozygosity is $H = \theta/(1+\theta)$, with $\theta = 4Nu$ ([7.4.23](/7.4.23)). The simulation in Figure 13.4 takes $N = 1000$ and $u = 5\times 10^{-4}$ ($\theta = 2$). Under neutrality the heterozygosity fluctuates widely under drift, and only a few alleles have frequency of at least 1%; $s = 0.02$ stabilizes the heterozygosity at about 0.85, and with $s = 0.1$ the effective number of alleles $1/(1-H)$ reaches more than three times the neutral value. The stronger the selection, the more alleles are maintained and the more even their frequencies.

:::

![Balancing selection maintains MHC polymorphism (Wright–Fisher simulation, illustrative parameters). $N = 1000$ diploid individuals; each gene copy mutates every generation to a new allele with probability $u = 5\times10^{-4}$ ($\theta = 4Nu = 2$); homozygote fitness is $1-s$. A: number of alleles with frequency of at least 1%. B: heterozygosity $H = 1 - \sum p_i^2$, with the dashed line the neutral steady-state expectation $\theta/(1+\theta)$; a neutral population starts from a single allele, needs about $4N$ generations to approach this expectation, and fluctuates widely under drift; with heterozygote advantage, heterozygosity rises rapidly and stabilizes at a high level. C: effective number of alleles $1/(1-H)$ (averaged over generations 1000–3000) increases with the selection coefficient $s$, with the dashed line the neutral expectation $1+\theta$](./plots/balancing-selection.py)

## 13.5. Distribution and Regulation of MHC Expression

The two classes of molecules differ in distribution, which is the basis of their division of labor:

- **MHC class I molecules** are expressed on almost all nucleated cells, but at very different levels: highest on lymphocytes, lower on hepatocytes and neurons; mature erythrocytes have no nucleus and do not express them; extravillous trophoblast cells of the placenta do not express HLA-A or -B and express only HLA-C, -E and -G (§13.6). Any cell may be infected by a virus or become malignant, so every cell needs to be able to "report" its intracellular proteins.
- **MHC class II molecules** are expressed constitutively on professional antigen-presenting cells (dendritic cells, macrophages, B cells) and thymic epithelial cells; human activated T cells also express them (mouse T cells do not); endothelial cells, epithelial cells and fibroblasts can be induced to express them under the action of IFN-γ. Class II molecules need to appear only on cells that can initiate, or receive, help from CD4⁺ T cells.

Expression is regulated by cytokines: **interferon** upregulates class I molecules, β2m, TAP and immunoproteasome subunits through JAK–STAT signaling, and IFN-γ also induces class II molecules. Transcription of class II genes is controlled centrally by the class II transactivator CIITA. CIITA itself does not bind DNA but is recruited to a promoter complex composed of RFX, CREB and NF-Y, where it acts as a "master switch"; the corresponding coactivator for class I genes is NLRC5. Mutations in CIITA or in RFX subunits abolish class II molecules completely and cause bare lymphocyte syndrome type II, in which patients have almost no CD4⁺ T cells ([7.15.31](/7.15.31)); this shows that class II molecules are required for the development of CD4⁺ T cells ([7.15.15](/7.15.15)).

Abnormal MHC expression also has clinical significance. Many tumors lose HLA class I molecules (β2m mutations, loss of an HLA haplotype) to escape CTLs ([7.15.30](/7.15.30)); in patients with type 1 diabetes, pancreatic β cells show increased aberrant expression of class I molecules, and induction of class II molecules on nonprofessional cells in inflamed tissue may amplify autoimmune responses ([7.15.28](/7.15.28)).

## 13.6. MHC Restriction and the Functions of HLA Molecules

**Example 13.6.1 (The Zinkernagel–Doherty Experiment)** In 1974, Zinkernagel and Doherty infected $H\text{-}2^k$ mice with lymphocytic choriomeningitis virus (LCMV) and tested their CTLs for killing of virus-infected fibroblasts of different origins:

| Target cell | Result | Interpretation |
|---|---|---|
| $H\text{-}2^k$ cell + LCMV | Killed | Recognition of self MHC I + viral antigen |
| $H\text{-}2^k$ cell + unrelated virus | Not killed | Wrong antigen |
| $H\text{-}2^b$ cell + LCMV | Not killed | Wrong MHC |
| $H\text{-}2^b$ cell + unrelated virus | Not killed | Both wrong |

CTLs kill only cells that have both the correct antigen and self MHC. The two investigators shared the 1996 Nobel Prize in Physiology or Medicine for this work.

:::

**Definition 13.6.1 (MHC Restriction)** The phenomenon that T cells recognize only antigenic peptides bound to self MHC molecules, and not free antigen or the same peptide bound to other MHC alleles, is called **MHC restriction**: CD8⁺ T cells are restricted by self MHC class I molecules, and CD4⁺ T cells by self MHC class II molecules.

The structural basis of restriction is that the TCR contacts both the peptide and the MHC: the TCR sits across the pMHC in a roughly diagonal orientation, with CDR1 and CDR2 (germline-encoded) contacting mainly the two α helices of the MHC and the hypervariable CDR3 contacting mainly the middle of the peptide ([7.15.12](/7.15.12)). Which MHC molecules are treated as "self" is learned by T cells in the thymus (**positive selection**, [7.15.15](/7.15.15)): in bone marrow chimeric mice, T cells are restricted by the MHC type of the thymic epithelium and not by the MHC type of the T cells themselves.

One corollary is alloreactivity: 1%–10% of the T cells in the body can directly recognize another person's MHC molecules, orders of magnitude higher than the precursor frequency for any single foreign peptide (about one in a hundred thousand). The reason is that the polymorphic residues of another person's MHC, together with the many different peptides it carries, look to the TCR like "self MHC plus assorted foreign peptides." This is why allograft rejection is so strong and why the **mixed lymphocyte reaction** is pronounced ([7.15.29](/7.15.29)).

The functions of HLA molecules can be summarized in two aspects:

1. Roles in adaptive immunity: presenting antigenic peptides and determining the MHC restriction of T-cell recognition; taking part in the selection and differentiation of T cells in the thymus; through MHC polymorphism, different individuals in a population present different epitopes, which makes the population's immune responses heterogeneous so that a pathogen can hardly escape everyone with a single mutation; determining individual differences in disease susceptibility (§13.7); and acting as the strongest transplantation antigens.
2. Roles in innate immunity and inflammation: the class III region encodes complement C2, C4 and factor B, as well as TNF and LT; nonclassical molecules regulate **natural killer cells** (NK cells).

**Definition 13.6.2 (Nonclassical MHC Molecule)** Molecules that are structurally similar to classical MHC molecules but have very low polymorphism, special distribution or ligands, and do not mainly present diverse peptides to conventional αβ T cells are called **nonclassical MHC molecules** (MHC class Ib).

| Molecule | Encoded in | Ligand or cargo | Recognized by, and function |
|---|---|---|---|
| HLA-E | MHC class I region | 9-mer from the signal peptides of other class I molecules | CD94/NKG2A of NK cells (inhibitory): reports whether the cell's class I synthesis is normal |
| HLA-G | MHC class I region | Limited set of peptides; soluble and membrane forms | Expressed by extravillous trophoblast cells; binds LILRB1 and KIR2DL4, inhibits maternal NK cells, and contributes to maternal–fetal tolerance |
| HLA-F | MHC class I region | Open-conformation heavy chains | KIR3DS1 and others; function still under study |
| MICA, MICB | MHC class I region | Do not bind peptides and do not need β2m | Induced by stress, infection and malignant transformation; activate NKG2D on NK cells and γδ T cells |
| HLA-DM, HLA-DO | MHC class II region | Do not present | Catalyze (DM) or inhibit (DO) peptide exchange on class II molecules ([7.15.14](/7.15.14)) |
| CD1a–e | Chromosome 1 | Lipids and glycolipids | Presented to NKT cells and some αβ and γδ T cells ([7.15.14](/7.15.14)) |
| MR1 | Chromosome 1 | Microbial riboflavin metabolites | MAIT cells |
| HFE, FcRn | Inside or outside the MHC | Do not present | Iron metabolism; transport and recycling of IgG ([7.15.21](/7.15.21)) |

HLA-E is an ingenious design. The peptide it loads comes from the signal peptides of HLA-A, -B and -C, so HLA-E can reach the cell surface and inhibit NK cells through NKG2A only when the cell is synthesizing classical class I molecules normally. If a virus shuts down class I synthesis to escape CTLs, HLA-E disappears with it and NK cells are released; this is one concrete mechanism of **missing self** recognition. The extravillous trophoblast cells of the placenta do not express HLA-A or -B, which avoids recognition by maternal T cells; the retained HLA-C, HLA-E and HLA-G inhibit uterine NK cells and regulate their secretion of factors that promote spiral artery remodeling ([7.14.38](/7.14.38)).

## 13.7. HLA and Clinical Medicine

HLA typing: early methods used serology (the complement-dependent microcytotoxicity test) and the mixed lymphocyte reaction; now PCR-based typing and sequencing are used, which can resolve to the second field or beyond.

Transplant matching: survival decreases in the order identical twins > HLA-identical siblings > other relatives > unrelated donors. Different organs have different requirements:

- In solid organ (for example kidney) transplantation, matching at the DR locus matters most, followed by B and A; more critical is whether the recipient has preexisting antibodies against donor HLA (a positive crossmatch causes hyperacute rejection).
- Hematopoietic stem cell transplantation has the most stringent matching requirements. For unrelated donors, high-resolution 8/8 matching at HLA-A, -B, -C and -DRB1 is usually required (10/10 with DQB1); otherwise the risk of graft-versus-host disease increases markedly. Bone marrow registries and cord blood banks were established for this purpose. The mechanisms of rejection and matching are discussed in [7.15.29](/7.15.29).

Disease associations: some HLA alleles are significantly more frequent in patients than in healthy populations. Associations are measured by relative risk or odds ratio, and the calculation is covered in the tests for categorical data ([7.7.9](/7.7.9)).

**Example 13.7.1** About 90% of patients with ankylosing spondylitis are HLA-B27 positive, versus about 8% of the general population (4%–9% across populations). Putting the positivity rates of patients and controls directly into a $2\times 2$ table gives the odds ratio

$$
\mathrm{OR} = \frac{0.90/0.10}{0.08/0.92} \approx 104.
$$

This is one of the strongest genetic associations among human diseases. But a strong association does not mean that most carriers become ill. Suppose the population prevalence is $\mathbb{P}(\mathrm{AS}) = 0.3\%$; by **Bayes' theorem**,

$$
\mathbb{P}(\mathrm{AS}\mid \mathrm{B27}^+) = \frac{\mathbb{P}(\mathrm{B27}^+\mid \mathrm{AS})\,\mathbb{P}(\mathrm{AS})}{\mathbb{P}(\mathrm{B27}^+)} = \frac{0.90 \times 0.003}{0.08} \approx 3.4\%,
$$

so only a few percent of B27-positive people fall ill. HLA-B27 testing is therefore used to support a diagnosis (in symptomatic people the posterior probability is high), not to screen healthy people.

:::

| Disease | Associated HLA | Strength of association (order of magnitude) | Notes |
|---|---|---|---|
| Ankylosing spondylitis | B\*27 | OR about $10^2$ | Hypothesized mechanisms: B27 misfolding and the unfolded protein response, recognition of heavy-chain dimers by KIRs, presentation of arthritogenic peptides |
| Celiac disease | DQ2.5 (DQA1\*05–DQB1\*02), DQ8 | Almost all patients carry one of them | Binds deamidated, negatively charged gliadin peptides; the best-understood mechanism ([7.15.23](/7.15.23)) |
| Type 1 diabetes | DR3-DQ2, DR4-DQ8; DQ6 (DQB1\*06:02) protective | OR about 15–20 for DR3/DR4 heterozygotes | A non-Asp residue at position 57 of the DQ8 β chain alters the P9 pocket |
| Narcolepsy | DQB1\*06:02 | Carried by the great majority of patients | T-cell-mediated destruction of hypocretin (orexin) neurons in the hypothalamus |
| Rheumatoid arthritis | The "shared epitope" of DRB1 (for example \*04:01) | OR about 3–5 | Shared sequence at positions 70–74; related to binding of citrullinated peptides |
| Multiple sclerosis | DRB1\*15:01 | OR about 3 | The strongest genetic risk factor, but with a moderate effect |
| Drug hypersensitivity | B\*57:01 (abacavir), B\*15:02 (carbamazepine, in Han Chinese and other Asian populations), B\*58:01 (allopurinol) | OR up to $10^2$–$10^3$ | The drug alters the peptides carried in the groove or interacts directly with the HLA–TCR complex; genetic testing before treatment is now routine |

There are several possible mechanisms behind an association: the HLA molecule presents a pathogenic self peptide or a cross-reactive pathogen peptide, it influences selection in the thymus, or it is merely in linkage disequilibrium with the truly causal gene. The statistics and mechanisms of HLA associations in autoimmune diseases are discussed in [7.15.28](/7.15.28).

Other applications: the high polymorphism of HLA makes it nearly impossible for two unrelated people to have identical HLA types, so it was once used in paternity testing and forensics (now largely replaced by STR typing and sequencing); allele and haplotype frequencies of HLA differ greatly among populations and serve as genetic markers for studying the origins and migrations of populations.

## Summary

- The **MHC** is a group of tightly linked genes encoding antigen-presenting molecules; in humans it is called the **HLA** complex (6p21.3), and in mice H-2 (chromosome 17). The name comes from transplantation, and the function is antigen presentation (Definition 13.1.1).
- Three regions: class I (classical HLA-A, -B, -C; nonclassical E, F, G; MIC), class III (complement, TNF, HSP70; no antigen presentation), class II (classical DR, DQ, DP; DM, DO; TAP, PSMB8/9).

| | Class I molecule (Definition 13.3.1) | Class II molecule (Definition 13.3.2) |
|---|---|---|
| Composition | α chain + β2m | α chain + β chain |
| Binding groove (Definition 13.3.3) | α1α2, closed at both ends, 8–10-mers | α1β1, open at both ends, 13–25-mers |
| Coreceptor | CD8 (α3) | CD4 (β2) |
| Distribution | Almost all nucleated cells | Professional APCs, thymic epithelium; inducible |
| Target | CD8⁺ T cells | CD4⁺ T cells |

- Each MHC molecule binds a large family of peptides sharing a common motif through a few **anchor residues** (Definition 13.3.4, Example 13.3.1).
- Genetic features: polygeny, high polymorphism (Definition 13.4.1; more than 40,000 alleles, with differences concentrated in the binding groove), codominant expression (Definition 13.4.2), haplotype inheritance (full sibling match 1/4, Example 13.4.1), and strong linkage disequilibrium (Example 13.4.2).
- Polymorphism is maintained by balancing selection: heterozygote advantage and negative frequency-dependent selection both favor rare alleles (Example 13.4.3), leaving the signatures of $d_N/d_S > 1$ and trans-species polymorphism.
- Expression is regulated by interferons; CIITA controls class II genes, and its deficiency abolishes CD4⁺ T cells.
- **MHC restriction** (Definition 13.6.1, Example 13.6.1): T cells recognize self MHC plus peptide; alloreactive T cells make up as much as 1%–10%.
- **Nonclassical MHC molecules** (Definition 13.6.2) link the MHC to innate immunity: HLA-E reports class I synthesis (missing self), HLA-G contributes to maternal–fetal tolerance, MIC proteins are stress ligands, and CD1 and MR1 present nonpeptide antigens.
- Clinical aspects: matching (most stringent for hematopoietic stem cell transplantation); disease associations (OR about 100 for HLA-B27, yet only a few percent of carriers become ill, Example 13.7.1); genetic testing for drug hypersensitivity.

## Questions

1. Why do MHC class I molecules need to be expressed on almost all nucleated cells, whereas class II molecules need to be expressed on only a few cell types?

   **Answer** Class I molecules present proteins synthesized inside the cell, allowing CD8⁺ T cells to monitor virus infection and malignant transformation; any nucleated cell may be infected or become cancerous, so all of them need to "report" their intracellular state, and recognized cells are eliminated by CTLs. Class II molecules present ingested exogenous proteins to CD4⁺ T cells; the function of CD4⁺ T cells is help and regulation, so they need to recognize antigen only on the professional APCs that can initiate them and on the cells that receive their help (B cells, macrophages). Expressing class II molecules on all cells would instead increase the risk of autoimmunity.

2. A patient has 2 siblings. Ignoring recombination within the MHC, what is the probability that at least one sibling is fully HLA-matched? How does the result change if a recombination rate of about 2% per meiosis is considered?

   **Answer** Each sibling is fully matched with probability $1/4$, independently, so the probability is $1-(3/4)^2 = 7/16 \approx 44\%$. With recombination, the probability that a sibling receives from each parent the same intact haplotype as the patient is slightly below $1/4$: the haplotypes that the patient and the sibling each receive from each parent may be recombinant, so the probability that a single sibling is fully matched is about $(1/2 \times 0.98)^2 \approx 0.24$, and the probability that at least one is fully matched is about $1 - 0.76^2 \approx 42\%$, little changed. But recombinant haplotypes mean that a "full match" has to be confirmed by typing rather than inferred from the pedigree.

3. MHC polymorphism benefits the individual, so why does each person not simply have dozens of MHC loci?

   **Answer** One leading explanation is the cost to the T-cell repertoire: each additional kind of MHC molecule means that negative selection in the thymus must eliminate another batch of T cells with high affinity for "self peptide plus that MHC," shrinking the usable repertoire. Theoretical models and comparative data (such as the relation between MHC gene number and repertoire in fish and birds) indicate that the number of expressed MHC types has an intermediate optimum. Polymorphism at the population level (different individuals having different MHC) does not pay this cost and yet prevents a pathogen from escaping all individuals at once, which is why polymorphism is high while the number of loci per individual is limited.

4. A study finds that HLA-X positivity is 30% in patients with some disease and 10% in controls. Calculate the odds ratio; why can such an association not directly show that HLA-X causes the disease?

   **Answer** $\mathrm{OR} = (0.3/0.7)/(0.1/0.9) \approx 3.9$. The association may arise because HLA-X itself presents a pathogenic peptide; because HLA-X is in linkage disequilibrium with the truly causal variant (another locus in the MHC); or because cases and controls come from different populations (population stratification: HLA frequencies differ greatly among populations). To identify the causal allele, fine mapping and conditional analysis in multiple populations are needed, together with structural and functional experiments testing whether the HLA molecule can present the relevant peptides.
