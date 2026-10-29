"""The Maxwell viscoelastic liquid: a spring and a dashpot in series.

Constitutive law: d(tau)/dt + tau / t_r = G d(eps)/dt, with shear modulus G, viscosity eta and
relaxation time t_r = eta / G. Time in units of t_r, stress in units of G times the imposed strain
(or the imposed stress), strain in units of tau0 / G.
A: the mechanical analogue. B: stress relaxation after a step strain eps0: tau = G eps0 exp(-t/t_r).
C: creep under a step stress tau0: eps = tau0/G + tau0 t / eta (instant elastic jump, then flow).
D: start-up at constant shear rate: tau = eta (d eps/dt) (1 - exp(-t/t_r)), elastic at t << t_r
(tau ~ G eps), Newtonian viscous at t >> t_r.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(34.0, 9.0)
bio.panel(ax, "A", (0.1, 8.9))
y = 4.6
# wall
ax.plot([0.8, 0.8], [3.4, 5.8], color=P.ink(), lw=2.0)
for k in range(6):
    ax.plot([0.8, 0.45], [3.5 + 0.45 * k, 3.15 + 0.45 * k], color=P.ink(), lw=0.8)
# spring
xs = np.linspace(0.8, 3.6, 200)
zig = np.where((xs > 1.2) & (xs < 3.2), 0.35 * np.sign(np.sin((xs - 1.2) / 2.0 * 6 * 2 * np.pi)), 0)
ax.plot(xs, y + zig * (np.abs(np.sin((xs - 1.2) / 2.0 * 6 * 2 * np.pi)) ** 0.2), color=P.edge("ectoderm"), lw=1.6)
bio.label(ax, (2.2, y + 0.9), "spring G", size="small")
# dashpot
ax.plot([3.6, 4.4], [y, y], color=P.ink(), lw=1.4)
ax.plot([4.4, 6.4, 6.4, 4.4], [y + 0.55, y + 0.55, y - 0.55, y - 0.55], color=P.edge("mesoderm"), lw=1.6)
ax.plot([5.2, 5.2], [y - 0.42, y + 0.42], color=P.edge("mesoderm"), lw=2.2)
ax.plot([5.2, 7.4], [y, y], color=P.ink(), lw=1.4)
bio.label(ax, (5.4, y + 0.95), "dashpot η", size="small")
bio.arrow(ax, (7.4, y), (8.6, y), kind="process")
bio.label(ax, (8.0, y - 0.55), "τ", size="normal", italic=True)
bio.label(ax, (4.5, 2.2), "t_r = η / G", size="small")

t = np.linspace(0, 5, 300)
for letter, x0, title, ylab, curves in (
        ("B", 10.6, "Stress relaxation (step strain)", "τ / (G ε0)", [(np.exp(-t), "ectoderm")]),
        ("C", 18.4, "Creep (step stress)", "ε / (τ0 / G)", [(1 + t, "mesoderm")]),
        ("D", 26.2, "Start-up at constant rate", "τ / (η dε/dt)", [(1 - np.exp(-t), "positive"), (t, "neutral")])):
    bio.panel(ax, letter, (x0 - 1.0, 8.9))
    pp = charts.axes_at(ax, (x0 + 0.8, 1.6, 6.2, 6.0))
    for k, (yy, tok) in enumerate(curves):
        pp.plot(t, yy, color=quant.line_color(tok), lw=2.0 if k == 0 else 1.0, ls="-" if k == 0 else (0, (3, 2)))
    pp.set_xlim(0, 5)
    pp.set_ylim(0, 1.2 if letter != "C" else 6.2)
    charts.style_axes(pp, "t / t_r", ylab)
    charts.title(pp, title)
    if letter == "D":
        pp.text(0.5, 0.25, "elastic: τ ≈ Gε", fontsize=bio.core.FONT["tiny"], color=P.muted())
        pp.text(2.6, 1.03, "viscous: τ ≈ η dε/dt", fontsize=bio.core.FONT["tiny"], color=P.muted())
    if letter == "C":
        pp.text(0.2, 1.4, "elastic jump", fontsize=bio.core.FONT["tiny"], color=P.muted())
        pp.plot([0, 0], [0, 1], color=quant.line_color("mesoderm"), lw=2.0)
        pp.text(2.4, 2.6, "viscous flow, rate τ0/η", fontsize=bio.core.FONT["tiny"], color=P.muted())
