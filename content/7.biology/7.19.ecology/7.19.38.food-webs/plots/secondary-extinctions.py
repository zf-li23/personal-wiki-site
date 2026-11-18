"""Secondary extinctions and food-web robustness (after Dunne et al. 2002).

Niche-model food webs (S = 50) are subjected to sequential removal of species (primary extinctions).
After each removal, every consumer left without any prey (cannibalistic links ignored) goes extinct,
repeatedly, until no further losses occur (secondary extinctions); basal species suffer only primary
extinction. Orders: most connected first (total degree, recomputed after each step), random, and
most connected first among non-basal species (basal species removed only when no other species is
left). A: fraction of the original species remaining against the fraction removed,
mean of 40 webs with C = 0.10 (random order: mean of 5 permutations per web). B: robustness R50, the
fraction of species that must be removed for at least half of all species to be lost, against
connectance (20 webs per value).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(7)
fig, ax = bio.canvas(30.0, 12.0)

S = 50


def niche_web(Ct):
    while True:
        n = np.sort(rng.random(S))
        r = rng.beta(1, 1 / (2 * Ct) - 1, S) * n
        r[0] = 0
        c = rng.uniform(r / 2, n)
        A = (n[None, :] >= (c - r / 2)[:, None]) & (n[None, :] <= (c + r / 2)[:, None])
        np.fill_diagonal(A, False)
        if ((A.sum(0) + A.sum(1)) > 0).all():
            return A


def removal(A, order):
    alive = np.ones(S, bool)
    basal = A.sum(1) == 0
    remaining = [1.0]
    for step in range(S):
        if not alive.any():
            remaining.append(0.0)
            continue
        idx = np.flatnonzero(alive)
        if order == "random":
            v = rng.choice(idx)
        else:
            sub = A[np.ix_(alive, alive)]
            deg = sub.sum(0) + sub.sum(1)
            if order == "nonbasal" and (~basal[idx]).any():
                deg = np.where(basal[idx], -1, deg)
            v = idx[np.argmax(deg)]
        alive[v] = False
        changed = True
        while changed:
            prey = (A[:, alive].sum(1) > 0)
            dead = alive & ~basal & ~prey
            changed = dead.any()
            alive &= ~dead
        remaining.append(alive.sum() / S)
    return np.array(remaining)


def r50(rem):
    frac = np.arange(S + 1) / S
    return frac[np.argmax(rem <= 0.5)]


orders = [("most", "most connected first", "negative"), ("random", "random", "dna"),
          ("nonbasal", "most connected first, basal species spared", "positive")]
webs = [niche_web(0.10) for _ in range(40)]
fr = np.arange(S + 1) / S
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
for o, lab, tok in orders:
    reps = 5 if o == "random" else 1
    curves = [removal(A, o) for A in webs for _ in range(reps)]
    pa.plot(fr, np.mean(curves, 0), color=Q.line_color(tok), lw=1.8, label=lab)
pa.plot([0, 1], [1, 0], color=P.muted(), lw=0.9, ls=":", label="no secondary extinctions")
pa.axhline(0.5, color=P.muted(), lw=0.7, ls="--")
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.02)
C.style_axes(pa, "fraction of species removed", "fraction of species remaining")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Extinction sequences (S = 50, C = 0.10)", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
Cs = [0.04, 0.07, 0.10, 0.15, 0.20, 0.25]
for o, lab, tok in orders:
    vals = []
    for Ct in Cs:
        ws = [niche_web(Ct) for _ in range(20)]
        reps = 3 if o == "random" else 1
        vals.append(np.mean([r50(removal(A, o)) for A in ws for _ in range(reps)]))
    pb.plot(Cs, vals, "o-", ms=3, color=Q.line_color(tok), lw=1.6, label=lab)
pb.set_xlim(0.03, 0.26)
pb.set_ylim(0, 0.52)
C.style_axes(pb, "connectance C", "robustness R50")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Robustness increases with connectance", size="small", bold=True, ha="left")
