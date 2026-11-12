"""The DNA barcode gap (schematic). Histograms of pairwise COI distances within species and between each
species and its nearest neighbour, drawn from illustrative gamma distributions (not data for a real group).
Panel A: a group with a clear gap, where a 2% threshold separates the distributions. Panel B: a group with
recently diverged or hybridizing species, where the distributions overlap and a threshold misassigns the
shaded tails.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(22.0, 8.6)
edges = np.linspace(0, 12, 61)


def panel(x0, intra, inter, title, letter):
    p = quant.Plot(ax, (x0, 1.6, 8.6, 5.6), xlim=(0, 12), ylim=(0, 1.1), xlabel="pairwise COI distance / %",
                   ylabel="relative frequency", xticks=[0, 2, 4, 6, 8, 10, 12], yticks=[0, 0.5, 1.0])
    hi, _ = np.histogram(intra, edges)
    he, _ = np.histogram(inter, edges)
    m = max(hi.max(), he.max())
    mid = (edges[:-1] + edges[1:]) / 2
    yi, ye = hi / m, he / m
    # errors: within-species distances above the threshold, between-species distances below it
    p.band(mid[mid >= 2.0], 0 * mid[mid >= 2.0], yi[mid >= 2.0], "negative", alpha=0.45)
    p.band(mid[mid <= 2.0], 0 * mid[mid <= 2.0], ye[mid <= 2.0], "negative", alpha=0.45)
    p.line(mid, ye, "rna", lw=1.8)
    p.line(mid, yi, "dna", lw=1.8)
    p.vline(2.0, token="ink", dashed=True, lw=1.2, text="threshold 2%")
    err = (np.mean(intra > 2.0) + np.mean(inter < 2.0)) / 2
    msg = "misassigned: under 1%" if err < 0.01 else f"misassigned: about {100 * err:.0f}%"
    p.text(8.0, 0.55, msg, color=quant.line_color("negative"))
    p.legend([("within species", "dna", "-"), ("to nearest species", "rna", "-")], (x0 + 5.0, 6.6))
    bio.panel(ax, letter, (x0 - 1.0, 8.2))
    bio.label(ax, (x0 + 4.3, 8.2), title, size="small", bold=True)

panel(1.8, rng.gamma(2.0, 0.25, 4000), 3.0 + rng.gamma(4.0, 1.0, 4000), "A clear barcode gap", "A")
panel(12.8, rng.gamma(2.0, 0.6, 4000), 0.5 + rng.gamma(2.5, 1.2, 4000), "Overlap: recent or hybridizing species", "B")
bio.label(ax, (11.0, 0.3), "schematic: illustrative distributions", size="tiny", color=P.muted())
