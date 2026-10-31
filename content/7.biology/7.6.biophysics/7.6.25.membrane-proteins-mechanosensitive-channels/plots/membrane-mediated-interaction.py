"""Membrane-mediated interaction between two inclusions in the one-dimensional thickness model.

The strip of bilayer between two walls a distance d apart satisfies Kb u'''' + (Kt/w0^2) u = 0 with
u = U1 at x = 0, u = U2 at x = d and zero slopes (hydrophobic gluing). Its energy, minus the energy 2f
of two isolated faces (the outer faces are unchanged), is the interaction per unit length of contact.
Same constants as the deformation figure (1/lambda = 1.0 nm). A: interaction energy in units of the
line tension f against lambda d, for equal mismatches (U1 = U2) and opposite ones (U1 = -U2).
B: profiles between equal inclusions at three separations: the bilayer cannot relax between close
neighbors, so its deformation energy, and with it the attraction, comes from the lost faces."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
KB, KT, W0 = 20.0, 60.0, 1.75
LAM = (KT / (KB * W0 ** 2)) ** 0.25
A = LAM / np.sqrt(2.0)


def basis(x, c):
    """Four solutions centered at c (well conditioned): cosh cos, cosh sin, sinh cos, sinh sin."""
    y = A * (x - c)
    ch, sh, co, si = np.cosh(y), np.sinh(y), np.cos(y), np.sin(y)
    f = np.array([ch * co, ch * si, sh * co, sh * si])
    # derivatives d/dx
    df = A * np.array([sh * co - ch * si, sh * si + ch * co, ch * co - sh * si, ch * si + sh * co])
    d2 = A ** 2 * np.array([-2 * sh * si, 2 * sh * co, -2 * ch * si, 2 * ch * co])
    return f, df, d2


def strip(d, U1, U2, n=2001):
    c = d / 2
    f0, df0, _ = basis(0.0, c)
    f1, df1, _ = basis(d, c)
    M = np.array([f0, df0, f1, df1])
    coef = np.linalg.solve(M, [U1, 0.0, U2, 0.0])
    x = np.linspace(0, d, n)
    f, df, d2 = basis(x, c)
    u = coef @ f
    upp = coef @ d2
    dens = 0.5 * KB * upp ** 2 + 0.5 * KT / W0 ** 2 * u ** 2
    return x, u, np.trapezoid(dens, x)


F = KT / (np.sqrt(2.0) * LAM * W0 ** 2)  # line tension per U^2

fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
ld = np.linspace(0.05, 9, 400)
for U2, tok, lab in ((1.0, "channel", r"equal mismatch, $U_2 = U_1$"), (-1.0, "negative", r"opposite mismatch, $U_2 = -U_1$")):
    g = np.array([strip(v / LAM, 1.0, U2)[2] for v in ld]) / F - 2.0
    ax.plot(ld, g, color=charts.line(tok), lw=1.4, label=lab)
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-2.3, 3.2)
ax.set_xlim(0, 9)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, r"separation $\lambda d$", r"interaction per length / $f$")
charts.title(ax, "A  Interaction energy")
ax.annotate("contact: two faces\nof deformed bilayer lost", (0.05, -2.0), xytext=(1.6, -1.7), fontsize=bio.core.FONT["tiny"],
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))

ax = axs[1]
for v, ls in ((1.0, "-"), (2.5, "--"), (6.0, ":")):
    x, u, _ = strip(v / LAM, 1.0, 1.0)
    ax.plot(LAM * x / v, u, color=charts.line("lipid_head"), lw=1.4, ls=ls, label=rf"$\lambda d = {v:g}$")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlim(0, 1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, r"position between the inclusions $x/d$", r"$u/U$")
charts.title(ax, "B  Profiles between equal inclusions")
