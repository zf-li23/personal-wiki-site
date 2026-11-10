# The affinity (signal-strength) window of thymic selection, as a Monte Carlo model.
# Each double-positive thymocyte gets a random TCR; its strongest signal from self-peptide-MHC in the thymus is
# summarised by one number x = log10(signal strength), drawn from a normal distribution (mean 0, sd 1).
# Fates by thresholds (illustrative, chosen so that the fractions match the order of magnitude reported for
# mouse thymus: about 90% die by neglect, a few % are deleted, 2-5% are exported):
#   x < 1.405            death by neglect
#   1.405 <= x < 1.74    positive selection (conventional T cell)
#   1.74 <= x < 1.79     agonist selection into the thymic Treg lineage
#   x >= 1.79            negative selection (clonal deletion)
# Panel B shifts every signal by log10(d), d being a relative density of self-peptide-MHC, to show how
# changing MHC expression changes the outcome.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
x = rng.normal(0, 1, 400_000)
T_POS, T_TREG, T_NEG = 1.405, 1.74, 1.79
FATES = [("death by neglect", "neutral"), ("positive selection", "positive"), ("Treg lineage", "dna"),
         ("negative selection", "negative")]


def fates(v):
    return np.array([np.mean(v < T_POS), np.mean((v >= T_POS) & (v < T_TREG)), np.mean((v >= T_TREG) & (v < T_NEG)),
                     np.mean(v >= T_NEG)])


fig, axs = plt.subplots(1, 2, figsize=(10, 3.5), gridspec_kw={"width_ratios": [1.25, 1]})
bins = np.linspace(-4, 4.5, 171)
edges = [-np.inf, T_POS, T_TREG, T_NEG, np.inf]
for k, (name, tok) in enumerate(FATES):
    sel = x[(x >= edges[k]) & (x < edges[k + 1])]
    axs[0].hist(sel, bins=bins, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.3, label=name)
f = fates(x)
for xv in (T_POS, T_NEG):
    axs[0].axvline(xv, color=P.muted(), lw=0.8, ls="--")
txt = "\n".join(f"{n}: {100 * v:.1f}%" for (n, _), v in zip(FATES, f))
axs[0].set_yscale("log")
axs[0].set_ylim(1, 2e5)
axs[0].text(-3.9, 1.6e5, txt, fontsize=7, color=P.ink(), va="top")
charts.style_axes(axs[0], "self-pMHC signal strength, log10 (arbitrary units)", "thymocytes (of 400 000)")
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.title(axs[0], "A")

shift = np.linspace(-1.0, 1.0, 81)
fr = np.array([fates(x + s) for s in shift])
for k, (name, tok) in enumerate(FATES[1:], start=1):
    axs[1].plot(10 ** shift, 100 * fr[:, k], color=charts.line(tok), lw=1.5, label=name)
axs[1].plot(10 ** shift, 100 * (fr[:, 1] + fr[:, 2]), color=P.ink(), lw=1.0, ls="--", label="exported (sum)")
axs[1].set_xscale("log")
axs[1].axvline(1, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(axs[1], "relative density of self-pMHC", "percent of DP thymocytes")
axs[1].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper left")
charts.title(axs[1], "B")
fig.tight_layout()
