"""How actin polymerization pushes a membrane: the dendritic network of a lamellipodium and the
polymerization ratchet.

A: schematic of the leading edge (dendritic nucleation model). Rac-GTP activates WAVE at the membrane,
which activates the Arp2/3 complex to branch new filaments off existing ones (70 degrees, about +-35
degrees to the edge); plus ends that reach the membrane push it forward, others are capped within a short
distance; behind the front cofilin disassembles the old (ADP) filaments and the monomers are recycled
by profilin. The network flows backward (retrograde flow) relative to the moving edge.
B: force-velocity relation of a polymerization ratchet (Peskin, Odell and Oster 1993) in the limit where
membrane fluctuations are fast: v = delta (k_on c exp(-f delta / k_B T) - k_off), with delta = 2.7 nm
(the filament grows by half a monomer per subunit added), barbed-end k_on = 11.6 per uM per s,
k_off = 1.4 per s and k_B T = 4.1 pN nm, for three monomer concentrations; the stall force is
f_s = (k_B T / delta) ln(c / C_c).
C: Euler buckling force F_c = pi^2 kappa / L^2 of a single actin filament (flexural rigidity kappa =
7.3e-26 N m^2, Gittes et al. 1993; hinged ends) against its free length L: a filament longer than about
0.3 um buckles before it can exert the stall force, which is why pushing filaments are short and branched.
"""

import math

import numpy as np

import wikibio as bio
from wikibio import charts, quant
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(27.0, 9.0)

# ---- A
bio.panel(ax, "A", (0.1, 8.9))
net = C.lamellipodium(ax, 1.8, 9.4, front=7.2, depth=4.6, density=0.75, seed=7, lw=1.5)
for x in np.linspace(2.2, 9.0, 5):
    bio.protein(ax, (x, 7.48), 0.42, 0.22, C.tok("adaptor"))
bio.label(ax, (9.65, 7.55), "WAVE\n(Rac-GTP)", size="tiny", ha="left")
bio.label(ax, (9.65, 6.6), "Arp2/3", size="tiny", ha="left")
bio.label(ax, (9.65, 5.6), "capping\nprotein", size="tiny", ha="left")
for k, x in enumerate(np.linspace(2.2, 8.8, 6)):
    bio.protein(ax, (x, 2.0 + 0.25 * (k % 2)), 0.2, 0.15, C.tok("cofilin"))
bio.label(ax, (9.65, 2.1), "cofilin:\ndisassembly", size="tiny", ha="left")
bio.label(ax, (5.6, 1.25), "profilin-actin recycled to the front", size="tiny", color=P.muted())
bio.arrow(ax, (5.6, 8.1), (5.6, 8.85), kind="process")
bio.label(ax, (5.9, 8.5), "protrusion", size="tiny", ha="left")
bio.arrow(ax, (0.9, 6.4), (0.9, 3.4), kind="process", color=P.muted())
bio.label(ax, (0.9, 2.9), "retrograde\nflow", size="tiny", color=P.muted())
bio.label(ax, (5.6, 0.55), "Outside above the membrane, cytosol below", size="tiny", color=P.muted())

# ---- B
bio.panel(ax, "B", (12.0, 8.9))
pb = charts.axes_at(ax, (13.6, 1.4, 5.6, 6.6))
d, kon, koff, kT = 2.7, 11.6, 1.4, 4.1
f = np.linspace(0, 12, 300)
for c, tk in ((1.0, "channel"), (5.0, "actin"), (20.0, "protein")):
    v = d * (kon * c * np.exp(-f * d / kT) - koff)  # nm/s
    pb.plot(f, v * 60 / 1000, color=quant.line_color(tk), lw=1.8, label=f"c = {c:g} µM")
    fs = kT / d * math.log(c / (koff / kon))
    pb.plot([fs], [0], "o", color=quant.line_color(tk), ms=4)
pb.axhline(0, color=P.muted(), lw=0.7)
pb.set_ylim(-1, 40)
pb.set_xlim(0, 10)
pb.text(4.6, 2.0, "stall forces", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "load per filament / pN", "velocity / (µm min⁻¹)")
charts.title(pb, "Polymerization ratchet")

# ---- C
bio.panel(ax, "C", (20.4, 8.9))
pc = charts.axes_at(ax, (22.0, 1.4, 4.6, 6.6))
L = np.linspace(0.05, 2.0, 300)
kappa = 7.3e-26
Fc = math.pi**2 * kappa / (L * 1e-6) ** 2 * 1e12
pc.loglog(L, Fc, color=quant.line_color("actin"), lw=1.8)
fs10 = kT / d * math.log(5 / (koff / kon))
pc.axhline(fs10, color=quant.line_color("muted"), lw=0.9, ls=(0, (3, 2)))
pc.text(0.06, fs10 * 1.25, "stall force (5 µM)", fontsize=bio.core.FONT["tiny"], color=P.muted())
pc.text(0.45, 30, "stable", fontsize=bio.core.FONT["tiny"], color=P.muted())
pc.text(0.08, 1.2, "buckles", fontsize=bio.core.FONT["tiny"], color=P.muted())
pc.set_xticks([0.1, 0.3, 1])
pc.set_xticklabels(["0.1", "0.3", "1"])
charts.style_axes(pc, "free filament length / µm", "buckling force / pN")
charts.title(pc, "Why short filaments push")
