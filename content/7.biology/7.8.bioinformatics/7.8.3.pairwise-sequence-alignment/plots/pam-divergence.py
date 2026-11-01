# PAM matrices as powers of one Markov transition matrix. The mutation probabilities of PAM250 are recovered
# from Dayhoff's published log-odds matrix (log10 of M250[i, j] / f_i, Schwartz and Dayhoff 1978) and the
# amino acid frequencies f of the same work; the 1-PAM matrix is the 250th root of M250 (computed by
# symmetrizing with diag(f)^(1/2), since the chain is reversible) rescaled to exactly 1 % expected change.
# A: expected percent difference between two sequences n PAM apart, sum_j f_j (1 - M^n[j, j]), with the
# correspondence tabulated by Dayhoff (points). B: relative entropy of the PAM n log-odds matrix in bits per
# aligned pair; the dashed lines are BLOSUM matrices evaluated with the background frequencies used by BLAST.
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C

P = bio.P
AA = "ARNDCQEGHILKMFPSTWYV"
MDM78 = [
    "0.18 -0.15 0.02 0.03 -0.20 -0.04 0.03 0.13 -0.14 -0.05 -0.19 -0.12 -0.11 -0.35 0.11 0.11 0.12 -0.58 -0.35 0.02",
    "-0.15 0.61 0.00 -0.13 -0.36 0.13 -0.11 -0.26 0.16 -0.20 -0.30 0.34 -0.04 -0.45 -0.02 -0.03 -0.09 0.22 -0.42 -0.25",
    "0.02 0.00 0.20 0.21 -0.36 0.08 0.14 0.03 0.16 -0.18 -0.29 0.10 -0.17 -0.35 -0.05 0.07 0.04 -0.42 -0.21 -0.17",
    "0.03 -0.13 0.21 0.39 -0.51 0.16 0.34 0.06 0.07 -0.24 -0.40 0.01 -0.26 -0.56 -0.10 0.03 -0.01 -0.68 -0.43 -0.21",
    "-0.20 -0.36 -0.36 -0.51 1.19 -0.54 -0.53 -0.34 -0.34 -0.23 -0.60 -0.54 -0.52 -0.43 -0.28 0.00 -0.22 -0.78 0.03 -0.19",
    "-0.04 0.13 0.08 0.16 -0.54 0.40 0.25 -0.12 0.29 -0.20 -0.18 0.07 -0.10 -0.47 0.02 -0.05 -0.08 -0.48 -0.40 -0.19",
    "0.03 -0.11 0.14 0.34 -0.53 0.25 0.38 0.02 0.07 -0.20 -0.34 -0.01 -0.21 -0.54 -0.06 0.00 -0.04 -0.70 -0.43 -0.18",
    "0.13 -0.26 0.03 0.06 -0.34 -0.12 0.02 0.48 -0.21 -0.26 -0.41 -0.17 -0.28 -0.48 -0.05 0.11 0.00 -0.70 -0.52 -0.14",
    "-0.14 0.16 0.16 0.07 -0.34 0.29 0.07 -0.21 0.65 -0.24 -0.21 0.00 -0.21 -0.18 -0.02 -0.08 -0.13 -0.28 -0.01 -0.22",
    "-0.05 -0.20 -0.18 -0.24 -0.23 -0.20 -0.20 -0.26 -0.24 0.45 0.24 -0.19 0.22 0.10 -0.20 -0.14 0.01 -0.51 -0.09 0.37",
    "-0.19 -0.30 -0.29 -0.40 -0.60 -0.18 -0.34 -0.41 -0.21 0.24 0.59 -0.29 0.37 0.18 -0.25 -0.28 -0.17 -0.18 -0.09 0.19",
    "-0.12 0.34 0.10 0.01 -0.54 0.07 -0.01 -0.17 0.00 -0.19 -0.29 0.47 0.04 -0.53 -0.11 -0.02 0.00 -0.35 -0.44 -0.24",
    "-0.11 -0.04 -0.17 -0.26 -0.52 -0.10 -0.21 -0.28 -0.21 0.22 0.37 0.04 0.64 0.02 -0.21 -0.16 -0.06 -0.42 -0.24 0.18",
    "-0.35 -0.45 -0.35 -0.56 -0.43 -0.47 -0.54 -0.48 -0.18 0.10 0.18 -0.53 0.02 0.91 -0.46 -0.32 -0.31 0.04 0.70 -0.12",
    "0.11 -0.02 -0.05 -0.10 -0.28 0.02 -0.06 -0.05 -0.02 -0.20 -0.25 -0.11 -0.21 -0.46 0.59 0.09 0.03 -0.56 -0.49 -0.12",
    "0.11 -0.03 0.07 0.03 0.00 -0.05 0.00 0.11 -0.08 -0.14 -0.28 -0.02 -0.16 -0.32 0.09 0.16 0.13 -0.25 -0.28 -0.10",
    "0.12 -0.09 0.04 -0.01 -0.22 -0.08 -0.04 0.00 -0.13 0.01 -0.17 0.00 -0.06 -0.31 0.03 0.13 0.26 -0.52 -0.27 0.03",
    "-0.58 0.22 -0.42 -0.68 -0.78 -0.48 -0.70 -0.70 -0.28 -0.51 -0.18 -0.35 -0.42 0.04 -0.56 -0.25 -0.52 1.73 -0.02 -0.62",
    "-0.35 -0.42 -0.21 -0.43 0.03 -0.40 -0.43 -0.52 -0.01 -0.09 -0.09 -0.44 -0.24 0.70 -0.49 -0.28 -0.27 -0.02 1.01 -0.25",
    "0.02 -0.25 -0.17 -0.21 -0.19 -0.19 -0.18 -0.14 -0.22 0.37 0.19 -0.24 0.18 -0.12 -0.12 -0.10 0.03 -0.62 -0.25 0.43",
]
L = np.array([[float(v) for v in r.split()] for r in MDM78])
freq = dict(G=.089, A=.087, L=.085, K=.081, S=.070, V=.065, T=.058, P=.051, E=.050, D=.047, R=.041, N=.040,
            F=.040, Q=.038, I=.037, H=.034, C=.033, Y=.030, M=.015, W=.010)
f = np.array([freq[a] for a in AA])
f = f / f.sum()
M250 = f[:, None] * 10 ** L          # M250[i, j] = P(j is replaced by i in 250 PAM)
M250 = M250 / M250.sum(axis=0)
Dh, Dih = np.diag(np.sqrt(f)), np.diag(1 / np.sqrt(f))
S = Dih @ M250 @ Dh
w, V = np.linalg.eigh((S + S.T) / 2)
w = np.clip(w, 1e-9, None)


def M(t):
    return Dh @ V @ np.diag(w ** t) @ V.T @ Dih


t1 = brentq(lambda t: 1 - (f * np.diag(M(t))).sum() - 0.01, 1e-5, 0.1)
n = np.arange(1, 401)
diff, H = [], []
for k in n:
    Mk = np.clip(M(t1 * k), 1e-12, None)
    diff.append(100 * (1 - (f * np.diag(Mk)).sum()))
    H.append((Mk * f[None, :] * np.log2(Mk / f[:, None])).sum())
day_pct = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
day_pam = [1, 5, 11, 17, 23, 30, 38, 47, 56, 67, 80, 94, 112, 133, 159, 195, 246, 328]

fig, ax = bio.canvas(24.0, 10.0)
a = C.axes_at(ax, (2.0, 1.5, 9.0, 7.6))
b = C.axes_at(ax, (14.4, 1.5, 9.0, 7.6))
a.plot(n, diff, color=C.line("protein"), lw=1.8, label="powers of the 1-PAM matrix")
a.plot(day_pam, day_pct, "o", color=C.line("negative"), ms=4, label="Dayhoff (1978) table")
a.axhline(100 * (1 - (f ** 2).sum()), color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.text(395, 100 * (1 - (f ** 2).sum()) - 4, "unrelated sequences", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
a.set_xlim(0, 400)
a.set_ylim(0, 100)
C.style_axes(a, "evolutionary distance (PAM)", "expected difference (%)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="center right")
b.plot(n, H, color=C.line("protein"), lw=1.8)
for name, h in [("BLOSUM80", 0.913), ("BLOSUM62", 0.579), ("BLOSUM45", 0.363)]:
    b.axhline(h, color=C.line("dna"), lw=0.8, ls=(0, (3, 2)))
    b.text(395, h + 0.05, name, fontsize=bio.core.FONT["tiny"], color=C.line("dna"), ha="right")
b.set_xlim(0, 400)
b.set_ylim(0, 4)
C.style_axes(b, "PAM n", "relative entropy (bits per pair)")
bio.panel(ax, "A", (0.2, 9.7))
bio.panel(ax, "B", (12.6, 9.7))
