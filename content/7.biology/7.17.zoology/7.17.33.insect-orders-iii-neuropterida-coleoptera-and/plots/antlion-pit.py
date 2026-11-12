# The economics of an antlion pit (model, illustrative parameters). A conical pit of rim radius R with walls
# at the angle of repose theta of dry sand (about 30-35 degrees) has depth h = R tan(theta) and volume
# V = (pi/3) R^3 tan(theta). Lifting the excavated sand to the surface requires at least the work
# W = rho g pi R^4 tan^2(theta) / 12 (rho: bulk density of sand, about 1500 kg/m^3), whereas the chance that a
# wandering ant meets the pit grows with its rim diameter, ~ R, and its area grows with R^2. The cost of
# digging therefore rises much faster with pit size than the benefit, so that pit size is expected to be
# set by larval size and prey availability. Values are a model, not measurements.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rho, g = 1500.0, 9.81
R = np.linspace(0.2, 4.0, 200) / 100  # m
fig, ax = bio.canvas(16, 9.5)
a = charts.axes_at(ax, (1.9, 1.4, 13.2, 7.4))
for th, tok in ((30, "enzyme"), (35, "negative")):
    t = np.tan(np.deg2rad(th))
    W = rho * g * np.pi * R ** 4 * t ** 2 / 12
    a.plot(R * 100, W * 1e3, color=P.edge(tok), lw=2, label=f"minimum digging work, wall angle {th} deg")
Rn = R / R.max()
Wmax = rho * g * np.pi * R.max() ** 4 * np.tan(np.deg2rad(35)) ** 2 / 12 * 1e3
a.plot(R * 100, Wmax * Rn, color=P.edge("positive"), lw=1.6, ls="--", label="encounter rate with ants ~ R (scaled)")
a.plot(R * 100, Wmax * Rn ** 2, color=P.edge("positive"), lw=1.2, ls=":", label="pit area ~ R^2 (scaled)")
a.set_xlim(0, 4.0)
a.set_xlabel("Pit radius at the rim, R (cm)")
a.set_ylabel("Work to excavate (mJ)")
a.legend(fontsize=7, frameon=False, loc="upper left")
