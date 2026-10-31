"""A charged membrane in salt water (Gouy-Chapman). The membrane carries sigma = -0.31 e/nm^2
(20 % anionic lipids at 0.65 nm^2 per lipid) in a 1:1 salt at 25 C. A: potential against distance
from the surface at 150 mM (Debye length 0.78 nm) and 15 mM (2.5 nm): nonlinear Poisson-Boltzmann
solution (line; dots: numerical solution of the boundary-value problem) and the linearized
Debye-Hueckel solution (dashed), which overestimates the surface potential. B: concentrations of
Na+ and Cl- at 150 mM: counterions accumulate about sevenfold at the surface and coions are
depleted, within about one Debye length. C: surface potential (left axis) and the corresponding
lowering of the local pH at the surface (right axis) against salt concentration for 5, 20 and
100 % anionic lipids (Grahame equation)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import wikibio as bio
from wikibio import charts

P = bio.P
lB = 0.715  # nm
kTe = 25.69  # mV
A_lip = 0.65


def lam(c):
    return 0.304 / np.sqrt(c)


def y0_of(sig, c):
    """Dimensionless surface potential (negative for negative sigma) from the Grahame equation."""
    return 2 * np.arcsinh(2 * np.pi * lB * sig * lam(c))


def y_gc(x, sig, c):
    y0 = y0_of(sig, c)
    return 4 * np.arctanh(np.tanh(y0 / 4) * np.exp(-x / lam(c)))


sig = -0.2 / A_lip
fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.5, left=0.07, right=0.93, bottom=0.17, top=0.88)

ax = axs[0]
x = np.linspace(0, 6, 400)
for c, tok in ((0.15, "blood"), (0.015, "dna")):
    ax.plot(x, y_gc(x, sig, c) * kTe, color=charts.line(tok), lw=1.8, label=f"{c * 1000:.0f} mM, PB")
    ydh = 4 * np.pi * lB * sig * lam(c) * np.exp(-x / lam(c))
    ax.plot(x, ydh * kTe, color=charts.line(tok), lw=1.0, ls="--", label=f"{c * 1000:.0f} mM, linearized")
    k2 = 1 / lam(c) ** 2
    xs = np.linspace(0, 12 * lam(c), 200)
    sol = solve_bvp(lambda xx, Y: np.vstack([Y[1], k2 * np.sinh(Y[0])]),
                    lambda ya, yb: np.array([ya[1] + 4 * np.pi * lB * sig, yb[0]]),
                    xs, np.vstack([y_gc(xs, sig, c), np.gradient(y_gc(xs, sig, c), xs)]), tol=1e-6)
    xd = np.linspace(0, 6, 13)
    ax.plot(xd, sol.sol(xd)[0] * kTe, "o", color=charts.line(tok), ms=3)
ax.set_ylim(-180, 3)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "distance from membrane / nm", r"$\varphi$ / mV")
charts.title(ax, r"A  Potential, $\sigma = -0.31\,e\,\mathrm{nm^{-2}}$")

ax = axs[1]
c = 0.15
y = y_gc(x, sig, c)
ax.plot(x, c * np.exp(-y) * 1000, color=charts.line("na"), lw=1.8, label=r"$\mathrm{Na^+}$")
ax.plot(x, c * np.exp(y) * 1000, color=charts.line("cl"), lw=1.8, label=r"$\mathrm{Cl^-}$")
ax.axhline(150, color=P.muted(), lw=0.6, ls=":")
ax.axvline(lam(c), color=P.muted(), lw=0.5, ls=":")
ax.text(lam(c) + 0.08, 800, r"$\lambda_\mathrm{D}$", fontsize=bio.core.FONT["small"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "distance from membrane / nm", "concentration / mM")
charts.title(ax, "B  Ions at 150 mM")

ax = axs[2]
cs = np.logspace(-3, 0, 200)
for frac, tok in ((0.05, "neutral"), (0.2, "blood"), (1.0, "protein")):
    s_ = -frac / A_lip
    ax.plot(cs * 1000, y0_of(s_, cs) * kTe, color=charts.line(tok), lw=1.8, label=f"{frac * 100:.0f} % anionic")
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "salt / mM", r"surface potential $\varphi_0$ / mV")
ax2 = ax.twinx()
lo, hi = ax.get_ylim()
ax2.set_ylim(lo / (kTe * np.log(10)), hi / (kTe * np.log(10)))
charts.style_axes(ax2, None, r"$\mathrm{pH_{surface}} - \mathrm{pH_{bulk}}$", box=True)
ax2.spines["left"].set_visible(False)
charts.title(ax, "C  Grahame equation")
