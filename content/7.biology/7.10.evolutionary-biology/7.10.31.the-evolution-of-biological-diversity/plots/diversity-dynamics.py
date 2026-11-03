"""Models of diversity through time (Sections 31.1.1 and 31.6). A: a clade that starts with one species
and grows exponentially at net diversification rate D = 0.2 per Myr, or logistically with the same
initial rate and an equilibrium of K = 20 species (after Futuyma and Kirkpatrick 2017, Fig. 19.2).
B and C: two competing clades, each limited by the diversity of both, in the form of the coupled
logistic model of Sepkoski and colleagues: dN1/dt = r1 N1 (1 - (N1 + a12 N2)/K1),
dN2/dt = r2 N2 (1 - (N2 + a21 N1)/K2), with r1 = 0.4, r2 = 0.15 per Myr, K1 = K2 = 100 and clade 2
the superior competitor (a12 = 1.2, a21 = 0.6). B: clade 2 arises in a world already full of clade 1
and slowly displaces it (competitive displacement). C: here neither clade can invade the other when the other is near
its equilibrium (a12 = 1.2, a21 = 1.02; r1 = 0.3, r2 = 0.5 per Myr), so clade 2 stays rare beside the
incumbent; an external perturbation 60 Myr after the start removes 98 % of clade 1 and 50 % of
clade 2, and clade 2 then radiates and holds the ecological space (incumbent replacement)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def run(r1, r2, K1, K2, a12, a21, N1, N2, t_end, kick=None, dt=0.01):
    t = np.arange(0, t_end, dt)
    out = np.zeros((t.size, 2))
    for k, tt in enumerate(t):
        if kick is not None and abs(tt - kick) < dt / 2:
            N1, N2 = 0.02 * N1, 0.5 * N2
        out[k] = N1, N2
        d1 = r1 * N1 * (1 - (N1 + a12 * N2) / K1)
        d2 = r2 * N2 * (1 - (N2 + a21 * N1) / K2)
        N1, N2 = max(N1 + d1 * dt, 0), max(N2 + d2 * dt, 0)
    return t, out


fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.18, top=0.86, wspace=0.3)
t = np.linspace(0, 30, 301)
D, K = 0.2, 20
axes[0].plot(t, np.exp(D * t), color=charts.line("dna"), lw=2, label="exponential")
axes[0].plot(t, K / (1 + (K - 1) * np.exp(-D * t)), color=charts.line("rna"), lw=2, label="logistic")
axes[0].axhline(K, color=P.muted(), lw=0.8, ls=":")
axes[0].set_ylim(0, 30)
charts.style_axes(axes[0], "time (Myr)", "number of species")
charts.title(axes[0], "A  Exponential and logistic")
axes[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
tt, X = run(0.4, 0.15, 100, 100, 1.2, 0.6, 100.0, 1.0, 150)
axes[1].plot(tt, X[:, 0], color=charts.line("neutral"), lw=2, label="clade 1 (incumbent)")
axes[1].plot(tt, X[:, 1], color=charts.line("plant"), lw=2, label="clade 2 (superior)")
charts.style_axes(axes[1], "time (Myr)", "number of genera")
charts.title(axes[1], "B  Competitive displacement")
axes[1].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
tt, X = run(0.3, 0.5, 100, 100, 1.2, 1.02, 100.0, 5.0, 150, kick=60.0)
axes[2].plot(tt, X[:, 0], color=charts.line("neutral"), lw=2)
axes[2].plot(tt, X[:, 1], color=charts.line("plant"), lw=2)
axes[2].axvline(60, color=charts.line("negative"), lw=1, ls="--")
axes[2].text(61, 95, "mass\nextinction", fontsize=FT["tiny"], color=charts.line("negative"), va="top")
charts.style_axes(axes[2], "time (Myr)")
charts.title(axes[2], "C  Incumbent replacement")
