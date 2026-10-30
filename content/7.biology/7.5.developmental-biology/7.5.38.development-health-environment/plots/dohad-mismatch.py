"""The mismatch idea of the developmental origins of health and disease (Formula 38.6.1, illustrative).

Each individual has a metabolic set point s fixed in fetal life by the nutrition it received (scale 0-1, poor
to rich); in adult life it lives in an environment of nutritional level e. Disease risk is modeled as
r(s, e) = r0 exp(alpha (e - s)^2) + beta e^2 with r0 = 0.05, alpha = 4 and beta = 0.04 (the second term:
a general cost of rich diets). A: risk against adult environment for set points s = 0.2 (fetal undernutrition),
0.5 and 0.8: each curve is lowest near its own set point, so a fetus that "predicted" scarcity is at highest
risk in an affluent environment. B: risk against the set point (a proxy of birth weight) in a uniformly
affluent adult environment (e = 0.9): low set points carry the highest risk.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
r0, alpha, beta = 0.05, 4.0, 0.04


def risk(s, e):
    return r0 * np.exp(alpha * (e - s) ** 2) + beta * e**2


fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
e = np.linspace(0, 1, 300)
a = axs[0]
for sv, tok, lab in ((0.2, "negative", "s = 0.2 (fetal undernutrition)"), (0.5, "dna", "s = 0.5"),
                     (0.8, "positive", "s = 0.8 (rich fetal supply)")):
    a.plot(e, risk(sv, e), color=charts.line(tok), lw=1.8, label=lab)
    a.plot(sv, risk(sv, sv), "o", color=charts.line(tok), ms=4)
a.axvspan(0.8, 1.0, color=P.light("highlight"), lw=0)
a.text(0.9, 0.72, "affluent\nadult life", fontsize=FT["tiny"], color=P.ink(), ha="center", va="top")
a.set_ylim(0, 0.75)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(a, "adult nutritional environment e", "disease risk (model)")
charts.title(a, "A  Risk is lowest where adult life matches the set point")

b = axs[1]
s = np.linspace(0, 1, 300)
b.plot(s, risk(s, 0.9), color=charts.line("drug"), lw=1.8)
b.set_ylim(0, 0.75)
charts.style_axes(b, "fetal set point s (proxy: birth weight)", "disease risk at e = 0.9")
charts.title(b, "B  In an affluent world, small babies carry the risk")
