"""Two models of the intermediate disturbance hypothesis and Huston's dynamic equilibrium.

A: mosaic of patches (Connell's verbal argument). Patches are reset by disturbances that occur at rate
delta; a patch of age a holds s(a) = 1 + (S0 - 1)(1 - exp(-lambda a)) exp(-mu a) species (colonization at
rate lambda = 0.2 per year, competitive exclusion at rate mu = 0.02 per year, pool S0 = 30). Ages are
exponential with mean 1/delta, so the mean richness per patch is
1 + (S0 - 1) delta [1/(delta + mu) - 1/(delta + lambda + mu)] (line); grey: s(a) itself (top axis).
B-C: Tilman's (1994) competitive hierarchy, dp_i/dt = c_i p_i (1 - sum_{j<=i} p_j) - m p_i
- p_i sum_{j<i} c_j p_j, with 20 species, colonization rates c_i = 0.05 x 1.25^(i-1) per year rising as
competitive rank falls, and a density-independent disturbance mortality m. Equilibria from the exact
recursion p_i* = max(0, 1 - sum_{j<i} p_j* - (m + sum_{j<i} c_j p_j*)/c_i). B: number of species with
p_i* > 0 and the effective number of species exp(H') of the occupancies against m. C: equilibrium occupancies (stacked, species 1 = best competitor at the bottom).
D: Huston's dynamic equilibrium: all colonization rates multiplied by a productivity factor g; the number
of coexisting species depends only on m/g, so the ridge of maximum richness runs along m proportional to g (dashed line m = 0.04 g).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT

n = 20
c0 = 0.05 * 1.25 ** np.arange(n)


def equilibrium(c, m):
    p = np.zeros(len(c))
    for i in range(len(c)):
        val = 1 - p[:i].sum() - (m + (c[:i] * p[:i]).sum()) / c[i]
        p[i] = max(0.0, val)
    return p


fig, ax = bio.canvas(27.0, 20.0)

pa = C.axes_at(ax, (2.6, 11.6, 9.4, 6.6))
S0, lam, mu = 30, 0.2, 0.02
d = np.logspace(-3.5, 1, 300)
mean_s = 1 + (S0 - 1) * d * (1 / (d + mu) - 1 / (d + lam + mu))
pa.semilogx(d, mean_s, color=Q.line_color("dna"), lw=1.8, label="mean richness per patch")
pa.set_xlim(d[0], d[-1])
pa.set_ylim(0, 31)
C.style_axes(pa, "disturbance rate δ (per year)", "species per patch")
pa2 = pa.twiny()
age = np.linspace(0, 400, 400)
pa2.plot(age, 1 + (S0 - 1) * (1 - np.exp(-lam * age)) * np.exp(-mu * age), color=P.muted(), lw=1.0, ls=(0, (3, 2)))
pa2.set_xlim(0, 400)
C.style_axes(pa2, None, None)
pa2.spines["top"].set_visible(True)
pa2.set_xlabel("patch age a (years), grey dashed curve s(a)", fontsize=FS["tiny"], color=P.muted())
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.5, 19.6))
bio.label(ax, (2.6, 19.6), "Successional mosaic", size="small", bold=True, ha="left")

ms = np.logspace(-3, 0.5, 400)
eqs = np.array([equilibrium(c0, m) for m in ms])
pb = C.axes_at(ax, (16.0, 11.6, 9.4, 6.6))
rel = eqs / eqs.sum(axis=1, keepdims=True)
with np.errstate(divide="ignore", invalid="ignore"):
    hill = np.exp(-np.nansum(np.where(rel > 0, rel * np.log(rel), 0.0), axis=1))
pb.semilogx(ms, (eqs > 1e-9).sum(axis=1), color=Q.line_color("negative"), lw=1.6, label="species with p* > 0")
pb.semilogx(ms, hill, color=Q.line_color("dna"), lw=1.8, label="effective number exp(H′)")
pb.set_xlim(ms[0], ms[-1])
pb.set_ylim(0, 21.5)
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.style_axes(pb, "disturbance mortality m (per year)", "coexisting species")
bio.panel(ax, "B", (14.2, 19.6))
bio.label(ax, (16.0, 19.6), "Competition–colonization hierarchy", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (2.6, 1.8, 9.4, 6.6))
cols = [Q.line_color(t) for t in ("dna", "enzyme", "protein", "negative", "plant", "highlight", "rna", "muted")]
pc.stackplot(ms, eqs.T, colors=[cols[i % len(cols)] for i in range(n)], lw=0)
pc.set_xscale("log")
pc.set_xlim(ms[0], ms[-1])
pc.set_ylim(0, 1)
C.style_axes(pc, "disturbance mortality m (per year)", "fraction of sites occupied")
bio.panel(ax, "C", (0.5, 9.8))
bio.label(ax, (2.6, 9.8), "Who persists (best competitor at the bottom)", size="small", bold=True, ha="left")

pd = C.axes_at(ax, (16.0, 1.8, 8.4, 6.6))
gs = np.logspace(-1, 1, 90)
mm = np.logspace(-3, 0.5, 90)
R = np.array([[(equilibrium(c0 * g, m) > 1e-9).sum() for m in mm] for g in gs])
im = pd.pcolormesh(mm, gs, R, cmap="viridis", shading="auto")
pd.set_xscale("log")
pd.set_yscale("log")
pd.plot(mm, mm / 0.04, color="white", lw=1.0, ls=(0, (4, 2)))
pd.set_xlim(mm[0], mm[-1])
pd.set_ylim(gs[0], gs[-1])
C.style_axes(pd, "disturbance mortality m", "productivity factor g")
cb = fig.colorbar(im, ax=pd, fraction=0.06, pad=0.03)
cb.set_label("coexisting species", fontsize=FS["tiny"], color=P.ink())
cb.ax.tick_params(labelsize=FS["tiny"], colors=P.ink())
bio.panel(ax, "D", (14.2, 9.8))
bio.label(ax, (16.0, 9.8), "Dynamic equilibrium (Huston)", size="small", bold=True, ha="left")
