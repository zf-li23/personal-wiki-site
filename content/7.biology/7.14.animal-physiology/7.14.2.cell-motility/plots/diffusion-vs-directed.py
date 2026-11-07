# Distance covered by diffusion and by directed motion, against time (log-log).
# Diffusion in water: root-mean-square displacement along one axis x = sqrt(2 D t), with the diffusion
# coefficients of a small molecule (500 um^2/s), a protein (50), a bacterium-sized particle (0.5) and an
# animal cell (0.05). Directed motion: x = v t, for a crawling neutrophil (about 10 um/min), a swimming
# bacterium (25 um/s) and a swimming sperm (50 um/s).
# Diffusion wins over short distances, but its time grows with the square of the distance: ten times
# farther takes a hundred times longer. Each directed line crosses the diffusion line of the same object
# at the distance where active motion starts to pay off.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(14.0, 9.6)
pa = charts.axes_at(ax, (2.3, 1.5, 11.0, 7.2))
t = np.logspace(-3, 7, 300)
for D, lab, tok in ((500, "small molecule", "metabolite"), (50, "protein", "protein"),
                    (0.5, "bacterium (passive)", "bacterium"), (0.05, "animal cell (passive)", "animal")):
    x = np.sqrt(2 * D * t)
    pa.loglog(t, x, color=charts.line(tok), lw=1.6, label="diffusion: " + lab)
for v, lab, tok in ((10 / 60, "neutrophil crawling", "blood"), (25, "bacterium swimming", "bacterium"),
                    (50, "sperm swimming", "neutral")):
    x = v * t
    pa.loglog(t, x, color=charts.line(tok), lw=1.6, ls="--", label="directed: " + lab)
for d, lab in ((10, "cell (10 µm)"), (1e3, "1 mm"), (1e6, "1 m")):
    pa.axhline(d, color=P.muted(), lw=0.6, ls=":")
    pa.text(1.3e-3, d * 1.15, lab, fontsize=7, color=P.muted())
for s, lab in ((1, "1 s"), (3600, "1 h"), (86400 * 30, "1 month")):
    pa.axvline(s, color=P.muted(), lw=0.6, ls=":")
    pa.text(s * 1.2, 3e-2, lab, fontsize=7, color=P.muted(), rotation=90, va="bottom")
leg = pa.legend(loc="upper left", fontsize=7, frameon=False, bbox_to_anchor=(0.06, 0.93))
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(1e-3, 1e7)
pa.set_ylim(1e-2, 1e7)
charts.style_axes(pa, "time / s", "distance / µm")
charts.title(pa, "Diffusion (x = √(2Dt), solid) versus directed motion (x = vt, dashed)")
