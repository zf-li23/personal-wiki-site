# Continuity in a leuconoid sponge (schematic). The same volume flow Q passes every stage of the
# aquiferous system, so the mean speed at a stage is Q divided by the total cross-section of all the
# parallel channels at that stage. Relative areas are illustrative, chosen to show the typical profile.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
stages = ["Ostia", "Incurrent\ncanals", "Prosopyles", "Choanocyte\nchambers", "Apopyles", "Excurrent\ncanals", "Osculum"]
area = np.array([40.0, 15.0, 150.0, 1500.0, 250.0, 6.0, 1.0])  # relative to the osculum
speed = 1.0 / area

fig, ax = bio.canvas(16, 8.6)
x = np.arange(len(stages))
pl = quant.Plot(ax, (2.2, 1.6, 12.6, 6.0), (-0.6, len(stages) - 0.4), (0.0005, 3000), ylog=True,
                ylabel="Relative to osculum (log scale)", ylabel_offset=1.45,
                xlabel="Direction of water flow", xlabel_offset=1.05,
                yticks=[(0.001, "0.001"), (0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")],
                grid=True)
for i, a in enumerate(area):
    x0, y0 = pl.xy(i - 0.3, 0.0005)
    x1, y1 = pl.xy(i + 0.3, a)
    bio.box(ax, ((x0 + x1) / 2, (y0 + y1) / 2), x1 - x0, y1 - y0, token="channel", radius=0.05, zorder=6)
    bio.label(ax, (pl.X(i), y0 - 0.15), stages[i], size="tiny", va="top")
pl.line(x, speed, token="negative", lw=2.0)
for i, s in enumerate(speed):
    ax.plot(pl.X(i), pl.Y(s), "o", ms=5, color=quant.line_color("negative"), zorder=12)
bio.label(ax, (pl.X(3.0) + 0.75, pl.Y(1500)), "Total cross-section", size="small", color=P.edge("channel"), ha="left")
bio.label(ax, (pl.X(4.5), pl.Y(0.0015)), "Mean speed", size="small", color=quant.line_color("negative"))
