# Progress of a (hypothetical) five-step purification of an enzyme, from the purification table in the text:
# specific activity (units per mg protein, log scale) rises 1200-fold while the yield of activity falls to 40 %.
import numpy as np
import wikibio as bio
from wikibio import charts as C

steps = ["crude\nextract", "(NH$_4$)$_2$SO$_4$\n40–60 %", "anion\nexchange", "gel\nfiltration", "affinity"]
protein = np.array([12000, 3600, 480, 120, 4.0])      # mg
activity = np.array([240000, 216000, 168000, 132000, 96000])  # units (umol/min)
sa = activity / protein
yld = 100 * activity / activity[0]

fig, ax = bio.canvas(18, 8.2)
F = bio.core.FONT["tiny"]
a = C.axes_at(ax, (1.9, 1.9, 6.8, 5.6))
x = np.arange(len(steps))
a.bar(x, sa, width=0.62, color=bio.P.fill("enzyme"), edgecolor=bio.P.edge("enzyme"), lw=0.9)
for xi, v in zip(x, sa):
    a.text(xi, v * 1.25, f"{v:,.0f}", ha="center", fontsize=F, color=bio.P.ink())
a.set_yscale("log")
a.set_ylim(5, 1e5)
a.set_xticks(x, steps, fontsize=F)
C.style_axes(a, None, "specific activity / (U mg$^{-1}$)")
bio.panel(ax, "A", (0.1, 7.9))

b = C.axes_at(ax, (11.0, 1.9, 6.6, 5.6))
fold = sa / sa[0]
b.plot(x, yld, "o-", color=C.line("negative"), lw=2.0, ms=5)
b.set_ylim(0, 110)
b.set_xticks(x, steps, fontsize=F)
C.style_axes(b, None, "yield of activity / %")
b2 = b.twinx()
b2.plot(x, fold, "s--", color=C.line("positive"), lw=1.6, ms=5)
b2.set_yscale("log")
b2.set_ylim(0.5, 5000)
C.style_axes(b2, None, "purification / fold", box=True)
b2.spines["right"].set_visible(True)
b.text(0.15, 103, "yield", color=C.line("negative"), fontsize=F)
b.text(3.0, 70, "purification", color=C.line("positive"), fontsize=F)
bio.panel(ax, "B", (9.6, 7.9))
