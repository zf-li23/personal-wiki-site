"""Target-decoy estimation of the false discovery rate (simulation). 20000 spectra are searched
against a concatenated database of target and reversed (decoy) sequences; 60% of the spectra come
from peptides in the database. The best random match to a spectrum has a Gumbel-distributed score
(location 15, scale 3), equally likely to be a target or a decoy sequence; a correct match scores
Normal(32, 7). Each spectrum keeps its best match. A: scores of the accepted target matches,
split into correct and incorrect (known only in the simulation), and of the decoy matches, whose
distribution mirrors the incorrect targets. B: estimated FDR (decoys / targets above the threshold)
against the true false discovery proportion. C: number of target matches accepted as a function of
the q-value threshold; dashed: 1%."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N, pi = 20000, 0.6
ident = rng.random(N) < pi
rand_t = rng.gumbel(15, 3, N)                 # best random target match
rand_d = rng.gumbel(15, 3, N)                 # best decoy match
correct = np.where(ident, rng.normal(32, 7, N), -np.inf)
best_t = np.maximum(correct, rand_t)
is_correct = ident & (correct >= rand_t)
score = np.maximum(best_t, rand_d)
decoy = rand_d > best_t
true_ok = ~decoy & is_correct

order = np.argsort(-score)
s, d, ok = score[order], decoy[order], true_ok[order]
T = np.cumsum(~d)
D = np.cumsum(d)
fdr = D / np.maximum(T, 1)
fdp = np.cumsum(~d & ~ok) / np.maximum(T, 1)
q = np.minimum.accumulate(fdr[::-1])[::-1]

cc, ci, cd = charts.line("positive"), charts.line("rna"), charts.line("dna")
fig, (a, b, c) = plt.subplots(1, 3, figsize=(10.5, 3.4))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.16, top=0.88, wspace=0.32)
bins = np.linspace(0, 60, 61)
a.hist(score[~decoy & true_ok], bins, color=P.fill("positive"), alpha=0.75, label="target, correct")
a.hist(score[~decoy & ~true_ok], bins, color=P.fill("rna"), alpha=0.75, label="target, incorrect")
a.hist(score[decoy], bins, histtype="step", color=cd, lw=1.4, label="decoy")
a.legend(frameon=False, fontsize=7)
charts.style_axes(a, "score of the best match", "spectra")
charts.title(a, "A  Score distributions")

m = T > 200
b.plot(s[m], fdr[m], color=cd, lw=1.5, label="estimated: decoys / targets")
b.plot(s[m], fdp[m], color=ci, lw=1.2, ls="--", label="true false discovery proportion")
b.set_xlim(15, 45)
b.set_ylim(0, 0.5)
b.legend(frameon=False, fontsize=7)
charts.style_axes(b, "score threshold", "FDR")
charts.title(b, "B  The decoys estimate the FDR")

c.plot(q[~d], T[~d], color=cc, lw=1.5)
c.axvline(0.01, color=P.muted(), ls="--", lw=0.8)
c.set_xscale("log")
c.set_xlim(1e-4, 0.5)
charts.style_axes(c, "q-value threshold", "target matches accepted")
charts.title(c, "C  Identifications against q")
