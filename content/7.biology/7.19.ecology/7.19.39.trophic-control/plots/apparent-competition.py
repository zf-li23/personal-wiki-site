"""Apparent competition between two prey that share a predator (Holt 1977).

dN1/dt = N1 [r1 (1 - N1/K1) - a1 P]
dN2/dt = N2 [r2 (1 - N2/K2) - a2 P]
dP/dt  = P [e1 a1 N1 + e2 a2 N2 - m - q P]
with r1 = 1, K1 = 1, a1 = 0.5 (prey 1 is less vulnerable), r2 = 0.5, K2 = 1, a2 = 1, e1 = e2 = 1,
m = 0.1, q = 0.5. The prey do not compete for any resource. If the predator equilibrates fast,
P = (e1 a1 N1 + e2 a2 N2 - m)/q, and the prey obey Lotka-Volterra competition equations with
rho_i = r_i + a_i m / q, beta_ii = r_i/K_i + e_i a_i^2/q and beta_ij = a_i e_j a_j / q.
A: the two straight zero-growth isoclines of this reduced system (prey 1 green, prey 2 orange) and
trajectories of the full three-species model projected on the (N1, N2) plane (gray, from five starts;
dots: start). The isocline of prey 1 lies outside that of prey 2: prey 1 excludes prey 2.
B: time course: prey 2 and the predator at equilibrium; prey 1 introduced at t = 50 at low density.
The predator increases on the extra food and drives prey 2 to extinction.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

r1, K1, a1, e1 = 1.0, 1.0, 0.5, 1.0
r2, K2, a2, e2 = 0.5, 1.0, 1.0, 1.0
m, q = 0.1, 0.5


def rhs(t, y):
    n1, n2, p = np.maximum(y, 0)
    return [n1 * (r1 * (1 - n1 / K1) - a1 * p), n2 * (r2 * (1 - n2 / K2) - a2 * p),
            p * (e1 * a1 * n1 + e2 * a2 * n2 - m - q * p)]


rho1, rho2 = r1 + a1 * m / q, r2 + a2 * m / q
b11, b12 = r1 / K1 + e1 * a1 ** 2 / q, a1 * e2 * a2 / q
b21, b22 = a2 * e1 * a1 / q, r2 / K2 + e2 * a2 ** 2 / q
pa = C.axes_at(ax, (2.6, 1.9, 9.0, 8.4))
x = np.linspace(0, 1.0, 50)
pa.plot(x, (rho1 - b11 * x) / b12, color=Q.line_color("positive"), lw=1.8, label="prey 1 isocline")
pa.plot(x, (rho2 - b21 * x) / b22, color=Q.line_color("rna"), lw=1.8, label="prey 2 isocline")
for y0 in [(0.05, 0.6, 0.2), (0.9, 0.5, 0.2), (0.3, 0.05, 0.1), (0.05, 0.1, 0.05), (0.6, 0.8, 0.5)]:
    s = solve_ivp(rhs, (0, 300), y0, rtol=1e-8, atol=1e-11, t_eval=np.linspace(0, 300, 1500))
    pa.plot(s.y[0], s.y[1], color=P.muted(), lw=0.9)
    pa.plot([y0[0]], [y0[1]], "o", ms=3, color=P.muted())
pa.plot([rho1 / b11], [0], "o", ms=6, color=Q.line_color("positive"), mec=P.ink(), mew=0.6, zorder=5)
pa.set_xlim(0, 1.0)
pa.set_ylim(0, 1.0)
C.style_axes(pa, "prey 1, N1", "prey 2, N2")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Isoclines of the reduced system", size="small", bold=True, ha="left")

s1 = solve_ivp(rhs, (0, 50), [0.0, 0.5, 0.2], rtol=1e-8, atol=1e-11, t_eval=np.linspace(0, 50, 200))
y = s1.y[:, -1].copy()
y[0] = 0.01
s2 = solve_ivp(rhs, (50, 400), y, rtol=1e-8, atol=1e-11, t_eval=np.linspace(50, 400, 1400))
t = np.concatenate([s1.t, s2.t])
Y = np.concatenate([s1.y, s2.y], axis=1)
pb = C.axes_at(ax, (16.0, 1.9, 12.8, 8.4))
for i, (lab, tok) in enumerate([("prey 1", "positive"), ("prey 2", "rna"), ("predator", "negative")]):
    pb.plot(t, Y[i], color=Q.line_color(tok), lw=1.7, label=lab)
pb.axvline(50, color=P.muted(), lw=0.8, ls="--")
pb.text(54, 0.8, "prey 1 introduced", fontsize=FS["tiny"], color=P.ink())
pb.set_xlim(0, 400)
pb.set_ylim(0, 0.85)
C.style_axes(pb, "time", "density")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1, 0.92))
bio.panel(ax, "B", (14.0, 11.6))
bio.label(ax, (16.0, 11.2), "Exclusion through a shared predator", size="small", bold=True, ha="left")
