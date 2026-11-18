"""Null-model analysis of species co-occurrence with the C-score (Stone and Roberts 1990).

Two simulated presence-absence matrices (18 species x 30 islands; species = rows). "Structured": each
species has its own occupancy probability, and the species are grouped into nine pairs that are forced into checkerboards (on
each island a member of a pair is removed when its partner is present, as Diamond proposed for
competitors). "Random": the same occupancy probabilities, no interactions. The C-score of a pair is
(R_i - S)(R_j - S), with R_i, R_j the numbers of islands occupied and S the number shared; the statistic is
its mean over all pairs. Null matrices preserve both the row sums (how widespread each species is) and the
column sums (how rich each island is): fixed-fixed randomization by the curveball algorithm (Strona et al.
2014), 1000 null matrices each after 5000 trades. A: the structured matrix with species and islands sorted
by frequency (filled = present). B: null distributions, standardized, and observed values (vertical lines) for the two
matrices as standardized effect sizes SES = (observed - mean null)/sd null; the grey band is |SES| < 2. Data are simulated.
"""

import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)

n_sp, n_is = 18, 30
p_occ = rng.uniform(0.3, 0.6, n_sp)


def make(structured):
    M = (rng.random((n_sp, n_is)) < p_occ[:, None]).astype(int)
    if structured:
        for a in range(0, 18, 2):
            both = (M[a] == 1) & (M[a + 1] == 1)
            loser = rng.random(n_is) < 0.5
            M[a, both & loser] = 0
            M[a + 1, both & ~loser] = 0
    return M


def cscore(M):
    R = M.sum(axis=1)
    S = M @ M.T
    Cm = (R[:, None] - S) * (R[None, :] - S)
    iu = np.triu_indices(M.shape[0], 1)
    return Cm[iu].mean()


def curveball(M, trades):
    rows = [set(np.flatnonzero(r)) for r in M]
    n = len(rows)
    for _ in range(trades):
        i, j = rng.choice(n, 2, replace=False)
        a, b = rows[i], rows[j]
        only_a, only_b = list(a - b), list(b - a)
        pool = only_a + only_b
        if not only_a or not only_b:
            continue
        rng.shuffle(pool)
        k = len(only_a)
        common = a & b
        rows[i] = common | set(pool[:k])
        rows[j] = common | set(pool[k:])
    out = np.zeros_like(M)
    for i, r in enumerate(rows):
        out[i, list(r)] = 1
    return out


def structured_label(name):
    return name == "structured"


results = {}
for name, structured in (("structured", True), ("random", False)):
    M = make(structured)
    obs = cscore(M)
    null = []
    X = M.copy()
    X = curveball(X, 5000)
    for _ in range(1000):
        X = curveball(X, 200)
        null.append(cscore(X))
    null = np.array(null)
    results[name] = (M, obs, null, (obs - null.mean()) / null.std())

fig, ax = bio.canvas(30.0, 10.5)

pa = C.axes_at(ax, (2.4, 1.6, 10.0, 6.8))
M = results["structured"][0]
ro = np.argsort(-M.sum(axis=1))
co = np.argsort(-M.sum(axis=0))
Ms = M[ro][:, co]
for i in range(n_sp):
    for j in range(n_is):
        if Ms[i, j]:
            pa.add_patch(Rectangle(
                (j - 0.42, n_sp - 1 - i - 0.42), 0.84, 0.84, color=Q.line_color("dna"), lw=0))
pa.set_xlim(-0.8, n_is - 0.2)
pa.set_ylim(-0.8, n_sp - 0.2)
pa.set_xticks([])
pa.set_yticks([])
C.style_axes(pa, "islands (richest on the left)", "species (most widespread on top)")
bio.panel(ax, "A", (0.6, 10.0))
bio.label(ax, (2.4, 9.6), "Presence–absence matrix (structured)", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (16.0, 1.6, 12.6, 6.8))
for name, tok in (("structured", "negative"), ("random", "dna")):
    _, obs, null, ses = results[name]
    c = Q.line_color(tok)
    z = (null - null.mean()) / null.std()
    pb.hist(z, bins=np.linspace(-4, 4, 41), color=c, alpha=0.4, lw=0, label=f"null, {name} matrix")
    pb.axvline(ses, color=c, lw=1.8)
    pb.text(ses + 0.15, 100 if structured_label(name) else 92, f"{name}: SES = {ses:.1f}", fontsize=FS["tiny"], color=c)
pb.set_ylim(0, 108)
pb.axvspan(-2, 2, color=P.muted(), alpha=0.08, lw=0)
pb.set_xlim(-4, max(4, results["structured"][3] + 2.5))
C.style_axes(pb, "standardized C-score (observed or null − null mean) / null sd", "number of null matrices")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (14.4, 10.0))
bio.label(ax, (16.0, 9.6), "Fixed–fixed null distributions", size="small", bold=True, ha="left")
