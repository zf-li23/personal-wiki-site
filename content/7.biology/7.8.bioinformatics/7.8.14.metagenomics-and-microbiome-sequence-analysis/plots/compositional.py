# Pitfalls of compositional data. A: four taxa with equal absolute abundance (100 cells each, arbitrary units);
# then taxon D blooms tenfold while A-C are unchanged. Relative abundances (what sequencing measures) of A-C
# fall from 0.25 to 0.077, although nothing happened to them; the log-ratios between A, B and C stay 0. B: 500
# samples of 5 taxa whose absolute abundances vary independently (log-normal, SD 0.6 on the log scale, taxon 1
# more abundant): the absolute abundances of taxa 1 and 2 are uncorrelated, their proportions are negatively
# correlated. C: mean correlation between the proportions of pairs of independent, identically distributed
# taxa against the number of taxa D, from 2000 simulated samples, against -1/(D - 1), the value forced by the
# constraint that proportions sum to 1.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 10.6)
a = C.axes_at(ax, (1.8, 1.6, 7.6, 7.6))
before = np.array([100, 100, 100, 100.0])
after = np.array([100, 100, 100, 1000.0])
toks = ["dna", "enzyme", "protein", "rna"]
for k, (vec, x0) in enumerate([(before, 0), (after, 1), (before / before.sum(), 2.6), (after / after.sum(), 3.6)]):
    bottom = 0
    tot = 1300.0 if k < 2 else 1.0                  # absolute bars on a common scale
    for i, v in enumerate(vec):
        h = v / tot
        a.bar(x0, h, bottom=bottom, width=0.7, color=P.fill(toks[i]), edgecolor=P.edge(toks[i]), lw=0.6)
        if h > 0.06:
            a.text(x0, bottom + h / 2, f"{'ABCD'[i]}: {v:.0f}" if k < 2 else f"{'ABCD'[i]}: {v:.3f}",
                   ha="center", va="center", fontsize=bio.core.FONT["tiny"], color=P.on_fill())
        bottom += h
a.set_xticks([0, 1, 2.6, 3.6])
a.set_xticklabels(["before", "after", "before", "after"])
a.set_yticks([])
a.text(0.5, 1.05, "absolute abundance", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.text(3.1, 1.05, "relative abundance", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_ylim(0, 1.12)
C.style_axes(a, None, None)
n, Dn = 500, 5
absl = np.exp(rng.normal(0, 0.6, (n, Dn)) + np.array([1.0, 0, 0, 0, 0]))
prop = absl / absl.sum(1, keepdims=True)
b = C.axes_at(ax, (12.2, 1.6, 7.0, 7.6))
r_abs = np.corrcoef(absl[:, 0], absl[:, 1])[0, 1]
r_prop = np.corrcoef(prop[:, 0], prop[:, 1])[0, 1]
b.scatter(prop[:, 0], prop[:, 1], s=6, color=C.line("rna"), lw=0, alpha=0.6)
b.text(0.97, 0.95, f"proportions: r = {r_prop:.2f}\nabsolute abundances: r = {r_abs:.2f}", transform=b.transAxes,
       ha="right", va="top", fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(b, "proportion of taxon 1", "proportion of taxon 2")
c = C.axes_at(ax, (22.6, 1.6, 6.8, 7.6))
Ds = np.array([2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 50])
mc = []
for d in Ds:
    x = np.exp(rng.normal(0, 0.6, (2000, d)))
    pr = x / x.sum(1, keepdims=True)
    R = np.corrcoef(pr.T)
    mc.append(R[np.triu_indices(d, 1)].mean())
dd = np.linspace(2, 50, 200)
c.plot(dd, -1 / (dd - 1), color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="-1 / (D - 1)")
c.plot(Ds, mc, "o", color=C.line("protein"), ms=4, label="simulated")
c.axhline(0, color=P.muted(), lw=0.6)
c.set_xscale("log")
c.set_xticks([2, 5, 10, 20, 50])
c.set_xticklabels(["2", "5", "10", "20", "50"])
C.style_axes(c, "number of taxa D", "mean correlation of proportions")
c.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.2, 10.2))
bio.panel(ax, "B", (10.6, 10.2))
bio.panel(ax, "C", (21.0, 10.2))
