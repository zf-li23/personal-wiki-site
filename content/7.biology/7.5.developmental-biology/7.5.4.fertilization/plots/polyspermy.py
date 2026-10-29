"""Sperm arrival as a Poisson process: why eggs need fast blocks to polyspermy.

Fusion-competent sperm reach the egg membrane at random times at rate lam (per second). After the first
fusion at time t1, a second sperm can still fuse until a block takes effect. Slow block only, effective after
T = 60 s: P(poly) = 1 - exp(-lam T). Fast plus slow block: the membrane depolarizes after delta = 1 s and
reduces the fusion rate to eps * lam (eps = 0.01) until the slow block is complete at T:
P(poly) = 1 - exp(-lam delta - eps lam (T - delta)).
A: probability of polyspermy against the arrival rate. B: an egg exposed to sperm for W = 300 s is
fertilized with probability 1 - exp(-lam W) and is fertilized by exactly one sperm with probability
(1 - exp(-lam W)) exp(-lam delta - eps lam (T - delta)) (fast block) or (1 - exp(-lam W)) exp(-lam T)
(slow block only): monospermy is maximal at an intermediate sperm density, and the fast block widens the
range of densities at which most eggs are fertilized normally by about two orders of magnitude.
"""

import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27, 10.0)
lam = np.geomspace(1e-4, 10, 300)
T, d, eps, W = 60.0, 1.0, 0.01, 300.0

bio.panel(ax, "A", (0.2, 9.9))
pa = quant.Plot(ax, (2.3, 1.5, 9.6, 7.6), xlim=(1e-4, 10), ylim=(0, 1), xlog=True, xlabel="sperm arrival rate λ / s⁻¹",
                ylabel="P(polyspermy)", xticks=[(1e-4, "10⁻⁴"), (1e-3, "10⁻³"), (1e-2, "10⁻²"), (1e-1, "0.1"), (1, "1"), (10, "10")],
                yticks=[0, 0.5, 1], grid=True)
pa.line(lam, 1 - np.exp(-lam * T), "highlight")
pa.line(lam, 1 - np.exp(-lam * d - eps * lam * (T - d)), "dna")
pa.text(2.2e-3, 0.3, "slow block\nonly (60 s)", token="highlight", ha="left")
pa.text(1.6, 0.45, "fast (1 s)\n+ slow\nblock", token="dna", ha="left")

bio.panel(ax, "B", (13.8, 9.9))
pb = quant.Plot(ax, (15.9, 1.5, 9.6, 7.6), xlim=(1e-4, 10), ylim=(0, 1), xlog=True, xlabel="sperm arrival rate λ / s⁻¹",
                ylabel="probability", xticks=[(1e-4, "10⁻⁴"), (1e-3, "10⁻³"), (1e-2, "10⁻²"), (1e-1, "0.1"), (1, "1"), (10, "10")],
                yticks=[0, 0.5, 1], grid=True)
fert = 1 - np.exp(-lam * W)
pb.line(lam, fert, "muted", dashed=True)
pb.line(lam, fert * np.exp(-lam * T), "highlight")
pb.line(lam, fert * np.exp(-lam * d - eps * lam * (T - d)), "dna")
pb.text(3e-4, 0.9, "fertilized (any)", color=P.muted(), ha="left")
pb.text(2.5e-2, 0.12, "monospermic,\nslow block only", token="highlight", ha="left")
pb.text(0.12, 0.62, "monospermic,\nfast + slow", token="dna", ha="left")
