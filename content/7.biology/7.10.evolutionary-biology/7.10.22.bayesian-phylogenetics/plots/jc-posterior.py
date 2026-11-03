"""Bayesian estimation of a JC69 distance. A: the human and orangutan mitochondrial 12S rRNA genes
(x = 90 differences at n = 948 sites; data from Yang (2014)): the exponential prior with mean 0.2, the
likelihood (scaled to the height of the posterior) and the posterior, with the posterior mean and the 95%
equal-tail credible interval. B: the posterior under four priors (exponential with mean 0.2 or 10,
uniform on (0, 10) and the gamma prior G(100, 10) with mean 10); the data dominate all except the strongly
informative gamma prior. C: the human and chimpanzee genes (x = 11 at n = 946), whose likelihood is far
from the same gamma prior: the log posterior has its highest mode well above the MLE and a second local
mode near the prior mean, lower by many log units but able to trap an MCMC sampler started there; dots
mark the local maxima."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, gamma, uniform
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def loglik(d, x, n):
    e = np.exp(-4 * d / 3)
    return x * np.log(0.75 - 0.75 * e) + (n - x) * np.log(0.25 + 0.75 * e)


def posterior(d, logprior, x, n):
    lp = logprior + loglik(d, x, n)
    w = np.exp(lp - lp.max())
    return w / np.trapezoid(w, d)


fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.0, 3.8))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.16, top=0.9, wspace=0.3)
d = np.linspace(1e-5, 0.3, 6000)
x, n = 90, 948
prior = expon.pdf(d, scale=0.2)
post = posterior(d, np.log(prior), x, n)
lik = np.exp(loglik(d, x, n) - loglik(d, x, n).max()) * post.max()
cdf = np.cumsum(post) * (d[1] - d[0])
lo, hi = np.interp([0.025, 0.975], cdf, d)
mean = np.trapezoid(d * post, d)
a.plot(d, prior, color=P.muted(), lw=1.2, ls="--", label="prior Exp(mean 0.2)")
a.plot(d, lik, color=charts.line("enzyme"), lw=1.2, ls=":", label="likelihood (scaled)")
a.plot(d, post, color=charts.line("dna"), lw=1.7, label="posterior")
m = (d >= lo) & (d <= hi)
a.fill_between(d[m], 0, post[m], color=P.fill("dna"), alpha=0.35, lw=0)
a.text(0.16, 0.75 * post.max(), f"mean {mean:.4f}\n95% CI ({lo:.4f}, {hi:.4f})", fontsize=FT["tiny"], color=P.ink())
a.set_xlim(0, 0.3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "distance $d$", "density")
charts.title(a, "A  12S rRNA, human vs orangutan")

priors = [("Exp(mean 0.2)", expon.logpdf(d, scale=0.2), "dna"), ("Exp(mean 10)", expon.logpdf(d, scale=10), "rna"),
          ("U(0, 10)", np.zeros_like(d), "plant"), ("G(100, 10)", gamma.logpdf(d, 100, scale=0.1), "negative")]
for lab, lp, tok in priors:
    b.plot(d, posterior(d, lp, x, n), color=charts.line(tok), lw=1.4, label=lab)
b.set_xlim(0.04, 0.3)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "distance $d$", "posterior density")
charts.title(b, "B  Sensitivity to the prior")

dd = np.logspace(-3, 1.6, 6000)
x2, n2 = 11, 946
lpri = gamma.logpdf(dd, 100, scale=0.1)
llk = loglik(dd, x2, n2)
lp = lpri + llk
top = lp.max()
c.plot(dd, lp - top, color=charts.line("negative"), lw=1.6, label="log posterior")
c.plot(dd, llk - llk.max(), color=charts.line("enzyme"), lw=1.0, ls=":", label="log likelihood")
c.plot(dd, lpri - lpri.max(), color=P.muted(), lw=1.0, ls="--", label="log prior G(100, 10)")
loc = [k for k in range(1, len(dd) - 1) if lp[k] > lp[k - 1] and lp[k] > lp[k + 1]]
for k in loc:
    c.plot([dd[k]], [lp[k] - top], "o", ms=4, color=charts.line("negative"))
    c.text(dd[k], lp[k] - top + 40, f"{dd[k]:.3g}", ha="center", fontsize=FT["tiny"], color=P.ink())
c.set_xscale("log")
c.set_ylim(-1300, 80)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(c, "distance $d$", "log density (relative to maximum)")
charts.title(c, "C  Prior–likelihood conflict, human vs chimpanzee")
