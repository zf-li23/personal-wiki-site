"""Elasticity analysis of the loggerhead sea turtle (Crouse, Crowder and Caswell 1987).

Stage-classified matrix for loggerheads (Caretta caretta) nesting on Little Cumberland Island, Georgia
(seven stages: eggs and hatchlings, small juveniles, large juveniles, subadults, novice breeders, first-year
remigrants, mature breeders), as published by Crouse et al. (1987); lambda1 = 0.945. Stage survival
sigma_i is split into staying (P_i) and growing to the next stage (G_i); F_i are fecundities.
A: elasticities of lambda1 summed for each stage and type of transition (they sum to 1). B: lambda1 after
reducing the annual mortality 1 - sigma_i of a single stage by half (keeping the proportions of staying
and growing), or after a 50 % increase in fecundity; the dashed line is lambda = 1, the solid line the
original lambda1. No single change reaches replacement, but the largest gains come from the survival of
large juveniles, subadults and small juveniles; protecting eggs and nests (stage 1) does little.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
A = np.array([[0, 0, 0, 0, 127, 4, 80],
              [0.6747, 0.7370, 0, 0, 0, 0, 0],
              [0, 0.0486, 0.6610, 0, 0, 0, 0],
              [0, 0, 0.0147, 0.6907, 0, 0, 0],
              [0, 0, 0, 0.0518, 0, 0, 0],
              [0, 0, 0, 0, 0.8091, 0, 0],
              [0, 0, 0, 0, 0, 0.8091, 0.8089]])
stages = ["eggs/\nhatchlings", "small\njuveniles", "large\njuveniles", "subadults", "novice\nbreeders",
          "remigrants", "mature\nbreeders"]


def lam_vecs(M):
    ev, W = np.linalg.eig(M)
    i = np.argmax(ev.real)
    lam = ev[i].real
    w = np.abs(W[:, i].real)
    evl, V = np.linalg.eig(M.T)
    v = np.abs(V[:, np.argmax(evl.real)].real)
    return lam, w, v


lam, w, v = lam_vecs(A)
E = np.outer(v, w) * A / (lam * (v @ w))
fec = E[0, :]
stay = np.diag(E).copy()
stay[0] = 0.0
grow = np.array([E[i + 1, i] for i in range(6)] + [0.0])

fig, ax = bio.canvas(30.0, 10.5)
pa = C.axes_at(ax, (2.0, 2.2, 12.0, 6.6))
x = np.arange(7)
pa.bar(x, fec, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.5, label="fecundity F")
pa.bar(x, stay, bottom=fec, color=P.fill("dna2"), edgecolor=P.edge("dna2"), lw=0.5, label="stay in stage P")
pa.bar(x, grow, bottom=fec + stay, color=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.5,
       label="grow to next stage G")
pa.set_xticks(x)
pa.set_xticklabels(stages, fontsize=FS["tiny"])
C.style_axes(pa, None, "elasticity of lambda1")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper center")
pa.set_ylim(0, 0.35)
bio.panel(ax, "A", (0.3, 10.1))
bio.label(ax, (2.0, 9.7), f"Elasticities by stage (lambda1 = {lam:.3f})", size="small", bold=True, ha="left")

out = []
for i in range(7):
    M = A.copy()
    sig = M[i, i] + (M[i + 1, i] if i < 6 else 0.0)
    if sig > 0:
        new = 1 - 0.5 * (1 - sig)
        M[i, i] *= new / sig
        if i < 6:
            M[i + 1, i] *= new / sig
    out.append(lam_vecs(M)[0])
Mf = A.copy()
Mf[0, :] *= 1.5
out.append(lam_vecs(Mf)[0])
pb = C.axes_at(ax, (18.0, 2.2, 11.0, 6.6))
xb = np.arange(8)
cols = [P.fill("dna2")] * 7 + [P.fill("rna")]
edges = [P.edge("dna2")] * 7 + [P.edge("rna")]
pb.bar(xb, out, color=cols, edgecolor=edges, lw=0.5)
pb.axhline(1.0, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pb.axhline(lam, color=P.muted(), lw=0.6)
pb.set_xticks(xb)
pb.set_xticklabels([s.replace("\n", " ").replace("eggs/ ", "eggs/") for s in stages] + ["fecundity\n+50 %"],
                   fontsize=FS["tiny"] - 1, rotation=35, ha="right")
pb.set_ylim(0.93, 1.005)
C.style_axes(pb, None, "lambda1 after the change")
bio.panel(ax, "B", (16.5, 10.1))
bio.label(ax, (18.0, 9.7), "Halving the mortality of one stage", size="small", bold=True, ha="left")
