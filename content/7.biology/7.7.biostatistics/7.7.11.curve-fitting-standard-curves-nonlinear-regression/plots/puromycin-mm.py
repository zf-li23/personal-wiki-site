"""Michaelis-Menten fit to the Puromycin data (Treloar 1974; R datasets::Puromycin): initial rate of a
galactosyltransferase reaction (counts/min/min) against substrate concentration (ppm), for cells treated
with puromycin and untreated. A: nonlinear least-squares fits (solid) and, for the treated cells, the
curve implied by the Lineweaver-Burk line (dashed), which underestimates the plateau. B: the
double-reciprocal plot of the treated cells; the bars show how a fixed error of one residual SD in the
rate (about 11 counts/min/min) becomes in 1/v: tiny at high [S], huge at the two lowest concentrations,
which therefore dominate the straight-line fit.
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
data = {}
for st in ("treated", "untreated"):
    S = np.array([float(r["conc"]) for r in rows if r["state"] == st])
    v = np.array([float(r["rate"]) for r in rows if r["state"] == st])
    data[st] = (S, v)


def mm(S, V, K):
    return V * S / (K + S)


TOK = {"untreated": "dna", "treated": "rna"}
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.87, wspace=0.27)
ax = axs[0]
g = np.linspace(0, 1.15, 200)
for st, (S, v) in data.items():
    p, _ = optimize.curve_fit(mm, S, v, p0=[200, 0.05])
    ax.scatter(S, v, s=18, color=P.fill(TOK[st]), edgecolor=charts.line(TOK[st]), lw=0.8, zorder=3, label=st)
    ax.plot(g, mm(g, *p), color=charts.line(TOK[st]), lw=1.5)
    ax.text(1.13, mm(1.13, *p) + 4, f"V = {p[0]:.0f}, K = {p[1]:.3f}", fontsize=FT["tiny"], color=P.ink(), ha="right")
S, v = data["treated"]
r = stats.linregress(1 / S, 1 / v)
Vlb, Klb = 1 / r.intercept, r.slope / r.intercept
ax.plot(g, mm(g, Vlb, Klb), color=charts.line("rna"), lw=1.2, ls="--")
ax.text(0.75, mm(0.75, Vlb, Klb) - 14, "Lineweaver-Burk", fontsize=FT["tiny"], color=charts.line("rna"))
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
ax.set_xlim(0, 1.15)
ax.set_ylim(0, 235)
charts.style_axes(ax, "[S] / ppm", "v / (counts/min/min)")
charts.title(ax, "A  Nonlinear least squares")

ax = axs[1]
p, _ = optimize.curve_fit(mm, S, v, p0=[200, 0.05])
sd = np.sqrt(((v - mm(S, *p)) ** 2).sum() / (S.size - 2))
for s_, v_ in zip(S, v):
    ax.plot([1 / s_] * 2, [1 / (v_ + sd), 1 / max(v_ - sd, 1)], color=P.muted(), lw=1.0)
ax.scatter(1 / S, 1 / v, s=18, color=P.fill("rna"), edgecolor=charts.line("rna"), lw=0.8, zorder=3)
gx = np.linspace(0, 52, 50)
ax.plot(gx, r.intercept + r.slope * gx, color=charts.line("rna"), lw=1.2, ls="--")
ax.plot(gx, 1 / p[0] + p[1] / p[0] * gx, color=charts.line("rna"), lw=1.5)
ax.set_xlim(0, 52)
ax.set_ylim(0, 0.028)
charts.style_axes(ax, "1/[S] / ppm⁻¹", "1/v")
charts.title(ax, "B  Double-reciprocal plot (treated)")
