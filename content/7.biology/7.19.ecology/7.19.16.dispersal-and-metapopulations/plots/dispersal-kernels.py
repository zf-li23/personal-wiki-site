"""Dispersal kernels with the same mean distance but different tails.

Distribution of dispersal distance r for three kernels with mean distance 1 (arbitrary units):
half-normal (Gaussian kernel, sigma = sqrt(pi/2)), exponential (rate 1) and a fat-tailed Lomax (Pareto type
II) kernel with shape 2.5 and scale 1.5, whose tail decays as a power of r. A: densities on a log scale:
near the source the kernels are similar, far away they differ by orders of magnitude. B: probability of
dispersing farther than r (log-log): the fraction of propagules beyond 10 mean distances is about 1e-15
(Gaussian), 5e-5 (exponential) and 6e-3 (fat-tailed). C: 2000 seeds dispersed in random directions from
one parent with each kernel (seed 0): the fat-tailed kernel produces a few distant colonists.
"""

import numpy as np
from scipy import stats

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
kern = [("Gaussian", stats.halfnorm(scale=np.sqrt(np.pi / 2)), "dna"),
        ("exponential", stats.expon(scale=1.0), "enzyme"),
        ("fat-tailed (Lomax)", stats.lomax(2.5, scale=1.5), "negative")]

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 7.5, 6.8))
r = np.linspace(0, 12, 400)
for name, dist, tok in kern:
    pa.plot(r, dist.pdf(r), color=Q.line_color(tok), lw=1.6, label=name)
pa.set_yscale("log")
pa.set_ylim(1e-8, 2)
pa.set_xlim(0, 12)
C.style_axes(pa, "distance r (mean distance = 1)", "probability density")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Same mean, different tails", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (12.0, 1.6, 7.0, 6.8))
r2 = np.logspace(-1, 2, 300)
for name, dist, tok in kern:
    pb.plot(r2, np.clip(dist.sf(r2), 1e-12, 1), color=Q.line_color(tok), lw=1.6)
pb.set_xscale("log")
pb.set_yscale("log")
pb.set_ylim(1e-8, 1.5)
pb.axvline(10, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
C.style_axes(pb, "distance r", "P(distance > r)")
bio.panel(ax, "B", (10.5, 9.6))
bio.label(ax, (12.0, 9.2), "Tail probabilities", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.0, 1.6, 7.0, 6.8))
rng = np.random.default_rng(0)
for name, dist, tok in kern:
    d = dist.rvs(size=2000, random_state=rng)
    th = rng.uniform(0, 2 * np.pi, 2000)
    pc.plot(d * np.cos(th), d * np.sin(th), "o", ms=1.4, alpha=0.6, color=Q.line_color(tok))
pc.plot([0], [0], "*", ms=9, color=P.ink())
pc.set_xlim(-12, 12)
pc.set_ylim(-12, 12)
pc.set_aspect("equal")
C.style_axes(pc, "x", "y")
bio.panel(ax, "C", (20.5, 9.6))
bio.label(ax, (22.0, 9.2), "Seed shadows around one parent", size="small", bold=True, ha="left")
