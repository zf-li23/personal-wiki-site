# Why the RMSD must be normalized: random protein-like chains. Self-avoiding chains of C-alpha atoms are
# generated with a bond length of 3.8 A, virtual bond angles drawn uniformly between 80 and 130 degrees, a
# minimum distance of 4 A between nonadjacent atoms and confinement in a sphere of the radius expected for
# a globular protein of that length (radius of gyration 2.2 N^0.38 A). For each length, 15 pairs of
# unrelated chains are superposed optimally by the Kabsch algorithm. A: the RMSD of the best superposition
# of two unrelated chains grows with the length, so a fixed RMSD threshold means different things for
# short and long proteins. B: the TM-score of the same pairs stays near 0.2 at all lengths, which is what
# the normalization by d0(L) = 1.24 (L - 15)^(1/3) - 1.8 is designed to achieve; the dashed line at 0.5 is
# the usual threshold above which two structures are taken to share a fold.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(1)


def chain(L):
    """A self-avoiding C-alpha chain of L residues inside a sphere of protein-like radius."""
    Rs = np.sqrt(5 / 3) * 2.2 * L ** 0.38
    while True:
        X = np.zeros((L, 3))
        X[0] = [-1.9, 0, 0]
        X[1] = [1.9, 0, 0]
        ok = True
        for i in range(2, L):
            b = X[i - 1] - X[i - 2]
            b /= np.linalg.norm(b)
            for _ in range(200):
                th = np.deg2rad(rng.uniform(80, 130))
                ph = rng.uniform(0, 2 * np.pi)
                a = np.cross(b, [0.3, 0.5, 0.8])
                a /= np.linalg.norm(a)
                c = np.cross(b, a)
                d = -np.cos(th) * b + np.sin(th) * (np.cos(ph) * a + np.sin(ph) * c)
                p = X[i - 1] + 3.8 * d
                if np.linalg.norm(p) > Rs:
                    continue
                if i > 2 and (np.linalg.norm(X[:i - 2] - p, axis=1) < 4.0).any():
                    continue
                X[i] = p
                break
            else:
                ok = False
                break
        if ok:
            return X


def kabsch(A, B):
    am, bm = A.mean(0), B.mean(0)
    U, S, Vt = np.linalg.svd((A - am).T @ (B - bm))
    R = Vt.T @ np.diag([1, 1, np.sign(np.linalg.det(Vt.T @ U.T))]) @ U.T
    return R, bm - R @ am


def d0(L):
    return 1.24 * (L - 15) ** (1 / 3) - 1.8


def tm(A, B):
    n = len(A)
    dd = d0(n)
    best = 0.0
    for frag in sorted({n, n // 2, n // 4, max(8, n // 8)}, reverse=True):
        for s in range(0, n - frag + 1, max(1, frag // 2)):
            sel = np.zeros(n, bool)
            sel[s:s + frag] = True
            for it in range(10):
                R, t = kabsch(A[sel], B[sel])
                di = np.sqrt((((A @ R.T + t) - B) ** 2).sum(1))
                best = max(best, (1 / (1 + (di / dd) ** 2)).mean())
                new = di < dd + (1.5 if it else 0.0)
                if new.sum() < 3 or (new == sel).all():
                    break
                sel = new
    return best


Ls = [50, 100, 150, 200, 300, 400]
rm, ts = [], []
for L in Ls:
    r, s = [], []
    for _ in range(15):
        A, B = chain(L), chain(L)
        R, t = kabsch(A, B)
        r.append(np.sqrt((((A @ R.T + t) - B) ** 2).sum(1).mean()))
        s.append(tm(A, B))
    rm.append(r)
    ts.append(s)
rm, ts = np.array(rm), np.array(ts)

fig, ax = bio.canvas(22.0, 9.0)
a = C.axes_at(ax, (2.0, 1.4, 8.0, 7.0))
a.errorbar(Ls, rm.mean(1), yerr=rm.std(1), fmt="o-", color=C.line("negative"), lw=1.3, ms=4, capsize=2)
a.plot(Ls, [0.8 * L ** 0.38 * 2.2 for L in Ls], ls=(0, (4, 2)), color=P.muted(), lw=1.0)
a.text(260, 13, "proportional to the radius\nof gyration", fontsize=FT["tiny"], color=P.muted())
C.style_axes(a, "chain length (residues)", "RMSD of unrelated chains (Å)")
a.set_ylim(0, 30)
b = C.axes_at(ax, (13.0, 1.4, 8.0, 7.0))
b.errorbar(Ls, ts.mean(1), yerr=ts.std(1), fmt="o-", color=C.line("dna"), lw=1.3, ms=4, capsize=2)
b.axhline(0.5, color=P.muted(), ls=(0, (4, 2)), lw=1.0)
b.text(60, 0.52, "same fold above 0.5", fontsize=FT["tiny"], color=P.muted())
b.set_ylim(0, 0.7)
C.style_axes(b, "chain length (residues)", "TM-score of unrelated chains")
bio.panel(ax, "A", (0.2, 8.6))
bio.panel(ax, "B", (11.2, 8.6))
