# Gilliam's rule (Gilliam 1982; Werner and Gilliam 1984) with illustrative parameters for a juvenile fish
# such as the bluegill sunfish. Habitat 1 (open water and bottom sediments) gives fast growth, g1 = 1.0 mm
# per day, but exposes small fish to gape-limited predators: mortality mu1 = 0.002 + 0.05 exp(-(L - 20) / 12)
# per day for body length L (mm), falling as the fish outgrows the predator's mouth. Habitat 2 (vegetation)
# is safe, mu2 = 0.004 per day, but growth is slower, g2 = 0.55 mm per day. A: the ratio mu/g, the mortality
# incurred per mm of growth, in each habitat; a fish that minimizes mu/g at each size maximizes its chance
# of surviving to a size at which it is safe, and should switch from vegetation to open water where the
# two curves cross. B: predicted proportion of time in open water against length, with predators present
# (switch at the crossing; a smooth version is drawn to represent individual variation) and absent (mu1 =
# 0.002, open water preferred at all sizes), the pattern found in experimental ponds with and without bass.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
L = np.linspace(20, 100, 400)
g1, g2, mu2 = 1.0, 0.55, 0.004
mu1 = 0.002 + 0.05 * np.exp(-(L - 20) / 12)
r1, r2 = mu1 / g1, np.full_like(L, mu2 / g2)
Ls = L[np.argmin(np.abs(r1 - r2))]

fig, ax = bio.canvas(22.0, 9.8)
pa = quant.Plot(ax, (2.2, 1.8, 7.8, 6.4), (20, 100), (0.001, 0.1), ylog=True, xlabel="Body length L / mm",
                ylabel="Mortality per mm of growth  μ/g", xticks=[20, 40, 60, 80, 100],
                yticks=[(0.001, "0.001"), (0.01, "0.01"), (0.1, "0.1")], ylabel_offset=1.1)
bio.panel(ax, "A", (0.2, 9.6))
pa.span(20, Ls, "plant", strength=0.75)
pa.line(L, r1, "dna", lw=2.2)
pa.line(L, r2, "plant", lw=2.2, dashed=True)
pa.vline(Ls, text=f"switch at {Ls:.0f} mm", top=True)
pa.text(24, 0.07, "open water: fast growth,\nrisky while small", ha="left", va="top", token="dna")
pa.text(98, 0.0085, "vegetation: slow growth, safe", ha="right", va="bottom", token="plant")
pa.text((20 + Ls) / 2, 0.0013, "stay in cover", color=P.muted())
pa.text((Ls + 100) / 2, 0.0013, "forage in the open", color=P.muted())

pb = quant.Plot(ax, (13.2, 1.8, 7.6, 6.4), (20, 100), (0, 1.05), xlabel="Body length L / mm",
                ylabel="Proportion of time in open water", xticks=[20, 40, 60, 80, 100], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (11.4, 9.6))
pb.line([20, Ls, Ls, 100], [0, 0, 1, 1], "dna", lw=1.2, dotted=True)
pb.line(L, 1 / (1 + np.exp(-(L - Ls) / 4)), "dna", lw=2.2)
pb.line(L, np.full_like(L, 0.97), "rna", lw=2.0, dashed=True)
pb.text(98, 0.9, "predators absent", ha="right", va="top", token="rna")
pb.text(Ls + 3, 0.45, "predators present", ha="left", token="dna")
