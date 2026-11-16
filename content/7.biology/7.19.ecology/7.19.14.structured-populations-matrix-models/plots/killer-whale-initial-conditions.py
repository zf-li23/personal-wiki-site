"""Initial conditions, reproductive value and elasticities in the killer whale model.

Matrix of Brault and Caswell (1993) (see killer-whale-projection.py). A: four populations of 250 females
that start entirely in one stage. Plotted is N(t) / (250 lambda1^t), total size relative to growth at the
asymptotic rate: each curve converges to v_j / <v, w> (with w scaled to sum 1), the reproductive value of
the starting stage (Theorem 14.3.2); a population of post-reproductive females dies out. B: the stable
stage distribution w (right eigenvector, proportions) and the reproductive values v (left eigenvector,
scaled so that v of a yearling = 1). C: elasticities e_ij = (a_ij / lambda) dlambda/da_ij of the six
non-zero entries (they sum to 1): survival of reproductive adults in their stage dominates.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
A = np.array([[0, 0.0043, 0.1132, 0],
              [0.9775, 0.9111, 0, 0],
              [0, 0.0736, 0.9534, 0],
              [0, 0, 0.0452, 0.9804]])
names = ["yearling", "juvenile", "reproductive", "post-repr."]
toks = ["atp", "enzyme", "dna", "protein"]
ev, W = np.linalg.eig(A)
i = np.argmax(ev.real)
lam = ev[i].real
w = np.abs(W[:, i].real)
w /= w.sum()
evl, V = np.linalg.eig(A.T)
v = V[:, np.argmax(evl.real)].real
v = v / v[0]
v[np.abs(v) < 1e-12] = 0.0

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 8.0, 6.8))
T = 120
for k in range(4):
    x = np.zeros(4)
    x[k] = 250.0
    rel = []
    for t in range(T + 1):
        rel.append(x.sum() / (250.0 * lam ** t))
        x = A @ x
    pa.plot(np.arange(T + 1), rel, color=Q.line_color(toks[k]), lw=1.6, label=f"all {names[k]}")
    pa.axhline(v[k] / (v @ w), color=Q.line_color(toks[k]), lw=0.7, ls=(0, (3, 2)))
pa.set_xlim(0, T)
pa.set_ylim(0, 2.0)
C.style_axes(pa, "year", "N(t) / (N(0) lambda1^t)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center right", bbox_to_anchor=(1.0, 0.36))
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Starting stage and long-run size", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (13.0, 1.6, 6.5, 6.8))
xs = np.arange(4)
pb.bar(xs - 0.2, w, width=0.38, color=P.fill("dna2"), edgecolor=P.edge("dna2"), lw=0.5, label="w (proportion)")
pb2 = pb.twinx()
pb2.bar(xs + 0.2, v, width=0.38, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.5, label="v (yearling = 1)")
pb.set_xticks(xs)
pb.set_xticklabels(names, fontsize=FS["tiny"], rotation=20)
C.style_axes(pb, None, "stable stage distribution w")
C.style_axes(pb2, None, "reproductive value v", box=True)
pb2.spines["left"].set_visible(False)
pb.spines["right"].set_visible(False)
pb.set_ylim(0, 0.4)
pb2.set_ylim(0, 2.0)
h1, l1 = pb.get_legend_handles_labels()
h2, l2 = pb2.get_legend_handles_labels()
pb.legend(h1 + h2, l1 + l2, frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (11.5, 9.6))
bio.label(ax, (13.0, 9.2), "Right and left eigenvectors", size="small", bold=True, ha="left")

S = np.outer(v, w) / (v @ w)
E = S * A / lam
pc = C.axes_at(ax, (23.5, 1.6, 6.0, 6.8))
idx = [(0, 1), (0, 2), (1, 0), (1, 1), (2, 1), (2, 2)]
labels = ["F juv", "F repr", "yearl -> juv", "juv stays", "juv -> repr", "repr stays"]
vals = [E[a, b] for a, b in idx]
pc.barh(np.arange(len(vals)), vals, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.5)
for k, val in enumerate(vals):
    pc.text(val + 0.01, k, f"{val:.3f}", va="center", fontsize=FS["tiny"], color=P.ink())
pc.set_yticks(np.arange(len(vals)))
pc.set_yticklabels(labels, fontsize=FS["tiny"])
pc.invert_yaxis()
pc.set_xlim(0, 0.75)
C.style_axes(pc, "elasticity of lambda1", None)
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (21.5, 9.2), "Elasticities (sum = 1)", size="small", bold=True, ha="left")
