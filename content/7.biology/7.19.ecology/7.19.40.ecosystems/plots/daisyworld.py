"""Daisyworld (Watson and Lovelock 1983): regulation of planetary temperature by biota.

A planet with bare ground (albedo 0.5), white daisies (0.75) and black daisies (0.25), lit by a star
whose luminosity L (relative to S = 917 W m^-2) slowly changes. Planetary temperature from radiation
balance, sigma Te^4 = S L (1 - A), A the area-weighted albedo; local temperatures
T_i^4 = q (A - A_i) + Te^4 with q = 2.06e9 K^4 (heat transfer from dark to light areas).
Daisy cover a_i grows as da_i/dt = a_i (x beta(T_i) - gamma), x = 1 - a_w - a_b bare fertile ground,
beta(T) = 1 - 0.003265 (295.5 - T)^2 (optimum 22.5 C, zero below 5 and above 40 C), gamma = 0.3.
At each L the equations are integrated to equilibrium starting from the previous state (seeded with
1 % cover of each daisy), once with L increasing and once decreasing.
A: planetary temperature without life (dashed) and with daisies for increasing (solid) and
decreasing (dotted) luminosity: over a wide range the temperature stays near the optimum and even
falls as L rises; at the edges regulation fails abruptly, and the collapse at high L is not
reversed until L is much lower (hysteresis). B: equilibrium cover of black and white daisies
(L increasing).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 12.0)

sig, S, q = 5.670374e-8, 917.0, 2.06e9
Ag, Aw, Ab, gam = 0.5, 0.75, 0.25, 0.3


def temps(aw, ab, L):
    A = (1 - aw - ab) * Ag + aw * Aw + ab * Ab
    Te4 = S * L * (1 - A) / sig
    return Te4 ** 0.25, (q * (A - Aw) + Te4) ** 0.25, (q * (A - Ab) + Te4) ** 0.25


def beta(T):
    return max(0.0, 1 - 0.003265 * (295.5 - T) ** 2)


def rhs(t, y, L):
    aw, ab = max(y[0], 0), max(y[1], 0)
    x = 1 - aw - ab
    _, Tw, Tb = temps(aw, ab, L)
    return [aw * (x * beta(Tw) - gam), ab * (x * beta(Tb) - gam)]


def sweep(Ls):
    y = np.array([0.01, 0.01])
    out = []
    for L in Ls:
        y = np.maximum(y, 0.01)
        y = solve_ivp(rhs, (0, 300), y, args=(L,), rtol=1e-7).y[:, -1]
        y = np.where(y < 1e-3, 0.0, y)
        out.append((L, y[0], y[1], temps(y[0], y[1], L)[0] - 273.15))
    return np.array(out)


Ls = np.linspace(0.6, 1.7, 111)
up, dn = sweep(Ls), sweep(Ls[::-1])
bare = (S * Ls * (1 - Ag) / sig) ** 0.25 - 273.15

pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
pa.plot(Ls, bare, color=P.muted(), lw=1.3, ls="--", label="no life")
pa.plot(up[:, 0], up[:, 3], color=Q.line_color("plant"), lw=1.9, label="daisies, L increasing")
pa.plot(dn[:, 0], dn[:, 3], color=Q.line_color("negative"), lw=1.3, ls=":", label="daisies, L decreasing")
pa.axhline(22.5, color=P.muted(), lw=0.6)
pa.text(0.62, 24.0, "optimum for growth", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0.6, 1.7)
pa.set_ylim(-20, 75)
C.style_axes(pa, "relative luminosity L", "planetary temperature / degrees C")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Temperature regulation by daisies", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
pb.plot(up[:, 0], up[:, 2], color=Q.line_color("neutral"), lw=1.9, label="black daisies")
pb.plot(up[:, 0], up[:, 1], color=Q.line_color("highlight"), lw=1.9, label="white daisies")
pb.plot(up[:, 0], up[:, 1] + up[:, 2], color=Q.line_color("plant"), lw=1.1, ls="--", label="total cover")
pb.set_xlim(0.6, 1.7)
pb.set_ylim(0, 0.8)
C.style_axes(pb, "relative luminosity L", "fraction of area covered")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Daisy cover (L increasing)", size="small", bold=True, ha="left")
