"""Tilman's resource-ratio hypothesis of succession: a consumer-resource simulation.

Five plant species with biomass B_i compete for soil nitrogen N and light L. Growth follows Liebig's law,
mu_i = r min(N/(N + kN_i), L/(L + kL_i)), r = 0.3 per year, with loss rate m = 0.1 per year and a small seed
rain (1e-4 per year). Species are ranked along a trade-off: species 1 needs little nitrogen but much light,
species 5 the reverse (R*_N = kN m/(r - m), R*_L = kL m/(r - m)). Available nitrogen is renewed at rate
D = 0.5 per year toward a supply S_N(t) that rises as the soil develops, S_N = 0.3 + 7.7(1 - exp(-t/150)),
and is taken up in proportion to growth (q = 0.3); light at the ground falls with total biomass,
L = exp(-0.25 sum B). A: biomass of each species. B: the path of the two resources (arrow: direction of time)
and the R* of each species (dots): the environment moves from low nitrogen and bright light to rich soil
and deep shade, and each species dominates where the resource ratio suits it. C: the number of species with
at least 5 % of total biomass and the Shannon diversity of biomass, both highest in mid-succession (computed once total biomass exceeds 0.5; before that the ground is nearly bare, gray band).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT

n = 5
kN = np.linspace(0.3, 3.0, n)
kL = np.linspace(0.9, 0.1, n)
r, m, D, q, k, eps = 0.3, 0.1, 0.5, 0.3, 0.25, 1e-4
toks = ["highlight", "enzyme", "protein", "dna", "plant"]


def supply(t):
    return 0.3 + 7.7 * (1 - np.exp(-t / 150))


def rhs(t, y):
    B, N = y[:n], y[n]
    L = np.exp(-k * B.sum())
    mu = r * np.minimum(N / (N + kN), L / (L + kL))
    return np.r_[B * (mu - m) + eps, D * (supply(t) - N) - q * (mu * B).sum()]


t = np.linspace(0, 350, 701)
sol = solve_ivp(rhs, (0, 350), np.r_[np.full(n, 0.01), 0.5], t_eval=t, rtol=1e-7, atol=1e-10, method="LSODA")
B = sol.y[:n]
N = sol.y[n]
L = np.exp(-k * B.sum(axis=0))

fig, ax = bio.canvas(31.0, 10.0)

pa = C.axes_at(ax, (2.2, 1.6, 7.6, 6.8))
for i in range(n):
    pa.plot(t, B[i], color=Q.line_color(toks[i]), lw=1.7, label=f"species {i + 1}")
pa.set_xlim(0, 350)
pa.set_ylim(0, 12.5)
C.style_axes(pa, "years since exposure of the substrate", "biomass (arbitrary units)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Replacement sequence", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.6, 1.6, 7.0, 6.8))
pb.plot(N, L, color=P.ink(), lw=1.4)
j = 260
pb.annotate("", xy=(N[j + 6], L[j + 6]), xytext=(N[j], L[j]),
            arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.2))
rs = m / (r - m)
for i in range(n):
    c = Q.line_color(toks[i])
    pb.plot([kN[i] * rs], [kL[i] * rs], "o", ms=6, color=c)
    pb.text(kN[i] * rs + 0.08, kL[i] * rs + 0.02, f"{i + 1}", fontsize=FS["tiny"], color=c)
for tt in (0, 50, 100, 150, 250):
    jj = int(tt * 2)
    pb.plot([N[jj]], [L[jj]], "s", ms=3, color=P.muted())
    pb.text(N[jj] + 0.1, L[jj] + 0.015, f"{tt} yr", fontsize=FS["tiny"] - 1, color=P.muted())
pb.set_xlim(0, 7)
pb.set_ylim(0, 1.05)
C.style_axes(pb, "available soil nitrogen N", "light at the ground L")
bio.panel(ax, "B", (11.1, 9.6))
bio.label(ax, (12.6, 9.2), "Resource path and species R*", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.0, 6.8))
rel = B / B.sum(axis=0)
rich = (rel >= 0.05).sum(axis=0)
H = -(rel * np.log(rel)).sum(axis=0)
bare = B.sum(axis=0) < 0.5
rich = np.where(bare, np.nan, rich)
H = np.where(bare, np.nan, H)
pc.axvspan(0, t[bare].max(), color=P.muted(), alpha=0.15, lw=0)
pc.text(t[bare].max() / 2, 0.3, "sparse\ncover", fontsize=FS["tiny"], color=P.muted(), ha="center")
pc.step(t, rich, where="mid", color=Q.line_color("dna"), lw=1.5, label="species with ≥ 5 % of biomass")
pc2 = pc.twinx()
pc2.plot(t, H, color=Q.line_color("negative"), lw=1.5)
pc.plot([], [], color=Q.line_color("negative"), lw=1.5, label="Shannon diversity H′ (right axis)")
pc.set_xlim(0, 350)
pc.set_ylim(0, 5.5)
pc2.set_ylim(0, 1.65)
C.style_axes(pc, "years", "number of species")
C.style_axes(pc2, None, "H′")
pc2.spines["right"].set_visible(True)
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "C", (21.1, 9.6))
bio.label(ax, (22.6, 9.2), "Diversity peaks in mid-succession", size="small", bold=True, ha="left")
