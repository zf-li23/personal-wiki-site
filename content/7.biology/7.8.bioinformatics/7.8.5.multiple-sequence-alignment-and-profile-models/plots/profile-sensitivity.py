# Why profiles detect remote homologs: a simulation without insertions and deletions, so that the correct
# alignment is known and only the scoring differs. Sequences of 100 residues evolve under the PAM Markov
# chain (reconstructed from Dayhoff's PAM250 as in 7.8.3). For each distance D, 200 homologous pairs of
# families are generated: a root sequence, two family ancestors D/2 PAM from it, and 10 members per family
# 30 PAM from their ancestor; 2000 unrelated families serve as negatives. Three scores of the query family
# (or its first member) against each target family (or its first member): pairwise log-odds with the PAM
# matrix of the true distance; a sequence against the position-specific scoring matrix of the query family;
# and profile against profile, sum over columns of log2 sum_a p(a) p'(a) / f(a). Plotted: the fraction of
# homologs scoring above the 99th percentile of the negatives (sensitivity at 1 % false positives).
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
M250 = f[:, None] * 10 ** L
M250 = M250 / M250.sum(axis=0)
Dh, Dih = np.diag(np.sqrt(f)), np.diag(1 / np.sqrt(f))
w, V = np.linalg.eigh((lambda S_: (S_ + S_.T) / 2)(Dih @ M250 @ Dh))
w = np.clip(w, 1e-9, None)


def M(t):
    return np.clip(Dh @ V @ np.diag(w ** t) @ V.T @ Dih, 0, None)


t1 = brentq(lambda t: 1 - (f * np.diag(M(t))).sum() - 0.01, 1e-5, 0.1)


def pam(n):
    m = M(t1 * n)
    return m / m.sum(axis=0)


rng = np.random.default_rng(1)
Lseq, NF, NPOS, NNEG = 50, 10, 400, 2000


def evolve(anc, n):
    """Children of the sequences anc (integer array, any shape) after n PAM."""
    cum = np.cumsum(pam(n), axis=0)[:, anc]          # 20 x anc.shape
    u = rng.random(anc.shape)
    return np.minimum((u[None] > cum).sum(axis=0), 19)


def root(k):
    return rng.choice(20, size=(k, Lseq), p=f)


def family(anc, n):
    """NF members per root row, each n PAM from the root: shape (k, NF, Lseq)."""
    return evolve(np.repeat(anc[:, None, :], NF, axis=1), n)


def profile(fam, B=5.0):
    """Position-specific residue probabilities with pseudocounts from the substitution model."""
    cnt = np.zeros(fam.shape[:1] + (Lseq, 20))
    for a in range(20):
        cnt[..., a] = (fam == a).sum(axis=1)
    freqs = cnt / NF
    g = freqs @ pam(120).T                         # g[j, a] = sum_b f_j(b) M(a | b)
    return (cnt + B * g) / (NF + B)


Ds = np.arange(100, 1001, 75)
res = {"pairwise": [], "sequence-profile": [], "profile-profile": []}
for D in Ds:
    r = root(NPOS)
    qfam, tfam = family(r, D // 2), family(r, D // 2)
    nfam = family(root(NNEG), D // 2)
    qfam_n = np.repeat(qfam[:1], NNEG, axis=0)       # one query family against all negatives
    S2 = np.log2(pam(D) / f[:, None])    # pairwise log-odds at the true distance
    def pairwise(qf, tf):
        return S2[tf[:, 0], qf[:, 0]].sum(axis=1)
    def seqprof(qf, tf):
        pr = profile(qf)
        return np.log2(np.take_along_axis(pr, tf[:, 0, :, None], axis=2)[..., 0] / f[tf[:, 0]]).sum(axis=1)
    def profprof(qf, tf):
        return np.log2((profile(qf) * profile(tf) / f).sum(axis=2)).sum(axis=1)
    for name, fn in [("pairwise", pairwise), ("sequence-profile", seqprof), ("profile-profile", profprof)]:
        pos, neg = fn(qfam, tfam), fn(qfam_n, nfam)
        res[name].append((pos > np.quantile(neg, 0.99)).mean())
fig, ax = bio.canvas(16.0, 10.0)
a = C.axes_at(ax, (2.2, 1.5, 12.6, 7.8))
for (name, vals), tok in zip(res.items(), ["neutral", "dna", "protein"]):
    a.plot(Ds, vals, "o-", ms=3.5, lw=1.6, color=C.line(tok), label=name)
a.set_ylim(0, 1.03)
C.style_axes(a, "PAM distance between the compared sequences", "sensitivity at 1 % false positives")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
