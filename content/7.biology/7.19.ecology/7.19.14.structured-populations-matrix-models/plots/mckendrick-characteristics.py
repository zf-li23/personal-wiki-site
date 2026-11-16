"""Continuous age structure: the McKendrick-von Foerster equation solved along characteristics.

Model: dn/dt + dn/da = -mu n, n(t, 0) = integral of m(a) n(t, a) da, with constant mortality mu = 0.3 per
year (survivorship l(a) = exp(-mu a)) and fecundity m(a) = 1.2 per year between ages 2 and 6 (0 otherwise);
ages truncated at 12 years. Initial population: a narrow pulse of individuals aged 0-1 year. Numerical
scheme: age step = time step = 0.02 year, which follows the characteristics a - t = const exactly.
A: the age distribution n(t, a) / N(t) as a heat map: cohorts travel along the diagonals and the echoes of
the initial pulse fade. B: age distributions at four times and the stable age distribution
c(a) proportional to exp(-r a) l(a) (dashed), with r the root of the Euler-Lotka equation
integral exp(-r a) l(a) m(a) da = 1.
"""

import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
mu, h, amax, tmax = 0.3, 0.02, 12.0, 40.0
a = np.arange(0, amax, h) + h / 2
l = np.exp(-mu * a)
m = np.where((a > 2) & (a < 6), 1.2, 0.0)
r = brentq(lambda r: np.sum(np.exp(-r * a) * l * m) * h - 1, -1, 2)
c = np.exp(-r * a) * l
c /= c.sum() * h

n = np.where(a < 1, 1.0, 0.0)
snaps = {}
rows = []
nt = int(tmax / h)
for k in range(nt + 1):
    t = k * h
    if k % 10 == 0:
        rows.append(n / (n.sum() * h))
    for ts in (0, 5, 10, 40):
        if abs(t - ts) < h / 2:
            snaps[ts] = n / (n.sum() * h)
    births = np.sum(m * n) * h
    n = np.r_[births, n[:-1] * np.exp(-mu * h)]
img = np.array(rows)

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 11.0, 6.8))
im = pa.imshow(img.T, origin="lower", aspect="auto", extent=[0, tmax, 0, amax], cmap="viridis",
               vmin=0, vmax=np.percentile(img, 99))
for a0 in range(-40, 12, 4):
    pa.plot([0, tmax], [a0, a0 + tmax], color="white", lw=0.4, alpha=0.5)
pa.set_xlim(0, tmax)
pa.set_ylim(0, amax)
C.style_axes(pa, "time t (years)", "age a (years)")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Cohorts move along characteristics a - t = const", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (18.0, 1.6, 11.0, 6.8))
for ts, tok in [(0, "neutral"), (5, "atp"), (10, "enzyme"), (40, "dna")]:
    pb.plot(a, snaps[ts], color=Q.line_color(tok), lw=1.5, label=f"t = {ts}")
pb.plot(a, c, color=P.ink(), lw=1.2, ls=(0, (4, 2)), label=f"stable, r = {r:.3f} per year")
pb.set_xlim(0, amax)
pb.set_ylim(0, 0.6)
C.style_axes(pb, "age a (years)", "density of ages")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (16.5, 9.6))
bio.label(ax, (18.0, 9.2), "Convergence to the stable age distribution", size="small", bold=True, ha="left")
