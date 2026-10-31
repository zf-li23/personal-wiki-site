# Where the load acts determines the shape of a motor's force-velocity curve. A tightly coupled two-step cycle
# (Theorem 27.3.2 of 7.6.27): a load-independent chemical step (rate k_c) and a mechanical step of size d whose
# forward rate is k_m exp(-F d / kBT); stall at F_s = dmu/d with dmu = 20 kBT. Curves are normalized as v/Vmax
# against F/F_half (F_half: the force that halves the speed), as in single-molecule comparisons of motors.
# k_m/k_c = 1000: the mechanical step is fast and in rapid equilibrium; the speed is set by chemistry until the load
# makes the mechanical step rate-limiting, then it drops abruptly (RNA polymerase-like).
# k_m/k_c = 0.01: the loaded step is rate-limiting at all forces; the speed falls exponentially from zero load
# (gradual, phi29-like). k_m/k_c = 1: intermediate (kinesin-like).
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
kT, dmu = 1.0, 20.0


def v(F, r):
    kc, km = 1.0, r
    u0, w1 = kc, kc * np.exp(-dmu / 2)
    u1 = km * np.exp(-F)  # load on the forward mechanical rate (F in units of kBT/d)
    w0 = km * np.exp(-dmu / 2)  # chosen so that u0 u1 / (w0 w1) = exp(dmu - F)
    return (u0 * u1 - w0 * w1) / (u0 + u1 + w0 + w1)


fig, ax = plt.subplots(figsize=(5.6, 4.0))
for r, tok, lab in ((1000.0, "rna", "fast loaded step ($k_m/k_c$ = 1000)"), (1.0, "enzyme", "comparable ($k_m/k_c$ = 1)"),
                    (0.01, "virus", "slow loaded step ($k_m/k_c$ = 0.01)")):
    v0 = v(0.0, r)
    Fh = brentq(lambda F: v(F, r) - v0 / 2, 0, dmu)
    F = np.linspace(0, 2.2 * Fh, 300)
    ax.plot(F / Fh, v(F, r) / v0, color=charts.line(tok), lw=2.0, label=lab)
ax.set_xlim(0, 2.2); ax.set_ylim(0, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "load $F/F_{1/2}$", "velocity $v/V_\\max$")
charts.title(ax, "Three shapes from one model")
fig.tight_layout()
