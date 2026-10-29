"""Reaggregation as coagulation: the Smoluchowski equation with three kernels.

p_k(t) is the number of k-cell clusters divided by the total number of cells, so sum_k k p_k = 1.
dp_k/dt = (1/2) sum_{l<k} f(k-l, l) p_{k-l} p_l - p_k sum_l f(k, l) p_l, starting from single cells.
A: constant kernel f = 1. Lines: the exact solution p_k = 4 t^(k-1) / (2 + t)^(k+1) (k = 1..4);
dots: a stochastic (Marcus-Lushnikov) simulation of N = 3000 cells in which every pair of clusters
merges at rate 1/N.
B: weight-average cluster size S = sum_k k^2 p_k from stochastic simulations (N = 3000) for the
constant kernel (exact S = 1 + t, dashed), the surface kernel f = (k l)^(2/3) and the product kernel
f = k l, for which S diverges at the gel point t = 1 (exact S = 1/(1 - t) for t < 1, dashed).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
N = 3000
rng = np.random.default_rng(5)


def simulate(kind, tmax, nsamp):
    sizes = [1] * N
    t = 0.0
    out_t, out_p, out_s = [], [], []
    grid = np.linspace(0, tmax, nsamp)
    gi = 0
    while gi < nsamp:
        m = len(sizes)
        if m < 2:
            break
        arr = np.array(sizes, float)
        if kind == "const":
            rate = m * (m - 1) / 2 / N
        elif kind == "prod":
            rate = (arr.sum() ** 2 - (arr ** 2).sum()) / 2 / N
        else:
            w = arr ** (2 / 3)
            rate = (w.sum() ** 2 - (w ** 2).sum()) / 2 / N
        dt = rng.exponential(1 / rate)
        while gi < nsamp and grid[gi] <= t + dt:
            cnt = np.bincount(np.array(sizes), minlength=6)
            out_t.append(grid[gi])
            out_p.append(cnt[1:6] / N)
            out_s.append((arr ** 2).sum() / N)
            gi += 1
        t += dt
        if kind == "const":
            i, j = rng.choice(m, 2, replace=False)
        else:
            w = arr if kind == "prod" else arr ** (2 / 3)
            pr = w / w.sum()
            while True:
                i, j = rng.choice(m, 2, p=pr)
                if i != j:
                    break
        a, b = (i, j) if i > j else (j, i)
        sizes[b] += sizes[a]
        sizes.pop(a)
    return np.array(out_t), np.array(out_p), np.array(out_s)


tc, pc_, sc = simulate("const", 8.0, 17)
_, _, ss = simulate("surf", 2.0, 21)
tp, _, sp = simulate("prod", 1.2, 25)

fig, ax = bio.canvas(30.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.0, 1.8, 11.0, 7.0))
tt = np.linspace(0, 8, 300)
toks = ["mesoderm", "ectoderm", "positive", "protein"]
for k in range(1, 5):
    col = quant.line_color(toks[k - 1])
    pa.plot(tt, 4 * tt ** (k - 1) / (2 + tt) ** (k + 1), color=col, lw=2.0, label=f"k = {k}")
    pa.plot(tc, pc_[:, k - 1], "o", color=col, ms=3.5)
pa.set_xlim(0, 8)
pa.set_ylim(0, 1.02)
charts.style_axes(pa, "time t (units of 1/(rate × cell density))", "clusters of k cells per cell, p_k")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper right")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pa, "Constant kernel: exact solution (lines) and simulation (dots)")

bio.panel(ax, "B", (16.0, 9.9))
pb = charts.axes_at(ax, (18.0, 1.8, 11.0, 7.0))
pb.plot(tc[tc <= 2.0], sc[tc <= 2.0], "o-", color=quant.line_color("ectoderm"), lw=1.6, ms=3, label="f = 1")
pb.plot(np.linspace(0, 2, 21), ss, "o-", color=quant.line_color("highlight"), lw=1.6, ms=3, label="f = (kl)^(2/3)")
pb.plot(tp, sp, "o-", color=quant.line_color("mesoderm"), lw=1.6, ms=3, label="f = kl")
x = np.linspace(0, 2, 50)
pb.plot(x, 1 + x, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
x = np.linspace(0, 0.93, 50)
pb.plot(x, 1 / (1 - x), color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.axvline(1.0, color=P.muted(), lw=0.8)
pb.text(1.03, 40, "gel point", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_yscale("log")
pb.set_xlim(0, 2)
pb.set_ylim(1, 3000)
charts.style_axes(pb, "time t", "weight-average size S")
leg = pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper left")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pb, "Growth laws differ with the kernel")
