"""One count model for the whole course: sampling noise plus biological variation.

A: squared coefficient of variation of a count with mean mu, CV^2 = 1/mu + phi, for Poisson
sampling alone (phi = 0) and for negative binomial counts with the dispersions used in the
chapters: phi = 0.05 for bulk RNA-seq replicates (Example 2.2.1) and phi = 1/theta = 0.1 for UMI
counts (Example 5.4.1). The Poisson part falls with depth, the biological part is a floor.
B: standard error of a log fold change between two groups of n replicates,
sqrt((1/mu_A + 1/mu_B + 2 phi)/n) with mu_B = 2 mu_A and phi = 0.05 (the variance formula of
Example 2.2.1), against the mean count mu_A per library for n = 3 and n = 6. Dots: the two designs of one budget
in Example 2.2.1 (3 libraries at mu_A = 20, 6 at mu_A = 10). Dotted lines: the
floors sqrt(2 phi / n) at infinite depth. The same structure governs splicing ratios between
replicates (Algorithm 4.1.1), pseudobulk comparisons (Definition 5.6.1), methylation (Formula 8.5.1)
and guide counts (Formula 10.7.1)."""

import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(8.6, 3.5))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.16, top=0.88, wspace=0.32)

mu = np.logspace(-1, 4, 300)
for phi, tok, lab in ((0.0, "neutral", "Poisson (sampling only)"), (0.05, "rna", "NB, φ = 0.05 (bulk replicates)"),
                      (0.1, "protein", "NB, φ = 0.1 (UMI counts)")):
    a.loglog(mu, 1 / mu + phi, color=charts.line(tok), lw=1.8, label=lab)
    if phi:
        a.axhline(phi, color=charts.line(tok), lw=0.8, ls=":")
a.set_ylim(5e-3, 20)
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, loc="upper right")
charts.style_axes(a, "mean count μ", "CV² = Var / μ²")
charts.title(a, "A  sampling noise falls, biology stays")

phi = 0.05
muA = np.logspace(0, 4, 300)
for n, tok in ((3, "rna"), (6, "enzyme")):
    se = np.sqrt((1 / muA + 1 / (2 * muA) + 2 * phi) / n)
    b.semilogx(muA, se, color=charts.line(tok), lw=1.8, label=f"n = {n} per group")
    b.axhline(np.sqrt(2 * phi / n), color=charts.line(tok), lw=0.8, ls=":")
# the two designs of one budget of 120 million reads in Example 2.2.1
for m, n, tok in ((20, 3, "rna"), (10, 6, "enzyme")):
    s = np.sqrt((1 / m + 1 / (2 * m) + 2 * phi) / n)
    b.plot(m, s, "o", ms=5, mfc=P.fill(tok), mec=P.edge(tok), zorder=5)
b.set_ylim(0, 0.75)
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, loc="upper right")
b.text(1.3, 0.04, "floors: √(2φ/n)", fontsize=bio.core.FONT["tiny"], color=P.muted())
charts.style_axes(b, "mean count per library in group A", "s.e. of ln fold change")
charts.title(b, "B  replicates, not reads")
