# PCA of simulated genotypes. Three populations of 100 individuals diverge from a common ancestral population
# (Balding-Nichols model: at each of 5000 SNPs with ancestral frequency p ~ U(0.05, 0.95), population k has
# frequency ~ Beta(p(1 - F_k)/F_k, (1 - p)(1 - F_k)/F_k) with F = 0.05, 0.08, 0.12); 40 further individuals are
# admixed between populations 1 and 2 with a uniform ancestry proportion. Genotypes are standardized by the
# sample allele frequencies, Z_ij = (g_ij - 2 p_j) / sqrt(2 p_j (1 - p_j)), and the eigenvectors of Z Z^T / m are
# the principal components. A: PC1 against PC2; admixed individuals lie on the line between their source
# populations, at a position given by their ancestry. B: the leading eigenvalues against the upper edge
# (1 + sqrt(n/m))^2 of the Marchenko-Pastur law for unstructured data: two eigenvalues (K - 1 for K = 3
# populations) stand far above it, the rest lie at or below it.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
m, npop = 5000, 100
p0 = rng.uniform(0.05, 0.95, m)
F = [0.05, 0.08, 0.12]
freqs = [rng.beta(p0 * (1 - f) / f, (1 - p0) * (1 - f) / f) for f in F]
G, lab = [], []
for k in range(3):
    G.append(rng.binomial(2, freqs[k], (npop, m)))
    lab += [k] * npop
q = rng.uniform(0, 1, 40)
pmix = q[:, None] * freqs[0] + (1 - q[:, None]) * freqs[1]
G.append(rng.binomial(2, pmix))
lab += [3] * 40
G = np.vstack(G).astype(float)
lab = np.array(lab)
n = G.shape[0]
ph = G.mean(0) / 2
keep = (ph > 0.01) & (ph < 0.99)
Z = (G[:, keep] - 2 * ph[keep]) / np.sqrt(2 * ph[keep] * (1 - ph[keep]))
mk = Z.shape[1]
U, s, Vt = np.linalg.svd(Z, full_matrices=False)
ev = s ** 2 / mk
pcs = U[:, :2] * s[:2]

fig, ax = bio.canvas(28.0, 10.6)
a = C.axes_at(ax, (2.2, 1.6, 11.0, 8.0))
toks = ["dna", "rna", "enzyme", "protein"]
names = ["population 1 (F = 0.05)", "population 2 (F = 0.08)", "population 3 (F = 0.12)", "admixed 1 x 2"]
for k in range(4):
    sel = lab == k
    if k < 3:
        a.scatter(pcs[sel, 0], pcs[sel, 1], s=9, color=C.line(toks[k]), lw=0, alpha=0.8, label=names[k])
    else:
        a.scatter(pcs[sel, 0], pcs[sel, 1], s=16, c=q, cmap="viridis", vmin=0, vmax=1, lw=0.3,
                  edgecolors=P.ink(), label=names[k])
C.style_axes(a, f"PC1 ({100 * ev[0] / ev.sum():.1f} % of variance)", f"PC2 ({100 * ev[1] / ev.sum():.1f} %)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="best", markerscale=1.4)

b = C.axes_at(ax, (16.8, 1.6, 10.4, 8.0))
edge = (1 + np.sqrt(n / mk)) ** 2
idx = np.arange(1, 21)
b.plot(idx, ev[:20], "o-", color=C.line("dna"), ms=4, lw=1.0)
b.axhline(edge, color=C.line("negative"), lw=1.0, ls=(0, (3, 2)))
b.text(10.5, edge * 1.25, f"Marchenko-Pastur edge {edge:.2f}", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_yscale("log")
b.set_xticks([1, 5, 10, 15, 20])
for i in range(2):
    b.text(idx[i] + 0.5, ev[i], f"{ev[i]:.1f}", fontsize=bio.core.FONT["tiny"], color=P.ink(), va="center")
C.style_axes(b, "eigenvalue rank", "eigenvalue of Z Z^T / m")
bio.panel(ax, "A", (0.3, 10.2))
bio.panel(ax, "B", (15.0, 10.2))
