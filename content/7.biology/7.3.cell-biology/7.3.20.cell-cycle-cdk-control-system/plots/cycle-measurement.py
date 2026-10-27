"""Measuring the cell cycle in an asynchronous population (simulation).

A population of cells proliferates asynchronously with mean phase durations G1 = 11 h, S = 8 h, G2 = 4 h
and M = 1 h (cycle time 24 h); each phase of each cell cycle is drawn independently from a gamma distribution
with a coefficient of variation of 0.15, and the population is grown for 120 h before measurement so that its
age structure is stable.
(A) DNA content measured by flow cytometry (DNA dye, 2C = unreplicated diploid content). DNA content rises
linearly through S; the measurement adds Gaussian noise with a coefficient of variation of 4%. Shaded areas:
the contributions of G1, S and G2 + M cells. For exponential growth with no variation, the fractions are
2(1 - 2^(-a1/T)) - 2(1 - 2^(-a0/T)) for a phase spanning ages a0..a1, giving G1 : S : G2+M of about
0.54 : 0.30 : 0.15; more cells are young than old, so G1 is over-represented relative to its share of T.
(B) The percent-labeled-mitoses method: a brief pulse of labeled thymidine (or EdU) at t = 0 marks the cells
in S; the fraction of mitotic cells that are labeled is then followed over time. Labeled mitoses first appear
after the shortest G2; the curve reaches 50% at about TG2 + TM/2, stays high for about TS, and the second
wave follows one cycle time TC after the first.
"""

import heapq

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

MEAN = np.array([11.0, 8.0, 4.0, 1.0])  # G1, S, G2, M (h)
CV = 0.15
k = 1 / CV**2


def durations():
    return rng.gamma(k, MEAN / k)


# event-driven growth of a population from 300 cells of random age
T_PULSE = 120.0
T_END = T_PULSE + 52.0
cells = []  # (birth, g1, s, g2, m, parent)
queue = []
for _ in range(300):
    d = durations()
    b = -rng.uniform(0, d.sum())
    cells.append((b, *d, -1))
    heapq.heappush(queue, (b + d.sum(), len(cells) - 1))
while queue:
    tdiv, i = heapq.heappop(queue)
    if tdiv > T_END:
        continue
    for _ in range(2):
        d = durations()
        cells.append((tdiv, *d, i))
        heapq.heappush(queue, (tdiv + d.sum(), len(cells) - 1))
C = np.array(cells)
birth, g1, s, g2, m, parent = C.T
parent = parent.astype(int)
e1, e2, e3, e4 = birth + g1, birth + g1 + s, birth + g1 + s + g2, birth + g1 + s + g2 + m

# ----- DNA content at the pulse time
alive = (birth <= T_PULSE) & (e4 > T_PULSE)
age = T_PULSE - birth[alive]
ph = np.select([age < g1[alive], age < (g1 + s)[alive]], [0, 1], 2)
dna = np.where(ph == 0, 2.0, np.where(ph == 1, 2.0 + 2.0 * (age - g1[alive]) / s[alive], 4.0))
meas = dna * (1 + 0.04 * rng.standard_normal(dna.size))
frac = [np.mean(ph == j) for j in range(3)]

fig, ax = bio.canvas(24.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a = charts.axes_at(ax, (1.8, 1.5, 9.0, 6.6))
bins = np.linspace(1.4, 4.8, 120)
toks = ("positive", "dna", "negative")
names = ("G1", "S", "G2 + M")
hs = [np.histogram(meas[ph == j], bins=bins)[0] for j in range(3)]
ctr = (bins[1:] + bins[:-1]) / 2
bottom = np.zeros_like(ctr)
for j in (0, 2, 1):
    a.fill_between(ctr, bottom, bottom + hs[j], step="mid", color=P.fill(toks[j]), alpha=0.75, lw=0)
    bottom = bottom + hs[j]
a.step(ctr, bottom, where="mid", color=P.ink(), lw=1.0)
for j, (x, y) in enumerate(((1.62, 0.7), (3.0, 0.22), (4.05, 0.42))):
    a.text(x, y * bottom.max(), f"{names[j]}\n{100 * frac[j]:.0f}%", ha="center", fontsize=FT["small"],
           color=charts.line(toks[j]), weight="bold")
a.set_xlim(1.4, 4.8)
a.set_xticks([2, 3, 4])
a.set_xticklabels(["2C", "3C", "4C"])
a.set_yticks([])
charts.style_axes(a, "DNA content per cell (fluorescence)", "number of cells")

# ----- percent labeled mitoses
lab0 = (e1 <= T_PULSE) & (e2 > T_PULSE)  # in S at the pulse
label = lab0.copy()
order = np.argsort(birth)
gen = np.where(lab0, 0, -1)
for i in order:  # label passes to the daughters (detectable for two divisions)
    p = parent[i]
    if p >= 0 and gen[p] >= 0 and gen[p] < 2 and birth[i] >= T_PULSE:
        gen[i] = gen[p] + 1
label = gen >= 0
ts = np.linspace(0, 50, 251)
plm = []
for t in ts:
    tt = T_PULSE + t
    mit = (e3 <= tt) & (e4 > tt)
    plm.append(100 * label[mit].mean() if mit.any() else np.nan)
plm = np.array(plm)

bio.panel(ax, "B", (12.0, 8.8))
b = charts.axes_at(ax, (13.8, 1.5, 9.6, 6.6))
b.plot(ts, plm, color=charts.line("dna"), lw=1.8)
b.axhline(50, color=P.muted(), ls=":", lw=0.8)
# idealized read-out
TG2, TM, TS, TC = MEAN[2], MEAN[3], MEAN[1], MEAN.sum()
up = TG2 + TM / 2
b.annotate("", xy=(up, 50), xytext=(0, 50), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
b.text(up / 2, 53, "TG2 + TM/2", ha="center", fontsize=FT["tiny"], color=P.muted())
b.annotate("", xy=(up + TS, 40), xytext=(up, 40), arrowprops=dict(arrowstyle="<->", color=charts.line("dna"), lw=0.8))
b.text(up + TS / 2, 33, "TS", ha="center", fontsize=FT["small"], color=charts.line("dna"))
b.annotate("", xy=(up + TC, 90), xytext=(up, 90), arrowprops=dict(arrowstyle="<->", color=charts.line("negative"), lw=0.8))
b.text(up + TC / 2, 93, "TC", ha="center", fontsize=FT["small"], color=charts.line("negative"))
b.set_xlim(0, 50)
b.set_ylim(0, 105)
charts.style_axes(b, "time after the label pulse / h", "labeled mitoses / %")
