# Jumping by a springtail's furcula, estimated from ballistics. A jump of height h needs take-off speed
# v = sqrt(2 g h); if the furcula pushes over a distance d at constant acceleration, a = v^2 / (2 d) and the
# push lasts t = 2 d / v. Curves: acceleration (in multiples of g) against push distance for several jump
# heights (air resistance ignored, which overestimates the height actually reached by mm-sized animals).
# Dots: published take-off measurements for comparison (froghopper Philaenus, Burrows 2003; rat flea,
# Bennet-Clark & Lucey 1967).
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
g = 9.81
fig, ax = bio.canvas(20, 9.5)
pax = charts.axes_at(ax, (2.0, 1.6, 10.5, 7.2))
d = np.logspace(-4, -2.3, 100)  # m
for h, tok in ((0.02, "neutral"), (0.05, "channel"), (0.10, "enzyme"), (0.20, "negative")):
    v = np.sqrt(2 * g * h)
    a = v ** 2 / (2 * d) / g
    pax.plot(d * 1e3, a, color=charts.line(tok), lw=1.6)
    pax.text(d[8] * 1e3, a[8] * 1.15, "h = %d cm" % round(h * 100), fontsize=8, color=charts.line(tok))
pax.scatter([4.7 ** 2 / (2 * 400 * g) * 1e3], [400], s=28, color=charts.line("protein"), zorder=5)
pax.text(3.0, 330, "froghopper", fontsize=8, color=P.ink())
pax.scatter([1.0 ** 2 / (2 * 135 * g) * 1e3], [135], s=28, color=charts.line("protein"), zorder=5)
pax.text(0.42, 110, "flea", fontsize=8, color=P.ink())
pax.set_xscale("log")
pax.set_yscale("log")
charts.style_axes(pax, "Push distance d / mm", "Take-off acceleration / g")
txt = ("v = sqrt(2 g h)\na = v^2 / (2 d)\nt = 2 d / v\n\n"
       "Example: h = 10 cm, d = 0.5 mm\nv = %.1f m/s, a = %.0f g, t = %.1f ms"
       % (np.sqrt(2 * g * 0.1), 2 * g * 0.1 / (2 * 5e-4) / g, 2 * 5e-4 / np.sqrt(2 * g * 0.1) * 1e3))
bio.label(ax, (13.6, 8.0), txt, size="small", ha="left", va="top")
