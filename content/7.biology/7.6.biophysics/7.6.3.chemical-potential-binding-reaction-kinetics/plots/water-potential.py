# Water potential along the soil-plant-atmosphere continuum of a transpiring plant on a moist day (typical
# values; 20 C). Water moves passively down the gradient of water potential, Psi_w = (mu_w - mu_w0)/V_w,
# measured in MPa: moist soil -0.3 MPa, root xylem -0.6 MPa, stem xylem 10 m up -0.8 MPa (including the
# gravitational term rho g h = 0.1 MPa), leaf xylem -1.0 MPa, leaf mesophyll cells -1.2 MPa, and the air at
# 50 % relative humidity, Psi = (RT/V_w) ln(RH) = -94 MPa, off the scale of the plot (arrow).
# Left: schematic tree with the sampling points; right: the potentials in order along the path.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(16.0, 7.2)

# soil and plant
ax.add_patch(Rectangle((0.2, 0.3), 6.0, 1.75, facecolor=P.fill("cell_wall"), alpha=0.35, lw=0, zorder=1))
bio.label(ax, (0.4, 0.55), "soil", size="small", ha="left", color=P.ink())
bio.icon(ax, "phylopic/tree", at=(3.2, 0.4), height=6.4, anchor="bottom", color="plant")

pts = [((4.9, 0.8), (5.6, 1.0), "soil −0.3"),
       ((3.25, 1.1), (5.6, 1.7), "root xylem −0.6"),
       ((3.25, 2.2), (5.6, 2.8), "stem xylem −0.8"),
       ((2.95, 4.6), (0.4, 5.0), "leaf xylem −1.0"),
       ((3.5, 5.6), (5.0, 6.2), "mesophyll −1.2"),
       ((2.3, 6.8), (0.4, 6.8), "air (50 % RH) −94")]
for p, t, txt in pts:
    bio.callout(ax, p, t, txt + " MPa", size="tiny")

# quantitative panel
plot = quant.Plot(ax, (8.6, 1.3, 6.6, 4.9), xlim=(-0.5, 5.5), ylim=(-1.6, 0.0), ylabel="Ψw / MPa",
                  xticks=[(0, "soil"), (1, "root"), (2, "stem"), (3, "leaf\nxylem"), (4, "meso-\nphyll"), (5, "air")],
                  yticks=[0, -0.4, -0.8, -1.2, -1.6], grid=True, ylabel_offset=1.0)
xs = np.array([0, 1, 2, 3, 4])
ys = np.array([-0.3, -0.6, -0.8, -1.0, -1.2])
plot.line(xs, ys, "plant", lw=1.8)
plot.points(xs, ys, "plant", r=0.09)
# off-scale air value
x5, y5 = plot.xy(5, -1.55)
bio.arrow(ax, plot.xy(4.1, -1.25), (x5, y5), kind="process", dashed=True, lw=1.0, head=0.16)
bio.label(ax, plot.xy(5, -0.95), "air:\n−94 MPa\n(off scale)", size="tiny", ha="center")
bio.label(ax, (11.9, 6.75), "Water flows down the gradient of Ψw", size="small", bold=True)
