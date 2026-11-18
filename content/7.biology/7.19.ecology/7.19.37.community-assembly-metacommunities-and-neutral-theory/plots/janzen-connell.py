"""The Janzen-Connell mechanism.

A: Janzen's (1970) graphical model. Seed density falls with distance r from the parent tree,
D(r) = exp(-r / a) with a = 10 m; the probability that a seed or seedling escapes host-specific enemies,
which are concentrated near the parent, rises with distance, E(r) = 1 - exp(-r / b) with b = 15 m. The
recruitment curve D(r) E(r) is humped, with its maximum at r* = b ln((a + b) / b) = 7.7 m: recruits
appear at some distance from the parent, leaving space near it to other species.
B: consequence for diversity in a lottery community of J = 2000 individuals and initially 40 equally
abundant species. Each generation all J sites are refilled by a multinomial lottery (three runs of
1000 generations each). Neutral: a site is won by a species with probability proportional to its abundance. With conspecific negative density dependence: species
i wins a site with weight n_i exp(-k n_i / J), k = 25, so the per capita recruitment of a species falls
as it becomes common. Neutral drift loses species steadily; the stabilizing density dependence keeps
almost all of them.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(1)
fig, ax = bio.canvas(30.0, 12.0)

a, b = 10.0, 15.0
r = np.linspace(0, 60, 400)
D = np.exp(-r / a)
E = 1 - np.exp(-r / b)
pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
pa.plot(r, D, color=Q.line_color("plant"), lw=1.6, label="seed density D(r)")
pa.plot(r, E, color=Q.line_color("negative"), lw=1.6, label="escape from enemies E(r)")
pa.plot(r, 4 * D * E, color=Q.line_color("dna"), lw=2.0, label="recruitment D(r) E(r)  (x4)")
rs = b * np.log((a + b) / b)
pa.axvline(rs, color=P.muted(), lw=0.9, ls=":")
pa.text(rs + 1, 0.95, f"r* = {rs:.1f} m", fontsize=FS["tiny"], color=P.ink())
pa.set_xlim(0, 60)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "distance from parent tree / m", "relative value")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Janzen's recruitment curve", size="small", bold=True, ha="left")


def lottery(J, S0, gens, k, every):
    n = np.full(S0, J // S0, float)
    out = [S0]
    for g in range(gens):
        w = n * np.exp(-k * n / J) if k else n.copy()
        n = rng.multinomial(J, w / w.sum()).astype(float)
        if (g + 1) % every == 0:
            out.append(int((n > 0).sum()))
    return np.array(out)


J, S0, G, ev = 2000, 40, 1000, 10
tg = np.arange(0, G + 1, ev)
pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
for rep in range(3):
    pb.plot(tg, lottery(J, S0, G, 0.0, ev), color=Q.line_color("muted"), lw=1.2, label="neutral" if rep == 0 else None)
    pb.plot(tg, lottery(J, S0, G, 25.0, ev), color=Q.line_color("positive"), lw=1.4,
            label="negative density dependence" if rep == 0 else None)
pb.set_xlim(0, G)
pb.set_ylim(0, 42)
C.style_axes(pb, "time / generations", "number of species")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Richness with and without density dependence", size="small", bold=True, ha="left")
