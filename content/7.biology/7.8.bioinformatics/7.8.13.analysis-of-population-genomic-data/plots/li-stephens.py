# Haplotype imputation with the Li-Stephens model (simulated). A reference panel of 24 haplotypes over 300 SNPs
# is built as mosaics of 6 ancestral haplotypes (switch probability 0.01 per SNP, 1 % new mutations); the target
# haplotype copies panel haplotype 3 at SNPs 0-99, haplotype 17 at 100-209 and haplotype 8 at 210-299, with
# 0.5 % differences. Only every fifth SNP is typed (an array). The hidden state is the panel haplotype being
# copied; transitions switch to a uniformly chosen haplotype with probability rho = 0.04 between typed SNPs,
# and a copied allele is observed with error eps = 0.01. A: posterior copying probabilities from the forward-
# backward algorithm at the typed SNPs (darker = higher); red boxes mark the haplotypes actually copied. Panel
# haplotypes that descend from the same ancestral haplotype are identical at most typed SNPs, so the posterior
# is shared among them; in the first segment it falls on haplotype 23, which matches the target at all typed
# SNPs, while haplotype 3 differs at one of them through the target's own error. B: the
# imputed probability of allele 1 at the 240 untyped SNPs (posterior-weighted panel alleles, with the posterior
# interpolated linearly between typed SNPs), coloured by the true allele, and the accuracy against imputing
# the panel's majority allele.
import numpy as np
from matplotlib.patches import Rectangle
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
m, K, nf = 300, 24, 6
fp = rng.uniform(0.1, 0.9, m)
found = (rng.random((nf, m)) < fp).astype(int)
panel = np.empty((K, m), int)
for k in range(K):
    src = rng.integers(nf)
    for j in range(m):
        if rng.random() < 0.01:
            src = rng.integers(nf)
        panel[k, j] = found[src, j]
panel ^= (rng.random((K, m)) < 0.01)
truth_path = np.r_[np.full(100, 3), np.full(110, 17), np.full(90, 8)]
target = panel[truth_path, np.arange(m)] ^ (rng.random(m) < 0.005)
typed = np.arange(0, m, 5)
obs = target[typed]
H = panel[:, typed]
eps, rho = 0.01, 0.04
L = len(typed)
e = np.where(H == obs, 1 - eps, eps)                    # emission probabilities, K x L
fw = np.empty((K, L))
bw = np.ones((K, L))
fw[:, 0] = e[:, 0] / K
fw[:, 0] /= fw[:, 0].sum()
for t in range(1, L):                                   # O(K) per step: the jump is uniform
    fw[:, t] = e[:, t] * ((1 - rho) * fw[:, t - 1] + rho / K)
    fw[:, t] /= fw[:, t].sum()
for t in range(L - 2, -1, -1):
    x = e[:, t + 1] * bw[:, t + 1]
    bw[:, t] = (1 - rho) * x + rho * x.sum() / K
    bw[:, t] /= bw[:, t].sum()
post = fw * bw
post /= post.sum(0)
untyped = np.setdiff1d(np.arange(m), typed)
pj = np.array([np.interp(j, typed, post[k]) for k in range(K) for j in untyped]).reshape(K, -1)
pj /= pj.sum(0)
p1 = (pj * panel[:, untyped]).sum(0)
acc = np.mean((p1 > 0.5) == target[untyped])
acc0 = np.mean((panel[:, untyped].mean(0) > 0.5) == target[untyped])

fig, ax = bio.canvas(30.0, 10.4)
a = C.axes_at(ax, (2.0, 1.6, 14.5, 7.8))
a.imshow(post, aspect="auto", cmap="Blues", vmin=0, vmax=1, origin="lower",
         extent=(-2.5, m - 2.5, -0.5, K - 0.5), interpolation="nearest")
for (x0, x1, k) in [(0, 100, 3), (100, 210, 17), (210, 300, 8)]:
    a.add_patch(Rectangle((x0 - 2.5, k - 0.5), x1 - x0, 1, fill=False, ec=C.line("negative"), lw=1.3))
C.style_axes(a, "SNP position", "panel haplotype", box=True)
a.set_yticks([0, 5, 10, 15, 20])
b = C.axes_at(ax, (19.6, 1.6, 9.8, 7.8))
for v, tok, name in [(0, "dna", "true allele 0"), (1, "rna", "true allele 1")]:
    s = target[untyped] == v
    b.scatter(untyped[s], p1[s], s=9, color=C.line(tok), lw=0, label=name)
b.axhline(0.5, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
b.set_ylim(-0.05, 1.05)
b.text(5, 0.6, f"accuracy {100 * acc:.1f} %\npanel majority allele {100 * acc0:.1f} %",
       fontsize=bio.core.FONT["tiny"], color=P.ink())
C.style_axes(b, "untyped SNP position", "imputed P(allele 1)")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right",
         bbox_to_anchor=(1.0, 1.12), ncol=2, markerscale=1.5)
bio.panel(ax, "A", (0.2, 10.0))
bio.panel(ax, "B", (17.8, 10.0))
