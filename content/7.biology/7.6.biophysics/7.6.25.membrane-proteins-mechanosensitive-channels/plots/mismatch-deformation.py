"""Hydrophobic mismatch: the bilayer deformation around a membrane protein and its energy.

Thickness-deformation model (Formula 25.2.1): G = int [Kb/2 (u'')^2 + Kt/(2 w0^2) u^2], with
Kb = 20 kBT, Kt = 60 kBT/nm^2 and w0 = 1.75 nm, so that 1/lambda = (Kb w0^2/Kt)^(1/4) = 1.0 nm.
A: leaflets around a protein whose hydrophobic half-width exceeds that of the bilayer by U = 0.4 nm
(positive mismatch) or falls short by U = -0.4 nm (negative mismatch); 1D solution of Theorem 25.2.1.
B: the profile u(x)/U in one dimension (line) and around a cylinder of radius R = 2.5 nm in two
dimensions (Kelvin-function solution, dashed), both with u(R) = U, u'(R) = 0.
C: deformation energy per unit length of boundary in two dimensions relative to the one-dimensional
line tension f = Kt U^2/(sqrt(2) lambda w0^2), as a function of lambda R."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import kv
from scipy.integrate import quad
import wikibio as bio
from wikibio import charts

P = bio.P
KB, KT, W0 = 20.0, 60.0, 1.75
LAM = (KT / (KB * W0 ** 2)) ** 0.25
S2 = np.sqrt(2.0) / 2.0


def u1d(x, U):
    """1D profile for x >= 0 measured from the protein wall (Theorem 25.2.1)."""
    y = LAM * x
    return U * np.exp(-S2 * y) * (np.cos(S2 * y) + np.sin(S2 * y))


MU = LAM * np.exp(1j * np.pi / 4)  # (nabla^2 - MU^2) K0(MU r) = 0, MU^2 = i lambda^2


def coeffs(R, U):
    """Complex C with u(r) = Re[C K0(MU r)], u(R) = U, u'(R) = 0."""
    k0, k1 = kv(0, MU * R), kv(1, MU * R)
    # Re[C k0] = U, Re[-C MU k1] = 0 ; write C = a + i b
    A = np.array([[k0.real, -k0.imag], [(-MU * k1).real, -(-MU * k1).imag]])
    a, b = np.linalg.solve(A, [U, 0.0])
    return a + 1j * b


def u2d(r, R, U):
    return (coeffs(R, U) * kv(0, MU * r)).real


def energy2d(R, U=1.0):
    C = coeffs(R, U)

    def dens(r):
        k0 = kv(0, MU * r)
        u = (C * k0).real
        lap = (C * MU ** 2 * k0).real
        return (0.5 * KB * lap ** 2 + 0.5 * KT / W0 ** 2 * u ** 2) * 2 * np.pi * r

    val, _ = quad(dens, R, R + 40.0 / LAM, limit=400)
    return val


F1D = KT / (np.sqrt(2.0) * LAM * W0 ** 2)  # per U^2

fig = plt.figure(figsize=(10.4, 3.5))
gs = fig.add_gridspec(1, 3, width_ratios=[1.35, 1, 1], wspace=0.38, left=0.02, right=0.98, bottom=0.17, top=0.86)

# A: schematic of the deformed bilayer (computed profiles)
ax = fig.add_subplot(gs[0])
ax.set_xlim(-6.5, 7.4)
ax.set_ylim(-11.0, 4.6)
ax.set_aspect("equal")
ax.axis("off")
HEAD = 0.8
for yc, U, name in ((0.0, 0.5, "positive mismatch, U > 0"), (-7.4, -0.5, "negative mismatch, U < 0")):
    a = 1.2  # half-width of the protein in the drawing
    for sgn in (-1, 1):
        x = np.linspace(a, 6.3, 200)
        w = W0 + u1d(x - a, U)
        xs = sgn * x
        ax.fill_between(xs, yc - w, yc + w, color=P.fill("lipid_tail"), lw=0, zorder=2)
        ax.fill_between(xs, yc + w, yc + w + HEAD, color=P.fill("lipid_head"), lw=0, zorder=2)
        ax.fill_between(xs, yc - w - HEAD, yc - w, color=P.fill("lipid_head"), lw=0, zorder=2)
        for s in (1, -1):
            ax.plot(xs, yc + s * w, color=P.edge("lipid_tail"), lw=0.6, zorder=3)
            ax.plot(xs, yc + s * (w + HEAD), color=P.edge("lipid_head"), lw=0.7, zorder=3)
    Wp = W0 + U
    bio.shape(ax, [(-a, yc - Wp - 0.9), (a, yc - Wp - 0.9), (a, yc + Wp + 0.9), (-a, yc + Wp + 0.9)], token="channel", zorder=4)
    ax.plot([-a, a], [yc + Wp, yc + Wp], color=P.edge("channel"), lw=0.6, ls=":", zorder=5)
    ax.plot([-a, a], [yc - Wp, yc - Wp], color=P.edge("channel"), lw=0.6, ls=":", zorder=5)
    bio.label(ax, (0, yc), "protein", size="tiny", color=P.on_fill())
    bio.label(ax, (0, yc + W0 + HEAD + 1.55), name, size="small")
    ax.annotate("", xy=(5.9, yc + W0), xytext=(5.9, yc - W0),
                arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.7))
    bio.label(ax, (6.35, yc), r"$2w_0$", size="tiny", ha="left")
ax.set_title("A  Hydrophobic matching", fontsize=bio.core.FONT["small"], color=P.ink(), loc="left", weight="bold", pad=10)

# B: profiles
ax = fig.add_subplot(gs[1])
R = 2.5
x = np.linspace(0, 6, 300)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.plot(x * LAM, u1d(x, 1.0), color=charts.line("channel"), lw=1.4, label="one dimension")
ax.plot(x * LAM, u2d(R + x, R, 1.0), color=charts.line("lipid_head"), lw=1.4, ls="--", label=r"cylinder, $R = 2.5$ nm")
ax.set_xlim(0, 6)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, r"distance from the protein $\lambda(r - R)$", r"$u/U$")
charts.title(ax, "B  Decaying, oscillating profile")

# C: energy per unit boundary length
ax = fig.add_subplot(gs[2])
lr = np.linspace(0.5, 12, 40)
ratio = [energy2d(v / LAM) / (2 * np.pi * (v / LAM) * F1D) for v in lr]
ax.plot(lr, ratio, color=charts.line("lipid_head"), lw=1.4)
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.text(11.8, 1.02, "line-tension approximation", color=P.muted(), fontsize=bio.core.FONT["tiny"], ha="right", va="bottom")
for Rm, nm in ((2.3, "MscL closed"), (3.5, "MscL open")):
    v = Rm * LAM
    yv = energy2d(Rm) / (2 * np.pi * Rm * F1D)
    ax.plot(v, yv, "o", color=charts.line("channel"), ms=4)
    ax.annotate(nm, (v, yv), xytext=(v + 1.2, yv + 0.12), fontsize=bio.core.FONT["tiny"], color=P.ink(),
                arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.set_ylim(0.8, 1.9)
charts.style_axes(ax, r"$\lambda R$", r"$G_{\mathrm{2D}}/(2\pi R f)$")
charts.title(ax, "C  Energy of the annulus")
