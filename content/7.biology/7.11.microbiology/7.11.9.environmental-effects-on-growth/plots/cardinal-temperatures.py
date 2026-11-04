# Temperature and growth.
# A: growth rate against temperature for the four temperature classes, drawn with the cardinal temperature
#    model with inflection (Rosso et al. 1993), which needs only Tmin, Topt, Tmax and the rate at Topt:
#    psychrophile -5 / 10 / 18 C (illustrative), mesophile Escherichia coli 8 / 39 / 48 C, thermophile
#    40 / 63 / 75 C (illustrative), hyperthermophile Pyrolobus fumarii 90 / 106 / 113 C. Rates are scaled to
#    1 at the optimum. Each curve rises slowly and falls steeply above the optimum.
# B: why the curve is asymmetric (a toy model). The rate of the enzymatic reactions rises with temperature
#    (Arrhenius, activation energy 60 kJ/mol), while the fraction of an essential protein that is folded falls
#    sharply near its melting temperature (two-state unfolding, unfolding enthalpy 600 kJ/mol, Tm = 49 C).
#    Their product, the growth rate, has its optimum a few degrees below the maximum.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P


def ctmi(T, tmin, topt, tmax):
    T = np.asarray(T, float)
    num = (T - tmax) * (T - tmin) ** 2
    den = (topt - tmin) * ((topt - tmin) * (T - topt) - (topt - tmax) * (topt + tmin - 2 * T))
    r = num / den
    return np.where((T > tmin) & (T < tmax), r, np.nan)


fig, axs = plt.subplots(1, 2, figsize=(13.0, 4.2), gridspec_kw=dict(width_ratios=[1.9, 1.0], wspace=0.25))
ax = axs[0]
classes = [("psychrophile", -5, 10, 18, "dna", None),
           ("mesophile", 8, 39, 48, "positive", "Escherichia coli"),
           ("thermophile", 40, 63, 75, "highlight", None),
           ("hyperthermophile", 90, 106, 113, "negative", "Pyrolobus fumarii")]
for name, a, o, b, tok, sp in classes:
    T = np.linspace(a, b, 400)
    ax.plot(T, ctmi(T, a, o, b), color=charts.line(tok), lw=2.2)
    ax.text(o, 1.06, name, ha="center", fontsize=8, color=charts.line(tok), weight="bold")
    if sp:
        x, y, ha = (21, 0.8, "center") if sp.startswith("Esch") else (114, 0.35, "left")
        ax.text(x, y, sp, ha=ha, fontsize=7, color=P.ink(), style="italic")
    for t, lab in ((a, "min"), (o, "opt"), (b, "max")):
        ax.plot([t], [0 if lab != "opt" else 1], "o", ms=3.2, color=charts.line(tok))
# E. coli cardinal temperatures annotated
ax.annotate("", xy=(8, -0.08), xytext=(48, -0.08), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
ax.text(28, -0.16, "growth range of $E.\\ coli$: about 40 degrees", ha="center", fontsize=6.8, color=P.muted())
ax.set_xlim(-10, 128)
ax.set_ylim(-0.22, 1.18)
ax.set_yticks([0, 0.5, 1])
charts.style_axes(ax, "temperature / $^\\circ$C", "growth rate (relative to optimum)")
charts.title(ax, "A   Cardinal temperatures of the four classes")

ax = axs[1]
Tc = np.linspace(10, 55, 500)
TK = Tc + 273.15
R = 8.314
arr = np.exp(-60e3 / R * (1 / TK - 1 / 310.15))
Tm = 49 + 273.15
dG = 600e3 * (1 - TK / Tm)
fold = 1 / (1 + np.exp(-dG / (R * TK)))
rate = arr * fold
ax.plot(Tc, arr / arr.max() * 1.0, color=charts.line("enzyme"), lw=1.6, ls="--", label="reaction rates (Arrhenius)")
ax.plot(Tc, fold, color=charts.line("protein"), lw=1.6, ls=":", label="fraction of protein folded")
ax.plot(Tc, rate / rate.max(), color=P.ink(), lw=2.2, label="product: growth rate")
ax.axvline(Tc[np.argmax(rate)], color=P.muted(), lw=0.7)
ax.set_ylim(0, 1.12)
ax.legend(fontsize=6.8, frameon=False, loc="upper left")
charts.style_axes(ax, "temperature / $^\\circ$C", "relative value")
charts.title(ax, "B   Why the optimum lies near the maximum")
