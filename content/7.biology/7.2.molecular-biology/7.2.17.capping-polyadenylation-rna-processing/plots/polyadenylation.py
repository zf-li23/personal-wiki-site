# Mammalian 3'-end processing and the two phases of poly(A) synthesis.
# A: the signals around a poly(A) site: an upstream UGUA element bound by CFIm, the AAUAAA hexamer 10-30 nt
# upstream of the cleavage site (usually after a CA) bound by CPSF (CPSF30 and WDR33), and a GU-rich or
# U-rich downstream element (DSE) within about 30 nt bound by CstF64; CPSF73 cleaves, poly(A) polymerase
# (PAP) adds A residues to the new 3' end, and the nuclear poly(A)-binding protein PABPN1 coats the tail.
# B: master-equation model of tail growth on a cleaved substrate. Each A is added at rate k_n: slow
# initiation k_i = 0.02 /s for n < 10 (requires AAUAAA and CPSF), fast PABPN1-stimulated elongation
# k_e = 2 /s for 10 <= n < 250, and no further addition at 250 (length control). Curves: mean tail length for
# the wild-type signal, for a mutant AAUAAA (k_i 50-fold lower) and for the same mutant substrate carrying a
# preformed A10 tail (elongation no longer needs the signal). Inset bars: distribution of tail lengths of
# the wild-type substrate at 2, 5 and 10 min (fraction per 10-nt bin, short tails < 10 drawn as one bar).
import numpy as np
from scipy.linalg import expm
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 10.5)

# --- A ---------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.35))
y = 6.0
ax.plot([0.8, 11.8], [y, y], color=P.edge("rna"), lw=2.0, zorder=4)
bio.label(ax, (0.5, y), "5′", size="tiny", bold=True)
bio.label(ax, (12.1, y), "3′", size="tiny", bold=True)
X = {"UGUA": 2.2, "AAUAAA": 5.0, "CA": 7.3, "DSE": 9.4}
for name, xx in X.items():
    w = 1.5 if name in ("AAUAAA", "DSE") else 1.0 if name == "UGUA" else 0.6
    bio.box(ax, (xx, y), w, 0.5, token="highlight", text=name if name != "DSE" else "GU/U-rich", size="tiny", radius=0.06, zorder=6)
ax.plot([7.62, 7.62], [y - 0.6, y + 0.6], color=P.edge("negative"), lw=1.2, ls=(0, (2, 1.4)), zorder=7)
bio.label(ax, (7.75, y + 0.62), "cleavage", ha="left", size="tiny", color=P.edge("negative"))
Q.bracket(ax, (5.75, y - 0.55), (7.6, y - 0.55), text="10–30 nt", side=1)
Q.bracket(ax, (7.65, y - 0.55), (10.15, y - 0.55), text="< 30 nt", side=1)
bio.protein(ax, (2.2, y + 1.3), 1.5, 0.85, "receptor", text="CFIm", size="tiny")
bio.protein(ax, (5.3, y + 1.45), 2.6, 1.1, "protein", text="CPSF (30, WDR33, 73)", size="tiny")
bio.protein(ax, (9.4, y + 1.3), 1.6, 0.85, "enzyme", text="CstF64", size="tiny")
bio.protein(ax, (7.6, y + 2.75), 2.9, 0.85, "positive", text="CFIIm, symplekin", size="tiny")
for xx, yy in ((2.2, y + 0.88), (5.0, y + 0.9), (9.4, y + 0.88)):
    ax.plot([xx, xx], [yy, y + 0.27], color=P.muted(), lw=0.7)
bio.label(ax, (6.3, 9.7), "3′-end processing complex on the pre-mRNA", size="small", bold=True)
# after cleavage: tail
y2 = 2.4
ax.plot([0.8, 7.6], [y2, y2], color=P.edge("rna"), lw=2.0, zorder=4)
bio.box(ax, (5.0, y2), 1.5, 0.5, token="highlight", text="AAUAAA", size="tiny", radius=0.06, zorder=6)
for k in range(10):
    xx = 7.85 + k * 0.33
    bio.label(ax, (xx, y2), "A", size="tiny", bold=True, color=P.edge("mrna"))
    if k % 2 == 0:
        bio.molecule(ax, (xx + 0.18, y2 + 0.5), token="antibody", r=0.17)
bio.label(ax, (9.5, y2 + 1.05), "PABPN1", size="tiny", color=P.muted())
bio.protein(ax, (12.2, y2), 1.2, 0.8, "enzyme", text="PAP", size="tiny")
bio.label(ax, (9.6, y2 - 0.6), "≈ 250 A in mammals", size="tiny", color=P.muted())
bio.arrow(ax, (6.3, y - 2.3), (6.3, y2 + 0.85), kind="process")
bio.label(ax, (6.55, (y + y2) / 2 - 0.2), "cleave, then add A", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.5, y2), "5′", size="tiny", bold=True)
# --- B: kinetics ----------------------------------------------------------------------------------------------
bio.panel(ax, "B", (13.6, 10.35))
N = 250


def rates(ki, ke=2.0, n0=10):
    k = np.where(np.arange(N + 1) < n0, ki, ke).astype(float)
    k[N] = 0.0
    return k


def generator(k):
    A = np.zeros((N + 1, N + 1))
    for n in range(N + 1):
        A[n, n] -= k[n]
        if n < N:
            A[n + 1, n] += k[n]
    return A


ts = np.linspace(0, 900, 91)  # s
lens = np.arange(N + 1)
curves = {}
for name, ki, start in (("wt", 0.02, 0), ("mut", 0.0004, 0), ("mutA10", 0.0004, 10)):
    A = generator(rates(ki))
    p0 = np.zeros(N + 1)
    p0[start] = 1
    dt = ts[1] - ts[0]
    E = expm(A * dt)
    p = p0.copy()
    means, snaps = [], {}
    for j, t in enumerate(ts):
        means.append(lens @ p)
        snaps[round(t)] = p.copy()
        p = E @ p
    curves[name] = (np.array(means), snaps)

pl = Q.Plot(ax, (15.2, 1.4, 5.6, 7.6), xlim=(0, 15), ylim=(0, 260), xlabel="t / min", ylabel="mean poly(A) length / nt",
            xticks=[0, 5, 10, 15], yticks=[0, 50, 100, 150, 200, 250])
pl.line(ts / 60, curves["wt"][0], "positive", text="AAUAAA", at=0.62, dx=0.2, dy=-0.1)
pl.line(ts / 60, curves["mut"][0], "negative", text="AAUAGA (mutant)", at=0.55, dy=0.3)
pl.line(ts / 60, curves["mutA10"][0], "dna", dashed=True, text="mutant + preformed A10", at=0.1, dx=0.2, dy=0.1)

# distributions of the wild type
bins = np.arange(10, 251, 10)
for k, (tmin, yy) in enumerate(((2, 7.0), (5, 4.4), (10, 1.8))):
    p = curves["wt"][1][tmin * 60]
    h = [p[:10].sum()] + [p[b:b + 10].sum() for b in bins[:-1]] + [p[250]]
    edges = np.r_[0, bins, 260]
    q = Q.Plot(ax, (22.0, yy, 2.6, 1.7), xlim=(0, 260), ylim=(0, 1.0), frame="l",
               xticks=[0, 250] if k == 2 else None, yticks=None)
    q.bars(edges, h, token="positive")
    bio.label(ax, (23.3, yy + 1.95), f"{tmin} min", size="tiny", color=P.muted())
bio.label(ax, (23.3, 0.6), "tail length / nt", size="tiny")
