"""Progress curves and isozymes.

A: product against time for a Michaelis-Menten enzyme, from the integrated rate law
v_max t = [S]0 - [S] + K_M ln([S]0/[S]), solved with the Lambert W function:
[S](t) = K_M W(([S]0/K_M) exp(([S]0 - v_max t)/K_M)). Dashed lines are the tangents at t = 0,
whose slopes are the initial velocities v0 = v_max [S]0/(K_M + [S]0). The curves bend as substrate
is consumed, so v0 must be measured while only a few percent has reacted.
B: two isozymes with the same V_max but different K_M acting on the same substrate: a low-K_M form
(like mitochondrial acetaldehyde dehydrogenase, ALDH2, K_M about 0.2 uM) and a high-K_M form (like
cytosolic ALDH1A1, K_M taken as 50 uM; illustrative values). At low substrate concentrations only
the low-K_M form works near capacity."""

import numpy as np
from scipy.special import lambertw
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 8.0)

# --- A: progress curves -------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.9))
a = charts.axes_at(ax, (1.3, 1.0, 8.0, 6.0))
KM, VMAX = 1.0, 1.0  # concentrations in units of K_M, time in units of K_M / v_max
t = np.linspace(0, 12, 600)
for S0, tok in ((0.5, "channel"), (2.0, "enzyme"), (8.0, "protein")):
    S = KM * np.real(lambertw(S0 / KM * np.exp((S0 - VMAX * t) / KM)))
    a.plot(t, S0 - S, color=charts.line(tok), lw=2.0, label=f"[S]$_0$ = {S0:g} $K_\\mathrm{{M}}$")
    v0 = VMAX * S0 / (KM + S0)
    tt = np.linspace(0, min(12, 1.15 * S0 / v0), 50)
    a.plot(tt, v0 * tt, color=charts.line(tok), lw=0.9, ls="--")
a.set_xlim(0, 12)
a.set_ylim(0, 8.5)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
a.text(6.3, 1.0, "dashed: tangent at $t = 0$,\nslope $v_0$", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(a, r"$t$ / ($K_\mathrm{M}/v_{\max}$)", r"[P] / $K_\mathrm{M}$")
charts.title(a, "Integrated Michaelis–Menten progress curves")

# --- B: isozymes --------------------------------------------------------------------------
bio.panel(ax, "B", (10.6, 7.9))
b = charts.axes_at(ax, (11.8, 1.0, 7.8, 6.0))
S = np.logspace(-2, 4, 500)  # uM
for km, name, tok in ((0.2, "low $K_\\mathrm{M}$ (ALDH2-like), 0.2 µM", "enzyme"), (50.0, "high $K_\\mathrm{M}$ (ALDH1A1-like), 50 µM", "drug")):
    b.plot(S, S / (km + S), color=charts.line(tok), lw=2.0, label=name)
    b.plot([km, km], [0, 0.5], color=charts.line(tok), lw=0.8, ls=":")
b.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
b.axvline(1.0, color=P.muted(), lw=0.9, ls="--")
b.text(1.15, 0.2, "at 1 µM:\n83% vs 2%\nof $v_{\\max}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_xscale("log")
b.set_xlim(1e-2, 1e4)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "[acetaldehyde] / µM", r"$v_0/v_{\max}$")
charts.title(b, "Two isozymes, same reaction")
