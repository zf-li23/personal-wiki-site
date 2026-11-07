"""Static pressure-volume curves of an excised lung inflated with air and with saline (after von Neergaard 1929),
and the surface tension-area loop of a surfactant film (Wilhelmy balance, after Clements 1957). Schematic curves.

A: volume (% of total lung capacity) against transpulmonary pressure. Saline removes the air-liquid interface,
so only tissue elasticity remains: V = 100 / (1 + exp(-(P - 2)/2)). Air: inflation needs an opening pressure
(recruitment of collapsed units), V = 100 / (1 + exp(-(P - 12)/2.8)); deflation, V = 100 / (1 + exp(-(P - 5)/3)),
stays at a higher volume (hysteresis). The area between the limbs is energy lost in each cycle.
B: surface tension against relative film area for water (70 mN/m, constant), a detergent (about 25 mN/m, constant)
and lung surfactant: on compression the film is enriched in DPPC and gamma falls to about 1 mN/m.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(12, 4.3))
ax = axs[0]
p = np.linspace(0, 30, 300)
sal = 100 / (1 + np.exp(-(p - 2) / 2))
inf = 100 / (1 + np.exp(-(p - 12) / 2.8))
dfl = 100 / (1 + np.exp(-(p - 5) / 3))
ax.plot(p, sal, color=P.edge("dna"), lw=2, label="saline (tissue only)")
ax.plot(p, inf, color=P.edge("blood"), lw=2, label="air, inflation")
ax.plot(p, dfl, color=P.edge("blood"), lw=2, ls="--", label="air, deflation")
ax.fill_between(p, inf, dfl, color=P.fill("blood"), alpha=0.15, lw=0)
ax.annotate("", xy=(20, 93), xytext=(14, 66), arrowprops=dict(arrowstyle="->", color=P.edge("blood")))
ax.annotate("", xy=(6, 60), xytext=(10, 85), arrowprops=dict(arrowstyle="->", color=P.edge("blood")))
ax.text(16, 30, "extra pressure\n= surface tension", fontsize=8, color=P.muted())
ax.set_xlabel("Transpulmonary pressure / cmH$_2$O")
ax.set_ylabel("Lung volume / % of TLC")
ax.set_xlim(0, 30)
ax.set_ylim(0, 105)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  Air versus saline filling", loc="left", fontsize=10)
sec = ax.secondary_xaxis("top", functions=(lambda c: c * 0.0981, lambda k: k / 0.0981))
sec.set_xlabel("kPa")

ax = axs[1]
a = np.linspace(0.2, 1.0, 200)
comp = 1 + 44 * ((a - 0.2) / 0.8) ** 3
expd = 1 + 44 * ((a - 0.2) / 0.8) ** 1.3
ax.plot(a * 100, np.full_like(a, 70), color=P.edge("dna"), lw=2, label="water")
ax.plot(a * 100, np.full_like(a, 25), color=P.muted(), lw=2, ls="--", label="detergent")
ax.plot(a * 100, comp, color=P.edge("blood"), lw=2, label="lung surfactant, compression")
ax.plot(a * 100, expd, color=P.edge("blood"), lw=2, ls="--", label="lung surfactant, expansion")
ax.annotate("", xy=(35, 2.5), xytext=(70, 12), arrowprops=dict(arrowstyle="->", color=P.edge("blood")))
ax.annotate("", xy=(70, 33), xytext=(40, 20), arrowprops=dict(arrowstyle="->", color=P.edge("blood")))
ax.set_xlabel("Film area / % of maximum")
ax.set_ylabel("Surface tension $\\gamma$ / (mN m$^{-1}$)")
ax.set_ylim(0, 80)
ax.legend(frameon=False, fontsize=8, loc="center left", bbox_to_anchor=(0.0, 0.62))
ax.set_title("B  Surface tension of the film", loc="left", fontsize=10)
for x in axs:
    x.grid(True, alpha=0.3)
fig.tight_layout()
