"""Relay of cAMP pulses between amoebae (Cohen-Robertson model).

A pulse of strength s released by one amoeba diffuses in the plane; a neighbour at the mean distance R, with
1/a = pi R^2 / 4 for cell density a, sees rho(R, t) = (s a / 4) g(tau), g(tau) = exp(-1/tau) / tau, tau = 4 nu t / R^2.
A: g(tau) has its maximum 1/e at tau = 1; a neighbour fires when rho reaches the threshold rho_c, that is when
g = (a_c / a) / e with a_c = 4 e rho_c / s, so waves propagate only above the critical density a_c and the trigger
time (dots, for a / a_c = 1.2, 2 and 5) shortens with density. B: wave speed v = R / (T_p + T_d), T_p = R^2 tau_p
/ (4 nu), against density, for nu = 400 um^2/s (cAMP), a relay delay T_d = 15 s and a_c = 300 cells/mm^2; the
speed is dominated by the relay delay, v ~ R / T_d, and therefore falls with density as a^(-1/2): denser
cells are closer together, and each relay step costs the same delay. Dashed:
R / T_d.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(24.0, 9.2)
tau = np.linspace(0.05, 6, 500)
g = np.exp(-1 / tau) / tau
pa = C.axes_at(ax, (1.8, 1.4, 8.8, 6.4))
pa.plot(tau, g, color=Q.line_color("protein"), lw=1.8)
for ratio, tk in ((1.2, "negative"), (2.0, "na"), (5.0, "highlight")):
    lev = 1 / (np.e * ratio)
    tp = brentq(lambda x: np.exp(-1 / x) / x - lev, 0.05, 1.0)
    pa.axhline(lev, color=Q.line_color(tk), lw=0.9, ls=(0, (3, 2)))
    pa.plot([tp], [lev], "o", color=Q.line_color(tk), ms=5)
    pa.text(4.2, lev + 0.008, f"a/a_c = {ratio:g}", color=Q.line_color(tk), fontsize=FS["tiny"])
pa.axhline(1 / np.e, color=P.muted(), lw=0.8)
pa.text(3.0, 1 / np.e + 0.01, "maximum 1/e", color=P.muted(), fontsize=FS["tiny"])
pa.set_xlim(0, 6)
pa.set_ylim(0, 0.42)
C.style_axes(pa, "τ = 4νt / R²", "g(τ) = 4ρ / (s a)")
bio.panel(ax, "A", (0.3, 8.6))
bio.label(ax, (1.8, 8.6), "Signal seen by the nearest neighbour", size="small", bold=True, ha="left")

nu, Td, ac = 400.0, 15.0, 300e-6  # um^2/s, s, cells/um^2
a = np.linspace(1.02 * ac, 10 * ac, 300)
R = np.sqrt(4 / (np.pi * a))
tp = np.array([brentq(lambda x: np.exp(-1 / x) / x - (ac / ai) / np.e, 0.01, 1.0) for ai in a])
v = R / (R**2 * tp / (4 * nu) + Td) * 60
pb = C.axes_at(ax, (14.2, 1.4, 8.8, 6.4))
pb.plot(a * 1e6, v, color=Q.line_color("protein"), lw=1.8, label="v = R / (T_p + T_d)")
pb.plot(a * 1e6, R / Td * 60, color=P.muted(), lw=1.1, ls=(0, (4, 2)), label="R / T_d")
pb.axvline(ac * 1e6, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pb.text(ac * 1e6 * 1.05, 20, "a_c", color=P.edge("highlight"), fontsize=FS["tiny"])
pb.set_ylim(0, None)
C.style_axes(pb, "cell density a / (cells per mm²)", "wave speed / (µm per min)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (12.7, 8.6))
bio.label(ax, (14.2, 8.6), "Speed of the relayed wave", size="small", bold=True, ha="left")
