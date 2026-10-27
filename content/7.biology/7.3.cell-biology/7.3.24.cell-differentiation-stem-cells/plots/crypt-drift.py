"""Neutral drift of stem-cell clones in the intestinal crypt (after Lopez-Garcia and colleagues 2010; Snippert
and colleagues 2010).

Model: N = 16 equipotent stem cells sit on a ring at the crypt base. Each stem cell is lost (pushed out of
the niche to differentiate) at rate lambda = 1 per day and is replaced by the division of one of its two
neighbours, chosen at random. A clone labelled in one stem cell then stays contiguous and its size n
(number of labelled stem cells) performs a symmetric random walk, n -> n + 1 and n -> n - 1 each at rate
lambda, absorbed at n = 0 (clone lost) and n = N (crypt monoclonal). A: snapshots of one simulated crypt
base (labelled cells dark). B: fraction of crypts that still contain the clone, and fraction that have become
monoclonal, among 20000 simulated crypts; the monoclonal fraction tends to 1/N = 6.25 %, the probability that
a given stem cell's progeny takes over the crypt, and the conditional time to monoclonality is
(N^2 - 1) / (6 lambda), about 42 days here. C: distribution of clone size among surviving, not yet monoclonal
clones at 7, 21 and 63 days: the clones that survive grow, and the distribution broadens, as expected for
neutral competition rather than fixed asymmetric divisions (which would keep every clone at one cell).
"""

import numpy as np
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts, quant

P = bio.P
rng = np.random.default_rng(5)
N, lam, crypts, dt, T = 16, 1.0, 20000, 0.01, 120.0
n = np.ones(crypts, dtype=int)
ts, alive, mono, snaps = [], [], [], {}
steps = int(T / dt)
for i in range(steps + 1):
    t = i * dt
    if i % 50 == 0:
        ts.append(t)
        alive.append(np.mean(n > 0))
        mono.append(np.mean(n == N))
    for d in (7, 21, 63):
        if abs(t - d) < dt / 2:
            snaps[d] = n.copy()
    active = (n > 0) & (n < N)
    u = rng.random(crypts)
    up = active & (u < lam * dt)
    down = active & (u >= lam * dt) & (u < 2 * lam * dt)
    n = n + up - down

fig, ax = bio.canvas(28.0, 9.6)
bio.panel(ax, "A", (0.1, 9.5))

# one crypt history for the snapshots (ring with contiguous clone)
hist = [1]
m = 1
r2 = np.random.default_rng(11)
while 0 < m < N:
    m += 1 if r2.random() < 0.5 else -1
    hist.append(m)
while hist[-1] == 0:  # find a history that fixes, for the illustration
    hist, m = [1], 1
    while 0 < m < N:
        m += 1 if r2.random() < 0.5 else -1
        hist.append(m)
show = [0, len(hist) // 3, 2 * len(hist) // 3, len(hist) - 1]
for k, j in enumerate(show):
    cx, cy = 1.5 + 2.3 * k, 5.4
    nk = hist[j]
    for c in range(N):
        ang = 2 * np.pi * c / N
        lab = c < nk
        ax.add_patch(Circle((cx + 0.78 * np.cos(ang), cy + 0.78 * np.sin(ang)), 0.17,
                            facecolor=P.fill("drug") if lab else P.fill("cytoplasm"),
                            edgecolor=P.edge("drug") if lab else P.edge("membrane"), lw=0.8, zorder=5))
    bio.label(ax, (cx, cy), f"{nk}/{N}", size="tiny")
    bio.label(ax, (cx, cy - 1.4), f"event {j}", size="tiny", color=P.muted())
bio.label(ax, (4.8, 7.4), "Stem-cell ring at the crypt base (one crypt)", size="tiny")
bio.label(ax, (4.8, 2.9), "Each loss is replaced by a neighbour's division:\nthe labelled clone drifts until lost or fixed",
          size="tiny", color=P.muted())

bio.panel(ax, "B", (9.8, 9.5))
pb = charts.axes_at(ax, (11.2, 1.4, 6.6, 7.4))
pb.plot(ts, alive, color=quant.line_color("drug"), lw=2.0, label="crypts containing the clone")
pb.plot(ts, mono, color=quant.line_color("positive"), lw=2.0, label="monoclonal crypts")
pb.axhline(1 / N, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pb.text(80, 1 / N + 0.02, "1/N", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_xlim(0, T)
pb.set_ylim(0, 1.02)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "time after labelling / days", "fraction of crypts")
charts.title(pb, "Clones are lost or take over")

bio.panel(ax, "C", (19.4, 9.5))
pc = charts.axes_at(ax, (20.8, 1.4, 6.8, 7.4))
sizes = np.arange(1, N)
for d, tk in ((7, "channel"), (21, "drug"), (63, "protein")):
    s = snaps[d]
    s = s[(s > 0) & (s < N)]
    freq = np.array([(s == k).mean() for k in sizes])
    pc.plot(sizes, freq, color=quant.line_color(tk), lw=1.8, marker="o", ms=3, label=f"day {d}")
pc.set_xlim(1, N - 1)
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pc, "clone size n (stem cells)", "fraction of surviving clones")
charts.title(pc, "Surviving clones grow and spread")
