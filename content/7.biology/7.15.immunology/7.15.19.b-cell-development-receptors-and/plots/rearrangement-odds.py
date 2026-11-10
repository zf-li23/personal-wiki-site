# Discrete probability model of immunoglobulin gene rearrangement during B-cell development.
# Each V(D)J join keeps the downstream reading frame with probability p = 1/3 (the joint is imprecise).
# Heavy chain: allele 1 is tried first; only if it is nonproductive is allele 2 tried (allelic exclusion).
# Light chain: kappa then lambda, two alleles each; every locus allows m successive attempts
# (secondary rearrangement of an upstream V to a downstream J). Exact results are compared with a
# Monte Carlo simulation of 200,000 developing cells.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
p = 1 / 3
N = 200_000

# ---- heavy chain: exact outcome probabilities and simulation -------------------------------------------
first = rng.random(N) < p
second = (~first) & (rng.random(N) < p)
sim_h = np.array([first.mean(), second.mean(), 1 - first.mean() - second.mean()])
exact_h = np.array([p, (1 - p) * p, (1 - p) ** 2])

fig, ax = bio.canvas(24, 9.4)

bio.panel(ax, "A", (0.1, 9.2))
bio.label(ax, (6.2, 8.9), "Heavy chain: two alleles, tried one after the other", size="small")
bars = [("allele 1 productive\n(allele 2 stays DJ)", "positive"),
        ("allele 1 out of frame,\nallele 2 productive", "enzyme"),
        ("both out of frame:\ncell dies", "negative")]
pa = quant.Plot(ax, (2.0, 2.2, 8.6, 5.6), (0, 3), (0, 0.6), ylabel="Fraction of pro-B cells",
                yticks=[0, 0.2, 0.4, 0.6], grid=True)
for k, ((txt, tok), e, s) in enumerate(zip(bars, exact_h, sim_h)):
    pa.bars([k + 0.18, k + 0.82], [e], tok)
    pa.points([k + 0.5], [s], "ink", r=0.09, hollow=True)
    pa.text(k + 0.5, e + 0.02, f"{e:.3f}", va="bottom", size="tiny")
    bio.label(ax, (pa.X(k + 0.5), 1.75), txt, size="tiny", va="top")
bio.label(ax, (6.3, 0.25), "bars: exact; circles: simulation of 200,000 cells", size="tiny", color=P.muted())
surv = exact_h[0] + exact_h[1]
bio.label(ax, (10.9, 6.6), f"survive heavy-chain\ncheckpoint: {surv:.3f} (= 5/9)", size="tiny", ha="left")
bio.label(ax, (10.9, 5.2), f"of survivors, VDJ on both\nalleles: {exact_h[1] / surv:.2f}", size="tiny", ha="left")

# ---- light chain: success vs number of attempts per locus ---------------------------------------------
bio.panel(ax, "B", (13.6, 9.2))
bio.label(ax, (18.6, 8.9), "Light chain: four loci, m attempts each", size="small")
m = np.arange(1, 6)
pl = 1 - (1 - p) ** (4 * m)
kappa_only = 1 - (1 - p) ** (2 * m)
sim_l = []
for mm in m:
    tries = rng.random((40_000, 4 * mm)) < p
    sim_l.append(tries.any(axis=1).mean())
pb = quant.Plot(ax, (15.4, 2.2, 7.8, 5.6), (0.6, 5.4), (0.4, 1.0), xlabel="Attempts per locus, m",
                ylabel="Probability of a light chain", xticks=[1, 2, 3, 4, 5], yticks=[0.4, 0.6, 0.8, 1.0], grid=True)
pb.line(m, pl, "dna", lw=1.8, text="κ + λ (4 loci)", at=0.72, dy=-0.75, va="top")
pb.line(m, kappa_only, "rna", lw=1.4, dashed=True, text="κ only (2 loci)", at=0.3, dy=-0.4, va="top", ha="left")
pb.points(m, sim_l, "ink", r=0.09, hollow=True)
pb.line(m, surv * pl, "muted", lw=1.2, dotted=True, text="whole development (× 5/9)", at=0.45, dy=0.25, va="bottom")

