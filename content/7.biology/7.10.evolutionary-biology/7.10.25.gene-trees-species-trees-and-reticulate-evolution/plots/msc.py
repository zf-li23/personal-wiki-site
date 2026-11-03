"""Gene trees under the multispecies coalescent. A: for three species with species tree ((A, B), C),
the probability that the rooted gene tree of one sequence per species matches the species tree,
1 - (2/3) exp(-T), and the probability of each of the two discordant gene trees, (1/3) exp(-T),
against the length T of the internal branch in coalescent units (lines), with simulated frequencies
(dots, 4000 loci each). B: the anomaly zone for four species with the asymmetric species tree
(((A, B), C), D): x and y are the lengths of the two internal branches (the younger and the older,
in coalescent units). In the shaded region the symmetric gene tree ((A, B), (C, D)) is more probable
than the gene tree that matches the species tree (exact probabilities computed by enumerating the
coalescent histories); the line is the boundary y = a(x) of Degnan and Rosenberg (2006)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(8)
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
T = np.linspace(0, 3, 200)
a.plot(T, 1 - 2 / 3 * np.exp(-T), color=charts.line("dna"), lw=1.8, label="gene tree = species tree")
a.plot(T, np.exp(-T) / 3, color=charts.line("rna"), lw=1.5, label="each discordant gene tree")
a.axhline(1 / 3, color=P.muted(), lw=0.6, ls=":")
for t in (0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0):
    n = 4000
    early = rng.random(n) < 1 - np.exp(-t)
    first = rng.integers(0, 3, n)
    conc = early | (first == 0)
    a.scatter([t], [conc.mean()], s=14, color=charts.line("dna"), zorder=4)
    a.scatter([t], [((~early) & (first == 1)).mean()], s=14, color=charts.line("rna"), zorder=4)
a.set_ylim(0, 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(a, "internal branch $T$ (coalescent units)", "probability")
charts.title(a, "A  Three species: concordance $1 - \\frac{2}{3}\\mathrm{e}^{-T}$")


def probs(x, y):
    p1, e = 1 - np.exp(-x), np.exp(-x)
    g33 = np.exp(-3 * y)
    g32 = 1.5 * (np.exp(-y) - np.exp(-3 * y))
    g31 = 1 - g33 - g32
    conc = p1 * ((1 - np.exp(-y)) + np.exp(-y) / 3) + e * (g31 / 3 + g32 / 9 + g33 / 18)
    bal = p1 * np.exp(-y) / 3 + e * (g32 / 9 + g33 * 2 / 18)
    return conc, bal


xs = np.linspace(0.002, 0.4, 300)
ys = np.linspace(0.002, 0.4, 300)
X, Y = np.meshgrid(xs, ys)
c, bl = probs(X, Y)
b.contourf(X, Y, (bl > c).astype(float), levels=[0.5, 1.5], colors=[P.fill("highlight")], alpha=0.6)
az = np.log(2 / 3 + (3 * np.exp(2 * xs) - 2) / (18 * (np.exp(3 * xs) - np.exp(2 * xs))))
ok = (az > 0) & (az < 0.4)
b.plot(az[ok], xs[ok], color=P.ink(), lw=1.2)
b.text(0.03, 0.05, "anomaly zone:\n((A,B),(C,D)) more\nprobable than\n(((A,B),C),D)", fontsize=FT["tiny"], color=P.ink())
b.set_xlim(0, 0.4)
b.set_ylim(0, 0.4)
charts.style_axes(b, "younger internal branch $x$", "older internal branch $y$")
charts.title(b, "B  Four species: the anomaly zone")
