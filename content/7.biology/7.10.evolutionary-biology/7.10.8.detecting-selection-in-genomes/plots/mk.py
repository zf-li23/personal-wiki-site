"""McDonald-Kreitman test. A: Adh data (McDonald and Kreitman 1991): fraction of nonsynonymous changes among
fixed differences (7 of 24) and among polymorphisms (2 of 44); the dashed bar is the nonsynonymous fraction
expected among fixed differences if divergence followed the polymorphism ratio, 0.81 / (0.81 + 17).
B: expected MK estimate of alpha under a nearly neutral model, from the equilibrium frequency density of
derived alleles f(x) ~ (1 - exp(-S(1 - x))) / ((1 - exp(-S)) x (1 - x)) with S = 4 N_e s, and relative
substitution rate S / (1 - exp(-S)). Synonymous sites neutral; nonsynonymous: 70 % strongly deleterious
(no contribution), 20 % weakly deleterious (S = -5), 10 % neutral, plus adaptive substitutions making up
alpha = 0.3 of nonsynonymous divergence. alpha_hat = 1 - (P_N/P_S)/(D_N/D_S) counting polymorphisms with
population frequency of the derived allele above c."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8), gridspec_kw={"width_ratios": [0.8, 1.2]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.3)
vals = [7 / 24, 2 / 44]
a.bar([0, 1], vals, color=[P.fill("rna"), P.fill("dna")], edgecolor=[P.edge("rna"), P.edge("dna")], width=0.55)
exp_fix = 17 * 2 / 42
a.bar([0], [exp_fix / (exp_fix + 17)], width=0.55, fill=False, edgecolor=P.ink(), ls="--", lw=1.1)
for x, v, lab in ((0, vals[0], "7 / 24"), (1, vals[1], "2 / 44")):
    a.text(x, v + 0.01, lab, ha="center", fontsize=FT["tiny"], color=P.ink())
a.text(0.33, exp_fix / (exp_fix + 17) + 0.005, "expected\nif neutral", fontsize=FT["tiny"], color=P.ink())
a.set_xticks([0, 1], ["fixed differences", "polymorphisms"])
a.set_ylim(0, 0.36)
charts.style_axes(a, None, "nonsynonymous fraction")
a.set_title("A  $\\it{Adh}$ in $\\it{Drosophila}$", fontsize=FT["small"], color=P.ink(), loc="left", weight="bold")


def f(x, S):
    if S == 0:
        return 1 / x
    return (1 - np.exp(-S * (1 - x))) / ((1 - np.exp(-S)) * x * (1 - x))


def poly(c, S):
    return quad(f, c, 1 - 1e-6, args=(S,), limit=200)[0]


def rate(S):
    return 1.0 if S == 0 else S / (1 - np.exp(-S))


Sw, fw, fn, alpha = -5.0, 0.2, 0.1, 0.3
DN_nonadapt = fw * rate(Sw) + fn
DN = DN_nonadapt / (1 - alpha)
DS = 1.0
cs = np.logspace(-3, np.log10(0.5), 40)
ah = []
for c in cs:
    PN = fw * poly(c, Sw) + fn * poly(c, 0)
    PS = poly(c, 0)
    ah.append(1 - (PN / PS) / (DN / DS))
b.semilogx(cs, ah, color=charts.line("rna"), lw=1.8, label="$\\hat\\alpha$ from polymorphisms above $c$")
b.axhline(alpha, color=P.ink(), lw=1, ls="--", label="true $\\alpha = 0.3$")
b.axhline(0, color=P.muted(), lw=0.7, ls=":")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "frequency cutoff $c$ for polymorphisms", "estimated $\\alpha$")
charts.title(b, "B  Slightly deleterious polymorphisms bias $\\hat\\alpha$")
