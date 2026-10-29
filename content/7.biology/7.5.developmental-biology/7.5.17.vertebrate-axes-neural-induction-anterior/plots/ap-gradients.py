# Two posterior signals position the main subdivisions of the neural plate (Formula 17.2.1). Along a normalized
# anterior-posterior axis (0 anterior tip, 1 posterior end), retinoic acid (RA) is synthesized by Raldh2 in the
# paraxial mesoderm (0.45 < x < 0.8) and degraded by Cyp26 in the anterior neural plate (x < 0.3) and the tailbud
# (x > 0.88), which shapes it into a source-sink profile peaking in the hindbrain and anterior spinal cord; Wnt and
# FGF form a posterior gradient from the tailbud. A: steady profiles from a numerical solution. B: the domains read
# from them with fixed thresholds: forebrain where both are low, midbrain where Wnt/FGF is intermediate and RA low,
# hindbrain where RA is high, spinal cord where Wnt/FGF is high.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
N = 201
x = np.linspace(0, 1, N)
dx = x[1] - x[0]
src = ((x > 0.45) & (x < 0.8)).astype(float)
k = np.where(x < 0.3, 30.0, np.where(x > 0.88, 30.0, 1.0))
D = 0.004
A = np.zeros((N, N))
for i in range(N):
    A[i, i] = -2 * D / dx ** 2 - k[i]
    if i > 0:
        A[i, i - 1] = D / dx ** 2
    if i < N - 1:
        A[i, i + 1] = D / dx ** 2
A[0, 1] = 2 * D / dx ** 2
A[-1, -2] = 2 * D / dx ** 2
ra = np.linalg.solve(A, -src)
ra /= ra.max()
wnt = np.exp(-(1 - x) / 0.22)
fig, ax = bio.canvas(20.0, 9.6)
pa = C.axes_at(ax, (1.8, 3.6, 16.4, 5.0))
pa.axvspan(0.45, 0.8, color=P.fill("muscle"), alpha=0.18, lw=0)
pa.axvspan(0, 0.3, color=P.fill("neutral"), alpha=0.25, lw=0)
pa.axvspan(0.88, 1, color=P.fill("neutral"), alpha=0.25, lw=0)
pa.plot(x, ra, color=C.line("highlight"), lw=2.0, label="retinoic acid")
pa.plot(x, wnt, color=C.line("positive"), lw=2.0, label="Wnt / FGF")
tR, tW1, tW2 = 0.5, 0.04, 0.34
pa.axhline(tR, color=C.line("highlight"), lw=0.8, ls=(0, (3, 2)))
pa.axhline(tW1, color=C.line("positive"), lw=0.8, ls=(0, (3, 2)))
pa.axhline(tW2, color=C.line("positive"), lw=0.8, ls=(0, (1, 2)))
pa.text(0.15, 0.9, "Cyp26", fontsize=bio.core.FONT["tiny"], ha="center", color=P.muted())
pa.text(0.62, 0.9, "Raldh2 (paraxial mesoderm)", fontsize=bio.core.FONT["tiny"], ha="center", color=P.muted())
pa.text(0.94, 0.9, "Cyp26", fontsize=bio.core.FONT["tiny"], ha="center", color=P.muted())
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.05)
pa.set_xticklabels([])
C.style_axes(pa, None, "level (normalized)")
pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center left")
bio.panel(ax, "A", (0.2, 9.4))
# domains
dom = np.where(wnt > tW2, 3, np.where(ra > tR, 2, np.where(wnt > tW1, 1, 0)))
names = ["forebrain", "midbrain", "hindbrain", "spinal cord"]
toks = ["receptor", "protein", "highlight", "positive"]
y0 = 1.6
X0, W = 1.8, 16.4
start = 0
for i in range(1, N + 1):
    if i == N or dom[i] != dom[start]:
        a, b = x[start], x[i - 1] + dx
        ax.add_patch(bio.core.FancyBboxPatch((X0 + a * W, y0 - 0.4), (b - a) * W - 0.05, 0.8, boxstyle="round,pad=0,rounding_size=0.1",
                                             facecolor=P.fill(toks[dom[start]]), edgecolor=P.edge(toks[dom[start]]), lw=0.8))
        bio.label(ax, (X0 + (a + b) / 2 * W, y0), names[dom[start]], size="small")
        start = i
bio.panel(ax, "B", (0.2, 2.7))
bio.label(ax, (X0, 0.6), "anterior", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (X0 + W, 0.6), "posterior", size="tiny", color=P.muted(), ha="right")
