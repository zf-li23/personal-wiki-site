"""Comparing two measurement methods (simulated): 100 patients measured once by a reference method and
once by a new method; true values from 80 to 200, new method = 5 + 1.0 x true, measurement error SD 12
for both methods. A: new against reference with the line of identity, the ordinary least-squares line
(slope attenuated because the reference also has error) and the Deming line (error-variance ratio 1).
B: Bland-Altman plot: differences against means, mean difference (bias) and 95 % limits of agreement.
The correlation is high (r about 0.9) although the methods do not agree within +/- 30 units.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
true = rng.uniform(80, 200, 100)
xr = true + rng.normal(0, 12, 100)
yn = 5 + true + rng.normal(0, 12, 100)


def deming(x, y, lam=1.0):
    sxx, syy = np.var(x, ddof=1), np.var(y, ddof=1)
    sxy = np.cov(x, y)[0, 1]
    b = (syy - lam * sxx + np.sqrt((syy - lam * sxx) ** 2 + 4 * lam * sxy ** 2)) / (2 * sxy)
    return y.mean() - b * x.mean(), b


bo, ao = np.polyfit(xr, yn, 1)
ad, bd = deming(xr, yn)
r = np.corrcoef(xr, yn)[0, 1]
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.7))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.87, wspace=0.27)
ax = axs[0]
g = np.array([60, 220])
ax.plot(g, g, color=P.muted(), lw=0.9, ls=":", label="identity")
ax.plot(g, ao + bo * g, color=charts.line("dna"), lw=1.3, label=f"OLS: slope {bo:.2f}")
ax.plot(g, ad + bd * g, color=charts.line("rna"), lw=1.5, label=f"Deming: slope {bd:.2f}")
ax.scatter(xr, yn, s=14, color=P.fill("enzyme"), edgecolor=charts.line("enzyme"), lw=0.6, zorder=3)
ax.text(65, 205, f"r = {r:.3f}", fontsize=FT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
ax.set_xlim(60, 220)
ax.set_ylim(60, 220)
charts.style_axes(ax, "reference method", "new method")
charts.title(ax, "A  Regression with errors in both")
ax = axs[1]
m = (xr + yn) / 2
d = yn - xr
bias, sd = d.mean(), d.std(ddof=1)
ax.scatter(m, d, s=14, color=P.fill("enzyme"), edgecolor=charts.line("enzyme"), lw=0.6, zorder=3)
for v, lab in [(bias, f"bias {bias:.1f}"), (bias + 1.96 * sd, f"+1.96 SD: {bias + 1.96 * sd:.1f}"),
               (bias - 1.96 * sd, f"-1.96 SD: {bias - 1.96 * sd:.1f}")]:
    ax.axhline(v, color=charts.line("rna"), lw=1.0, ls="-" if v == bias else "--")
    ax.text(222, v + 0.8, lab, fontsize=FT["tiny"], color=P.ink(), ha="right")
ax.axhline(0, color=P.muted(), lw=0.8, ls=":")
ax.set_xlim(70, 225)
charts.style_axes(ax, "mean of the two methods", "new - reference")
charts.title(ax, "B  Bland-Altman plot")
