"""Bell's receptor-ligand model: from the product rule to the minimum rule of adhesion.

Equilibrium bond density for receptor and ligand densities r0, l0 and 2D affinity K = k+/k-:
b_eq = (1/2)[(r0 + l0 + 1/K) - sqrt((r0 + l0 + 1/K)^2 - 4 r0 l0)].
A: b_eq against K for r0 = 1, l0 = 0.4 (densities in arbitrary units); dashed: the limits K r0 l0
(K(r0 + l0) << 1) and min(r0, l0) (K(r0 + l0) >> 1).
B: interfacial tension between cell types with site densities N and n (adhesive energy taken equal
to b_eq of the contact, gamma = (b(N,N) + b(n,n))/2 - b(N,n)), normalized by its value at n = 0,
against n/N for K N = 0.01, 1, 100 and 10^4: the parabola (1 - n/N)^2 of the sparse-site (product) rule
turns into the straight line 1 - n/N of the floating-site (minimum) rule.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P


def beq(r, l, K):
    s = r + l + 1 / K
    return 0.5 * (s - np.sqrt(s * s - 4 * r * l))


fig, ax = bio.canvas(30.0, 10.0)
bio.panel(ax, "A", (0.1, 9.9))
pa = charts.axes_at(ax, (2.2, 1.8, 11.0, 7.0))
K = np.logspace(-3, 3, 300)
pa.plot(K, beq(1.0, 0.4, K), color=quant.line_color("receptor"), lw=2.2, label="b_eq")
pa.plot(K, K * 0.4, color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="K r0 l0 (product rule)")
pa.plot(K, 0 * K + 0.4, color=P.muted(), lw=1.0, ls=(0, (1, 1.5)), label="min(r0, l0)")
pa.set_xscale("log")
pa.set_yscale("log")
pa.set_xlim(1e-3, 1e3)
pa.set_ylim(1e-4, 1)
charts.style_axes(pa, "affinity K (per unit density)", "bond density b_eq")
leg = pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="lower right")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pa, "Bond density: product at low affinity, minimum at high")

bio.panel(ax, "B", (16.0, 9.9))
pb = charts.axes_at(ax, (18.2, 1.8, 11.0, 7.0))
x = np.linspace(0, 1, 200)
for KN, tok in ((0.01, "ectoderm"), (1.0, "highlight"), (100.0, "protein"), (1e4, "mesoderm")):
    Nn, Kv = 1.0, KN
    g = 0.5 * (beq(Nn, Nn, Kv) + beq(x, x, Kv)) - beq(Nn, x, Kv)
    pb.plot(x, g / g[0], color=quant.line_color(tok), lw=2.2, label=f"K N = {KN:g}")
pb.plot(x, (1 - x) ** 2, color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="(1 − n/N)²")
pb.plot(x, 1 - x, color=P.muted(), lw=1.0, ls=(0, (1, 1.5)), label="1 − n/N")
pb.set_xlim(0, 1)
pb.set_ylim(0, 1.05)
charts.style_axes(pb, "site density ratio n/N", "interfacial tension (normalized)")
leg = pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], loc="upper right")
for t in leg.get_texts():
    t.set_color(P.ink())
charts.title(pb, "Tension between cell types with N and n sites")
