"""Linear stability of Turing's example: f = a(h - 1)/16 - 3/4, g = 1 - a h / 16 (uniform state a = h = 4).

The Jacobian has f_a = 3/16, f_h = 1/4, g_a = -1/4, g_h = -1/4 (trace -1/16, determinant 1/64), so the well-mixed
system is stable. With activator diffusion eps = 1 and inhibitor diffusion nu, a perturbation cos(k x) exp(Omega t)
grows at the largest real part of the eigenvalues of M(k^2) = J - k^2 diag(eps, nu). A: growth rate against k for
nu / eps = 2, 4 (the threshold) and 8; for nu / eps = 8 a band of wave numbers grows, and the dot marks the fastest
mode given by the closed formula for k^2_max. B: the discrete modes k = p pi / L allowed by no-flux boundaries on an
interval of length L = 40 (vertical ticks): only modes inside the band grow, so a tissue shorter than the shortest
unstable wavelength stays uniform.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fa, fh, ga, gh = 3 / 16, 1 / 4, -1 / 4, -1 / 4
eps = 1.0


def growth(nu, k):
    out = []
    for kk in k:
        M = np.array([[fa - eps * kk**2, fh], [ga, gh - nu * kk**2]])
        out.append(np.linalg.eigvals(M).real.max())
    return np.array(out)


fig, ax = bio.canvas(24.0, 9.0)
k = np.linspace(0, 0.6, 600)
pa = C.axes_at(ax, (1.8, 1.4, 9.4, 6.2))
for nu, tk in ((2.0, "neutral"), (4.0, "na"), (8.0, "negative")):
    pa.plot(k, growth(nu, k), color=Q.line_color(tk), lw=1.8, label=f"ν/ε = {nu:g}")
nu = 8.0
Pp = -fh * ga
k2 = ((nu + eps) * np.sqrt(Pp / (eps * nu)) + gh - fa) / (nu - eps)
om = (nu * fa - eps * gh - 2 * np.sqrt(eps * nu * Pp)) / (nu - eps)
pa.plot([np.sqrt(k2)], [om], "o", color=Q.line_color("negative"), ms=6)
pa.text(np.sqrt(k2) + 0.015, om + 0.004, "fastest mode", color=P.ink(), fontsize=FS["tiny"])
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 0.6)
top = 1.25 * growth(8.0, k).max()
pa.set_ylim(-0.08, top)
C.style_axes(pa, "wave number k", "growth rate max Re Ω")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 8.4))
bio.label(ax, (1.8, 8.4), "Dispersion relation of Turing's example", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (14.0, 1.4, 9.4, 6.2))
L = 40.0
pb.plot(k, growth(8.0, k), color=Q.line_color("negative"), lw=1.8)
ks = np.arange(0, 9) * np.pi / L
gk = growth(8.0, ks)
for kk, gg in zip(ks, gk):
    pb.plot([kk, kk], [-0.08, gg], color=Q.line_color("protein") if gg > 0 else P.muted(), lw=1.4)
    pb.plot([kk], [gg], "o", ms=4.5, color=Q.line_color("protein") if gg > 0 else P.muted())
pb.axhline(0, color=P.muted(), lw=0.8)
pb.set_xlim(0, 0.6)
pb.set_ylim(-0.08, top)
C.style_axes(pb, "wave number k", "growth rate")
pb.text(0.42, 0.8 * top, "modes k = pπ/L, L = 40", color=P.ink(), fontsize=FS["tiny"])
bio.panel(ax, "B", (12.5, 8.4))
bio.label(ax, (14.0, 8.4), "A finite tissue selects discrete modes", size="small", bold=True, ha="left")
