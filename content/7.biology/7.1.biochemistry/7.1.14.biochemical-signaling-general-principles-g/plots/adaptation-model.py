"""A minimal model of receptor desensitization and cAMP signaling.

Occupancy theta = L/(L + Kd) (binding at equilibrium); a fraction d of the receptors is desensitized
(phosphorylated by GRK and bound to arrestin) at a rate proportional to occupancy and recovers at a
constant rate: dd/dt = kdes theta (1 - d) - krec d. Signaling receptors a = theta (1 - d) drive cAMP
synthesis, and phosphodiesterase removes it: dc/dt = kAC a - kPDE c.
Parameters (per minute): kdes = 0.3, krec = 0.05, kAC = kPDE = 2 (c is in units of the maximal level).
A: agonist at 10 Kd for 30 min, washout for 15 min, then a second identical stimulus. The response
peaks and then adapts to about a fifth of the peak although the agonist is still present; after a short
washout the second response is smaller, because resensitization (time constant 1/krec = 20 min) is
incomplete.
B: the first stimulus with phosphodiesterase partly inhibited (kPDE = 0.5 per minute, as with caffeine
or IBMX): cAMP rises to a much higher peak and plateau and decays more slowly after washout.
"""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
kdes, krec, kac = 0.3, 0.05, 2.0


def ligand(t, pulses):
    return 10.0 if any(a <= t < b for a, b in pulses) else 0.0


def run(pulses, kpde, tmax):
    def f(t, y):
        d, c = y
        th = ligand(t, pulses) / (ligand(t, pulses) + 1.0)
        return [kdes * th * (1 - d) - krec * d, kac * th * (1 - d) - kpde * c]

    t = np.linspace(0, tmax, 3000)
    s = solve_ivp(f, (0, tmax), [0.0, 0.0], t_eval=t, max_step=0.05)
    th = np.array([ligand(x, pulses) / (ligand(x, pulses) + 1.0) for x in t])
    return t, th, s.y[0], s.y[1]


fig, ax = bio.canvas(20.0, 7.8)
bio.panel(ax, "A", (0.1, 7.7))
pa = charts.axes_at(ax, (1.6, 1.4, 8.0, 5.6))
pulses = [(5, 35), (50, 80)]
t, th, d, c = run(pulses, 2.0, 110)
for a, b in pulses:
    pa.axvspan(a, b, color=P.fill("drug"), alpha=0.25, lw=0)
pa.plot(t, th, color=P.muted(), lw=1.2, ls=(0, (4, 2.4)), label="receptor occupancy θ")
pa.plot(t, d, color=charts.line("negative"), lw=1.6, label="desensitized fraction d")
pa.plot(t, c, color=charts.line("highlight"), lw=2.0, label="cAMP (relative)")
pa.text(20, 0.96, "agonist", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.text(65, 0.96, "agonist again", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
pa.set_xlim(0, 110)
pa.set_ylim(0, 1.45)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=2)
charts.style_axes(pa, "time / min", "fraction")
charts.title(pa, "Adaptation and incomplete resensitization")

bio.panel(ax, "B", (10.9, 7.7))
pb = charts.axes_at(ax, (12.4, 1.4, 7.0, 5.6))
for kpde, tok, name in ((2.0, "highlight", "PDE active ($k_\\mathrm{PDE}$ = 2 min⁻¹)"), (0.5, "drug", "PDE inhibited ($k_\\mathrm{PDE}$ = 0.5 min⁻¹)")):
    t, th, d, c = run([(5, 35)], kpde, 60)
    pb.plot(t, c, color=charts.line(tok), lw=2.0, label=name)
pb.axvspan(5, 35, color=P.fill("drug"), alpha=0.25, lw=0)
pb.set_xlim(0, 60)
pb.set_ylim(0, 2.3)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "time / min", "cAMP (relative)")
charts.title(pb, "Phosphodiesterase sets speed and level")
