"""Muller's ratchet: individual-based Wright-Fisher simulations.

Each generation: parents sampled with probability proportional to (1 - s)^k; offspring receive
Poisson(U) new mutations. Asexual: offspring inherit the parent's k. Sexual (free recombination,
infinitely many loci): offspring k = Bin(k1, 1/2) + Bin(k2, 1/2) from two parents. U = 0.1, s = 0.02,
start from the Poisson equilibrium with mean U/s = 5. N = 1000 and 10 000 (asexual), 1000 (sexual).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
U, s, T = 0.1, 0.02, 2000
rng = np.random.default_rng(3)


def sim(N, sexual):
    k = rng.poisson(U / s, N)
    kmin, kmean = [], []
    for _ in range(T):
        w = (1 - s) ** k
        w = w / w.sum()
        if sexual:
            a = k[rng.choice(N, N, p=w)]
            b = k[rng.choice(N, N, p=w)]
            k = rng.binomial(a, 0.5) + rng.binomial(b, 0.5)
        else:
            k = k[rng.choice(N, N, p=w)]
        k = k + rng.poisson(U, N)
        kmin.append(k.min())
        kmean.append(k.mean())
    return np.array(kmin), np.array(kmean)


runs = [(1000, False, "asexual, N = 1000", "negative"), (10000, False, "asexual, N = 10 000", "enzyme"),
        (1000, True, "sexual, N = 1000", "protein")]
res = [sim(N, sx) for N, sx, _, _ in runs]
fig, ax = bio.canvas(30.0, 10.0)
t = np.arange(1, T + 1)
for k, (title, x0, idx, ylab) in enumerate((("Least-loaded class", 2.2, 0, "minimum mutations per genome"),
                                          ("Mean load", 17.5, 1, "mean mutations per genome"))):
    p = C.axes_at(ax, (x0, 1.6, 11.0, 6.8))
    for (N, sx, lab, tok), r in zip(runs, res):
        p.plot(t, r[idx], color=C.line(tok), lw=1.5, drawstyle="steps-post" if idx == 0 else "default", label=lab)
    if idx == 1:
        p.axhline(U / s, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
        p.text(T * 0.98, U / s + 0.3, "U/s", color=P.muted(), fontsize=FS["tiny"], ha="right", va="bottom")
    p.set_xlim(0, T)
    p.set_ylim(bottom=0)
    C.style_axes(p, "generation", ylab)
    p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
    bio.panel(ax, "AB"[k], (x0 - 2.0, 9.8))
    bio.label(ax, (x0, 9.4), title, size="small", bold=True, ha="left")
