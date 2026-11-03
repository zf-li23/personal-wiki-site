"""Sampling properties of the JC69 distance. A: log-likelihood of the distance d for the human and
orangutan mitochondrial 12S rRNA genes (x = 90 differences at n = 948 sites; data from Yang (2014),
Table 1.3), with the 95% likelihood interval (drop of 1.92) and the normal-approximation interval
from the delta-method standard error. B: standard deviation of the estimate among 20 000 simulated
pairs of sequences (dots, finite estimates only) and the delta-method standard error (lines) against
the true distance, for n = 500 and 2000 sites. C: the probability that the estimate does not exist
(observed proportion of differences at least 3/4), computed exactly from the binomial distribution."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def p_of(d):
    return 0.75 - 0.75 * np.exp(-4 * d / 3)


def d_of(p):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(p < 0.75, -0.75 * np.log(1 - 4 * p / 3), np.inf)


def se(d, n):
    p = p_of(d)
    return np.sqrt(p * (1 - p) / n) / (1 - 4 * p / 3)


fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 3.8))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.16, top=0.9, wspace=0.32)
n, x = 948, 90
dd = np.linspace(0.05, 0.17, 400)
pp = p_of(dd)
ll = x * np.log(pp / 12) + (n - x) * np.log((1 - pp) / 4)
dh = float(d_of(np.array(x / n)))
lmax = x * np.log(x / n / 12) + (n - x) * np.log((1 - x / n) / 4)
a.plot(dd, ll, color=charts.line("dna"), lw=1.6)
a.axhline(lmax - 1.921, color=P.muted(), lw=0.7, ls=":")
def lik(d):
    p = p_of(d)
    return x * np.log(p / 12) + (n - x) * np.log((1 - p) / 4) - lmax + 1.921


inside = [brentq(lik, 0.05, dh), brentq(lik, dh, 0.2)]
a.plot([inside[0], inside[-1]], [lmax - 1.921] * 2, color=charts.line("rna"), lw=3, solid_capstyle="butt",
       label=f"likelihood interval ({inside[0]:.4f}, {inside[-1]:.4f})")
s = float(se(dh, n))
a.plot([dh - 1.96 * s, dh + 1.96 * s], [lmax - 3.2] * 2, color=charts.line("enzyme"), lw=3,
       solid_capstyle="butt", label=f"normal interval ({dh - 1.96 * s:.4f}, {dh + 1.96 * s:.4f})")
a.axvline(dh, color=P.muted(), lw=0.7, ls="--")
a.set_ylim(lmax - 12, lmax + 1)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower center")
charts.style_axes(a, "distance $d$", "log-likelihood $\\ell(d)$")
charts.title(a, "A  12S rRNA, human vs orangutan")

rng = np.random.default_rng(0)
dgrid = np.linspace(0.1, 2.0, 20)
for nn, tok in ((500, "dna"), (2000, "rna")):
    sd = []
    for d0 in dgrid:
        est = d_of(rng.binomial(nn, p_of(d0), 20000) / nn)
        sd.append(np.std(est[np.isfinite(est)]))
    b.plot(dgrid, sd, "o", ms=3.5, color=charts.line(tok), label=f"simulated, $n = {nn}$")
    dl = np.linspace(0.05, 2.0, 300)
    b.plot(dl, se(dl, nn), color=charts.line(tok), lw=1.2, label=f"delta method, $n = {nn}$")
b.set_yscale("log")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "true distance $d$", "standard deviation of $\\hat d$")
charts.title(b, "B  Standard error grows with $d$")

dl = np.linspace(0.5, 4.0, 300)
for nn, tok in ((100, "enzyme"), (500, "dna"), (2000, "rna")):
    pr = binom.sf(np.ceil(0.75 * nn) - 1, nn, p_of(dl))
    c.plot(dl, pr, color=charts.line(tok), lw=1.6, label=f"$n = {nn}$")
c.set_ylim(0, 0.6)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(c, "true distance $d$", "$\\mathbb{P}(\\hat p \\geq 3/4)$")
charts.title(c, "C  The estimate is infinite")
