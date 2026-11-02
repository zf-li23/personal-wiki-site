---
title: Protein Sequence, Structure and Function
description: "Computing with protein structures: predicting local properties from sequence (secondary structure, disorder, transmembrane helices and signal peptides, with a hydropathy analysis of bacteriorhodopsin); the PDB and mmCIF, B factors and resolution, SCOP and CATH; structure comparison by the Kabsch algorithm, RMSD, TM-score and GDT on the two conformations of adenylate kinase, DALI, TM-align and the 3Di alphabet of Foldseek; running AlphaFold in practice and reading pLDDT and PAE (the NGLY1 model); the architecture of AlphaFold 2 and 3; functional annotation, GO transfer and CAFA; docking and virtual screening; design."
---

Structure is where a protein sequence becomes a mechanism, and it is now computable: predicted models exist for nearly every known sequence, and the questions have shifted from "what does this protein look like" to "how far can the model be trusted, what is it a model of, and what does it say about function". This chapter is the computational half of that subject. It treats what can be predicted from sequence alone without a three-dimensional model, how structures are stored and classified, how two structures are compared and searched for, how structure prediction is run and how its confidence estimates should be read, how the AlphaFold architecture works, and how structures are used to annotate function, to dock ligands and to design new proteins. The physics and the theory of prediction were written in biophysics and are not repeated: force fields, molecular dynamics, statistical potentials, templates and fragments, coevolution and the Potts model, the idea of AlphaFold, docking and design are in [7.6.15](/7.6.15), folding itself in [7.6.16](/7.6.16), and the structural chemistry of proteins in [7.1.5](/7.1.5) and [7.1.6](/7.1.6). Sequence alignment and profile models, which supply the alignments that prediction depends on, are in [7.8.3](/7.8.3)–[7.8.5](/7.8.5), and the learned sequence models in [7.8.15](/7.8.15). The running examples are adenylate kinase, a two-state enzyme that shows what a single structure cannot say, and the human N-glycanase NGLY1, whose gene appeared in [7.8.12](/7.8.12) as a rare-disease example.

## 17.1. Predicting Local Properties from Sequence

Before any three-dimensional model, a sequence can be annotated with local properties, and these predictions remain useful: they are fast, they apply to every protein, and they are what pipelines use to decide what a protein is.

### 17.1.1. Secondary Structure

Assigning each residue to helix, strand or coil (the three-state problem, measured by the accuracy $Q_3$) began with the statistical propensities of Chou and Fasman and the information-theoretic GOR method, which reached about $60\,\%$. The step to $70\,\%$ came from neural networks on a window of sequence, and the step to $76$–$80\,\%$ from giving the network a profile instead of a single sequence (PSIPRED, Jones 1999): evolution reveals which positions tolerate substitutions, and that is more informative than the residue types themselves ([7.8.5](/7.8.5)). Current predictors built on protein language models or on predicted structures reach $85$–$88\,\%$, close to the estimated ceiling set by the disagreement between assignment programs on real structures.

### 17.1.2. Disorder

Many regions do not fold on their own ([7.1.6](/7.1.6)). They are recognized by composition — low hydrophobicity, high net charge, an excess of proline, glycine, serine and glutamate — which is what IUPred and its relatives score, and, since 2021, by a low pLDDT in an AlphaFold model, which is one of the best available disorder predictors (17.4).

### 17.1.3. Transmembrane Helices and Signal Peptides

A helix that crosses a bilayer is about $20$ residues long and strongly hydrophobic, so a sliding window of hydropathy finds it.

**Example 17.1.1 (Hydropathy of Bacteriorhodopsin)** We averaged the Kyte–Doolittle hydropathy of bacteriorhodopsin (UniProt P02945, $262$ residues) over a window of $19$ residues. All seven annotated transmembrane helices appear as peaks, and five of them exceed the classical threshold of $1.6$: the maxima are $1.84$, $1.82$, $1.52$, $1.81$, $1.88$, $1.51$ and $2.12$ for helices A to G. The two that fall short, C and F, carry the polar residues of the proton pathway (among them the Schiff-base lysine and the aspartates that accept and donate the proton), and a buried polar residue is exactly what a hydropathy scale cannot distinguish from a residue at the surface. The method also cannot see the orientation of a helix in the membrane.

![Predicting transmembrane helices from sequence: bacteriorhodopsin (UniProt P02945). A: the Kyte–Doolittle hydropathy averaged over a sliding window of 19 residues and plotted at the center of the window; the shaded bands are the seven transmembrane helices annotated in UniProt and the dashed line the classical threshold of 1.6. B: the maximum of the window average inside each annotated helix; helices C and F, which line the proton pathway and carry polar residues, stay below the threshold](./plots/hydropathy.py)

Modern predictors replace the window by a model that also uses the rules of membrane topology: the positive-inside rule (loops on the cytoplasmic side are enriched in arginine and lysine) is a correlation across the whole protein, which a hidden Markov model with states for inside loops, outside loops, helix cores and caps captures naturally (TMHMM; [4.6.8](/4.6.8)), and which DeepTMHMM now learns with a language model. Signal peptides are a related problem — a short hydrophobic stretch at the N terminus followed by a cleavage site — complicated by the fact that signal peptides, signal anchors and transmembrane helices resemble one another; SignalP 6 predicts all the classes at once and gives the cleavage site. Other local predictions in routine use are relative solvent accessibility, which a network predicts to within about $0.15$ of the true fraction, coiled coils, low-complexity and compositionally biased regions ([7.8.4](/7.8.4)), and sites of post-translational modification.

## 17.2. Structures as Data

The **Protein Data Bank** holds the experimentally determined structures ([7.1.6](/7.1.6)), more than $230\,000$ entries, deposited through the worldwide PDB and mirrored by RCSB, PDBe and PDBj. An entry is a list of atoms with coordinates in ångströms, an occupancy and a **temperature factor**, together with the sequence of each chain, the ligands, the crystallographic or cryo-EM metadata and the resolution. The legacy PDB file format, with its fixed columns and its limit of $99\,999$ atoms and single-character chain identifiers, has been replaced for large structures by mmCIF, a tagged format with no such limits; new software should read mmCIF, and the PDB distributes everything in it.

Three fields decide what a coordinate means. The resolution states how much detail the data support: below $1.5$ Å individual atoms and alternative side-chain conformations are visible, around $3$ Å the backbone is reliable and side chains are modeled by expectation, above $4$ Å only the fold is. The B factor measures the spread of an atom's position, from vibration and from disorder across the molecules in the crystal; a side chain with a B factor of $80$ Å² is barely located, and in a cryo-EM structure the same field may hold a sharpening factor instead. The occupancy records that an atom is present in only part of the molecules. Missing residues are the commonest trap: a loop with no density is simply absent from the file, so a chain that should have $300$ residues may contain $280$, and any program that compares two structures must align the residue numbers rather than assume they correspond. For predicted models, the AlphaFold Protein Structure Database stores the per-residue confidence in the B-factor field ([7.8.2](/7.8.2)), which is convenient and a source of confusion.

Structures are classified by fold. SCOP (now SCOP2) is curated by inspection into classes (all α, all β, α/β, α+β and others), folds, superfamilies (probable common ancestry) and families; CATH classifies domains automatically with manual checking into Class, Architecture, Topology and Homologous superfamily; ECOD organizes domains by evolutionary relationship and keeps pace with new structures better than either. The empirical finding behind all of them is that the number of distinct folds is limited, of the order of a thousand to fifteen hundred, and that new folds are now rare ([7.1.5](/7.1.5)). The unit of classification is the domain, not the chain, so the first step in comparing or annotating a structure is usually to cut it into domains, by a parser such as Merizo or SWORD or by the pattern of the predicted aligned error (17.4).

```python
from Bio.PDB import MMCIFParser, PPBuilder                  # Biopython

structure = MMCIFParser(QUIET=True).get_structure("ake", "1ake.cif")
chain = structure[0]["A"]
ca = {r.id[1]: r["CA"].coord for r in chain if "CA" in r}    # residue number -> coordinates
bfac = [a.get_bfactor() for a in chain.get_atoms()]
sequence = str(next(iter(PPBuilder().build_peptides(chain))).get_sequence())
```

```text
# PyMOL: fetch two structures, superpose them and color by the per-atom deviation
fetch 4ake 1ake, async=0
align 4ake and chain A and name CA, 1ake and chain A and name CA
spectrum b, blue_white_red, 4ake
```

## 17.3. Comparing Structures

### 17.3.1. Optimal Superposition

Given a correspondence between the residues of two structures, the first question is how different they are after the best rigid movement of one onto the other.

**Definition 17.3.1 (Root-Mean-Square Deviation)** For two sets of $n$ matched points $\boldsymbol{x}_i, \boldsymbol{y}_i \in \mathbb{R}^3$ (usually the $\mathrm{C}_\alpha$ atoms of matched residues), the **root-mean-square deviation** after a rigid motion is

$$
\operatorname{RMSD} = \min_{R \in \operatorname{SO}(3),\ \boldsymbol{t}}\sqrt{\frac{1}{n}\sum_{i=1}^{n}\lVert R\boldsymbol{x}_i + \boldsymbol{t} - \boldsymbol{y}_i\rVert^2}.
$$

**Theorem 17.3.1 (Kabsch Algorithm)** Let $\bar{\boldsymbol{x}}, \bar{\boldsymbol{y}}$ be the centroids of the two sets and let

$$
H = \sum_{i=1}^{n}(\boldsymbol{x}_i - \bar{\boldsymbol{x}})(\boldsymbol{y}_i - \bar{\boldsymbol{y}})^{\mathsf T} = U\Sigma V^{\mathsf T}
$$
be a **singular value decomposition** ([2.1](/2.1)). Then the minimum is attained at

$$
R = V\operatorname{diag}(1, 1, d)U^{\mathsf T}, \quad d = \operatorname{sgn}\det(VU^{\mathsf T}), \qquad \boldsymbol{t} = \bar{\boldsymbol{y}} - R\bar{\boldsymbol{x}}. \tag{17.1}
$$

**Proof** Write $\boldsymbol{a}_i = \boldsymbol{x}_i - \bar{\boldsymbol{x}}$ and $\boldsymbol{b}_i = \boldsymbol{y}_i - \bar{\boldsymbol{y}}$. For fixed $R$ the sum $\sum_i\lVert R\boldsymbol{x}_i + \boldsymbol{t} - \boldsymbol{y}_i\rVert^2$ is minimized by the translation that matches the centroids, which leaves $\sum_i\lVert R\boldsymbol{a}_i - \boldsymbol{b}_i\rVert^2 = \sum_i(\lVert\boldsymbol{a}_i\rVert^2 + \lVert\boldsymbol{b}_i\rVert^2) - 2\operatorname{tr}(R H)$ with $H = \sum_i\boldsymbol{a}_i\boldsymbol{b}_i^{\mathsf T}$. Minimizing is therefore maximizing $\operatorname{tr}(RH)$. With $H = U\Sigma V^{\mathsf T}$ and the orthogonal matrix $W = V^{\mathsf T}RU$, the invariance of the trace under cyclic permutation gives $\operatorname{tr}(RH) = \operatorname{tr}(RU\Sigma V^{\mathsf T}) = \operatorname{tr}(V^{\mathsf T}RU\Sigma) = \operatorname{tr}(W\Sigma) = \sum_k\sigma_kW_{kk} \le \sum_k\sigma_k$, since the entries of an orthogonal matrix satisfy $\lvert W_{kk}\rvert \le 1$ and the singular values are nonnegative. The bound is attained by $W = I$, that is $R = VU^{\mathsf T}$, which is orthogonal but may have determinant $-1$, a reflection. Restricted to rotations, the largest value of $\sum_k\sigma_kW_{kk}$ with $\det W = \det(VU^{\mathsf T})$ is obtained by flipping the sign of the smallest singular value, which gives Eq. (17.1). $\square$

Two consequences are used constantly. The RMSD is dominated by the worst-fitting parts, because the deviations are squared: a few displaced residues spoil the superposition of the rest. And it has no scale: the same value means different things for a small and a large protein, since unrelated structures of increasing size can be superposed less and less well.

**Example 17.3.1 (Two Conformations of One Enzyme)** Adenylate kinase of *Escherichia coli* was solved in an open form without ligand (PDB 4AKE) and closed on the inhibitor Ap5A (1AKE); $214$ residues are present in both. The global Kabsch superposition gives an RMSD of $7.13$ Å, which would suggest two different structures. Superposing instead on the CORE domain (residues $1$–$29$, $60$–$121$ and $160$–$214$) gives an RMSD of $1.98$ Å over the core while the LID domain ($122$–$159$) moves by up to $23.7$ Å and the NMP-binding domain ($30$–$59$) by up to $17$ Å. Each moving domain, superposed on its own, fits with an RMSD of $0.47$ Å (LID) and $1.58$ Å (NMP): the domains are internally rigid and move as units. The TM-score of the whole molecule is $0.68$ and its GDT_TS is $57$: both say, correctly, that this is the same fold in two conformations. A single number is thus a poor description of a protein with moving parts, and this is the limitation of comparing predicted models with experimental ones as well (17.4).

![Structural superposition of the two conformations of adenylate kinase of *Escherichia coli* (PDB 4AKE open, 1AKE closed; 214 matched Cα atoms). A: the two chains after the global superposition of Theorem 17.3.1, projected on the first two principal axes and colored by domain. B: the distance between matched atoms along the sequence after the global fit and after fitting on the CORE domain only; the shaded bands are the NMP and LID domains. C: the RMSD of the whole chain and of each domain superposed on its own: the domains are rigid and move relative to one another](./plots/superposition.py)

### 17.3.2. Scores That Do Not Depend on Length

**Definition 17.3.2 (TM-Score)** For two structures with $n$ matched residues at distances $d_i$ after a superposition, and a reference length $L$ (that of the target structure),

$$
\operatorname{TM} = \max_{\text{superposition}}\frac{1}{L}\sum_{i=1}^{n}\frac{1}{1 + (d_i/d_0(L))^2}, \qquad d_0(L) = 1.24\sqrt[3]{L - 15} - 1.8\ \text{Å}, \tag{17.2}
$$
a value in $(0, 1]$. The normalization $d_0$ is chosen so that the expected TM-score of two unrelated structures is independent of their length; the maximum is taken by the iterative search of Zhang and Skolnick (2004), which superposes on a fragment, keeps the residues that fall within a cutoff, superposes again and repeats, starting from fragments of several lengths and positions.

Each residue contributes between $0$ and $1$ instead of a squared distance, so distant parts stop mattering instead of dominating, and the sum is divided by the length of the reference, so an unmatched region counts as zero. Empirically, pairs with $\operatorname{TM} > 0.5$ almost always have the same fold in SCOP or CATH and pairs below $0.3$ are unrelated (Xu and Zhang, 2010); the region between is the twilight zone of structure comparison, the analogue of the twilight zone of sequence identity ([7.8.3](/7.8.3)).

**Example 17.3.2** We generated self-avoiding chains of $\mathrm{C}_\alpha$ atoms with protein-like bond geometry, confined to a sphere of the radius of gyration expected for a globular protein of that length, and superposed unrelated pairs optimally. The RMSD of the best superposition grows from $8.6 \pm 0.9$ Å at $50$ residues to $23.5 \pm 1.5$ Å at $400$ residues, following the size of the molecule, while the TM-score stays at $0.19$ to $0.21$ at every length. A threshold of "RMSD below $4$ Å" is therefore strict for a domain of $50$ residues and generous for one of $400$, whereas the TM-score threshold of $0.5$ means the same thing throughout. The global distance test used in CASP, $\mathrm{GDT\_TS}$, achieves the same end differently: it averages the percentages of residues that can be superposed within $1$, $2$, $4$ and $8$ Å.

![Why the RMSD must be normalized. Self-avoiding Cα chains with protein-like bond geometry, confined to the radius of gyration expected for a globular protein, 15 unrelated pairs per length, superposed by the Kabsch algorithm. A: the RMSD of the best superposition of two unrelated chains grows with their length, roughly as the radius of gyration. B: the TM-score of the same pairs is about 0.2 at every length, which is what the normalization by d₀(L) is designed to achieve; the dashed line is the usual threshold of 0.5 for sharing a fold](./plots/tm-vs-rmsd.py)

### 17.3.3. Searching Without a Correspondence

Comparing two structures requires a correspondence between residues, which for homologs of different lengths must be found as part of the comparison. The methods differ in what they optimize. TM-align alternates a dynamic-programming alignment scored by the TM-score terms with a superposition, until the alignment stops changing. DALI compares intramolecular distance matrices, so no superposition is needed at all and the method tolerates domain motions and permutations: it maximizes a similarity between the matrices by Monte Carlo over alignments. CE and FATCAT build an alignment from fragment pairs, FATCAT allowing a limited number of hinges, which is how the two forms of adenylate kinase are recognized as the same structure in one alignment.

Searching a database of hundreds of millions of predicted structures with any of these is too slow. Foldseek (van Kempen and colleagues, 2024) makes the problem a sequence problem: each residue is described by the identity of its closest neighbor in space and the local geometry of the two backbones, and this description is quantized into an alphabet of $20$ structural states (the 3Di alphabet) learned by a small network. A structure becomes a string over this alphabet, a substitution matrix for the states is derived as for amino acids ([7.8.3](/7.8.3)), and the search uses the $k$-mer prefilter, gapless extension and Smith–Waterman alignment of MMseqs2 ([7.8.4](/7.8.4)), with E-values computed in the same way. The result is structure search thousands of times faster than TM-align at comparable sensitivity, which is what made all-against-all comparison of the AlphaFold database possible and turned structure comparison into a routine step of annotation: when a sequence search finds no homolog, predict the structure and search with Foldseek ([7.8.5](/7.8.5#sec-5.7)).

```bash
foldseek easy-search query.pdb afdb_proteome/ hits.tsv tmp --format-output \
    "query,target,fident,alntmscore,evalue,prob"
USalign -mm 0 model.pdb native.pdb          # TM-score of a model against an experimental structure
```

## 17.4. Running a Prediction and Reading Its Confidence

The theory of structure prediction is in [7.6.15](/7.6.15#sec-15.5); what matters here is practice. Four routes are in use. The AlphaFold Protein Structure Database already contains a model for almost every UniProt sequence, and should be checked first. ColabFold (Mirdita and colleagues, 2022) runs **AlphaFold** with alignments built by MMseqs2 against clustered environmental and reference databases, which is what makes it fast enough for a notebook; this is the usual route for a protein not in the database, for a mutant or for a complex. The AlphaFold 3 server and the open reimplementations (Boltz, Chai) predict complexes with nucleic acids, ligands, ions and modified residues. ESMFold predicts from a single sequence with a protein language model ([7.8.15](/7.8.15#sec-15.4.1)), less accurately but fast enough for whole metagenomes.

The alignment is the main variable the user controls. Accuracy rises with the number of effective sequences in the alignment and falls off below roughly $30$ to $100$ of them; for an orphan protein, searching metagenomic databases often supplies them. For complexes, the chains' alignments must be *paired*, so that sequences from the same species or operon are placed in the same row, which is how the network sees coevolution between the chains rather than within them.

**Definition 17.4.1 (Per-Residue Confidence)** The **predicted local distance difference test** ([7.6.15](/7.6.15)) is a per-residue confidence score in $[0, 100]$ that estimates the lDDT-Cα score of the model at that residue, that is, the fraction of distances to nearby atoms (within $15$ Å) that the model reproduces to within a tolerance. It is produced by the network itself, not by comparison with a structure. Conventional bands are above $90$ (the backbone and most side chains are reliable), $70$ to $90$ (the backbone is reliable), $50$ to $70$ (low confidence) and below $50$ (the region should not be interpreted as a structure, and is often intrinsically disordered).

**Definition 17.4.2 (Predicted Aligned Error)** The *predicted aligned error* is a matrix $\mathrm{PAE}_{ij}$, in ångströms, estimating the error in the position of residue $j$ when the predicted and true structures are superposed on residue $i$. Low values within a block of residues and high values between blocks mean that each block is predicted confidently but their relative placement is not; for complexes, the inter-chain block is the evidence that the interface is predicted, summarized as the interface predicted TM-score (ipTM).

The two measures answer different questions, and both are needed. A model can have high pLDDT everywhere and a large PAE between two domains, which is the normal situation for a multidomain protein with a flexible linker; conversely a low-pLDDT region may be genuinely disordered rather than badly predicted.

**Example 17.4.1 (The Model of NGLY1)** The AlphaFold model of human NGLY1 (UniProt Q96IV0, $654$ residues), the N-glycanase whose loss causes a congenital disorder of deglycosylation, has a mean pLDDT of $85.5$: $68\,\%$ of residues are above $90$ and $12\,\%$ below $50$. The confidence follows the annotation of the protein. The PUB domain (residues $30$–$91$, which binds p97) averages $91$, the transglutaminase-like catalytic core $92$, with the three residues of the catalytic triad (Cys309, His336, Asp353) at $88$, $94$ and $95$, and the C-terminal PAW domain, which binds the glycan, $88$. The two low regions are the segment $112$–$163$, which UniProt annotates as disordered (mean pLDDT $42$), and the linker before the PAW domain around residues $455$–$480$. The model is therefore trustworthy where a mechanism would be read from it, and the regions it cannot place are regions that have no single structure. What such a model does not give is the effect of the patient mutations: predicting that a substitution destabilizes a protein, or changes the equilibrium between two states, is a different problem from predicting the fold ([7.8.15](/7.8.15#sec-15.5)).

![Per-residue confidence of an AlphaFold model: human NGLY1 (UniProt Q96IV0, 654 residues, AlphaFold DB model, data under CC BY 4.0). A: pLDDT along the sequence with the conventional confidence bands, the UniProt annotations of the PUB and PAW domains and of the disordered region 112–163, and the three residues of the catalytic triad. B: the fraction of residues above each pLDDT value. C: the mean pLDDT of the annotated segments; only the disordered region falls into the low-confidence range](./plots/plddt.py)

Four failure modes are worth remembering, because the confidence scores do not report them. A model is a single structure, usually the state most represented in the PDB, so a protein like the adenylate kinase of Example 17.3.1 is predicted in one of its conformations and the other is missing. A point mutation usually changes the model very little, even when it abolishes function, because the network predicts the family's fold rather than the energetics of the variant. Designed sequences without natural homologs, and fast-evolving viral proteins with shallow alignments, are predicted less reliably. And a confident model of a complex is evidence of an interface, not of an interaction that occurs in a cell at a relevant concentration and time ([7.9.10](/7.9.10)).

```bash
colabfold_batch --num-recycle 3 --amber seqs.fasta out/     # MSA by MMseqs2, then AlphaFold2
colabfold_batch --templates --msa-mode mmseqs2_uniref_env complex.fasta out/   # chains separated by ":"
```

## 17.5. Inside AlphaFold

The architecture repays study, because each part encodes an idea about proteins. [7.6.15](/7.6.15#sec-15.5.5) describes it as a whole; here are the components that are specific enough to state precisely.

*Two representations.* AlphaFold 2 keeps an MSA representation, one vector per sequence and residue, and a pair representation, one vector per ordered pair of residues, which plays the role of a distance map. The $48$ blocks of the Evoformer update both and let them exchange information: row attention over the MSA (within a sequence, biased by the pair representation), column attention (across sequences at one position, which is where **coevolution** enters), and an outer product of the MSA columns that writes the coevolutionary signal into the pair representation.

*Triangle updates.* Distances are not free: for any three residues $d_{ik} \le d_{ij} + d_{jk}$. The network enforces consistency by updating the pair $(i, k)$ from all paths through a third residue $j$, with multiplicative updates ("outgoing" and "incoming") and attention around triangles,

$$
\boldsymbol{z}_{ik} \leftarrow \boldsymbol{z}_{ik} + g_{ik} \odot \sum_{j}a_{ij} \odot b_{jk},
$$
a learned analogue of composing two edges into a third. This is the step that turns a set of predicted pairwise relations into something that can be realized in three dimensions.

*Frames and invariance.* The structure module gives every residue a local coordinate frame, a rotation and a translation derived from its N, $\mathrm{C}_\alpha$ and C atoms, and updates the frames by invariant point attention, in which points produced in one residue's frame are compared in another's. Because all geometric quantities are computed between frames, the output transforms correctly under a global rotation or translation of the whole structure: the network is equivariant by construction rather than by training on rotated copies.

*The loss.* Frame-aligned point error compares a predicted atom position with the true one after superposing the two structures on each residue's frame in turn, and averages over all pairs of residue and atom (clamped at $10$ Å):

$$
\mathcal{L}_{\mathrm{FAPE}} = \frac{1}{N_{\mathrm{frames}}N_{\mathrm{atoms}}}\sum_{i}\sum_{a}\min\left(d_{\max},\ \bigl\lVert T_i^{-1}\boldsymbol{x}_a - \hat{T}_i^{-1}\hat{\boldsymbol{x}}_a\bigr\rVert\right).
$$
Like the TM-score and unlike the RMSD, it is a sum of locally evaluated errors rather than one global superposition, so a correctly folded domain in the wrong place is not penalized as if every atom were wrong — and, being computed in local frames, it distinguishes a structure from its mirror image.

*Recycling and self-assessment.* The output is fed back into the input three times, which lets the network refine its own prediction, and separate heads predict pLDDT and the PAE, trained against the errors the model actually makes.

AlphaFold 3 (2024) replaces the structure module with a diffusion model that generates atom coordinates from noise, conditioned on the trunk, and represents everything at the atom level, so proteins, nucleic acids, ions, ligands and modified residues are handled by one model; the MSA stack is reduced. The cost is that a generative model can produce plausible but unsupported structure in disordered regions, which is countered by a confidence head and by generating several samples. The open reimplementations, trained on the public PDB, make the architecture available without the restrictions of the server.

## 17.6. From Structure to Function

**Definition 17.6.1 (Functional Annotation)** *Functional annotation* is the assignment to a gene or protein of terms describing what it does, usually from the **Gene Ontology** ([7.8.2](/7.8.2)): molecular function, biological process and cellular component, with an evidence code recording whether the assignment comes from experiment, from an author statement or from computation.

Most annotations are transferred from homologs, by sequence ([7.8.4](/7.8.4)) or by domain signatures: InterProScan runs the member databases of InterPro — Pfam profile HMMs ([7.8.5](/7.8.5)), PROSITE patterns and profiles, CDD, SMART, PANTHER families — and reports the domains, their boundaries and the GO terms attached to them, which is the standard first annotation of a new proteome ([7.8.11](/7.8.11)). Transfer by homology has two systematic errors: an annotation may be propagated from a protein that was itself annotated by transfer, so that an error multiplies through the databases, and the function may genuinely differ, as enzymes of one family often act on different substrates and a change of one residue in an active site is enough. Identity thresholds are therefore not a guarantee, and the most specific GO terms should be transferred only from close orthologs ([7.8.6](/7.8.6)).

Structure adds information where sequence has none. Two proteins may have the same fold below $20\,\%$ identity, so a Foldseek or DALI search finds relationships that no sequence search can (17.3.3), and local comparison can match an active site, a few residues in a particular geometry, independently of the fold: the catalytic triad of serine proteases is recognized by searching for its spatial arrangement, and the Catalytic Site Atlas and the MCSA collect such templates. Pockets are found geometrically (fpocket) or by learned models, and their size, shape and electrostatics predict what can bind. Still, structure is not function: an orphan fold with a deep pocket says that something binds, not what.

The field measures itself in CAFA, a community experiment in which predictors annotate proteins whose experimental annotations are expected but not yet published, and are scored when the annotations appear, by an F-measure over the ontology that accounts for its hierarchy. Three findings have been stable across rounds: methods combining several sources of evidence beat any single source; a naive baseline that assigns the most frequent terms of the species is surprisingly hard to beat, because the ontology is unbalanced; and molecular function is predicted far better than biological process, which depends on context rather than on the molecule.

Predicted structures have been used at proteome scale for exactly these tasks: clustering the AlphaFold database with Foldseek found tens of thousands of structural clusters with no annotation, some of them new folds; structure-based searches have assigned families to proteins that sequence searches left as "hypothetical"; and comparisons across species have identified remote homologs of disease genes in model organisms.

## 17.7. Docking and Virtual Screening

**Molecular docking** predicts the pose and affinity of a small molecule in a protein's binding site, and **virtual screening** applies it to a library of compounds to choose which ones to test; both are treated physically in [7.6.15](/7.6.15#sec-15.7). The computational points are these. A docking program separates a search over poses (position, orientation and the ligand's rotatable bonds, sometimes a few side chains) from a scoring function, usually an empirical sum of terms for steric fit, hydrogen bonds, hydrophobic contact and torsional entropy, fitted to measured affinities (AutoDock Vina, Glide, Gold). Scoring functions rank poses much better than they rank compounds: the standard measures of success are therefore the fraction of ligands redocked within $2$ Å of the crystal pose, and, for screening, the enrichment factor, the fraction of known actives found in the top $1\,\%$ of a ranked library divided by $0.01$. Benchmarks must be built carefully: the decoys in a screening benchmark should resemble the actives in physical properties but differ in structure, since otherwise a program can "succeed" by learning molecular weight (the lesson of the DUD and DUD-E sets). Libraries of $10^9$ or more purchasable compounds are now screened by distributing the docking or by training a cheap learned model on a docked subset and using it to triage the rest; deep-learning docking (DiffDock and relatives) predicts poses directly and is fast, though its advantage shrinks on proteins unlike those in its training set, the familiar leakage problem ([7.8.15](/7.8.15#sec-15.6.1)).

Protein–protein docking is the same problem with a much larger search space, now largely replaced for proteins with homologs by the complex prediction of 17.4, with the PAE of the interface as the criterion. What prediction has not replaced is affinity: neither docking scores nor model confidences are free energies, and quantitative affinities still need the free-energy calculations of [7.6.15](/7.6.15#sec-15.3.3) or experiment.

## 17.8. Design

**Protein design** inverts the prediction problem: given a structure or a function, find sequences that realize it ([7.6.15](/7.6.15#sec-15.8)). Computationally the pipeline now has three learned stages. A backbone is generated, either taken from nature or produced by a generative model (RFdiffusion and relatives) conditioned on a motif, a binding partner or a symmetry. A sequence is designed for that backbone by an inverse-folding model (ProteinMPNN), a network that predicts amino acids from the geometry of the backbone and that raised the experimental success rate of design substantially over physics-based packing. The designs are then filtered in silico by predicting their structures and keeping those whose prediction matches the intended backbone with high confidence — a self-consistency check that uses AlphaFold or ESMFold as a cheap surrogate for the experiment, and whose main weakness is that the same models were trained on natural proteins and are over-confident about designed sequences. What is then tested in the laboratory is a few tens to a few hundred designs per target; the honest measure of a design method is the fraction of them that fold and work, not the computed score.

The same tools serve analysis: inverse-folding likelihoods score natural sequences for their compatibility with a structure, generative models produce libraries for directed evolution, and designed binders are being used as reagents and candidate therapeutics. The boundary with chemistry — delivery, stability, immunogenicity — is where most designs still fail.

## Summary

| Topic | Key points |
|---|---|
| Local prediction | secondary structure $Q_3$ from $60\,\%$ (propensities) to $76$–$80\,\%$ (profiles, PSIPRED) and $85\,\%$+ (language models); disorder from composition or low pLDDT; hydropathy windows find five of seven helices of bacteriorhodopsin (Example 17.1.1), HMM topology models and SignalP do better |
| Structure data | PDB and mmCIF; resolution, B factors, occupancy, missing residues; pLDDT stored in the B-factor field of predicted models; SCOP, CATH, ECOD classify domains; about $10^3$ folds |
| Superposition | RMSD (Definition 17.3.1) minimized by the Kabsch algorithm through an SVD (Theorem 17.3.1); dominated by the worst parts and dependent on size |
| Adenylate kinase | global RMSD $7.13$ Å but $1.98$ Å on the CORE with the LID displaced by up to $23.7$ Å; each domain fits itself to $0.5$–$1.6$ Å; TM-score $0.68$, GDT_TS $57$ (Example 17.3.1) |
| Length-independent scores | TM-score with $d_0(L) = 1.24\sqrt[3]{L-15} - 1.8$ (Definition 17.3.2); unrelated chains score about $0.2$ at every length while their RMSD grows from $8.6$ to $23.5$ Å (Example 17.3.2); $0.5$ means the same fold; GDT_TS averages $1$, $2$, $4$, $8$ Å |
| Searching | TM-align, DALI (distance matrices, tolerates motion), FATCAT (hinges); Foldseek turns a structure into a string over a 3Di alphabet and reuses sequence search |
| Prediction in practice | AlphaFold DB, ColabFold, AlphaFold 3 and open reimplementations, ESMFold; alignment depth and chain pairing are what the user controls |
| Confidence | pLDDT per residue (Definition 17.4.1) and PAE per pair (Definition 17.4.2); NGLY1: mean $85.5$, domains $88$–$92$, annotated disordered region $42$ (Example 17.4.1); single conformation, mutations, designed and orphan sequences are the failure modes |
| Architecture | MSA and pair representations, row and column attention, triangle updates for geometric consistency, frames and invariant point attention, FAPE loss, recycling; AlphaFold 3 diffuses atoms |
| Function | GO transfer with evidence codes (Definition 17.6.1), InterProScan; error propagation and substrate change; structure and active-site templates where sequence fails; CAFA findings |
| Docking and design | pose search plus empirical scoring; redocking within $2$ Å and enrichment factors; property-matched decoys; generation, inverse folding (ProteinMPNN) and self-consistency filtering, with experimental success as the measure |

## Questions

1. Why does the Kabsch algorithm need the correction $\operatorname{diag}(1, 1, d)$ in Eq. (17.1), and what would be wrong with the superposition without it?

   **Answer** Maximizing $\operatorname{tr}(RH)$ over all orthogonal matrices gives $R = VU^{\mathsf T}$, which has determinant $\pm1$. If the determinant is $-1$, $R$ is a rotation combined with a reflection, and applying it to a protein produces its mirror image: all $\mathrm{C}_\alpha$ distances are preserved but the chirality is inverted, so right-handed α helices become left-handed. Such a superposition can fit better numerically than any proper rotation, and the reported RMSD would be meaningless. Restricting to $\det R = +1$ costs the smallest singular value, which is why the sign is flipped in the third column.

2. A model of a domain of $200$ residues has $60\,\%$ of its residues within $1$ Å of the native structure and the rest, a misplaced loop, at $15$ Å. Compute the RMSD and the TM-score and say which describes the model better.

   **Answer** $\operatorname{RMSD} = \sqrt{0.6 \times 1^2 + 0.4 \times 15^2} = 9.5$ Å, a value typical of two unrelated structures. With $d_0(200) = 1.24\sqrt[3]{185} - 1.8 = 5.27$ Å, the TM-score is $0.6/(1 + (1/5.27)^2) + 0.4/(1 + (15/5.27)^2) = 0.59 + 0.04 = 0.62$, which correctly says that the fold is right and part of the model is not. The RMSD is dominated by the squared large deviations; the TM-score saturates them. For a model one should report both, or the RMSD over the well-fitting core together with the fraction of residues it covers.

3. Explain why the expected TM-score of unrelated structures is roughly independent of length while the expected RMSD is not, and why $d_0$ grows as the cube root of $L$.

   **Answer** Two unrelated compact structures of $L$ residues occupy a volume proportional to $L$, so their linear size, and hence the typical distance between arbitrarily matched residues, grows as $L^{1/3}$; the RMSD follows that growth, as the simulation of Example 17.3.2 shows. The TM-score measures each distance in units of $d_0(L)$, so if $d_0$ grows as $L^{1/3}$ the typical ratio $d_i/d_0$ stays constant, every term keeps the same expected value and the average over residues does not change with $L$. The constants $1.24$ and $-1.8$ were fitted so that the mean score of random pairs is about $0.17$ at all lengths.

4. The AlphaFold model of a two-domain protein has pLDDT above $90$ throughout and a PAE of $25$ Å between the domains. What can be concluded, and what experiment or analysis would resolve the ambiguity?

   **Answer** Each domain is predicted reliably, including its side chains, but their relative position and orientation are not: the model shows one arrangement out of many, and distances between residues of different domains must not be interpreted, which rules out, for example, reading a composite active site or modeling a FRET pair from it. The PAE matrix also defines the domain boundaries, which is how automatic parsers use it. To resolve the arrangement, use data that report on it: small-angle X-ray scattering for the overall shape, crosslinking mass spectrometry or FRET for specific distances, cryo-EM if the complex is large enough, or NMR residual dipolar couplings; or ask whether a single arrangement exists at all, since a flexible linker means an ensemble, which is better described by a distribution than by one model.

5. Two proteins share $18\,\%$ sequence identity, and TM-align gives a TM-score of $0.72$ over $150$ aligned residues. What does each number mean, and what follows about their relationship?

   **Answer** Eighteen percent identity is inside the twilight zone, where sequence alignment alone cannot distinguish homology from chance ([7.8.3](/7.8.3)); a TM-score of $0.72$ is well above $0.5$ and means the same fold, which is strong evidence of a relationship, since fold is conserved far longer than sequence. The two are therefore probably homologous, though convergence to a common fold cannot be excluded for simple architectures (for example small all-α bundles or TIM barrels, which arise repeatedly). Supporting evidence would be shared function or substrate, conservation of the active-site residues in the structural alignment, matching domain architectures, and detection by a profile–profile comparison such as HHpred ([7.8.5](/7.8.5)).

6. Why does Foldseek encode local structural environments as letters of a $20$-state alphabet rather than comparing coordinates, and what does it give up?

   **Answer** Reducing each residue to a letter turns structure comparison into string comparison, so decades of sequence-search machinery apply: $k$-mer prefilters, substitution matrices, gapless prefiltering, Smith–Waterman alignment and Karlin–Altschul E-values ([7.8.4](/7.8.4)), with a cost per comparison thousands of times lower than an iterative superposition, which is what makes searching hundreds of millions of predicted structures feasible. What is given up is precision: the alphabet describes each residue by its nearest neighbor in space and the local backbone geometry, so fine differences within a state are lost, and the resulting alignment is approximate — Foldseek therefore reports a structural alignment that is normally refined and rescored (for example by TM-align) for the hits that matter. Long-range topology enters only through the chain of states, so permutations and large motions are handled less well than by DALI.

7. A pipeline annotates a new bacterial proteome by transferring GO terms from the best BLAST hit above $40\,\%$ identity. Name three errors this will produce and how to reduce them.

   **Answer** (a) Transfer from a paralog rather than an ortholog gives the wrong specific function, since paralogs often diverge in substrate; use orthology assignment ([7.8.6](/7.8.6)) or require reciprocal best hits, and prefer terms shared by several orthologs. (b) Propagation of annotations that were themselves computational multiplies errors through the databases; filter by GO evidence code, keeping experimental ones. (c) Multidomain proteins get the whole annotation of a hit that matches only one domain; annotate per domain with InterProScan and require the alignment to cover the domain. Two further safeguards: transfer general terms when the evidence is weak rather than specific ones, since the ontology is hierarchical, and check the conservation of catalytic and binding residues in the alignment before transferring an enzymatic activity.

8. In a virtual screening benchmark a program recovers $20$ of $100$ known actives in the top $1\,\%$ of a library of $50\,000$ compounds. Compute the enrichment factor, and state the two controls needed before believing it.

   **Answer** The top $1\,\%$ is $500$ compounds; by chance it would contain $100 \times 0.01 = 1$ active, so the enrichment factor at $1\,\%$ is $20/1 = 20$. First control: the decoys must match the actives in molecular weight, charge, logP and the number of rotatable bonds while being structurally dissimilar, otherwise the program may be ranking by physical properties; a property-matched set (as in DUD-E) and a check that a trivial score, such as molecular weight alone, does not reproduce the enrichment. Second: the actives must not be near-duplicates of each other or of compounds used to parameterize or train the method, since a few scaffolds repeated many times inflate the count; cluster the actives by chemical similarity and count scaffolds found, not molecules. Beyond the benchmark, what matters is the experimental hit rate of the compounds actually bought and tested.

9. (Design) A patient has a rare missense variant in NGLY1, and the AlphaFold model of the protein is available. Describe how you would use structure and sequence to build an argument about whether the variant is damaging, and what the argument cannot establish.

   **Answer** Place the residue in the model and record its environment: is it in the catalytic triad or the glycan-binding PAW domain, buried or exposed, in a region with high pLDDT? Burial and proximity to the active site raise the prior. Compute conservation from a deep alignment of orthologs and the family ([7.8.5](/7.8.5)) and the zero-shot score of a protein language model and of a family model such as EVE or AlphaMissense ([7.8.15](/7.8.15#sec-15.5)); check the frequency of the variant in gnomAD and the classification of nearby variants in ClinVar ([7.8.12](/7.8.12#sec-12.8)). Estimate the effect on stability with a predictor or a free-energy calculation ([7.6.15](/7.6.15#sec-15.3.3)), remembering that these are unreliable for large changes. Assemble the evidence in the ACMG/AMP framework, where computational evidence is supporting and the strong evidence is segregation in the family, the match of the patient's phenotype to the known disorder, and a functional assay of deglycosylation activity. The computation cannot establish pathogenicity: it cannot predict the quantitative loss of activity, the effect on expression or on interaction with p97, or whether a partially active enzyme suffices in the relevant tissue.

10. (Open) Predicted structures now exist for almost every protein sequence. Which questions in this chapter does that solve, and which does it leave untouched?

    **Answer** It largely solves the problem of recognizing distant homology, since structure is conserved longer than sequence and Foldseek makes structural search as cheap as sequence search; of assigning domains, since predicted models with their PAE matrices define boundaries; of giving a starting model for crystallographic phasing and for fitting into cryo-EM maps; and of making structure-based function transfer available for the whole proteome rather than for the few percent with experimental structures. It leaves untouched everything that depends on which state a protein is in and on energetics: conformational ensembles and allostery, the effect of mutations on stability and activity, binding affinities, the dependence of structure on partners, ions, modifications and membrane environment, and function in the sense of what the protein does in a cell rather than what it looks like. It also creates a problem of its own: a database of $2\times10^8$ confident models invites the assumption that a structure is known when what is known is a plausible model of one state, and the distinction between a prediction and a measurement has to be preserved in the databases, in the figures and in the reasoning built on them.
