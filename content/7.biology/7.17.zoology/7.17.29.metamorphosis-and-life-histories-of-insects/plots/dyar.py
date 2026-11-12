# Dyar's rule (Eq. 29.1, Example 29.1.1; illustrative head-capsule widths 0.32, 0.46, 0.95, 1.35 mm).
# A: ln(width) against instar: numbered 1-4 the points show a kink; numbered 1, 2, 4, 5 they fit one line
# (growth ratio g ~ 1.43) and the missing instar 3 is predicted at ~0.66 mm.
# B: geometric growth on a linear scale, compared with Przibram's rule (ratio 2^(1/3)).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 10.5)
w = np.array([0.32, 0.46, 0.95, 1.35])
right = np.array([1, 2, 4, 5])
lnw = np.log(w)
b, a = np.polyfit(right, lnw, 1)
g = np.exp(b)

pA = quant.Plot(ax, (2.2, 1.7, 8.2, 7.2), xlim=(0.5, 5.5), ylim=(-1.3, 0.5), xlabel="Instar",
                ylabel="ln(head width / mm)", xticks=[1, 2, 3, 4, 5], yticks=[-1.2, -0.8, -0.4, 0, 0.4],
                ylabel_offset=1.1)
pA.line([1, 2, 3, 4], lnw, "negative", dashed=True, lw=1.2)
pA.points([1, 2, 3, 4], lnw, "negative", r=0.13, hollow=True)
xx = np.linspace(0.8, 5.2, 50)
pA.line(xx, a + b * xx, "enzyme", lw=1.4)
pA.points(right, lnw, "enzyme", r=0.12)
pred = a + b * 3
cx, cy = pA.xy(3, pred)
bio.label(ax, (cx, cy), "*", size="title", bold=True, color=P.edge("highlight"))
pA.text(3.1, pred - 0.17, "missing instar: %.2f mm" % np.exp(pred), ha="left", size="tiny")
pA.text(0.7, 0.42, "numbered 1-4: kink", token="negative", ha="left")
pA.text(0.7, 0.26, "numbered 1, 2, 4, 5: g = %.2f" % g, token="enzyme", ha="left")
bio.label(ax, (6.3, 9.7), "A  Dyar plot", size="small", bold=True)

pB = quant.Plot(ax, (14.0, 1.7, 8.6, 7.2), xlim=(0.5, 5.5), ylim=(0, 1.6), xlabel="Instar",
                ylabel="Head width / mm", xticks=[1, 2, 3, 4, 5], yticks=[0, 0.4, 0.8, 1.2, 1.6])
i = np.arange(1, 6)
pB.line(i, np.exp(a) * g ** i, "enzyme", lw=1.4, text="Dyar, g = %.2f" % g, at=0.75, dx=-2.6, dy=0.25)
pB.points(right, w, "enzyme", r=0.11)
pB.line(i, 0.32 * 2 ** ((i - 1) / 3), "neutral", dashed=True, lw=1.3, text="Przibram, g = 1.26", at=0.9, dx=-1.2, dy=-0.55)
bio.label(ax, (18.3, 9.7), "B  Geometric growth", size="small", bold=True)
