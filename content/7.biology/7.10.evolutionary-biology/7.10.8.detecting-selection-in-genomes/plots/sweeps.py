"""Hard and soft sweeps (forward Wright-Fisher simulation of 2N = 2000 haploid chromosomes with selection on
a site at position 0 and 16 neutral sites at 0-400 kb, recombination 1e-8 per bp per generation as one
crossover point per offspring, plus an unlinked control site). Neutral sites start at linkage equilibrium
with allele frequency 0.5. The beneficial allele (advantage s = 0.05) starts on 1 chromosome (hard sweep) or
on 20 or 100 randomly chosen chromosomes (soft sweeps from standing variation); runs in which it is lost are
discarded. Shown: heterozygosity just after fixation relative to before, divided by that of the unlinked
site, averaged over 30 completed sweeps; line: Eq. (5.8) for the hard sweep."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(31)
n2, s, L = 2000, 0.05, 16
pos_kb = np.linspace(0, 400, L)
dist = np.append(pos_kb * 1e3 * 1e-8, 0.5)


def run(k0):
    out, done = np.zeros(L + 1), 0
    while done < 30:
        H = (rng.random((n2, L + 1)) < 0.5).astype(np.int8)
        sel = np.zeros(n2, bool)
        sel[rng.choice(n2, k0, replace=False)] = True
        h0 = 2 * H.mean(0) * (1 - H.mean(0))
        while 0 < sel.sum() < n2:
            fit = np.where(sel, 1 + s, 1.0)
            par = rng.choice(n2, size=(n2, 2), p=fit / fit.sum())
            newH = H[par[:, 0]].copy()
            cut = rng.random(n2)
            rows = np.where(cut < dist[L - 1])[0]
            if len(rows):
                mask = dist[None, :L] > cut[rows, None]
                newH[rows, :L] = np.where(mask, H[par[rows, 1], :L], H[par[rows, 0], :L])
            free = rng.random(n2) < 0.5
            newH[free, L] = H[par[free, 1], L]
            H, sel = newH, sel[par[:, 0]]
        if sel.all():
            p = H.mean(0)
            out += 2 * p * (1 - p) / h0
            done += 1
    out /= done
    return out[:L] / out[L]


fig, ax = plt.subplots(figsize=(7.0, 3.9))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.15, top=0.9)
x = np.linspace(0, 400, 200)
ax.plot(x, 1 - n2 ** (-2 * x * 1e3 * 1e-8 / s), color=P.ink(), lw=1, label="Eq. (5.8), hard sweep")
for k0, tok, lab in ((1, "rna", "hard: 1 copy"), (20, "enzyme", "soft: 20 copies"), (100, "dna", "soft: 100 copies")):
    ax.plot(pos_kb, run(k0), color=charts.line(tok), lw=1.6, marker="o", ms=3.5, label=lab)
ax.set_xlim(0, 400)
ax.set_ylim(0, 1.1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "distance from the selected site (kb)", "relative diversity after the sweep")
charts.title(ax, "Hard and soft sweeps")
