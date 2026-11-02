---
title: Variant Calling and Interpretation
description: "Turning mapped reads into a list of variants and deciding what they mean. Pileups, genotype likelihoods from base qualities and Bayesian genotyping with priors, GQ, QUAL and the PL field; haplotype-based calling by local assembly and pair hidden Markov models, the GATK workflow (duplicate marking, base quality recalibration, GVCFs and joint genotyping, hard filters and VQSR) and deep-learning callers. The VCF format, normalization of indels and multi-allelic records. Evaluating calls against benchmark sets: precision and recall by hap.py, the transition/transversion ratio, heterozygous/homozygous ratio and Mendelian consistency in trios. Structural variants and copy number: the four read signatures, segmentation of depth. Somatic variants: tumour purity, copy number and allele fraction, the power of a read threshold. Annotation with HGVS names and transcript consequences, population frequencies, conservation and computational predictors; the ACMG/AMP classification read as a Bayesian point system; rare-disease diagnosis with trios and phenotype-driven ranking."
---

A mapped read file ([7.8.10](/7.8.10)) is a list of observations; what a genome study needs is a list of differences from the reference and their meaning. The two halves of that task are of different kinds. Calling variants is statistical inference: given the reads at a position, their base qualities and mapping qualities, decide which genotype the sample carries, with a probability attached. Interpreting them is evidence synthesis: given a variant and everything known about the gene, the population and the patient, decide whether it explains a disease. The genetic background is in [7.4.14](/7.4.14#sec-14.7) (classes of variants, exome sequencing, Mendelian disease), [7.4.12](/7.4.12) (how mutations arise), [7.4.21](/7.4.21) (somatic variants in cancer) and [7.4.22](/7.4.22) (allele frequencies); the population-scale handling of the resulting genotypes is in [7.8.13](/7.8.13). This chapter covers calling (12.2–12.3), the file format and its traps (12.4), evaluation against benchmark sets (12.5), structural and copy-number variants (12.6), somatic variants (12.7), annotation and classification (12.8) and rare-disease diagnosis (12.9). The examples are HG002, whose variants are known from a public benchmark, and the lactase-persistence variant rs4988235 in *MCM6*, carried through from [7.8.2](/7.8.2).

## 12.1. What Is Being Called

Variants are classified by size and by whether they are inherited. **Single nucleotide polymorphisms**, **indels** up to about $50$ bases, **structural variants** above that size and **copy-number variants** were defined in [7.4.14](/7.4.14#sec-14.7.1); the methods of this chapter follow that division because the data carry different signals for each. A second division is between germline variants, present in every cell and inherited, and **somatic mutations**, present in some cells only: for a germline variant the possible genotypes of a diploid site are three and their fractions are $0$, $1/2$ or $1$, which is a strong constraint, while a somatic variant may occur at any fraction, so it must be distinguished from errors by depth and by a matched normal sample.

A typical human genome differs from GRCh38 at about $4$–$5$ million positions: roughly $3.5\times10^6$ single-nucleotide variants, $5$–$6\times10^5$ short indels and $2$–$3\times10^4$ structural variants, affecting more bases than all the single-nucleotide variants together. Of these, a few tens of thousands alter protein sequence and a handful are new mutations not present in the parents.

## 12.2. From Reads to Genotypes

### 12.2.1. The Pileup and Genotype Likelihoods

At one position, the data are the bases of the overlapping reads and their qualities, the *pileup*. The first calling programs compared the fraction of non-reference bases with a threshold, which wastes the information in the qualities and cannot express uncertainty.

**Definition 12.2.1 (Genotype Likelihood)** For a diploid site with reference allele $A_0$ and alternative allele $A_1$, and reads contributing bases $b_1, \dots, b_n$ with error probabilities $\varepsilon_1, \dots, \varepsilon_n$, the **genotype likelihood** of a genotype $G$ with alternative-allele fraction $f_G$ ($f = 0$ for $A_0A_0$, $1/2$ for $A_0A_1$, $1$ for $A_1A_1$) is
$$
\mathbb{P}(\text{reads} \mid G) = \prod_{i=1}^{n}\Bigl[f_G\,\mathbb{P}(b_i \mid A_1) + (1 - f_G)\,\mathbb{P}(b_i \mid A_0)\Bigr],
$$
where $\mathbb{P}(b_i \mid A) = 1 - \varepsilon_i$ if $b_i = A$ and $\varepsilon_i/3$ otherwise; each read is assumed to come from either haplotype with probability $1/2$ and to err independently.

**Formula 12.2.1 (Bayesian Genotyping)** With a prior over genotypes built from the heterozygosity $\theta$ (for a human site, $\mathbb{P}(A_0A_1) = \theta \approx 10^{-3}$, $\mathbb{P}(A_1A_1) = \theta/2$, $\mathbb{P}(A_0A_0) = 1 - 3\theta/2$, since under Hardy–Weinberg proportions with a rare allele the heterozygote is twice as likely as the rare homozygote), the posterior is
$$
\mathbb{P}(G \mid \text{reads}) = \frac{\mathbb{P}(\text{reads} \mid G)\,\mathbb{P}(G)}{\sum_{G'}\mathbb{P}(\text{reads} \mid G')\,\mathbb{P}(G')}.
$$
The called genotype is the one with the largest posterior; its *genotype quality* is $\mathrm{GQ} = -10\log_{10}[1 - \mathbb{P}(\hat G \mid \text{reads})]$ (in practice the Phred-scaled difference to the second-best genotype), and the quality of the variant site is $\mathrm{QUAL} = -10\log_{10}\mathbb{P}(A_0A_0 \mid \text{reads})$, the evidence that the site is not homozygous reference.

```python
import numpy as np

EPS, THETA = 1e-3, 1e-3            # per-base error probability and heterozygosity
FRAC = np.array([0.0, 0.5, 1.0])   # alternative-allele fraction of 0/0, 0/1, 1/1
PRIOR = np.array([1 - 1.5 * THETA, THETA, THETA / 2])

def genotype(n_ref, n_alt):
    """Posterior, Phred-scaled likelihoods (PL), called genotype, GQ and QUAL at a biallelic site."""
    p_alt = FRAC * (1 - EPS) + (1 - FRAC) * EPS / 3
    p_ref = FRAC * EPS / 3 + (1 - FRAC) * (1 - EPS)
    loglik = n_ref * np.log(p_ref) + n_alt * np.log(p_alt)
    post = np.exp(loglik + np.log(PRIOR) - (loglik + np.log(PRIOR)).max())
    post /= post.sum()
    pl = np.round(-10 * (loglik - loglik.max()) / np.log(10)).astype(int)
    g = int(np.argmax(post))
    return post, pl, ["0/0", "0/1", "1/1"][g], -10 * np.log10(1 - post[g]), -10 * np.log10(post[0])

post, pl, gt, gq, qual = genotype(6, 4)
print(gt, pl, round(gq, 1), round(qual, 1))       # 0/1 [109 0 179] 79.0 79.0
print(genotype(18, 2)[2:])                        # ('0/0', 20.7, 0.0)
```

**Example 12.2.1** At depth $10$ with four alternative reads of quality Q$30$, the posterior of the heterozygote is $1 - 1.3\times10^{-8}$: the site is called $0/1$ with GQ $79$ and QUAL $79$, and the VCF field `PL` is $109,0,179$. At depth $20$ with only two alternative reads, the posterior of the heterozygote is $0.0086$ and the site is called homozygous reference: two reads out of twenty are better explained by errors ($20 \times 10^{-3}$ expected errors, but concentrated by chance) and by the prior than by a genotype that should give about ten. At depth $4$ with one alternative read, the heterozygote has posterior $0.16$, GQ $8$: such calls are filtered. This is why low-coverage data are genotyped not site by site but with haplotype information from a reference panel ([7.8.13](/7.8.13)).

![Genotype posteriors from read counts (Formula 12.2.1), with per-base error probability 0.001 and prior heterozygosity 0.001. A: for each depth (horizontal) and number of alternative reads (vertical), the colour shows the genotype of highest posterior probability and the shade its genotype quality, capped at 99 as in VCF files; the diagonal boundaries between the regions are where the evidence balances, and pale cells at the boundaries are calls with low GQ. A single alternative read is never enough at any depth, and two are enough only up to depth 14. B: the posterior probability of the heterozygote against the observed alternative-allele fraction for depths 5, 10, 20 and 40; the curves steepen with depth, and at depth 5 even a fraction of 0.2 (one read) leaves the heterozygote improbable](./plots/genotype-posterior.py)

### 12.2.2. Why Sites Cannot Be Treated Independently

Position-by-position calling fails around indels. A read carrying a deletion is often aligned with the deletion placed at a different position in a repeat, or with several mismatches instead, so the evidence is smeared over neighbouring positions; the same is true where two variants lie close together on one haplotype. The remedy is to call haplotypes rather than bases.

**Algorithm 12.2.1 (Haplotype-Based Calling)** For each *active region* of the genome where the reads show evidence of variation (mismatches, indels, soft clips above a threshold):

1. Assemble the reads of the region into a de Bruijn graph ([7.8.11](/7.8.11)) and enumerate the plausible paths; each path is a candidate haplotype, which is aligned to the reference by the **Smith–Waterman algorithm** to yield its set of variants.
2. For each read $r$ and candidate haplotype $H$, compute $\mathbb{P}(r \mid H)$ with a pair hidden Markov model whose emission probabilities come from the base qualities and whose indel transitions come from a model of polymerase slippage ([7.8.5](/7.8.5#sec-5.5.1) treats pair HMMs).
3. For each candidate variant site, marginalize over haplotypes to obtain the genotype likelihoods of Definition 12.2.1, and genotype as in Formula 12.2.1.

This is the scheme of GATK HaplotypeCaller and, with a different assembler, of freebayes, which evaluates haplotypes within a window rather than assembling them. Its benefits are largest for indels, for clustered variants and in regions where mapping has placed reads imperfectly, because step 2 re-evaluates every read against the whole candidate haplotype rather than against the reference base by base.

### 12.2.3. Deep-Learning Callers

DeepVariant turns the pileup at a candidate site into an image-like tensor (channels for base identity, base quality, mapping quality, strand, whether the base matches the reference) and classifies it with a convolutional network into the three genotypes, trained on benchmark samples ([7.8.15](/7.8.15) treats such models). It learns error patterns that hand-built models miss, which is why it was adopted first for platforms whose errors are hardest to model: PacBio HiFi and nanopore reads, where Clair3 and PEPPER-DeepVariant do the same. The cost is that a learned caller is only as good as the samples and platforms it was trained on, and its decisions are harder to audit than a likelihood.

## 12.3. A Germline Workflow

The steps between mapped reads and a filtered call set are stable across pipelines:

1. *Duplicate marking* ([7.8.9](/7.8.9), [7.8.10](/7.8.10)): copies of one molecule must not count as independent evidence.
2. *Base quality score recalibration*: empirical qualities by cycle and context from mismatches at known non-variant sites ([7.8.9](/7.8.9#sec-9.2.3)). It matters because the likelihoods of Definition 12.2.1 multiply those probabilities directly.
3. *Per-sample calling into a GVCF*: a genomic VCF records, in addition to the variant sites, blocks of reference-matching positions with the confidence that no variant is present. This makes the next step possible.
4. *Joint genotyping*: the GVCFs of all samples are combined, and each site is genotyped in all of them with a prior informed by the allele frequency in the cohort. Joint analysis distinguishes "homozygous reference" from "no data", which single-sample calling cannot, and lends power to low-coverage samples.
5. *Filtering*: hard thresholds on annotations (depth, strand bias, mapping quality of the supporting reads, the position of the variant within the reads), or a model trained to separate true from false calls using known sites as positive examples (VQSR, and more recently learned filters). Filters are applied by writing a value in the FILTER column, not by deleting records.

```bash
gatk MarkDuplicates -I HG002.bam -O HG002.md.bam -M dup_metrics.txt
gatk BaseRecalibrator -I HG002.md.bam -R GRCh38.fa --known-sites dbsnp.vcf.gz -O recal.table
gatk ApplyBQSR -I HG002.md.bam -R GRCh38.fa --bqsr-recal-file recal.table -O HG002.bqsr.bam
gatk HaplotypeCaller -R GRCh38.fa -I HG002.bqsr.bam -O HG002.g.vcf.gz -ERC GVCF
gatk GenomicsDBImport --genomicsdb-workspace-path db -L chr2 -V HG002.g.vcf.gz -V HG003.g.vcf.gz
gatk GenotypeGVCFs -R GRCh38.fa -V gendb://db -O trio.vcf.gz
# A lighter alternative for one sample, and a deep-learning caller
bcftools mpileup -f GRCh38.fa -q 20 -Q 20 -a AD,DP HG002.md.bam | bcftools call -mv -Oz -o bcf.vcf.gz
run_deepvariant --model_type=WGS --ref=GRCh38.fa --reads=HG002.md.bam --output_vcf=dv.vcf.gz
```

For the amplicon panel of [7.8.10](/7.8.10), where the targets are few and known, a single-sample caller restricted to the target intervals is enough, and the primer positions must be excluded from calling: a variant under a primer is replaced by the primer's own sequence and becomes invisible.

## 12.4. The VCF Format

**Definition 12.4.1 (VCF)** The **Variant Call Format** stores variants as tab-separated text: a header of `##` lines declaring the reference, the contigs and the meaning of every INFO, FORMAT and FILTER key, a `#CHROM` line naming the samples, then one line per variant site with the fields CHROM, POS (one-based), ID, REF, ALT (comma-separated alternatives), QUAL, FILTER, INFO, FORMAT and one column per sample. BCF is its binary form.

```text
##fileformat=VCFv4.3
##reference=GRCh38
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
##FORMAT=<ID=AD,Number=R,Type=Integer,Description="Read depth per allele">
##FORMAT=<ID=PL,Number=G,Type=Integer,Description="Phred-scaled genotype likelihoods">
#CHROM POS       ID        REF ALT QUAL FILTER INFO          FORMAT       sample1
chr2   135851076 rs4988235 G   A   790  PASS   DP=32;AF=0.5  GT:AD:DP:GQ:PL 0/1:16,16:32:99:790,0,780
```

The genotype `0/1` indexes the alleles ($0$ = REF, $1$ = first ALT); `|` instead of `/` means the genotype is phased, so that the first allele of every phased record lies on the same haplotype. `AD` gives the reads per allele, `PL` the Phred-scaled genotype likelihoods normalized so that the best is $0$ (the `PL` of Example 12.2.1), and `GQ` the difference between the two best.

Two operations must be done before VCFs are compared or merged. *Left alignment* moves an indel inside a repeat as far left as it can go without changing the implied sequence, because `POS=1000 REF=GAA ALT=G` and `POS=1002 REF=AAC ALT=AC` can describe the same deletion; and *decomposition* splits a multi-allelic record into biallelic ones, removing bases shared by REF and ALT. `bcftools norm -f ref.fa -m -any` does both. Without them, the same variant called by two pipelines, or seen in two samples, is counted as two different variants.

```bash
bcftools norm -f GRCh38.fa -m -any -Oz -o norm.vcf.gz calls.vcf.gz && bcftools index norm.vcf.gz
bcftools view -i 'FILTER="PASS" && FMT/GQ>=20 && FMT/DP>=10' -Oz -o pass.vcf.gz norm.vcf.gz
bcftools query -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT\t%AD]\n' -r chr2:135851076 pass.vcf.gz
```

## 12.5. Is the Call Set Any Good?

**Definition 12.5.1 (Benchmark Set)** A *benchmark* (truth) set is a list of variants and a set of regions for a sample in which the variants are known with high confidence, established by combining several technologies and pipelines, as for the Genome in a Bottle samples HG001–HG007. Calls are compared with it inside the confident regions only.

Comparison must allow for representation: the same event can be written in several ways, so a comparison tool (hap.py, vcfeval) matches calls by the haplotype sequences they imply rather than by their records. The results are the precision (fraction of calls that are true), the recall (fraction of true variants called) and their harmonic mean, reported separately for single-nucleotide variants and indels, since indel calling is much harder. Current short-read pipelines reach above $99.5\,\%$ for both measures on single-nucleotide variants in confident regions, and lower for indels, especially in homopolymers; the error rate outside the confident regions, which include the hardest $5$–$10\,\%$ of the genome, is unknown by construction.

Three internal checks need no benchmark.

**Definition 12.5.2 (Transition/Transversion Ratio)** The **transition/transversion ratio** (Ti/Tv) of a call set is the number of **transition** substitutions (purine to purine or pyrimidine to pyrimidine) divided by the number of **transversion** substitutions.

Random substitutions would give $\mathrm{Ti/Tv} = 0.5$, since each base has one transition and two transversion partners. Real human whole-genome call sets give $2.0$–$2.1$, mostly because deamination of methylated cytosine in CpG dinucleotides is frequent ([7.4.12](/7.4.12#sec-12.6.1)); exomes give about $3.0$, because the genetic code and selection ([7.2.2](/7.2.2#sec-2.4.2)) make transitions more often synonymous. A set whose Ti/Tv is pulled towards $0.5$ contains false positives, and the deficit estimates their number: if a set of $N$ calls has ratio $r$ and the true ratio is $r_0$, with false calls at ratio $0.5$, the false fraction $\phi$ satisfies $r = [(1-\phi)r_0/(1+r_0) + \phi/3]/[(1-\phi)/(1+r_0) + 2\phi/3]$.

The ratio of heterozygous to homozygous alternative calls is a second check: about $1.5$–$2.0$ for a human genome, higher in samples of African ancestry and lower in inbred or consanguineous ones; a ratio far above $2$ suggests contamination with another sample, since a mixture creates apparent heterozygotes.

**Definition 12.5.3 (Mendelian Consistency)** In a mother–father–child trio, a genotype call is a *Mendelian violation* if the child's genotype cannot be produced from the parents' genotypes by transmitting one allele from each, for example a $1/1$ child of a $0/0$ parent.

Real violations are new mutations, of which a child has about $60$–$80$ genome-wide; everything beyond that is error. With $4$–$5\times10^6$ variant sites per genome and three genotypes per site to get right, even a per-genotype error rate of $10^{-4}$ produces of the order of a thousand violations, so the violation rate is a sensitive measure of genotyping accuracy, and it is available for any trio without a benchmark.

## 12.6. Structural and Copy-Number Variants

Structural variants are the class short reads detect worst, and the class that accounts for most of the differing bases between two genomes. Four signals are available after mapping.

| Signal | What it shows | Detects |
|---|---|---|
| Discordant read pairs | insert size or orientation unlike the library's distribution ([7.8.9](/7.8.9#sec-9.3.1)) | deletions (insert too large), insertions (too small), duplications (mates in the wrong order), inversions (mates on the same strand), translocations (mates on different chromosomes) |
| Split reads | one read aligned in two parts to different places (supplementary alignments, [7.8.10](/7.8.10#sec-10.5.1)) | breakpoints at base resolution |
| Read depth | local change in coverage | copy-number gains and losses, including those with no unique breakpoint |
| Local assembly | the sample's own sequence at the locus ([7.8.11](/7.8.11)) | insertions of novel sequence, complex events |

![The four signatures of a structural variant in mapped paired-end reads. In each panel the sample's arrangement is drawn above the reference, with the breakpoints marked, and below it the read pairs as they appear after mapping (arrows are mates, the arrowhead gives the strand; grey pairs are normal, red pairs discordant, yellow pairs contain a split read), with the depth below. A: a deletion of segment B gives pairs whose insert is larger than expected, split reads at the junction, and a drop in depth. B: a tandem duplication gives pairs whose mates appear in the wrong order (the junction joins the end of the duplicated segment to its start), split reads of the same junction, and a rise in depth. C: an inversion gives pairs whose mates lie on the same strand at both breakpoints, split reads, and no change of depth](./plots/sv-signatures.py)

Callers combine the signals: Manta and Delly for short reads, Sniffles2 and cuteSV for long reads, where one read often spans the whole event and the detection becomes almost trivial by comparison (long reads roughly triple the number of structural variants found per genome). Copy number is estimated from depth after correcting for GC content and mappability, then segmenting the log ratios.

**Algorithm 12.6.1 (Binary Segmentation of Depth)** Given log ratios $x_1, \dots, x_n$ in windows along the genome: find the split point $k$ maximizing the two-sample $t$ statistic between $x_1, \dots, x_k$ and $x_{k+1}, \dots, x_n$; if the statistic exceeds a threshold, accept the split and recurse on both parts, otherwise return the segment. Circular binary segmentation (Olshen and colleagues, 2004) tests instead the best *interval* against its complement, which finds short focal changes that one-sided splits miss, and assesses significance by permutation.

![Copy number from read depth (simulated: read counts in 1 kb windows along 2 Mb at a mean of 30 per window, with 10 % window-to-window variation from mappability and GC bias, carrying a heterozygous deletion of 150 kb and a duplication of 300 kb). A: log2 ratios to the diploid mean, with the segment means found by binary segmentation (Algorithm 12.6.1, threshold t = 6) in red. B: the segment means converted to copy number as 2 × 2^(log2 ratio): the segmentation recovers 0.98, 1.95–1.98 and 3.00 against the true 1, 2 and 3, and places the breakpoints within a few windows](./plots/cnv-segmentation.py)

## 12.7. Somatic Variants

In a tumour sample the three-genotype constraint is gone: a mutation present in a subclone appears at any allele fraction, and the sample also contains normal cells. Somatic calling therefore compares a tumour with a matched normal sample from the same individual (Mutect2, Strelka2), which removes the germline variants and the recurrent artefacts shared by both.

**Formula 12.7.1 (Expected Variant-Allele Fraction)** Let a fraction $p$ of the cells in the sample carry a mutation (the product of tumour purity and the fraction of tumour cells in the clone), let the locus have $C_{\mathrm{T}}$ copies in those cells, of which $m$ carry the mutation, and $2$ copies in the other cells. Then the expected fraction of reads supporting the mutation is
$$
f = \frac{p\,m}{p\,C_{\mathrm{T}} + 2(1 - p)}.
$$

**Example 12.7.1** In a sample of purity $0.6$ with a heterozygous mutation at a diploid locus, $f = 0.6/(1.2 + 0.8) = 0.30$. If the other allele has been lost ($C_{\mathrm{T}} = 1$, $m = 1$), $f = 0.6/(0.6 + 0.8) = 0.43$; if the mutant allele is duplicated ($C_{\mathrm{T}} = 3$, $m = 2$), $f = 1.2/(1.8 + 0.8) = 0.46$. A mutation present in only half of the tumour cells of the same sample has $p = 0.3$ and $f = 0.15$. Inverting the formula with the copy number from Algorithm 12.6.1 gives the fraction of cells carrying each mutation, which is how the clonal structure of a tumour is reconstructed ([7.4.21](/7.4.21#sec-21.1.1)).

![Detecting a somatic variant. A: the expected variant-allele fraction (Formula 12.7.1) against the fraction p of cells carrying the mutation, for a heterozygous mutation at a diploid locus, after loss of the other allele, and with the mutant allele duplicated; the dotted line is a fraction of 0.05. B: the probability of observing at least five supporting reads, 1 − P(Bin(n, f) ≤ 4), against depth, for allele fractions 0.02 to 0.25. At 100× a variant at f = 0.05 is seen with probability 0.56 and at f = 0.10 with 0.98; f = 0.02 needs about 300×. The dashed line is the chance that five or more reads carry the same wrong base at Q30: 3 × 10⁻¹⁰ at depth 100 but 3 × 10⁻⁵ at depth 1000, so very deep sequencing needs error models per context or molecular identifiers rather than a fixed read threshold](./plots/somatic-detection.py)

Two further problems are specific to somatic calling. Clonal haematopoiesis puts real somatic mutations in the "normal" blood sample, where they are mistaken for artefacts or, worse, cause a true tumour variant to be filtered; and low-level contamination of the normal with tumour does the same. And at low allele fractions the error processes of the library (oxidative damage during fragmentation, deamination in formalin-fixed tissue) dominate, which is why liquid-biopsy assays use **unique molecular identifiers** and duplex consensus reads ([7.8.9](/7.8.9#sec-9.3.3)).

## 12.8. Annotation and Interpretation

### 12.8.1. Naming and Consequences

**Definition 12.8.1 (HGVS Nomenclature)** The **HGVS nomenclature** names a variant relative to a stated, versioned reference sequence: `NC_000002.12:g.135851076G>A` on a genome, `NM_004006.2:c.4375C>T` on a coding sequence (positions counted from the A of the start codon; negative upstream, `+`/`−` offsets into introns) and `NP_003997.1:p.Arg1459Ter` on a protein. Deletions, duplications, insertions and combinations are written `c.4375_4379del`, `c.4375_4385dup`, `c.4375_4376insACCT`, `c.4375_4376delinsAGTT`.

Because the name depends on the transcript, the same variant has different `c.` names on different transcripts of a gene, and a different one again on a new version of the same transcript; clinical reports therefore state the transcript with its version, and projects agree on a set of clinical reference transcripts (MANE Select). Annotation tools (Ensembl VEP, ANNOVAR, SnpEff) place each variant on every overlapping transcript and report the consequence (**missense mutation**, **nonsense mutation**, **frameshift mutation**, synonymous, splice-site, intronic, regulatory) with a controlled vocabulary of Sequence Ontology terms, along with frequencies, predictions and clinical annotations gathered from the databases of [7.8.2](/7.8.2).

**Example 12.8.1** rs4988235 is `NC_000002.12:g.135851076G>A`, and `NM_005915.6:c.1917+326C>T` relative to the *MCM6* transcript: it lies deep inside intron 13 of *MCM6* and has no protein consequence at all. Its effect is on *LCT*, a different gene $13.9\,\mathrm{kb}$ away, whose enhancer it alters ([7.8.2](/7.8.2)), which is why the older literature writes it as `LCT:c.-13910C>T`. A variant whose consequence annotation is "intron variant" is not thereby harmless, and a pipeline that filters non-coding variants away would discard the best-known regulatory variant in the human genome.

### 12.8.2. Evidence about Effect

- *Population frequency.* A variant more common than the disease can be is not a cause of it. For a dominant disorder of prevalence $P$, in which the variant explains a fraction $A$ of cases, with allelic heterogeneity and **penetrance** $\pi$, the maximum credible allele frequency is about $PA/(2\pi)$: for $P = 1/500$, $A = 0.02$ and $\pi = 0.5$ that is $4\times10^{-5}$, so a variant at $10^{-3}$ in any population of gnomAD is excluded. The frequency must be read in the ancestry-matched population, not globally.
- *Constraint.* Genes differ in how much variation they tolerate; gnomAD reports the depletion of loss-of-function variants in each gene (LOEUF), and a damaging variant in a highly constrained gene carries more weight.
- *Conservation and computational prediction.* Conservation scores ([7.8.8](/7.8.8)) say whether a position has been preserved by selection. Predictors of missense effect combine conservation, physicochemical change and structure (SIFT, PolyPhen-2), ensembles combine predictors (REVEL, CADD, which also covers non-coding variants), and unsupervised models learn the distribution of the family's sequences and score a variant by how unlikely it is under that distribution (EVE, AlphaMissense; [7.8.15](/7.8.15)). SpliceAI predicts gain and loss of splice sites from sequence, which recovers pathogenic variants that other tools call benign because they are synonymous or intronic.
- *Functional assays.* Multiplexed assays of variant effect measure every possible variant of a gene in one experiment (saturation **genome editing**, [7.4.19](/7.4.19)); for *BRCA1* they have reclassified most previously uncertain variants ([7.4.21](/7.4.21#sec-21.4.2)).

Predictors are correlated with one another and are trained on the same clinical databases they are then evaluated on, so their reported accuracies are optimistic and "four out of five tools agree" is not four independent pieces of evidence. The classification framework treats computational evidence as supporting, not decisive.

### 12.8.3. The ACMG/AMP Classification

The guidelines of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology (Richards and colleagues, 2015) place a variant in one of five classes — pathogenic, likely pathogenic, of uncertain significance, likely benign, benign — by combining criteria of stated strength: very strong (a null variant in a gene where loss of function causes the disease), strong (same amino-acid change as a known pathogenic variant; a well-established functional assay), moderate (de novo occurrence without confirmed parentage; absent from population databases), supporting (computational predictions; co-segregation), and the mirror-image benign criteria, up to stand-alone (frequency too high for the disease).

**Formula 12.8.1 (Point System)** In the Bayesian reconstruction of the rules (Tavtigian and colleagues, 2018), one supporting point has odds of pathogenicity $O_{\mathrm{PVSt}}^{1/8}$ with $O_{\mathrm{PVSt}} = 350$, moderate counts as $2$ points, strong as $4$ and very strong as $8$, benign criteria count negative, and the posterior probability of pathogenicity after $P$ summed points with prior $\pi$ is
$$
\mathbb{P} = \frac{\mathrm{odds}}{1 + \mathrm{odds}}, \qquad \mathrm{odds} = 350^{P/8}\,\frac{\pi}{1 - \pi}.
$$

**Example 12.8.2** With the prior $\pi = 0.1$ used by the authors, the class boundaries $0.99$, $0.90$, $0.10$ and $0.001$ fall at $+10$, $+6$, $-1$ and $-7$ points: $+10$ gives $0.994$, $+6$ gives $0.900$, $-1$ gives $0.051$ and $-7$ gives $0.00066$. The combinations listed in the 2015 guidelines (one very strong plus one strong; two strong; one strong plus three moderate) all sum to at least $10$ points, so the verbal rules and the arithmetic agree, and the point system also settles combinations the rules left undefined. The value of this reconstruction is that it makes the assumptions visible: the prior and the strength of each criterion can be estimated from data and revised, and criteria that are not independent (several correlated predictors) must not be counted twice.

![The Bayesian reading of the ACMG/AMP rules. A: posterior probability that a variant is pathogenic against the summed points of evidence (Formula 12.8.1), for three prior probabilities; the dotted lines are the class boundaries 0.99, 0.90, 0.10 and 0.001, which with the prior 0.1 fall at +10, +6, −1 and −7 points. The vertical axis is on a logit scale, on which the curves are straight lines: each point of evidence multiplies the odds by 350^(1/8) = 2.08. B: the points assigned to the criteria by their strength; benign criteria count negative](./plots/acmg-points.py)

Most variants collect too little evidence and remain *variants of uncertain significance*, which cannot be used for clinical decisions. The fraction is higher for people whose ancestry is under-represented in the databases, since the population-frequency and segregation evidence is weaker. ClinVar collects submitted classifications with their evidence and flags conflicts between laboratories; ClinGen expert panels write gene-specific rules, which is the practical answer to the generic guidelines being too loose for any one gene.

## 12.9. Diagnosing a Rare Disease

Exome or genome sequencing of a patient yields some $4\times10^6$ variants, of which one or two may explain the disease. The analysis is a sequence of filters, each justified by genetics rather than by convenience: variants frequent in the matched population are excluded (Section 12.8.2); the consequence and the gene are required to fit the phenotype; and the inheritance pattern in the family must hold — a de novo variant for a sporadic dominant disorder, two variants in trans for a recessive one (phase matters, and can be determined from the parents or from long reads), homozygosity in a consanguineous family ([7.4.14](/7.4.14#sec-14.11)).

**Example 12.9.1** A trio gives the strongest design for a severe sporadic disorder. Each child carries about $74$ new single-nucleotide mutations genome-wide ($6.2\times10^9$ base pairs at $1.2\times10^{-8}$ per base pair per generation), of which about $0.8$ falls in the $35\,\mathrm{Mb}$ of coding exons. A damaging new mutation in a constrained gene whose function fits the phenotype is therefore, by itself, strong evidence. The filter is only as good as the genotypes: as Section 12.5 showed, genotyping errors produce Mendelian violations in numbers far exceeding the true de novo count, so candidates are confirmed by inspecting the reads and by an independent assay.

Phenotype-driven tools (Exomiser and similar) rank candidate genes by the semantic similarity between the patient's Human Phenotype Ontology terms and the phenotypes recorded for each gene, in humans and in model organisms, combined with the variant-level evidence; this converts the physician's observations into a prior over genes. Where no diagnosis is found, the causes are in order: the variant is of a class not well detected (structural, repeat expansion, deep intronic, mosaic), the gene is not yet known to cause disease, or the phenotype is not genetic in the assumed way. Re-analysis of unsolved cases after one or two years yields further diagnoses at an appreciable rate, purely because gene–disease knowledge has grown, which is an argument for storing the data in a reanalysable form ([7.8.1](/7.8.1#sec-1.6)).

The story of NGLY1 deficiency shows the pipeline at the limit of what it can do. A boy with an undiagnosed multisystem disorder — developmental delay, liver abnormalities, a near absence of tears — was sequenced with his parents after years of inconclusive metabolic testing; he carried two different loss-of-function variants in *NGLY1*, one from each parent, a gene then connected with no human disease, which encodes the enzyme that removes N-glycans from misfolded glycoproteins before their degradation. The evidence was the fit between the biochemical function and the phenotype, and above all the identification of further patients, found when the family published the case and other clinicians recognized the same unusual combination of features. The variants were of uncertain significance until a second family made them interpretable: a single genome is rarely diagnostic by itself, and the limiting resource in rare-disease genomics is the matching of patients, not the sequencing.

## Summary

| Topic | Key points |
|---|---|
| Genotyping | genotype likelihood from base qualities (Definition 12.2.1); Bayesian posterior with prior $\theta$, GQ and QUAL (Formula 12.2.1); one alternative read is never enough, two only at low depth (Example 12.2.1) |
| Haplotype callers | active regions, local assembly, pair HMM read likelihoods, marginalization (Algorithm 12.2.1); indels and clustered variants are the reason; DeepVariant classifies pileup images |
| Workflow | duplicate marking, BQSR, GVCF per sample, joint genotyping (distinguishes "reference" from "no data"), filtering by hard thresholds or a trained model |
| VCF | fields, GT/AD/GQ/PL (Definition 12.4.1); left alignment and decomposition of multi-allelic records before any comparison |
| Evaluation | benchmark sets and haplotype-aware comparison (Definition 12.5.1); precision and recall, indels worst; Ti/Tv $\approx 2.0$ genome-wide, $3.0$ exome against $0.5$ for random (Definition 12.5.2); het/hom ratio; Mendelian violations against about $60$–$80$ true de novo mutations (Definition 12.5.3) |
| Structural variants | discordant pairs, split reads, depth, local assembly, each with its signature per variant class; long reads find far more; segmentation of depth for copy number (Algorithm 12.6.1) |
| Somatic variants | tumour–normal pairs; $f = pm/[pC_{\mathrm{T}} + 2(1 - p)]$ (Formula 12.7.1); detection power by depth and $f$; clonal haematopoiesis, damage artefacts, UMIs |
| Annotation | HGVS names relative to a versioned transcript (Definition 12.8.1); consequences on all transcripts; rs4988235 is an intron variant of *MCM6* acting on *LCT* (Example 12.8.1); frequency ceilings, constraint, conservation, predictors, functional assays |
| Classification | five classes from criteria of graded strength; points and posterior, boundaries at $+10$, $+6$, $-1$, $-7$ (Formula 12.8.1, Example 12.8.2); predictors are correlated and only supporting; variants of uncertain significance and the ancestry gap |
| Rare disease | filtering by frequency, consequence and inheritance; trios and the de novo count (Example 12.9.1); phenotype-driven ranking; re-analysis and patient matching |

## Questions

1. A site has depth $12$ with $3$ alternative reads, all bases at Q$30$. Compute the three genotype likelihoods and the posterior with $\theta = 10^{-3}$. What is the call?

   **Answer** With $\varepsilon = 10^{-3}$, the per-read probabilities of seeing the alternative base are $\varepsilon/3 = 3.33\times10^{-4}$ ($0/0$), $0.5$ ($0/1$) and $1 - \varepsilon$ ($1/1$), and of the reference base $1 - \varepsilon$, $0.5$ and $\varepsilon/3$. Log-likelihoods: $0/0$: $9\ln(0.999) + 3\ln(3.33\times10^{-4}) = -24.02$; $0/1$: $12\ln 0.5 = -8.32$; $1/1$: $9\ln(3.33\times10^{-4}) + 3\ln(0.999) = -72.1$. Adding $\ln$ priors $\ln(0.9985)$, $\ln(10^{-3})$, $\ln(5\times10^{-4})$ gives $-24.02$, $-15.23$, $-79.7$, so the heterozygote wins with posterior $1/(1 + \mathrm{e}^{-8.79}) = 0.99985$: called $0/1$ with GQ $38$. Three reads out of twelve are an unusual split for a heterozygote but far more likely than three independent errors.

2. Why does a haplotype-based caller outperform a position-by-position caller at indels in homopolymers, and what does the pair HMM contribute?

   **Answer** In a homopolymer the aligner can place a one-base deletion at any position of the run, so reads supporting the same event are spread over several positions and none reaches significance; and reads with the indel may be aligned with mismatches instead, hiding it. A haplotype caller assembles the region's reads, proposes the two candidate sequences (with and without the deleted base) and scores every read against each as a whole, so the evidence is pooled regardless of how the read was originally aligned. The pair HMM supplies $\mathbb{P}(\text{read} \mid \text{haplotype})$ with explicit insertion and deletion states whose probabilities depend on the local context, which is exactly the slippage process that makes homopolymer indels common; a fixed gap penalty cannot express that the same deletion is likely in a run of eight A and unlikely elsewhere.

3. A call set of $4.0\times10^6$ single-nucleotide variants has Ti/Tv $= 1.8$. Assuming the true ratio is $2.1$ and that false calls have Ti/Tv $= 0.5$, estimate the number of false positives.

   **Answer** Let $\phi$ be the false fraction. Transitions are a fraction $r/(1 + r)$ of a set with ratio $r$: $0.677$ for the true variants and $1/3$ for false ones. Then $\mathrm{Ti/Tv} = [(1-\phi)0.677 + \phi/3]/[(1-\phi)0.323 + 2\phi/3] = 1.8$. Solving: numerator $= 0.677 - 0.344\phi$, denominator $= 0.323 + 0.344\phi$, so $0.677 - 0.344\phi = 0.581 + 0.619\phi$, $\phi = 0.096/0.963 = 0.0997$. About $4.0\times10^5$ false calls, a tenth of the set — a strong signal that the filters are too permissive.

4. Explain why joint genotyping of a cohort gives better calls than genotyping each sample separately, and what a GVCF stores that a VCF does not.

   **Answer** A single-sample VCF lists only variant sites, so when sample B lacks a record at a site where sample A has a variant, one cannot tell whether B is homozygous reference or simply had no coverage. A GVCF stores, in addition, blocks of non-variant positions with the likelihood that no variant is present, so the information is preserved. Joint genotyping then uses the cohort's allele frequency as a prior: evidence that is too weak in one sample (two alternative reads of twelve) becomes convincing if the allele is common among the others, and conversely an isolated weak call surrounded by cohort-wide absence is penalized. It also provides a complete genotype matrix for population analysis ([7.8.13](/7.8.13)) and better-calibrated filtering, since the annotations of thousands of samples train the model.

5. A deletion of $4$ kb is present on one chromosome of a sample sequenced at $30\times$ with $2\times150$ reads and inserts of $350 \pm 90$ nt. Which of the four signals will show it, and with roughly how many supporting reads?

   **Answer** Discordant pairs: a pair spans the deletion if one mate falls on each side, that is if the fragment covers the junction; the effective window is the insert size, so the expected number of fragments spanning it is about $c \cdot I/(2\ell) \cdot$ (fraction from the deleted haplotype), with $c = 30$, $I = 350$, $\ell = 150$: about $35$ fragments cross the junction, half from the deleted haplotype, giving roughly $17$ discordant pairs, with inserts near $4350$ rather than $350$. Split reads: a read crosses the junction if its $150$ bases span it, giving about $30 \times 150/150 /2 \approx 15$ reads, of which those with enough bases on each side (say $\ge 20$) are usable, about $12$. Depth: the $4$ kb interval has half the normal depth, which over $4000$ bases is a clear signal ($\approx 1600$ versus $3200$ expected read starts, far outside Poisson noise). Local assembly also recovers the junction. For a $50$-base deletion, by contrast, the insert-size shift is within the normal spread and only split reads and assembly work.

6. Tumour purity is $0.4$. What allele fraction does a clonal heterozygous mutation have at a diploid locus, and what depth is needed to see at least five supporting reads with probability $0.95$?

   **Answer** $f = 0.4/(0.8 + 1.2) = 0.20$. The number of supporting reads is $\mathrm{Bin}(n, 0.2)$; $\mathbb{P}(\ge 5)$ reaches $0.95$ at $n = 44$ ($0.948$ at $43$, $0.957$ at $44$). A subclonal mutation in a third of the tumour cells has $p = 0.133$, $f = 0.071$, and needs about $130\times$; this is why tumours are sequenced at $60$–$100\times$ or more and why subclonal structure is resolvable only at high depth.

7. A missense variant in a dominant disease gene has: absent from gnomAD (moderate), de novo with confirmed parentage (strong), computational predictors in agreement that it is damaging (supporting), and a well-established functional assay showing loss of function (strong). Classify it with Formula 12.8.1, and explain what would change if the functional assay were not validated.

   **Answer** Points: $2 + 4 + 1 + 4 = 11$. With $\pi = 0.1$, odds $= 350^{11/8}\times(1/9) = 0.111 \times 350^{1.375}$. Since $350^{1.375} = \mathrm{e}^{1.375 \times 5.858} = \mathrm{e}^{8.05} = 3140$, odds $= 349$ and $\mathbb{P} = 0.997$: pathogenic (above the $+10$-point threshold). If the assay is not validated against known pathogenic and benign variants, the criterion drops to supporting ($1$ point), giving $8$ points, $\mathbb{P} = 0.975$: likely pathogenic but not pathogenic. The strength of a functional criterion depends on the assay's demonstrated ability to separate known classes, which is the main reason ClinGen panels write assay-specific rules.

8. A variant is reported as `NM_004006.2:c.4375C>T` in one laboratory and as "intronic, no consequence" by another pipeline for the same genomic position. Give two reasons the reports can differ, and say how to resolve it.

   **Answer** First, the transcript: a position that is exonic on one transcript of a gene is intronic on another, and tools default to different transcript sets (RefSeq, Ensembl, MANE Select) and to different rules for which consequence to report when several apply. Second, the version: positions in `c.` notation are counted on a particular version of the transcript, so `NM_004006.2` and a later version may number the same base differently, and a liftover between assemblies may have moved the genomic coordinate. Resolve it by comparing the genomic HGVS name on a versioned chromosome record (`NC_…:g.…`), which is unambiguous, then re-annotating both with the same, stated transcript set, preferring the clinical reference transcript; a report that gives only a `c.` name without the transcript version cannot be checked.

9. Why does filtering out non-coding variants work well in practice for rare disease and fail for a variant such as rs4988235?

   **Answer** It works because the coding fraction of the genome is $1$–$2\,\%$ but contains the great majority of known Mendelian disease variants, and because coding consequences can be predicted reliably from the sequence, while the effect of a non-coding variant usually cannot. It fails whenever the mechanism is regulatory: rs4988235 lies in an intron of *MCM6* and changes a binding site in an enhancer of *LCT*, a neighbouring gene, so every coding-consequence annotation of it is "intron variant, no protein change", and both the gene assignment and the effect are wrong. Non-coding variants require different evidence — conservation, chromatin and enhancer annotation, predicted change in transcription-factor binding ([7.8.8](/7.8.8)), expression data linking the element to its target gene ([7.9](/7.9)) — and this is one reason the diagnostic yield of genome sequencing exceeds that of exome sequencing by only a few percent today while the gap is expected to grow.

10. (Design) You must set up a pipeline that calls germline variants in a panel of $400$ cancer-predisposition genes from targeted sequencing of $500$ patients, and reports classified variants. Describe the steps, the quality checks, and the places where your pipeline could do harm.

    **Answer** Steps: demultiplex and quality-control the reads ([7.8.9](/7.8.9)); map with BWA-MEM to GRCh38 including alternative contigs handled explicitly; mark duplicates (not for an amplicon design, where reads share start positions — check which chemistry the panel uses) and recalibrate qualities; call with a haplotype-based caller restricted to the target intervals plus flanking bases, producing GVCFs, and genotype the $500$ samples jointly so that the cohort's frequencies inform the priors and so that artefacts recurring across samples become visible; call copy-number variants from depth within the panel (exon-level deletions in *BRCA1*, *MSH2* and others are a substantial fraction of pathogenic variants and are missed by small-variant callers); normalize and annotate with a stated transcript set; classify with gene-specific ClinGen rules where they exist. Checks: per-sample coverage of every target base with a stated minimum (say $20\times$) and an explicit list of positions not callable; sample identity and sex from genotypes; contamination estimation; a benchmark sample (one of the GIAB genomes) in every run, with precision and recall reported; Ti/Tv and het/hom per sample; tracking of which pipeline and database versions produced each report. Harms: a false positive leads to surgery; a false negative gives false reassurance, and the silent failure mode is a target region with no coverage that is never reported as such, which is why the callable-region report is as important as the variant list. Variants of uncertain significance must be reported as such and not acted on, their rate is higher in under-represented ancestries, and the laboratory needs a procedure for re-contacting patients when a classification changes, since reclassification is frequent in these genes.
