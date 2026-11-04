"""Sampling depth and spatial scale in microbial diversity (simulated communities).

A: rarefaction curves, the expected number of taxa observed in a random subsample of n reads
(E[S_n] = sum_i [1 - C(N - N_i, n) / C(N, n)], computed with log-gamma), for two simulated communities of
10^5 reads: an even community of 300 taxa and a log-normal community of 2000 taxa (SD of log10 abundance
0.8) with a long tail of rare taxa. The rich community is far from saturation at depths where the even one
has levelled off, so richness must be compared at equal depth (see 7.8.14).
B: distance-decay of community similarity. 150 sites at random positions in a 1000 km square; an
environmental variable varies smoothly in space (sum of random cosine waves). Each of 400 taxa has a
Gaussian niche on that variable. "Environmental selection only": a taxon occurs wherever the environment
suits it. "With dispersal limitation": in addition it occurs only within a radius (50-600 km) of a random
origin. Jaccard similarity of presence-absence between site pairs against distance; lines are binned means.
"""
import numpy as np
from scipy.special import gammaln

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(24.0, 10.0)


def rarefy(counts, ns):
    N = counts.sum()
    out = []
    for n in ns:
        lp = gammaln(N - counts + 1) - gammaln(N - counts - n + 1) - (gammaln(N + 1) - gammaln(N - n + 1))
        lp = np.where(N - counts >= n, lp, -np.inf)
        out.append(np.sum(1 - np.exp(lp)))
    return np.array(out)


Nreads = 100000
even = rng.multinomial(Nreads, np.ones(300) / 300)
w = 10 ** rng.normal(0, 0.8, 2000)
logn = rng.multinomial(Nreads, w / w.sum())
logn = logn[logn > 0]
ns = np.unique(np.round(np.logspace(1, np.log10(Nreads), 60)).astype(int))

bio.panel(ax, "A", (0.3, 9.8))
pa = quant.Plot(ax, (2.2, 1.5, 8.5, 7.2), xlim=(10, Nreads), ylim=(0, 2000), xlog=True,
                xlabel="reads sampled", ylabel="taxa observed",
                xticks=[(10, "10"), (100, "10²"), (1000, "10³"), (10000, "10⁴"), (100000, "10⁵")],
                yticks=[0, 500, 1000, 1500, 2000], grid=True, ylabel_offset=1.1)
pa.line(ns, rarefy(even, ns), "dna", lw=1.8, text="even, 300 taxa", at=0.95, dx=-0.2, dy=0.35, ha="right")
pa.line(ns, rarefy(logn, ns), "atp", lw=1.8, text="log-normal, 2000 taxa", at=0.8, dx=-0.3, dy=0.4, ha="right")
pa.hline(300, token="dna", dashed=True)
pa.hline(2000, token="atp", dashed=True)

# B: distance decay ---------------------------------------------------------------------------------
nsite, ntax, L = 150, 400, 1000.0
xy = rng.uniform(0, L, (nsite, 2))
k = rng.normal(0, 2 * np.pi / 800, (6, 2))
ph = rng.uniform(0, 2 * np.pi, 6)
env = np.cos(xy @ k.T + ph).sum(axis=1)
env = (env - env.mean()) / env.std()
opt = rng.normal(0, 1.2, ntax)
wid = rng.uniform(0.3, 0.8, ntax)
pres_env = np.exp(-0.5 * ((env[:, None] - opt[None, :]) / wid[None, :]) ** 2) > 0.5
origin = rng.uniform(0, L, (ntax, 2))
rad = rng.uniform(50, 600, ntax)
dist_o = np.linalg.norm(xy[:, None, :] - origin[None, :, :], axis=2)
pres_disp = pres_env & (dist_o < rad[None, :])

i, j = np.triu_indices(nsite, 1)
dgeo = np.linalg.norm(xy[i] - xy[j], axis=1)


def jaccard(M):
    inter = (M[i] & M[j]).sum(axis=1)
    union = (M[i] | M[j]).sum(axis=1)
    return np.where(union > 0, inter / np.maximum(union, 1), np.nan)


bio.panel(ax, "B", (13.0, 9.8))
pb = quant.Plot(ax, (15.0, 1.5, 8.5, 7.2), xlim=(0, 1200), ylim=(0, 1), xlabel="distance between sites / km",
                ylabel="Jaccard similarity", xticks=[0, 400, 800, 1200], yticks=[0, 0.25, 0.5, 0.75, 1], grid=True,
                ylabel_offset=1.1)
cand = np.flatnonzero(dgeo < 1200)
sel = rng.choice(cand, 350, replace=False)
bins = np.linspace(0, 1200, 13)
for M, tok, txt, ty in [(pres_env, "plant", "environmental selection only", 0.42),
                        (pres_disp, "receptor", "with dispersal limitation", 0.1)]:
    s = jaccard(M)
    pb.points(dgeo[sel], s[sel], tok, r=0.03, hollow=True)
    mids, means = [], []
    for a, b in zip(bins[:-1], bins[1:]):
        m = (dgeo >= a) & (dgeo < b) & np.isfinite(s)
        if m.sum() > 20:
            mids.append((a + b) / 2)
            means.append(np.nanmean(s[m]))
    pb.line(mids, means, tok, lw=2.4)
    pb.text(1190, ty, txt, token=tok, ha="right", va="bottom")
