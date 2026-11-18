"""Why the oxygen of Biosphere 2 declined: a two-box model of a closed atmosphere.

Atmosphere of about 8.3e6 mol of air (2e5 m^3), initially 20.9 % O2 and 400 ppm CO2, followed for two
years from late September. Fluxes in mol per day: community respiration R0 = 5000 mol O2 consumed
(and CO2 released), dominated by decomposition of the organic-rich soils; gross photosynthesis
Pmax L(t) C/(K + C), with Pmax = 15000, K = 3e4 mol (about 3600 ppm) and seasonal light
L(t) = 0.7 + 0.3 cos(2 pi (t - 270)/365), maximal in late June; uptake of CO2 by carbonation of the
exposed concrete, kc C with kc = 0.04 per day. Then
    dO2/dt = photosynthesis - R0,    dC/dt = R0 - photosynthesis - kc C,
so that d(O2 + C)/dt = -kc C: the oxygen lost is the carbon locked in the concrete.
A: O2 with the concrete sink (solid) and without it (dashed); the cross marks the observed value,
14.5 % after 16 months (Severinghaus et al. 1994). B: CO2 in the two cases. Parameters are illustrative,
chosen to reproduce the observed magnitudes, not fitted to the full records.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

nair, R0, Pmax, K = 8.3e6, 5000.0, 15000.0, 3e4


def L(t):
    return 0.7 + 0.3 * np.cos(2 * np.pi * (t - 270) / 365)


def run(kc):
    def f(t, y):
        ph = Pmax * L(t) * y[1] / (K + y[1])
        return [ph - R0, R0 - ph - kc * y[1]]

    return solve_ivp(f, (0, 730), [0.209 * nair, 0.0004 * nair], t_eval=np.linspace(0, 730, 731), rtol=1e-8)


s1, s0 = run(0.04), run(0.0)
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
pa.plot(s1.t / 30.4, s1.y[0] / nair * 100, color=Q.line_color("dna"), lw=1.9, label="with CO2 uptake by concrete")
pa.plot(s0.t / 30.4, s0.y[0] / nair * 100, color=Q.line_color("plant"), lw=1.5, ls="--", label="without concrete sink")
pa.plot([16], [14.5], "x", ms=8, mew=2, color=Q.line_color("negative"), label="observed (16 months)")
pa.set_xlim(0, 24)
pa.set_ylim(10, 22)
C.style_axes(pa, "months after closure (from late September)", "oxygen / %")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Oxygen in a closed atmosphere", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
pb.plot(s1.t / 30.4, s1.y[1] / nair * 1e6, color=Q.line_color("dna"), lw=1.9, label="with concrete sink")
pb.plot(s0.t / 30.4, s0.y[1] / nair * 1e6, color=Q.line_color("plant"), lw=1.5, ls="--", label="without concrete sink")
pb.set_xlim(0, 24)
pb.set_ylim(0, 12000)
C.style_axes(pb, "months after closure", "carbon dioxide / ppm")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Carbon dioxide: winter peaks, summer drawdown", size="small", bold=True, ha="left")
