"""Steepening of a morphogen gradient into a stationary shock at a nodal line (Section 33.8.3, case 1).

The local amplitude equation d phi / d theta = sigma + theta phi + lambda phi^3, lambda = -1, where sigma is
proportional to the distance from the nodal point and theta to time. A: profiles phi(sigma) at successive times
theta, started from phi = 0 at theta = -3: the smooth gradient becomes steeper and develops a jump at sigma = 0.
B: the equilibrium surface sigma + theta phi - phi^3 = 0 (the cusp) for sigma = -0.05, 0, +0.05: for theta > 0 the
system follows one of the two outer branches, selected by the sign of sigma, and the middle branch is unstable.
"""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
lam = -1.0
sig = np.linspace(-0.4, 0.4, 161)
th_out = [-1.0, 0.0, 1.0, 2.0, 3.0]
sol = solve_ivp(lambda th, phi: sig + th * phi + lam * phi**3, (-3, 3), np.zeros_like(sig), t_eval=th_out, rtol=1e-8,
                atol=1e-10)
fig, ax = bio.canvas(24.0, 9.5)
pa = C.axes_at(ax, (1.8, 1.5, 8.6, 6.6))
toks = ["neutral", "channel", "positive", "highlight", "drug"]
for k, th in enumerate(th_out):
    pa.plot(sig, sol.y[:, k], color=Q.line_color(toks[k]), lw=1.7, label=f"θ = {th:g}")
pa.axvline(0, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
C.style_axes(pa, "σ (distance from the nodal point)", "φ")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 9.3))
bio.label(ax, (1.8, 9.1), "A gradient steepens into a shock", size="small", bold=True, ha="left", va="top")

pb = C.axes_at(ax, (14.0, 1.5, 8.6, 6.6))
phi = np.linspace(-2.2, 2.2, 800)
for s0, tk in ((-0.05, "channel"), (0.0, "neutral"), (0.05, "drug")):
    th = (phi**3 - s0) / phi
    ok = np.abs(phi) > 1e-3
    stable = (th - 3 * phi**2) < 0
    for mask, ls in ((ok & stable, "-"), (ok & ~stable, (0, (3, 2)))):
        y = np.where(mask, phi, np.nan)
        pb.plot(th, y, color=Q.line_color(tk), lw=1.6, ls=ls)
pb.plot([], [], color=Q.line_color("channel"), label="σ = −0.05")
pb.plot([], [], color=Q.line_color("neutral"), label="σ = 0")
pb.plot([], [], color=Q.line_color("drug"), label="σ = +0.05")
pb.set_xlim(-1.5, 4)
pb.set_ylim(-2.2, 2.2)
C.style_axes(pb, "θ (time)", "equilibrium φ")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (12.5, 9.3))
bio.label(ax, (14.0, 9.1), "Equilibria: a cusp (dashed: unstable)", size="small", bold=True, ha="left", va="top")
