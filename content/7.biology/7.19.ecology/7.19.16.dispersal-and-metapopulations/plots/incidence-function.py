"""A spatially realistic metapopulation: Hanski's incidence function model (illustrative parameters).

Sixty habitat patches placed at random in a 10 km x 10 km landscape (seed 4), with log-normal areas
A_i (median 0.5 ha). Discrete-time stochastic dynamics: an occupied patch goes extinct in a year with
probability E_i = min(1, e / A_i^x) (e = 0.1, x = 1); an empty patch is colonized with probability
C_i = S_i^2 / (S_i^2 + y^2) (y = 2.5), where the connectivity S_i = sum_j p_j exp(-alpha d_ij) A_j^b
(alpha = 1 per km, b = 0.5) counts occupied patches j weighted by their area and distance d_ij.
A: the landscape (circle size increases with patch area); fill shows the fraction of the last 400 of
600 simulated years in which each patch was occupied. B: the same incidences against patch area, colored
by mean connectivity (low, middle, high third), with the equilibrium incidence of the model,
J = C / (C + E - C E), for three fixed connectivities (lines). Large, well-connected patches are almost
always occupied; small, isolated ones rarely.
"""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)
n = 60
xy = rng.uniform(0, 10, (n, 2))
A = np.exp(rng.normal(np.log(0.5), 1.0, n))
e, x, y, alpha, b = 0.1, 1.0, 2.5, 1.0, 0.5
d = np.hypot(*(xy[:, None, :] - xy[None, :, :]).transpose(2, 0, 1))
Wt = np.exp(-alpha * d) * A[None, :] ** b
np.fill_diagonal(Wt, 0)
E = np.minimum(1, e / A ** x)
p = rng.random(n) < 0.5
occ = np.zeros(n)
Ssum = np.zeros(n)
T, burn = 600, 200
for t in range(T):
    S = Wt @ p
    Cp = S ** 2 / (S ** 2 + y ** 2)
    u = rng.random(n)
    p = np.where(p, u > E, u < Cp)
    if t >= burn:
        occ += p
        Ssum += S
inc = occ / (T - burn)
Smean = Ssum / (T - burn)

fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.0, 1.4, 8.5, 8.5))
for k in range(n):
    rad = 0.08 + 0.13 * np.sqrt(A[k])
    col = P.mix(P.fill("dna"), P.surface(), 1 - inc[k])
    pa.add_patch(Circle(xy[k], rad, facecolor=col, edgecolor=P.edge("dna"), lw=0.7))
pa.set_xlim(0, 10)
pa.set_ylim(0, 10)
pa.set_aspect("equal")
C.style_axes(pa, "km", "km", box=True)
bio.panel(ax, "A", (0.3, 10.6))
bio.label(ax, (2.0, 10.2), "Patch network (fill = incidence)", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (15.5, 1.4, 13.5, 8.5))
cuts = np.quantile(Smean, [1 / 3, 2 / 3])
grp = np.digitize(Smean, cuts)
for g, tok, lab in [(0, "negative", "low connectivity"), (1, "atp", "middle"), (2, "dna", "high connectivity")]:
    sel = grp == g
    pb.plot(A[sel], inc[sel], "o", ms=4, color=Q.line_color(tok), label=lab)
Ag = np.logspace(np.log10(A.min() * 0.8), np.log10(A.max() * 1.2), 200)
Eg = np.minimum(1, e / Ag ** x)
for S, tok in [(np.quantile(Smean, 1 / 6), "negative"), (np.median(Smean), "atp"), (np.quantile(Smean, 5 / 6), "dna")]:
    Cg = S ** 2 / (S ** 2 + y ** 2)
    pb.plot(Ag, Cg / (Cg + Eg - Cg * Eg), color=Q.line_color(tok), lw=1.2)
pb.set_xscale("log")
pb.set_ylim(-0.02, 1.02)
C.style_axes(pb, "patch area A (ha)", "incidence (fraction of years occupied)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (13.8, 10.6))
bio.label(ax, (15.5, 10.2), "Incidence rises with area and connectivity", size="small", bold=True, ha="left")
