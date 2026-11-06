# Yield responses to a nutrient.
# A: growth (percent of maximum) against the concentration of one nutrient in a tissue (all other nutrients
#    adequate): deficiency, adequate and toxic zones. Model: Y = 100 (1 - exp(-k (c - c0))) / (1 + exp((c - ct) / s))
#    with c0 = 2, k = 0.12, ct = 95, s = 6 (arbitrary units, illustrative). The critical concentration is the
#    tissue concentration at 90 % of the maximum.
# B: the Mitscherlich equation y = A (1 - exp(-c (x + b))) for the response of grain yield to applied nitrogen,
#    A = 10 t/ha, c = 0.02 ha/kg, b = 20 kg/ha (nitrogen already available in the soil). Marked: the rate for 90 %
#    of A, x90 = ln(10)/c - b = 95 kg/ha, and the economic optimum where the marginal yield dy/dx equals the
#    price ratio r = 10 kg grain per kg N: x* = ln(A c / r)/c - b = 130 kg/ha.
# C: two nutrients. Liebig's law of the minimum, y = A min(fN, fP) (solid), against the multiplicative
#    Mitscherlich-Baule form y = A fN fP (dashed), with f = 1 - exp(-c x) for each nutrient; the curves show the
#    response to N at three phosphorus supplies.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(14.0, 4.3), gridspec_kw=dict(wspace=0.34))

# ---- A ----------------------------------------------------------------------------------------------
ax = axs[0]
c = np.linspace(0, 130, 800)
c0, k, ct, s = 2.0, 0.12, 95.0, 6.0
Y = np.where(c > c0, 100 * (1 - np.exp(-k * (c - c0))), 0) / (1 + np.exp((c - ct) / s))
i_max = np.argmax(Y)
crit = c[np.argmax(Y >= 0.9 * Y.max())]
ax.axvspan(0, crit, color=P.fill("negative"), alpha=0.35, lw=0)
tox0 = c[i_max:][np.argmax(Y[i_max:] < 0.9 * Y.max())]
ax.axvspan(crit, tox0, color=P.fill("positive"), alpha=0.35, lw=0)
ax.axvspan(tox0, 130, color=P.fill("highlight"), alpha=0.35, lw=0)
ax.plot(c, Y, color=charts.line("plant"), lw=2.2)
ax.axhline(90, color=P.muted(), lw=0.7, ls=":")
ax.plot([crit, crit], [0, 90], color=P.ink(), lw=0.9, ls="--")
ax.text(crit + 1.5, 8, "critical\nconcentration", fontsize=7, color=P.ink(), ha="left")
for x, t in ((crit / 2, "Deficiency\nzone"), ((crit + tox0) / 2, "Adequate\nzone"), ((tox0 + 130) / 2, "Toxic\nzone")):
    ax.text(x, 104, t, ha="center", va="bottom", fontsize=7.2, color=P.ink())
ax.set_xlim(0, 130)
ax.set_ylim(0, 122)
ax.set_xticks([])
ax.set_yticks([0, 50, 90, 100])
charts.style_axes(ax, "nutrient concentration in tissue (arbitrary units)", "growth or yield / % of maximum")
charts.title(ax, "A   Critical tissue concentration")

# ---- B ----------------------------------------------------------------------------------------------
ax = axs[1]
A, cc, b, r = 10.0, 0.02, 20.0, 0.010
x = np.linspace(0, 250, 500)
y = A * (1 - np.exp(-cc * (x + b)))
x90 = np.log(10) / cc - b
xs = np.log(A * cc / r) / cc - b
ax.plot(x, y, color=charts.line("plant"), lw=2.2)
ax.axhline(A, color=P.muted(), lw=0.7, ls=":")
ax.text(245, A + 0.15, "$A$", ha="right", va="bottom", fontsize=8, color=P.ink())
for xv, lab, tok in ((x90, "90 % of $A$", "dna"), (xs, "economic optimum", "negative")):
    yv = A * (1 - np.exp(-cc * (xv + b)))
    ax.plot([xv, xv], [0, yv], color=charts.line(tok), lw=1.0, ls="--")
    ax.plot([xv], [yv], "o", ms=4.5, color=charts.line(tok))
    if tok == "dna":
        ax.text(xv - 4, yv - 1.6, f"{lab}\n$x$ = {xv:.0f} kg ha$^{{-1}}$", fontsize=6.8, color=charts.line(tok), ha="right")
    else:
        ax.text(xv + 4, yv - 2.0, f"{lab}\n$x$ = {xv:.0f} kg ha$^{{-1}}$", fontsize=6.8, color=charts.line(tok))
# tangent with slope r at the optimum
yv = A * (1 - np.exp(-cc * (xs + b)))
tt = np.array([xs - 70, xs + 70])
ax.plot(tt, yv + r * (tt - xs), color=charts.line("negative"), lw=0.8, alpha=0.8)
ax.text(xs + 52, yv + r * 52 + 0.25, "slope = price ratio", fontsize=6.4, color=P.muted(), ha="center")
ax.set_xlim(0, 250)
ax.set_ylim(0, 11.5)
charts.style_axes(ax, "applied nitrogen $x$ / (kg ha$^{-1}$)", "grain yield $y$ / (t ha$^{-1}$)")
charts.title(ax, "B   Mitscherlich equation")

# ---- C ----------------------------------------------------------------------------------------------
ax = axs[2]
xN = np.linspace(0, 250, 500)
fN = 1 - np.exp(-0.02 * xN)
for xp, tok in ((15, "negative"), (40, "highlight"), (120, "dna")):
    fP = 1 - np.exp(-0.04 * xp)
    ax.plot(xN, A * np.minimum(fN, fP), color=charts.line(tok), lw=2.0, label=f"P = {xp} kg ha$^{{-1}}$")
    ax.plot(xN, A * fN * fP, color=charts.line(tok), lw=1.1, ls="--")
ax.plot([], [], color=P.muted(), lw=2.0, label="law of the minimum")
ax.plot([], [], color=P.muted(), lw=1.1, ls="--", label="multiplicative")
ax.legend(fontsize=6.6, frameon=False, loc="lower right")
ax.set_xlim(0, 250)
ax.set_ylim(0, 11.5)
charts.style_axes(ax, "applied nitrogen / (kg ha$^{-1}$)", "grain yield / (t ha$^{-1}$)")
charts.title(ax, "C   Two nutrients: Liebig vs multiplicative")
