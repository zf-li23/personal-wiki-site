"""Why a plate count recovers only a small fraction of the cells in a natural sample (illustrative simulation).

A community of 3000 species with log-normally distributed abundances (log10 of the number of cells per gram
has mean 5 and standard deviation 0.9), about 1e9 cells per gram in total.
A: Preston plot, the number of species per doubling class (octave) of abundance; the species that grow on a
given plate medium (here 3% of species, chosen with a weight proportional to 1/abundance, i.e. the
fast-growing "weeds" that are rare in nature) are shown in the darker bars.
B: fraction of all cells that belong to culturable species, as a function of the fraction of species that is
culturable, when culturability is independent of abundance (diagonal on average) and when it is biased toward
rare species; mean of 200 random draws, band = 5th to 95th percentile. The shaded band marks the 0.1-1%
ratio of plate count to direct count typical of soils and seawater.
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
S = 3000
logN = rng.normal(5.0, 0.9, S)
N = 10 ** logN
w_rare = 1.0 / N


def draw(frac, weights, reps=200):
    k = max(1, int(round(frac * S)))
    out = []
    p = weights / weights.sum()
    for _ in range(reps):
        idx = rng.choice(S, size=k, replace=False, p=p)
        out.append(N[idx].sum() / N.sum())
    out = np.array(out)
    return out.mean(), np.percentile(out, 5), np.percentile(out, 95)


fig, ax = bio.canvas(24.0, 10.0)

# A: Preston plot ------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 9.8))
cult = rng.choice(S, size=int(0.03 * S), replace=False, p=w_rare / w_rare.sum())
oct_ = np.floor(np.log2(N)).astype(int)
lo, hi = oct_.min(), oct_.max()
edges = np.arange(lo, hi + 2)
counts = np.array([(oct_ == o).sum() for o in range(lo, hi + 1)])
ccounts = np.array([(oct_[cult] == o).sum() for o in range(lo, hi + 1)])
ymax = 500
pa = quant.Plot(ax, (2.0, 1.5, 8.5, 7.0), xlim=(lo, hi + 1), ylim=(0, ymax),
                xlabel="abundance / (cells g⁻¹), log₂ classes", ylabel="number of species",
                xticks=[(np.log2(10 ** k), "10" + "⁰¹²³⁴⁵⁶⁷⁸⁹"[k]) for k in range(3, 9)],
                yticks=[0, 100, 200, 300, 400, 500], grid=True)
pa.bars(edges, counts, "neutral")
pa.bars(edges, ccounts, "positive")
pa.text(hi - 1.0, 470, "all species (3000)", token="neutral", ha="right")
pa.text(hi - 1.0, 430, "culturable on the plate (3%)", token="positive", ha="right")

# B: fraction of cells vs fraction of species --------------------------------------------------------
bio.panel(ax, "B", (13.0, 9.8))
fr = np.linspace(0.005, 0.2, 30)
ind = np.array([draw(f, np.ones(S)) for f in fr])
rar = np.array([draw(f, w_rare) for f in fr])
pb = quant.Plot(ax, (15.0, 1.5, 8.0, 7.0), xlim=(0, 0.2), ylim=(1e-4, 0.3), ylog=True,
                xlabel="fraction of species culturable", ylabel="fraction of cells recovered",
                xticks=[0, 0.05, 0.1, 0.15, 0.2],
                yticks=[(1e-4, "0.01%"), (1e-3, "0.1%"), (1e-2, "1%"), (1e-1, "10%")], grid=True)
pb.band(fr, np.full_like(fr, 0.001), np.full_like(fr, 0.01), "highlight", alpha=0.18)
pb.band(fr, ind[:, 1], ind[:, 2], "neutral", alpha=0.3)
pb.band(fr, rar[:, 1], rar[:, 2], "positive", alpha=0.35)
pb.line(fr, ind[:, 0], "neutral", lw=1.8, text="independent of abundance", at=0.45, dx=-0.2, dy=0.35, ha="right")
pb.line(fr, rar[:, 0], "positive", lw=1.8, text="biased toward rare species", at=0.6, dx=0.0, dy=-0.45)
pb.text(0.198, 0.0105, "typical plate count / direct count", ha="right", va="bottom", color=P.muted())
