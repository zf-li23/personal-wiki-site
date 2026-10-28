"""The liability-threshold model of a disease with population prevalence K = 1 %. A: liability is normal with
variance 1 in the population; individuals above the threshold t = 2.33 are affected. Relatives of affected
individuals have a liability distribution (shown in its normal approximation) shifted to the right (here first-degree relatives for a
heritability of liability h^2 = 0.5, computed exactly from the bivariate normal distribution with correlation
r h^2 = 0.25), and a larger fraction of them lies above the threshold: recurrence risk 4.4 %. B: recurrence
risk relative to the population prevalence (lambda) for monozygotic twins, first-, second- and third-degree
relatives, for h^2 = 0.5 and 0.8, against the halving with each degree expected for a single dominant gene:
under the polygenic threshold model the risk falls off much faster than linearly with relatedness."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
K = 0.01
t = stats.norm.isf(K)


def recurrence(h2, r):
    rho = r * h2
    bv = stats.multivariate_normal(mean=[0, 0], cov=[[1, rho], [rho, 1]])
    both = 1 - 2 * stats.norm.cdf(t) + bv.cdf([t, t])
    return both / K


fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw={"width_ratios": [1.5, 1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.15, top=0.88, wspace=0.25)
a = axs[0]
x = np.linspace(-4, 5, 600)
y = stats.norm.pdf(x)
rho = 0.25
mu_aff = stats.norm.pdf(t) / K
mR = rho * mu_aff
vR = 1 - rho**2 * mu_aff * (mu_aff - t)
yR = stats.norm.pdf(x, mR, np.sqrt(vR))
a.plot(x, y, color=charts.line("dna"), lw=2, label="general population")
a.fill_between(x[x >= t], y[x >= t], color=P.fill("dna"), lw=0)
a.plot(x, yR, color=charts.line("rna"), lw=2, label="first-degree relatives of cases")
a.fill_between(x[x >= t], yR[x >= t], color=P.fill("rna"), lw=0, alpha=0.6)
a.axvline(t, color=P.ink(), lw=1)
a.text(t + 0.08, 0.3, f"threshold $t = {t:.2f}$", fontsize=FT["tiny"], color=P.ink())
a.text(t + 0.15, 0.05, f"{100 * K:g}% / {100 * recurrence(0.5, 0.5):.1f}% affected", fontsize=FT["tiny"], color=P.ink())
a.axvline(mR, color=charts.line("rna"), lw=0.8, ls=":")
a.set_xlim(-4, 5)
a.set_ylim(0, 0.45)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "liability (SD units)", "density")
charts.title(a, "A  Liability and threshold, $K = 1\\%$")
b = axs[1]
rs = [1, 0.5, 0.25, 0.125]
labels = ["MZ", "1st", "2nd", "3rd"]
for h2, tok in ((0.8, "rna"), (0.5, "dna")):
    b.semilogy(range(4), [recurrence(h2, r) / K for r in rs], "o-", color=charts.line(tok), lw=1.8, ms=4,
               label=f"threshold model, $h^2 = {h2}$")
b.semilogy(range(4), [100, 50, 25, 12.5], "s--", color=P.muted(), lw=1.2, ms=3, label="single dominant gene (×1/2)")
b.set_xticks(range(4), labels)
b.set_ylim(1, 160)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "relationship to an affected person", "relative risk $\\lambda$")
charts.title(b, "B  Recurrence risk falls fast")
