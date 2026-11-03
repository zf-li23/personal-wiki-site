"""Ancestral state reconstruction by empirical Bayes. A and B: marginal posterior probabilities of the
four nucleotides at the internal nodes of a rooted five-taxon tree for one site with tip states T, C, A,
C, C, under K80 with kappa = 2, with short branches (A) and with all branch lengths multiplied by 4 (B);
each bar shows T, C, A, G from left to right, and the most probable joint reconstruction and its
posterior probability are given below. C: a systematic bias (example of Yang 2014). Three
sequences evolve on a star tree with branches of 0.2 under F81 with the base frequencies of the human
mitochondrial D-loop; the expected composition of the root reconstructed by choosing the most probable
nucleotide at every site is more extreme than the true stationary composition, while averaging the
posterior probabilities recovers it."""
import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
NUC = "TCAG"
kappa = 2.0
Q = np.ones((4, 4))
Q[0, 1] = Q[1, 0] = Q[2, 3] = Q[3, 2] = kappa
np.fill_diagonal(Q, 0)
np.fill_diagonal(Q, -Q.sum(1))
Q /= -np.mean(np.diag(Q))
pi = np.full(4, 0.25)

# rooted tree: node -> (parent, branch length); tips 1-5, internal 0 (root), 6, 7, 8
PARENT = {6: (0, 0.1), 8: (0, 0.1), 7: (6, 0.1), 1: (7, 0.15), 2: (7, 0.15), 3: (6, 0.25), 4: (8, 0.2), 5: (8, 0.2)}
TIPS = {1: "T", 2: "C", 3: "A", 4: "C", 5: "C"}
INTERNAL = [0, 6, 7, 8]
CHILD = {v: [c for c, (p, _) in PARENT.items() if p == v] for v in INTERNAL}


def joint_table(scale):
    """Posterior of every assignment of states to the internal nodes (4^4 of them)."""
    M = {c: expm(Q * t * scale) for c, (p, t) in PARENT.items()}
    out = {}
    for states in itertools.product(range(4), repeat=4):
        s = dict(zip(INTERNAL, states))
        pr = pi[s[0]]
        for c, (p, _) in PARENT.items():
            sc = NUC.index(TIPS[c]) if c in TIPS else s[c]
            pr *= M[c][s[p], sc]
        out[states] = pr
    tot = sum(out.values())
    return {k: v / tot for k, v in out.items()}


POS = {1: (0, 4), 2: (0, 3), 3: (0, 2), 4: (0, 1), 5: (0, 0), 7: (-1, 3.5), 6: (-2, 2.75), 8: (-1.5, 0.5), 0: (-3, 1.6)}


def draw(ax, scale, title):
    J = joint_table(scale)
    marg = {v: np.zeros(4) for v in INTERNAL}
    for st, p in J.items():
        for v, s in zip(INTERNAL, st):
            marg[v][s] += p
    for c, (p, _) in PARENT.items():
        (x0, y0), (x1, y1) = POS[p], POS[c]
        ax.plot([x0, x0, x1], [y0, y1, y1], color=P.ink(), lw=1.2)
    for t, s in TIPS.items():
        x, y = POS[t]
        ax.text(x + 0.12, y, s, color=P.NUCLEOTIDE[s], fontsize=FT["normal"], weight="bold", va="center")
    for v in INTERNAL:
        x, y = POS[v]
        w = 0.13
        for k in range(4):
            h = 0.75 * marg[v][k]
            ax.add_patch(plt.Rectangle((x - 0.3 + k * w, y + 0.06), w * 0.9, max(h, 0.005),
                                       color=P.NUCLEOTIDE[NUC[k]], lw=0))
        ax.plot([x - 0.32, x + 0.24], [y + 0.06, y + 0.06], color=P.muted(), lw=0.5)
        best = NUC[int(np.argmax(marg[v]))]
        ax.text(x - 0.05, y - 0.2, f"{best} {marg[v].max():.2f}", fontsize=FT["tiny"], color=P.ink(), ha="center")
    st, p = max(J.items(), key=lambda kv: kv[1])
    ax.text(-1.5, -0.9, "best joint (nodes 0, 6, 7, 8): " + "".join(NUC[s] for s in st) + f", P = {p:.2f}",
            fontsize=FT["tiny"], color=P.ink(), ha="center")
    ax.set_xlim(-3.5, 0.5)
    ax.set_ylim(-1.1, 4.9)
    ax.axis("off")
    charts.title(ax, title)


fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 4.0), gridspec_kw={"width_ratios": [1, 1, 1.05]})
fig.subplots_adjust(left=0.02, right=0.985, bottom=0.14, top=0.9, wspace=0.18)
draw(a, 1.0, "A  Short branches")
draw(b, 4.0, "B  Branches four times longer")

f = np.array([0.2263, 0.3282, 0.3393, 0.1062])
B = 1 - (f ** 2).sum()
e = np.exp(-0.2 / B)
Pm = e * np.eye(4) + (1 - e) * np.outer(np.ones(4), f)
comp_map, comp_mean = np.zeros(4), np.zeros(4)
for pat in itertools.product(range(4), repeat=3):
    jt = f * Pm[:, pat[0]] * Pm[:, pat[1]] * Pm[:, pat[2]]
    tot = jt.sum()
    comp_map[np.argmax(jt)] += tot
    comp_mean += jt
x = np.arange(4)
for k, (vals, tok, lab) in enumerate(((f, "neutral", "true (stationary)"), (comp_map, "negative", "most probable state"),
                                      (comp_mean, "dna", "posterior average"))):
    c.bar(x + (k - 1) * 0.26, vals, 0.25, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, label=lab)
c.set_xticks(x, list(NUC))
c.set_ylim(0, 0.42)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(c, "nucleotide", "frequency at the root")
charts.title(c, "C  Bias of the best reconstruction")
