"""Tree shape decides which method wins (after Swofford and colleagues 2001). Data of 1000 sites are
simulated under JC69 on four-taxon trees with two long external branches (0.5 substitutions per site),
two short ones (0.05) and an internal branch t0. Left (Farris zone): the long branches are sisters,
((a, b), (c, d)) with a and b long; right (Felsenstein zone): they are not, ((a, c), (b, d)) with a and b
long. At t0 = 0 the true tree is the star. The probability of recovering the true tree, from 30 data
sets per point, by maximum parsimony and by maximum likelihood under JC69 with branch lengths optimized
for each of the three topologies. Parsimony is nearly always right in the Farris zone and nearly always
wrong in the Felsenstein zone; likelihood is consistent in both, but in the Farris zone it is less
accurate than the biased method whose bias happens to point to the truth."""
import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

# canonical site patterns of four taxa (states relabeled in order of first appearance)
CANON = []
for pat in itertools.product(range(4), repeat=4):
    seen, lab = {}, []
    for s in pat:
        seen.setdefault(s, len(seen))
        lab.append(seen[s])
    if tuple(lab) not in CANON:
        CANON.append(tuple(lab))
CANON = np.array(CANON)                      # 15 x 4
INDEX = {tuple(c): k for k, c in enumerate(CANON)}
LOOKUP = np.zeros(256, int)
for pat in itertools.product(range(4), repeat=4):
    seen, lab = {}, []
    for s in pat:
        seen.setdefault(s, len(seen))
        lab.append(seen[s])
    LOOKUP[pat[0] * 64 + pat[1] * 16 + pat[2] * 4 + pat[3]] = INDEX[tuple(lab)]
# the three unrooted topologies as taxon orders (pairs (0,1)|(2,3))
TOPO = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]


def pjc(t):
    e = np.exp(-4 * t / 3)
    return 0.25 + 0.75 * e, 0.25 - 0.25 * e


def jc_matrix(t):
    s, d = pjc(t)
    return np.full((4, 4), d) + (s - d) * np.eye(4)


def pattern_probs(b, order):
    """b = (t1, t2, t3, t4, t0) for tips in `order`: ((o0, o1), (o2, o3)); returns prob of each canonical pattern."""
    M = [jc_matrix(x) for x in b]
    X = CANON[:, list(order)]                  # states of the tips in topology order
    A = 0.25 * M[0][:, X[:, 0]] * M[1][:, X[:, 1]]       # 4 x 15 (state a at node u)
    Bm = M[2][:, X[:, 2]] * M[3][:, X[:, 3]]             # 4 x 15 (state b at node v)
    return np.einsum("ak,ab,bk->k", A, M[4], Bm)


def simulate(b, n, rng):
    """Simulate n sites on ((0,1),(2,3)) with branch lengths b = (t1..t4, t0); return canonical counts."""
    a = rng.integers(0, 4, n)

    def evolve(x, t):
        s, _ = pjc(t)
        ch = rng.random(n) > s
        return np.where(ch, (x + rng.integers(1, 4, n)) % 4, x)
    u = a
    v = evolve(u, b[4])
    tips = np.stack([evolve(u, b[0]), evolve(u, b[1]), evolve(v, b[2]), evolve(v, b[3])], 1)
    code = tips @ np.array([64, 16, 4, 1])
    return np.bincount(LOOKUP[code], minlength=15).astype(float)


def fit(counts, order):
    def nll(x):
        p = pattern_probs(np.exp(x), order)
        return -(counts * np.log(p)).sum()
    best = None
    for x0 in (np.log([0.1] * 5),):
        r = minimize(nll, x0, method="L-BFGS-B", bounds=[(-12, 2)] * 5)
        if best is None or r.fun < best.fun:
            best = r
    return -best.fun, np.log(pattern_probs(np.exp(best.x), order))


INFORMATIVE = [INDEX[(0, 0, 1, 1)], INDEX[(0, 1, 0, 1)], INDEX[(0, 1, 1, 0)]]   # support TOPO[0], [1], [2]
rng = np.random.default_rng(1)
L, S, n, reps = 0.5, 0.05, 1000, 30
t0s = np.array([0.01, 0.02, 0.035, 0.05])
res = {}
for zone in ("farris", "felsenstein"):
    pml, pmp = [], []
    for t0 in t0s:
        # simulate on ((0,1),(2,3)); the long branches are taxa 0 and 1 (Farris) or 0 and 2 (Felsenstein)
        b = (L, L, S, S, t0) if zone == "farris" else (L, S, L, S, t0)
        ok_ml = ok_mp = 0.0
        for _ in range(reps):
            c = simulate(b, n, rng)
            ll = [fit(c, o)[0] for o in TOPO]
            ok_ml += float(np.argmax(ll) == 0)
            sup = c[INFORMATIVE]
            best = np.flatnonzero(sup == sup.max())
            ok_mp += float(0 in best) / len(best)
        pml.append(ok_ml / reps)
        pmp.append(ok_mp / reps)
    res[zone] = (np.array(pml), np.array(pmp))

fig, ax = plt.subplots(figsize=(8.0, 3.9))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.2, top=0.88)
x_f, x_z = -t0s, t0s
for xs, zone in ((x_f, "farris"), (x_z, "felsenstein")):
    ml, mp = res[zone]
    ax.plot(xs, ml, "o-", color=charts.line("dna"), lw=1.5, ms=4, label="likelihood (JC69)" if zone == "farris" else None)
    ax.plot(xs, mp, "s-", color=charts.line("rna"), lw=1.5, ms=4, label="parsimony" if zone == "farris" else None)
ax.axvline(0, color=P.muted(), lw=0.8, ls=":")
ax.axhline(1 / 3, color=P.muted(), lw=0.6, ls="--")
ax.text(-0.03, 1.07, "Farris zone: long branches are sisters", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.text(0.03, 1.07, "Felsenstein zone: long branches apart", ha="center", fontsize=FT["tiny"], color=P.ink())
ax.set_xticks([-0.05, -0.025, 0, 0.025, 0.05], ["0.05", "0.025", "0", "0.025", "0.05"])
ax.set_ylim(-0.03, 1.12)
ax.set_xlim(-0.056, 0.056)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left")
charts.style_axes(ax, "internal branch length $t_0$", "probability of the true tree")
