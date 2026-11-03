"""Selection that maintains variation. A: haploid frequency-dependent selection with w_a = 1 and
w_A = 1 - 0.2 (p - 0.5) (negative frequency dependence) or 1 + 0.2 (p - 0.5) (positive): change in the
frequency p of A per generation, with the direction of change marked on the axis (filled dot: stable
equilibrium, open dot: unstable). B: haploid Levene model with two niches of equal weight; axes: relative
fitness of A in each niche (a has fitness 1). Shaded: arithmetic mean > 1 > harmonic mean, where both alleles
increase when rare (Theorem 5.5.1). C: diploid selection with two generations a year and the fecundities of
Example 5.5.1 (spring 50, 55, 70 and autumn 70, 65, 55 for A1A1, A1A2, A2A2 in schedule 1; spring 55, 65, 75
and autumn 75, 65, 55 in schedule 2), starting from frequency 0.1 of A2,
shown once a year."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.7), gridspec_kw={"width_ratios": [1, 0.9, 1.1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.89, wspace=0.32)

a = axs[0]
p = np.linspace(0, 1, 300)
for sign, tok, lab in ((-1, "dna", "negative: $w_A = 1 - 0.2(p - 0.5)$"), (1, "rna", "positive: $w_A = 1 + 0.2(p - 0.5)$")):
    wA = 1 + sign * 0.2 * (p - 0.5)
    dp = p * (1 - p) * (wA - 1) / (p * wA + (1 - p))
    a.plot(p, dp, color=charts.line(tok), lw=1.8, label=lab)
a.axhline(0, color=P.muted(), lw=0.8)
for x0, x1, y in ((0.12, 0.38, -0.0021), (0.88, 0.62, -0.0021)):
    a.annotate("", xy=(x1, y), xytext=(x0, y), arrowprops=dict(arrowstyle="->", color=charts.line("dna"), lw=1.1))
for x0, x1, y in ((0.38, 0.12, 0.0021), (0.62, 0.88, 0.0021)):
    a.annotate("", xy=(x1, y), xytext=(x0, y), arrowprops=dict(arrowstyle="->", color=charts.line("rna"), lw=1.1))
a.scatter([0.5], [0], s=36, color=charts.line("dna"), zorder=5)
a.scatter([0.5], [0], s=70, facecolor="none", edgecolor=charts.line("rna"), lw=1.3, zorder=6)
a.set_xlim(0, 1)
a.set_ylim(-0.014, 0.014)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper center")
charts.style_axes(a, "frequency $p$ of $A$", "$\\Delta p$ per generation")
charts.title(a, "A  Frequency dependence")

b = axs[1]
v = np.linspace(0.3, 2.0, 400)
V1, V2 = np.meshgrid(v, v)
am = (V1 + V2) / 2
hm = 2 / (1 / V1 + 1 / V2)
prot = (am > 1) & (hm < 1)
b.contourf(V1, V2, prot.astype(float), levels=[0.5, 1.5], colors=[P.fill("positive")], alpha=0.6)
b.contour(V1, V2, am, levels=[1], colors=[P.ink()], linewidths=0.9)
b.contour(V1, V2, hm, levels=[1], colors=[P.ink()], linewidths=0.9, linestyles="--")
b.scatter([1.5, 0.6], [0.6, 1.5], s=26, color=P.ink(), zorder=5)
b.scatter([1.1], [0.85], s=26, facecolor="none", edgecolor=P.ink(), zorder=5)
b.annotate("(1.5, 0.6)", (1.5, 0.6), xytext=(1.55, 0.42), fontsize=FT["tiny"], color=P.ink())
b.annotate("(1.1, 0.85)", (1.1, 0.85), xytext=(1.16, 0.95), fontsize=FT["tiny"], color=P.ink())
b.text(1.55, 1.75, "$A$ fixed", fontsize=FT["tiny"], color=P.muted())
b.text(0.38, 0.45, "$a$ fixed", fontsize=FT["tiny"], color=P.muted())
b.text(0.36, 0.95, "solid: AM = 1\ndashed: HM = 1", fontsize=FT["tiny"], color=P.muted(), va="top")
b.set_xlim(0.3, 2.0)
b.set_ylim(0.3, 2.0)
b.set_aspect("equal")
charts.style_axes(b, "fitness of $A$ in niche 1", "fitness of $A$ in niche 2", box=True)
charts.title(b, "B  Levene model, two niches")

c = axs[2]
sched = {1: ((50, 55, 70), (70, 65, 55)), 2: ((55, 65, 75), (75, 65, 55))}
for k, tok in ((1, "rna"), (2, "dna")):
    q = 0.1
    traj = [q]
    for g in range(1600):
        w = np.array(sched[k][g % 2], float)
        pa = 1 - q
        wb = pa * pa * w[0] + 2 * pa * q * w[1] + q * q * w[2]
        q = (q * q * w[2] + pa * q * w[1]) / wb
        if g % 2 == 1:
            traj.append(q)
    c.plot(np.arange(len(traj)), traj, color=charts.line(tok), lw=1.2, label=f"schedule {k}")
c.set_xlim(0, 800)
c.set_ylim(0, 1.02)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.72))
charts.style_axes(c, "year (frequency after the autumn generation)", "frequency of $A_2$")
charts.title(c, "C  Fluctuating selection")
