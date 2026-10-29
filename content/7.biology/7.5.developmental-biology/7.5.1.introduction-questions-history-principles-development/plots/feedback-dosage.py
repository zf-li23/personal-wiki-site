"""Negative autoregulation buffers gene dosage.

Model (dimensionless): a gene present in g copies (g = 1 in the wild type, 0.5 in a heterozygote for a
null allele, 1.5 or 2 with extra copies) makes a protein X that represses its own promoter:
    du/dt = g a / (1 + u^n) - u,        u = X / K,  a = beta / (gamma K),
with Hill coefficient n (n = 0: no feedback, constant production g a / 2). At steady state
u (1 + u^n) = g a, and the logarithmic sensitivity of u to g is S = 1 / (1 + n u^n / (1 + u^n)), which tends
to 1 / (1 + n) for strong repression (u >> 1).
A: the circuit. B: steady-state level against gene dosage (both relative to the wild type, log scales) for
n = 0, 1, 2, 4 with a = 20. C: steady-state levels in 4000 cells whose production rate varies by a
log-normal factor (standard deviation 0.3 of ln g): without feedback the spread equals that of the input;
with n = 4 it is about five times narrower.
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(30, 10.4)
a = 20.0


def steady(g, n):
    if n == 0:
        return g * a / 2
    return brentq(lambda u: u * (1 + u**n) - g * a, 0, g * a + 1)


# A: circuit
bio.panel(ax, "A", (0.2, 10.2))
ax.plot([0.8, 7.6], [5.2, 5.2], color=P.ink(), lw=2.0, zorder=5)
bio.box(ax, (2.2, 5.2), 1.2, 0.7, "dna", text="P")
bio.box(ax, (4.6, 5.2), 2.6, 0.75, "dna2", text="gene (g copies)", size="small")
bio.box(ax, (5.3, 7.9), 1.5, 0.9, "protein", text="X")
bio.arrow(ax, (4.8, 5.7), (5.2, 7.35), kind="process")
bio.label(ax, (6.2, 6.5), "synthesis\n∝ g", size="tiny", ha="left")
bio.arrow(ax, (4.6, 8.0), (2.25, 5.65), kind="inhibition", bend=0.25)
bio.label(ax, (1.6, 7.6), "represses its\nown promoter", size="tiny")
bio.arrow(ax, (6.1, 7.9), (7.5, 7.9), kind="process")
bio.label(ax, (7.6, 7.9), "decay", size="tiny", ha="left")
bio.label(ax, (4.2, 3.4), "du/dt = g a / (1 + uⁿ) − u", size="small")
bio.label(ax, (4.2, 2.6), "S = d ln u / d ln g = 1 / (1 + n uⁿ/(1 + uⁿ))", size="tiny", color=P.muted())

# B: dose response
bio.panel(ax, "B", (9.6, 10.2))
p = quant.Plot(ax, (11.4, 2.0, 7.0, 7.4), xlim=(0.25, 4), ylim=(0.25, 4), xlog=True, ylog=True,
               xlabel="gene dosage g (relative)", ylabel="steady-state X (relative)",
               xticks=[(0.25, "0.25"), (0.5, "0.5"), (1, "1"), (2, "2"), (4, "4")],
               yticks=[(0.25, "0.25"), (0.5, "0.5"), (1, "1"), (2, "2"), (4, "4")], grid=True)
gs = np.geomspace(0.25, 4, 80)
toks = {0: "negative", 1: "highlight", 2: "enzyme", 4: "dna"}
for n, tok in toks.items():
    u1 = steady(1.0, n)
    us = np.array([steady(g, n) for g in gs]) / u1
    p.line(gs, us, tok, text=("no feedback" if n == 0 else f"n = {n}"), at=0.98, dx=0.1, dy=-0.05, size="tiny")
p.vline(0.5, text="heterozygote", size="tiny")
p.points([0.5], [steady(0.5, 4) / steady(1, 4)], "dna", r=0.09)
p.points([0.5], [0.5], "negative", r=0.09)

# C: distributions under variable production
bio.panel(ax, "C", (20.4, 10.2))
rng = np.random.default_rng(3)
g = np.exp(rng.normal(0, 0.3, 4000))
bins = np.linspace(-1.2, 1.2, 49)
q = quant.Plot(ax, (22.0, 2.0, 7.2, 7.4), xlim=(-1.2, 1.2), ylim=(0, 1.0), xlabel="ln (X / X wild type)",
               ylabel="fraction of cells (scaled)", xticks=[-1, -0.5, 0, 0.5, 1], yticks=[0, 0.5, 1])
for n, tok in ((0, "negative"), (4, "dna")):
    u1 = steady(1.0, n)
    vals = np.log(np.array([steady(x, n) for x in g]) / u1)
    h, _ = np.histogram(vals, bins=bins)
    q.bars(bins, h / h.max() * (0.95 if n == 4 else 0.45), tok, lw=0.4)
    sd = vals.std()
    q.text(0.62 if n == 0 else -0.95, 0.9 if n == 4 else 0.5, f"{'no feedback' if n == 0 else 'n = 4'}\nSD = {sd:.2f}",
           token=tok, size="tiny", ha="left")
