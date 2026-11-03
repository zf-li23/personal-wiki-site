"""Radiometric dating (Formula 29.1.1): A parent and daughter fractions against half-lives; B age against
D/N for 14C (5730 yr), 40K->40Ar (1.25 Gyr, branching fraction 0.107) and 238U->206Pb (4.47 Gyr)."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(24, 9)
bio.panel(ax, "A", (0.2, 8.8)); bio.panel(ax, "B", (12.2, 8.8))
pa = charts.axes_at(ax, (2.0, 1.6, 9.0, 6.6)); pb = charts.axes_at(ax, (14.4, 1.6, 9.0, 6.6))
h = np.linspace(0, 5, 300)
pa.plot(h, 0.5 ** h, color=charts.line("dna"), lw=1.8, label="parent N/N₀")
pa.plot(h, 1 - 0.5 ** h, color=charts.line("rna"), lw=1.8, label="daughter D/N₀")
for k in range(1, 5):
    pa.plot([k], [0.5 ** k], "o", color=charts.line("dna"), ms=4)
    pa.text(k + 0.05, 0.5 ** k + 0.04, f"D/N = {2 ** k - 1}", fontsize=FT["tiny"], color=P.ink())
pa.set_xlim(0, 5); pa.set_ylim(0, 1.02)
charts.style_axes(pa, "time (half-lives)", "fraction of original parent atoms")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
r = np.logspace(-4, 1.5, 300)
for name, thalf, frac, tok in (("¹⁴C (5730 yr)", 5730, 1.0, "positive"), ("⁴⁰K→⁴⁰Ar (1.25 Gyr)", 1.25e9, 0.107, "rna"),
                               ("²³⁸U→²⁰⁶Pb (4.47 Gyr)", 4.47e9, 1.0, "dna")):
    lam = np.log(2) / thalf
    t = np.log(1 + r / frac) / lam
    pb.plot(r, t, color=charts.line(tok), lw=1.8, label=name)
pb.set_xscale("log"); pb.set_yscale("log"); pb.set_ylim(1, 3e10)
charts.style_axes(pb, "measured daughter/parent ratio D/N (¹⁴C: decayed/remaining)", "age (years)")
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
