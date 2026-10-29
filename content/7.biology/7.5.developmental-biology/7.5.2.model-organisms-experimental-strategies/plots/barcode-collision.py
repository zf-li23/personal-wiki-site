"""When do two clones share a label by chance? The birthday problem of lineage tracing.

A: probability that at least two of n independently labelled clones carry the same label when each label is
drawn uniformly from N possibilities: 1 - prod_{k<n} (1 - k/N), close to 1 - exp(-n(n-1)/2N). N = 4
(the four colours of a Confetti/Brainbow reporter), 100, 10^4 and 10^6. The dashed line marks 50 %,
reached near n = 1.18 sqrt(N). B: with unequal label frequencies p_i the relevant number is the
effective diversity N_eff = 1 / sum p_i^2. For 10^4 possible barcodes whose frequencies follow a Zipf law
(p_i proportional to 1/i, as edit outcomes of CRISPR arrays roughly do), N_eff is only about 58, and
collisions become likely with about ten clones (curve,
from 1 - exp(-n(n-1)/2N_eff)), compared with the uniform case (dashed).
"""

import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27, 10.0)


def p_collide(n, N):
    n = np.asarray(n, float)
    out = []
    for m in n:
        k = np.arange(int(m))
        out.append(1 - np.exp(np.sum(np.log1p(-np.minimum(k / N, 1 - 1e-15)))) if m <= N + 1 else 1.0)
    return np.array(out)


bio.panel(ax, "A", (0.2, 9.9))
pa = quant.Plot(ax, (2.2, 1.5, 9.8, 7.6), xlim=(1, 1e4), ylim=(0, 1), xlog=True, xlabel="number of labelled clones n",
                ylabel="P(at least one shared label)", xticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "1000"), (1e4, "10⁴")],
                yticks=[0, 0.5, 1], grid=True)
ns = np.unique(np.geomspace(1, 1e4, 120).astype(int))
for N, tok, lab in ((4, "negative", "N = 4"), (100, "highlight", "N = 100"), (1e4, "enzyme", "N = 10⁴"), (1e6, "dna", "N = 10⁶")):
    y = p_collide(ns, N)
    k = np.searchsorted(y, 0.5)
    pa.line(ns, y, tok)
    pa.text(ns[min(k, len(ns) - 1)] * 1.25, 0.42, lab, token=tok, ha="left")
pa.hline(0.5)

bio.panel(ax, "B", (13.8, 9.9))
M = 10_000
w = 1 / np.arange(1, M + 1)
p = w / w.sum()
Neff = 1 / np.sum(p**2)
pb = quant.Plot(ax, (15.8, 1.5, 9.8, 7.6), xlim=(1, 1000), ylim=(0, 1), xlog=True, xlabel="number of labelled clones n",
                ylabel="P(at least one shared label)", xticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "1000")],
                yticks=[0, 0.5, 1], grid=True)
ns2 = np.unique(np.geomspace(1, 1000, 80).astype(int))
# for unequal frequencies: P(collision) ~ 1 - exp(-n(n-1)/2 * sum p_i^2) = 1 - exp(-n(n-1)/(2 N_eff))
zipf = 1 - np.exp(-ns2 * (ns2 - 1) / (2 * Neff))
pb.line(ns2, zipf, "drug")
pb.text(14, 0.42, f"Zipf frequencies, 10⁴ barcodes\n(N_eff ≈ {Neff:.0f})", token="drug", ha="left")
pb.line(ns2, p_collide(ns2, M), "enzyme", dashed=True)
pb.text(160, 0.3, "uniform,\n10⁴ barcodes", token="enzyme", ha="left")
pb.hline(0.5)
