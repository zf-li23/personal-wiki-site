# Pupil shape and defocus blur (geometric optics; idea after Banks et al. 2015, illustrative numbers).
# An eye focused at z0 sees a point at distance z as a blur patch whose angular extent along each
# axis is the pupil extent along that axis times |1/z - 1/z0| (the defocus in dioptres).
# A vertical slit (1 mm wide, 12 mm tall) blurs horizontal contours strongly and vertical contours
# hardly at all; a round pupil (4 mm) blurs both equally.
import numpy as np
from matplotlib.patches import Ellipse
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 9.6)

# A: three pupil shapes in an iris
for k, (name, w, h, eco) in enumerate((("Round", 1.2, 1.2, "active foragers,\nlarger predators"),
                                         ("Vertical slit", 0.3, 2.2, "ambush predators\nwith frontal eyes"),
                                         ("Horizontal", 2.0, 0.55, "grazing prey,\nlateral eyes"))):
    cx, cy = 1.6 + 2.6 * k, 6.0
    ax.add_patch(Ellipse((cx, cy), 2.3, 2.3, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1))
    ax.add_patch(Ellipse((cx, cy), w, h, facecolor=P.ink(), edgecolor=P.ink()))
    bio.label(ax, (cx, 8.0), name, size="small", bold=True)
    bio.label(ax, (cx, 4.1), eco, size="tiny", color=P.muted())
bio.panel(ax, "A", (0.2, 9.4))

# B: blur versus distance
z0 = 1.0
z = np.logspace(np.log10(0.2), np.log10(10), 300)
defocus = np.abs(1 / z - 1 / z0)                   # dioptres (1/m)


def blur(aperture_mm):
    return aperture_mm * 1e-3 * defocus * (180 / np.pi) * 60   # arcmin


p = quant.Plot(ax, (10.6, 1.6, 10.4, 6.8), xlim=(0.2, 10), ylim=(0, 160), xlog=True,
               xlabel="Object distance z / m (eye focused at 1 m)", ylabel="Angular blur / arcmin",
               xticks=[0.2, 0.5, 1, 2, 5, 10], yticks=[0, 40, 80, 120, 160])
p.line(z, np.minimum(blur(12), 160), "receptor")
p.line(z, blur(4), "enzyme")
p.line(z, blur(1), "channel", dashed=True)
p.vline(z0, text="focus", token="muted")
p.legend([("vertical slit, horizontal contours (12 mm)", "receptor", "-"), ("round pupil (4 mm)", "enzyme", "-"),
          ("vertical slit, vertical contours (1 mm)", "channel", "--")], at=(15.4, 8.0), step=0.42)
bio.panel(ax, "B", (9.6, 9.4))
