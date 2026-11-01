---
title: Read Mapping and Genome Indexing
description: "How hundreds of millions of short and long reads are placed on a reference genome. The scale of the problem and the seed-and-extend paradigm with the pigeonhole bound; indexes of the genome: hash tables of k-mers, suffix arrays and binary search, the Burrows–Wheeler transform, LF mapping and its inversion, the FM-index with backward search and sampled suffix arrays, and the memory of a human index. Aligners: super-maximal exact matches, chaining and banded extension in BWA-MEM, end-to-end and local modes, pairing; minimizers and colinear chaining in minimap2; spliced alignment (STAR, HISAT2) and graph genomes. Mapping quality as a posterior probability and its calibration, mappability and reference bias. The SAM/BAM/CRAM formats, FLAG bits, CIGAR strings, MD and NM tags; sorting, indexing, duplicate marking, coverage and genome browsers. Application: searching a genome for CRISPR off-target sites."
---

A **reference genome** turns the analysis of resequencing data into a search problem: each **read** of [7.8.9](/7.8.9) is a short, slightly erroneous copy of some stretch of the reference, and the first task is to find which stretch. Mapping is the step on which variant calling ([7.8.12](/7.8.12)), the analysis of population data ([7.8.13](/7.8.13)) and almost every functional genomics assay of [7.9](/7.9) depend. It is a **sequence alignment** problem ([7.8.3](/7.8.3)), but of a size at which the dynamic programming of [7.8.3](/7.8.3) is useless by itself: the solution combines the seed-and-extend idea of BLAST ([7.8.4](/7.8.4)) with indexes of the genome that answer exact-match queries in time independent of its length. The central index, the FM-index built on the Burrows–Wheeler transform, is one of the most consequential ideas imported into biology from computer science; its ancestors, the **trie**, the **suffix tree** and the **suffix array**, are described in [4.3.13](/4.3.13). This chapter develops the indexes (10.2), the aligners built on them (10.3), the probability that a read has been placed wrongly (10.4), the files in which alignments are kept (10.5), and one application of approximate genome search beyond mapping, the search for off-target sites of CRISPR guides (10.6). The running examples are the whole-genome reads of HG002 from [7.8.9](/7.8.9) and the $50$-nt amplicon reads of a teaching panel of single-nucleotide polymorphisms that includes rs4988235 in *MCM6* ([7.8.1](/7.8.1), [7.8.2](/7.8.2)). When no reference exists, reads are assembled instead ([7.8.11](/7.8.11)).

## 10.1. The Mapping Problem

### 10.1.1. Scale

A $30\times$ human genome sequenced with $150$-nt reads consists of $3.1\times10^9 \times 30/150 = 6.2\times10^8$ reads. Aligning one read to the whole genome with the **Smith–Waterman algorithm** fills $150 \times 3.1\times10^9 = 4.65\times10^{11}$ cells; for all reads that is $2.9\times10^{20}$ cells, about ninety years at $10^{11}$ cell updates per second, the speed of a well-vectorized implementation on a large server. The task must be solved in hours, so a factor of about $10^5$ has to come from not looking at most of the genome.

**Definition 10.1.1 (Read Mapping)** **Read mapping** is the problem of finding, for each read and a reference genome, the position (chromosome, coordinate and strand) and alignment that best explain the read as a copy of the reference with sequencing errors and small variants, together with a measure of confidence that this position is correct. The alignment is a **semi-global alignment** ([7.8.3](/7.8.3#sec-3.5.5)): global in the read, possibly with its ends clipped, and local in the reference.

Two features of the data make the problem tractable. Reads differ from their true source in few positions: at an error rate of about $0.1$–$1\,\%$ and a human heterozygosity of about $0.1\,\%$, a $150$-nt read typically has zero to three differences. And most of the genome is unique at the length of a read, so the source can be identified from a short exact match. The difficulties are the exceptions: repeats, for which a read fits several places equally well (Section 10.4), and regions where the sample differs more from the reference, such as indels, structural variants and divergent haplotypes, which are mapped poorly or not at all (reference bias, [7.4.14](/7.4.14#sec-14.2.3)).

### 10.1.2. Seeds and the Pigeonhole Principle

Mappers follow the *seed-and-extend* paradigm of BLAST ([7.8.4](/7.8.4#sec-4.3)): find short exact matches (seeds) between the read and the genome with an index, then align the read around the seeds by dynamic programming in a small window. The question is how long a seed may be while still guaranteeing that the true location is found.

**Theorem 10.1.1 (Pigeonhole Bound)** If a read of length $L$ has an alignment to its source with at most $k$ substitutions, insertions or deletions (an **edit distance** of at most $k$), and the read is divided into $k + 1$ non-overlapping pieces, then at least one piece occurs exactly in the source. In particular there is an exact match of length at least $\lfloor L/(k+1)\rfloor$.

**Proof** Each edit operation of the alignment affects the read at one position or, for a deletion, between two adjacent positions of the read, and so touches at most one piece if we assign a deletion between pieces to either neighbour. With $k$ edits and $k + 1$ pieces, some piece is touched by none, and it is copied exactly from the source. $\square$

**Formula 10.1.1 (Chance Seed Hits)** In a random genome of length $G$ with equal base frequencies, a given $s$-mer occurs on either strand at an expected number of
$$
\frac{2G}{4^s}
$$
positions.

**Example 10.1.1** For $L = 150$ and $k = 4$ the pigeonhole bound guarantees an exact $30$-mer. In a random genome of $3.1\times10^9$ bases an $s$-mer has $2G/4^{s}$ chance occurrences: $370$ for $s = 12$, $1.4$ for $s = 16$, $0.0056$ for $s = 20$ and $5\times10^{-9}$ for $s = 30$. Seeds of about $20$ nt are therefore long enough to be specific in unique sequence and short enough to survive a few differences. The real genome is far from random: half of it consists of repeats ([7.2.2](/7.2.2#sec-2.2.1)), and a $20$-mer from an Alu element occurs hundreds of thousands of times. Mappers therefore limit the number of occurrences they examine for any seed, and rely on other seeds of the same read to place it.

## 10.2. Indexing a Genome

An index of the reference answers the query "where does this string occur?" quickly. Three kinds are used, which trade memory against speed and flexibility.

### 10.2.1. Hash Tables of k-mers

The simplest index is a **hash table** keyed by every $s$-mer of the genome, with the list of its positions as the value. A query takes constant time per seed. Its drawback is memory: one position per genome base, at $4$ bytes each, is already $12\,\mathrm{GB}$ for the human genome, and the seed length is fixed when the index is built. Early short-read mappers hashed either the reads, scanning the genome against them (MAQ), or seeds of the genome (SOAP); BLAT and SSAHA hashed non-overlapping $s$-mers of the genome to save space. Modern long-read mappers keep the hash table but sample the $k$-mers by minimizers (Section 10.3.2), which reduces its size several-fold.

### 10.2.2. Suffix Arrays

The **suffix array** of a text $T$ of length $n$ ending in a sentinel symbol $\mathrm{}\char36$, smaller than every letter, lists the starting positions of the suffixes of $T$ in lexicographic order. All occurrences of a pattern $P$ are prefixes of a contiguous block of suffixes, so they occupy an interval of the array that is found by **binary search** in $O(m\log n)$ comparisons of the pattern of length $m$ with suffixes (each comparison costs up to $m$ steps, or less with stored longest common prefixes). For $T = \mathrm{acaacg}\char36$ the sorted suffixes are $\mathrm{}\char36$, $\mathrm{aacg}\char36$, $\mathrm{acaacg}\char36$, $\mathrm{acg}\char36$, $\mathrm{caacg}\char36$, $\mathrm{cg}\char36$, $\mathrm{g}\char36$, so $\mathrm{SA} = (6, 2, 0, 3, 1, 4, 5)$ in zero-based positions, and the occurrences of $\mathrm{ac}$ are rows $2$–$3$, positions $0$ and $3$.

A suffix array of the human genome needs $\lceil\log_2 n\rceil = 32$ bits per base, $12\,\mathrm{GB}$, and more for both strands; the text itself is needed for the comparisons. The spliced aligner STAR uses an uncompressed suffix array and needs about $30\,\mathrm{GB}$ of memory for the human genome, which it repays with speed. Building a suffix array by sorting takes $O(n\log n)$ comparisons of long strings; linear-time algorithms such as SA-IS construct it in $O(n)$ by induced sorting.

### 10.2.3. The Burrows–Wheeler Transform

**Definition 10.2.1 (Burrows–Wheeler Transform)** Let $T$ be a text of length $n$ whose last symbol is the unique sentinel $\mathrm{}\char36$, and let $\mathrm{SA}$ be its suffix array. The **Burrows–Wheeler transform** of $T$ is the string $L = \mathrm{BWT}(T)$ of length $n$ with
$$
L[i] = T[\mathrm{SA}[i] - 1] \quad (\text{and } L[i] = \mathrm{}\char36 \text{ if } \mathrm{SA}[i] = 0),
$$
the symbol preceding the $i$-th smallest suffix. Equivalently, if the $n$ cyclic rotations of $T$ are sorted into the rows of a matrix (the Burrows–Wheeler matrix), $L$ is its last column; its first column $F$ consists of the symbols of $T$ in sorted order.

For $T = \mathrm{acaacg}\char36$, the sorted rotations begin with $\mathrm{}\char36, \mathrm{a}, \mathrm{a}, \mathrm{a}, \mathrm{c}, \mathrm{c}, \mathrm{g}$ and end with $\mathrm{g}, \mathrm{c}, \mathrm{}\char36, \mathrm{a}, \mathrm{a}, \mathrm{a}, \mathrm{c}$, so $\mathrm{BWT}(T) = \mathrm{gc}\char36\mathrm{aaac}$. The transform was invented for compression (Burrows and Wheeler, 1994): symbols that precede similar contexts are grouped, so the last column consists of long runs in repetitive text and compresses well (it is the core of `bzip2`). The property that makes it an index is that it is invertible, and the inversion is a walk that can be stopped at any point.

**Theorem 10.2.1 (LF Mapping)** In the Burrows–Wheeler matrix, the $j$-th occurrence of a symbol $c$ in the last column $L$ and the $j$-th occurrence of $c$ in the first column $F$ are the same symbol of $T$. Consequently, if $C[c]$ is the number of symbols of $T$ smaller than $c$ and $\mathrm{Occ}(c, i)$ the number of occurrences of $c$ in $L[0, i)$, the row whose rotation begins with the symbol $L[i]$ of row $i$ is
$$
\mathrm{LF}(i) = C[L[i]] + \mathrm{Occ}(L[i], i).
$$

**Proof** Consider the rows whose last symbol is $c$; their rotations have the form $\alpha c$. Rotating each by one position gives $c\alpha$, the rows that begin with this same occurrence of $c$. Rows ending in $c$ are in the order of their $\alpha$ (the rows are sorted, and rows ending in $c$ are compared on $\alpha$, which comes first); rows $c\alpha$ that begin with $c$ are also in the order of $\alpha$. So the order of the occurrences of $c$ is the same in both columns. The rows beginning with $c$ form the block starting at $C[c]$, and the occurrence at $L[i]$ is the $(\mathrm{Occ}(L[i], i) + 1)$-th $c$ in $L$, hence the formula. $\square$

Starting from row $0$, whose rotation begins with $\mathrm{}\char36$ (so $L[0]$ is the last letter of $T$), repeated application of $\mathrm{LF}$ visits the rows in which the text is rotated one more step to the right and reads $T$ backwards from $L$: the transform is inverted with only $L$ and the counts $C$ and $\mathrm{Occ}$.

### 10.2.4. The FM-Index and Backward Search

**Definition 10.2.2 (FM-Index)** The **FM-index** of a text $T$ (Ferragina and Manzini, 2000) consists of its Burrows–Wheeler transform $L$, the array $C$ of counts of smaller symbols, a structure that returns $\mathrm{Occ}(c, i)$ for any symbol $c$ and position $i$ in constant time (the counts stored at checkpoints every $b$ positions, completed by counting within the block), and a *sampled* suffix array that stores $\mathrm{SA}[i]$ only for rows whose text position is a multiple of a step $s$.

**Algorithm 10.2.1 (Backward Search)** Input: an FM-index of $T$ ($n$ symbols) and a pattern $P = p_1 \cdots p_m$. Output: the interval $[sp, ep)$ of rows of the Burrows–Wheeler matrix whose rotations begin with $P$.

1. Set $sp = 0$, $ep = n$.
2. For $j = m, m - 1, \dots, 1$: set $c = p_j$, $sp \gets C[c] + \mathrm{Occ}(c, sp)$, $ep \gets C[c] + \mathrm{Occ}(c, ep)$. If $sp \ge ep$, stop: $P$ does not occur.
3. Return $[sp, ep)$; the number of occurrences is $ep - sp$.

To report a position, from each row $i$ in the interval apply $\mathrm{LF}$ until reaching a row whose suffix-array entry is sampled, at text position $t$ after $u$ steps; the occurrence starts at $t + u$.

**Theorem 10.2.2** After processing $p_j \cdots p_m$, the interval $[sp, ep)$ of Algorithm 10.2.1 consists exactly of the rows whose rotations begin with $p_j \cdots p_m$. Counting the occurrences of $P$ takes $O(m)$ time, independent of $n$, and locating each occurrence takes at most $s - 1$ further LF steps.

**Proof** By induction on the number of processed symbols. Initially the interval contains all rows, which begin with the empty string. Suppose $[sp, ep)$ are the rows beginning with $Q = p_{j+1} \cdots p_m$. A row begins with $cQ$ exactly when it is the LF image of a row that begins with $Q$ and ends with $c$. The rows in $[sp, ep)$ ending in $c$ are the occurrences of $c$ in $L[sp, ep)$, which by Theorem 10.2.1 map to consecutive rows in the block of $c$ from $C[c] + \mathrm{Occ}(c, sp)$ to $C[c] + \mathrm{Occ}(c, ep)$, exclusive. Each step uses two $\mathrm{Occ}$ queries of constant time. The sampled positions are $s$ apart in the text and each LF step moves one position back, so at most $s - 1$ steps reach a sampled row. $\square$

**Example 10.2.1** For $T = \mathrm{acaacg}\char36$, $L = \mathrm{gc}\char36\mathrm{aaac}$, $C[\mathrm{}\char36] = 0$, $C[\mathrm{a}] = 1$, $C[\mathrm{c}] = 4$, $C[\mathrm{g}] = 6$. Search for $P = \mathrm{aac}$: for $\mathrm{c}$, $[4 + 0, 4 + 2) = [4, 6)$; for $\mathrm{a}$, $\mathrm{Occ}(\mathrm{a}, 4) = 1$ and $\mathrm{Occ}(\mathrm{a}, 6) = 3$, giving $[1 + 1, 1 + 3) = [2, 4)$, the rows beginning with $\mathrm{ac}$; for the second $\mathrm{a}$, $\mathrm{Occ}(\mathrm{a}, 2) = 0$ and $\mathrm{Occ}(\mathrm{a}, 4) = 1$, giving $[1, 2)$. One occurrence, in row $1$, whose suffix-array entry is $2$: $\mathrm{aac}$ starts at position $2$ of $T$.

![The Burrows–Wheeler transform of T = acaacg followed by the sentinel, and backward search for P = aac. A: the sorted rotations (rows i), the suffix array SA, the first column F and the last column L, which is the BWT of T. B–D: backward search processes P from its last letter; at each step the interval of rows from sp to ep (exclusive) is updated by sp ← C(c) + Occ(c, sp) and ep ← C(c) + Occ(c, ep), and the shaded rows are those whose rotations begin with the part of P processed so far: c, then ac, then aac, which occurs once, in row 1 (text position 2)](./plots/bwt-backward-search.py)

The following implementation keeps full $\mathrm{Occ}$ tables for clarity; it returns the results shown in the comments.

```python
def suffix_array(t):
    """Suffix array by sorting (O(n^2 log n); real tools use O(n) algorithms such as SA-IS)."""
    return sorted(range(len(t)), key=lambda i: t[i:])

class FMIndex:
    def __init__(self, text, sa_step=4):
        t = text + "$"
        sa = suffix_array(t)
        self.L = "".join(t[i - 1] for i in sa)      # t[-1] is "$" when sa[i] == 0
        self.n = len(t)
        alphabet = sorted(set(t))
        self.C, total = {}, 0                        # C[c]: symbols of t smaller than c
        for c in alphabet:
            self.C[c] = total
            total += t.count(c)
        self.occ = {c: [0] * (self.n + 1) for c in alphabet}   # occ[c][i]: c in L[0:i]
        for i, ch in enumerate(self.L):
            for c in alphabet:
                self.occ[c][i + 1] = self.occ[c][i] + (ch == c)
        self.ssa = {i: p for i, p in enumerate(sa) if p % sa_step == 0}   # sampled SA

    def lf(self, i):
        c = self.L[i]
        return self.C[c] + self.occ[c][i]

    def backward_search(self, p):
        sp, ep = 0, self.n
        for c in reversed(p):
            if c not in self.C:
                return 0, 0
            sp, ep = self.C[c] + self.occ[c][sp], self.C[c] + self.occ[c][ep]
            if sp >= ep:
                return 0, 0
        return sp, ep

    def locate(self, i):
        steps = 0
        while i not in self.ssa:
            i, steps = self.lf(i), steps + 1
        return self.ssa[i] + steps

    def find(self, p):
        sp, ep = self.backward_search(p)
        return sorted(self.locate(i) for i in range(sp, ep))

fm = FMIndex("acaacg")
print(fm.L)                                  # gc$aaac
print(fm.backward_search("aac"), fm.find("aac"))   # (1, 2) [2]
print(fm.backward_search("ac"), fm.find("ac"))     # (2, 4) [0, 3]
```

**Example 10.2.2 (The Size of a Human FM-Index)** An index of both strands of the human genome covers $n = 6.2\times10^9$ symbols. The BWT at $2$ bits per base takes $1.55\,\mathrm{GB}$; occurrence counts for the four bases stored as $32$-bit integers at checkpoints every $128$ symbols take $6.2\times10^9/128 \times 16$ bytes $= 0.78\,\mathrm{GB}$; a suffix array sampled every $32$ positions with $8$-byte entries takes $1.55\,\mathrm{GB}$. The total, about $4\,\mathrm{GB}$, is a third of an uncompressed suffix array of one strand, and the parameters $b$ and $s$ trade memory for time. This is why FM-index mappers such as BWA and Bowtie2 run on ordinary computers with a few gigabytes of memory, and why the BWT made genome-scale resequencing routine around 2009.

### 10.2.5. Inexact Matching

Backward search finds exact matches only. Bowtie (2009) allowed a few mismatches by backtracking: when the interval becomes empty, it tries the other three bases at recent positions, preferring positions with low base quality, at a cost that grows exponentially with the number of mismatches allowed; a second index of the reversed genome lets the search start from whichever half of the read is more likely to be exact. The approach of BWA-MEM is to find exact seeds of maximal length instead.

**Definition 10.2.3 (Super-Maximal Exact Match)** A *maximal exact match* (MEM) between a read and a reference is an exact match of a substring of the read with the reference that cannot be extended to the left or right on either. A **super-maximal exact match** (SMEM) is a MEM whose substring of the read is not contained in the substring of any other MEM.

SMEMs covering each read position are found with a bidirectional FM-index (an index of the genome together with its reverse, or of both strands), which can extend a match by one symbol on either side in constant time. Seeds of maximal length adapt to the data: in unique sequence they are long and have one occurrence, in repeats they have many and are reseeded as shorter matches or skipped.

## 10.3. Aligners

### 10.3.1. Short Reads: BWA-MEM and Bowtie2

**Algorithm 10.3.1 (BWA-MEM, Outline)** For each read, or pair of reads (Li, 2013):

1. Seeding: compute the SMEMs of the read with the bidirectional FM-index; reseed long SMEMs that have few occurrences by shorter exact matches that occur more often, to find alternative locations; discard seeds with too many occurrences.
2. Chaining: group seeds that are colinear (in the same order and on the same diagonal band in read and reference) into chains, and drop chains largely contained in better ones.
3. Extension: from the ends of the seeds of each chain, extend by banded **dynamic programming** with an **affine gap penalty**, stopping when the score falls too far below the best (a Z-drop, the gapped analogue of the X-drop of [7.8.4](/7.8.4#sec-4.3.2)); bases at the read ends that do not align well are soft-clipped (Section 10.5).
4. Pairing: estimate the insert-size distribution from confidently mapped pairs; choose for each pair the combination of mate alignments maximizing the sum of their scores and a penalty for improbable insert sizes, and if a mate is unmapped, search the window where it should lie by Smith–Waterman alignment (mate rescue).
5. Report the best alignment with its mapping quality (Section 10.4), alternative hits as secondary alignments, and parts of a chimeric read aligned elsewhere as supplementary alignments.

The default scores of BWA-MEM are match $+1$, mismatch $-4$, gap open $-6$ and extension $-1$ per base, and a clipping penalty of $5$ at each end, so that a read is clipped rather than aligned through a cluster of mismatches at its end. Bowtie2 combines FM-index seeds with SIMD-accelerated dynamic programming and offers an *end-to-end* mode, in which the whole read must align, and a *local* mode with soft clipping. BWA-MEM2 reimplements BWA-MEM with vectorized code and a different index layout, giving identical output two to three times faster; the hardware-accelerated DRAGEN platform maps a $30\times$ genome in under an hour.

```bash
# Index the reference once (several hours and about 5 GB for GRCh38), then map, sort and index
bwa-mem2 index GRCh38.fa
bwa-mem2 mem -t 16 -R '@RG\tID:HG002\tSM:HG002\tPL:ILLUMINA' GRCh38.fa \
    trim_R1.fq.gz trim_R2.fq.gz | samtools sort -@ 8 -o HG002.bam -
samtools index HG002.bam
# The amplicon panel: single-end 50-nt reads against the panel's target sequences (MGI358.SNP.fa)
bwa-mem2 index MGI358.SNP.fa
bwa-mem2 mem -M -Y -t 8 MGI358.SNP.fa my.clean.fq.gz | samtools sort -@ 7 -o my.bam -
```

The read-group line (`-R`) records the sample and library; variant callers use it to keep samples apart and to model errors per library ([7.8.12](/7.8.12)). For the panel, `-Y` soft-clips supplementary alignments and `-M` marks split hits as secondary for compatibility with older tools; the reference is the set of $214$ target sequences of the panel ($445\,923$ bases) rather than the whole genome, which makes mapping fast but forces reads from paralogous sequence outside the targets onto them, a reminder that a reduced reference changes what "best position" means.

### 10.3.2. Long Reads: Minimizers and Chaining

Long reads ($10$ kb to over $1$ Mb) with errors of $1$–$10\,\%$ need a different strategy: exact seeds of $20$–$30$ nt still occur, but a read contains thousands of them, and the alignment of a long read is dominated by finding the right chain of seeds and by base-level alignment in the gaps between them.

**Definition 10.3.1 (Minimizer)** Given a total order on $k$-mers (in practice the order of a hash function applied to the canonical $k$-mer), the $(w, k)$-**minimizer** of a window of $w$ consecutive $k$-mers of a sequence is its smallest $k$-mer. The minimizers of a sequence are the $k$-mers that are the minimizer of at least one of its windows (Roberts and colleagues, 2004; Schleimer and colleagues, 2003, as *winnowing*).

Two sequences that share an exact substring of length $w + k - 1$ share the window of $w$ $k$-mers it contains, hence its minimizer: minimizers are a sample of the $k$-mers that is guaranteed to include a common seed for every sufficiently long exact match. Consecutive windows usually share their minimum, so the sample is sparse.

**Formula 10.3.1 (Minimizer Density)** For a random sequence and a random order on $k$-mers, with $k$ large enough that $k$-mers in a window are distinct, the expected fraction of $k$-mer positions that are minimizers is approximately
$$
\frac{2}{w + 1}.
$$
A new minimizer is selected when the window advances by one position only if the newly entering $k$-mer is the minimum of the new window (probability $1/w$ per window of $w$ $k$-mers) or the outgoing one was the minimum of the old window ($1/w$ similarly); each of the $w + 1$ $k$-mers spanned by two consecutive windows is equally likely to be the minimum of their union, which gives the exact value $2/(w + 1)$ for the probability that the two windows choose different $k$-mers.

![Minimizer sampling. A: the (w, k) = (6, 5) minimizers of a 60-nt random sequence; each window of six consecutive 5-mers selects its 5-mer of smallest hash value, and the bars mark the selected 5-mers (13 of 56, density 0.23, against 2/(w + 1) = 0.29 expected over long sequences). Any substring of w + k − 1 = 10 nt shared by two sequences gives them a common minimizer. B: density on a 200 kb random sequence with k = 15 against the window size, for a random hash order (circles, on the curve 2/(w + 1)) and for lexicographic order (squares, systematically denser because k-mers beginning with runs of A are chosen in clusters)](./plots/minimizers.py)

**Example 10.3.1** minimap2 uses $k = 15$, $w = 10$ for nanopore reads, $k = 19$, $w = 19$ for HiFi reads and $k = 21$, $w = 11$ for short reads. With $w = 10$, a random sequence keeps $2/11 = 18.2\,\%$ of its $k$-mers; on $200$ kb of random sequence the measured density is $18.1\,\%$ with a random hash order and $19.7\,\%$ with lexicographic order. For the human genome the index of $(10, 15)$-minimizers holds about $5.6\times10^8$ entries instead of $3.1\times10^9$.

**Algorithm 10.3.2 (Colinear Chaining)** Input: anchors (matching minimizers) $i = 1, \dots, N$, each with read position $x_i$, reference position $y_i$ and length $w_i$, sorted by reference position. Let $f(i)$ be the best score of a chain ending at anchor $i$:
$$
f(i) = \max\Bigl\{w_i,\; \max_{j < i,\; x_j < x_i,\; y_j < y_i}\bigl[f(j) + \alpha(j, i) - \beta(j, i)\bigr]\Bigr\},
$$
where $\alpha(j, i) = \min\{x_i - x_j, y_i - y_j, w_i\}$ is the number of new matching bases and $\beta(j, i)$ a gap cost that grows with the difference of the distances on read and reference, $\lvert(x_i - x_j) - (y_i - y_j)\rvert$, and with their size. Report the chains of highest score by backtracking from the maxima of $f$.

The exact recursion takes $O(N^2)$ time; minimap2 examines only the $h$ preceding anchors (about $50$), giving $O(hN)$, and newer versions refine the result by a range-maximum-query formulation with better guarantees. The base-level alignment between anchors is filled by banded dynamic programming with a two-piece affine gap cost, which penalizes long gaps less than an affine cost does and suits the long deletions of structural variants and introns.

```bash
minimap2 -ax map-hifi -t 16 GRCh38.fa HG002.hifi.fq.gz | samtools sort -o HG002.hifi.bam -
minimap2 -ax map-ont  -t 16 GRCh38.fa HG002.ont.fq.gz  | samtools sort -o HG002.ont.bam -
minimap2 -cx asm5 GRCh38.fa assembly.fa > asm_vs_ref.paf      # whole-assembly alignment (7.8.11)
```

### 10.3.3. Spliced Alignment

**Definition 10.3.2 (Spliced Alignment)** A **spliced alignment** of an RNA-derived read to a genome is an alignment in which the read is split into segments that align to the genome in order, separated by long reference skips (introns) that are not penalized as deletions, but scored by the plausibility of their boundaries (the canonical GT…AG dinucleotides and annotated **5′ splice sites** and **3′ splice sites**).

STAR finds, from each read position, the *maximal mappable prefix*, the longest prefix of the rest of the read that matches the genome exactly, by binary search in an uncompressed suffix array; a read spanning an exon junction yields two maximal mappable prefixes that are then stitched together with a junction. HISAT2 uses a hierarchical graph FM-index: one global index and tens of thousands of small local indexes of overlapping genome segments, which keep the extension of short anchors across junctions local and fast, with known variants and splice sites built into the graph. Long cDNA and direct RNA reads are aligned with `minimap2 -ax splice`. Quantification of expression, often by *pseudoalignment*, which assigns reads to compatible transcripts without base-level alignment, is part of [7.9](/7.9).

### 10.3.4. Graph References

A linear reference contains one allele at each variable site, so reads carrying the other allele, especially at indels and structural variants, align with penalties or not at all. Aligning to a **pangenome** graph ([7.4.14](/7.4.14#sec-14.2.3)) whose paths include common haplotypes (vg giraffe for short reads; GraphAligner and minigraph for long reads) removes much of this reference bias and is the basis of the pangenome references of [7.8.11](/7.8.11). The alignment is then a path in a graph rather than an interval of a string, and coordinates are projected back to a linear reference for downstream tools.

## 10.4. How Certain Is a Position?

### 10.4.1. Mapping Quality

**Definition 10.4.1 (Mapping Quality)** The **mapping quality** (MAPQ) of an alignment is the Phred-scaled probability that the reported position is wrong:
$$
\mathrm{MAPQ} = -10\log_{10}\mathbb{P}(\text{the read does not come from the reported position}).
$$
The value $255$ means that it is not available.

**Formula 10.4.1 (Mapping Posterior)** Suppose a read $r$ with base error probabilities $p_1, \dots, p_L$ has candidate positions $u = 1, \dots, U$ in the genome, and at candidate $u$ its alignment mismatches the reference at the set $M_u$ of read positions. If errors are independent and every candidate is a priori equally likely to be the source, the likelihood of candidate $u$ is
$$
\mathbb{P}(r \mid u) = \prod_{i \in M_u}\frac{p_i}{3}\prod_{i \notin M_u}(1 - p_i),
$$
and by **Bayes' theorem** the posterior probability of the best candidate $u^*$ is $\mathbb{P}(r \mid u^*)/\sum_u\mathbb{P}(r \mid u)$, so that $\mathrm{MAPQ} = -10\log_{10}\bigl[1 - \mathbb{P}(r \mid u^*)/\sum_u\mathbb{P}(r \mid u)\bigr]$.

Every extra mismatch at a base of quality $Q$ multiplies the likelihood by $(p/3)/(1 - p)$, so the comparison between the best and the second-best candidates is a sum over the bases where they differ.

**Example 10.4.1** A read aligns at its best position with one mismatch.

- If the second-best position has one additional mismatch at a Q$30$ base, the likelihood ratio is $(0.001/3)/0.999 = 3.34\times10^{-4}$, the posterior error $3.34\times10^{-4}$, and MAPQ $= 34.8$.
- If the extra mismatch is at a Q$20$ base, the ratio is $(0.01/3)/0.99 = 3.37\times10^{-3}$ and MAPQ $= 24.7$: a low-quality base is weak evidence against a position.
- With two extra Q$30$ mismatches, MAPQ $= 69.5$; mappers cap values (BWA at $60$) because the model ignores candidates that were never found and variants of the sample.
- If two positions are identical over the read, the posterior is $1/2$ and MAPQ $= 3.0$; for three copies, $-10\log_{10}(2/3) = 1.8$. BWA reports $0$ for any read with an equally good alternative, and the position chosen among them is random.

The posterior is calibrated only if the model is right: if base qualities are wrong, or candidates are missed, MAPQ misstates the error rate. Mappers approximate the sum over candidates from the scores of the best and second-best alignments and the number of suboptimal hits, with empirical corrections, and MAPQ values of different mappers are not on the same scale. Variant callers ([7.8.12](/7.8.12)) use MAPQ to weight or discard reads (a common filter is MAPQ $\ge 20$ or $30$), so both overconfidence (false variants from mismapped paralogs) and underconfidence (lost data) matter.

![Mapping quality on a simulated genome with repeats (300 kb random sequence carrying 80 copies of a 1.5 kb repeat diverged by 0–2 % from its consensus and 5 identical copies of a 1 kb duplication; 40 000 reads of 100 nt with qualities Q20, Q30 or Q37 and errors at those rates; mapping by five exact 20-mer seeds per read, which by Theorem 10.1.1 always find a source with up to four differences, and ungapped scoring of every candidate). A: reported MAPQ against the empirical error rate in bins; with the posterior of Formula 10.4.1 (blue) the points lie on the diagonal, whereas ignoring base qualities and treating all bases as Q20 (red) misstates the confidence. Triangles are bins without a single wrongly placed read, for which only a bound can be given. B: distribution of MAPQ by the origin of the read: reads from unique sequence are all placed correctly at MAPQ 60; reads from repeat copies take every value, and reads from identical copies have MAPQ near 0](./plots/mapq-calibration.py)

### 10.4.2. Mappability and Reference Bias

The *mappability* of a position for reads of length $L$ is the fraction of reads covering it that can be placed uniquely; it is computed by mapping all $L$-mers of the reference back to itself. Low mappability marks segmental duplications, recent transposable elements, centromeric satellites and genes with close **pseudogenes**; analyses report "callable" regions and exclude blacklisted ones where artefactual signal accumulates. Longer reads and pairs raise mappability, which is one reason the complete T2T-CHM13 reference and long reads add correctly placed data in medically relevant genes that GRCh38 short-read pipelines miss. Reference bias is the complementary error: reads carrying a non-reference allele have one more mismatch and slightly lower alignment scores, so at heterozygous sites slightly fewer of them are mapped, and alleles at indels and divergent haplotypes are undercounted; variant callers that realign reads locally ([7.8.12](/7.8.12)) and graph references reduce it.

## 10.5. Alignment Files

### 10.5.1. The SAM Format

**Definition 10.5.1 (SAM Format)** The **SAM format** (Sequence Alignment/Map; Li and colleagues, 2009) stores read alignments as tab-separated text: a header of lines beginning with `@` (`@HD` version and sort order, `@SQ` names and lengths of the reference sequences, `@RG` read groups, `@PG` programs), followed by one line per alignment with eleven mandatory fields and optional typed tags `TAG:TYPE:VALUE`. *BAM* is its compressed binary form in BGZF blocks ([7.8.1](/7.8.1#sec-1.4.5)), and *CRAM* stores reads as differences from the reference sequence with column-wise compression of the other fields.

| Field | Name | Content |
|---|---|---|
| 1 | QNAME | read name |
| 2 | FLAG | bitwise flags (below) |
| 3 | RNAME | reference sequence name |
| 4 | POS | one-based leftmost position of the aligned part |
| 5 | MAPQ | mapping quality (Definition 10.4.1) |
| 6 | CIGAR | alignment operations (Definition 10.5.2) |
| 7 | RNEXT | reference of the mate (`=` if the same) |
| 8 | PNEXT | position of the mate |
| 9 | TLEN | signed observed template length |
| 10 | SEQ | read sequence, on the forward strand of the reference |
| 11 | QUAL | base qualities, Phred+33, in the same orientation |

| Bit | Value | Meaning |
|---|---|---|
| `0x1` | 1 | read is paired |
| `0x2` | 2 | each mate properly aligned (orientation and distance as expected) |
| `0x4` | 4 | read unmapped |
| `0x8` | 8 | mate unmapped |
| `0x10` | 16 | read aligned to the reverse strand (SEQ is reverse-complemented) |
| `0x20` | 32 | mate on the reverse strand |
| `0x40` | 64 | first read of the pair |
| `0x80` | 128 | second read of the pair |
| `0x100` | 256 | secondary alignment |
| `0x200` | 512 | failed quality checks |
| `0x400` | 1024 | PCR or optical duplicate |
| `0x800` | 2048 | supplementary alignment (part of a chimeric read) |

**Example 10.5.1** A properly paired forward first mate has FLAG $1 + 2 + 32 + 64 = 99$, and its reverse-strand second mate $1 + 2 + 16 + 128 = 147$; the mirror orientation gives $83$ and $163$. A FLAG of $1107 = 1024 + 64 + 16 + 2 + 1$ is a duplicate-marked, reverse-strand first mate of a proper pair. `samtools view -F 0x904` keeps primary mapped alignments by excluding unmapped ($4$), secondary ($256$) and supplementary ($2048$) records; `-f 4` selects the unmapped reads.

**Definition 10.5.2 (CIGAR String)** A **CIGAR string** encodes an alignment as a sequence of lengths and operations: `M` aligned (match or mismatch), `=` match, `X` mismatch, `I` insertion in the read, `D` deletion from the read, `N` skipped reference region (an intron), `S` soft clip (bases present in SEQ but not aligned), `H` hard clip (bases removed from SEQ), `P` padding. The operations `M`, `=`, `X`, `D` and `N` consume reference positions; `M`, `=`, `X`, `I` and `S` consume read bases.

The aligned span on the reference is the sum of the lengths of the reference-consuming operations, so a record's end coordinate is computed from POS and CIGAR. The optional tags `NM` (edit distance of the aligned part) and `MD` (the reference bases at mismatches and deletions) let tools reconstruct the reference sequence of the alignment without the reference; `AS` and `XS` give the best and second-best alignment scores, and `SA` lists the supplementary parts of a chimeric read.

![Anatomy of an alignment record. A 30-nt read aligned to the reference from one-based position 101: three soft-clipped bases (lower case; kept in SEQ but not aligned, for example an adapter remnant), 8 aligned bases containing one mismatch (T for the reference A at position 106), 2 bases inserted in the read, 7 aligned bases, a deletion of the reference bases AG at positions 116–117, and 10 aligned bases. The CIGAR string is 3S8M2I7M2D10M, the edit distance NM = 1 + 2 + 2 = 5, and MD = 5A9^AG10 records 5 matching bases, the reference A, 9 matches, the deleted AG and 10 matches; the alignment spans 8 + 7 + 2 + 10 = 27 reference bases, positions 101–127](./plots/cigar-anatomy.py)

```python
import pysam

REF_OPS = {0, 2, 3, 7, 8}          # M, D, N, =, X consume the reference

def reference_end(pos1, cigartuples):
    """One-based closed end coordinate of an alignment from POS and CIGAR (op, length) pairs."""
    return pos1 + sum(n for op, n in cigartuples if op in REF_OPS) - 1

print(reference_end(101, [(4, 3), (0, 8), (1, 2), (0, 7), (2, 2), (0, 10)]))   # 127

# Reads covering rs4988235 (GRCh38 chr2:135851076) and the allele each carries at that base
with pysam.AlignmentFile("HG002.bam") as bam:
    for col in bam.pileup("chr2", 135851075, 135851076, truncate=True,
                          min_mapping_quality=20, min_base_quality=20):
        alleles = [p.alignment.query_sequence[p.query_position]
                   for p in col.pileups if p.query_position is not None]
        print(col.reference_pos + 1, {a: alleles.count(a) for a in set(alleles)})
```

### 10.5.2. Processing Alignments

```bash
samtools flagstat HG002.bam                     # counts by FLAG: mapped, properly paired, duplicates
samtools idxstats HG002.bam                     # reads per chromosome (sex check, contamination)
samtools view -b -q 20 -F 0x904 HG002.bam chr2:135800000-135900000 > lct.bam
# Duplicate marking: name-group, add mate tags, sort by position, mark duplicates (7.8.9)
samtools collate -O -u HG002.bam | samtools fixmate -m -u - - \
  | samtools sort -u - | samtools markdup -@ 8 - HG002.md.bam
mosdepth -t 8 --by 500 HG002 HG002.md.bam       # depth in 500-bp windows and its distribution
bedtools intersect -a targets.bed -b low_mappability.bed -v > callable_targets.bed
bedtools getfasta -fi GRCh38.fa -bed regions.bed -fo regions.fa
samtools view -C -T GRCh38.fa -o HG002.cram HG002.md.bam    # CRAM needs the same reference to decode
```

Sorting by coordinate makes records of one region adjacent, and the index (`.bai`, `.csi` or `.crai`) uses the binning scheme of [7.8.1](/7.8.1#sec-1.4.5) to jump to a region. Duplicate marking uses the positions of both mates and their orientations (Definition 9.4.1 of [7.8.9](/7.8.9)); for amplicon data it must be skipped, since all reads of an amplicon share their start. CRAM files are decoded only with the exact reference used to write them, so the reference (with its checksum, recorded in the `@SQ` header lines) is part of the data.

### 10.5.3. Genome Browsers

Genome browsers display alignments over annotation tracks. In IGV, reads are drawn as bars with mismatching bases coloured, a coverage track above shows the allele fractions at positions where non-reference bases exceed a threshold, and pairs whose insert is larger than expected (a deletion between the mates) or smaller (an insertion) are coloured, red and blue by default; reads with MAPQ $0$ are drawn transparent. At rs4988235 in a heterozygous sample, the coverage bar splits into reference G and alternative A at roughly equal heights on the forward strand of the reference, the C and T of the *LCT* transcript on the minus strand ([7.8.1](/7.8.1)). The UCSC and Ensembl browsers ([7.8.2](/7.8.2)) display remote BAM or CRAM files by URL together with their own annotation and conservation tracks.

## 10.6. Application: Searching for CRISPR Off-Target Sites

A Cas9 nuclease is directed by the 20-nt spacer of a **single guide RNA** to a **protospacer** followed by a **protospacer adjacent motif** (NGG for SpCas9), and it also cleaves sites that match imperfectly, mostly with mismatches far from the PAM ([7.2.24](/7.2.24#sec-24.4.2)); such cleavage is an **off-target effect** ([7.2.24](/7.2.24#sec-24.8.1)). Designing a guide therefore includes a search of the genome for all sites within a few mismatches, and possibly DNA or RNA bulges (a base unpaired on one side), of the guide followed by a permissible PAM. This is read mapping turned around: one short query, a small number of differences, and the need for all hits rather than the best.

**Formula 10.6.1 (Chance Off-Target Sites)** The number of $\ell$-mers within Hamming distance $d$ of a given $\ell$-mer is $N_\ell(d) = \sum_{j=0}^{d}\binom{\ell}{j}3^j$. In a random genome of length $G$, on both strands, with a PAM of probability $\pi$ (for NGG, $\pi = 1/16$), the expected number of sites within $d$ mismatches of a guide of length $\ell$ followed by a PAM is
$$
2G\pi\,\frac{N_\ell(d)}{4^\ell}.
$$

**Example 10.6.1** For $\ell = 20$ and $G = 3.1\times10^9$, $N_{20}(d) = 1, 61, 1771, 32\,551, 424\,996$ for $d = 0, \dots, 4$, and the expected number of chance NGG sites is $3.5\times10^{-4}$, $0.021$, $0.62$, $11.5$ and $150$. A guide unique to the genome is therefore expected to have about a dozen sites with three mismatches and more than a hundred with four. Real genomes are not random: guides in repeats have thousands of exact matches, which is why design tools discard them first. A shorter guide is less specific: at $d \le 3$ an $18$-nt guide has $132$ expected chance sites and a $16$-nt guide $1466$.

![Expected numbers of sites resembling a guide by chance in a random 3.1 Gb genome (both strands, NGG PAM at one in 16 positions; Formula 10.6.1). A: for a 20-nt guide, the expected number of sites with at most d mismatches rises from 0.00035 for exact matches to 11 for d = 3 and 150 for d = 4. B: for d ≤ 3, against the guide length; the dashed line marks one expected site. Real genomes contain repeats and are not random, so the real numbers depend on the guide](./plots/off-target-counts.py)

Exhaustive search is practical because the genome is scanned once: Cas-OFFinder compares the guide with every PAM-adjacent position, in parallel on a GPU, allowing a set number of mismatches and bulges. Index-based methods use the FM-index with backtracking or the pigeonhole bound: for $d = 3$ mismatches in $20$ nt, one of four $5$-nt pieces must match exactly, which is too short to be selective, so tools combine the PAM with a longer exact seed next to it (the PAM-proximal $10$–$12$ nt, where mismatches are least tolerated) and verify candidates by direct comparison. Candidates are then ranked by empirically derived scores of how mismatch position and type reduce cleavage (the MIT and CFD scores), and the most likely sites are checked experimentally by the assays of [7.2.24](/7.2.24#sec-24.8.1). Predicting the efficiency of a guide and the repair outcome at its target are learning problems treated in [7.8.15](/7.8.15).

```bash
# Cas-OFFinder input: genome directory, pattern (20 N + NGG), then guides with allowed mismatches
cat > input.txt <<'EOF'
GRCh38_chromosomes/
NNNNNNNNNNNNNNNNNNNNNGG
GCTAAAGACAATTACATAACNNN 4
EOF
cas-offinder input.txt G off_targets.txt         # G: run on the GPU
```

## Summary

| Topic | Key points |
|---|---|
| Problem | $6.2\times10^8$ reads per $30\times$ genome; Smith–Waterman against the genome would take about $90$ years; read mapping (Definition 10.1.1) finds the position, semi-global alignment and confidence |
| Seeds | seed and extend; pigeonhole bound: $k$ edits leave an exact match of $\lfloor L/(k+1)\rfloor$ (Theorem 10.1.1); chance hits $2G/4^s$ (Formula 10.1.1); repeats limit seed occurrences |
| Indexes | hash tables of $k$-mers (fast, large); suffix arrays and binary search ($32$ bits per base); BWT (Definition 10.2.1), LF mapping (Theorem 10.2.1) and inversion; FM-index (Definition 10.2.2) with backward search (Algorithm 10.2.1) in $O(m)$ and locating by sampled SA (Theorem 10.2.2); about $4\,\mathrm{GB}$ for both strands of the human genome (Example 10.2.2) |
| Short reads | SMEMs (Definition 10.2.3), chaining, banded affine extension with Z-drop, pairing and mate rescue in BWA-MEM (Algorithm 10.3.1); Bowtie2 end-to-end and local modes |
| Long reads | minimizers (Definition 10.3.1) with density $2/(w + 1)$ (Formula 10.3.1); colinear chaining by dynamic programming (Algorithm 10.3.2); minimap2 presets |
| Splicing and graphs | spliced alignment (Definition 10.3.2): STAR (maximal mappable prefixes, suffix array), HISAT2 (graph FM-index), minimap2 splice; pangenome graphs against reference bias |
| Confidence | MAPQ $= -10\log_{10}\mathbb{P}(\text{wrong})$ (Definition 10.4.1) from the posterior over candidates (Formula 10.4.1); repeats give MAPQ near $0$; calibration requires correct qualities; mappability and reference bias |
| Files | SAM fields, FLAG bits (99, 147, 83, 163), CIGAR operations and which consume read or reference (Definitions 10.5.1, 10.5.2), NM and MD; sort, index, markdup, flagstat, depth, CRAM with its reference |
| Off-target search | guide + PAM within $d$ mismatches; $2G\pi N_\ell(d)/4^\ell$ chance sites, about $11$ at $d = 3$ for $20$ nt (Formula 10.6.1); exhaustive (Cas-OFFinder) or seeded index search; ranking by cleavage scores |

## Questions

1. Compute the BWT of $T = \mathrm{banana}\char36$ and use backward search to count the occurrences of $\mathrm{ana}$.

   **Answer** The sorted suffixes are $\mathrm{}\char36$ ($6$), $\mathrm{a}\char36$ ($5$), $\mathrm{ana}\char36$ ($3$), $\mathrm{anana}\char36$ ($1$), $\mathrm{banana}\char36$ ($0$), $\mathrm{na}\char36$ ($4$), $\mathrm{nana}\char36$ ($2$), so $\mathrm{SA} = (6, 5, 3, 1, 0, 4, 2)$ and $L = \mathrm{annb}\char36\mathrm{aa}$. $C[\mathrm{}\char36] = 0$, $C[\mathrm{a}] = 1$, $C[\mathrm{b}] = 4$, $C[\mathrm{n}] = 5$. Backward search for $\mathrm{ana}$: last $\mathrm{a}$: $[1, 4)$; $\mathrm{n}$: $\mathrm{Occ}(\mathrm{n}, 1) = 0$, $\mathrm{Occ}(\mathrm{n}, 4) = 2$, giving $[5, 7)$; $\mathrm{a}$: $\mathrm{Occ}(\mathrm{a}, 5) = 1$, $\mathrm{Occ}(\mathrm{a}, 7) = 3$, giving $[2, 4)$. Two occurrences, rows $2$ and $3$, at positions $\mathrm{SA}[2] = 3$ and $\mathrm{SA}[3] = 1$.

2. Invert $L = \mathrm{gc}\char36\mathrm{aaac}$ by LF mapping and check that it gives $\mathrm{acaacg}$.

   **Answer** $C$ as in Example 10.2.1; the ranks of the symbols of $L$ among equal symbols are $\mathrm{g}_0, \mathrm{c}_0, \mathrm{}\char36_0, \mathrm{a}_0, \mathrm{a}_1, \mathrm{a}_2, \mathrm{c}_1$. Start at row $0$: output $L[0] = \mathrm{g}$, go to $C[\mathrm{g}] + 0 = 6$; output $L[6] = \mathrm{c}$, go to $4 + 1 = 5$; output $\mathrm{a}$, go to $1 + 2 = 3$; output $\mathrm{a}$, go to $1 + 0 = 1$; output $\mathrm{c}$, go to $4 + 0 = 4$; output $\mathrm{a}$, go to $1 + 1 = 2$, which holds $\mathrm{}\char36$. The output $\mathrm{gcaaca}$ read backwards is $\mathrm{acaacg}$.

3. Why does an FM-index need a sampled suffix array, and what is the trade-off in choosing the sampling step $s$?

   **Answer** Backward search yields rows of the Burrows–Wheeler matrix, not text positions; converting a row to a position needs $\mathrm{SA}[i]$. Storing the whole array costs $4$–$8$ bytes per base, more than the BWT itself, so only entries at text positions divisible by $s$ are kept, and the position of any row is found by at most $s - 1$ LF steps (Theorem 10.2.2). Memory falls as $1/s$ and the time to locate each hit grows as $s$; mappers that locate few hits per read use $s = 32$ or more, while applications that enumerate all occurrences of many patterns choose smaller $s$.

4. A $100$-nt read is to be found with at most $3$ mismatches. What seed length does the pigeonhole principle guarantee, how many chance hits does such a seed have in a random $3.1$ Gb genome, and why do mappers not rely on this guarantee alone?

   **Answer** Four pieces of $25$ nt; one matches exactly (Theorem 10.1.1). By Formula 10.1.1, $2 \times 3.1\times10^9/4^{25} = 5.5\times10^{-6}$ chance hits, so in unique sequence the seed is perfectly specific. But the guarantee requires all four pieces to be looked up and fails if the read contains an indel near a piece boundary in a way that shifts it (it is still covered, since an indel touches one piece), or more differences than assumed, as at a cluster of variants; and in repeats the exact $25$-mers occur many times. Mappers therefore use variable-length maximal seeds, several per read, reseeding and a limit on occurrences, and accept a small probability of missing alignments with many differences.

5. A read has its best alignment with no mismatches, a second alignment with one mismatch at a Q$35$ base, and a third with two mismatches at Q$30$ bases. Compute the MAPQ of the best alignment by Formula 10.4.1.

   **Answer** Relative likelihoods: best $1$; second $(10^{-3.5}/3)/(1 - 10^{-3.5}) = 1.054\times10^{-4}$; third $(3.336\times10^{-4})^2 = 1.11\times10^{-7}$. Posterior error $= (1.054\times10^{-4} + 1.11\times10^{-7})/(1 + 1.055\times10^{-4}) = 1.055\times10^{-4}$, MAPQ $= 39.8$. The third candidate barely matters; the second one, differing at one high-quality base, determines the value.

6. Decode the FLAG values $83$, $163$ and $2145$, and write a `samtools view` filter that keeps only primary, mapped, non-duplicate reads in proper pairs.

   **Answer** $83 = 64 + 16 + 2 + 1$: paired, proper pair, read on the reverse strand, first mate. $163 = 128 + 32 + 2 + 1$: paired, proper, mate on the reverse strand, second mate; these two form a proper pair in the "reverse first" orientation. $2145 = 2048 + 64 + 32 + 1$: a supplementary alignment of a first mate whose mate is on the reverse strand, not properly paired. Filter: `samtools view -f 0x2 -F 0xD0C`, requiring bit $2$ and excluding $4 + 8 + 256 + 1024 + 2048 = 3340 = \mathrm{0xD0C}$ (unmapped read or mate, secondary, duplicate, supplementary).

7. A spliced RNA-seq read has POS $= 5000$ and CIGAR `40M1200N60M`, and its mate has `2S98M`. What reference interval does the first read cover, how long is the intron, and why must variant callers treat `N` differently from `D`?

   **Answer** Reference-consuming lengths: $40 + 1200 + 60 = 1300$, so the read spans $5000$–$6299$, with aligned blocks $5000$–$5039$ and $6240$–$6299$ and an intron of $1200$ bases ($5040$–$6239$). The mate's two soft-clipped bases are not aligned, and it covers $98$ reference positions. `N` means the bases are absent from the transcript, not deleted from the genome: a variant caller that counted `N` as a deletion would report every intron as a homozygous deletion, and the depth over introns must not count these reads. Callers for RNA-seq data split reads at `N` operations before calling.

8. Show that consecutive windows of $w$ $k$-mers choose different minimizers with probability $2/(w + 1)$ under a random order, and explain why a lexicographic order is worse on real genomes.

   **Answer** Two consecutive windows together contain $w + 1$ distinct $k$-mers (positions $i, \dots, i + w$). Under a random order each is equally likely to be the smallest of the union. If the minimum of the union lies at an inner position $i + 1, \dots, i + w - 1$, both windows contain it and choose it; if it is the first $k$-mer ($i$), the second window chooses something else, and if it is the last ($i + w$), the first window chooses something else. So the choices differ with probability $2/(w + 1)$, and the expected density is $2/(w + 1)$ as in Formula 10.3.1. Under lexicographic order, $k$-mers starting with runs of A are minimal; in a run of A (common in real genomes, poly-A tails of transposons) many overlapping windows choose different but adjacent $k$-mers, raising the density, and minimizers concentrate in low-complexity sequence, where they are least informative. The measured density at $w = 10$ in Figure B is $19.7\,\%$ against $18.1\,\%$ with hashing even on random sequence.

9. Why does a mapper report MAPQ $0$ for a read from one of two identical copies of a segmental duplication, and what are the consequences for detecting a heterozygous variant in one copy? What data would help?

   **Answer** The two positions have identical likelihoods, so the posterior of either is $1/2$ (MAPQ $3$, reported as $0$ by BWA), and the read is placed at random. Reads from both copies are split between them, so a heterozygous variant in copy 1 appears at an allele fraction of about $1/4$ in each copy (half the reads of copy 1 carry it and they are mixed with copy 2's reads), and most callers filter MAPQ-$0$ reads anyway, so the variant is either missed or attributed to the wrong copy. Long reads, linked reads or longer inserts that anchor in unique flanking sequence, paralog-specific variants used as markers, and calling with copy-number-aware models (or on a pangenome) resolve such loci, as for *SMN1*/*SMN2*.

10. (Design) A guide RNA for a therapeutic edit has, by exhaustive search, no other site with fewer than three mismatches, two sites with three mismatches in the PAM-distal half, and one site with two mismatches in the PAM-proximal seed. Which sites concern you most, and how would you check them?

    **Answer** Cleavage tolerates mismatches far from the PAM much better than in the PAM-proximal $10$–$12$ nt ([7.2.24](/7.2.24#sec-24.4.2)), so the two three-mismatch sites with PAM-distal mismatches are the most likely off-targets despite their larger mismatch count, while the two-mismatch site with seed mismatches is probably cut weakly. Rank them by an empirical score (CFD), check whether they lie in genes or regulatory elements, include bulge-allowing searches (a site with one bulge may be closer than it looks), then test in the cell type of interest: amplicon sequencing of the predicted sites after editing, an unbiased genome-wide break-capture assay to find sites prediction missed, and long-read or whole-genome sequencing of edited clones for large deletions and translocations at the target. Expected chance sites from Formula 10.6.1 (about $11$ at $d = 3$) show that a few such sites are normal and that the decision rests on their measured activity.
