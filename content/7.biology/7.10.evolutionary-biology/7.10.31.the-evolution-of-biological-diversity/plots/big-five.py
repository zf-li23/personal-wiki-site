"""The five largest mass extinctions of the Phanerozoic on the ICS geological time scale (Section 31.4).
Ages are the period boundaries (the Late Devonian extinction is placed at the Frasnian-Famennian
boundary, about 372 Myr ago). The magnitudes noted are those given by Futuyma and Kirkpatrick (2017)
and Barton et al. (2007); estimates differ among studies and measures (families, genera or species)."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, phylo

P = bio.P
FT = bio.core.FONT
ink, muted = P.ink(), P.muted()
fig, ax = plt.subplots(figsize=(10.6, 3.6))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.97)
EVENTS = [(444, "end-Ordovician", "cooling and falling sea level;\npossibly the second largest", 2.7),
          (372, "Late Devonian", "marine, prolonged;\ncauses debated", 1.55),
          (252, "end-Permian", "Siberian Traps volcanism;\n>80 % of marine invertebrate species", 2.7),
          (201, "end-Triassic", "carbon release, warming;\nmarine diversity about halved", 1.55),
          (66, "K/Pg", "Chicxulub impact;\nnon-avian dinosaurs, ammonites", 2.7)]
ax.set_xlim(545, -5)
ax.set_ylim(-1.1, 3.6)
bottom = phylo.geo_scale(ax, (541, 0), (541, 0), 0.0, ranks=("era", "period"), height=0.45)
for x, name, note, h in EVENTS:
    ax.plot([x, x], [0.05, h], color=charts.line("negative"), lw=1.4)
    ax.plot([x], [h], "v", ms=7, color=charts.line("negative"))
    ax.text(x, h + 0.12, name, ha="center", va="bottom", fontsize=FT["small"], color=ink, weight="bold")
    ax.text(x - 4, h - 0.12, note, ha="left", va="top", fontsize=FT["tiny"], color=muted)
for tick in (500, 400, 300, 200, 100, 0):
    ax.text(tick, bottom - 0.12, f"{tick}", ha="center", va="top", fontsize=FT["tiny"], color=muted)
ax.text(270, bottom - 0.45, "time (Myr ago)", ha="center", va="top", fontsize=FT["small"], color=ink)
ax.axis("off")
