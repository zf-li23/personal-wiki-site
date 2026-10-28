"""Risk of Down syndrome at birth as a function of maternal age, from the logistic model of Morris, Mutton
and Alberman (2002) fitted to births in England and Wales: risk = 1/(1 + exp(7.330 - 4.211/(1 + exp(-0.282(age - 37.23))))).
B: the same risk on a log scale with the expected fraction of trisomy 21 conceptions that survive to term
(about 20 %) used to convert it to an approximate risk at conception."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
age = np.linspace(15, 50, 351)
risk = 1 / (1 + np.exp(7.330 - 4.211 / (1 + np.exp(-0.282 * (age - 37.23)))))
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
ax = axs[0]
ax.plot(age, 100 * risk, color=charts.line("dna"), lw=1.6)
for a in (20, 30, 35, 40, 45):
    r = 1 / (1 + np.exp(7.330 - 4.211 / (1 + np.exp(-0.282 * (a - 37.23)))))
    ax.plot(a, 100 * r, "o", color=charts.line("dna"), ms=4)
    ax.annotate(f"1 in {round(1 / r):,}".replace(",", " "), (a, 100 * r), xytext=(-6, 8), textcoords="offset points",
                ha="right", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xlim(15, 50)
charts.style_axes(ax, "maternal age / years", "risk at birth / %")
charts.title(ax, "A  Trisomy 21 at birth")
ax = axs[1]
ax.semilogy(age, risk, color=charts.line("dna"), lw=1.6, label="at birth")
ax.semilogy(age, np.minimum(risk / 0.2, 1), color=charts.line("receptor"), lw=1.4, ls="--",
            label="at conception (approx., 20 % survive)")
ax.set_xlim(15, 50)
ax.set_ylim(3e-4, 0.6)
charts.style_axes(ax, "maternal age / years", "risk")
charts.title(ax, "B  Log scale")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
