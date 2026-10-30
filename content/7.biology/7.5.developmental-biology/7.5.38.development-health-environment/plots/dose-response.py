"""Dose-response of a teratogen in a simulated embryo assay, fitted with four-parameter logistic curves (Formula 38.4.2).

Nine doses (0.5-200 in arbitrary units, e.g. mg/L in a zebrafish or Xenopus embryo test), 40 embryos per dose,
exposure during the sensitive window. True model: probability of malformation 4PL with bottom 0.03,
top 0.95, EC50 = 8, Hill slope 2.5; probability of death 4PL with bottom 0.02, top 1, LC50 = 60, slope 3.
Counts are drawn from binomial distributions (seed 0) and each proportion is fitted by least squares with
wikibio.stats.fit_4pl; shaded: 95 % confidence bands of the fitted curves. The teratogenic index
TI = LC50 / EC50 of the fits is printed; TI > 1.5 is the usual criterion for a teratogen in such assays.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, stats

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

dose = np.array([0.5, 1, 2, 4, 8, 16, 32, 64, 128, 200], float)
n = 40
p_mal = stats.four_pl(dose, 0.03, 0.95, np.log10(8.0), 2.5)
p_dead = stats.four_pl(dose, 0.02, 1.0, np.log10(60.0), 3.0)
y_mal = rng.binomial(n, p_mal) / n
y_dead = rng.binomial(n, p_dead) / n
f_mal = stats.fit_4pl(dose, y_mal, p0=[0.0, 1.0, 1.0, 2.0])
f_dead = stats.fit_4pl(dose, y_dead, p0=[0.0, 1.0, 1.8, 2.0])
ec50 = f_mal.ci["EC50"]
lc50 = f_dead.ci["EC50"]

fig, ax = plt.subplots(figsize=(7.2, 4.0))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.15, top=0.9)
xx = np.logspace(np.log10(0.4), np.log10(250), 300)
for f, tok, lab in ((f_mal, "dna", "malformed"), (f_dead, "negative", "dead")):
    lo, hi = f.band(xx)
    ax.fill_between(xx, np.clip(lo, -0.05, 1.1), np.clip(hi, -0.05, 1.1), color=P.light(tok), lw=0)
    ax.plot(xx, f.predict(xx), color=charts.line(tok), lw=1.8, label=lab)
    ax.plot(f.x, f.y, "o", mfc="none", mec=charts.line(tok), ms=4.5, mew=1.1)
for (e, lo, hi), tok, nm in ((ec50, "dna", "EC50"), (lc50, "negative", "LC50")):
    ax.axvline(e, color=charts.line(tok), lw=0.8, ls=(0, (3, 2)))
    ax.text(e * 1.08, 0.08 if nm == "EC50" else 0.2, f"{nm} = {e:.1f}\n(95 % CI {lo:.1f}-{hi:.1f})",
            fontsize=FT["tiny"], color=P.ink())
ax.text(0.45, 0.82, f"teratogenic index\nTI = LC50 / EC50 = {lc50[0] / ec50[0]:.1f}", fontsize=FT["small"],
        color=P.ink())
ax.set_xscale("log")
ax.set_xlim(0.4, 250)
ax.set_ylim(-0.04, 1.08)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(ax, "dose (log scale)", "fraction of embryos")
charts.title(ax, "Malformation and lethality curves of a teratogen")
