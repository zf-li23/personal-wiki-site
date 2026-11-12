"""Monte Carlo propagation of uncertainty through Erwin's (1982) product N = T s / (b c) for the number of
tropical arthropod species (schematic). The input distributions are illustrative ranges chosen in the spirit
of Hamilton et al. (2010, Am. Nat. 176: 90-95), not their fitted values: T, number of tropical tree species;
s, effective number of host-specific beetle species per tree species (Erwin assumed 163); b, fraction of
canopy arthropod species that are beetles; c, fraction of tropical arthropod species living in the canopy.
Panel A: distribution of N (log axis) with its median and 90% interval, against Erwin's point estimate.
Panel B: share of Var(ln N) contributed by each factor (the variances of the logarithms add).
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
n = 100_000
T = rng.uniform(40_000, 60_000, n)
s = np.exp(rng.normal(np.log(30.0), 0.8, n))       # effective specialists per tree species
b = rng.uniform(0.2, 0.4, n)
c = rng.uniform(0.5, 0.85, n)
N = T * s / (b * c)
logN = np.log10(N)
med = np.median(logN)
lo, hi = np.percentile(logN, [5, 95])

fig, ax = bio.canvas(22.0, 9.0)

# --- A: distribution of the total
pa = quant.Plot(ax, (1.8, 1.6, 10.2, 6.0), xlim=(5.5, 8.0), ylim=(0, 1.1),
                xlabel="total tropical arthropod species, N (log scale)", ylabel="relative frequency",
                xticks=[(6, "1 million"), (np.log10(3e6), "3 M"), (7, "10 M"), (np.log10(3e7), "30 M")],
                yticks=[0, 0.5, 1.0])
edges = np.linspace(5.5, 8.0, 61)
h, _ = np.histogram(logN, edges)
pa.span(lo, hi, "highlight", strength=0.6)
pa.bars(edges, h / h.max(), "dna")
pa.vline(med, token="ink", dashed=False, lw=1.4, text="median", top=True)
pa.vline(np.log10(3.0e7), token="negative", dashed=True, lw=1.4, text="Erwin 1982", top=True)
pa.text(lo + 0.05, 1.04, "90% interval", color=P.muted(), ha="left")
bio.panel(ax, "A", (0.6, 8.6))
bio.label(ax, (7.0, 8.6), "Distribution of the estimate", size="small", bold=True)

# --- B: variance shares of the factors
parts = {"tree species T": np.var(np.log(T)), "specialists s": np.var(np.log(s)),
         "beetle share b": np.var(np.log(b)), "canopy share c": np.var(np.log(c))}
tot = sum(parts.values())
pb = quant.Plot(ax, (15.4, 1.6, 5.8, 6.0), xlim=(-0.6, 3.6), ylim=(0, 1.0), ylabel="share of Var(ln N)",
                yticks=[0, 0.25, 0.5, 0.75, 1.0])
for i, (name, v) in enumerate(parts.items()):
    pb.bars([i - 0.32, i + 0.32], [v / tot], "negative" if i == 1 else "neutral")
    bio.label(ax, (pb.X(i), 1.35), name, size="tiny", rotation=25, va="top")
    pb.text(i, v / tot + 0.05, f"{100 * v / tot:.0f}%", size="tiny")
bio.panel(ax, "B", (13.6, 8.6))
bio.label(ax, (18.3, 8.6), "Where the uncertainty comes from", size="small", bold=True)
bio.label(ax, (11.0, 0.3), "schematic: illustrative input ranges", size="tiny", color=P.muted())
