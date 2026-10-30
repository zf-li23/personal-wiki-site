"""Contact inhibition of division and number fluctuations (Section 31.7).

A: 120 synthetic tissue samples with areal nuclear density rho between 0.007 and 0.03 per square micrometre; the
probability of mitosis follows the collision model (31.10) in the form m = 0.13 (1/rho - 30.8 um^2) percent, and each
sample of about 250 nuclei gives a binomial count of mitoses. The least-squares line of m against 1/rho recovers
the slope and intercept of Eq. (31.9). B: hard rods on a line (Tonks gas): N rods of length a placed at random
without overlap (exponential free gaps) on a ring; the number of rod centres in windows of length 40a. The
variance-to-mean ratio (points, 4000 windows per packing fraction) follows (1 - rho v0)^2 (line), the result of
Theorem 31.7.1; independent positions would give 1 (dashed).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
rng = np.random.default_rng(11)
fig, ax = bio.canvas(24.0, 9.5)

# A
rho = rng.uniform(0.007, 0.03, 120)
m_true = 0.13 * (1 / rho - 30.8)          # percent
n = rng.poisson(250, 120)
m_obs = 100 * rng.binomial(n, np.clip(m_true, 0, 100) / 100) / n
X = 1 / rho
A_ = np.vstack([np.ones_like(X), X]).T
c0, c1 = np.linalg.lstsq(A_, m_obs, rcond=None)[0]
pa = C.axes_at(ax, (1.8, 1.5, 8.6, 6.6))
pa.plot(X, m_obs, "o", ms=3.6, color=Q.line_color("protein"), alpha=0.85)
xs = np.linspace(30, 145, 50)
pa.plot(xs, c0 + c1 * xs, color=P.ink(), lw=1.6, label=f"fit: m = {c0:.1f} + {c1:.3f}/ρ")
pa.plot(xs, -4 + 0.13 * xs, color=P.muted(), lw=1.2, ls=(0, (4, 2)), label="m = −4 + 0.13/ρ")
pa.set_xlim(30, 145)
pa.set_ylim(-1, 18)
C.style_axes(pa, "1/ρ / µm²", "mitotic index m / %")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 9.3))
bio.label(ax, (1.8, 9.1), "Index against inverse density", size="small", bold=True, ha="left", va="top")

# B
a, N, w = 1.0, 2000, 40.0
etas = np.linspace(0.05, 0.8, 12)
ratio = []
for eta in etas:
    L = N * a / eta
    vals = []
    for rep in range(20):
        gaps = rng.exponential(1.0, N)
        gaps *= (L - N * a) / gaps.sum()
        centres = np.cumsum(gaps + a) - a / 2
        starts = rng.uniform(0, L - w, 200)
        idx = np.searchsorted(centres, starts)
        idx2 = np.searchsorted(centres, starts + w)
        vals.append(idx2 - idx)
    vals = np.concatenate(vals)
    ratio.append(vals.var() / vals.mean())
pb = C.axes_at(ax, (14.0, 1.5, 8.6, 6.6))
e = np.linspace(0, 0.85, 100)
pb.plot(e, (1 - e) ** 2, color=P.ink(), lw=1.6, label="(1 − ρv₀)²")
pb.axhline(1.0, color=P.muted(), lw=1.0, ls=(0, (4, 2)), label="Poisson")
pb.plot(etas, ratio, "o", ms=5, color=Q.line_color("enzyme"), label="hard rods, simulation")
pb.set_xlim(0, 0.85)
pb.set_ylim(0, 1.1)
C.style_axes(pb, "packing fraction ρv₀", "Var(N) / E[N]")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (12.5, 9.3))
bio.label(ax, (14.0, 9.1), "Number fluctuations with excluded volume", size="small", bold=True, ha="left", va="top")
