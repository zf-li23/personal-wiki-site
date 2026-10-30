"""Sequential excitation of modes as diffusivities fall with synchronous cleavage (KST, Section 33.7.1).

Two-species Turing kinetics (Turing's example, a11 = 3/16, a12 = 1/4, a21 = a22 = -1/4) with the diffusivity ratio
nu / mu = r chosen so that the band of unstable k^2 spans a factor B / A = 1.5. On an interval of unit length the
modes are cos(n pi x), k_n^2 = n^2 pi^2; the diffusivities fall by theta = 2^(-1/2) per generation m, so mode n is
unstable when A < n^2 theta^m < B (A = 0.8, B = 1.2 after scaling). A: the growth rate against s = n^2 theta^m
(a universal curve). B: generations (rows) and modes (columns); filled: unstable in that generation. Only at m = 13
are two modes (n = 9 and 10) unstable together.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
a11, a12, a21, a22 = 3 / 16, 1 / 4, -1 / 4, -1 / 4
Dt = a11 * a22 - a12 * a21
rho = 1.5


def f(r):
    return (a11 * r + a22) ** 2 * rho - Dt * r * (1 + rho) ** 2


r = brentq(f, 3.5, 20.0)
ssum = (a11 * r + a22) / r
s1 = ssum / (1 + rho)
s2 = rho * s1
A, B = 0.8, 1.2
scale = s1 / A                      # mu0 pi^2 in units of s


def sigma(s):
    mu, nu = s * scale, r * s * scale  # mu k^2 and nu k^2
    tr = a11 + a22 - mu - nu
    det = (a11 - mu) * (a22 - nu) - a12 * a21
    return (tr + np.sqrt(tr**2 - 4 * det + 0j)).real / 2


fig, ax = bio.canvas(26.0, 10.0)
pa = C.axes_at(ax, (1.8, 1.6, 8.6, 6.8))
s = np.linspace(0.4, 1.8, 400)
pa.plot(s, sigma(s), color=Q.line_color("protein"), lw=1.8)
pa.axhline(0, color=P.muted(), lw=0.8)
pa.axvspan(A, B, color=P.mix(P.fill("highlight"), P.surface(), 0.6), lw=0)
pa.set_xlim(0.4, 1.8)
C.style_axes(pa, "s = n² θ^m (scaled)", "growth rate σ")
pa.text((A + B) / 2, pa.get_ylim()[0] * 0.6, "unstable\nwindow", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
bio.panel(ax, "A", (0.3, 9.8))
bio.label(ax, (1.8, 9.6), "Dispersion relation", size="small", bold=True, ha="left", va="top")

theta = 2 ** -0.5
pb = C.axes_at(ax, (13.4, 1.6, 11.6, 6.8))
M, Nn = 15, 12
for m in range(M):
    for n in range(1, Nn + 1):
        v = n * n * theta**m
        on = A < v < B
        pb.add_patch(__import__("matplotlib").patches.Rectangle((n - 0.42, m - 0.42), 0.84, 0.84,
                     facecolor=Q.line_color("protein") if on else P.mix(P.fill("neutral"), P.surface(), 0.75),
                     edgecolor="none"))
pb.set_xlim(0.4, Nn + 0.6)
pb.set_ylim(M - 0.4, -0.6)
pb.set_xticks(range(1, Nn + 1))
pb.set_yticks(range(0, M, 2))
C.style_axes(pb, "mode n", "generation m")
bio.panel(ax, "B", (12.0, 9.8))
bio.label(ax, (13.4, 9.6), "Which mode is unstable in which generation", size="small", bold=True, ha="left", va="top")
