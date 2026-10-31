# Resolution of compound eyes and camera eyes (geometric and diffraction limits).
# Compound eye of radius r with facets of diameter delta: the angle between neighbouring ommatidia is
# theta_s = delta / r (sampling), and the diffraction blur of one facet lens is theta_d = lambda / delta
# (prefactor dropped, lambda = 0.5 um). Their sum is smallest at delta_opt = sqrt(lambda r), where
# theta = 2 sqrt(lambda / r).
# A: the two contributions for r = 1 mm and their sum; the optimum facet is 22 um (about the 20-25 um of
#    honeybee facets).
# B: best angular resolution against eye size: compound eye, theta = 2 sqrt(lambda / r); camera eye with
#    pupil diameter D, Rayleigh limit theta = 1.22 lambda / D. The human eye (D = 2-3 mm) reaches about one
#    arc minute; a compound eye would need a radius of metres to do the same.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
lam = 0.5e-6
fig, axs = plt.subplots(1, 2, figsize=(11.2, 4.0))

ax = axs[0]
r = 1e-3
d = np.linspace(3e-6, 80e-6, 400)
deg = 180 / np.pi
ax.plot(d * 1e6, d / r * deg, color=charts.line("dna"), lw=1.6, label="sampling δ / r")
ax.plot(d * 1e6, lam / d * deg, color=charts.line("rna"), lw=1.6, label="diffraction λ / δ")
ax.plot(d * 1e6, (d / r + lam / d) * deg, color=P.ink(), lw=1.8, label="sum")
dopt = np.sqrt(lam * r)
ax.plot(dopt * 1e6, 2 * np.sqrt(lam / r) * deg, "o", ms=5, color=charts.line("atp"))
ax.text(dopt * 1e6 + 2, 2 * np.sqrt(lam / r) * deg + 0.6, f"δ_opt = {dopt * 1e6:.0f} μm,\nθ = {2 * np.sqrt(lam / r) * deg:.1f}°",
        fontsize=7, color=P.ink())
ax.set_ylim(0, 8)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "facet diameter δ / μm", "angle / degree")
charts.title(ax, "A   Optimal facet size (r = 1 mm)")

ax = axs[1]
size = np.logspace(-4, 2, 300)
arcmin = 180 * 60 / np.pi
ax.loglog(size * 1e3, 2 * np.sqrt(lam / size) * arcmin, color=charts.line("enzyme"), lw=1.8,
          label="compound eye, radius r")
ax.loglog(size * 1e3, 1.22 * lam / size * arcmin, color=charts.line("protein"), lw=1.8,
          label="camera eye, pupil diameter D")
ax.axhline(1.0, color=P.muted(), lw=0.6, ls=":")
ax.text(2e-1, 1.15, "1 arc minute", fontsize=7, color=P.muted())
ax.plot(2.5, 1.22 * lam / 2.5e-3 * arcmin, "o", ms=5, color=charts.line("protein"))
ax.text(3.2, 0.5, "human pupil", fontsize=7, color=P.ink())
rneed = 4 * lam / (1 / arcmin) ** 2
ax.plot(rneed * 1e3, 1.0, "o", ms=5, color=charts.line("enzyme"))
ax.text(rneed * 1e3 / 200, 0.25, f"compound eye needs\nr ≈ {rneed:.0f} m", fontsize=7, color=P.ink())
ax.set_xlim(0.1, 1e5)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "eye size (r or D) / mm", "best resolution / arc minute")
charts.title(ax, "B   Lenses beat facets")
fig.tight_layout()
