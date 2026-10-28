"""A threshold model of the A^vy epiallele (illustrative parameters). Each A^vy/a offspring has an IAP
methylation level m drawn from a Beta distribution with mean mu (set by the mother: her phenotype, or her
diet) and concentration kappa; fixed thresholds of m divide the offspring into five coat classes."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
classes = ["yellow", "slightly\nmottled", "mottled", "heavily\nmottled", "pseudo-\nagouti"]
cuts = np.array([0.0, 0.2, 0.35, 0.5, 0.65, 1.0])
kappa = 5.0


def probs(mu):
    a, b = mu * kappa, (1 - mu) * kappa
    return np.diff(stats.beta.cdf(cuts, a, b))


fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.9))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.2, top=0.88, wspace=0.22)
sets = [("A  Phenotype of the $A^{vy}/a$ mother", [("yellow mother", 0.32, "highlight"), ("pseudoagouti mother", 0.46, "dna")]),
        ("B  Diet of the $a/a$ mother during pregnancy", [("control diet", 0.32, "neutral"), ("methyl-donor supplement", 0.52, "positive")])]
x = np.arange(len(classes))
for a, (title, groups) in zip(axs, sets):
    for k, (name, mu, tok) in enumerate(groups):
        p = probs(mu)
        a.bar(x + (k - 0.5) * 0.38, p, width=0.36, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8,
              label=f"{name} (mean m = {mu:.2f})")
    a.set_xticks(x)
    a.set_xticklabels(classes, fontsize=FT["tiny"])
    a.set_ylim(0, 0.42)
    a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
    charts.style_axes(a, "coat class (methylation of the IAP increases to the right)", "fraction of offspring")
    charts.title(a, title)
