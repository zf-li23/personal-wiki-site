"""Calcium feedback extends the operating range of a rod (minimal cGMP model).

Dimensionless variables (dark values = 1): cGMP G, free Ca2+ c, circulating current J = G^3
(the CNG channel opens cooperatively, Hill coefficient about 3, far below saturation).
  dG/dt = alpha(c) - beta(I) G,   beta(I) = beta_d (1 + I/I0)      (light activates PDE6)
  dc/dt = (J - c) / tau_c                                           (Ca2+ influx through the CNG channel)
  alpha(c) = alpha_max / (1 + (c/K)^m)                              (GCAPs: low Ca2+ stimulates cyclase)
With feedback: K = 0.12, m = 2, alpha_max chosen so that alpha(1) = beta_d.
Without feedback: alpha = beta_d (constant). beta_d = 1 s^-1, tau_c = 0.05 s; I in units of I0.
Response R = 1 - J (fraction of the dark current suppressed).
A: steady response versus log background. B: responses to 3 s light steps.
C: incremental sensitivity dR/dI at each background (log-log); slope -1 is Weber's law.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio

P = bio.P
bd, tau_c, K, m = 1.0, 0.05, 0.12, 2
amax = bd * (1 + (1 / K) ** m)


def alpha(c, fb):
    return amax / (1 + (c / K) ** m) if fb else bd


def steady(I, fb):
    f = lambda G: alpha(G**3, fb) - bd * (1 + I) * G
    G = brentq(f, 1e-9, 1.0 + 1e-9)
    return 1 - G**3


Ib = np.logspace(-2, 4, 400)
R_fb = np.array([steady(i, True) for i in Ib])
R_no = np.array([steady(i, False) for i in Ib])

c_fb, c_no = P.edge("rna"), P.edge("dna")
fig, axs = plt.subplots(1, 3, figsize=(13, 4.0))

ax = axs[0]
def span(R):
    i10, i90 = Ib[np.argmin(abs(R - 0.1))], Ib[np.argmin(abs(R - 0.9))]
    return np.log10(i90 / i10)


ax.plot(Ib, R_no, color=c_no, lw=2,
        label=f"no Ca$^{{2+}}$ feedback (10-90 %: {span(R_no):.1f} log units)")
ax.plot(Ib, R_fb, color=c_fb, lw=2,
        label=f"with Ca$^{{2+}}$ feedback (10-90 %: {span(R_fb):.1f} log units)")
ax.set_xscale("log")
ax.set_xlabel(r"Background intensity $I/I_0$")
ax.set_ylabel("Steady response R")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Steady-state compression", loc="left", fontsize=10)

dt = 1e-3
t = np.arange(-0.5, 5.0, dt)
bx = axs[1]
for I, ls in ((0.3, "-"), (3, "-"), (30, "-")):
    for fb, c in ((False, c_no), (True, c_fb)):
        G, cc = 1.0, 1.0
        out = np.empty_like(t)
        for k, tk in enumerate(t):
            Ik = I if 0 <= tk < 3 else 0.0
            dG = alpha(cc, fb) - bd * (1 + Ik) * G
            dc = (G**3 - cc) / tau_c
            G += dt * dG
            cc += dt * dc
            out[k] = 1 - G**3
        bx.plot(t, out, color=c, lw=1.6, ls="--" if not fb else "-")
    bx.text(1.5, out[int((1.5 + 0.5) / dt)] + 0.025, f"I = {I}", fontsize=7.5, color=P.muted(),
            va="bottom", ha="center")
bx.axvspan(0, 3, color=P.fill("highlight"), alpha=0.25, lw=0)
bx.set_xlabel("Time / s")
bx.set_ylabel("Response")
bx.set_ylim(0, 1.05)
bx.set_title("B  Light steps: sag and faster recovery", loc="left", fontsize=10)
bx.plot([], [], color=c_no, ls="--", label="no feedback")
bx.plot([], [], color=c_fb, label="with feedback")
bx.legend(frameon=False, fontsize=8, loc="upper right")

cx = axs[2]
for R, c, lab in ((R_no, c_no, "no feedback"), (R_fb, c_fb, "with feedback")):
    S = np.gradient(R, Ib)
    cx.plot(Ib, S / S[0], color=c, lw=2, label=lab)
ref = Ib ** -1.0
cx.plot(Ib, 0.3 * ref / ref[np.argmin(abs(Ib - 1))] * 1, color=P.muted(), lw=1, ls=":",
        label="slope -1 (Weber)")
cx.set_xscale("log")
cx.set_yscale("log")
cx.set_ylim(1e-9, 3)
cx.set_xlabel(r"Background intensity $I/I_0$")
cx.set_ylabel("Incremental sensitivity (relative to dark)")
cx.legend(frameon=False, fontsize=8, loc="lower left")
cx.set_title("C  Sensitivity follows Weber's law", loc="left", fontsize=10)
fig.tight_layout()
