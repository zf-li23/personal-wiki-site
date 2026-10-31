"""The MWC model of a ligand-gated channel with n = 2 binding sites (nicotinic acetylcholine
receptor). The closed state is favoured by eps = eps_open - eps_closed (L = e^eps), and the ligand
binds the open state more tightly (K_O < K_C). A: open probability (solid) and occupancy of the
sites (dashed) against c/K_C for K_C/K_O = 100 and eps = 3, 5, 7 kBT: raising eps lowers the
leak 1/(1 + L) and shifts the response to higher concentrations, and activity and occupancy no
longer coincide. B: eps = 5 kBT and K_C/K_O = 10, 100, 1000: the ratio of affinities sets the
ceiling and the sharpness. C: half-maximal concentration EC50 (relative to K_C) and Hill
coefficient of the open probability against eps for K_C/K_O = 100; the Hill coefficient never
exceeds n = 2 and is largest when the switch happens in the middle of the binding range."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
n = 2


def mwc(c, eps, r):
    """c in units of K_C; r = K_C/K_O."""
    L = np.exp(eps)
    zo, zc = (1 + c * r) ** n, L * (1 + c) ** n
    po = zo / (zo + zc)
    occ = (c * r * (1 + c * r) ** (n - 1) + L * c * (1 + c) ** (n - 1)) / (zo + zc)
    return po, occ


def ec50_nh(eps, r):
    p0, pinf = mwc(np.array([0.0]), eps, r)[0][0], mwc(np.array([1e12]), eps, r)[0][0]
    f = lambda lc: (mwc(np.array([10 ** lc]), eps, r)[0][0] - p0) / (pinf - p0)
    l50 = brentq(lambda lc: f(lc) - 0.5, -10, 10)
    h = 1e-4
    lgt = lambda y: np.log(y / (1 - y))
    nh = (lgt(f(l50 + h)) - lgt(f(l50 - h))) / (2 * h * np.log(10))
    return 10 ** l50, nh


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.45, left=0.07, right=0.97, bottom=0.17, top=0.88)
c = np.logspace(-4, 2, 500)

ax = axs[0]
for eps, tok in ((3.0, "enzyme"), (5.0, "channel"), (7.0, "protein")):
    po, occ = mwc(c, eps, 100.0)
    ax.plot(c, po, color=charts.line(tok), lw=1.8, label=rf"$\varepsilon = {eps:.0f}$")
    ax.plot(c, occ, color=charts.line(tok), lw=0.9, ls="--")
ax.set_xscale("log")
ax.set_ylim(-0.02, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$c/K_\mathrm{C}$", r"$p_\mathrm{open}$ (solid), occupancy (dashed)")
charts.title(ax, r"A  $K_\mathrm{C}/K_\mathrm{O} = 100$")

ax = axs[1]
for r, tok in ((10.0, "neutral"), (100.0, "channel"), (1000.0, "blood")):
    po, _ = mwc(c, 5.0, r)
    ax.plot(c, po, color=charts.line(tok), lw=1.8, label=rf"$K_\mathrm{{C}}/K_\mathrm{{O}} = {r:.0f}$")
ax.set_xscale("log")
ax.set_ylim(-0.02, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$c/K_\mathrm{C}$", r"$p_\mathrm{open}$")
charts.title(ax, r"B  $\varepsilon = 5\,k_\mathrm{B}T$")

ax = axs[2]
eps = np.linspace(-4, 14, 120)
res = np.array([ec50_nh(e, 100.0) for e in eps])
ax.plot(eps, np.log10(res[:, 0]), color=charts.line("channel"), lw=1.8, label=r"$\log_{10}(\mathrm{EC}_{50}/K_\mathrm{C})$")
ax2 = ax.twinx()
ax2.plot(eps, res[:, 1], color=charts.line("blood"), lw=1.8, ls="--")
ax2.set_ylim(0.9, 2.1)
ax.plot([], [], color=charts.line("blood"), lw=1.8, ls="--", label=r"$n_\mathrm{H}$ (right axis)")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$\varepsilon$ / $k_\mathrm{B}T$", r"$\log_{10}(\mathrm{EC}_{50}/K_\mathrm{C})$")
charts.style_axes(ax2, None, r"$n_\mathrm{H}$", box=True)
ax2.spines["left"].set_visible(False)
charts.title(ax, "C  One energy shifts the curve")
