# Economic injury level (EIL), economic threshold (ET) and general equilibrium position (GEP), schematic
# (after Stern and coauthors 1959): seasonal pest density with and without a control action applied when
# the economic threshold is reached.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(16, 9)
A = charts.axes_at(ax, (1.8, 1.4, 13.4, 7.0))
t = np.linspace(0, 120, 600)
untreated = 2 + 22 / (1 + np.exp(-(t - 45) / 6)) * np.exp(-((t - 60) / 40) ** 2) + 5 * np.exp(-((t - 100) / 8) ** 2)
EIL, ET, GEP = 15, 11, 5
treated = untreated.copy()
tc = t[np.argmax(untreated >= ET)]
after = t > tc
treated[after] = untreated[after] * (0.25 + 0.75 * np.exp(-(t[after] - tc) / 3))
A.plot(t, untreated, color=P.muted(), lw=1.2, ls="--", label="without control")
A.plot(t, treated, color=P.edge("negative"), lw=2, label="pest density")
for y, lab, tok in [(EIL, "EIL", "negative"), (ET, "ET", "enzyme"), (GEP, "GEP", "positive")]:
    A.axhline(y, color=P.edge(tok), lw=1, ls=":")
    A.text(119, y + 0.4, lab, ha="right", fontsize=8, color=P.edge(tok))
A.annotate("control applied", xy=(tc, ET), xytext=(tc - 28, ET + 7), fontsize=7, color=P.ink(),
           arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
A.set_xlabel("Days after planting")
A.set_ylabel("Pests per plant")
A.set_ylim(0, 26)
A.set_xlim(0, 120)
A.legend(fontsize=7, frameon=False, loc="upper right")
