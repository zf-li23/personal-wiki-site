# The sliding-filament mechanism: one sarcomere drawn to scale when relaxed (2.6 um) and contracted (2.1 um),
# with A band, I band and H zone; and the isometric length-tension curve of frog muscle (Gordon, Huxley &
# Julian 1966) with filament configurations at key lengths and the overlap prediction of the descending limb.
import numpy as np

import wikibio as bio
from wikibio import physiology as phys
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 12.4)

# ---- A: relaxed vs contracted, M lines aligned ------------------------------------------------------
bio.panel(ax, "A", (0.1, 12.3))
scale = 3.3  # canvas units per um
xm = 6.0
states = [(2.6, 8.4, "Relaxed"), (2.1, 3.0, "Contracted")]
edges = []
for SL, y, name in states:
    e = phys.sarcomere(ax, xm - SL * scale / 2, y, SL, scale=scale, rows=3)
    edges.append(e)
    bio.label(ax, (0.5, e["top"] + 1.75), f"{name}\n{SL:g} µm", size="small", bold=True, ha="left")
# the A band keeps its width; I band and H zone shorten
for xa in edges[0]["A"]:
    ax.plot([xa, xa], [edges[1]["top"] + 1.6, edges[0]["bottom"]], color=P.muted(), lw=0.7, ls=(0, (2, 2)), zorder=1)
bio.label(ax, (xm, (edges[0]["bottom"] + edges[1]["top"]) / 2 + 0.75), "A band constant;  I band and H zone shorten",
          size="tiny", color=P.muted())
# key
kx, ky = 0.6, 0.55
for k, (tok, text) in enumerate((("muscle", "thin filament (actin)"), ("protein", "thick filament (myosin)"))):
    x = kx + k * 5.2
    ax.plot([x, x + 0.6], [ky, ky], color=P.edge(tok), lw=3.0, solid_capstyle="round", zorder=10)
    bio.label(ax, (x + 0.75, ky), text, size="tiny", ha="left")

# ---- B: length-tension ----------------------------------------------------------------------------------
X0, Y0, W, H = 14.6, 1.4, 9.6, 6.9
pl = quant.Plot(ax, (X0, Y0, W, H), (1.2, 3.8), (0, 1.15), xlabel="Sarcomere length / µm",
                ylabel="Active tension (relative)", xticks=[1.5, 2.0, 2.5, 3.0, 3.5], yticks=[0, 0.5, 1.0], grid=True)
bio.panel(ax, "B", (X0 - 1.5, 12.3))
SL = np.linspace(1.2, 3.8, 400)
pred = np.where(SL >= 2.25, phys.overlap(SL) / ((phys.THICK - phys.BARE) / 2), np.nan)
pl.line(SL, phys.length_tension(SL), "muscle", lw=3.6)
pl.line(SL, pred, "protein", lw=1.3, dashed=True, color=P.surface())
pl.text(3.0, 0.62, "dashed: predicted from the overlap\nof thin filaments with myosin heads", ha="left", va="bottom", color=P.muted())
key = [(1.6, "1"), (1.9, "2"), (2.15, "3"), (3.65, "4")]
for k, (sl, tag) in enumerate(key):
    tval = float(phys.length_tension(sl))
    pl.points([sl], [tval], "ink", r=0.11, zorder=14)
    pl.text(sl + 0.07, tval + 0.05, tag, ha="left", va="bottom", size="small", bold=True)
# glyphs of the four configurations above the plot
gs = 0.85
gy = 10.4
gap = (W + 0.6 - sum(sl for sl, _ in key) * gs) / (len(key) - 1)
notes = ["thick filaments\nhit the Z discs", "thin filaments\ndouble-overlap", "full overlap\n(plateau)", "no overlap"]
gx = X0 - 0.3
for k, (sl, tag) in enumerate(key):
    cx = gx + sl * gs / 2
    phys.sarcomere(ax, gx, gy, sl, scale=gs, rows=2, spacing=0.32, labels=False, bands=False, detail=False)
    bio.label(ax, (cx, gy + 0.85), f"{tag}:  {sl:g} µm", size="tiny", bold=True)
    bio.label(ax, (cx, gy - 0.75), notes[k], size="tiny", color=P.muted(), va="top")
    gx += sl * gs + gap
