# A small convolutional network learns a binding motif from labeled sequences (simulated data).
# 7000 random sequences of 120 bp (human base frequencies); half of them carry one site drawn from the
# JASPAR CTCF matrix MA0139.1 on a random strand at a random position. The network (implemented here in
# numpy): one convolutional layer of 8 filters of width 24 on the one-hot sequence, ReLU, global max
# pooling over positions, a linear output and the logistic loss with weight decay, trained with Adam on
# 4000 sequences for 15 epochs; 1000 sequences for validation, 2000 for testing.
# A: training and validation loss and AUROC by epoch. B: logo of the planted matrix. C, D: the two filters
# with the largest output weights, converted to frequency matrices from the validation windows that
# activate them above half their maximum, aligned to the CTCF matrix (D is the reverse complement).
import numpy as np
import wikibio as bio
from wikibio import charts as C, sequence as S

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(7)
# JASPAR CTCF matrix MA0139.1 (counts of A, C, G, T at 19 positions), as in 7.8.8
CTCF = np.array([[87, 291, 76, 459], [167, 145, 414, 187], [281, 49, 449, 134], [56, 800, 21, 36],
                 [8, 903, 0, 2], [744, 13, 65, 91], [40, 528, 334, 11], [107, 433, 48, 324],
                 [851, 11, 32, 18], [5, 0, 903, 3], [333, 3, 566, 9], [54, 12, 504, 341], [12, 0, 890, 8],
                 [56, 8, 775, 71], [104, 733, 5, 67], [372, 13, 507, 17], [82, 482, 307, 37],
                 [117, 322, 73, 396], [402, 181, 266, 59]], float)
bg = np.array([0.295, 0.205, 0.205, 0.295])
pm = CTCF / CTCF.sum(1, keepdims=True)
W, Lseq, K, w = 19, 120, 8, 24


def make(n):
    X = rng.choice(4, size=(n, Lseq), p=bg)
    y = rng.random(n) < 0.5
    pos = np.full(n, -1)
    strand = np.zeros(n, int)
    for i in np.where(y)[0]:
        site = np.array([rng.choice(4, p=pm[j]) for j in range(W)])
        if rng.random() < 0.5:
            site = 3 - site[::-1]
            strand[i] = 1
        k = rng.integers(0, Lseq - W + 1)
        X[i, k:k + W] = site
        pos[i] = k
    return X, y.astype(float), pos, strand


def onehot(X):
    return np.eye(4)[X]


def windows(O):
    n, L, _ = O.shape
    idx = np.arange(L - w + 1)[:, None] + np.arange(w)[None]
    return O[:, idx, :].reshape(n, L - w + 1, w * 4)


def forward(Wn, F, bF, v, c):
    A = Wn @ F + bF
    R = np.maximum(A, 0)
    am = R.argmax(1)
    h = R.max(1)
    return A, am, h, h @ v + c


def auc(y, s):
    o = np.argsort(s)
    r = np.empty(len(s))
    r[o] = np.arange(1, len(s) + 1)
    n1 = y.sum()
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def train(epochs=15, lr=0.01, lam=1e-3, batch=100):
    # conv (K filters of width w) -> ReLU -> global max pool -> linear -> logistic; Adam
    F = rng.normal(0, 0.1, (w * 4, K))
    bF = np.zeros(K)
    v = rng.normal(0, 0.1, K)
    c = np.zeros(1)
    ps = [F, bF, v, c]
    m1 = [np.zeros_like(p) for p in ps]
    m2 = [np.zeros_like(p) for p in ps]
    step, hist = 0, []
    for ep in range(epochs):
        perm = rng.permutation(len(ytr))
        for b in range(0, len(perm), batch):
            ii = perm[b:b + batch]
            Wb, yb = Wtr[ii], ytr[ii]
            A, am, h, z = forward(Wb, F, bF, v, c)
            g = (1 / (1 + np.exp(-z)) - yb) / len(ii)
            gh = np.outer(g, v) * (h > 0)
            sel = Wb[np.arange(len(ii))[:, None], am]
            grads = [np.einsum("nk,nkd->dk", gh, sel) + lam * F, gh.sum(0), h.T @ g + lam * v, np.array([g.sum()])]
            step += 1
            for k_, (p, gr) in enumerate(zip(ps, grads)):
                m1[k_] = 0.9 * m1[k_] + 0.1 * gr
                m2[k_] = 0.999 * m2[k_] + 0.001 * gr ** 2
                p -= lr * (m1[k_] / (1 - 0.9 ** step)) / (np.sqrt(m2[k_] / (1 - 0.999 ** step)) + 1e-8)
        row = [ep + 1]
        for Wn, yy in ((Wtr, ytr), (Wva, yva)):
            z = forward(Wn, F, bF, v, c)[3]
            p_ = 1 / (1 + np.exp(-z))
            row += [-np.mean(yy * np.log(p_ + 1e-12) + (1 - yy) * np.log(1 - p_ + 1e-12)), auc(yy, z)]
        hist.append(row)
    return F, bF, v, c, np.array(hist)


Xtr, ytr, _, _ = make(4000)
Xva, yva, _, _ = make(1000)
Xte, yte, pte, ste = make(2000)
Wtr, Wva, Wte = windows(onehot(Xtr)), windows(onehot(Xva)), windows(onehot(Xte))
F, bF, v, c, hist = train()

# filters -> frequency matrices from strongly activating validation windows, aligned to the planted motif
Ava = Wva @ F + bF
pmr = pm[::-1, ::-1]
aligned = []
for k in np.argsort(v)[::-1][:2]:
    a = Ava[:, :, k]
    hits = np.argwhere(a > 0.5 * a.max())
    pfm = np.zeros((w, 4))
    for n_, m_ in hits:
        pfm += onehot(Xva[n_, m_:m_ + w])
    pad = np.vstack([np.tile(bg * len(hits), (W, 1)), pfm, np.tile(bg * len(hits), (W, 1))])
    best = (-2, 0, 0)
    for sgn in (0, 1):
        M = pad if sgn == 0 else pad[::-1, ::-1]
        for off in range(1, w + W):
            r = np.corrcoef((M[off:off + W] / M[off:off + W].sum(1, keepdims=True)).ravel(), pm.ravel())[0, 1]
            if r > best[0]:
                best = (r, sgn, off)
    r, sgn, off = best
    M = pad if sgn == 0 else pad[::-1, ::-1]
    aligned.append((k, M[off:off + W], r, sgn, len(hits)))

fig, ax = bio.canvas(30.0, 12.0)
a = C.axes_at(ax, (1.9, 6.9, 7.6, 4.2))
a.plot(hist[:, 0], hist[:, 1], "o-", ms=3, color=C.line("dna"), lw=1.2, label="training loss")
a.plot(hist[:, 0], hist[:, 3], "s-", ms=3, color=C.line("rna"), lw=1.2, label="validation loss")
C.style_axes(a, "epoch", "logistic loss")
a.set_ylim(0, 0.45)
a2 = a.twinx()
a2.plot(hist[:, 0], hist[:, 4], "--", color=C.line("positive"), lw=1.2)
a2.set_ylim(0.95, 1.0)
C.style_axes(a2, None, "validation AUROC", box=False)
a2.spines["right"].set_visible(True)
a2.spines["right"].set_color(P.muted())
a.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
a.text(9.5, 0.29, "AUROC", color=C.line("positive"), fontsize=FT["tiny"])
bio.panel(ax, "A", (0.2, 11.6))
S.logo(ax, CTCF, at=(13.5, 7.0), col_width=0.8, height=3.2, title="B   Planted motif (CTCF, MA0139.1)")
for j, (k, M, r, sgn, nh) in enumerate(sorted(aligned, key=lambda t: -t[2])):
    x0 = 1.9 + j * 15.0
    S.logo(ax, M, at=(x0, 1.2), col_width=0.62, height=3.2,
           title=f"{'CD'[j]}   Filter {k + 1}{' (reverse complement)' if sgn else ''}: r = {r:.2f}, {nh} windows")
