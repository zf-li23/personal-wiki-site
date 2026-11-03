"""Sequential reproductive barriers between the monkeyflowers Mimulus lewisii (bee-pollinated) and
M. cardinalis (hummingbird-pollinated). Strengths of individual barriers as given by Futuyma and
Kirkpatrick (2017) after field studies of Schemske, Bradshaw and colleagues: elevational separation reduces
gene exchange by 59 %, pollinator fidelity by 98 % among plants at the same elevation, conspecific pollen
precedence by 70 % and reduced germination of F1 seed by 20 %. A: strength RI_i of each barrier on its own.
B: its absolute contribution AC_i = RI_i (1 - sum of the contributions of earlier barriers), stacked in the
order in which the barriers act; the total isolation is 1 - prod(1 - RI_i) = 0.998, and barriers acting
late (after the first two) contribute almost nothing because little gene exchange is left for them to
prevent."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
names = ["elevation", "pollinator\nfidelity", "pollen\nprecedence", "hybrid\ngermination"]
ri = np.array([0.59, 0.98, 0.70, 0.20])
ac = []
rem = 1.0
for r in ri:
    ac.append(r * rem)
    rem *= 1 - r
ac = np.array(ac)
toks = ["plant", "petal", "anther", "ovary"]

fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.9), gridspec_kw={"width_ratios": [1.2, 1]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.2, top=0.9, wspace=0.3)
a = axs[0]
xs = np.arange(len(ri))
a.bar(xs, ri, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.8)
for x, r in zip(xs, ri):
    a.text(x, r + 0.02, f"{r:.2f}", ha="center", fontsize=FT["tiny"], color=P.ink())
a.set_xticks(xs)
a.set_xticklabels(names, fontsize=FT["tiny"])
a.set_ylim(0, 1.1)
charts.style_axes(a, None, "strength of barrier $RI_i$")
charts.title(a, "A  Individual barriers")

b = axs[1]
bottom = 0.0
for k, (v, t) in enumerate(zip(ac, toks)):
    b.bar([0], [v], bottom=bottom, width=0.5, color=P.fill(t), edgecolor=P.edge(t), lw=0.8)
    lab = names[k].replace("\n", " ")
    ty = bottom + v / 2 if v > 0.03 else 0.90 - 0.07 * (k - 2)
    if v <= 0.03:
        b.plot([0.25, 0.31], [bottom + v / 2, ty], color=P.muted(), lw=0.6)
    b.text(0.32, ty, f"{lab}: {v:.4f}", va="center", fontsize=FT["tiny"], color=P.ink())
    bottom += v
b.set_xlim(-0.4, 1.5)
b.set_xticks([])
b.set_ylim(0, 1.05)
b.text(0, 1.01, f"total {bottom:.4f}", ha="center", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(b, None, "cumulative isolation")
charts.title(b, "B  Contributions in sequence")
