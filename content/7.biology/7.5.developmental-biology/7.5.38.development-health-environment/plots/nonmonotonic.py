"""Monotonic and non-monotonic dose-response curves (Formula 38.5.1).

Grey: a monotonic Hill curve (EC50 = 1, n = 1). Coloured: a receptor-mediated effect E(x) = x / (x + EC50)
multiplied by a high-dose loss of response 1 / (1 + (x / IC50)^m) (receptor down-regulation, negative
feedback or toxicity), with EC50 = 0.01 and IC50 = 1, m = 1.5, which gives an inverted U. Doses are relative
(log scale). Dots: a classical design that tests three high doses (10, 30, 100) and a control; a straight line
through the high-dose points extrapolated downwards (dashed) predicts no effect at low doses, where the
non-monotonic curve has its maximum.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

x = np.logspace(-5, 3, 400)
mono = x / (x + 1.0)
nmdr = x / (x + 0.01) / (1 + (x / 1.0) ** 1.5)

fig, ax = plt.subplots(figsize=(7.0, 3.8))
fig.subplots_adjust(left=0.11, right=0.97, bottom=0.15, top=0.9)
ax.semilogx(x, mono, color=P.muted(), lw=1.6, label="monotonic (Hill)")
ax.semilogx(x, nmdr, color=charts.line("drug"), lw=1.9, label="non-monotonic (inverted U)")
hd = np.array([10.0, 30.0, 100.0])
yd = hd / (hd + 0.01) / (1 + hd**1.5)
ax.plot(hd, yd, "o", color=charts.line("negative"), ms=5)
ax.plot([1e-5], [0], "s", color=charts.line("negative"), ms=5)
ax.text(1.3e-5, 0.05, "control", fontsize=FT["tiny"], color=P.ink())
ax.text(12, 0.12, "high-dose tests", fontsize=FT["tiny"], color=P.ink())
# linear extrapolation in log dose through the high-dose points
sl, ic = np.polyfit(np.log10(hd), yd, 1)
xe = np.logspace(-1, 2, 50)
ax.semilogx(xe, np.clip(sl * np.log10(xe) + ic, 0, None), color=charts.line("negative"), lw=1.0, ls=(0, (4, 2)))
ax.annotate("maximum effect at low dose", xy=(x[np.argmax(nmdr)], nmdr.max()), xytext=(4e-5, 0.9), fontsize=FT["tiny"],
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.set_xlim(1e-5, 1e3)
ax.set_ylim(-0.03, 1.05)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "relative dose (log scale)", "response (fraction of maximum)")
charts.title(ax, "A low-dose effect missed by high-dose testing")
