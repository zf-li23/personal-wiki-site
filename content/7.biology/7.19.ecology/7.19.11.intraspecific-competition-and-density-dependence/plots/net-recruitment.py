"""Net recruitment and regulation (Section 11.3.2).

A: per capita birth rate b(N) = 0.9 - 0.004 N and death rate d(N) = 0.1 + 0.004 N (continuous time); they
cross at the carrying capacity K = 100. B: numbers per unit time: births b(N)N, deaths d(N)N and net
recruitment (b - d)N, dome-shaped with its peak at K/2.
C: the Hassell model N_{t+1} = lambda N_t (1 + a N_t)^(-b) with lambda = 4, b = 1 (Beverton-Holt) and
a = 0.03 (K = (lambda^(1/b) - 1)/a = 100) iterated from N0 = 2, shown as successive steps up the
net-recruitment curve F(N) - N (inset: the resulting S-shaped growth).
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
N = np.linspace(0, 150, 400)
bN, dN = 0.9 - 0.004 * N, 0.1 + 0.004 * N

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.9))
ax = axes[0]
ax.plot(N, bN, color=C.line("positive"), lw=2, label="birth rate b(N)")
ax.plot(N, dN, color=C.line("negative"), lw=2, label="death rate d(N)")
ax.axvline(100, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
ax.text(102, 0.85, "K", fontsize=FS["small"], color=P.ink())
ax.annotate("", (96, 0.05), (60, 0.05), arrowprops=dict(arrowstyle="-|>", color=P.ink()))
ax.annotate("", (104, 0.05), (140, 0.05), arrowprops=dict(arrowstyle="-|>", color=P.ink()))
ax.set_ylim(0, 1)
C.style_axes(ax, "density N", "per capita rate")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "A  Density-dependent birth and death")

ax = axes[1]
ax.plot(N, bN * N, color=C.line("positive"), lw=1.6, label="births")
ax.plot(N, dN * N, color=C.line("negative"), lw=1.6, label="deaths")
ax.plot(N, (bN - dN) * N, color=C.line("dna"), lw=2.2, label="net recruitment")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.plot([50], [20], "o", color=C.line("dna"), ms=5)
ax.text(52, 23, "maximum at K/2", fontsize=FS["tiny"], color=P.muted())
C.style_axes(ax, "density N", "individuals per unit time")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "B  The n-shaped net recruitment curve")

ax = axes[2]
lam, bb, aa = 4.0, 1.0, 0.03
F = lambda n: lam * n / (1 + aa * n) ** bb
ax.plot(N, F(N) - N, color=C.line("dna"), lw=2)
ax.axhline(0, color=P.muted(), lw=0.6)
n = 2.0
traj = [n]
for _ in range(12):
    nn = F(n)
    ax.annotate("", (nn, F(nn) - nn), (n, F(n) - n),
                arrowprops=dict(arrowstyle="-|>", color=C.line("rna"), lw=0.9, shrinkA=0, shrinkB=1))
    n = nn
    traj.append(n)
ax.plot(traj, [F(v) - v for v in traj], "o", ms=3, color=C.line("rna"))
nopt = (np.sqrt(lam) - 1) / aa
ax.text(nopt, F(nopt) - nopt + 4, "peak at (√λ − 1)/a", fontsize=FS["tiny"], color=P.muted(), ha="center")
ax.set_ylim(-30, 75)
C.style_axes(ax, "Nₜ", "net recruitment Nₜ₊₁ − Nₜ")
C.title(ax, "C  Beverton–Holt: steps towards K")
ins = ax.inset_axes([0.6, 0.7, 0.36, 0.26])
ins.plot(range(len(traj)), traj, "o-", ms=2, lw=1, color=C.line("rna"))
C.style_axes(ins, "t", "N", size="tiny")
fig.tight_layout()
