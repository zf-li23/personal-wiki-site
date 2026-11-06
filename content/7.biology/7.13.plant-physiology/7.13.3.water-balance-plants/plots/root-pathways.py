# Radial water uptake by a young root as a hydraulic circuit.
# A: eudicot root in transverse section (zone of maturation; Casparian strips red in the endodermis),
#    with the radial path marked: soil -> root hair / epidermis -> cortex -> endodermis -> pericycle -> xylem.
# B: the same path as resistances in series and parallel: soil and the root-soil interface; across the cortex
#    the apoplastic route (cell walls) in parallel with the cell-to-cell route (symplast via plasmodesmata and
#    the transmembrane route via aquaporins); at the endodermis the apoplastic route is blocked by the
#    Casparian strip, so all water crosses membranes; then the low-resistance axial path in the xylem.
#    When transpiration stops, ions loaded into the xylem lower its osmotic potential and the root acts as an
#    osmometer: water flows in across the endodermis and root pressure builds up.
import numpy as np

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(28.0, 10.6)


def resistor(a, b, text=None, tok="neutral", below=False):
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = b[0] - a[0]
    xs = [a[0], a[0] + 0.25 * L]
    ys = [a[1], a[1]]
    n = 6
    for k in range(n):
        xs.append(a[0] + 0.25 * L + (k + 0.5) * 0.5 * L / n)
        ys.append(a[1] + (0.22 if k % 2 == 0 else -0.22))
    xs += [a[0] + 0.75 * L, b[0]]
    ys += [a[1], a[1]]
    ax.plot(xs, ys, color=P.edge(tok), lw=1.5, zorder=8, solid_joinstyle="round")
    if text:
        bio.label(ax, ((a[0] + b[0]) / 2, a[1] + (-0.6 if below else 0.6)), text, size="tiny")


def node(xy, text, tok="neutral"):
    bio.box(ax, xy, 2.0, 1.0, tok, text=text, size="tiny")


# ---- A ------------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 10.5))
c = np.array([5.2, 5.0])
R = 4.3
B.root_section(ax, c, R, kind="eudicot", hairs=4)
ang = np.radians(205)
d = np.array([np.cos(ang), np.sin(ang)])
p0, p1 = c + d * (R + 0.4), c + d * 0.55
bio.arrow(ax, p0, p1, kind="process", color=P.edge("dna"), lw=2.2, head=0.3, zorder=30)
for frac, txt, xy in ((0.97, "epidermis", (0.5, 2.1)), (0.62, "cortex", (1.3, 1.25)), (0.36, "endodermis", (2.6, 0.55)),
                      (0.1, "xylem", (4.3, 0.2))):
    bio.callout(ax, c + d * R * frac + np.array([0, 0.05]), xy, txt, size="tiny")

# ---- B ------------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (11.0, 10.5))
y0, yu, yd = 5.0, 7.3, 2.7
node((12.4, y0), "Soil", "cell_wall")
resistor((13.4, y0), (15.4, y0), "soil + interface")
x1 = 15.4
ax.plot([x1, x1], [yd, yu], color=P.muted(), lw=1.2, zorder=7)
resistor((x1, yu), (19.4, yu), "apoplast: cell walls", tok="cell_wall")
resistor((x1, yd), (19.4, yd), "cell to cell: plasmodesmata,\nmembranes (aquaporins)", tok="channel", below=True)
x2 = 19.4
ax.plot([x2, x2], [yd, yu], color=P.muted(), lw=1.2, zorder=7)
ax.plot([x2, 19.9], [y0, y0], color=P.muted(), lw=1.2, zorder=7)
resistor((19.9, y0), (22.7, y0), "endodermis:\nmembranes only", tok="golgi")
node((23.7, y0), "Xylem", "channel")
resistor((24.7, y0), (27.3, y0), "axial\n(small)", tok="channel")
# Casparian strip blocking the apoplast at the endodermis
bio.label(ax, (21.3, 8.6), "Casparian strip blocks the apoplastic route", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (20.2, 8.25), (19.75, 7.45), kind="inhibition", color=P.edge("negative"), lw=1.2)
bio.label(ax, (16.2, 9.8), "Cortex (parallel routes)", size="small", bold=True)
# root pressure
bio.arrow(ax, (23.7, 2.2), (23.7, 4.35), kind="process", color=P.edge("k"), lw=1.3)
bio.label(ax, (23.7, 1.6), "ions loaded into xylem:\nΨs falls → root pressure", size="tiny")
bio.label(ax, (19.4, 0.5), "Transpiring: tension in the xylem pulls water (hydrostatic gradient, apoplast important)",
          size="tiny", color=P.muted())
