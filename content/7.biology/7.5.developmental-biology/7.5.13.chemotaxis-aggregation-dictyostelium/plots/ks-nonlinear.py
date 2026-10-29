"""Nonlinear steady states of the Keller-Segel model.

A: near onset, the scaled amplitude equation a_t + r a_xx + a_xxxx + (a^2)_xx = 0 has periodic steady states of period
1 given by Jacobi elliptic functions, A = A0 (1 - m) sn^2(xi, m) / (1 - m sn^2(xi, m)), with
r = 48 K (E + m K / 3 - 2 K / 3) and A0 = 24 K^2 m (m = k^2 the elliptic parameter, K and E the complete elliptic
integrals). The branch leaves the linear threshold r = 4 pi^2 with zero amplitude and bends back to smaller r as
the amplitude grows: the bifurcation is subcritical. Inset: profiles for m = 0.5 and 0.99. B: solitary
aggregates of the special case f a - rho + nu rho_xx = 0, mu a_xx = kappa (a rho_x)_x with background rho1 = 1:
the peak attractant rho2 solves rho2^2 - (2 / lambda) exp(lambda (rho2 - 1)) = 1 - 2 / lambda (lambda = kappa / mu),
and the peak cell density a2 = exp(lambda (rho2 - 1)) / f (f = 1) grows without bound as lambda -> 0 while the
bump vanishes at lambda = 1. C: the boundary-layer aggregate at large lambda, a = lambda B sech^2(sqrt(B/2) xi),
B = 1 / (8 f^2 nu): cells are exponentially rare away from the aggregation point.
"""

import numpy as np
from scipy.optimize import brentq
from scipy.special import ellipe, ellipj, ellipk
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 9.6)

m = np.linspace(1e-4, 0.995, 400)
K, E = ellipk(m), ellipe(m)
r = 48 * K * (E + m * K / 3 - 2 * K / 3)
A0 = 24 * K**2 * m
pa = C.axes_at(ax, (1.6, 1.4, 7.6, 6.4))
pa.plot(r, A0, color=Q.line_color("protein"), lw=1.8, label="periodic steady states")
pa.plot([-20, 4 * np.pi**2], [0, 0], color=P.ink(), lw=1.6, label="uniform, stable")
pa.plot([4 * np.pi**2, 60], [0, 0], color=P.ink(), lw=1.6, ls=(0, (3, 2)), label="uniform, unstable")
pa.set_xlim(-20, 60)
pa.set_ylim(-10, 230)
pa.axvline(4 * np.pi**2, color=P.muted(), lw=0.7, ls=(0, (2, 2)))
pa.text(4 * np.pi**2 + 1, 200, "r = 4π²", color=P.muted(), fontsize=FS["tiny"])
C.style_axes(pa, "control parameter r (∝ Δ)", "amplitude A₀")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
ins = C.axes_at(ax, (2.0, 2.0, 3.2, 1.9))
for mm, tk in ((0.5, "na"), (0.99, "negative")):
    Kk = ellipk(mm)
    a0 = 24 * Kk**2 * mm
    x = np.linspace(0, 1, 300)
    sn = ellipj(x * np.sqrt(a0 / 6) / np.sqrt(mm), mm)[0]
    A = a0 * (1 - mm) * sn**2 / (1 - mm * sn**2)
    ins.plot(x, (A - A.mean()) / a0, color=Q.line_color(tk), lw=1.3)
C.style_axes(ins, None, None)
ins.set_xticks([])
ins.set_yticks([])
bio.panel(ax, "A", (0.3, 9.0))
bio.label(ax, (1.6, 9.0), "Subcritical bifurcation", size="small", bold=True, ha="left")

lam = np.linspace(0.04, 0.999, 300)
rho2 = []
for l in lam:
    F = lambda x: x * x - (2 / l) * np.exp(l * (x - 1)) - (1 - 2 / l)
    hi = 1.0 + 1e-9
    x = 2.0
    while F(x) > 0 and x < 1e4:
        x *= 1.5
    # largest root above 1 lies where F changes sign from + to -
    xs = np.linspace(1.0 + 1e-6, x, 4000)
    v = F(xs)
    idx = np.where(np.diff(np.sign(v)) != 0)[0]
    rho2.append(brentq(F, xs[idx[-1]], xs[idx[-1] + 1]) if len(idx) else np.nan)
rho2 = np.array(rho2)
a2 = np.exp(lam * (rho2 - 1))
pb = C.axes_at(ax, (11.8, 1.4, 7.4, 6.4))
pb.semilogy(lam, a2, color=Q.line_color("protein"), lw=1.8, label="peak cell density a₂")
ls_ = lam < 0.25
pb.semilogy(lam[ls_], np.log(lam[ls_]) ** 2 / (2 * lam[ls_]), color=P.muted(), lw=1.1, ls=(0, (4, 2)), label="leading order (ln λ)² / 2λ")
pb.set_xlim(0, 1)
C.style_axes(pb, "λ = κ / μ", "a₂ (log scale)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (10.5, 9.0))
bio.label(ax, (11.8, 9.0), "Solitary aggregate: collapse as λ → 0", size="small", bold=True, ha="left")

nu, f = 1.0, 1.0
B = 1 / (8 * f * f * nu)
xi = np.linspace(-12, 12, 400)
pc = C.axes_at(ax, (22.0, 1.4, 7.4, 6.4))
for l, tk in ((5.0, "na"), (20.0, "negative")):
    pc.plot(xi / np.sqrt(l), l * B * np.cosh(np.sqrt(B / 2) * xi) ** -2, color=Q.line_color(tk), lw=1.8, label=f"λ = {l:g}")
pc.set_xlim(-3, 3)
C.style_axes(pc, "x − L₀/2 (units of √ν)", "cell density a")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (20.7, 9.0))
bio.label(ax, (22.0, 9.0), "Boundary-layer aggregate (sech²)", size="small", bold=True, ha="left")
