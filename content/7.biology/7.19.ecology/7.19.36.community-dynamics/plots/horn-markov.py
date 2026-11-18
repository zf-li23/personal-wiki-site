"""Horn's Markov chain model of forest succession (Horn 1975, 1981; Princeton, New Jersey).

Transition matrix P (50-year steps): row = present occupant of a canopy site, column = occupant 50 years
later, for grey birch, blackgum, red maple and beech. A: composition pi_t = pi_0 P^t from a stand of 100 %
grey birch; the dashed lines are the stationary distribution (left eigenvector of P for eigenvalue 1),
the diamonds the composition of an old forest observed by Horn. B: total variation distance between pi_t and
the stationary distribution for four initial stands; all decay at the rate of the second eigenvalue
lambda_2 = 0.716 per 50 years (parallel lines on the log scale). C: one realization of the chain for 60 individual sites
started as grey birch (each row of tiles is a site), showing that the stationary composition is a mosaic
in which individual sites keep changing.
"""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT

M = np.array([
    [0.05, 0.36, 0.50, 0.09],
    [0.01, 0.57, 0.25, 0.17],
    [0.00, 0.14, 0.55, 0.31],
    [0.00, 0.01, 0.03, 0.96],
])
names = ["grey birch", "blackgum", "red maple", "beech"]
toks = ["highlight", "protein", "negative", "plant"]

w, v = np.linalg.eig(M.T)
order = np.argsort(-np.abs(w))
pi = np.real(v[:, order[0]])
pi = pi / pi.sum()
lam2 = float(np.real(w[order[1]]))
old = np.array([0.0, 0.03, 0.04, 0.93])

fig, ax = bio.canvas(31.0, 10.0)

pa = C.axes_at(ax, (2.2, 1.6, 7.6, 6.8))
steps = 10
comp = [np.array([1.0, 0, 0, 0])]
for _ in range(steps):
    comp.append(comp[-1] @ M)
comp = np.array(comp)
years = 50 * np.arange(steps + 1)
for k in range(4):
    c = Q.line_color(toks[k])
    pa.plot(years, 100 * comp[:, k], "-o", ms=3, color=c, lw=1.6, label=names[k])
    pa.axhline(100 * pi[k], color=c, lw=0.8, ls=(0, (3, 2)))
    pa.plot([535], [100 * old[k]], "D", ms=4, color=c, clip_on=False)
pa.set_xlim(0, 540)
pa.set_ylim(0, 102)
C.style_axes(pa, "years since start (100 % grey birch)", "canopy composition (%)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Convergence to the stationary composition", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.6, 1.6, 7.0, 6.8))
starts = {
    "100 % grey birch": np.array([1.0, 0, 0, 0]),
    "100 % red maple": np.array([0, 0, 1.0, 0]),
    "50 % blackgum, 50 % maple": np.array([0, 0.5, 0.5, 0]),
    "100 % beech": np.array([0, 0, 0, 1.0]),
}
for (lab, x0), tok in zip(starts.items(), ["highlight", "negative", "protein", "plant"]):
    x = x0.copy()
    d = []
    for _ in range(16):
        d.append(0.5 * np.abs(x - pi).sum())
        x = x @ M
    pb.semilogy(50 * np.arange(16), d, "-o", ms=2.6, color=Q.line_color(tok), lw=1.3, label=lab)
tt = 50 * np.arange(16)
pb.text(740, 0.45, "all decay as λ₂ = %.3f per 50 yr" % lam2, fontsize=FS["tiny"], color=P.muted(), ha="right")
pb.set_xlim(0, 760)
pb.set_ylim(1e-3, 1.2)
C.style_axes(pb, "years", "distance from stationary distribution")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (11.1, 9.6))
bio.label(ax, (12.6, 9.2), "Rate of convergence", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.8, 6.8))
rng = np.random.default_rng(1)
n_sites, n_steps = 60, 13
state = np.zeros(n_sites, dtype=int)
grid = [state.copy()]
cum = np.cumsum(M, axis=1)
for _ in range(n_steps - 1):
    u = rng.random(n_sites)
    state = np.array([np.searchsorted(cum[s], uu) for s, uu in zip(state, u)])
    state = np.minimum(state, 3)
    grid.append(state.copy())
grid = np.array(grid)
for t in range(n_steps):
    for i in range(n_sites):
        pc.add_patch(Rectangle((50 * t - 22, i - 0.45), 44, 0.9, color=Q.line_color(toks[grid[t, i]]), lw=0))
pc.set_xlim(-25, 50 * (n_steps - 1) + 25)
pc.set_ylim(-1, n_sites)
pc.set_yticks([])
C.style_axes(pc, "years", "individual canopy sites")
bio.panel(ax, "C", (21.2, 9.6))
bio.label(ax, (22.6, 9.2), "Tree-by-tree replacement (60 sites)", size="small", bold=True, ha="left")
