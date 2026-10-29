"""Two titration models of the timing of the mid-blastula transition. A: a maternal repressor of fixed total
amount R binds sites on the DNA, whose number doubles at every cleavage; zygotic transcription (the fraction
of promoters free of repressor) switches on when the free repressor falls below its dissociation constant.
Haploid embryos reach the threshold one cycle later and tetraploid embryos one cycle earlier, as in the
experiments on Xenopus. B: if a maternal replication factor can serve only a fixed amount of DNA, S phase
lengthens once the DNA content exceeds that capacity, and the cleavage cycle slows at the same ratio of DNA
to cytoplasm. Units are schematic (R = 1000 in units of the dissociation constant; capacity reached at cycle
12 in diploids)."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(21, 8.4)
n = np.linspace(6, 16, 400)
R = 1000.0
s = 2 * (R - 1) / (2 * 2**12)  # sites per haploid genome per nucleus: diploid crosses at cycle 12
cols = {1: "receptor", 2: "dna", 4: "positive"}
names = {1: "haploid", 2: "diploid", 4: "tetraploid"}

a = charts.axes_at(ax, (1.6, 1.5, 7.8, 5.6))
for p in (1, 2, 4):
    S = p * s * 2**n
    b = 1 + S - R
    rf = (-b + np.sqrt(b**2 + 4 * R)) / 2
    act = 1 / (1 + rf)
    a.plot(n, act, color=charts.line(cols[p]), lw=1.8)
    k = np.argmin(abs(act - 0.5))
    a.plot([n[k]], [0.5], "o", color=charts.line(cols[p]), ms=4)
    dx, dy, ha = {1: (0.3, -0.2, "left"), 2: (0.3, -0.06, "left"), 4: (-0.3, 0.1, "right")}[p]
    a.text(n[k] + dx, 0.5 + dy, f"{names[p]}: cycle {n[k]:.0f}", color=charts.line(cols[p]), fontsize=7, va="center", ha=ha)
a.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.set_xlim(6, 16)
a.set_ylim(0, 1.02)
charts.style_axes(a, "cleavage cycle n", "fraction of promoters free of repressor")
charts.title(a, "A  Repressor titrated by the DNA")

b_ = charts.axes_at(ax, (12.4, 1.5, 7.8, 5.6))
nn = np.arange(1, 17)
TS, TM, F = 20.0, 10.0, 2 * 2**12
for p in (1, 2, 4):
    T = TS * np.maximum(1, p * 2.0**nn / F) + TM
    b_.plot(nn, T, "-o", color=charts.line(cols[p]), lw=1.5, ms=3, label=names[p])
b_.set_yscale("log")
b_.set_ylim(20, 700)
b_.set_xlim(1, 16.5)
b_.set_yticks([30, 60, 120, 240, 480])
b_.set_yticklabels(["30", "60", "120", "240", "480"])
charts.style_axes(b_, "cleavage cycle n", "cycle length / min (model)")
charts.title(b_, "B  Limiting replication factor")
leg = b_.legend(fontsize=7, frameon=False, loc="upper left")
for t in leg.get_texts():
    t.set_color(P.ink())
