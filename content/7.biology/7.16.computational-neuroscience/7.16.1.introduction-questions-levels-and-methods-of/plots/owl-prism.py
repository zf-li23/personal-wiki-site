"""Prism adaptation of the auditory space map of the barn owl, as an illustrative model.
A: ITD tuning of a neuron in the external nucleus of the inferior colliculus (ICX) that
represents a fixed visual location, before prisms and after weeks of prism rearing (the visual
field is displaced by 23 degrees, about 50 us of ITD at 2.2 us per degree). B: the shift s(t) of
the best ITD follows ds/dt = eta (D - s), with the instructive target D = 50 us while prisms are
worn and 0 after removal; eta is large in juveniles, small in naive adults, and intermediate in
adults that had adapted as juveniles (a stored alternative map)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.3))
fig.subplots_adjust(wspace=0.32, left=0.08, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
itd = np.linspace(-150, 150, 400)
for c, tok, lab in [(0, "neutral", "normal owl"), (50, "highlight", "after prism rearing")]:
    ax.plot(itd, np.exp(-0.5 * ((itd - c) / 28) ** 2), color=charts.line(tok), lw=1.8, label=lab)
ax.annotate("", xy=(50, 1.05), xytext=(0, 1.05), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1))
ax.text(25, 1.09, "~50 µs", ha="center", va="bottom", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_ylim(0, 1.22)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "interaural time difference / µs", "normalized response")
charts.title(ax, "A  ITD tuning of one ICX site")

ax = axs[1]
days = np.arange(0, 301)
D = np.where(days < 150, 50.0, 0.0)
for eta, s0, tok, lab in [(1 / 25, 0, "positive", "juvenile (prisms at 60 d of age)"),
                          (1 / 600, 0, "negative", "naive adult"),
                          (1 / 40, 0, "highlight", "adult with juvenile experience")]:
    s = np.zeros_like(days, float)
    s[0] = s0
    for k in range(1, len(days)):
        s[k] = s[k - 1] + eta * (D[k - 1] - s[k - 1])
    ax.plot(days, s, color=charts.line(tok), lw=1.8, label=lab)
ax.axvspan(0, 150, color=P.mix(P.muted(), P.surface(), 0.85), lw=0)
ax.text(75, 54, "prisms on", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.text(225, 54, "prisms removed", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.set_ylim(-3, 92)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "days after prism mounting", "shift of best ITD / µs")
charts.title(ax, "B  Shift of the auditory map")
