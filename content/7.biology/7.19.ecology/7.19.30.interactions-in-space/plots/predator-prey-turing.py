"""Turing patterns in a predator-prey model with a saturating functional response and predator self-limitation.

u_t = u (1 - u) - u v / (u + a) + lap u,   v_t = v (u / (u + a) - b - c v) + d lap v,
with a = 0.2, c = 1.2 and b = 0.0716 chosen so that the uniform state is u* = 0.15, v* = 0.2975, on the
rising (left) side of the prey isocline, where prey growth is self-enhancing (f_u = 0.214 > 0); predator
self-limitation (g_v = -0.357) keeps tr J = -0.143 < 0 and det J = 0.132 > 0: stable without movement.
A: dispersion relation for d = 5, d = d_c = 14.6 and d = 40 (fastest mode k^2 = 0.061, wavelength 25.4).
B: prey density after t = 400 on a periodic square of side 128 (128 x 128 grid, semi-implicit Fourier
scheme, dt = 0.05) from the uniform state with 2 % noise, d = 40: patches of high prey density.
C: prey (blue) and predator (red) along the horizontal line through the middle of B: the slowly moving
prey forms sharp patches, the fast-moving predator is nearly uniform but slightly higher in prey patches.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
a, c = 0.2, 1.2
us = 0.15
vs = (1 - us) * (us + a)
b = us / (us + a) - c * vs
fu = 1 - 2 * us - vs * a / (us + a) ** 2
fv = -us / (us + a)
gu = vs * a / (us + a) ** 2
gv = -c * vs
J = np.array([[fu, fv], [gu, gv]])
A2, B2, C2 = fu**2, 2 * (2 * fv * gu - fu * gv), gv**2
dc = (-B2 + np.sqrt(B2**2 - 4 * A2 * C2)) / (2 * A2)

fig, ax = bio.canvas(33.0, 11.0)
k2 = np.linspace(0, 0.3, 400)
pa = C.axes_at(ax, (2.0, 1.7, 8.0, 7.6))
for d, tok, lab in ((5.0, "dna", "d = 5"), (dc, "ink", f"d = d_c = {dc:.1f}"), (40.0, "negative", "d = 40")):
    g = [np.linalg.eigvals(J - q * np.diag([1.0, d])).real.max() for q in k2]
    pa.plot(k2, g, color=Q.line_color(tok), lw=1.7, label=lab)
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 0.3)
pa.set_ylim(-0.15, 0.15)
C.style_axes(pa, "squared wave number k^2", "growth rate Re sigma")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Dispersion relation", size="small", bold=True, ha="left")

n, L, dt, T, d = 128, 128.0, 0.05, 400.0, 40.0
kk = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
K2 = kk[:, None] ** 2 + kk[None, :] ** 2
rng = np.random.default_rng(2)
u = us * (1 + 0.02 * rng.standard_normal((n, n)))
v = vs * (1 + 0.02 * rng.standard_normal((n, n)))
Eu = 1 / (1 + dt * K2)
Ev = 1 / (1 + dt * d * K2)
for _ in range(int(T / dt)):
    fr = u / (u + a)
    u2 = u + dt * (u * (1 - u) - fr * v)
    v2 = v + dt * v * (fr - b - c * v)
    u = np.fft.ifft2(np.fft.fft2(u2) * Eu).real
    v = np.fft.ifft2(np.fft.fft2(v2) * Ev).real
cmap = LinearSegmentedColormap.from_list("prey", [P.surface(), P.fill("dna"), P.edge("dna")])
pb = C.axes_at(ax, (13.0, 1.7, 7.6, 7.6))
pb.imshow(u, cmap=cmap, origin="lower", extent=[0, L, 0, L], interpolation="bilinear")
pb.axhline(L / 2, color=P.muted(), lw=0.8, ls=":")
pb.set_xticks([])
pb.set_yticks([])
for sp in pb.spines.values():
    sp.set_color(P.muted())
bio.panel(ax, "B", (11.3, 10.7))
bio.label(ax, (13.0, 10.0), "Prey density, d = 40", size="small", bold=True, ha="left")

xs = np.linspace(0, L, n, endpoint=False)
pc = C.axes_at(ax, (24.0, 1.7, 8.0, 7.6))
pc.plot(xs, u[n // 2], color=Q.line_color("dna"), lw=1.6, label="prey u")
pc.plot(xs, v[n // 2], color=Q.line_color("negative"), lw=1.6, label="predator v")
pc.axhline(us, color=Q.line_color("dna"), lw=0.7, ls=":")
pc.axhline(vs, color=Q.line_color("negative"), lw=0.7, ls=":")
pc.set_xlim(0, L)
pc.set_ylim(0, 0.6)
C.style_axes(pc, "position along transect", "density")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (22.3, 10.7))
bio.label(ax, (24.0, 10.0), "Transect (dotted: uniform state)", size="small", bold=True, ha="left")
