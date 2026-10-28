"""Truncation selection and the breeder's equation (phenotypes standardized: mean 0, SD 1). The parents are
the top 20 % of the population (threshold z = 0.84); their mean exceeds the population mean by the selection
differential S = i sigma_P with selection intensity i = phi(z)/0.2 = 1.40. With h^2 = 0.4 the offspring of
random mating among the selected parents have mean R = h^2 S = 0.56 (dashed curve: offspring distribution,
assumed normal with the same variance). Right: selection intensity i as a function of the proportion
selected."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw={"width_ratios": [1.7, 1]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.15, top=0.88, wspace=0.25)
a = axs[0]
x = np.linspace(-3.5, 4, 500)
z = stats.norm.isf(0.2)
i = stats.norm.pdf(z) / 0.2
h2 = 0.4
R = h2 * i
y = stats.norm.pdf(x)
a.plot(x, y, color=charts.line("dna"), lw=2, label="parental generation")
a.fill_between(x[x >= z], y[x >= z], color=P.fill("dna"), lw=0, alpha=0.6)
a.plot(x, stats.norm.pdf(x, R), color=charts.line("rna"), lw=2, ls="--", label="offspring of the selected")
a.axvline(z, color=P.muted(), lw=0.9)
a.text(z + 0.05, 0.36, f"threshold $z = {z:.2f}$\n20% selected", fontsize=FT["tiny"], color=P.muted())
for xv, lab, tok, yv in ((0, "$\\mu$", "muted", 0.43), (i, "$\\mu_S$", "dna", 0.43), (R, "$\\mu'$", "rna", 0.47)):
    a.plot([xv, xv], [0, yv], color=P.ink() if tok == "muted" else charts.line(tok), lw=1)
    a.text(xv, yv + 0.005, lab, ha="center", va="bottom", fontsize=FT["small"], color=P.ink())
a.annotate("", xy=(i, 0.025), xytext=(0, 0.025), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
a.text(i / 2, 0.035, f"$S = {i:.2f}$", ha="center", fontsize=FT["tiny"], color=P.ink())
a.annotate("", xy=(R, 0.08), xytext=(0, 0.08), arrowprops=dict(arrowstyle="<->", color=charts.line("rna"), lw=0.8))
a.text(R / 2, 0.09, f"$R = h^2S = {R:.2f}$", ha="center", fontsize=FT["tiny"], color=charts.line("rna"))
a.set_ylim(0, 0.52)
a.set_xlim(-3.5, 4)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "phenotype (SD units)", "density")
charts.title(a, "A  Response to truncation selection, $h^2 = 0.4$")
b = axs[1]
pp = np.logspace(-3, 0, 300)[:-1]
b.semilogx(pp, stats.norm.pdf(stats.norm.isf(pp)) / pp, color=charts.line("enzyme"), lw=2)
for pv in (0.5, 0.2, 0.05, 0.01):
    iv = stats.norm.pdf(stats.norm.isf(pv)) / pv
    b.scatter([pv], [iv], s=14, color=P.ink(), zorder=4)
    b.text(pv * 1.15, iv + 0.06, f"{iv:.2f}", fontsize=FT["tiny"], color=P.ink())
b.set_ylim(0, 3.6)
charts.style_axes(b, "proportion selected $p$", "selection intensity $i$")
charts.title(b, "B  $i = \\varphi(z)/p$")
