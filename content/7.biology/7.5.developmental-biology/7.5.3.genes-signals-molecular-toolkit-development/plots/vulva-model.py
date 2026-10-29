"""Vulval induction in C. elegans: a graded paracrine signal combined with juxtacrine lateral signalling.

Model (dimensionless). Six vulval precursor cells P3.p-P8.p (index i = 3..8) lie below the gonad; the anchor
cell above P6.p secretes LIN-3 (EGF), whose level at cell i is s_i = s0 exp(-|i - 6| / lam). Each cell has a
level a_i of the primary (1 deg) program, driven by LET-23 (EGF receptor) - Ras - MAPK signalling, and it
receives a lateral signal n_i = a_{i-1} + a_{i+1} from its neighbours through LIN-12 (Notch), because
cells adopting the 1 deg fate express Delta-like ligands. LIN-12 signalling represses the 1 deg program:
    da_i/dt = h(s_i) / (1 + (n_i / Kn)^2) - a_i,    h(s) = s^4 / (K^4 + s^4),
with K = 0.35, Kn = 0.3. Fate: 1 deg if a_i > 0.5; otherwise 2 deg if n_i > 0.4 (and LIN-12 works);
otherwise 3 deg (the cell fuses with the epidermis). The initial a_i carry 1 % noise (fixed seed).
Rows: wild type (s0 = 1, lam = 0.7) gives 3 3 2 1 2 3; anchor cell ablated (s0 = 0): all 3 deg;
lin-12 loss of function: 3 3 3 1 3 3 (no 2 deg fates); lin-12 gain of function (n_i fixed high): all 2 deg;
LIN-3 overexpressed uniformly (s_i = 2): alternating 1 deg and 2 deg fates set by lateral inhibition;
LIN-3 overexpressed in a lin-12 mutant: all 1 deg.
"""

import numpy as np

import wikibio as bio
from wikibio import development as D
from wikibio import quant

P = bio.P
K, KN = 0.35, 0.3
idx = np.arange(3, 9)


def run(s, lin12="wt", T=60.0, dt=0.02, seed=1):
    rng = np.random.default_rng(seed)
    a = 0.01 * (1 + rng.standard_normal(6))
    hs = s**4 / (K**4 + s**4)
    for _ in range(int(T / dt)):
        n = np.r_[0, a[:-1]] + np.r_[a[1:], 0]
        if lin12 == "lf":
            n = 0 * n
        elif lin12 == "gf":
            n = np.full(6, 3.0)
        a = a + dt * (hs / (1 + (n / KN) ** 2) - a)
    n = np.r_[0, a[:-1]] + np.r_[a[1:], 0]
    if lin12 == "gf":
        n = np.full(6, 3.0)
    fate = []
    for i in range(6):
        if a[i] > 0.5:
            fate.append(0)
        elif lin12 != "lf" and n[i] > 0.4:
            fate.append(1)
        else:
            fate.append(2)
    return fate


wt = np.exp(-np.abs(idx - 6) / 0.7)
conds = [("wild type", wt, "wt"), ("anchor cell ablated", 0 * wt, "wt"), ("lin-12 loss of function", wt, "lf"),
         ("lin-12 gain of function", wt, "gf"), ("LIN-3 overexpressed", np.full(6, 2.0), "wt"),
         ("LIN-3 overexpressed, lin-12 loss", np.full(6, 2.0), "lf")]
FT = ["dna", "receptor", "neutral"]
NAMES = ["1°", "2°", "3°"]

fig, ax = bio.canvas(26, 14.6)
# top: anchor cell and LIN-3 profile
x0, x1 = 7.0, 19.0
cw = (x1 - x0) / 6
p = quant.Plot(ax, (x0, 11.1, x1 - x0, 2.2), xlim=(2.5, 8.5), ylim=(0, 1.1), ylabel="LIN-3 at cell", yticks=[0, 1], frame="l")
xs = np.linspace(2.5, 8.5, 200)
p.line(xs, np.exp(-np.abs(xs - 6) / 0.7), "highlight")
ac = (x0 + 3.5 * cw, 14.0)
bio.box(ax, ac, 1.4, 0.6, "highlight", text="anchor cell", size="tiny")
for k, i in enumerate(idx):
    bio.label(ax, (x0 + (k + 0.5) * cw, 10.7), f"P{i}.p", size="tiny", color=P.muted())
for r, (name, s, l12) in enumerate(conds):
    y = 9.6 - r * 1.55
    f = run(s, l12)
    cells = D.cell_row(ax, x0, x1, y, f, FT, h=0.9)
    for (cx, cy), fi in zip(cells, f):
        bio.label(ax, (cx + 0.55, cy + 0.2), NAMES[fi], size="tiny", color=P.on_fill())
    bio.label(ax, (x0 - 0.3, y), name.replace("lin-12", r"$\it{lin}$-$\it{12}$"), size="small", ha="right")
# legend
for k, (tok, txt) in enumerate(zip(FT, ("1° (vulva centre)", "2° (vulva flanks)", "3° (fuses with epidermis)"))):
    bio.box(ax, (20.2, 8.6 - k * 0.8), 0.55, 0.45, tok)
    bio.label(ax, (20.7, 8.6 - k * 0.8), txt, size="tiny", ha="left")
bio.label(ax, (22.6, 5.2), "LIN-3 (EGF) from the anchor cell\ninduces 1°; 1° cells signal\nlaterally through LIN-12 (Notch),\nwhich induces 2° and blocks 1°",
          size="tiny", color=P.muted())
