"""The MWC model of a chemoreceptor cluster (Formula 35.5.1) with parameters fitted to Tar and the
attractant MeAsp: N = 6 receptor dimers per cooperative unit, K_I = 18 uM, K_A = 3 mM, free-energy
offset f(m) = alpha (m0 - m) with alpha = 1.7 kT per methyl group and m0 = 1. A: cluster activity
against attractant concentration for methylation levels m = 1 to 4: methylation shifts the curve to
higher concentrations without changing its shape. B: the gain -da/d(ln c) at fixed m, largest
(N a(1 - a), at most N/4) in the window K_I << c << K_A. C: responses of adapted clusters (a0 = 1/3)
to a step that doubles or halves the concentration, from backgrounds spanning two orders of
magnitude: inside the window the response depends only on the fold change (Weber-Fechner law);
near K_A it fades."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
N, KI, KA, alpha, m0 = 6, 18e-3, 3.0, 1.7, 1.0   # concentrations in mM


def dF(m, c):
    return alpha * (m0 - m) + np.log((1 + c / KI) / (1 + c / KA))


def act(m, c):
    return 1 / (1 + np.exp(N * dF(m, c)))


c = np.logspace(-4, 2, 400)
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.42, left=0.06, right=0.98, bottom=0.17, top=0.88)
toks = ["receptor", "enzyme", "positive", "highlight"]

ax = axs[0]
for m, tok in zip(range(1, 5), toks):
    ax.semilogx(c, act(m, c), color=charts.line(tok), lw=1.4, label=f"m = {m}")
for k in (KI, KA):
    ax.axvline(k, color=P.muted(), lw=0.6, ls=":")
ax.text(KI, 1.03, r"$K_{\mathrm{I}}$", fontsize=7, color=P.ink(), ha="center")
ax.text(KA, 1.03, r"$K_{\mathrm{A}}$", fontsize=7, color=P.ink(), ha="center")
ax.set_ylim(0, 1.1)
ax.legend(frameon=False, fontsize=7, loc="lower left")
charts.style_axes(ax, "MeAsp / mM", "cluster activity a")
charts.title(ax, "A  methylation shifts the response")

ax = axs[1]
for m, tok in zip(range(1, 5), toks):
    a = act(m, c)
    dlna = N * a * (1 - a) * (c / KI / (1 + c / KI) - c / KA / (1 + c / KA))
    ax.semilogx(c, dlna, color=charts.line(tok), lw=1.4)
ax.axhline(N / 4, color=P.muted(), lw=0.7, ls="--")
ax.text(8, N / 4 - 0.12, "N/4", fontsize=7, color=P.ink())
charts.style_axes(ax, "MeAsp / mM", r"gain $-\mathrm{d}a/\mathrm{d}\ln c$")
charts.title(ax, "B  gain")

ax = axs[2]
a0 = 1 / 3
bg = np.logspace(-2.3, 0.7, 40)
for fold, tok, lab in ((2.0, "receptor", "twofold up"), (0.5, "enzyme", "twofold down")):
    resp = []
    for cb in bg:
        # adapted methylation: a(m, cb) = a0
        m = m0 + (np.log((1 + cb / KI) / (1 + cb / KA)) - np.log(1 / a0 - 1) / N) / alpha
        resp.append(act(m, fold * cb) - a0)
    ax.semilogx(bg, resp, color=charts.line(tok), lw=1.4, label=lab)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(KA, color=P.muted(), lw=0.6, ls=":")
ax.legend(frameon=False, fontsize=7, loc="center right")
charts.style_axes(ax, "background MeAsp / mM", r"response $a - a_0$")
charts.title(ax, "C  fold-change response")
