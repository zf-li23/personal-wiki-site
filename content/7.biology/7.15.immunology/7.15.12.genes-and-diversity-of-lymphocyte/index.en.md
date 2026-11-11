---
title: Genes and Diversity of Lymphocyte Antigen Receptors
description: How one gene, one polypeptide can yield 10^11 antibodies. The structure of the immunoglobulin heavy-chain and light-chain loci, the immunological consequences of V(D)J recombination (combinatorial diversity, junctional diversity, heavy–light chain pairing), allelic exclusion, isotypic exclusion and receptor editing, somatic hypermutation and AID, class switch recombination and alternative splicing of membrane and secreted forms, the TCR loci, and the size of the immune repertoire and its readout by sequencing.
source_hash: 0482dccbe640
---

[7.15.9](/7.15.9) described the structure of antibodies: each antibody has one specific binding site formed by $\mathrm{V_H}$ and $\mathrm{V_L}$, whereas the clonal selection theory of [7.15.1](/7.15.1) requires an organism to have on the order of $10^{11}$ different specificities. This chapter answers the genetic part of the question "who recognizes?" on the path of knowledge ([7.15.1](/7.15.1)): how can a limited number of genes encode an almost unlimited number of specificities? The answer is a somatic, irreversible process of DNA rearrangement (its mechanism was introduced in [7.2.9](/7.2.9)); this chapter treats only its immunological consequences, namely the sources of diversity, the guarantee that a cell expresses only one receptor, the secondary remodeling of receptors during a response, and how to measure the whole "repertoire."

Diversity is produced in two stages. The first stage takes place in the bone marrow and thymus and is independent of antigen: rearrangement of gene segments produces the initial, huge and random receptor repertoire (§12.3). The second stage occurs only in B cells and depends on antigen: somatic hypermutation and class switching further remodel the antibody in mature B cells (§12.5, §12.6), raising its affinity and changing its effector function, which is the affinity maturation of [7.15.20](/7.15.20). The T-cell receptor has only the first stage, a difference of important immunological significance (§12.7).

## 12.1. The Puzzle of Diversity and Antigen Receptors

In the 1960s, antibody amino acid sequences showed that the V region varies greatly while the C region is essentially constant. This contradicted the principle of "one gene, one polypeptide": either the genome contains $10^{11}$ antibody genes (the human genome has only about $2\times10^4$ protein-coding genes), or the V and C regions are encoded by different genes that are joined at the DNA or RNA level. Dreyer and Bennett (1965) proposed the latter hypothesis, and Tonegawa showed in 1976 that the same antibody gene has a different DNA arrangement in B cells than in germline cells: the V and C genes come closer together during lymphocyte development. This discovery earned the 1987 Nobel Prize in Physiology or Medicine.

**Definition 12.1.1 (Antigen Receptor)** The antigen-specific receptors expressed on the surface of lymphocytes are called **antigen receptors**, of which there are two kinds: the antigen receptor of the B cell is called the **B-cell receptor** (BCR), a complex of membrane immunoglobulin and the signaling molecules Igα/Igβ (CD79a/b); the antigen receptor of the T cell is called the **T-cell receptor** (TCR), an αβ or γδ heterodimer together with the CD3 complex.

Each lymphocyte expresses an antigen receptor of only one specificity (clonal selection, [7.15.1](/7.15.1)); the sum of the specificities that an individual possesses is its immune repertoire (§12.8). αβ T cells make up about 95% of T cells in peripheral blood and recognize peptides presented by MHC ([7.15.13](/7.15.13), [7.15.14](/7.15.14)); the receptors of γδ T cells recognize in a different way, independent of classical MHC. This chapter treats the BCR and TCR together because they share the same rearrangement machinery.

## 12.2. Structure of the Loci

The immunoglobulin heavy chain and the two light chains are each encoded by a separate locus, on different chromosomes. Each locus consists of many V, (D) and J gene segments and C genes arranged in tandem, separated from one another in the germline.

| Locus | Chromosome | V | D | J | C | Encodes |
|---|---|---|---|---|---|---|
| IGH | 14q32 | About 40 | About 23 | 6 | 9 functional C genes (Cμ, Cδ, Cγ3, Cγ1, Cα1, Cγ2, Cγ4, Cε, Cα2, in 5′ to 3′ order) | Heavy chain |
| IGK | 2p11 | About 35 | — | 5 | 1 (Cκ) | κ light chain |
| IGL | 22q11 | About 30 | — | 4 functional J–C pairs | 4 | λ light chain |
| TRA/TRD | 14q11 | About 45 (Vα, partly shared with Vδ) | δ: 3 | α: about 50; δ: 4 | Cα, Cδ | α chain, δ chain |
| TRB | 7q34 | About 48 | 2 | 13 | 2 (Cβ1, Cβ2) | β chain |
| TRG | 7p14 | About 6 | — | 5 | 2 | γ chain |

The numbers in the table are approximate numbers of functional segments (there are also a considerable number of pseudogenes, and segment numbers also vary with the individual haplotype), and the calculations in this chapter are based on them. The light-chain loci have no D segment: there is only one junction between V and J, whereas the heavy chain has two junctions, V–D and D–J.

The V, J (and D) segments are flanked by recombination signal sequences (RSS), recognized by RAG1/RAG2 and obeying the 12/23 rule, which ensures that V joins only to D and D only to J ([7.2.9](/7.2.9)). Rearrangement joins one V segment, (one D segment) and one J segment into a complete V-region exon located upstream of the C genes; on transcription, the rearranged V(D)J exon and the exons of the C gene are spliced into a single mRNA.

![Immunoglobulin loci and rearrangement (human, schematic; segment numbers and spacing not to scale). A: The heavy-chain locus. First a D joins a J, and the DNA between them is deleted (①); then a V joins the already joined DJ, and the DNA between them is also deleted (②), with N and P nucleotides added at the junctions (red); the rearranged gene is transcribed and spliced into the μ heavy-chain mRNA (③). B: The κ light-chain locus, with only one V-to-J joining, the C exon being spliced after the VJ exon](./plots/loci.py)

## 12.3. Diversity Generated by V(D)J Recombination

### 12.3.1. Combinatorial Diversity

**Definition 12.3.1 (Combinatorial Diversity)** The diversity that results from the combinations of segment choices when one each of the many V, D and J segments is joined into a V-region exon is called **combinatorial diversity**.

The heavy chain has $V_\mathrm{H} \times D \times J_\mathrm{H}$ choices, and the light chain has two classes, κ and λ, with $V \times J$ choices each. With the numbers of §12.2, the heavy chain has $40 \times 23 \times 6 = 5520$ possibilities, the κ chain $35 \times 5 = 175$ and the λ chain $30 \times 4 = 120$, so the light chains total 295. Heavy and light chains are chosen independently, so the number of combinations for the V region of one antibody is

$$
N_\text{comb} = V_\mathrm{H}\,D\,J_\mathrm{H} \times (V_\kappa J_\kappa + V_\lambda J_\lambda) \approx 5520 \times 295 \approx 1.6 \times 10^{6}. \tag{12.1}
$$

The same calculation for the TCR gives $45 \times 50 = 2250$ for the α chain and $48 \times 2 \times 13 = 1248$ for the β chain, about $2.8 \times 10^6$ combinations.

### 12.3.2. Junctional Diversity

**Definition 12.3.2 (Junctional Diversity)** The diversity that arises at the junctions between V, D and J segments because several nucleotides are removed at random from the ends by exonucleases and other nucleotides are added at random is called **junctional diversity**.

The junctions of rearrangement are not precise. After RAG cuts the DNA, the coding ends form hairpins; when these are opened by the Artemis nuclease, the cut is made at a random position near the tip of the hairpin, leaving a short palindromic sequence on the complementary strand, called P nucleotides. The ends may then be trimmed by exonucleases of several bases, and **terminal deoxynucleotidyl transferase** (TdT for short) adds template-independent N nucleotides at random, often 1–10, and finally non-homologous end joining repairs and joins the junction. These processes take place at the V–D and D–J junctions (heavy chain) and the V–J junction (light chain), exactly where CDR3 lies ([7.15.9](/7.15.9)), so junctional diversity is concentrated where contact with antigen is closest. The price is that, because the number of nucleotides added is random, only about one third of junctions keep the reading frame (codons are read in groups of 3), and the rest produce frameshifts and become nonfunctional rearrangements.

Suppose each junction has $j$ variants of different sequence. The heavy chain has two junctions and the light chain one, so the three junctions together contribute a factor $j^3$, and the total number of antibody receptors is

$$
N_\text{total} \approx N_\text{comb} \times j^{3}. \tag{12.2}
$$

The value of $j$ is hard to give directly, because different rearrangements can produce the same sequence and the probabilities of the variants are not uniform; some estimates put $j$ between $10^{2}$ and $10^{3}$, giving antibodies a theoretical diversity of $10^{12}$–$10^{15}$. Conversely, to reach the $10^{11}$ often quoted in textbooks, each junction needs only about 40 variants ($1.6\times10^6 \times 40^3 \approx 10^{11}$). The calculation for the TCR is the same, with $N_\mathrm{comb} \approx 2.8\times10^{6}$, so the theoretical diversity of the TCR is as enormous as that of antibodies, or even greater.

### 12.3.3. Heavy–Light Chain Pairing and Estimating Diversity

Heavy and light chains come from different loci and rearrange independently, and any pairing of the two chains can form a binding site: the pairing itself is the origin of the multiplication in Eq. (12.1). Diversity therefore relies not on many genes but on the combination and joining of several dozen segments: a genome needs only a few hundred segments to produce more than $10^{12}$ specificities.

![The size of the receptor repertoire. A: The theoretical number of receptors as a function of the number of variants per junction $j$ (Eq. (12.2)): antibodies (red) and αβ TCRs (blue); the dashed line is $10^{11}$, which antibodies reach with about 40 variants per junction. B: The expected number of identical receptor pairs $N^2/(2M)$ (Eq. (12.5)) when $N$ cells are drawn uniformly from $M$ possible receptors, with $M$ taken as $1.6\times10^6$ (combinatorial diversity only), $10^{11}$ and $10^{13}$. C: Somatic hypermutation: the mean number of mutations in a V region, $\mu L n$ (Eq. (12.4)), as a function of the number of cell divisions, with $L = 350$ bp and $\mu$ the mutation rate per base per division](./plots/diversity.py)

## 12.4. Regulation of Rearrangement: Allelic Exclusion, Isotypic Exclusion and Receptor Editing

### 12.4.1. One Cell, One Receptor

Clonal selection requires each lymphocyte to have only one specificity. But B cells are diploid: the heavy chain has two alleles, and the light chain has two alleles at each of the κ and λ loci, so there are six loci that can rearrange. If each rearranged successfully, one cell would express several receptors.

**Definition 12.4.1 (Allelic Exclusion)** The phenomenon in which only one allele (for the heavy chain and the TCR β chain) is expressed in a lymphocyte and the other allele is shut off is called **allelic exclusion**. For light chains there is in addition **isotypic exclusion** between κ and λ: a B cell expresses only one light chain, either κ or λ.

Exclusion is achieved by a feedback mechanism. B-cell development has a fixed order: at the pre-B-cell stage the heavy chain rearranges first, D–J first (on both alleles) and then V–DJ (first on one allele). If that allele forms a functional heavy chain (μ chain), it forms the pre-BCR with the surrogate light chain (VpreB, λ5) and transmits a signal into the cell; this signal lowers expression of RAG and prevents the other allele from rearranging further; if it does not, the other allele rearranges. After the heavy chain succeeds, the light chain rearranges at the small pre-B-cell stage: κ first and, if that fails, λ, each with two alleles. Expression of a functional BCR on the cell surface ends rearrangement ([7.15.19](/7.15.19)). The order of κ first, λ in reserve explains the human κ:λ ratio of about 60:40 (about 95:5 in the mouse).

Because only about one third of junctions keep the reading frame, rearrangement is a game of chance. Suppose the probability that each rearrangement is functional is $1/3$. The heavy chain has two alleles, and the second is tried after the first fails, so the probability of success is $1 - (2/3)^2 = 5/9 \approx 0.56$; the light chain has four alleles, at κ and λ, tried in turn, with success probability $1 - (2/3)^4 = 65/81 \approx 0.80$. The probability that a pre-B cell produces one functional receptor through rearrangement is therefore

$$
P = \left[1 - \left(\tfrac{2}{3}\right)^{2}\right]\left[1 - \left(\tfrac{2}{3}\right)^{4}\right] \approx 0.45. \tag{12.3}
$$

About half of pre-B cells die by apoptosis from failed rearrangement; add the subsequent negative selection ([7.15.19](/7.15.19), [7.15.24](/7.15.24)), and of the hundreds of millions of B-cell precursors that the bone marrow produces each day, only a few become mature B cells. This calculation is schematic: it assumes that the individual rearrangements are independent and that the allele attempts are completed in order, and it also ignores cell selection of functional rearrangements and screening between stages.

### 12.4.2. Receptor Editing

Rearrangement is random, and a randomly generated receptor may recognize a self antigen. If an immature B cell finds that its BCR binds a self antigen, it does not die at once but reopens expression of RAG and rearranges the light chain again, replacing the original with a new light chain so that the receptor no longer recognizes self.

**Definition 12.4.2 (Receptor Editing)** The process in which an immature lymphocyte that finds its receptor recognizes a self antigen reactivates RAG and rearranges the light chain further (for the κ chain, replacing the original rearrangement with an upstream V segment joined to a downstream J segment, or deleting the κ locus and rearranging λ), so as to change the receptor specificity and escape self-reactivity, is called **receptor editing**.

Receptor editing can convert a considerable fraction (estimated at 25%–50%) of B cells that were originally self-reactive into tolerant cells and is one of the main mechanisms of central tolerance ([7.15.24](/7.15.24)); it also explains why the proportion of mature B cells expressing λ light chains is often higher than the simple probability of rearrangement would predict.

## 12.5. Somatic Hypermutation and AID

Rearrangement provides only the initial receptor repertoire. In antigen-driven germinal centers ([7.15.20](/7.15.20)), the V-region genes of mature B cells undergo a second round of remodeling.

**Definition 12.5.1 (Somatic Hypermutation)** The phenomenon in which, under antigenic stimulation and as B cells proliferate, the rearranged V-region gene (and about 1–2 kb of its flanking sequence) undergoes point mutation at a very high frequency is called **somatic hypermutation** (SHM).

The mutation rate is about $10^{-3}$ per base per cell division, $10^6$ times higher than in other genes (about $10^{-9}$ to $10^{-10}$); mutations are concentrated in the V region and the CDRs (the hotspot sequence is RGYW, where R is a purine, Y a pyrimidine and W is A or T), and the C region is almost unaffected. Mutations accumulate with division. Let the V region have length $L = 350\ \mathrm{bp}$ and the mutation rate per division be $\mu$; then the mean number of mutations after $n$ divisions is

$$
\bar m = \mu L n. \tag{12.4}
$$

With $\mu = 10^{-3}$, each division produces on average 0.35 mutations, about 3.5 after 10 divisions, and after several tens of divisions it can reach 10–15, in agreement with the 10–20 mutations commonly found in the V regions of antibodies after affinity maturation (panel C). Mutations are random and most are unhelpful or even harmful; only a few raise affinity, and selection is carried out by antigen and T-cell help ([7.15.20](/7.15.20)). The mutation itself is not directed by antigen but by locus: specificity arises by "random mutation plus selection," the same principle as evolution (models in [7.10](/7.10)).

**Definition 12.5.2 (Activation-Induced Cytidine Deaminase)** **Activation-induced cytidine deaminase** (AID) is an enzyme expressed only in activated B cells that deaminates cytosine (C) to uracil (U) in transcribed single-stranded DNA; it is the initiating event required in common by somatic hypermutation and class switch recombination.

U in DNA is a mismatch, and different repair pathways handle it with different outcomes. If it is not repaired, U is read as T at replication, giving a C→T (G→A) transition; if it is removed by uracil DNA glycosylase, an abasic site results, which is filled by error-prone polymerases (such as Polη), producing substitutions to all four bases; mismatch repair proteins (MSH2/MSH6) recognize the U:G mismatch and recruit error-prone polymerases to synthesize, also producing mutations at neighboring A:T sites. The expression of AID is tightly controlled (CD40 signaling, Toll-like receptor signaling and others), because its action is risky: deamination outside its targets causes mutations and chromosomal translocations in other genes (such as *MYC*) and is an important cause of B-cell lymphoma (the translocation of *MYC* with IGH in Burkitt lymphoma). People with AID deficiency can undergo neither somatic hypermutation nor class switching, with excess IgM and a lack of the other classes in serum, called hyper-IgM syndrome type 2 ([7.15.31](/7.15.31)).

## 12.6. Class Switch Recombination and Alternative Splicing of Membrane and Secreted Forms

### 12.6.1. Class Switch Recombination

B cells initially express IgM and IgD and during a response can switch to IgG, IgA or IgE, the V region unchanged and only the C region replaced (the division of function of [7.15.9](/7.15.9)). This switching also takes place at the DNA level.

**Definition 12.6.1 (Class Switch Recombination)** The process in activated B cells in which the rearranged V(D)J exon is joined at the DNA level to another, downstream heavy-chain C gene, the DNA in between being deleted, so that the class of the antibody changes while its antigen specificity does not, is called **class switch recombination** (CSR).

Upstream of every heavy-chain C gene except Cδ lies a G-rich repetitive sequence called a switch region (S region: $\mathrm{S_\mu}$, $\mathrm{S_{\gamma}}$, $\mathrm{S_\alpha}$, $\mathrm{S_\varepsilon}$). AID makes multiple nicks in the two transcribed S regions (the donor $\mathrm{S_\mu}$ and the acceptor S region), producing double-strand breaks that are repaired by non-homologous end joining, so that VDJ-Cμ is joined to the new C gene and the intervening DNA is discarded as a circle. Two important properties follow. Switching is irreversible and can proceed only downstream (after IgG one cannot return to IgM, but a switch from IgG1 to the downstream IgE is possible). The direction of switching is determined by cytokines: the promoter upstream of each C gene is transcribed under the action of cytokines, and transcription exposes that S region as a target of AID, so IL-4 induces IgE and IgG4 (in humans), IFN-γ induces IgG1 and IgG3 (in humans), and TGF-β induces IgA ([7.15.20](/7.15.20), [7.15.23](/7.15.23)). CSR also requires CD40 ligand on the T cell to bind CD40 on the B cell, and CD40 ligand deficiency causes X-linked hyper-IgM syndrome ([7.15.31](/7.15.31)).

### 12.6.2. Membrane and Secreted Forms: Alternative Splicing

The same rearranged heavy-chain gene encodes both membrane immunoglobulin (the BCR) and secreted antibody, the difference being a choice in how the mRNA is processed ([7.2.16](/7.2.16)): at the 3′ end of the heavy-chain C region there are two membrane exons (encoding the transmembrane region and the cytoplasmic tail). Alternative polyadenylation and splicing decide the outcome: if cleavage and tailing occur at the secretory site, the secreted mRNA is obtained, whose C terminus is a hydrophilic secretory tail; if this site is bypassed and the membrane exons are spliced on, the membrane mRNA is obtained. Naive B cells express IgM and IgD together, from one long transcript (VDJ-Cμ-Cδ) processed by alternative splicing and polyadenylation, without DNA rearrangement. In plasma cells, the transcription factors (Blimp-1, XBP1) make the secreted form overwhelmingly predominant, and a cell can secrete thousands of antibody molecules per second ([7.15.19](/7.15.19)).

## 12.7. TCR Genes

The structure of the TCR loci is similar to that of Ig, and the rearrangement mechanism is the same (RAG and the 12/23 rule). There are several differences.

- The δ-chain locus is embedded within the α-chain locus: Dδ, Jδ and Cδ lie between the Vα and Jα segments, and some V segments are shared with δ. Once Vα and Jα rearrange, the δ locus in between is deleted and the cell can no longer become a γδ T cell; the choice between the αβ and γδ lineages is related to this.
- The order of rearrangement resembles that of B cells: TCRβ rearranges first (D–J and then V–DJ), forming the pre-TCR (the β chain with the surrogate α chain pTα) and sending a signal, after which the α chain rearranges ([7.15.15](/7.15.15)). TCRβ shows marked allelic exclusion; exclusion of TCRα is not strict, and about 10% of T cells express two α chains.
- The TCR has no somatic hypermutation and no class switching. The affinity of the TCR is selected during thymic development and remains unchanged after maturation. This is an important difference: T cells have no affinity maturation because mutation would generate self-reactive TCRs, and T cells do not have a selection mechanism like that of the germinal center in B cells to eliminate them; what T cells recognize is a peptide presented by MHC, for which "moderate affinity" for antigen is also sufficient.
- The TCR is always membrane-bound and is not secreted.

| | BCR / antibody | TCR |
|---|---|---|
| Loci | IGH, IGK, IGL | TRA/TRD, TRB, TRG |
| Rearrangement | V(D)J, RAG | V(D)J, RAG |
| Combinatorial diversity | About $1.6\times10^6$ | About $2.8\times10^6$ |
| Somatic hypermutation | Yes (AID) | No |
| Class switching | Yes | No |
| Secreted form | Yes (antibody) | No |
| Affinity maturation | Yes | No |
| Recognition | Conformational and linear epitopes of intact antigen | Peptide presented by MHC |

## 12.8. The Immune Repertoire

**Definition 12.8.1 (Immune Repertoire)** The sum of all lymphocyte antigen receptor sequences in an individual (or in a class of cells) is called the **immune repertoire**.

The theoretical diversity (Eq. (12.2), more than $10^{12}$) differs from the actual repertoire, which is limited by cell number. An adult has about $10^{10}$–$10^{11}$ B cells and several times as many T cells, so even if every cell had a different receptor, they would occupy only a small part of the theoretical space. This is the same as the birthday problem of probability theory ([3.1](/3.1)): when $N$ draws are made at random from $M$ possibilities, the expected number of duplicate pairs is approximately

$$
\frac{N(N-1)}{2M} \approx \frac{N^2}{2M}. \tag{12.5}
$$

Take $N = 10^{10}$. If $M = 1.6\times10^6$ (combinatorial diversity only), $3\times10^{13}$ duplicate pairs are expected, with about $6\times10^3$ cells per receptor on average, which amounts to very few specificities; if $M = 10^{13}$, there are only about $5\times10^{6}$ duplicate pairs and the receptors are almost all different (panel B). Junctional diversity is therefore necessary: combinatorial diversity alone cannot give hundreds of millions of cells each its own specificity. In fact, the probabilities of generating the different receptors are not uniform: receptors with short CDR3 and few N nucleotides are produced more easily and recur in different individuals, and are called public clones.

The repertoire can be read out by high-throughput sequencing: the region containing CDR3 is amplified and sequenced, and the sequences are grouped into clonotypes by V gene, J gene and the amino acid sequence of CDR3. Common readouts are the number and frequency distribution of clonotypes (diversity indices), clonal expansion (antigen-specific clones in a response), V-gene usage bias, and somatic mutation trees within a B-cell lineage. Estimates indicate that the number of unique BCR clonotypes in the human body is at least on the order of $10^{9}$ and of TCRβ clonotypes at least $10^{8}$. Sequenced repertoires are widely used in diagnosis (tracking of lymphoma and leukemia clones, vaccine responses, autoimmunity, tumor-infiltrating lymphocytes; [7.15.34](/7.15.34)), and combined with single-cell and spatial omics they can match receptor sequences to the phenotype and position of the cell ([7.9.6](/7.9.6)).

## Summary

| Topic | Key points |
|---|---|
| The problem (§12.1) | The contradiction between one gene, one polypeptide and $10^{11}$ antibodies; the answer is somatic rearrangement; antigen receptors (Definition 12.1.1) |
| Loci (§12.2) | The IGH, IGK, IGL and TCR loci consist of V, (D), J and C segments in tandem, and rearrangement forms the V-region exon |
| Diversity (§12.3) | Combinatorial diversity (Definition 12.3.1, Eq. (12.1), about $1.6\times10^6$ for antibodies) and junctional diversity (Definition 12.3.2), total number Eq. (12.2) |
| Regulation (§12.4) | Allelic and isotypic exclusion (Definition 12.4.1) through feedback from the pre-BCR signal; probability of successful rearrangement about 0.45 (Eq. (12.3)); receptor editing (Definition 12.4.2) |
| Mutation (§12.5) | Somatic hypermutation (Definition 12.5.1) is initiated by AID (Definition 12.5.2); mean number of mutations $\mu L n$ (Eq. (12.4)) |
| Switching and splicing (§12.6) | Class switch recombination (Definition 12.6.1) is irreversible and directed by cytokines; membrane and secreted forms are determined by alternative splicing |
| TCR (§12.7) | Same mechanism, with δ embedded in α; no somatic mutation or class switching |
| Repertoire (§12.8) | The immune repertoire (Definition 12.8.1) is much smaller than the theoretical space; the birthday estimate of Eq. (12.5); readout by sequencing |

## Questions

1. Why is combinatorial diversity alone not enough, so that junctional diversity is indispensable?

   **Answer** Combinatorial diversity gives only about $10^6$ possibilities (Eq. (12.1)), whereas one person has $10^{10}$–$10^{11}$ B cells, so on average each receptor corresponds to about $10^4$ cells and the "resolution" of specificity is inadequate. Junctional diversity adds random sequence at CDR3, increasing the number of possible receptors by several orders of magnitude (Eq. (12.2)), and concentrates it where contact with antigen is closest. The price is that about two thirds of junctions are frameshifted and wasted, but this is an investment in diversity.

2. What is the significance of a B cell expressing only one heavy chain and one light chain? What would happen if it expressed two specificities at once?

   **Answer** Clonal selection requires one cell to have one specificity. If a cell expressed two heavy chains or two light chains, several antibodies would form, and if one of them recognized a self antigen, the whole cell would be eliminated or tolerance would fail; moreover, the two specificities in the same cell would share its T-cell help and proliferative resources, so the response would no longer be specific. Allelic exclusion makes the specificity of each clone unambiguous and ensures that selection and tolerance can operate with the clone as the unit.

3. Use Eq. (12.3) to explain why having two light-chain loci, κ and λ, is advantageous for B-cell development. If there were only a κ locus (two alleles), what would the probability of success be?

   **Answer** The probability that each allele is functional is $1/3$. One light-chain locus (two alleles) has a probability of success of $1 - (2/3)^2 = 5/9 \approx 0.56$, and two loci (four attempts) $65/81 \approx 0.80$, so the second locus raises the success rate of rearrangement from 0.56 to 0.80 and lets more cells complete development; at the same time the λ locus is a reserve after failure or editing of κ and is also the site of receptor editing.

4. Compare patients with AID deficiency and with CD40 ligand deficiency: what do their serum immunoglobulins have in common and how do they differ?

   **Answer** Both show hyper-IgM syndrome: serum IgM is normal or elevated, and IgG, IgA and IgE are very low, because class switching requires CD40–CD40 ligand signaling to induce AID, and AID in turn causes switching. The difference is that AID deficiency makes B cells intrinsically unable to switch and mutate while other immune functions are normal; CD40 ligand deficiency (X-linked) affects not only B cells but also prevents T cells from activating macrophages and dendritic cells, so patients are susceptible to intracellular pathogens (such as *Pneumocystis jirovecii*) and germinal center formation is also defective ([7.15.31](/7.15.31)).

5. (Open question) Why does the TCR have no somatic hypermutation or affinity maturation? Discuss from the standpoint of evolution and risk.

   **Answer** Ideas: (1) T-cell recognition is MHC-restricted, the affinity of the TCR is adjusted in the thymus by positive and negative selection to a moderate range, and peripheral T cells need only reach this threshold; (2) B-cell mutation takes place in germinal centers, where follicular dendritic cells and Tfh cells select each mutant strictly, and the antibody produced is soluble, so the risk of self-reactivity can be controlled by other mechanisms; T cells have no such site of selection in the periphery, mutation would generate self-reactive T cells, and the danger is greater because T cells kill target cells and regulate other cells more powerfully; (3) too high a TCR affinity would also lower the sensitivity of the response, because binding that is too strong would keep the TCR from detaching from the presenting cell, which is unfavorable for serial triggering.
