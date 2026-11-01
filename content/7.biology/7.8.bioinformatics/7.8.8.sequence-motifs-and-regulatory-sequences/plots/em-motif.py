# De novo motif discovery by expectation maximization (the OOPS model of MEME). Simulated data: 25 random
# sequences of 150 bp (base frequencies 0.295/0.205/0.205/0.295, as in the human genome), each with one
# site of length 19 sampled from the JASPAR CTCF matrix MA0139.1 at a random position and strand-fixed
# orientation. EM is started from every 19-mer of the first sequence (the starting matrix puts probability 0.3
# on the base of the 19-mer and 0.7/3 on each other base), one iteration is run from each start, the five
# best starts are iterated to convergence and the run with the highest likelihood is kept. A: the log-likelihood ratio of the data under the motif model
# against the background over the iterations. B: the posterior probability of the site position in
# sequence 1 at iterations 0 (start), 1, 3 and at convergence; the dashed line marks the planted site.
# C: the logo of the planted sites; D: the logo of the estimated matrix (expected counts).
import numpy as np
import wikibio as bio
from wikibio import charts as C, sequence as S

P = bio.P
rng = np.random.default_rng(3)
CTCF = np.array([[87, 291, 76, 459], [167, 145, 414, 187], [281, 49, 449, 134], [56, 800, 21, 36],
                 [8, 903, 0, 2], [744, 13, 65, 91], [40, 528, 334, 11], [107, 433, 48, 324],
                 [851, 11, 32, 18], [5, 0, 903, 3], [333, 3, 566, 9], [54, 12, 504, 341], [12, 0, 890, 8],
                 [56, 8, 775, 71], [104, 733, 5, 67], [372, 13, 507, 17], [82, 482, 307, 37],
                 [117, 322, 73, 396], [402, 181, 266, 59]], float)
bg = np.array([0.295, 0.205, 0.205, 0.295])
W, N, Lseq = 19, 25, 150
pm = CTCF / CTCF.sum(1, keepdims=True)
seqs = rng.choice(4, size=(N, Lseq), p=bg)
true_pos = rng.integers(0, Lseq - W + 1, N)
for i in range(N):
    seqs[i, true_pos[i]:true_pos[i] + W] = [rng.choice(4, p=pm[j]) for j in range(W)]
M = Lseq - W + 1
win = np.stack([seqs[:, k:k + W] for k in range(M)], 1)          # N x M x W
logbg = np.log(bg)[win].sum(2)


def estep(theta):
    ll = np.log(theta)[np.arange(W), win].sum(2) - logbg       # log LR of each window
    mx = ll.max(1, keepdims=True)
    z = np.exp(ll - mx)
    post = z / z.sum(1, keepdims=True)
    loglik = (mx[:, 0] + np.log(z.sum(1) / M)).sum()            # sum_i log mean_k LR, uniform position prior
    return post, loglik


def mstep(post, beta=0.1):
    cnt = np.zeros((W, 4))
    for b in range(4):
        cnt[:, b] = (post[:, :, None] * (win == b)).sum((0, 1))
    return (cnt + beta * bg) / (cnt.sum(1, keepdims=True) + beta), cnt


def start(k, w=0.3):
    onehot = np.eye(4)[seqs[0, k:k + W]]
    return w * onehot + (1 - w) / 3 * (1 - onehot)


def run(theta, maxit=60):
    lls, posts = [], []
    for it in range(maxit):
        post, ll = estep(theta)
        lls.append(ll)
        posts.append(post[0].copy())
        theta, cnt = mstep(post)
        if it > 2 and abs(lls[-1] - lls[-2]) < 1e-4:
            break
    return theta, cnt, lls, posts


one = []
for k in range(M):
    th1, _ = mstep(estep(start(k))[0])
    one.append(estep(th1)[1])
cands = np.argsort(one)[::-1][:5]
runs = [run(start(k)) for k in cands]
theta, cnt, lls, posts = max(runs, key=lambda r: r[2][-1])
post, ll = estep(theta)
found = post.argmax(1)
n_ok = int((found == true_pos).sum())

fig, ax = bio.canvas(28.0, 11.5)
a = C.axes_at(ax, (1.8, 6.6, 6.6, 4.0))
b = C.axes_at(ax, (11.0, 6.6, 15.8, 4.0))
a.plot(np.arange(len(lls)), np.array(lls) / np.log(2), "o-", ms=3, color=C.line("dna"), lw=1.2)
C.style_axes(a, "iteration", "log2 likelihood ratio (bits)")
for it, tok in [(0, "neutral"), (1, "rna"), (3, "protein"), (len(posts) - 1, "dna")]:
    b.plot(np.arange(1, M + 1), posts[it], color=C.line(tok), lw=1.1,
           label=f"iteration {it}" if it < len(posts) - 1 else f"converged ({it})")
b.axvline(true_pos[0] + 1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
b.set_xlim(1, M)
b.set_ylim(0, 1.05)
C.style_axes(b, "start position in sequence 1", "posterior")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
planted = np.zeros((W, 4))
for i in range(N):
    for j in range(W):
        planted[j, seqs[i, true_pos[i] + j]] += 1
S.logo(ax, planted, at=(2.4, 0.9), col_width=0.55, height=3.2, title="Planted sites (25)")
S.logo(ax, cnt, at=(15.6, 0.9), col_width=0.55, height=3.2, title=f"EM estimate ({n_ok}/25 sites recovered)")
for lab, xy in zip("ABCD", [(0.2, 11.2), (9.6, 11.2), (0.2, 5.0), (13.4, 5.0)]):
    bio.panel(ax, lab, xy)
