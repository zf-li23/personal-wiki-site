"""Counting molecules by the noise of their partition at division.

Each of the N fluorescent molecules of a mother cell goes to daughter 1 with probability 1/2,
independently (binomial partitioning). A: distribution of the fraction n1/N received by daughter 1
for N = 10, 100 and 1000 (20000 divisions each) with the normal approximations of standard deviation
1/(2 sqrt N). B: a simulated calibration experiment: 400 mother cells with N drawn log-uniformly
between 20 and 2000, each molecule contributing alpha = 50 fluorescence units plus measurement noise
of 0.5 % of each daughter's intensity; points show (I1 - I2)^2 against I1 + I2 (logarithmic axes), open circles the binned
means, the line <(I1 - I2)^2> = alpha (I1 + I2) with the slope estimated as the mean of (I1 - I2)^2/(I1 + I2), which
recovers the brightness of one molecule (fitted value printed in the panel)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(11)

fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.97, bottom=0.16, top=0.88)
ax = axs[0]
for N, tok in ((10, "rna"), (100, "dna"), (1000, "protein")):
    f = rng.binomial(N, 0.5, 20000) / N
    step = 1.0 / N if N <= 100 else 0.005
    bins = np.arange(-0.5 * step, 1 + step, step)
    ax.hist(f, bins=bins, density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.3, alpha=0.6,
            label=f"N = {N}")
    x = np.linspace(0, 1, 400)
    s = 0.5 / np.sqrt(N)
    ax.plot(x, np.exp(-(x - 0.5) ** 2 / (2 * s * s)) / (s * np.sqrt(2 * np.pi)), color=charts.line(tok), lw=1.0)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"fraction received by daughter 1, $n_1/N$", "probability density")
charts.title(ax, "A  Binomial partitioning")

ax = axs[1]
alpha = 50.0
N = np.exp(rng.uniform(np.log(20), np.log(2000), 400)).astype(int)
n1 = rng.binomial(N, 0.5)
I1 = alpha * n1 * (1 + 0.005 * rng.normal(size=N.size))
I2 = alpha * (N - n1) * (1 + 0.005 * rng.normal(size=N.size))
It, dI2 = I1 + I2, (I1 - I2) ** 2
ax.plot(It, dI2, ".", color=charts.line("protein"), ms=3, alpha=0.5, label="single divisions")
edges = np.logspace(np.log10(It.min()), np.log10(It.max()), 9)
idx = np.digitize(It, edges)
xb = [It[idx == k].mean() for k in range(1, len(edges)) if (idx == k).sum() > 5]
yb = [dI2[idx == k].mean() for k in range(1, len(edges)) if (idx == k).sum() > 5]
ax.plot(xb, yb, "o", mfc="none", mec=P.ink(), ms=6, mew=1.2, label="binned means")
fit = np.mean(dI2 / It)
xs = np.logspace(np.log10(It.min()), np.log10(It.max()), 10)
ax.plot(xs, fit * xs, color=P.ink(), lw=1.2, label=r"$\langle(I_1 - I_2)^2\rangle = \alpha(I_1 + I_2)$")
ax.text(0.04, 0.6, f"fitted alpha = {fit:.0f} (true 50)", transform=ax.transAxes,
        fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(np.percentile(dI2, 3), dI2.max() * 2)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"mother intensity $I_1 + I_2$ / a.u.", r"$(I_1 - I_2)^2$ / a.u.$^2$")
charts.title(ax, "B  Calibrating one molecule")
