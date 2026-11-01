"""Disease modules and drug proximity in a simulated interactome. The interactome has 3000 proteins
grown by preferential attachment (three edges per new protein). A disease module of 60 proteins is
planted as a connected region (grown from one protein by repeatedly adding a random neighbor of the
region); only 30 of them, chosen at random, are 'known' disease genes, as in an incompletely
characterized disease. A: the size of the largest connected component formed by the 30 known
genes (line) against 1000 random sets of 30 proteins with matching degrees (histogram). B: the
closest distance d_c between the four targets of a drug and the known disease genes (Formula
12.6.2) for a drug whose targets lie in the module (blue line) and a drug with random targets (red
line); the histogram shows the distances of 1000 degree-matched random target sets for the random
drug (the null distribution for the module drug is similar, mean 2.16)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, connected_components
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N, m = 3000, 3
src, dst, targets = [], [], list(range(m + 1))
rep = []
for i in range(m + 1):
    for j in range(i + 1, m + 1):
        src.append(i); dst.append(j); rep += [i, j]
for v in range(m + 1, N):
    chosen = set()
    while len(chosen) < m:
        chosen.add(rep[int(rng.integers(len(rep)))])
    for u in chosen:
        src.append(u); dst.append(v); rep += [u, v]
Adj = csr_matrix((np.ones(len(src)), (src, dst)), shape=(N, N))
Adj = ((Adj + Adj.T) > 0).astype(float)
deg = np.asarray(Adj.sum(1)).ravel().astype(int)
nbrs = [Adj.indices[Adj.indptr[i]:Adj.indptr[i + 1]] for i in range(N)]
module = {int(rng.integers(N))}
while len(module) < 60:
    v = int(rng.choice(sorted(module)))
    module.add(int(rng.choice(nbrs[v])))
module = np.array(sorted(module))
known = rng.choice(module, 30, replace=False)
lo = np.digitize(np.log(deg), np.quantile(np.log(deg), np.linspace(0, 1, 11)[1:-1]))
bins = {b: np.where(lo == b)[0] for b in np.unique(lo)}


def matched(S):
    return np.array([rng.choice(bins[lo[s]]) for s in S])


def lcc(S):
    sub = Adj[S][:, S]
    _, lab = connected_components(sub, directed=False)
    return np.bincount(lab).max()


obs = lcc(known)
null = np.array([lcc(np.unique(matched(known))) for _ in range(1000)])
z_lcc = (obs - null.mean()) / null.std()
D = shortest_path(Adj, unweighted=True, indices=known)          # distances from known genes


def dc(T):
    return D[:, T].min(0).mean()


drug_in = rng.choice(module, 4, replace=False)
drug_out = rng.choice(np.setdiff1d(np.arange(N), module), 4, replace=False)
res = {}
for name, T in [("module drug", drug_in), ("random drug", drug_out)]:
    nd = np.array([dc(matched(T)) for _ in range(1000)])
    res[name] = (dc(T), nd.mean(), nd.std(), (dc(T) - nd.mean()) / nd.std(), nd)

fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.6))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.88, wspace=0.28)
a.hist(null, bins=np.arange(0.5, max(null.max(), obs) + 1.5), color=P.fill("neutral"), edgecolor=P.edge("neutral"))
a.axvline(obs, color=charts.line("highlight"), lw=1.6)
a.text(obs, a.get_ylim()[1] * 0.9, f"  observed {obs}\n  z = {z_lcc:.1f}", color=P.ink(), fontsize=7.5, va="top")
charts.style_axes(a, "largest connected component of 30 genes", "random sets")
charts.title(a, "A  Known disease genes form a module")
nd = res["random drug"][4]
b.hist(nd, bins=20, color=P.fill("neutral"), edgecolor=P.edge("neutral"))
for name, col in [("module drug", charts.line("dna")), ("random drug", charts.line("negative"))]:
    d, mu, sd, z, _ = res[name]
    b.axvline(d, color=col, lw=1.6, label=f"{name}: d_c = {d:.2f}, z = {z:.1f}")
b.legend(fontsize=7, frameon=False, labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "closest distance d_c to the disease genes", "random target sets")
charts.title(b, "B  Drug-disease proximity")
