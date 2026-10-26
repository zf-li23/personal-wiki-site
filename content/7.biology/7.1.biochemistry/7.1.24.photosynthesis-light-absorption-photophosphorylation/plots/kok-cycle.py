"""The Kok cycle of the oxygen-evolving complex. (A) Each photochemical turnover of PSII removes one electron
from the Mn4CaO5 cluster (through TyrZ), advancing it through the S states S0 -> S1 -> S2 -> S3 -> (S4) -> S0;
O2 is released in the S3 -> S4 -> S0 transition, and protons are released into the lumen in the pattern
1, 0, 1, 2. The dark-stable states are S1 (about 75%) and S0 (25%). (B) Oxygen evolved per flash in a train
of short saturating flashes given to dark-adapted thylakoids (Joliot's experiment), simulated with the Kok
model: on each flash a center advances by one state with probability 1 - alpha - beta, fails ("miss") with
probability alpha = 0.10, or advances two states ("double hit") with probability beta = 0.04. Yields peak on
flashes 3, 7, 11, ... with period four and damp to the steady-state value as the population dephases."""

import math

import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(20.0, 8.4)

# ---- A: the cycle ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.3))
c, r = (4.3, 4.3), 2.4
names = ["S₀", "S₁", "S₂", "S₃", "S₄"]
angles = [90, 18, -54, -126, -198]  # clockwise, S4 between S3 and S0
pts = [(c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a))) for a in angles]
toks = ["enzyme", "positive", "enzyme", "enzyme", "neutral"]
for p, n, t in zip(pts, names, toks):
    bio.molecule(ax, p, token=t, text=n, r=0.45, size="normal")
protons = ["1 H⁺", "0", "1 H⁺", "2 H⁺ + O₂", ""]
for k in range(5):
    a, b = np.array(pts[k]), np.array(pts[(k + 1) % 5])
    mid_angle = math.radians((angles[k] + (angles[k + 1] if k < 4 else angles[0] - 360)) / 2)
    d = (b - a) / np.linalg.norm(b - a)
    bio.arrow(ax, a + d * 0.55, b - d * 0.55, kind="process", color=P.ink(), lw=1.4, head=0.2, bend=-0.18)
    if k < 4:
        m = (a + b) / 2
        out = np.array([math.cos(mid_angle), math.sin(mid_angle)])
        ps.photon(ax, m + out * 1.25 + np.array([0.0, 0.2]), m + out * 0.45, text=None, waves=2, amp=0.08)
lab = [(0, "+1 H⁺"), (2, "+1 H⁺"), (3, "+2 H⁺")]
for k, t in lab:
    a, b = np.array(pts[k]), np.array(pts[(k + 1) % 5])
    m = (a + b) / 2
    v = (m - np.array(c)) / np.linalg.norm(m - np.array(c))
    bio.label(ax, m - v * 0.8, t, size="tiny", color=P.edge("h"))
bio.label(ax, (pts[4][0] - 0.1, pts[4][1] - 0.85), "O₂ released\n(S₄ → S₀, fast)", size="tiny", color=P.ink())
bio.label(ax, c, "Mn₄CaO₅", size="small", bold=True, color=P.muted())
bio.label(ax, (4.3, 0.6), "one hν (one e⁻ to P680⁺ via Tyr Z) per step; dark-stable: S₁", size="tiny", color=P.muted())

# ---- B: flash yields ----------------------------------------------------------------------------------
bio.panel(ax, "B", (9.0, 8.3))


def flashes(alpha, beta, n=20):
    T = np.zeros((4, 4))
    for st in range(4):
        T[st, st] += alpha
        T[(st + 1) % 4, st] += 1 - alpha - beta
        T[(st + 2) % 4, st] += beta
    pop = np.array([0.25, 0.75, 0.0, 0.0])
    out = []
    for _ in range(n):
        out.append((1 - alpha - beta) * pop[3] + beta * (pop[2] + pop[3]))  # S3 -> S0, or a double hit through S4
        pop = T @ pop
    return np.array(out) / 0.25


yields = flashes(0.10, 0.04)
ideal = flashes(0.0, 0.0)
b = charts.axes_at(ax, (10.6, 1.4, 8.8, 6.0))
n = np.arange(1, 21)
b.bar(n, yields, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), width=0.7, label="Kok model, α = 0.10, β = 0.04")
b.plot(n[ideal > 0], ideal[ideal > 0], "o", color=charts.line("negative"), ms=4, label="no misses or double hits")
b.axhline(1.0, color=P.muted(), lw=0.8, ls="--")
b.set_xticks([1, 3, 7, 11, 15, 19])
b.set_xlim(0.3, 20.7)
b.set_ylim(0, 4.0)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "flash number", "O₂ per flash / steady-state yield")
