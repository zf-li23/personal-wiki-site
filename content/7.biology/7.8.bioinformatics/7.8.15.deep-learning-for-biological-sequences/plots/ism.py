# In silico saturation mutagenesis and gradient-times-input attribution for the network of the previous
# figure (the same simulated data and training, recomputed here). For one test sequence that carries a
# planted CTCF site, every position is mutated to each of the three other bases and the change in the
# output logit is recorded (A, heat map: blue = loss of score, red = gain). B: the attribution per
# position: the mean loss of logit caused by mutating it (ISM) and the gradient of the logit with respect
# to the one-hot input times the input; the shaded band is the planted site, dots mark its bases in A.
# Because of global max pooling, only positions inside the maximally activated window of some filter can
# have nonzero attribution.
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


def logit(X):
    return forward(windows(onehot(X)), F, bF, v, c)[3]


cand = np.where((yte == 1) & (ste == 0))[0]
zc = logit(Xte[cand])
i0 = cand[np.argsort(zc)[len(zc) // 2]]          # a positive of median score, site on the + strand
x = Xte[i0]
z0 = logit(x[None])[0]
muts = np.repeat(x[None], Lseq * 4, 0)
for p in range(Lseq):
    for b in range(4):
        muts[p * 4 + b, p] = b
dz = (logit(muts) - z0).reshape(Lseq, 4)
# gradient times input
A, am, h, _ = forward(windows(onehot(x[None])), F, bF, v, c)
grad = np.zeros((Lseq, 4))
for k in range(K):
    if h[0, k] > 0:
        grad[am[0, k]:am[0, k] + w] += v[k] * F[:, k].reshape(w, 4)
gxi = grad[np.arange(Lseq), x]
ism = dz.sum(1) / 3

fig, ax = bio.canvas(30.0, 11.0)
a = C.axes_at(ax, (2.2, 5.6, 26.5, 3.8))
vm = np.abs(dz).max()
im = a.imshow(dz.T, aspect="auto", cmap="RdBu_r", vmin=-vm, vmax=vm, extent=(0.5, Lseq + 0.5, 3.5, -0.5),
              interpolation="nearest")
a.set_yticks(range(4))
a.set_yticklabels(list("ACGT"))
s0 = pte[i0]
for p in range(s0, s0 + W):
    a.text(p + 1, x[p], "•", ha="center", va="center", fontsize=FT["tiny"], color="#1f2430")
C.style_axes(a, None, "mutant base", box=True)
cb = C.axes_at(ax, (29.0, 5.6, 0.3, 3.8))
fig.colorbar(im, cax=cb)
C.style_axes(cb, None, None, box=True)
cb.set_ylabel("change in logit", fontsize=FT["small"], color=P.ink())
b = C.axes_at(ax, (2.2, 1.0, 26.5, 3.6))
b.axvspan(s0 + 0.5, s0 + W + 0.5, color=P.mix(P.light("highlight"), P.surface(), 0.55), lw=0)
b.bar(np.arange(1, Lseq + 1), -ism, width=0.8, color=C.line("negative"), label="ISM: mean loss of logit on mutation")
b.plot(np.arange(1, Lseq + 1), gxi, color=C.line("dna"), lw=1.1, label="gradient \u00d7 input")
b.axhline(0, color=P.muted(), lw=0.6)
b.set_xlim(0.5, Lseq + 0.5)
C.style_axes(b, "position in sequence (bp)", "attribution")
b.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 10.4))
bio.panel(ax, "B", (0.3, 4.9))
