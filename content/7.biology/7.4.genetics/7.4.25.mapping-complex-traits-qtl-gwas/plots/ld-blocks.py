"""Haplotype blocks in simulated haplotypes (400 chromosomes, 40 SNPs over a region with recombination
hotspots at 0.3 and 0.68 of its length; Li-Stephens copying model, seed 7). Each diamond is one pair of SNPs,
shaded by r^2 (A) or |D'| (B); the top track maps the SNPs, which are evenly spaced in the triangle, to
their physical positions. Within blocks |D'| is close to 1 for most pairs (little recombination since the
haplotypes arose), whereas r^2 is high only for SNPs with similar allele frequencies on the same
haplotype branch; both drop at the hotspots. A few SNPs per block (tag SNPs) capture most variation."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, gwas

H, pos = gwas.simulate_haplotypes(400, 40, hotspots=[0.3, 0.68], rng=np.random.default_rng(7))
fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.6))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.9, wspace=0.08)
gwas.ld_triangle(axs[0], gwas.ld_r2(H), pos=pos, token="negative")
charts.title(axs[0], "A  $r^2$")
gwas.ld_triangle(axs[1], gwas.ld_dprime(H), pos=pos, token="dna")
axs[1].texts[-1].set_text("$|D'|$")
charts.title(axs[1], "B  $|D'|$")
