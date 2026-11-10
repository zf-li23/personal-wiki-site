# Amplification of C3b deposition on a surface (Eq. 10.1 of the page), nondimensional.
#   dx/dt = s + a x^2/(1 + x^2) - delta x
# x: surface C3b density (units of the half-saturation density), s: spontaneous tick-over deposition,
# a: maximal convertase-driven deposition, delta: removal of C3b by factor I with its cofactors
# (factor H, CR1, MCP), strong on host surfaces and weak on microbes.
# A: time courses for three regulation strengths and, for the intermediate one, two initial doses.
# B: steady states against delta (stable solid, unstable dashed), with the three surface types marked.
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P
S, A = 0.02, 3.0


def rhs(t, x, delta):
    return S + A * x ** 2 / (1 + x ** 2) - delta * x


def run(x0, delta, t_end=40):
    t = np.linspace(0, t_end, 600)
    return t, solve_ivp(rhs, (0, t_end), [x0], args=(delta,), t_eval=t, rtol=1e-9, atol=1e-12).y[0]


fig, ax = bio.canvas(16.0, 7.2)
bio.panel(ax, "A", (0.1, 7.05))
bio.label(ax, (4.6, 6.9), "C3b deposition over time", size="title", bold=True)
pa = quant.Plot(ax, (1.4, 1.2, 6.4, 4.9), xlim=(0, 40), ylim=(3e-3, 10), ylog=True, xlabel="time (arbitrary units)",
                ylabel="surface C3b density $x$", xticks=[0, 10, 20, 30, 40], yticks=[(1e-2, "$10^{-2}$"), (1e-1, "$10^{-1}$"), (1, "1"), (10, "10")], ylabel_offset=0.9)
for x0, d, tok, txt in ((0.011, 0.4, "negative", "weak regulation"), (0.011, 1.8, "positive", "strong regulation")):
    t, x = run(x0, d)
    pa.line(t, x, tok, lw=1.8, text=txt, at=0.85, dy=0.25, dx=-0.1, ha="right")
for x0, ls in ((0.6, False), (0.3, True)):
    t, x = run(x0, 1.0)
    pa.line(t, x, "enzyme", lw=1.6, dashed=ls)
bio.label(ax, (pa.X(24), pa.Y(0.2)), "intermediate regulation:\nthe initial dose decides", size="tiny",
          color=quant.line_color("enzyme"), ha="left")

bio.panel(ax, "B", (8.8, 7.05))
bio.label(ax, (12.7, 6.9), "Steady states against regulation", size="title", bold=True)
pb = quant.Plot(ax, (10.2, 1.2, 5.2, 4.9), xlim=(0, 2.6), ylim=(3e-3, 10), ylog=True, xlabel="removal rate $\\delta$ (factor I and cofactors)",
                ylabel="steady-state $x^*$", xticks=[0, 0.5, 1, 1.5, 2, 2.5], yticks=[(1e-2, "$10^{-2}$"), (1e-1, "$10^{-1}$"), (1, "1"), (10, "10")], ylabel_offset=0.9)
ds = np.linspace(0.02, 2.6, 900)
branches = {"low": [], "mid": [], "high": []}
for d in ds:
    roots = np.roots([-d, S + A, -d, S])
    real = np.sort(roots[np.abs(roots.imag) < 1e-9].real)
    real = real[real > 0]
    if len(real) == 3:
        branches["low"].append((d, real[0])); branches["mid"].append((d, real[1])); branches["high"].append((d, real[2]))
    elif len(real) == 1:
        (branches["low"] if real[0] < 1 else branches["high"]).append((d, real[0]))
for k, dashed in (("low", False), ("high", False), ("mid", True)):
    arr = np.array(branches[k])
    pb.line(arr[:, 0], arr[:, 1], "muted" if dashed else "ink", lw=1.8, dashed=dashed)
for d, name, tok in ((0.4, "microbe\n(no regulator)", "negative"), (1.0, "damaged\ncell", "enzyme"), (1.8, "healthy host\ncell", "positive")):
    pb.vline(d, token=tok, dashed=True)
    bio.label(ax, (pb.X(d), pb.Y(3.6e-3)), name, size="tiny", color=quant.line_color(tok), va="bottom")
