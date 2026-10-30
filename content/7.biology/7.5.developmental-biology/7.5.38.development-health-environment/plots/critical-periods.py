"""Critical periods of human organ systems for teratogens, and a stage-sensitivity model (Formula 38.4.1).

A: weeks after fertilization; dark bars are the periods of highest sensitivity to major structural
malformations, light bars the periods of sensitivity to minor malformations and functional defects (schematic,
after the classical charts of human embryology; boundaries are approximate). Weeks 1-2: the all-or-none period.
B: the model P_k(t, D) = s_k(t) H(D) for three organs, with Gaussian sensitivity windows s_k(t) (peak value 1)
and a Hill dose term H(D) = D^h / (D^h + D50^h), h = 3, at three doses (D / D50 = 0.7, 1, 2); the probability
that at least one of the organs is malformed is 1 - prod_k (1 - P_k).
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

organs = [("central nervous system", 3, 16, 38), ("heart", 3, 6.5, 8), ("upper limbs", 4, 6, 8),
          ("lower limbs", 4.5, 6.5, 8), ("eyes", 4, 8, 38), ("ears", 4, 9, 16), ("palate", 6, 9, 16),
          ("teeth", 6, 8, 16), ("external genitalia", 7, 9, 16)]

fig, axs = plt.subplots(1, 2, figsize=(12.0, 4.0), gridspec_kw={"width_ratios": [1.25, 1.0]})
fig.subplots_adjust(left=0.13, right=0.98, bottom=0.15, top=0.87, wspace=0.28)

a = axs[0]
n = len(organs)
a.barh(n, 2, left=0, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6, height=0.6)
a.text(0.95, n, "all or none", fontsize=FT["tiny"], color=P.on_fill(), ha="left", va="center")
for i, (name, s, e, f) in enumerate(organs):
    y = n - 1 - i
    a.barh(y, f - e, left=e, color=P.light("drug"), edgecolor=P.edge("drug"), lw=0.5, height=0.6)
    a.barh(y, e - s, left=s, color=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.6, height=0.6)
a.set_yticks(range(n + 1))
a.set_yticklabels([o[0] for o in organs][::-1] + ["cleavage, implantation"])
a.set_xscale("log")
a.set_xticks([1, 2, 3, 4, 6, 8, 12, 16, 24, 38])
a.set_xticklabels(["1", "2", "3", "4", "6", "8", "12", "16", "24", "38"])
a.set_xlim(0.9, 40)
a.axvline(8, color=P.muted(), lw=0.8, ls=":")
a.text(8.3, n + 0.55, "embryonic | fetal period", fontsize=FT["tiny"], color=P.muted(), ha="center")
a.set_ylim(-0.6, n + 0.9)
charts.style_axes(a, "weeks after fertilization (log scale)")
charts.title(a, "A  Critical periods")

b = axs[1]
t = np.linspace(14, 76, 400)
windows = [("heart", 30, 5.0, "blood"), ("arms", 33, 3.5, "dna"), ("palate", 60, 5.0, "highlight")]
s = {nm: np.exp(-0.5 * ((t - mu) / sd) ** 2) for nm, mu, sd, _ in windows}
h = 3.0
for ratio, ls in ((0.7, (0, (1, 1.5))), (1.0, (0, (4, 2))), (2.0, "-")):
    H = ratio**h / (ratio**h + 1)
    for nm, mu, sd, tok in windows:
        b.plot(t, s[nm] * H, color=charts.line(tok), lw=1.4, ls=ls)
    anyp = 1 - np.prod([1 - s[nm] * H for nm, _, _, _ in windows], axis=0)
    if ratio == 2.0:
        b.plot(t, anyp, color=P.ink(), lw=0.9, alpha=0.6)
for nm, mu, sd, tok in windows:
    b.text(mu + (4 if nm == "arms" else -1 if nm == "heart" else 0), 0.98, nm, color=charts.line(tok), fontsize=FT["tiny"], ha="center")
b.text(41.5, 1.27, "solid: D = 2 D50\ndashed: D = D50\ndotted: D = 0.7 D50\ngrey: any of the three",
       fontsize=FT["tiny"], color=P.ink(), va="top")
b.set_ylim(0, 1.3)
charts.style_axes(b, "day of exposure after fertilization", "probability of malformation")
charts.title(b, "B  Model: stage window x dose")
