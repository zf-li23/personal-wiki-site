"""Changes of translation measured by ribosome profiling (simulated data and a model). A: log2 fold changes
of mRNA (RNA-seq) and of ribosome footprints (RPF) for 3000 genes, three replicates per condition and
assay, analysed by a linear model on log counts per million with the interaction of condition and assay,
whose coefficient is the change of log2 translation efficiency. Classes as in deltaTE: forwarded
(mRNA and RPF change together, TE unchanged), exclusive (TE changes without an mRNA change), buffered
(TE change opposes an mRNA change), intensified (both change in the same direction); grey: no
significant change (BH-adjusted p < 0.05). B, C: model profiles of ribosome density along a 300-codon
coding sequence with a 50-codon 5' leader, normalized to the control: B, a block of scanning in the
leader lowers footprints on the coding sequence uniformly and accumulates them upstream (an
initiation-responsive pattern); C, a block of early elongation piles ribosomes over the first 100 codons
(an elongation-responsive pattern). The polarity score of the coding sequence, from -1 (all density at
the 5' end) to +1 (all at the 3' end), changes only in C."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
G, R = 3000, 3
cls = rng.choice(5, G, p=[0.82, 0.07, 0.05, 0.03, 0.03])  # none, forwarded, exclusive, buffered, intensified
dm = np.zeros(G); dt = np.zeros(G)
s = rng.choice([-1, 1], G) * rng.uniform(1.0, 2.5, G)
dm[cls == 1] = s[cls == 1]
dt[cls == 2] = s[cls == 2]
dm[cls == 3] = s[cls == 3]; dt[cls == 3] = -s[cls == 3]
dm[cls == 4] = s[cls == 4] * 0.7; dt[cls == 4] = s[cls == 4] * 0.7
base = rng.normal(5, 1.5, G)
te = rng.normal(0, 0.7, G)
# log2 expression: assay a (0 mRNA, 1 RPF), condition c (0, 1)
y = {}
for a in (0, 1):
    for c in (0, 1):
        mu = base + a * te + c * dm + a * c * dt
        lam = 2 ** mu * 20
        x = rng.negative_binomial(40, 40 / (40 + lam[:, None] * np.ones((1, R))))
        y[a, c] = np.log2(x + 0.5)
Y = np.hstack([y[0, 0], y[0, 1], y[1, 0], y[1, 1]])
A = np.repeat([0, 0, 1, 1], R); C = np.repeat([0, 1, 0, 1], R)
X = np.c_[np.ones(4 * R), A, C, A * C]
beta, *_ = np.linalg.lstsq(X, Y.T, rcond=None)
res = Y.T - X @ beta
df = 4 * R - 4
s2 = (res ** 2).sum(0) / df
cov = np.linalg.inv(X.T @ X)


def padj(p):
    o = np.argsort(p); q = p[o] * len(p) / np.arange(1, len(p) + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]; out = np.empty_like(q); out[o] = np.minimum(q, 1); return out


t_int = beta[3] / np.sqrt(s2 * cov[3, 3])
q_int = padj(2 * stats.t.sf(np.abs(t_int), df))
t_m = beta[2] / np.sqrt(s2 * cov[2, 2])
q_m = padj(2 * stats.t.sf(np.abs(t_m), df))
lfc_m, lfc_r = beta[2], beta[2] + beta[3]
v = np.array([0, 1, 0, 0]); v2 = np.array([0, 0, 1, 1])
t_r = lfc_r / np.sqrt(s2 * (v2 @ cov @ v2))
q_r = padj(2 * stats.t.sf(np.abs(t_r), df))
lab = np.zeros(G, int)
sig_i, sig_m, sig_r = q_int < 0.05, q_m < 0.05, q_r < 0.05
lab[sig_m & sig_r & ~sig_i] = 1
lab[sig_i & ~sig_m] = 2
lab[sig_i & sig_m & (np.sign(beta[3]) != np.sign(beta[2]))] = 3
lab[sig_i & sig_m & (np.sign(beta[3]) == np.sign(beta[2]))] = 4
names = ["no change", "forwarded", "exclusive", "buffered", "intensified"]
toks = ["neutral", "dna", "rna", "protein", "positive"]
fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.8))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.16, top=0.88, wspace=0.3)
ax = axs[0]
for k in range(5):
    m = lab == k
    ax.scatter(lfc_m[m], lfc_r[m], s=3 if k == 0 else 6, lw=0, color=P.fill(toks[k]) if k == 0 else charts.line(toks[k]),
               label=f"{names[k]} ({m.sum()})", rasterized=True)
ax.plot([-4, 4], [-4, 4], color=P.muted(), lw=0.6, ls="--")
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
ax.legend(frameon=False, fontsize=7, loc="upper left", markerscale=2)
charts.style_axes(ax, "log2 fold change, mRNA", "log2 fold change, RPF")
charts.title(ax, "A  Differential translation")
truth = np.array([0, 1, 2, 3, 4])[cls]
print("counts", [int((lab == k).sum()) for k in range(5)], "agreement", np.mean(lab == truth))

# B, C: polarity model
L5, Lc = 50, 300
xs = np.arange(-L5, Lc)
ctrl = np.where(xs < 0, 0.08, 1.0)
ctrl[(xs >= 0) & (xs < 3)] += 2.0


def polarity(d):
    d = d[L5:]; L = len(d); i = np.arange(1, L + 1); w = (2 * i - (L + 1)) / (L - 1)
    return float((d / d.sum() * w).sum())


irg = ctrl.copy(); irg[xs >= 0] *= 0.35; irg[xs < 0] = 0.08 + 0.9 * np.exp(-((xs[xs < 0] + 20) / 12) ** 2)
erg = ctrl.copy(); erg[xs >= 0] *= 1 + 3.5 * np.exp(-xs[xs >= 0] / 45)
for ax, prof, ttl, tok in [(axs[1], irg, "B  Initiation-responsive pattern", "dna"),
                           (axs[2], erg, "C  Elongation-responsive pattern", "rna")]:
    ax.plot(xs, ctrl, color=P.muted(), lw=1.2, label=f"control (polarity {polarity(ctrl):+.2f})")
    ax.plot(xs, prof, color=charts.line(tok), lw=1.5, label=f"drug (polarity {polarity(prof):+.2f})")
    ax.axvline(0, color=P.muted(), lw=0.6, ls="--")
    ax.text(-L5 + 2, 4.0, "5' leader", fontsize=7, color=P.muted())
    ax.legend(frameon=False, fontsize=7.5, loc="upper right")
    ax.set_ylim(0, 4.8 if tok == "dna" else 14.5)
    charts.style_axes(ax, "codon (0 = start codon)", "ribosome density (model)")
    charts.title(ax, ttl)
    print(ttl, polarity(ctrl), polarity(prof), prof[L5:].sum() / ctrl[L5:].sum())
