"""Synonymous sites and the estimates of omega for the rbcL genes of cucumber and tobacco.
A: proportion of synonymous sites S/(S + N) in the universal genetic code with equal codon frequencies,
as a function of the transition/transversion rate ratio kappa (mutational opportunities weighted by
their rates; stop codons excluded). B: estimates of omega = dN/dS from the same pair of genes by six
counting methods and by maximum likelihood under codon models with different assumptions (values from
Yang (2014), Table 2.8)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
B = "TCAG"
AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codons = [a + b + c for a in B for b in B for c in B]
code = dict(zip(codons, AA))
sense = [c for c in codons if code[c] != "*"]


def is_ts(x, y):
    return {x, y} in ({"A", "G"}, {"C", "T"})


def syn_fraction(k):
    num = den = 0.0
    for c in sense:
        for p in range(3):
            for n in B:
                if n == c[p]:
                    continue
                d = c[:p] + n + c[p + 1:]
                if code[d] == "*":
                    continue
                r = k if is_ts(c[p], n) else 1.0
                den += r
                if code[d] == code[c]:
                    num += r
    return num / den


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8), gridspec_kw=dict(width_ratios=[1, 1.25]))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.55)
ks = np.linspace(0.5, 20, 60)
a.plot(ks, [syn_fraction(k) for k in ks], color=charts.line("dna"), lw=1.8)
for k in (1.0, 2.59):
    f = syn_fraction(k)
    a.scatter([k], [f], color=P.ink(), s=14, zorder=4)
    a.annotate(f"$\\kappa = {k:g}$: {f:.3f}", (k, f), xytext=(k + 1.5, f - 0.012), fontsize=FT["tiny"], color=P.ink())
a.set_xlim(0, 20)
charts.style_axes(a, "transition/transversion rate ratio $\\kappa$", "$S/(S + N)$")
charts.title(a, "A  Synonymous sites depend on $\\kappa$")

methods = ["NG86", "LWL85", "LWL85m", "LPB93", "Ina95", "YN00",
           "ML Fequal, $\\kappa = 1$", "ML Fequal, $\\hat\\kappa$", "ML F1x4, $\\hat\\kappa$",
           "ML F3x4, $\\hat\\kappa$", "ML F61, $\\hat\\kappa$", "ML FMutSel"]
omega = [0.095, 0.101, 0.134, 0.129, 0.131, 0.071, 0.096, 0.117, 0.099, 0.078, 0.074, 0.082]
y = np.arange(len(methods))[::-1]
cols = [charts.line("rna")] * 6 + [charts.line("dna")] * 6
b.barh(y, omega, color=[P.fill("rna")] * 6 + [P.fill("dna")] * 6, edgecolor=cols, lw=0.8, height=0.7)
b.set_yticks(y)
b.set_yticklabels(methods)
b.set_xlim(0, 0.15)
charts.style_axes(b, "$\\hat\\omega = \\hat d_{\\mathrm{N}}/\\hat d_{\\mathrm{S}}$")
b.tick_params(axis="y", labelsize=FT["tiny"])
charts.title(b, "B  $\\omega$ for *rbcL*: counting (orange) and likelihood (blue)".replace("*rbcL*", "$\\it{rbcL}$"))
