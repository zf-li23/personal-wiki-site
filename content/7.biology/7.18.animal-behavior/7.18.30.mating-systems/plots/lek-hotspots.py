"""The hotspot model of lek formation (Bradbury and colleagues 1986), simulated.

Forty females each have a nest site and a foraging site (two different clusters in a 10 x 10 km landscape) and
travel between them along straight routes. The density of female movements, accumulated on a grid, is high
where routes converge (A, shading). Twelve males settle in turn on the free cell with the highest female
traffic, at least 0.4 km from any other male (dots): they aggregate where females pass, without any benefit of
aggregation itself. B: expected female encounters per male, in rank order. The skew is modest: hotspots can
explain why males cluster, but not the extreme skew in mating success observed on real leks, which requires
female choice among the clustered males.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(7)
n_f = 40
nests = rng.normal([2.5, 7.0], [1.0, 1.2], (n_f, 2))
food = np.vstack([rng.normal([7.5, 7.5], 0.6, (n_f // 2, 2)), rng.normal([7.0, 2.5], 0.7, (n_f // 2, 2))])
rng.shuffle(food)
g = 100
H = np.zeros((g, g))
for a, b in zip(nests, food):
    t = np.linspace(0, 1, 400)
    pts = a + np.outer(t, b - a)
    idx = np.clip((pts / 10 * g).astype(int), 0, g - 1)
    cells = {tuple(i) for i in idx}
    for i, j in cells:
        H[j, i] += 1
from numpy.lib.stride_tricks import sliding_window_view as swv  # noqa: E402
pad = np.pad(H, 2)
Hs = swv(pad, (5, 5)).mean(axis=(2, 3))

males = []
order = np.dstack(np.unravel_index(np.argsort(-Hs, axis=None), Hs.shape))[0]
for j, i in order:
    p = np.array([(i + 0.5) / g * 10, (j + 0.5) / g * 10])
    if all(np.hypot(*(p - m)) > 0.4 for m in males):
        males.append(p)
    if len(males) == 12:
        break
males = np.array(males)
enc = np.array([Hs[int(m[1] / 10 * g), int(m[0] / 10 * g)] for m in males])

fig, ax = bio.canvas(28.0, 11.0)
pa = Ch.axes_at(ax, (2.0, 1.4, 8.6, 8.6))
pa.imshow(Hs, origin="lower", extent=(0, 10, 0, 10), cmap=LinearSegmentedColormap.from_list("traffic", [P.surface(), P.muted()]), interpolation="bilinear")
pa.plot(nests[:, 0], nests[:, 1], "^", color=Ch.line("rna"), ms=4, label="female nests")
pa.plot(food[:, 0], food[:, 1], "s", color=Ch.line("plant"), ms=3.5, label="foraging sites")
pa.plot(males[:, 0], males[:, 1], "o", color=Ch.line("dna"), ms=6, mec=P.surface(), label="settled males")
pa.set_xlim(0, 10)
pa.set_ylim(0, 10)
pa.set_aspect("equal")
Ch.style_axes(pa, "x / km", "y / km", box=True)
Ch.title(pa, "Males settle where female routes converge")
leg = pa.legend(fontsize=FS["tiny"], frameon=True, loc="lower left", facecolor=P.surface(), edgecolor=P.muted())
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "A", (0.2, 10.8))

pb = Ch.axes_at(ax, (16.0, 1.4, 10.8, 8.6))
share = np.sort(enc)[::-1] / enc.sum() * 100
pb.bar(np.arange(1, 13), share, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.7)
pb.set_xticks(np.arange(1, 13))
Ch.style_axes(pb, "males in rank order", "share of female encounters / %")
Ch.title(pb, "Encounters per male: only modest skew")
bio.panel(ax, "B", (14.2, 10.8))
