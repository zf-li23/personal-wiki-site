"""Multivalency and gelation in the Flory-Stockmayer (tree-like, no loops) theory of two complementary
f-valent molecules at equal concentrations c, whose sites bind with dissociation constant K_d.
A: fraction p of sites that are bound, from mass action p/(1-p)^2 = f c/K_d, with the gel point
p_c = 1/(f-1) (dots). B: fraction of molecules in the system-spanning network (gel fraction) against
c/K_d: the network appears abruptly at c_gel = K_d (f-1)/[f (f-2)^2], which falls steeply with the
valence. C: c_gel/K_d against valence (logarithmic scale): adding sites lowers the threshold by more
than an order of magnitude between f = 3 and f = 8, the trend seen for multivalent SH3/PRM proteins."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.98, bottom=0.17, top=0.87)

toks = {3: "dna", 4: "bacterium", 5: "blood", 6: "lipid_head"}
x = np.logspace(-2.5, 1.5, 400)  # c / K_d


def bound_fraction(cr, f):
    # p/(1-p)^2 = f c/Kd  ->  solve the quadratic for p in (0, 1)
    a = f * cr
    return (2 * a + 1 - np.sqrt(4 * a + 1)) / (2 * a)


def gel_fraction(p, f):
    # Q = probability that a site does not lead to the infinite network: Q = 1 - p + p Q^(f-1)
    if p * (f - 1) <= 1:
        return 0.0
    Q = brentq(lambda q: 1 - p + p * q ** (f - 1) - q, 0, 1 - 1e-12)
    return 1 - Q ** f


ax = axs[0]
for f, tok in toks.items():
    p = bound_fraction(x, f)
    ax.plot(x, p, color=charts.line(tok), lw=1.6, label=f"f = {f}")
    cg = (f - 1) / (f * (f - 2) ** 2)
    ax.plot([cg], [1 / (f - 1)], "o", ms=4, color=charts.line(tok))
ax.set_xscale("log")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$c/K_{\mathrm{d}}$", "bound fraction of sites $p$")
charts.title(ax, "A  Site binding")

ax = axs[1]
for f, tok in toks.items():
    p = bound_fraction(x, f)
    g = np.array([gel_fraction(pi, f) for pi in p])
    ax.plot(x, g, color=charts.line(tok), lw=1.6, label=f"f = {f}")
ax.set_xscale("log")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$c/K_{\mathrm{d}}$", "fraction of molecules in network")
charts.title(ax, "B  Percolation of the network")

ax = axs[2]
fs = np.arange(3, 11)
cg = (fs - 1) / (fs * (fs - 2.0) ** 2)
ax.semilogy(fs, cg, "o-", color=charts.line("protein"), lw=1.6, ms=4)
for f, c in zip(fs, cg):
    if f in (3, 5, 8):
        ax.annotate(f"{c:.3g}", (f, c), xytext=(5, 4), textcoords="offset points", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "valence $f$", r"gel point $c_{\mathrm{gel}}/K_{\mathrm{d}}$")
charts.title(ax, "C  Threshold falls with valence")
