"""Artificial selection on a polygenic behavioral trait: up, down and control lines for h2 = 0.4 and 0.1.

Additive model: 100 biallelic loci (effects +/-a), diploid, N = 200, truncation selection of 20 percent,
random mating among selected parents, free recombination. Environmental variance set to give the target h2.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(2)
L, N, G, frac = 100, 200, 12, 0.2


def run(h2, direction, rng):
    geno = (rng.random((N, 2, L)) < 0.5).astype(float)
    va0 = 2 * L * 0.25  # additive variance with a = 1, p = 0.5
    ve = va0 * (1 - h2) / h2
    means = []
    for g in range(G + 1):
        gv = geno.sum(axis=(1, 2)) - L
        ph = gv + rng.normal(0, np.sqrt(ve), N)
        means.append(ph.mean())
        k = int(frac * N)
        if direction == 0:
            idx = rng.choice(N, k, replace=False)
        else:
            idx = np.argsort(direction * ph)[-k:]
        par = geno[idx]
        kids = np.empty_like(geno)
        for i in range(N):
            a, b = par[rng.integers(k)], par[rng.integers(k)]
            ga = np.where(rng.random(L) < 0.5, a[0], a[1])
            gb = np.where(rng.random(L) < 0.5, b[0], b[1])
            kids[i, 0], kids[i, 1] = ga, gb
        geno = kids
    return np.array(means), np.sqrt(va0 / h2)


# selection differential for truncation of 20 percent: i * sigma_P, i = 1.40
i_sel = 1.40
fig, ax = bio.canvas(28.0, 10.0)
for j, h2 in enumerate([0.4, 0.1]):
    p = C.axes_at(ax, (2.6 + 14.0 * j, 1.6, 10.6, 7.2))
    for direction, tok in [(1, "negative"), (0, "neutral"), (-1, "dna")]:
        m, sp = run(h2, direction, rng)
        p.plot(range(G + 1), (m - m[0]) / sp, "o-", color=C.line(tok), lw=1.5, ms=3)
        if direction != 0:
            p.plot([0, G], [0, direction * h2 * i_sel * G], color=C.line(tok), lw=0.9, ls=(0, (3, 2)))
    p.text(0.3, 6.2, f"h² = {h2}", color=P.ink(), fontsize=FS["small"], va="top")
    p.text(G, 6.4 if j == 0 else 2.0, "up", color=C.line("negative"), fontsize=FS["tiny"], ha="right")
    p.text(G, -6.4 if j == 0 else -2.0, "down", color=C.line("dna"), fontsize=FS["tiny"], ha="right", va="top")
    p.set_xlim(0, G)
    p.set_ylim(-7.5, 7.5)
    C.style_axes(p, "generation", "change in mean / phenotypic SD")
    bio.panel(ax, "AB"[j], (0.5 + 14.0 * j, 9.7))
