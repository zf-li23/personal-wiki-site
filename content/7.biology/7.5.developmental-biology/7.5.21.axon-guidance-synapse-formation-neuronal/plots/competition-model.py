"""Competition for a neurotrophic factor can eliminate all but one input (Formula 21.7.1, a simplified version of
the model of van Ooyen and Willshaw 1999). Five axons innervate one target, which releases a neurotrophin at rate
sigma; the neurotrophin is degraded and taken up by the axons in proportion to their size, and each axon grows at a
rate that depends cooperatively on its uptake and is lost at a constant rate. (A) At low release rate one axon,
initially only slightly larger than the others, takes over the target and the others retract: single innervation,
as at the adult neuromuscular junction. (B) At high release rate all axons survive and coexist (multiple
innervation). (C) Number of surviving axons after a long time as a function of the release rate: the number of
inputs the target can support rises with its supply of neurotrophin, and below a minimum supply none survives."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
al, K, th, ga, de, be = 1.0, 1.0, 0.5, 0.1, 0.1, 0.2


def run(sigma, n=5, T=600.0, dt=0.02, seed=0, keep=True):
    """Integrate for one release rate or for an array of them at once (rows = release rates)."""
    rng = np.random.default_rng(seed)
    sigma = np.atleast_1d(np.asarray(sigma, float))[:, None]
    a = np.tile(1 + 0.05 * rng.standard_normal(n), (sigma.shape[0], 1))
    N = np.ones_like(sigma)
    hist = []
    for k in range(int(T / dt)):
        f = N / (K + N)
        u = a * f                                   # uptake by each axon
        a = np.maximum(a + dt * (al * u ** 2 / (th ** 2 + u ** 2) - ga * a), 0.0)
        N = N + dt * (sigma - de * N - be * f * a.sum(1, keepdims=True))
        if keep and k % 25 == 0:
            hist.append(a[0].copy())
    return np.array(hist), a


toks = ["receptor", "enzyme", "antibody", "dna", "k"]
fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.6))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.87, wspace=0.32)
for ax, sigma, title in ((axs[0], 0.2, "A  Low supply: one survivor"), (axs[1], 2.0, "B  High supply: all survive")):
    h, _ = run(sigma)
    t = np.arange(len(h)) * 25 * 0.02
    for i in range(h.shape[1]):
        ax.plot(t, h[:, i], color=charts.line(toks[i]), lw=1.5)
    charts.style_axes(ax, "time", "axon size (receptor amount)")
    charts.title(ax, title)
sig = np.linspace(0.1, 1.6, 16)
surv = (run(sig, keep=False, T=1500.0)[1] > 0.5).sum(1)
axs[2].step(sig, surv, where="mid", color=charts.line("protein"), lw=1.6)
axs[2].plot(sig, surv, "o", color=charts.line("protein"), ms=4)
axs[2].set_yticks(range(0, 6))
charts.style_axes(axs[2], "neurotrophin release rate", "surviving axons")
charts.title(axs[2], "C  Survivors versus supply")
