"""Estimating a marginal likelihood: the JC69 model for the human and orangutan 12S rRNA genes with an
exponential prior (mean 0.2), whose exact log marginal likelihood is obtained by quadrature. A: the power
posteriors p(d) L(d)^b, normalized, for several b between 0 (the prior) and 1 (the posterior). B: estimates
of the log marginal likelihood from 40 independent runs of each method, all using exact draws from the
target distributions: the harmonic mean of the likelihood over 1000 or 10 000 posterior draws, and stepping-
stone sampling with 16 values of b (b_k = (k/16)^(1/0.3)) and 200 draws from each power posterior. The
harmonic mean is biased upward and its error does not shrink with more samples; stepping-stone estimates
are close to the exact value (line)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
x, n, mu = 90, 948, 0.2
d = np.concatenate([np.linspace(1e-6, 0.4, 20000), np.linspace(0.4, 6, 4000)[1:]])
lprior = -np.log(mu) - d / mu
e = np.exp(-4 * d / 3)
ll = x * np.log(0.75 - 0.75 * e) + (n - x) * np.log(0.25 + 0.75 * e)
m = (lprior + ll).max()
exact = m + np.log(np.trapezoid(np.exp(lprior + ll - m), d))
rng = np.random.default_rng(9)


def sampler(b):
    lw = lprior + b * ll
    w = np.exp(lw - lw.max()) * np.gradient(d)
    cdf = np.cumsum(w)
    cdf /= cdf[-1]
    return lambda size: np.interp(rng.random(size), cdf, d)


def llik(v):
    ev = np.exp(-4 * v / 3)
    return x * np.log(0.75 - 0.75 * ev) + (n - x) * np.log(0.25 + 0.75 * ev)


def hme(N):
    s = llik(sampler(1.0)(N))
    return -(np.logaddexp.reduce(-s) - np.log(N))


bs = (np.arange(17) / 16) ** (1 / 0.3)


def stepping(N):
    tot = 0.0
    for k in range(16):
        s = llik(sampler(bs[k])(N))
        z = (bs[k + 1] - bs[k]) * s
        tot += np.logaddexp.reduce(z) - np.log(N)
    return tot


fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.9, wspace=0.3)
toks = ("neutral", "plant", "enzyme", "rna", "dna")
for bb, tok in zip((0.0, 0.002, 0.02, 0.2, 1.0), toks):
    lw = lprior + bb * ll
    w = np.exp(lw - lw.max())
    w /= np.trapezoid(w, d)
    a.plot(d, w, color=charts.line(tok), lw=1.4, label=f"$b = {bb:g}$")
a.set_xlim(0, 0.6)
a.set_yscale("log")
a.set_ylim(1e-2, 60)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "distance $d$", "power posterior density")
charts.title(a, "A  From prior to posterior")

runs = 40
res = {"harmonic mean, N = 1000": [hme(1000) for _ in range(runs)],
       "harmonic mean, N = 10 000": [hme(10000) for _ in range(runs)],
       "stepping-stone, 16 x 200": [stepping(200) for _ in range(runs)]}
for k, (lab, v) in enumerate(res.items()):
    tok = ("rna", "negative", "dna")[k]
    b.plot(np.full(runs, k) + rng.uniform(-0.15, 0.15, runs), v, "o", ms=3.2, color=charts.line(tok), alpha=0.8)
b.axhline(exact, color=P.ink(), lw=0.9)
b.text(1.0, exact + 0.05, f"exact {exact:.3f}", fontsize=FT["tiny"], color=P.ink(), ha="center", va="bottom")
b.set_xticks(range(3), list(res), fontsize=FT["tiny"])
b.set_xlim(-0.5, 2.5)
charts.style_axes(b, None, "log marginal likelihood")
charts.title(b, "B  Harmonic mean versus stepping-stone")
