---
title: RNA Sequence and Structure Analysis
description: "Computing with RNA: families of noncoding RNAs and Rfam; dot-bracket notation, arc diagrams and pseudoknots; the Zuker recursions on loop energies and their implementation, with a numpy folding of tRNA-Phe; the partition function, base-pair probabilities and maximum expected accuracy; chemical probing (SHAPE) as pseudo-energies; stochastic context-free grammars, CYK and covariance models (Infernal); comparative folding, compensatory mutations and R-scape, with the covariation of the Rfam tRNA alignment; RNA–RNA interaction and microRNA target prediction on the let-7 sites of HMGA2; deep-learning structure predictors and their generalization problem."
---

RNA is the one class of biological sequence whose three-dimensional behavior can be predicted, in part, from the sequence alone and in polynomial time. The reason is that most of the folding free energy comes from base pairs stacked on one another, and that the pairs of a secondary structure, if crossing pairs are excluded, nest like parentheses: the structure decomposes into independent subproblems and **dynamic programming** applies ([4.3.1](/4.3.1)). This chapter treats the computations: how a structure is written down, the recursions of *Zuker's algorithm* and what their tables mean, the partition function and base-pair probabilities, how chemical probing data are added as constraints, the grammar view that leads to covariance models and the search of sequence databases for members of an RNA family, how covariation in an alignment reveals the structure, and how RNA–RNA interactions, among them microRNA targeting, are predicted. The physics is in biophysics and is not repeated: the nearest-neighbor model, the Nussinov and McCaskill recursions in their simplest form, kinetics and tertiary structure are in [7.6.15](/7.6.15#sec-15.6) and [7.6.16](/7.6.16#sec-16.7), and the chemistry of the bases in [7.1.11](/7.1.11). Profile hidden Markov models, of which covariance models are the grammatical analogue, are in [7.8.5](/7.8.5), and the noncoding RNAs themselves in [7.2](/7.2). The running example is yeast tRNA-Phe, the first RNA whose structure was solved and still the best test of a folding program.

## 16.1. Representing a Structure

A **noncoding RNA** is specified at three levels: its sequence, its secondary structure (the set of base pairs) and its tertiary structure (the arrangement in space). The secondary structure is the useful intermediate: it carries most of the free energy, it is conserved in evolution over longer times than the sequence, and it can be computed.

**Definition 16.1.1 (Secondary Structure and Dot-Bracket Notation)** A secondary structure of a sequence $x_1\cdots x_n$ is a set $S$ of pairs $(i, j)$ with $i + 4 \le j$, each nucleotide in at most one pair, and no two pairs crossing: if $(i, j), (k, l) \in S$ with $i < k < j$ then $k < l < j$. Pairs are Watson–Crick (A–U, G–C) or **wobble** (G–U). In **dot-bracket notation** the structure is written as a string with an opening parenthesis at the $5'$ partner of each pair, a closing parenthesis at its $3'$ partner and a dot at every unpaired nucleotide. A set of pairs that includes two crossing pairs is a **pseudoknot**, which this notation cannot express and which the algorithms below exclude.

The minimum distance $j - i \ge 4$ expresses that a hairpin loop needs at least three nucleotides. Three displays are common: the dot-bracket string, the arc diagram (the sequence on a line and each pair as an arc above it, in which crossing arcs are exactly pseudoknots) and the conventional cloverleaf or planar drawing. Pseudoknots are real — they occur in **telomerase** RNA, in **riboswitches** and in the frameshifting signals of viruses — and predicting the best structure with arbitrary pseudoknots is NP-hard (Lyngsø and Pedersen, 2000), while restricted classes can be found in $O(n^5)$ or $O(n^6)$ time (Rivas and Eddy, 1999). Programs for the general problem therefore predict a pseudoknot-free structure and add pseudoknots heuristically afterwards.

A structure is decomposed into *loops*, and the energy model assigns a free energy to each loop rather than to each pair. A pair $(i, j)$ closes a loop whose other boundaries are the pairs immediately inside it: none (a hairpin loop), one (a stacked pair if adjacent, otherwise a bulge or an interior loop) or two or more (a multiloop). The free energies of these loops, measured by optical melting of short oligonucleotides, are the nearest-neighbor parameters of [7.6.15](/7.6.15#sec-15.6.1) (the Turner 1999 and 2004 sets, extended since with measurements of special hairpins, dangling ends and coaxial stacking).

## 16.2. Minimum Free Energy Folding

### 16.2.1. The Zuker Recursions

Nussinov's algorithm maximizes the number of pairs with one table ([7.6.15](/7.6.15#sec-15.6.2)). A loop-based energy model needs several, because the energy of a pair depends on what is inside it.

**Algorithm 16.2.1 (Zuker)** Let $V(i, j)$ be the minimum free energy of the subsequence $x_i\cdots x_j$ *given that $(i, j)$ is a pair*, $WM(i, j)$ the minimum energy of $x_i \cdots x_j$ as part of a multiloop containing at least one branch, $WM1(i, j)$ the same with exactly one branch that starts at $i$, and $W(j)$ the minimum energy of the prefix $x_1\cdots x_j$. With hairpin energies $H$, interior-loop energies $I$ (which include stacks and bulges) and multiloop parameters $a$ (closing), $b$ (per branch) and $c$ (per unpaired nucleotide),

$$
\begin{aligned}
V(i, j) &= \min\Bigl\{H(i, j),\ \min_{i<k<l<j}\bigl[I(i, j, k, l) + V(k, l)\bigr],\ \min_{i<u<j}\bigl[a + b + WM(i+1, u-1) + WM1(u, j-1)\bigr]\Bigr\},\\
WM1(i, j) &= \min_{l}\bigl[V(i, l) + b + c\,(j - l)\bigr],\\
WM(i, j) &= \min_{u}\min\bigl\{c\,(u - i) + WM1(u, j),\ WM(i, u-1) + WM1(u, j)\bigr\},\\
W(j) &= \min\Bigl\{W(j-1),\ \min_{i<j}\bigl[W(i-1) + V(i, j)\bigr]\Bigr\},
\end{aligned} \tag{16.1}
$$
computed for increasing $j - i$, with $V = \infty$ when $(i, j)$ cannot pair. The minimum free energy of the whole sequence is $W(n)$, and the structure is recovered by tracing back which alternative achieved each minimum.

**Theorem 16.2.1 (Complexity)** The recursions of Algorithm 16.2.1 are computed in $O(n^4)$ time and $O(n^2)$ memory; restricting interior loops to at most $L$ unpaired nucleotides, as all implementations do with $L = 30$, reduces the time to $O(n^2L^2) = O(n^2)$ for fixed $L$, and the multiloop and exterior cases cost $O(n^3)$ in total, so the running time is $O(n^3)$.

**Proof** There are $O(n^2)$ entries in each table. The interior-loop case of $V$ examines all pairs $(k, l)$ inside $(i, j)$, which is $O(n^2)$ per entry and $O(n^4)$ in total; with at most $L$ unpaired nucleotides on the two sides there are $O(L^2)$ candidates per entry. The multiloop case of $V$, and both cases of $WM$, $WM1$ and $W$, split the interval at one position, which is $O(n)$ per entry and $O(n^3)$ in all. Each table has $O(n^2)$ entries, which is the memory. $\square$

Every structure must be generated by exactly one path through the recursions, or minimization would still be correct but the partition function of 16.2.3 would count structures more than once; this is why $WM1$ fixes the first branch of a multiloop and why the exterior case of $W$ is written with the last branch. Implementations add refinements that matter in practice: dangling ends and terminal mismatches, a penalty for terminal A–U and G–U pairs, special energies for tetraloops and other frequent hairpins, coaxial stacking of helices in multiloops, and an affine rather than linear multiloop model. Mfold, RNAfold (the ViennaRNA package) and RNAstructure implement these.

### 16.2.2. An Implementation and What It Gets Right

**Example 16.2.1 (Folding tRNA-Phe)** We implemented Algorithm 16.2.1 in numpy with a simplified model: Watson–Crick stacks from Xia and colleagues (1998), one value for every stack involving a G–U pair, logarithmic loop penalties, a terminal A–U penalty and a linear multiloop term, and no dangling ends, tetraloop bonuses, coaxial stacking or modified nucleotides. The result was checked against exhaustive enumeration of all structures of random sequences of up to $23$ nucleotides: the minimum energy and the partition function agree exactly. For yeast tRNA-Phe ($76$ nt) the minimum free energy structure has $23$ pairs, of which $12$ are native: the acceptor stem is found, the anticodon stem is found, but the D and T arms are replaced by one long helix, an error of $-13$ kJ/mol in the model's own units (the predicted structure is given $-58.8$ kJ/mol and the native cloverleaf $-45.6$ kJ/mol). The sensitivity is $12/21 = 57\,\%$. The error has a physical cause that no secondary-structure model contains: the cloverleaf is held together by the tertiary interactions of the L-shaped molecule and by modified nucleotides, which the energy model does not see.

![Secondary structure of yeast tRNA-Phe predicted with a simplified nearest-neighbor model implemented in numpy (Algorithm 16.2.1). A: arc diagrams of the native cloverleaf (above the sequence, one color per stem) and of the predicted minimum free energy structure (below; red arcs are pairs that are not native). The acceptor and anticodon stems are recovered; the D and T arms are replaced by one long helix. B: base-pair probabilities from 1000 structures sampled from the Boltzmann ensemble (upper triangle, darker means more probable) against the native pairs (lower triangle): the acceptor stem has probability 0.97, the anticodon stem about 0.73, and the native T stem almost none](./plots/trna-fold.py)

### 16.2.3. The Ensemble

A single structure is a poor summary of a molecule that visits many. Replacing minima by sums and energies by Boltzmann factors in the same recursions gives the partition function $Z$ (McCaskill, 1990; [7.6.15](/7.6.15#sec-15.6.3)), from which follow the ensemble free energy $-RT\ln Z$ and, with an outside recursion or by sampling, the probability of every pair.

**Algorithm 16.2.2 (Stochastic Traceback)** Given the partition-function tables, generate a structure by tracing back as in the minimization, but at each step choose among the alternatives with probability proportional to their contributions to the corresponding table entry (Ding and Lawrence, 2003). Structures so generated are exact independent draws from the Boltzmann distribution; the probability of a pair is estimated by its frequency among $N$ samples, with standard error at most $1/(2\sqrt{N})$.

**Example 16.2.2** For tRNA-Phe in the model of Example 16.2.1, the ensemble free energy is $-64.3$ kJ/mol against $-58.8$ for the single best structure, so the minimum free energy structure holds only $\exp(-5.5/RT) = 12\,\%$ of the ensemble. Among $1000$ sampled structures the acceptor-stem pairs occur with probability $0.89$ to $0.97$ and the anticodon-stem pairs with $0.70$ to $0.74$, while the pairs of the native T stem occur with probability $0.05$ and those of the D stem never. The probabilities therefore say correctly which parts of the prediction to trust, without knowing the answer: a helix found in almost every sampled structure is a safe prediction, and the regions where the model is wrong are also the regions it is unsure about.

Base-pair probabilities are the input of the maximum expected accuracy structure, which maximizes $\sum_{(i,j) \in S}2\gamma P_{ij} + \sum_{i \text{ unpaired}}q_i$ (with $q_i$ the probability that $i$ is unpaired and $\gamma$ a weight) by the same kind of dynamic program, and is usually a little more accurate than the minimum free energy structure. They also give the probability that a stretch is unpaired, which is what determines accessibility to a **microRNA**, a ribosome or an antisense oligonucleotide (16.6). Other ensemble quantities follow from $Z$: the ensemble diversity (the mean base-pair distance between two sampled structures), the melting curve from $Z$ at several temperatures, and the energy of a given structure relative to the ensemble.

### 16.2.4. Folding in Practice

```bash
# minimum free energy structure, partition function and pair probabilities (ViennaRNA)
RNAfold -p --MEA < trna.fa > trna.out        # writes trna_dp.ps with the pair-probability dot plot
RNAsubopt -p 1000 < trna.fa > samples.txt    # 1000 structures from the Boltzmann ensemble
RNAfold --shape=reactivities.dat --shapeMethod=D < trna.fa   # with probing data (16.4)
```

```python
import RNA                                     # the ViennaRNA Python interface

seq = "GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA"
fc = RNA.fold_compound(seq)
structure, mfe = fc.mfe()                      # dot-bracket string and energy in kcal/mol
fc.exp_params_rescale(mfe)
_, ensemble_energy = fc.pf()                   # -RT ln Z
bpp = fc.bpp()                                 # bpp[i][j]: probability of the pair (i, j), 1-based
```

Accuracy falls with length: single-sequence prediction recovers roughly $70\,\%$ of the pairs of RNAs of a few hundred nucleotides and much less for RNAs of a few thousand, partly because errors accumulate and partly because long RNAs fold while they are transcribed and are bound by proteins ([7.6.16](/7.6.16#sec-16.7.5)). Three remedies are used, and they are the subjects of the next sections: experimental constraints, comparative analysis and learned models.

## 16.3. Chemical Probing as Constraints

Chemical probing measures, for every nucleotide of an RNA in solution or in cells, how accessible or flexible it is. In SHAPE chemistry (selective $2'$-hydroxyl acylation analyzed by primer extension) a reagent acylates the $2'$-OH of nucleotides that are conformationally flexible, which are mostly unpaired; dimethyl sulfate methylates unpaired A and C. The adducts are read out by reverse transcription: the enzyme stops at them, or, in the mutational-profiling variant (SHAPE-MaP, DMS-MaPseq), writes a mismatch, so that the rate of mismatches at a position in sequencing reads, compared with an untreated control, measures its reactivity. The same readout is used for structure probing inside cells and for RNA-binding protein footprints ([7.9.4](/7.9.4)).

**Formula 16.3.1 (Pseudo-Energy Constraints)** A normalized reactivity $S_i$ is converted into a pseudo-energy added to every stacked pair that contains nucleotide $i$,

$$
\Delta G_i = m\ln(S_i + 1) + b, \tag{16.2}
$$
with $m > 0$ and $b < 0$ (Deigan and colleagues, 2009; $m = 2.6$ and $b = -0.8$ kcal/mol, that is $10.9$ and $-3.3$ kJ/mol, for SHAPE data at $37\,^\circ\mathrm{C}$). A nucleotide with zero reactivity receives a bonus $b$ for pairing, one with high reactivity a penalty that grows logarithmically; nothing is forbidden, so the data bias the folding rather than constrain it absolutely.

**Example 16.3.1** We simulated reactivities for tRNA-Phe by drawing an exponential variable with mean $0.2$ for nucleotides paired in the cloverleaf and mean $1.0$ for unpaired ones, and folded with Eq. (16.2). The sensitivity rises from $57\,\%$ without data to $99\,\%$ with them, and the exact cloverleaf is recovered in $10$ of $12$ simulated profiles. Real probing data are less clean, because tertiary contacts and stacking protect many loop nucleotides: when a fraction of the unpaired nucleotides is drawn from the protected distribution instead, the mean sensitivity falls to $85\,\%$ at $40\,\%$ protected, $76\,\%$ at $60\,\%$ and $54\,\%$, no better than sequence alone, at $80\,\%$. The usefulness of probing data is therefore set by how specifically the reagent distinguishes paired from unpaired nucleotides in the molecule at hand.

![Chemical probing data as folding constraints (simulated reactivities, tRNA-Phe, the model of Example 16.2.1). A: one simulated profile with 20 % of the loop nucleotides protected; bars are colored by the native pairing state. B: the fraction of native pairs recovered without the data (dashed line) and with them, mean and 10th to 90th percentile over 12 simulated profiles, against the fraction of loop nucleotides that are protected. Data that distinguish paired from unpaired nucleotides cleanly almost determine the structure; data in which many unpaired nucleotides are protected add nothing](./plots/shape-constraints.py)

Probing data are also used without folding: the difference between reactivities measured in cells and in vitro locates protein binding and cotranscriptional folding, the difference between conditions locates **riboswitch** rearrangements, and reactivity patterns are themselves features for learned models.

## 16.4. Grammars and Covariance Models

### 16.4.1. Stochastic Context-Free Grammars

The recursions of 16.2 have a formal counterpart. A nested structure is exactly what a **context-free grammar** generates ([4.8.2](/4.8.2#sec-2.1)), with a rule that emits two correlated letters at once.

**Definition 16.4.1 (Stochastic Context-Free Grammar for RNA)** A *stochastic context-free grammar* is a context-free grammar in which every production of a nonterminal carries a probability, the probabilities of the productions of each nonterminal summing to one; the probability of a derivation is the product of the probabilities of the productions used, and the probability of a sequence is the sum over its derivations. For RNA the simplest grammar is

$$
S \to aSb \mid aS \mid Sa \mid SS \mid \varepsilon,
$$
in which $aSb$ emits a base pair, $aS$ and $Sa$ an unpaired nucleotide and $SS$ splits the sequence; a derivation of a sequence corresponds to a secondary structure.

The most probable derivation of a given sequence is found by the **CYK algorithm** ([4.8.8](/4.8.8#sec-8.5)), which is the same dynamic program as Algorithm 16.2.1 with $-\log$ probabilities in place of energies: the correspondence between a probability model and an energy model is $p \propto \mathrm{e}^{-\Delta G/RT}$. Summing over derivations instead of maximizing gives the inside algorithm, the grammatical partition function, and the inside–outside algorithm computes the posterior probability of every pair and trains the production probabilities by the **EM algorithm** ([3.5.6](/3.5.6)), exactly as the forward–backward and Baum–Welch algorithms do for hidden Markov models ([4.6.8](/4.6.8)). A hidden Markov model is a stochastic *regular* grammar; the step up to context-free grammars buys the ability to describe nested pairing, and costs $O(n^3)$ instead of $O(n)$ per sequence.

### 16.4.2. Covariance Models

A profile hidden Markov model describes a family of sequences column by column ([7.8.5](/7.8.5#sec-5.5)). A *covariance model* (Eddy and Durbin, 1994) does the same for a family with a conserved secondary structure: it is a stochastic context-free grammar whose nonterminals follow the consensus structure, with one state per consensus position or pair.

**Definition 16.4.2 (Covariance Model)** A *covariance model* of an RNA family is a stochastic context-free grammar built from a structural alignment, with match states of two kinds — a pair state that emits two nucleotides with a joint distribution over the $16$ combinations, and a single state that emits one nucleotide with a distribution over the $4$ — together with insert and delete states as in a profile hidden Markov model, arranged along a guide tree that follows the consensus structure.

A pair state scores the two columns jointly, which is what distinguishes a covariance model from a profile: a G–C pair replaced by A–U keeps a high score, whereas a profile that treats the columns independently loses twice. Rfam (Kalvari and colleagues) is built on this machinery: each family has a seed alignment with a consensus structure, a covariance model built from it by `cmbuild`, a calibrated score threshold, and full alignments of all hits in the sequence databases. Searching a genome with a covariance model, `cmsearch` in the Infernal package, costs far more than a profile search, and Infernal 1.1 makes it practical with a cascade of filters: a profile hidden Markov model of the sequence alone first discards most of the genome, and only the survivors are scored with the full model.

```bash
cmbuild trna.cm trna-seed.sto        # build a covariance model from a structural alignment
cmcalibrate trna.cm                  # fit the score distribution for E-values
cmsearch --cut_ga trna.cm genome.fa  # search a genome; --cut_ga uses the curated threshold
cmscan --rfam --tblout hits.tbl Rfam.cm query.fa      # annotate a sequence with all Rfam families
```

Specialized searches can do better than a general family model: tRNAscan-SE combines fast scans for the promoter elements and the invariant positions of tRNAs with a covariance model and is the standard annotation of tRNA genes in new genomes ([7.8.11](/7.8.11)).

## 16.5. Comparative Analysis

The secondary structures of transfer RNA, of ribosomal RNA and of the RNA component of RNase P were established before any crystal structure, by comparing homologous sequences: in an alignment, the two columns of a conserved pair change together, from G–C to A–U or C–G, while remaining complementary.

**Definition 16.5.1 (Compensatory Mutation)** A *compensatory mutation* is a pair of substitutions at two positions of an RNA that together preserve base pairing (G–C to A–U), as opposed to a consistent mutation, which preserves pairing with one substitution (G–C to G–U), and a single substitution that breaks the pair. An excess of compensatory and consistent changes between homologs is evidence that the two positions pair.

The statistic is the mutual information of two alignment columns, as for coevolution in proteins ([7.6.15](/7.6.15#sec-15.5.4)), with the difference that a base pair constrains two positions to a complementary combination rather than to a compatible physicochemical one, so the signal is strong and the number of sequences needed is small.

**Example 16.5.1 (The Cloverleaf from an Alignment)** The seed alignment of the Rfam family RF00005 contains $954$ tRNA sequences from all domains of life; after restricting to its $71$ consensus columns, weighting sequences by the inverse of the number of neighbors at $62\,\%$ identity (an effective sample size of $112$), we computed the mutual information of every pair of columns and applied the average product correction, which subtracts the part explained by the overall variability of each column. Of the $24$ highest-scoring pairs, $21$ are pairs of the consensus structure, and $20$ of the $21$ consensus pairs are among the top $21$ scores: the cloverleaf is recovered from the alignment alone, with no energy model. The highest-scoring pair that is not in the consensus structure, columns $18$ and $54$, is G–C in $723$ sequences, U–A in $44$ and A–U in $21$ — the covarying tertiary pair that joins the D and T loops in the elbow of the L-shaped molecule — and the next, columns $15$ and $46$, is G–C in $460$ sequences and A–U in $323$, the Levitt pair. Comparative analysis thus sees the interactions that the secondary-structure model cannot, which are the same interactions that made the thermodynamic prediction of Example 16.2.1 fail.

![Covariation in an alignment of transfer RNAs recovers the cloverleaf. The seed alignment of the Rfam family RF00005 (954 sequences, 71 consensus columns), sequences weighted by the inverse number of neighbors at 62 % identity. A: corrected mutual information of every pair of columns (lower triangle) against the consensus secondary structure of the family (upper triangle, one color per stem). B: the 24 highest-scoring pairs of columns; all but three are consensus pairs, and the exceptions are the tertiary contacts of the elbow](./plots/covariation.py)

Two uses follow. Given an alignment, fold all sequences at once: RNAalifold minimizes the sum of the folding energies of the aligned sequences plus a covariation bonus, and is far more accurate than folding one sequence; Pfold uses a stochastic context-free grammar with a phylogenetic model of substitution at paired and unpaired positions. Given a structure, test whether the covariation is real: related sequences are not independent observations, so two columns can covary merely because the sequences share ancestry. R-scape (Rivas and colleagues, 2017) computes a covariation statistic for every pair under a null model built from the phylogeny of the alignment and reports which pairs are significant. Applied to published structures of long noncoding RNAs, it found that many have no significant covariation at all, meaning that the proposed structures were predictions, not evidence; applied to ribosomal and transfer RNAs, it confirms nearly every helix. If an alignment is not available, one can be built by folding and aligning at the same time (the Sankoff algorithm, $O(n^6)$ in time, approximated by Foldalign, Dynalign and LocARNA).

## 16.6. RNA–RNA Interactions and MicroRNA Targets

### 16.6.1. Hybridization and Accessibility

Two RNAs that pair with each other pose the same problem with two sequences: an antisense oligonucleotide, a bacterial small RNA and its messenger, the two strands of an RNA duplex. The energy of the interaction has two parts, the energy gained by forming the intermolecular helix and the energy that must be paid to open the intramolecular structure that covers the site.

**Formula 16.6.1 (Interaction Energy with Accessibility)** For an interaction that uses the region $[i, j]$ of one RNA and $[k, l]$ of the other,

$$
\Delta G_{\mathrm{total}} = \Delta G_{\mathrm{hybrid}} + \Delta G_{\mathrm{open}}^{(1)}[i, j] + \Delta G_{\mathrm{open}}^{(2)}[k, l],
$$
where the opening energies are computed from the partition function of each molecule alone, $\Delta G_{\mathrm{open}}[i, j] = -RT\ln\mathbb{P}([i, j] \text{ unpaired})$, which is nonnegative. RNAup and IntaRNA minimize this sum over interaction sites.

Accessibility usually matters more than the hybridization energy: a perfectly complementary site hidden inside a stable hairpin is not used, while a shorter site in a single-stranded loop is.

### 16.6.2. MicroRNA Target Prediction

A **microRNA** directs the silencing complex to messenger RNAs that pair with it, and the pairing rules are unusually simple: nucleotides $2$ to $7$ of the microRNA, the **seed sequence**, must pair perfectly in most functional sites, while pairing of the $3'$ half contributes little except at compensatory sites. Target prediction therefore begins with exact matching rather than folding.

**Definition 16.6.1 (Seed Site Types)** For a microRNA with seed nucleotides $2$–$8$, a site in a target is a *6mer* if it matches nucleotides $2$–$7$, a *7mer-A1* if it matches $2$–$7$ and has an A opposite nucleotide $1$, a *7mer-m8* if it matches $2$–$8$, and an *8mer* if it matches $2$–$8$ and has an A opposite nucleotide $1$. Their efficacy increases in the order 6mer < 7mer-A1 < 7mer-m8 < 8mer; the A opposite nucleotide $1$ is read by a pocket of the Argonaute protein rather than paired with the microRNA.

Exact matches are far too numerous to be useful on their own: a given 7mer occurs by chance about once per $16$ kb of sequence, so a transcriptome contains tens of thousands of matches for every microRNA. Predictors therefore score the context of each site. The TargetScan context score combines the site type with the local AU content (AU-rich flanks are more effective, both because the site is more accessible and because they are associated with regulatory $3'$ untranslated regions), the position in the untranslated region (sites near the ends, and away from the center of long regions, work better), the pairing of the microRNA's $3'$ half, and conservation across species — the most informative single feature, since a site conserved in mammals is unlikely to be chance ([7.8.8](/7.8.8#sec-8.6)).

**Example 16.6.1 (let-7 Sites in HMGA2)** The $3'$ untranslated region of human *HMGA2* is $2999$ nt long in the canonical transcript and contains, for the seed of let-7a-5p, one 8mer, three 7mer-m8 sites, three 7mer-A1 sites and one 6mer: seven sites of the effective types, which is why *HMGA2* is strongly repressed by let-7 and why chromosomal rearrangements that truncate this untranslated region remove the repression and contribute to mesenchymal tumors ([7.4.15](/7.4.15)). The AU content of the $30$ nt flanking each site ranges from $0.48$ to $0.70$ against $0.64$ for the whole region, so the context favors the three 7mer-A1 sites and disfavors the 8mer, a reminder that site type alone does not rank sites. Predictions of this kind are tested by measuring the transcripts and proteins after transfecting or deleting the microRNA, and the agreement is modest: individual sites typically change their target's level by tens of percent.

![Target sites of the microRNA let-7 in the 3' untranslated region of human HMGA2 (2999 nt, Ensembl canonical transcript). A: the pairing of the 8mer site with let-7a-5p; nucleotides 2 to 8 pair with the target and the A of the target lies opposite nucleotide 1, where it is read by the Argonaute pocket rather than paired. B: the positions of all seed sites along the untranslated region, by type. C: the AU content of the 30 nt on each side of each site, a determinant of efficacy, against the AU content of the whole region (dashed line)](./plots/mirna-sites.py)

Sites that do not follow these rules exist: noncanonical sites with bulges, sites in coding regions and sites that pair extensively in the $3'$ half with a mismatched seed. Cross-linking methods that capture Argonaute together with its target (CLIP and its chimeric variants, [7.9.4](/7.9.4)) measure the sites directly and show both that most functional sites are canonical and that many canonical matches are never bound. Which messengers a microRNA actually controls in a cell, and what that does to the network, belongs to [7.9](/7.9).

## 16.7. Learned Models of RNA Structure

Networks trained on known structures predict secondary structure as a matrix of pairing probabilities: SPOT-RNA (Singh and colleagues, 2019) uses residual and recurrent layers and predicts pseudoknots and noncanonical pairs, which thermodynamic models exclude by construction; UFold and others treat the problem as image segmentation on an $L \times L$ representation of all possible pairs; MXfold2 constrains a learned model by the thermodynamic parameters. Within families represented in the training data these models beat energy minimization by a wide margin; on families held out, several studies have found that the advantage largely disappears (Flamm and colleagues, 2022; Szikszai and colleagues, 2022), the same homology leakage that [7.8.15](/7.8.15#sec-15.6.1) describes: the standard benchmarks contain families in both the training and the test set, so what is measured is recall of known structures. Evaluations that split by family, and hybrids that keep the physics and learn only corrections, are the current standard.

Tertiary structure is harder than for proteins, because far fewer RNA structures are known: the Protein Data Bank contains more than two hundred thousand protein structures and only a few thousand RNAs. Fragment assembly (FARFAR2), coarse-grained models with statistical potentials (SimRNA) and deep networks (trRosettaRNA, DRfold, the RNA modes of AlphaFold 3 and RoseTTAFold All-Atom) produce useful models for small RNAs with well-represented folds and fail for large ones and for folds without homologs, as the blind RNA-Puzzles and the RNA category of CASP15 showed. The physical reasons — the dominance of the secondary structure, the role of $\ce{Mg^2+}$ ions, the flexibility of junctions — are discussed in [7.6.15](/7.6.15#sec-15.6.4) and [7.6.16](/7.6.16#sec-16.7).

## Summary

| Topic | Key points |
|---|---|
| Representation | secondary structure as a nested set of pairs; dot-bracket notation, arc diagrams; pseudoknots are crossing pairs, NP-hard in general (Definition 16.1.1) |
| Energy model | loops, not pairs, carry the energy: hairpins, stacks, bulges, interior loops, multiloops (Turner parameters, [7.6.15](/7.6.15#sec-15.6.1)) |
| Zuker | tables $V$, $WM$, $WM1$, $W$ (Algorithm 16.2.1); $O(n^3)$ time and $O(n^2)$ memory with interior loops capped at $30$ (Theorem 16.2.1); every structure generated once |
| tRNA-Phe | a numpy implementation recovers the acceptor and anticodon stems but merges the D and T arms: $12$ of $21$ native pairs (Example 16.2.1) |
| Ensemble | partition function by sum-product; stochastic traceback (Algorithm 16.2.2); the best structure holds $12\,\%$ of the ensemble, and pair probabilities mark the reliable helices (Example 16.2.2); MEA structures, unpaired probabilities |
| Probing | SHAPE and DMS reactivities as pseudo-energies $m\ln(S + 1) + b$ (Formula 16.3.1); sensitivity $57\,\% \to 99\,\%$ with clean data and no gain when $80\,\%$ of loop nucleotides are protected (Example 16.3.1) |
| Grammars | stochastic context-free grammars; CYK = Zuker with log probabilities; inside–outside = EM (Definition 16.4.1); covariance models add pair states (Definition 16.4.2), Rfam and Infernal with HMM prefilters |
| Covariation | compensatory and consistent mutations (Definition 16.5.1); corrected mutual information recovers $20$ of $21$ tRNA pairs in the top $21$ and finds the elbow tertiary contacts (Example 16.5.1); RNAalifold, R-scape against phylogenetic artifacts |
| Interactions | hybridization plus opening energies (Formula 16.6.1); seed site types 6mer, 7mer-A1, 7mer-m8, 8mer (Definition 16.6.1); seven let-7 sites in the *HMGA2* untranslated region (Example 16.6.1); context, conservation and CLIP evidence |
| Learned models | SPOT-RNA, UFold, MXfold2 predict pairing matrices and pseudoknots; the advantage is largely lost on held-out families; tertiary prediction limited by the few thousand known RNA structures |

## Questions

1. Is the string `((..((...))..)).((...))` a valid dot-bracket structure for a sequence of its own length, and what would the structure `((..[[..))..]]` represent?

   **Answer** The first is valid: parentheses are balanced and nested, each hairpin loop has at least three unpaired nucleotides (three and three), and the two outer helices do not overlap. The second uses a second bracket type because its pairs cross — the pairs written with parentheses span positions that the pairs written with square brackets enter and leave — so it is a pseudoknot, outside the class that Definition 16.1.1 and the algorithms of 16.2 handle. Checking validity is a stack traversal: push on an opening bracket, pop on a closing one, and the structure is nested if and only if one stack suffices.

2. Why does Algorithm 16.2.1 need the two multiloop tables $WM$ and $WM1$ instead of one? Give an answer that works for the minimization and one that works for the partition function.

   **Answer** $WM1$ requires the branch to begin exactly at $i$, so a multiloop is decomposed as "everything up to the last branch" plus "the last branch and the unpaired nucleotides after it", and each arrangement of branches arises in exactly one way. For minimization a redundant decomposition would still give the correct minimum, but the traceback would be ambiguous and the per-branch and per-unpaired terms could be counted inconsistently. For the partition function redundancy is fatal: $Z$ is a sum over structures, so a structure generated by two different paths is counted twice, the probabilities are wrong and stochastic traceback no longer samples the Boltzmann distribution. This is the same requirement as unambiguity in a stochastic grammar (16.4.1).

3. Folding a sequence of $200$ nucleotides takes $0.2$ s with an $O(n^3)$ implementation. Estimate the time for $2000$ and for $20\,000$ nucleotides, and state the memory needed in the second case for four tables of double-precision numbers.

   **Answer** Cubic scaling multiplies the time by $10^3 = 1000$ per factor of ten: about $200$ s for $2000$ nt and about $2\times10^5$ s, more than two days, for $20\,000$ nt. Memory grows as $n^2$: four tables of $20\,000^2$ entries at $8$ bytes are $4 \times 4\times10^8 \times 8 = 1.3\times10^{10}$ bytes, about $13$ GB, which is why programs store only the upper triangle, use single precision, or fold long RNAs in overlapping windows of one or two kilobases.

4. In the ensemble of Example 16.2.2 ($Z$ known, $-RT\ln Z = -64.3$ kJ/mol), what is the probability of a particular structure whose energy is $4$ kJ/mol above the minimum of $-58.8$ kJ/mol? What does this say about reporting a single structure?

   **Answer** $\mathbb{P} = \mathrm{e}^{-(\Delta G - \Delta G_{\mathrm{ens}})/RT}$ with $RT = 2.58$ kJ/mol at $37\,^\circ\mathrm{C}$: for $\Delta G = -54.8$, $\mathbb{P} = \mathrm{e}^{-9.5/2.58} = 2.5\,\%$, against $12\,\%$ for the minimum. A structure $4$ kJ/mol worse is only five times less probable, and the parameters themselves are uncertain by more than that, so the single best structure is one of many comparable ones; the honest output is the pair probabilities, or a set of samples, and a prediction should be trusted only where they are concentrated.

5. Convert the reactivities $S = 0$, $0.3$ and $2.0$ into pseudo-energies with Eq. (16.2) ($m = 10.9$, $b = -3.3$ kJ/mol) and explain what each does to a helix.

   **Answer** $\Delta G = -3.3$, $10.9\ln1.3 - 3.3 = -0.44$ and $10.9\ln3 - 3.3 = +8.67$ kJ/mol. An unreactive nucleotide gives a bonus of $3.3$ kJ/mol to each stacked pair that contains it, so a helix of five pairs with unreactive nucleotides throughout gains about $33$ kJ/mol (two nucleotides per stack) — enough to overturn the sequence-based prediction. A moderately reactive nucleotide is nearly neutral, and a highly reactive one costs $8.7$ kJ/mol per stack, which usually prevents pairing without forbidding it; a single wrong measurement therefore bends but does not break the prediction.

6. An antisense oligonucleotide is designed against a target site whose probability of being unpaired is $0.05$. How much binding energy is spent opening the structure at $37\,^\circ\mathrm{C}$, and how should the site be chosen?

   **Answer** $\Delta G_{\mathrm{open}} = -RT\ln0.05 = 2.58 \times 3.0 = 7.7$ kJ/mol, about $1.8$ kcal/mol, which cancels the gain from roughly two base pairs. Sites should be chosen by the predicted unpaired probability from the partition function, not by complementarity alone: a site with $\mathbb{P} = 0.8$ costs only $0.6$ kJ/mol. Since long RNAs are folded only approximately, the probabilities should be computed in windows and checked against probing data, and several candidate sites tested.

7. Two columns of an alignment of $400$ sequences covary strongly, but the sequences fall into two clades, within each of which the two columns are invariant. What is the problem, and what does R-scape do about it?

   **Answer** The apparent covariation comes from one substitution event in the common ancestor of one clade, not from $400$ independent observations; sequences are related by descent, so the effective sample size is the number of independent changes on the tree, which here is one. Mutual information computed as if the sequences were independent is then badly inflated — the same phylogenetic inflation that makes sequence weighting necessary in Example 16.5.1. R-scape estimates a null distribution of the covariation statistic from the phylogeny of the alignment itself, by simulating sequences along the tree under a substitution model with no pairing, and reports a pair only if its statistic exceeds what the tree alone produces, which also controls the many pairs tested.

8. For a microRNA whose seed is given, how many chance 7mer-m8 matches are expected in a $3'$ untranslated region of $3$ kb, and how many in a transcriptome with $3.5\times10^7$ nucleotides of such regions? What follows for prediction?

   **Answer** A specific $7$-mer has probability $4^{-7} = 1/16\,384$ per position under a uniform model, so $3000/16\,384 = 0.18$ matches are expected in one region and $3.5\times10^7/16\,384 = 2100$ across the transcriptome; 6mer matches are four times as frequent, about $8500$. Since a microRNA measurably represses of the order of a few hundred messengers, most matches must be nonfunctional, and a predictor cannot rely on the match alone: conservation across species, site type, AU context and position, and direct evidence of binding are needed, exactly as for transcription factor motifs ([7.8.8](/7.8.8#sec-8.3.1)). Base composition also matters: AU-rich untranslated regions contain more matches for AU-rich seeds than the uniform estimate suggests.

9. (Design) A new long noncoding RNA of $2$ kb is proposed to act through a conserved structure. Design an analysis that would support or refute this, using the methods of this chapter.

   **Answer** First collect homologs by sequence search in related genomes ([7.8.4](/7.8.4)) and build an alignment; if homologs are detectable only in close relatives, the total branch length may be too small for covariation to be informative, which must be stated. Fold the sequence with a partition function in overlapping windows and report pair probabilities rather than a single structure, since $2$ kb is beyond the length where a minimum free energy structure is reliable. Fold the alignment with RNAalifold and test every proposed helix with R-scape: significant covariation is the strongest evidence, and its absence across a deep alignment is evidence against a conserved structure. Probe the RNA in vitro and in cells by SHAPE-MaP and refold with the reactivities as pseudo-energies (Formula 16.3.1), checking that the in-cell and in-vitro profiles agree where the structure is claimed. Compare the folding energy with that of shuffled sequences preserving dinucleotide composition, which is a weak but standard control. Finally test function: mutate one side of a proposed helix and the compensating side, and show that the single mutants lose the function while the double mutant restores it — the experimental analogue of a compensatory mutation.

10. (Open) Why do deep-learning predictors of RNA secondary structure outperform thermodynamic folding on standard benchmarks but not on new families, and what would make a fair comparison?

    **Answer** Standard benchmarks are built from the known structures, which are dominated by a few families (transfer RNA, ribosomal RNA, group I introns, riboswitches) whose members appear in both training and test sets; a network with enough capacity can learn the family rather than the folding rule, and recognizing a family from its sequence is far easier than folding it (the leakage of [7.8.15](/7.8.15#sec-15.6.1)). Thermodynamic models, fitted to melting experiments on short duplexes, have no such advantage and no such leakage. A fair comparison splits by family or by Rfam clan, reports accuracy separately for families seen and unseen in training, and includes a nearest-neighbor baseline that simply copies the structure of the most similar training sequence — if the learned model does not beat that baseline on held-out families, it has learned recall rather than folding. Approaches that generalize better either keep the physics and learn corrections to the parameters, or train on data that are not structures at all, such as probing profiles from many transcripts, which are available in quantity and are not concentrated in a few families.
