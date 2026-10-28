"""The Luria-Delbruck fluctuation test, simulated.
Fifty parallel cultures grow from N0 = 1000 to Nt = 2e8 cells. Random (spontaneous) mutation: resistance mutations
occur during growth at rate mu = 6e-9 per cell division, so m = mu (Nt - N0) = 1.2 mutations per culture on average;
a mutation that occurs when the culture has N cells founds a clone whose final size is geometric with mean Nt/N
(Lea-Coulson model). Induced mutation: each of the Nt cells becomes resistant only on contact with the selective
agent, independently, so the count is Poisson with the same median as the random-mutation cultures.
(A) Histogram of mutant counts per culture on logarithmic bins. (B) Counts of the fifty cultures in rank order
(log scale; zero counts drawn at 0.5). Random mutation gives many cultures with no mutants and a few "jackpots"."""

import numpy as np
from scipy.stats import poisson

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

C, N0, Nt, m = 50, 1e3, 2e8, 1.2
M = rng.poisson(m, C)
ld = np.array([rng.geometric(rng.uniform(N0, Nt, k) / Nt).sum() if k else 0 for k in M])
lam = max(np.median(ld), 1.0)
ind = poisson.rvs(lam, size=C, random_state=rng)

fig, ax = bio.canvas(16.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.9, 1.3, 5.6, 5.6))
edges = np.array([0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096])
labels = ["0", "1", "2-3", "4-7", "8-15", "16-31", "32-63", "64-127", "128-255", "256-511", "512-1023", "1024+"]
hl, _ = np.histogram(ld, bins=edges)
hi, _ = np.histogram(ind, bins=edges)
x = np.arange(len(labels))
a.bar(x - 0.2, hi, width=0.4, color=charts.line("channel"), label=f"induced (Poisson, mean {lam:g})")
a.bar(x + 0.2, hl, width=0.4, color=charts.line("negative"), label="random mutation (Luria–Delbrück)")
a.set_xticks(x)
a.set_ylim(0, 31)
a.set_xticklabels(labels, rotation=60, fontsize=FT["tiny"])
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "resistant mutants per culture", "number of cultures")

bio.panel(ax, "B", (8.3, 7.5))
b = charts.axes_at(ax, (10.1, 1.3, 5.6, 5.6))
r = np.arange(1, C + 1)
b.plot(r, np.maximum(np.sort(ind)[::-1], 0.5), "o", color=charts.line("channel"), ms=3.5, label="induced")
b.plot(r, np.maximum(np.sort(ld)[::-1], 0.5), "o", color=charts.line("negative"), ms=3.5, label="random mutation")
b.set_yscale("log")
b.set_xlim(0, C + 1)
b.text(C, 0.62, "zero counts", fontsize=FT["tiny"], color=P.muted(), ha="right")
vr_l = ld.var(ddof=1) / ld.mean()
vr_i = ind.var(ddof=1) / ind.mean()
b.text(C * 0.95, 0.6 * b.get_ylim()[1], f"variance/mean: random {vr_l:.0f}, induced {vr_i:.1f}",
       fontsize=FT["tiny"], color=P.ink(), ha="right", va="top")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(b, "culture (ranked by count)", "resistant mutants")
