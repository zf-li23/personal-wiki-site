# A compressible gas gill (physical gill), after the model of Rahn & Paganelli (1968). A diving insect
# carries a bubble of air; it consumes O2 from it at rate q. As the bubble's O2 partial pressure falls below
# that of the air-saturated water (21 kPa), O2 diffuses in; meanwhile N2, whose partial pressure in the
# bubble rises above that of the water (80 kPa) as O2 is used and with hydrostatic pressure, diffuses out,
# and the bubble shrinks until it must be renewed at the surface. Fluxes: J_i = G_i A (P_water,i - p_i),
# with bubble area A proportional to volume^(2/3) and the O2:N2 permeation ratio G_O2/G_N2 = 2.1 (diffusion
# coefficient times solubility in water). Units are relative: amounts as fractions of the initial bubble,
# q in units of the initial N2 conductance. A: time course at the surface (q = 0.02). B: gain factor
# (total O2 consumed / O2 initially in the bubble) against consumption rate at three depths; the
# theoretical ceiling at the surface is about 1 + 2.1 x 0.79 / 0.21, i.e. about 9.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
RATIO = 2.1


def run(depth, q, dt=0.01, tmax=4000):
    Pt = 101.3 + 9.81 * depth
    nO, nN, used, t = 0.21, 0.79, 0.0, 0.0
    tr = [(0.0, nO, nN)]
    while nO + nN > 0.02 and t < tmax:
        V = (nO + nN) * 101.3 / Pt
        A = V ** (2 / 3)
        pO, pN = nO / (nO + nN) * Pt, nN / (nO + nN) * Pt
        dO = RATIO * A * (21.2 - pO) * 0.01 - q
        dN = A * (80.1 - pN) * 0.01
        if nO + dO * dt <= 0:
            break
        nO += dO * dt
        nN += dN * dt
        used += q * dt
        t += dt
        if len(tr) < 4000 and int(t / dt) % 20 == 0:
            tr.append((t, nO, nN))
    return used / 0.21, np.array(tr)


fig, ax = bio.canvas(24, 10)
bio.panel(ax, "A", (0.2, 9.7))
bio.panel(ax, "B", (12.4, 9.7))
a = charts.axes_at(ax, (2.0, 1.6, 8.8, 7.4))
b = charts.axes_at(ax, (14.4, 1.6, 8.8, 7.4))
gain, tr = run(0.0, 0.02)
a.plot(tr[:, 0], tr[:, 1], color=charts.line("negative"), lw=1.6, label="O2")
a.plot(tr[:, 0], tr[:, 2], color=charts.line("channel"), lw=1.6, label="N2")
a.plot(tr[:, 0], 0.02 * tr[:, 0] / 0.21, color=charts.line("enzyme"), lw=1.2, ls=(0, (4, 3)))
a.text(tr[-1, 0] * 0.55, 0.02 * tr[-1, 0] * 0.55 / 0.21 + 0.3, "cumulative O2 used\n/ initial O2", fontsize=7, color=charts.line("enzyme"))
a.text(tr[5, 0], tr[5, 2] + 0.06, "N2 in bubble", fontsize=7, color=charts.line("channel"))
a.text(tr[5, 0], tr[5, 1] + 0.1, "O2 in bubble", fontsize=7, color=charts.line("negative"))
a.set_ylim(0, max(1.0, gain) * 1.05)
charts.style_axes(a, "Time (relative units)", "Amount (fraction of initial bubble)")
qs = np.logspace(-3, -0.7, 12)
for d, tok in ((0.0, "negative"), (0.1, "enzyme"), (0.3, "channel")):
    g = [run(d, q)[0] for q in qs]
    b.plot(qs, g, color=charts.line(tok), lw=1.6, marker="o", ms=3)
    b.text(qs[-1] * 1.05, g[-1], "%g m" % d, fontsize=7, color=charts.line(tok), va="center")
b.axhline(1 + RATIO * 0.79 / 0.21, color=P.muted(), lw=0.9, ls=(0, (4, 3)))
b.axhline(1, color=P.muted(), lw=0.6)
b.set_xscale("log")
charts.style_axes(b, "O2 consumption rate q (relative)", "Gain factor")
