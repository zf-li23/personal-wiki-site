# Sample quality control of genotype data (simulated). 2000 individuals typed on an array: most have a missing
# rate of 0.2-1 % and a heterozygosity rate near 0.32; a few samples are contaminated by DNA of another person
# (excess heterozygosity), a few come from consanguineous unions (reduced heterozygosity) and a few failed
# partly (high missingness). A: heterozygosity rate against missing rate (log scale), with the usual exclusion
# rules: missing rate >= 3 % or heterozygosity outside mean +/- 3 SD (computed from all samples). B: the
# X-chromosome inbreeding estimate F used by the sex check, for reported males and females; two samples are
# discordant (a reported female with F near 1, a reported male with F near 0), the signature of a sample swap.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
n = 2000
miss = np.exp(rng.normal(np.log(0.005), 0.45, n))
het = rng.normal(0.320, 0.0045, n)
kind = np.zeros(n, int)
idx = rng.choice(n, 34, replace=False)
contam, inbred, failed = idx[:10], idx[10:22], idx[22:]
het[contam] += rng.uniform(0.025, 0.06, contam.size)
miss[contam] *= rng.uniform(1.5, 3.0, contam.size)
het[inbred] *= 1 - rng.choice([0.0625, 0.125, 0.25], inbred.size)       # F of children of relatives
miss[failed] = rng.uniform(0.035, 0.12, failed.size)
het[failed] += rng.normal(-0.004, 0.006, failed.size)
kind[contam], kind[inbred], kind[failed] = 1, 2, 3
mu, sd = het.mean(), het.std()
bad = (miss >= 0.03) | (np.abs(het - mu) > 3 * sd)

fig, ax = bio.canvas(30.0, 10.6)
a = C.axes_at(ax, (2.2, 1.6, 13.0, 8.0))
names = ["typical", "contaminated", "consanguineous", "partly failed"]
toks = ["neutral", "negative", "protein", "highlight"]
for k in range(4):
    s = kind == k
    a.scatter(miss[s], het[s], s=6 if k == 0 else 14, color=C.line(toks[k]), alpha=0.55 if k == 0 else 0.95,
              lw=0, label=names[k])
a.set_xscale("log")
a.axvline(0.03, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
for y in (mu - 3 * sd, mu + 3 * sd):
    a.axhline(y, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
a.set_xlim(1e-3, 0.2)
a.set_ylim(0.225, 0.39)
a.text(0.032, 0.383, "missing >= 3 %", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(1.1e-3, mu + 3 * sd + 0.002, "mean + 3 SD", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(1.1e-3, mu - 3 * sd - 0.007, "mean - 3 SD", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(0.0012, 0.232, f"{bad.sum()} of {n} samples excluded", fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(a, "missing genotype rate", "heterozygosity rate (N - O) / N")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left", markerscale=1.5)

# X-chromosome F for the sex check
b = C.axes_at(ax, (18.6, 1.6, 10.6, 8.0))
males = rng.normal(0.995, 0.006, 1000)
females = rng.normal(0.0, 0.035, 1000)
males[17] = rng.normal(0.0, 0.035)          # reported male, genetically female
females[402] = rng.normal(0.995, 0.006)     # reported female, genetically male
bins = np.linspace(-0.2, 1.05, 64)
b.hist(females, bins=bins, color=P.light("receptor"), edgecolor=P.edge("receptor"), lw=0.4, label="reported female")
b.hist(males, bins=bins, color=P.light("dna"), edgecolor=P.edge("dna"), lw=0.4, label="reported male")
for x in (0.2, 0.8):
    b.axvline(x, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
b.set_yscale("log")
b.set_ylim(0.7, 2000)
b.annotate("female with F ~ 1", (0.995, 1.0), (0.45, 40), fontsize=bio.core.FONT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
b.annotate("male with F ~ 0", (0.0, 1.0), (0.25, 8), fontsize=bio.core.FONT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
C.style_axes(b, "X-chromosome inbreeding estimate F", "samples")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper center")
bio.panel(ax, "A", (0.3, 10.2))
bio.panel(ax, "B", (16.8, 10.2))
