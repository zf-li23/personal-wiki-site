"""Clonal interference in a haploid two-locus model.

Haplotypes ab, Ab, aB, AB with fitnesses 1, 1.05, 1.04, 1.05 * 1.04. Start: Ab = aB = 0.01, AB = 0.
Asexual (r = 0): AB arises only by a new B mutation in an Ab genome, introduced here as a single copy
(frequency 1e-4, population of 10 000) at generation 300. Sexual: recombination at rate r = 0.1.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
w = np.array([1.0, 1.05, 1.04, 1.05 * 1.04])
mu, T = 1e-5, 1200


def run(r):
    x = np.array([0.98, 0.01, 0.01, 0.0])
    out = [x.copy()]
    for _ in range(T):
        x = x * w / (x * w).sum()
        D = x[3] * x[0] - x[1] * x[2]
        x = x + r * D * np.array([-1, 1, 1, -1])
        if r == 0 and _ == 300:
            x = x + np.array([0, -1e-4, 0, 1e-4])
        out.append(x.copy())
    return np.array(out)


fig, ax = bio.canvas(30.0, 10.0)
names = ["ab", "Ab", "aB", "AB"]
toks = ["neutral", "dna", "rna", "protein"]
for k, (r, title, x0) in enumerate(((0.0, "Asexual (r = 0)", 2.2), (0.1, "Sexual (r = 0.1)", 17.5))):
    X = run(r)
    p = C.axes_at(ax, (x0, 1.6, 11.0, 6.8))
    t = np.arange(T + 1)
    for i in range(4):
        p.plot(t, X[:, i], color=C.line(toks[i]) if toks[i] != "neutral" else P.muted(), lw=1.9, label=names[i])
    p.set_xlim(0, T)
    p.set_ylim(0, 1.02)
    C.style_axes(p, "generation", "haplotype frequency")
    p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
    bio.panel(ax, "AB"[k], (x0 - 2.0, 9.8))
    bio.label(ax, (x0, 9.4), title, size="small", bold=True, ha="left")
