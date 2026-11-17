"""Population differentiation and the temporal method of estimating N_e.

A: F_ST in an island model of 10 demes of N = 50 diploids against the number of migrants per generation
N m (points: simulation of 200 biallelic loci, F_ST = Var(p) / (pbar (1 - pbar)) averaged over generations
600-1000), with Wright's 1 / (1 + 4 N m) (line); one migrant per generation already keeps F_ST near 0.2.
B: the temporal method. Wright-Fisher populations of N_e = 50 or 200 diploids with 40 biallelic loci are
sampled (S = 50 individuals) in generations 0 and t = 5; F_c of Nei and Tajima is computed from the two
samples and corrected for sampling (Waples 1989): N_e estimate = t / (2 (F_c - 1/(2 S0) - 1/(2 St))).
Histograms of the estimates from 400 replicate populations (log scale; estimates above 3000 are put in the
last bin, and replicates with a negative corrected F_c, an infinite estimate, are omitted); solid lines:
true values; dashed lines: medians of the estimates.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
fig, ax = bio.canvas(21.0, 10.0)

pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
nd, N, L = 10, 50, 200
Nms = [0.1, 0.25, 0.5, 1, 2, 5]
fst = []
for Nm in Nms:
    m = Nm / N
    p = np.tile(rng.uniform(0.2, 0.8, L), (nd, 1))
    vals = []
    for g in range(1000):
        pbar = p.mean(axis=0)
        pm = (1 - m) * p + m * pbar
        p = rng.binomial(2 * N, pm) / (2 * N)
        if g >= 600 and g % 10 == 0:
            pb_ = p.mean(axis=0)
            den = pb_ * (1 - pb_)
            ok = den > 0.02
            vals.append(p.var(axis=0)[ok].sum() / den[ok].sum())
    fst.append(np.mean(vals))
x = np.logspace(-1.3, 1.0, 200)
pa.semilogx(x, 1 / (1 + 4 * x), color=Q.line_color("protein"), lw=1.6, label="1 / (1 + 4Nm)")
pa.semilogx(Nms, fst, "o", ms=5, color=Q.line_color("enzyme"), label="simulation, 10 demes")
for xx in (0.25, 1):
    pa.plot([xx, xx], [0, 1 / (1 + 4 * xx)], color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.set_xlim(0.05, 10)
pa.set_ylim(0, 1)
C.style_axes(pa, "migrants per generation Nm", "F_ST")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Gene flow and differentiation", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.5, 1.6, 7.5, 6.8))
S, tgen, L2 = 50, 5, 40
bins = np.logspace(1, 3.5, 40)
for Ne, tok in [(50, "dna"), (200, "negative")]:
    est = []
    for _ in range(400):
        p0 = rng.uniform(0.2, 0.8, L2)
        x0 = rng.binomial(2 * S, p0) / (2 * S)
        p = p0.copy()
        for _ in range(tgen):
            p = rng.binomial(2 * Ne, p) / (2 * Ne)
        xt = rng.binomial(2 * S, p) / (2 * S)
        fc_loc = []
        for a, b in [(x0, xt), (1 - x0, 1 - xt)]:
            den = (a + b) / 2 - a * b
            fc_loc.append(np.where(den > 0, (a - b) ** 2 / np.where(den > 0, den, 1), 0))
        Fc = np.mean((fc_loc[0] + fc_loc[1]) / 2)
        corr = Fc - 1 / (2 * S) - 1 / (2 * S)
        est.append(tgen / (2 * corr) if corr > 0 else np.inf)
    est = np.array(est)
    fin = est[np.isfinite(est)]
    pb.hist(np.clip(fin, 10, 3000), bins=bins, color=Q.line_color(tok), alpha=0.45, label=f"true N_e = {Ne}")
    pb.axvline(Ne, color=Q.line_color(tok), lw=1.4)
    pb.axvline(np.median(fin), color=Q.line_color(tok), lw=0.9, ls=(0, (3, 2)))
pb.set_xscale("log")
pb.set_xlim(10, 3000)
C.style_axes(pb, "estimated N_e (log scale)", "number of replicates")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.8, 9.6))
bio.label(ax, (12.5, 9.2), "Temporal estimates of N_e", size="small", bold=True, ha="left")
