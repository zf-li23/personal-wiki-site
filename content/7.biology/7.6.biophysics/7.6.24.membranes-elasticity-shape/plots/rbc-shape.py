"""Geometry and bending energy of the human red blood cell. A: the measured biconcave profile
(Evans and Fung 1972: thickness T = R sqrt(1 - x^2) (c0 + c1 x^2 + c2 x^4), x = rho / R, R = 3.91 um,
c0 = 0.207, c1 = 2.003, c2 = -1.123; z = +-T/2), with the sphere of the same area (dashed) and of the same
volume (dotted). Its area is about 135 um^2 and its volume about 94 fL, a reduced volume
v = V / (4 pi R0^3 / 3) = 0.64, where R0 = sqrt(A / 4 pi): the cell has about 40 % more membrane than a
sphere of its volume. B: local mean curvature 2H (in 1/um) along the profile from the rim to the
dimple, computed from the profile; the energy (kappa/2) integral (2H)^2 dA is about 1.9 times that of
a sphere, 8 pi kappa. C: osmotic swelling at constant area: volume against the NaCl concentration of
the medium by the Boyle-van 't Hoff relation V = b V0 + (1 - b) V0 (c0 / c) with an osmotically
inactive fraction b = 0.4 and V0 = 94 fL in 0.9 % NaCl; the cell becomes a sphere, and then lyses,
when V reaches the volume of the sphere of its area, near 0.45 % NaCl (the osmotic fragility test)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
Rc, c0, c1, c2 = 3.91, 0.207161, 2.002558, -1.122762
u = np.linspace(0, np.pi / 2, 20001)  # x = sin u removes the square-root singularity at the rim
x = np.sin(u)
rho = Rc * x
z = Rc / 2 * np.cos(u) * (c0 + c1 * x**2 + c2 * x**4)
dr = np.gradient(rho, u); dz = np.gradient(z, u)
ddr = np.gradient(dr, u); ddz = np.gradient(dz, u)
sp = np.hypot(dr, dz)
k1 = (dr * ddz - dz * ddr) / sp**3  # meridional curvature
k2 = np.where(rho > 1e-6, dz / (np.maximum(rho, 1e-9) * sp), k1)  # parallel curvature
r_ = rho
dA = 2 * np.pi * rho * sp  # area element per du
area_half = np.trapezoid(dA, u)
A = 2 * area_half
V = 2 * np.trapezoid(2 * np.pi * rho * z * np.gradient(rho, u), u)
R0 = np.sqrt(A / (4 * np.pi))
v = V / (4 / 3 * np.pi * R0**3)
H2 = (k1 + k2) ** 2
mask = u > 1e-3
Eb = 2 * 0.5 * np.trapezoid((H2 * dA)[mask], u[mask])  # in units of kappa
ratio = Eb / (8 * np.pi)

fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2), gridspec_kw=dict(width_ratios=[1.3, 1, 1]))
fig.subplots_adjust(wspace=0.38, left=0.06, right=0.97, bottom=0.18, top=0.87)
ax = axs[0]
X = np.concatenate([-rho[::-1], rho])
Z = np.concatenate([z[::-1], z])
ax.fill_between(X, -Z, Z, color=P.fill("blood"), alpha=0.85, lw=0)
ax.plot(X, Z, color=P.edge("blood"), lw=1.2); ax.plot(X, -Z, color=P.edge("blood"), lw=1.2)
t = np.linspace(0, 2 * np.pi, 200)
ax.plot(R0 * np.cos(t), R0 * np.sin(t), color=P.muted(), lw=0.9, ls="--")
Rv = (3 * V / (4 * np.pi)) ** (1 / 3)
ax.plot(Rv * np.cos(t), Rv * np.sin(t), color=P.muted(), lw=0.9, ls=":")
ax.text(-4.3, -3.9, rf"A = {A:.0f} $\mu$m$^2$, V = {V:.0f} fL, v = {v:.2f}", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_aspect("equal"); ax.set_xlim(-4.5, 4.5); ax.set_ylim(-4.2, 3.6)
charts.style_axes(ax, r"$\rho$ / $\mu$m", r"z / $\mu$m")
charts.title(ax, "A  The discocyte")

ax = axs[1]
pm = (u > 1e-3) & (u < np.pi / 2 - 2e-3)
ax.plot(r_[pm], (k1 + k2)[pm], color=charts.line("blood"), lw=1.6)
ax.axhline(2 / R0, color=P.muted(), lw=0.8, ls="--")
ax.text(0.2, 2 / R0 + 0.15, "sphere of equal area", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.text(1.6, 0.85, rf"$E_{{\mathrm{{b}}}} = {ratio:.1f} \times 8\pi\kappa$", fontsize=bio.core.FONT["small"], color=P.ink())
charts.style_axes(ax, r"distance from axis $\rho$ / $\mu$m", r"mean curvature 2H / $\mu$m$^{-1}$")
charts.title(ax, "B  Curvature of the upper face")

ax = axs[2]
cs = np.linspace(0.3, 1.2, 300)
b, V0 = 0.4, V
Vc = b * V0 + (1 - b) * V0 * 0.9 / cs
Vs = 4 / 3 * np.pi * R0**3
ax.plot(cs, Vc, color=charts.line("blood"), lw=1.7)
ax.axhline(Vs, color=P.muted(), lw=0.8, ls="--")
cl = 0.9 * (1 - b) * V0 / (Vs - b * V0)
ax.axvline(cl, color=charts.line("negative"), lw=0.8, ls=":")
ax.text(cl + 0.02, Vs + 6, "sphere: lysis", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.text(0.92, V0 + 6, "isotonic", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.plot(0.9, V0, "o", color=charts.line("blood"), ms=4)
ax.set_ylim(40, 220)
charts.style_axes(ax, "NaCl in medium / %", "cell volume / fL")
charts.title(ax, "C  Fixed area limits swelling")
