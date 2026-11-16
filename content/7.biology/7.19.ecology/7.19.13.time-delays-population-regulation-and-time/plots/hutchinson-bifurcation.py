"""Linear stability and the Hopf bifurcation of the delayed logistic equation.

A: roots z = lambda T of the characteristic equation z e^z = -rT, computed with the branches W_k of the
Lambert W function (z = W_k(-rT), k = -3..3), for five values of rT. The roots move to the right as rT
grows; at rT = 1/e the two real roots merge into a complex pair, and at rT = pi/2 the pair z = +-i pi/2
crosses the imaginary axis. B: long-run maximum and minimum of N/K from simulations (Euler, step 0.002,
after a transient of 300/r): a single equilibrium below pi/2, a limit cycle whose amplitude grows quickly
above it. C: period in units of T: 2 pi / Im z of the dominant root (damped oscillations, line) and the
measured period of the limit cycle (points); it equals 4T at the bifurcation.
"""

import numpy as np
from scipy.special import lambertw

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

# --- A: roots -----------------------------------------------------------------------------------
pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
vals = [(0.2, "enzyme"), (np.exp(-1), "dna"), (1.0, "protein"), (np.pi / 2, "atp"), (2.2, "negative")]
for a, tok in vals:
    z = np.array([lambertw(-a, k) for k in range(-3, 4)])
    pa.plot(z.real, z.imag, "o", ms=3.2, color=Q.line_color(tok),
            label=f"rT = {a:.2f}")
pa.axvline(0, color=P.muted(), lw=0.8)
pa.axhline(0, color=P.muted(), lw=0.5)
pa.set_xlim(-4.2, 1.0)
pa.set_ylim(-17, 17)
C.style_axes(pa, "Re z", "Im z")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Roots of z exp(z) = -rT", size="small", bold=True, ha="left")


def run(a, dt=0.002, t_end=360.0, burn=300.0):
    lag = int(round(a / dt))
    n = int(t_end / dt)
    N = np.empty(n + lag + 1)
    N[: lag + 1] = 0.5
    for k in range(lag, lag + n):
        N[k + 1] = N[k] + dt * N[k] * (1.0 - N[k - lag])
    keep = N[lag + int(burn / dt):]
    return keep


A = np.linspace(0.05, 2.4, 48)
mx, mn, per = [], [], []
for a in A:
    x = run(a)
    mx.append(x.max())
    mn.append(x.min())
    if a > np.pi / 2 + 0.02:
        pk = np.where((x[1:-1] > x[:-2]) & (x[1:-1] > x[2:]))[0] + 1
        per.append(np.diff(pk).mean() * 0.002 / a if len(pk) > 2 else np.nan)
    else:
        per.append(np.nan)
mx, mn, per = map(np.array, (mx, mn, per))

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
pb.plot(A, mx, color=Q.line_color("negative"), lw=1.6, label="max N/K")
pb.plot(A, mn, color=Q.line_color("dna"), lw=1.6, label="min N/K")
for xv, txt in [(np.exp(-1), "1/e"), (np.pi / 2, "pi/2")]:
    pb.axvline(xv, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
    pb.text(xv + 0.03, 3.9, txt, fontsize=FS["tiny"], color=P.muted())
pb.set_ylim(0, 4.2)
C.style_axes(pb, "rT", "long-run extremes of N / K")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center left", bbox_to_anchor=(0.0, 0.62))
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Hopf bifurcation at rT = pi/2", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.0, 1.6, 7.0, 6.8))
ad = np.linspace(np.exp(-1) + 1e-3, np.pi / 2, 200)
zd = np.array([lambertw(-a, 0) for a in ad])
pc.plot(ad, 2 * np.pi / np.abs(zd.imag), color=Q.line_color("protein"), lw=1.6, label="damped: 2 pi / Im z")
pc.plot(A, per, "o", ms=3.0, color=Q.line_color("negative"), label="limit cycle (simulated)")
pc.axhline(4, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(0.5, 4.2, "4T", fontsize=FS["tiny"], color=P.muted())
pc.axvline(np.pi / 2, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.set_xlim(0, 2.45)
pc.set_ylim(0, 16)
C.style_axes(pc, "rT", "period / T")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.55))
bio.panel(ax, "C", (20.5, 9.6))
bio.label(ax, (22.0, 9.2), "Period of the oscillation", size="small", bold=True, ha="left")
