# Crossover interference under the chi-square (gamma renewal) model compared with the Poisson model
import numpy as np
import wikibio as bio
from wikibio import charts, transmission as T

rng = np.random.default_rng(0)
fig, ax = bio.canvas(24, 8.4)
L = 1.0  # morgans
cols = {1: "dna", 4: "receptor"}

for k, nu in enumerate((1, 4)):
    a = charts.axes_at(ax, (1.2 + k * 4.6, 1.3, 3.8, 5.8))
    ch = T.chiasma_process(25, L, nu, rng)
    for i, c in enumerate(ch):
        a.plot([0, 100], [i, i], color=charts.line("neutral"), lw=0.5)
        a.plot(c * 100, np.full(len(c), i), "|", color=charts.line(cols[nu]), ms=6, mew=1.6)
    a.set_xlim(0, 100)
    a.set_ylim(-1, 25)
    a.set_yticks([])
    charts.style_axes(a, "position / cM", "meiosis" if k == 0 else None)
    charts.title(a, ("A   " if k == 0 else "") + ("Poisson, nu = 1" if nu == 1 else "gamma, nu = 4"))

# B: coincidence between two 5 cM intervals as a function of separation
a = charts.axes_at(ax, (11.6, 1.3, 5.2, 5.8))
seps = np.arange(5, 60, 2.5) / 100
N = 60000
for nu in (1, 4):
    ch = T.chiasma_process(N, L, nu, np.random.default_rng(nu))
    idx = np.concatenate([np.full(len(c), i) for i, c in enumerate(ch)])
    pos = np.concatenate(ch)
    keep = rng.random(len(pos)) < 0.5  # chiasmata involving one random chromatid
    idx, pos = idx[keep], pos[keep]

    def parity(lo, hi):
        cnt = np.zeros(N, int)
        sel = (pos > lo) & (pos < hi)
        np.add.at(cnt, idx[sel], 1)
        return cnt % 2

    r1 = parity(0.2, 0.25)
    C = []
    for s in seps:
        r2 = parity(0.2 + s, 0.25 + s)
        C.append(np.mean(r1 * r2) / (np.mean(r1) * np.mean(r2)))
    a.plot(seps * 100, C, "o-", color=charts.line(cols[nu]), ms=3, lw=1.5, label=f"nu = {nu}")
a.axhline(1, color=charts.line("neutral"), lw=0.8, ls=":")
a.set_ylim(0, 1.6)
charts.style_axes(a, "distance between interval centres / cM", "coefficient of coincidence C")
leg = a.legend(frameon=False, fontsize=8, loc="lower right")
for t in leg.get_texts():
    t.set_color(bio.P.ink())
charts.title(a, "B   coincidence")

# C: number of chiasmata per bivalent
a = charts.axes_at(ax, (18.6, 1.3, 4.8, 5.8))
ks = np.arange(0, 7)
for j, nu in enumerate((1, 4)):
    ch = T.chiasma_process(20000, L, nu, np.random.default_rng(10 + nu))
    cnt = np.bincount([len(c) for c in ch], minlength=10)[:7] / len(ch)
    a.bar(ks + (j - 0.5) * 0.38, cnt, width=0.38, color=bio.P.fill(cols[nu]), edgecolor=bio.P.edge(cols[nu]), lw=0.6,
          label=f"nu = {nu}")
a.set_xticks(ks)
charts.style_axes(a, "chiasmata per bivalent", "proportion")
leg = a.legend(frameon=False, fontsize=8)
for t in leg.get_texts():
    t.set_color(bio.P.ink())
charts.title(a, "C   chiasma counts")
