"""The likelihood ratio test when the null value lies on the boundary of the parameter space. Data:
n = 50 observations from N(mu, 1); H0: mu = 0 against H1: mu >= 0, so the MLE under H1 is max(xbar, 0)
and 2 delta l = n max(xbar, 0)^2. A: distribution of 2 delta l over 20 000 data sets simulated under
H0: half of them give exactly 0 (bar at left, its height is the proportion), the rest follow chi-square
with 1 df (line). B: tail probabilities P(2 delta l > c) from the simulation (dots) compared with the
1:1 mixture of 0 and chi-square(1), with chi-square(1) and with chi-square(2); the 5 % critical values
are 2.71, 3.84 and 5.99. Using chi-square(1) or chi-square(2) instead of the mixture makes a test
conservative, as for the branch-site test and for the comparison of M1a with M2a."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(3)
n, reps = 50, 20000
xbar = rng.normal(0, 1 / np.sqrt(n), reps)
lrt = n * np.maximum(xbar, 0) ** 2
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.28)
pos = lrt[lrt > 0]
bins = np.linspace(0, 8, 41)
w = bins[1] - bins[0]
a.hist(pos, bins=bins, weights=np.full(len(pos), 1 / (reps * w)), color=P.fill("dna"), edgecolor=P.edge("dna"),
       lw=0.4, label="simulated, $2\\Delta\\ell > 0$")
x = np.linspace(0.05, 8, 200)
a.plot(x, 0.5 * stats.chi2.pdf(x, 1), color=P.ink(), lw=1.2, label="$\\frac{1}{2}\\chi^2_1$ density")
p0 = np.mean(lrt == 0)
a.bar([-0.25], [p0], width=0.3, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.6)
a.annotate(f"point mass at 0: {p0:.3f}", (-0.25, p0), xytext=(1.2, 0.55), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6), fontsize=FT["tiny"], color=P.ink())
a.set_xlim(-0.6, 8)
a.set_ylim(0, 0.62)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "$2\\Delta\\ell$", "density (bar: probability)")
charts.title(a, "A  Null distribution on the boundary")
c = np.linspace(0, 8, 200)
b.plot(c, 0.5 * stats.chi2.sf(c, 1), color=charts.line("dna"), lw=1.8, label="$\\frac{1}{2}$:$\\frac{1}{2}$ mixture of $0$ and $\\chi^2_1$")
b.plot(c, stats.chi2.sf(c, 1), color=charts.line("rna"), lw=1.2, ls="--", label="$\\chi^2_1$")
b.plot(c, stats.chi2.sf(c, 2), color=P.muted(), lw=1.2, ls=":", label="$\\chi^2_2$")
cc = np.arange(0.5, 8, 0.5)
b.scatter(cc, [np.mean(lrt > v) for v in cc], s=12, color=P.ink(), zorder=4, label="simulation")
b.axhline(0.05, color=P.muted(), lw=0.6)
for v in (2.71, 3.84, 5.99):
    b.axvline(v, color=P.muted(), lw=0.6, ls="-.")
    b.text(v + 0.08, 0.42, f"{v}", fontsize=FT["tiny"], color=P.ink())
b.set_ylim(0, 0.5)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(b, "critical value $c$", "$\\mathbb{P}(2\\Delta\\ell > c)$")
charts.title(b, "B  Tail probabilities and critical values")
