"""Germ-soma specialization (Formula 28.5.1): A trade-off curves v = (1-e)^alpha; B generalist vs specialist
group fitness against alpha; C volvocine series, cell number vs fraction of somatic cells (Barton et al. 2007)."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(30, 9)
for k, x in enumerate((0.2, 10.2, 20.2)):
    bio.panel(ax, "ABC"[k], (x, 8.8))
pa = charts.axes_at(ax, (2.0, 1.6, 7.0, 6.6)); pb = charts.axes_at(ax, (12.0, 1.6, 7.0, 6.6))
pc = charts.axes_at(ax, (22.0, 1.6, 7.0, 6.6))
e = np.linspace(0, 1, 200)
for a, tok in ((0.5, "dna"), (1.0, "neutral"), (2.0, "rna")):
    pa.plot(e, (1 - e) ** a, color=charts.line(tok), lw=1.8, label=f"α = {a:g}")
charts.style_axes(pa, "investment in reproduction e (fecundity)", "viability contribution v")
pa.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
al = np.linspace(0.2, 4, 200)
wg = al ** al / (1 + al) ** (1 + al)
pb.plot(al, wg, color=charts.line("dna"), lw=1.8, label="identical generalists")
pb.axhline(0.25, color=charts.line("rna"), lw=1.6, ls=(0, (4, 2)), label="specialized germ + soma")
pb.axvline(1, color=P.muted(), lw=0.8)
pb.set_xlim(0.2, 4)
charts.style_axes(pb, "curvature of trade-off α", "group fitness W")
pb.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
data = [("Chlamydomonas", 1, 0.0), ("Gonium", 16, 0.0), ("Pandorina", 16, 0.0),
        ("Pleodorina californica", 64, 24 / 64), ("Volvox carteri", 2016, 2000 / 2016)]
for name, n, f in data:
    pc.plot([n], [f], "o", ms=8, color=charts.line("plant"), zorder=5)
    dy = {"Gonium": 0.07, "Pandorina": -0.07}.get(name, 0.07)
    pc.text(n * 1.25, f + dy, name, fontsize=FT["tiny"], color=P.ink(), style="italic", va="center")
pc.set_xscale("log"); pc.set_xlim(0.7, 2e4); pc.set_ylim(-0.1, 1.1)
charts.style_axes(pc, "number of cells", "fraction of somatic cells")
