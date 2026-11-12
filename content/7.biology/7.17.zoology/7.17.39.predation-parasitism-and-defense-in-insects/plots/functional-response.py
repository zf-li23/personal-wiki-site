# Holling's functional responses (Eq. 39.1): type I f = aN; type II f = aN / (1 + a h N) with a = 0.5,
# h = 0.05 (saturating at 1/h = 20 prey per day); type III f = b N^2 / (1 + b h N^2) with b chosen so that
# the half-saturation densities are comparable. Lower panel: proportion eaten f / N.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(16, 14)
N = np.linspace(0.01, 200, 600)
a, h, b = 0.5, 0.05, 0.02
f1 = np.minimum(a * N, 40)
f2 = a * N / (1 + a * h * N)
f3 = b * N ** 2 / (1 + b * h * N ** 2)
curves = [(f1, "Type I", "neutral", ":"), (f2, "Type II (disc equation)", "positive", "-"), (f3, "Type III", "negative", "--")]
top = charts.axes_at(ax, (2.0, 7.6, 13.2, 5.6))
for f, lab, tok, ls in curves:
    top.plot(N, f, color=P.edge(tok), lw=1.8, ls=ls, label=lab)
top.axhline(1 / h, color=P.muted(), lw=0.8, ls="-.")
top.text(198, 1 / h + 0.6, "1/h = 20 prey per day", ha="right", fontsize=7, color=P.muted())
top.set_ylim(0, 26)
top.set_xlim(0, 200)
top.set_ylabel("Prey eaten per predator per day")
top.legend(fontsize=7, frameon=False, loc="lower right")
bot = charts.axes_at(ax, (2.0, 1.3, 13.2, 5.0))
for f, lab, tok, ls in curves[1:]:
    bot.plot(N, f / N, color=P.edge(tok), lw=1.8, ls=ls)
bot.set_xlim(0, 200)
bot.set_ylim(0, 0.6)
bot.set_xlabel("Prey density, N")
bot.set_ylabel("Proportion eaten per day")
