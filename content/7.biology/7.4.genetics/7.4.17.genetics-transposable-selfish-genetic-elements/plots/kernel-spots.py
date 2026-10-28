"""A developmental-timing model of McClintock's spotted kernels. The aleurone of a kernel grows from one
founder by K = 14 rounds of cell division; Ds excises from the c allele in a cell at division k with
probability eps_k, and all descendants of that cell are pigmented, giving a spot of 2^(K-k) cells.
With one dose of Ac excision can happen early (eps = 1.5e-3 at every division); with two doses it is
delayed to late divisions (here only from division 9 on, at a higher rate), so spots are smaller and more
numerous. A, B: one simulated kernel of each kind (spot areas to scale). C: spot-size distribution over
400 kernels of each kind with the expectation eps 2^(k-1) per division."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
K = 14


def simulate(eps):
    """Return the division index k (1..K) of each excision in one kernel; eps[k-1] per cell."""
    events = []
    clean = 1                       # cells still carrying the Ds insertion
    for k in range(1, K + 1):
        clean *= 2                  # cells after division k
        m = rng.binomial(clean, eps[k - 1])
        events += [k] * m
        clean -= m
    return events


eps1 = np.full(K, 1.5e-3)
eps2 = np.where(np.arange(1, K + 1) >= 9, 6e-3, 0.0)
fig, ax = bio.canvas(25, 8.6)
R = 3.0
for j, (eps, title, cx) in enumerate(((eps1, "A  one dose of Ac: early excisions", 4.0),
                                       (eps2, "B  two doses of Ac: late excisions", 12.0))):
    bio.label(ax, (cx - R, 8.2), title, size="small", ha="left")
    ax.add_patch(__import__("matplotlib.patches", fromlist=["Ellipse"]).Ellipse(
        (cx, 4.3), 2 * R, 2.3 * R, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=1.2, zorder=3))
    ev = simulate(eps)
    for k in ev:
        area = 2.0 ** (K - k) / 2 ** K * np.pi * R * R * 1.15
        r = np.sqrt(area / np.pi)
        while True:
            x, y = rng.uniform(-1, 1, 2)
            if x * x + y * y < 0.85:
                break
        ax.add_patch(__import__("matplotlib.patches", fromlist=["Circle"]).Circle(
            (cx + x * R, 4.3 + y * 1.15 * R), max(r, 0.035), facecolor=P.fill("protein"),
            edgecolor=P.edge("protein"), lw=0.4, zorder=4))
    bio.label(ax, (cx, 0.35), f"{len(ev)} spots", size="tiny", color=P.muted())
pax = charts.axes_at(ax, (18.0, 1.2, 6.5, 6.4))
bins = np.arange(0, K)
for eps, tok, lab, off in ((eps1, "dna", "one Ac", -0.18), (eps2, "receptor", "two Ac", 0.18)):
    counts = np.zeros(K)
    for _ in range(400):
        for k in simulate(eps):
            counts[K - k] += 1
    pax.bar(np.arange(K) + off, counts / 400, width=0.36, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, label=lab)
    expct = [eps[k - 1] * 2 ** (k - 1) * 2 for k in range(K, 0, -1)]
    pax.plot(np.arange(K) + off, expct, "_", color=P.edge(tok), ms=8)
pax.set_yscale("log")
pax.set_ylim(1e-3, 300)
pax.set_xticks(range(0, K, 2), [f"{2 ** i}" for i in range(0, K, 2)])
charts.style_axes(pax, "spot size / cells", "spots per kernel")
charts.title(pax, "C  spot sizes")
pax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
