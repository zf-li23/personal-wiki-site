# Structural superposition of the two conformations of adenylate kinase of Escherichia coli: the open
# apo form (PDB 4AKE, chain A) and the closed form with the inhibitor Ap5A (PDB 1AKE, chain A), 214
# matched C-alpha atoms (adenylate-kinase-ca.csv, coordinates from the Protein Data Bank). The optimal
# rotation and translation are computed by the Kabsch algorithm (singular value decomposition);
# the TM-score uses the iterative search described in the text. A: the two chains after global
# superposition, colored by domain (CORE, NMP-binding, LID). B: the per-residue distance after the global
# fit and after fitting on the CORE domain only. C: the RMSD of the whole molecule and of each domain
# superposed on its own, showing that the domains are internally rigid and move relative to each other.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
D = np.loadtxt("adenylate-kinase-ca.csv", delimiter=",", skiprows=1)
idx = D[:, 0].astype(int)
X, Y = D[:, 1:4], D[:, 4:7]
n = len(X)
CORE = (idx <= 29) | ((idx >= 60) & (idx <= 121)) | (idx >= 160)
NMP = (idx >= 30) & (idx <= 59)
LID = (idx >= 122) & (idx <= 159)


def kabsch(A, B):
    am, bm = A.mean(0), B.mean(0)
    U, S, Vt = np.linalg.svd((A - am).T @ (B - bm))
    d = np.sign(np.linalg.det(Vt.T @ U.T))
    R = Vt.T @ np.diag([1, 1, d]) @ U.T
    return R, bm - R @ am


def rmsd(A, B):
    return np.sqrt(((A - B) ** 2).sum(1).mean())


def d0(L):
    return 1.24 * (L - 15) ** (1 / 3) - 1.8


def tm_score(A, B, L=None):
    L = L or len(A)
    dd, n_ = d0(L), len(A)
    best = 0.0
    for frag in sorted({n_, n_ // 2, n_ // 4, max(8, n_ // 8)}, reverse=True):
        for s in range(0, n_ - frag + 1, max(1, frag // 2)):
            sel = np.zeros(n_, bool)
            sel[s:s + frag] = True
            for it in range(20):
                R, t = kabsch(A[sel], B[sel])
                di = np.sqrt((((A @ R.T + t) - B) ** 2).sum(1))
                best = max(best, (1 / (1 + (di / dd) ** 2)).sum() / L)
                new = di < dd + (1.5 if it else 0.0)
                if new.sum() < 3 or (new == sel).all():
                    break
                sel = new
    return best


R, t = kabsch(X, Y)
Xg = X @ R.T + t
Rc, tc = kabsch(X[CORE], Y[CORE])
Xc = X @ Rc.T + tc
rows = [("whole chain", np.ones(n, bool)), ("CORE", CORE), ("NMP", NMP), ("LID", LID)]
stats = []
for name, m in rows:
    Rm, tm_ = kabsch(X[m], Y[m])
    stats.append((name, int(m.sum()), rmsd(X[m] @ Rm.T + tm_, Y[m]),
                  tm_score(X, Y) if name == "whole chain" else None))

fig, ax = bio.canvas(28.0, 10.5)
a = C.axes_at(ax, (0.8, 1.2, 10.0, 8.6))
pc = np.linalg.svd(np.vstack([Xg, Y]) - np.vstack([Xg, Y]).mean(0), full_matrices=False)[2][:2]


def proj(V):
    return (V - np.vstack([Xg, Y]).mean(0)) @ pc.T


for V, style, lab in ((proj(Y), "-", "closed (1AKE)"), (proj(Xg), "--", "open (4AKE), superposed")):
    for m, tok in ((CORE, "protein"), (NMP, "enzyme"), (LID, "receptor")):
        seg = np.where(m)[0]
        for k in np.split(seg, np.where(np.diff(seg) > 1)[0] + 1):
            a.plot(V[k, 0], V[k, 1], style, color=C.line(tok), lw=1.3)
    a.plot([], [], style, color=P.muted(), label=lab)
a.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower right")
for nm, m, tok in (("CORE", CORE, "protein"), ("NMP", NMP, "enzyme"), ("LID", LID, "receptor")):
    c0 = proj(Y[m]).mean(0)
    a.text(c0[0], c0[1] + 3.0, nm, color=C.line(tok), fontsize=FT["small"], ha="center")
a.set_aspect("equal")
a.axis("off")
bio.panel(ax, "A", (0.2, 10.1))
b = C.axes_at(ax, (13.0, 1.2, 8.6, 8.6))
b.plot(idx, np.sqrt(((Xg - Y) ** 2).sum(1)), color=C.line("negative"), lw=1.2, label="global superposition")
b.plot(idx, np.sqrt(((Xc - Y) ** 2).sum(1)), color=C.line("dna"), lw=1.2, label="CORE superposition")
for m, tok in ((NMP, "enzyme"), (LID, "receptor")):
    b.axvspan(idx[m].min(), idx[m].max(), color=P.mix(P.light(tok), P.surface(), 0.5), lw=0)
b.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
C.style_axes(b, "residue", "distance after superposition (Å)")
bio.panel(ax, "B", (11.8, 10.1))
c = C.axes_at(ax, (24.0, 1.2, 3.4, 8.6))
ys = np.arange(len(stats))[::-1]
c.barh(ys, [s[2] for s in stats], color=C.line("negative"), height=0.5)
for y_, s in zip(ys, stats):
    c.text(0.3, y_, f"{s[0]} ({s[1]} res)", va="bottom", fontsize=FT["tiny"], color=P.ink())
    txt = f"RMSD {s[2]:.2f} Å" + (f", TM-score {s[3]:.2f}" if s[3] else "")
    c.text(0.3, y_ - 0.3, txt, va="top", fontsize=FT["tiny"], color=P.muted())
c.set_yticks([])
c.set_xlim(0, 8.5)
C.style_axes(c, "RMSD after own superposition (Å)", None)
c.spines["left"].set_visible(False)
bio.panel(ax, "C", (23.0, 10.1))
