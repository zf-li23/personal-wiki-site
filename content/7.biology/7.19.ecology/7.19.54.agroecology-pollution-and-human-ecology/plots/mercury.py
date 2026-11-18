"""Why methylmercury, not inorganic mercury, biomagnifies (Section 54.2.3).

Steady states of the food-chain model of Proposition 53.3.3 (7.19.53), BMF = alpha / (eps + k_e/I),
with gross growth efficiency eps = 0.1 at every step, applied separately to the two forms:
methylmercury (MeHg): assimilation alpha = 0.9, slow elimination k_e/I = 0.05 -> BMF = 6;
inorganic mercury (Hg(II)): alpha = 0.3, faster elimination k_e/I = 0.3 -> BMF = 0.75.
Level 1 (phytoplankton) holds 0.010 mg/kg total mercury (wet weight), of which 20% is MeHg.
Levels: 1 phytoplankton, 2 zooplankton, 3 planktivorous fish, 4 piscivorous fish, 5 top predator.
A: concentrations of both forms (log scale) with the guideline values for methylmercury in fish
(0.5 and 1.0 mg/kg: Chinese food standard for non-predatory and predatory fish).
B: methylmercury as a percentage of total mercury.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
lev = np.arange(1, 6)
names = ["phyto-\nplankton", "zoo-\nplankton", "plankti-\nvorous fish", "pisci-\nvorous fish", "top\npredator"]
bmf_me = 0.9 / (0.1 + 0.05)
bmf_in = 0.3 / (0.1 + 0.3)
me = 0.010 * 0.2 * bmf_me ** (lev - 1)
inorg = 0.010 * 0.8 * bmf_in ** (lev - 1)
cm, ci = C.line("negative"), C.line("dna")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axes[0]
ax.plot(lev, me, "o-", color=cm, lw=2, ms=6, label=f"methylmercury (BMF = {bmf_me:.0f})")
ax.plot(lev, inorg, "s-", color=ci, lw=2, ms=6, label=f"inorganic Hg(II) (BMF = {bmf_in:.2f})")
ax.plot(lev, me + inorg, color=P.ink(), lw=1, ls=(0, (3, 2)), label="total mercury")
for g, lab in ((0.5, "0.5 mg/kg"), (1.0, "1.0 mg/kg")):
    ax.axhline(g, color=P.muted(), lw=0.8, ls=":")
    ax.text(2.3, g * 1.12, lab, color=P.muted(), fontsize=FS["tiny"])
ax.set_yscale("log")
ax.set_xticks(lev, names)
ax.set_ylim(1e-5, 10)
C.style_axes(ax, None, "concentration (mg/kg wet weight)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "A  Two forms of mercury along a food chain")

ax = axes[1]
frac = 100 * me / (me + inorg)
ax.bar(lev, frac, 0.6, color=P.mix(cm, P.surface(), 0.4), edgecolor=cm)
for x, f in zip(lev, frac):
    ax.text(x, f + 1.5, f"{f:.0f}%", ha="center", fontsize=FS["tiny"], color=P.ink())
ax.set_xticks(lev, names)
ax.set_ylim(0, 110)
C.style_axes(ax, None, "methylmercury (% of total Hg)")
C.title(ax, "B  Methylmercury dominates at the top")
fig.tight_layout()
