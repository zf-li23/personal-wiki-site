"""Diameter rules at dendritic branch points, d_m^p = d_1^p + d_2^p.

A: for a symmetric bifurcation the daughter/parent diameter ratio is 2^(-1/p): p = 3/2 (Rall,
impedance matching of passive cables), p = 2 (Da Vinci, conserved cross-section), p = 3 (Murray,
minimum transport cost). Measured dendrites scatter between p = 3/2 and 3.
B: diameters after repeated symmetric branching from a 4 um primary dendrite. The rule of Liao,
Liang and Howard (2021), d_m^2 + d_0^2 = d_1^2 + d_2^2, adds a minimal terminal diameter d_0
(here 0.4 um, illustrative), so that branches stop thinning near d_0.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.1))

p = np.linspace(1, 4, 200)
ax.plot(p, 2 ** (-1 / p), color=P.ink(), lw=2)
rules = [(1.5, "Rall, p = 3/2", "channel"), (2.0, "Da Vinci, p = 2", "plant"), (3.0, "Murray, p = 3", "blood")]
for pp, name, tok in rules:
    r = 2 ** (-1 / pp)
    ax.plot([pp], [r], "o", color=P.edge(tok), ms=8)
    ax.text(pp + 0.08, r - 0.025, f"{name}: {r:.2f}", fontsize=8.5, color=P.edge(tok), va="top")
ax.axvspan(1.5, 3, color=P.fill("neutral"), alpha=0.2, lw=0)
ax.text(2.25, 0.86, "range measured\nin dendrites", ha="center", fontsize=8, color=P.muted())
ax.set_xlabel("Exponent $p$")
ax.set_ylabel("Daughter / parent diameter")
ax.set_xlim(1, 4)
ax.set_ylim(0.45, 0.9)
ax.set_title("A  Symmetric bifurcation: $d_1/d_m = 2^{-1/p}$", loc="left", fontsize=10)

orders = np.arange(0, 9)
d0 = 0.4
for pp, name, tok in rules:
    bx.semilogy(orders, 4.0 * 2 ** (-orders / pp), "o-", color=P.edge(tok), lw=1.6, ms=4, label=name)
d = [4.0]
for _ in orders[1:]:
    d.append(np.sqrt((d[-1] ** 2 + d0 ** 2) / 2))
bx.semilogy(orders, d, "s-", color=P.edge("protein"), lw=2, ms=4, label="Liao et al. 2021, $d_0$ = 0.4 $\\mu$m")
bx.axhline(d0, color=P.muted(), lw=1, ls=":")
bx.text(0.1, d0 * 1.06, "$d_0$", fontsize=9, color=P.muted(), ha="left", va="bottom")
bx.set_xlabel("Branch order")
bx.set_ylabel("Diameter / $\\mu$m")
bx.legend(frameon=False, fontsize=8, loc="lower left")
bx.set_title("B  Thinning along a dendritic tree", loc="left", fontsize=10)
for x in (ax, bx):
    x.grid(True, alpha=0.3, which="both")
fig.tight_layout()
