"""Model: phenological mismatch (schematic, after the pied flycatcher studies of Both and Visser 2001). The
caterpillar food peak (gray) advances with spring warming; a resident that times laying by local temperature
shifts its nestling period with the food peak, whereas a long-distance migrant whose arrival is fixed by a
circannual and photoperiodic program on the wintering grounds can advance laying only by shortening the interval
between arrival and laying (at most 8 days here). Breeding success = overlap of the nestling demand period with
the food supply. A: food peak and nestling periods in a cool and a warm spring (food 20 days earlier). B: success
against the advance of the food peak."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
d = np.linspace(100, 190, 901)


def gauss(c, w):
    return np.exp(-0.5 * ((d - c) / w) ** 2)


food0, need = 150.0, 152.0
fig, ax = bio.canvas(24, 10.4)
bio.panel(ax, "A", (0.3, 10.1))
p = quant.Plot(ax, (2.2, 1.8, 9.4, 7.4), xlim=(100, 190), ylim=(0, 1.35), xlabel="Day of year",
               ylabel="Food / demand (relative)", xticks=[(100, "10 Apr"), (130, "10 May"), (160, "9 Jun"), (190, "9 Jul")],
               yticks=None)
for shift, ls in [(0, False), (20, True)]:
    f = gauss(food0 - shift, 8)
    p.line(d, f, "neutral", lw=1.8, dashed=ls)
    res = gauss(need - shift, 6) * 0.8
    mig = gauss(need - min(shift, 8), 6) * 0.8
    p.line(d, res, "positive", lw=1.3, dashed=ls)
    p.line(d, mig, "rna", lw=1.3, dashed=ls)
p.legend([("food (caterpillars)", "neutral", "-"), ("resident nestlings", "positive", "-"),
          ("migrant nestlings", "rna", "-"), ("warm spring: dashed", "muted", "--")], at=p.xy(102, 1.3))
bio.panel(ax, "B", (13.0, 10.1))
q = quant.Plot(ax, (15.0, 1.8, 8.4, 7.4), xlim=(0, 25), ylim=(0, 1.1), xlabel="Advance of the food peak / days",
               ylabel="Breeding success (relative)", xticks=[0, 5, 10, 15, 20, 25], yticks=[0, 0.5, 1])
sh = np.linspace(0, 25, 100)
ov = lambda a, b: np.trapezoid(np.minimum(a, b), d)
base = ov(gauss(food0, 8), gauss(need, 6))
res = [ov(gauss(food0 - s, 8), gauss(need - s, 6)) / base for s in sh]
mig = [ov(gauss(food0 - s, 8), gauss(need - min(s, 8), 6)) / base for s in sh]
q.line(sh, res, "positive", lw=1.8, text="resident (tracks temperature)", at=0.45, dy=-0.12)
q.line(sh, mig, "rna", lw=1.8, text="long-distance migrant", at=0.45, dy=-0.35)
q.vline(8, text="limit of advance in laying", top=True)
ax.set_ylim(0.3, 10.4)
