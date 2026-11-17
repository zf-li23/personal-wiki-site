"""Turing instability in the Schnakenberg system u_t = a - u + u^2 v + lap u, v_t = b - u^2 v + d lap v.

Uniform state u* = a + b, v* = b / (a + b)^2.
A: dispersion relation for a = 0.1, b = 0.9: the largest real part of the eigenvalues of J - k^2 diag(1, d)
against k^2 for d = 5 (stable), d = d_c = 8.57 (threshold, critical k_c^2 = sqrt(det J / d_c) = 0.34) and
d = 20 (a band of unstable wave numbers).
B: Turing space in the (a, b) plane for d = 20: inside the shaded region the uniform state is stable
without diffusion (tr J < 0, det J > 0) but unstable with it; inside the dashed curve (tr J = 0) it is
unstable even without diffusion (Hopf); elsewhere it is stable. Point: the parameters of A and C.
C: pattern of u grown from the uniform state with 1 % noise (a = 0.1, b = 0.9, d = 20) on a periodic
square of side 64 (128 x 128 grid, semi-implicit Fourier scheme, dt = 0.02, t = 200): spots of
activator u with spacing close to 2 pi / k_max = 12.9 (fastest mode k_max^2 = 0.24).
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT


def jac(a, b):
    u = a + b
    v = b / u**2
    return np.array([[-1 + 2 * u * v, u * u], [-2 * u * v, -u * u]])


def growth(J, k2, d):
    out = []
    for q in k2:
        M = J - q * np.diag([1.0, d])
        out.append(np.linalg.eigvals(M).real.max())
    return np.array(out)


fig, ax = bio.canvas(33.0, 11.0)
a0, b0 = 0.1, 0.9
J0 = jac(a0, b0)
fu, fv, gu, gv = J0[0, 0], J0[0, 1], J0[1, 0], J0[1, 1]
A2, B2, C2 = fu**2, 2 * (2 * fv * gu - fu * gv), gv**2
dc = (-B2 + np.sqrt(B2**2 - 4 * A2 * C2)) / (2 * A2)
k2 = np.linspace(0, 1.2, 400)
pa = C.axes_at(ax, (2.0, 1.7, 8.0, 7.6))
for d, tok, lab in ((5.0, "dna", "d = 5"), (dc, "ink", f"d = d_c = {dc:.2f}"), (20.0, "negative", "d = 20")):
    pa.plot(k2, growth(J0, k2, d), color=Q.line_color(tok), lw=1.7, label=lab)
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 1.2)
pa.set_ylim(-0.4, 0.5)
C.style_axes(pa, "squared wave number k^2", "growth rate Re sigma")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (2.0, 10.0), "Dispersion relation", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.0, 1.7, 8.0, 7.6))
aa = np.linspace(0.001, 0.4, 220)
bb = np.linspace(0.001, 2.5, 220)
AA, BB = np.meshgrid(aa, bb)
U = AA + BB
FU = (BB - AA) / U
FV = U**2
GU = -2 * BB / U
GV = -(U**2)
tr = FU + GV
det = FU * GV - FV * GU
d = 20.0
h1 = d * FU + GV
turing = (tr < 0) & (det > 0) & (h1 > 0) & (h1**2 > 4 * d * det)
pb.contourf(aa, bb, turing.astype(float), levels=[0.5, 1.5], colors=[P.mix(P.fill("highlight"), P.surface(), 0.3)])
pb.contour(aa, bb, tr, levels=[0], colors=[P.ink()], linewidths=1.0, linestyles="dashed")
pb.plot([a0], [b0], "o", ms=5, color=Q.line_color("negative"))
pb.text(0.015, 0.42, "Hopf: unstable\nwithout diffusion", fontsize=FS["tiny"], color=P.ink())
pb.text(0.17, 1.15, "Turing space", fontsize=FS["small"], color=P.ink())
pb.text(0.28, 0.25, "stable", fontsize=FS["tiny"], color=P.ink())
pb.text(0.03, 2.25, "stable", fontsize=FS["tiny"], color=P.ink())
pb.set_xlim(0, 0.4)
pb.set_ylim(0, 2.5)
C.style_axes(pb, "a", "b")
bio.panel(ax, "B", (11.3, 10.7))
bio.label(ax, (13.0, 10.0), "Turing space for d = 20", size="small", bold=True, ha="left")

n, L, dt, T = 128, 64.0, 0.02, 200.0
kk = 2 * np.pi * np.fft.fftfreq(n, d=L / n)
K2 = kk[:, None] ** 2 + kk[None, :] ** 2
rng = np.random.default_rng(1)
us, vs = a0 + b0, b0 / (a0 + b0) ** 2
u = us * (1 + 0.01 * rng.standard_normal((n, n)))
v = vs * (1 + 0.01 * rng.standard_normal((n, n)))
Eu = 1 / (1 + dt * K2)
Ev = 1 / (1 + dt * d * K2)
for _ in range(int(T / dt)):
    uuv = u * u * v
    u = np.fft.ifft2(np.fft.fft2(u + dt * (a0 - u + uuv)) * Eu).real
    v = np.fft.ifft2(np.fft.fft2(v + dt * (b0 - uuv)) * Ev).real
cmap = LinearSegmentedColormap.from_list("act", [P.surface(), P.fill("plant"), P.edge("plant")])
pc = C.axes_at(ax, (24.0, 1.7, 7.6, 7.6))
pc.imshow(u, cmap=cmap, origin="lower", extent=[0, L, 0, L], interpolation="bilinear")
pc.set_xticks([])
pc.set_yticks([])
for sp in pc.spines.values():
    sp.set_color(P.muted())
bio.panel(ax, "C", (22.3, 10.7))
bio.label(ax, (24.0, 10.0), "Pattern of u (a = 0.1, b = 0.9, d = 20)", size="small", bold=True, ha="left")
