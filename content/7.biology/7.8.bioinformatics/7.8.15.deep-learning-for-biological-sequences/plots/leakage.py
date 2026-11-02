# Homology leakage (simulated). 1200 sequences of 150 bp in 40 superfamilies x 5 families x 6 members:
# each family ancestor differs from its superfamily ancestor at 25 % of sites, each member from its family
# ancestor at 5 %; the label is a random property of the superfamily, so no sequence rule exists and the
# true accuracy on a new superfamily is 50 %. A nearest-neighbor classifier (label of the most identical
# training sequence) stands for any model that can memorize. A: pairwise identity within families, within
# superfamilies and between superfamilies. B: test accuracy (mean and standard deviation over 20 splits,
# 20 % held out) for a random split and for splits by single-linkage clusters at decreasing identity
# thresholds: the estimate stays near 100 % until the clusters reach the superfamilies.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(11)
L = 150


def mutate(s, p):
    m = rng.random(len(s)) < p
    s = s.copy()
    s[m] = (s[m] + rng.integers(1, 4, m.sum())) % 4
    return s


seqs, sf, fam, lab = [], [], [], []
nS, nF, nM = 40, 5, 6
for a in range(nS):
    anc = rng.integers(0, 4, L)
    la = rng.random() < 0.5
    for b in range(nF):
        fa = mutate(anc, 0.25)
        for m in range(nM):
            seqs.append(mutate(fa, 0.05))
            sf.append(a)
            fam.append(a * nF + b)
            lab.append(la)
S = np.array(seqs)
sf, fam, y = np.array(sf), np.array(fam), np.array(lab).astype(int)
N = len(S)
ident = (S[:, None, :] == S[None, :, :]).mean(2)
eye = np.eye(N, dtype=bool)
same_f = (fam[:, None] == fam[None]) & ~eye
same_s = (sf[:, None] == sf[None]) & (fam[:, None] != fam[None])
diff = sf[:, None] != sf[None]


def clusters(t):
    parent = np.arange(N)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    ii, jj = np.where(np.triu(ident >= t, 1))
    for i, j in zip(ii, jj):
        a, b = find(i), find(j)
        if a != b:
            parent[a] = b
    return np.array([find(i) for i in range(N)])


def nn_acc(test):
    tr = ~test
    pred = y[tr][ident[np.ix_(test, tr)].argmax(1)]
    return (pred == y[test]).mean()


reps = 20
rand = [nn_acc(rng.random(N) < 0.2) for _ in range(reps)]
ths = [0.95, 0.9, 0.8, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45]
mean, sd, ncl = [], [], []
for t in ths:
    cl = clusters(t)
    u = np.unique(cl)
    acc = []
    for _ in range(reps):
        test = np.isin(cl, rng.choice(u, int(round(0.2 * len(u))), replace=False))
        acc.append(nn_acc(test))
    mean.append(np.mean(acc))
    sd.append(np.std(acc))
    ncl.append(len(u))

fig, ax = bio.canvas(26.0, 9.0)
a = C.axes_at(ax, (1.9, 1.5, 7.5, 6.6))
bins = np.linspace(0.15, 1.0, 69)
for m, tok, name in ((same_f, "positive", "same family"), (same_s, "dna", "same superfamily"), (diff, "neutral", "different superfamilies")):
    a.hist(ident[np.triu(m, 1)], bins=bins, density=True, color=C.line(tok), alpha=0.75, label=name)
C.style_axes(a, "pairwise identity", "density")
a.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper center")
b = C.axes_at(ax, (12.6, 1.5, 12.5, 6.6))
xs = np.arange(len(ths))
b.errorbar(xs, mean, yerr=sd, fmt="o-", ms=4, color=C.line("negative"), lw=1.3, capsize=2, label="split by identity clusters")
b.axhline(np.mean(rand), color=C.line("dna"), ls=(0, (4, 2)), lw=1.2, label=f"random split ({np.mean(rand):.0%})")
b.axhline(0.5, color=P.muted(), ls=":", lw=1.0, label="true accuracy on new superfamilies")
for x_, n_ in zip(xs, ncl):
    b.text(x_, 0.33, f"{n_}", ha="center", fontsize=FT["tiny"], color=P.muted())
b.text(-0.6, 0.38, "clusters:", fontsize=FT["tiny"], color=P.muted())
b.set_xticks(xs)
b.set_xticklabels([f"{t:.0%}" for t in ths])
b.set_ylim(0.3, 1.08)
C.style_axes(b, "identity threshold of the clusters that are kept together", "test accuracy (nearest neighbor)")
b.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="center left", bbox_to_anchor=(0.01, 0.56))
bio.panel(ax, "A", (0.2, 8.6))
bio.panel(ax, "B", (11.0, 8.6))
