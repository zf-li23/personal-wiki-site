"""Phenological mismatch under warming (illustrative model).

The date of the food peak (caterpillars) advances by 0.5 days per year over 40 years; birds advance their
laying date by only 0.15 days per year, starting matched. Breeding success declines with the mismatch
d between the date of peak food demand of the nestlings and the food peak: success = exp(-d^2 / (2 w^2))
with tolerance w = 8 days, and the population multiplies by lambda = 0.55 + 0.6 x success per year.
A: the two dates against year. B: mismatch and lambda against year; the population declines once the
mismatch exceeds about 6 days. C: population size (log scale) for birds advancing at 0.15 and 0.4 days
per year.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
yr = np.arange(0, 41)
food = 150 - 0.5 * yr


def run(rate):
    bird = 150 - rate * yr
    d = bird - food
    succ = np.exp(-d**2 / (2 * 8.0**2))
    lam = 0.55 + 0.6 * succ
    N = np.concatenate([[100.0], 100.0 * np.cumprod(lam[:-1])])
    return bird, d, lam, N


bird, d, lam, N = run(0.15)
pa = C.axes_at(ax, (2.0, 1.6, 7.0, 6.8))
pa.plot(yr, food, color=Q.line_color("plant"), lw=1.6, label="food peak")
pa.plot(yr, bird, color=Q.line_color("dna"), lw=1.6, label="nestling demand peak")
pa.fill_between(yr, food, bird, color=P.fill("negative"), alpha=0.3, lw=0)
pa.set_xlim(0, 40)
C.style_axes(pa, "year", "date (day of year)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Dates advance at different rates", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
pb.plot(yr, d, color=Q.line_color("negative"), lw=1.6, label="mismatch (days)")
pb.set_xlim(0, 40)
pb.set_ylim(0, 16)
C.style_axes(pb, "year", "mismatch (days)")
pb2 = pb.twinx()
pb2.plot(yr, lam, color=Q.line_color("protein"), lw=1.6)
pb2.axhline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb2.set_ylim(0.5, 1.2)
C.style_axes(pb2, None, "growth factor lambda", box=True)
pb2.spines["left"].set_visible(False)
pb.text(14, 2.6, "mismatch", fontsize=FS["tiny"], color=Q.line_color("negative"))
pb.text(6, 15.3, "lambda", fontsize=FS["tiny"], color=Q.line_color("protein"))
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Growing mismatch", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
for rate, tok in [(0.15, "negative"), (0.4, "dna")]:
    _, _, _, N = run(rate)
    pc.semilogy(yr, N, color=Q.line_color(tok), lw=1.6, label=f"birds advance {rate} d per year")
pc.set_xlim(0, 40)
C.style_axes(pc, "year", "population size")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Consequences for the population", size="small", bold=True, ha="left")
