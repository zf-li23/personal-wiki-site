"""Creep of the interstitial-membrane model compared with its Maxwell approximation.

Two apposed membranes slide past each other under a shear stress tau; site densities on the lower
membrane n = n0 (1 - g), with g obeying 2 dg/dt = K d2g/ds2 + dnu/dt on |s| < L0/2, g = nu at
s = L0/2 and g = 0 at s = -L0/2, where nu = tau L0 / (k n0) measures the stretch of the edges
(text, 8.2.2). The total shear strain is eps = nu/2 + (1/L0) int (u0 + u1) dt with
u0 + u1 = (K/2)[dg/ds(L0/2) + dg/ds(-L0/2)]. For a step stress applied at t = 0, the strain is
computed exactly by a Fourier sine series (units L0 = K = k = n0 = 1, so tau = nu).
Solid: exact creep compliance J(t) = eps(t)/tau. Dashed: Maxwell liquid with k_eff = 3 k n0/(2 L0)
and eta_eff = L0 n0^2 f, J = 1/k_eff + t/eta_eff; the instantaneous compliance of the exact model is
L0/(2 k n0), stiffer than 1/k_eff, because the model has a spectrum of relaxation times
(the slowest t_n = 2 L0^2/(n^2 pi^2 K), n even).
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
L0 = K = 1.0
x = np.linspace(0, L0, 4001)
w0 = -(x / L0 - 0.5)          # initial deviation from the steady linear profile (nu0 = 1)
t = np.logspace(-3, 1, 300)
strain = 0.5 + (K / 2) * 2 * t / L0 ** 2
for n in range(2, 400, 2):
    kn = n * np.pi / L0
    bn = 2 / L0 * np.trapezoid(w0 * np.sin(kn * x), x)
    an = (K / 2) * kn ** 2
    # derivative at both ends: bn kn (cos(n pi) + 1) = 2 bn kn for even n
    strain += (1 / L0) * (K / 2) * 2 * bn * kn * (1 - np.exp(-an * t)) / an
J = strain
Jm = 2 / 3 + t

fig, ax = bio.canvas(26.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
# schematic: two membranes in contact with sliding
for yy, tok, d in ((6.4, "ectoderm", 1), (5.4, "mesoderm", -1)):
    ax.plot([1.0, 9.0], [yy, yy], color=P.edge(tok), lw=2.4)
    for xx in np.linspace(1.4, 8.6, 13):
        ax.plot([xx, xx], [yy, yy - 0.22 * d], color=P.edge(tok), lw=1.0)
bio.arrow(ax, (3.5, 7.3), (6.5, 7.3), kind="process")
bio.arrow(ax, (6.5, 4.5), (3.5, 4.5), kind="process")
bio.label(ax, (5.0, 7.8), "upper cell", size="tiny")
bio.label(ax, (5.0, 4.0), "lower cell", size="tiny")
bio.label(ax, (5.0, 2.8), "contact of length L(t): sites stretched at the", size="tiny")
bio.label(ax, (5.0, 2.3), "leading edges, friction f n(s) n(−s) (u(s) + u(−s))", size="tiny")
bio.label(ax, (1.0, 5.9), "−L0/2", size="tiny")
bio.label(ax, (9.0, 5.9), "L0/2", size="tiny")

bio.panel(ax, "B", (11.2, 9.9))
pb = charts.axes_at(ax, (13.4, 1.8, 11.8, 7.2))
pb.plot(t, J, color=quant.line_color("mesoderm"), lw=2.2, label="site model (exact)")
pb.plot(t, Jm, color=P.muted(), lw=1.2, ls=(0, (3, 2)), label="Maxwell: 1/k_eff + t/η_eff")
pb.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (1, 1.5)))
pb.text(1.2e-3, 0.36, "instantaneous L0/(2kn0)", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_xscale("log")
pb.set_xlim(1e-3, 10)
pb.set_ylim(0, 4)
charts.style_axes(pb, "time t K / L0²", "creep compliance J k n0 / L0")
leg = pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper left")
for tx in leg.get_texts():
    tx.set_color(P.ink())
charts.title(pb, "Elastic at short times, viscous at long times")
