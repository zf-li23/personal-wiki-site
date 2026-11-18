"""Interaction types and stability (Allesina and Tang 2012).

Off-diagonal matrices M with S = 400 and connectance C = 0.25: each pair (i, j), i < j, interacts with
probability C. Random: M_ij and M_ji independent N(0, sigma^2). Predator-prey: one entry +|X|, the
other -|Y| (orientation random), X, Y ~ N(0, sigma^2). Competition-mutualism mixture: both entries
-|X|, -|Y| or both +|X|, +|Y| with equal probability. sigma is chosen so that sigma sqrt(SC) = 1.
The eigenvalues fill ellipses (elliptic law) with horizontal semi-axis sigma sqrt(SC)(1 + rho) and
vertical semi-axis sigma sqrt(SC)(1 - rho), where rho = E[M_ij M_ji]/Var(M_ij) is 0, -2/pi and +2/pi
in the three cases (red curves). Adding self-regulation -d shifts every cloud by -d, so the stability
condition is sigma sqrt(SC)(1 + rho) < d: predator-prey pairs tolerate 1/(1 - 2/pi) = 2.75 times
more complexity than random pairs.
"""

import numpy as np
from threadpoolctl import threadpool_limits

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
threadpool_limits(1)  # small eigenproblems: threads only add overhead
rng = np.random.default_rng(6)
fig, ax = bio.canvas(30.0, 11.0)

S, Cn = 400, 0.25
sig = 1 / np.sqrt(S * Cn)
iu = np.triu_indices(S, 1)
npair = len(iu[0])


def matrix(kind):
    link = rng.random(npair) < Cn
    x, y = np.abs(rng.normal(0, sig, npair)), np.abs(rng.normal(0, sig, npair))
    s = np.where(rng.random(npair) < 0.5, 1.0, -1.0)
    if kind == "random":
        a, b = rng.normal(0, sig, npair), rng.normal(0, sig, npair)
    elif kind == "pp":
        a, b = s * x, -s * y
    else:
        a, b = s * x, s * y
    M = np.zeros((S, S))
    M[iu] = a * link
    M[(iu[1], iu[0])] = b * link
    return M


cases = [("random", "Random (May)", 0.0, "dna"), ("pp", "Predator-prey", -2 / np.pi, "positive"),
         ("cm", "Competition + mutualism", 2 / np.pi, "rna")]
th = np.linspace(0, 2 * np.pi, 300)
for k, (kind, title, rho, tok) in enumerate(cases):
    ev = np.linalg.eigvals(matrix(kind))
    x0 = 2.4 + k * 9.4
    p = C.axes_at(ax, (x0, 1.6, 7.4, 7.4))
    p.scatter(ev.real, ev.imag, s=3, color=Q.line_color(tok), lw=0)
    p.plot((1 + rho) * np.cos(th), (1 - rho) * np.sin(th), color=Q.line_color("negative"), lw=1.2)
    p.set_xlim(-1.9, 1.9)
    p.set_ylim(-1.9, 1.9)
    p.set_aspect("equal")
    C.style_axes(p, "Re(lambda)", "Im(lambda)" if k == 0 else None)
    bio.panel(ax, "ABC"[k], (x0 - 1.9, 10.6))
    bio.label(ax, (x0, 10.2), title, size="small", bold=True, ha="left")
    bio.label(ax, (x0, 9.5), f"rho = {rho:+.2f}; max Re = {ev.real.max():.2f}", size="tiny", ha="left")
