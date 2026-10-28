"""A simulated genome-wide association study (case-control, 4000 cases and 4000 controls, about 5900 SNPs on
12 chromosomes; four causal variants with allelic odds ratios 1.2-1.35, each tagged by neighboring SNPs in
LD; seed 11). A: Manhattan plot: -log10 p of the allelic chi-square test for every SNP in genome order;
solid line: genome-wide significance 5e-8; dotted: suggestive 1e-5; red: the causal SNPs. B: QQ plot of the
same scan: the p-values follow the null diagonal except for the tail of true associations (lambda_GC near 1).
C: the same design but with 60 % of the cases but only 40 % of the controls drawn from one of two subpopulations that differ slightly in
allele frequency (F_ST = 0.0005): the whole distribution is inflated (lambda_GC > 1) and spurious signals appear across the
genome, the signature of population stratification."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, gwas

fig = plt.figure(figsize=(12.0, 6.6))
gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1], left=0.06, right=0.98, bottom=0.09, top=0.94, wspace=0.22,
                      hspace=0.45)
causal = [(2, 150, 1.35), (5, 300, 1.25), (7, 80, 1.3), (11, 200, 1.2)]
d = gwas.simulate_case_control(4000, 4000, n_chrom=12, snps_per_chrom=520, causal=causal, rng=np.random.default_rng(11))
a = fig.add_subplot(gs[0, :])
gwas.manhattan(a, d["chrom"], d["pos"], d["p"], highlight=d["causal"])
charts.title(a, "A  Manhattan plot")
b = fig.add_subplot(gs[1, 0])
gwas.qq(b, d["p"])
charts.title(b, "B  QQ plot, homogeneous sample")
s = gwas.simulate_case_control(4000, 4000, n_chrom=12, snps_per_chrom=520, causal=causal, fst=0.0005, case_share=0.6,
                               control_share=0.4, rng=np.random.default_rng(11))
c = fig.add_subplot(gs[1, 1])
gwas.qq(c, s["p"], token="rna")
charts.title(c, "C  QQ plot, stratified sample")
