"""Joint 95 % confidence regions for (V_max, K_M) of the Puromycin data (Treloar 1974; R datasets::Puromycin),
from the residual sum of squares S(V, K) <= S_min [1 + p/(n - p) F(p, n - p; 0.95)] with p = 2.
Solid: the likelihood-based region (slightly banana-shaped); dashed: the ellipse of the linear (Wald)
approximation. The regions of treated and untreated cells overlap in K but not in V.
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
with open("puromycin.csv") as fh:
    rows = list(csv.DictReader(fh))


def mm(S, V, K):
    return V * S / (K + S)


TOK = {"untreated": "dna", "treated": "rna"}
fig, ax = plt.subplots(figsize=(5.6, 4.0))
fig.subplots_adjust(left=0.14, right=0.97, bottom=0.14, top=0.93)
Vg = np.linspace(130, 250, 241)
Kg = np.linspace(0.015, 0.11, 241)
VV, KK = np.meshgrid(Vg, Kg)
for st in ("treated", "untreated"):
    S = np.array([float(r["conc"]) for r in rows if r["state"] == st])
    v = np.array([float(r["rate"]) for r in rows if r["state"] == st])
    n = S.size
    p, cov = optimize.curve_fit(mm, S, v, p0=[200, 0.05])
    rss = ((v - mm(S, *p)) ** 2).sum()
    SS = ((v[None, None, :] - VV[..., None] * S / (KK[..., None] + S)) ** 2).sum(-1)
    thr = rss * (1 + 2 / (n - 2) * stats.f.ppf(0.95, 2, n - 2))
    col = charts.line(TOK[st])
    ax.contour(VV, KK, SS, levels=[thr], colors=[col], linewidths=1.5)
    # Wald ellipse: (theta - p)' cov^-1 (theta - p) <= 2 F
    c = 2 * stats.f.ppf(0.95, 2, n - 2)
    w, U = np.linalg.eigh(cov)
    tt = np.linspace(0, 2 * np.pi, 200)
    E = (U @ (np.sqrt(c * w)[:, None] * np.vstack([np.cos(tt), np.sin(tt)]))) + p[:, None]
    ax.plot(E[0], E[1], color=col, lw=1.0, ls="--")
    ax.scatter([p[0]], [p[1]], s=24, color=P.fill(TOK[st]), edgecolor=col, zorder=3)
    ax.text(p[0] + 2, p[1] + 0.003, st, fontsize=FT["small"], color=col)
charts.style_axes(ax, "V_max / (counts/min/min)", "K_M / ppm")
charts.title(ax, "Joint 95 % confidence regions")
