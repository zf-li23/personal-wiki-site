"""Monocular deprivation and the critical period (schematic, after Wiesel and Hubel 1963 and Hensch 2005).

A: idealized ocular dominance histograms (Hubel-Wiesel classes 1 = driven only by the contralateral eye, 4 = equal,
7 = only ipsilateral eye). Values are idealized, chosen to reproduce the shape of the classic cat and monkey data:
normal rearing, closure of the contralateral eye for a few days in the critical period, the same in the adult.
B: the inhibitory-threshold picture of the critical period: the maturation of inhibition (PV interneuron
output) crosses a lower threshold at onset and an upper threshold at closing; plasticity (shaded) is present between
them. A mutant with weak inhibition (GAD65 knockout) never reaches the lower threshold and has no critical period
until inhibition is raised pharmacologically (benzodiazepine); dark rearing delays maturation; the thresholds and
times are schematic (mouse-like time axis, postnatal days).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
classes = np.arange(1, 8)
normal = np.array([0.10, 0.12, 0.15, 0.22, 0.16, 0.14, 0.11])
md_crit = np.array([0.01, 0.01, 0.02, 0.04, 0.07, 0.14, 0.71])
md_adult = np.array([0.08, 0.12, 0.14, 0.22, 0.17, 0.15, 0.12])

fig, axs = plt.subplots(1, 4, figsize=(14, 3.8), gridspec_kw=dict(width_ratios=[1, 1, 1, 1.6]))
for ax, h, t in zip(axs[:3], (normal, md_crit, md_adult),
                    ("A  Normal", "Deprived, critical period", "Deprived, adult")):
    cols = [P.edge("negative")] * 3 + [P.edge("neutral")] + [P.edge("dna")] * 3
    ax.bar(classes, h, color=[P.fill("negative")] * 3 + [P.fill("neutral")] + [P.fill("dna")] * 3,
           edgecolor=cols, lw=0.8)
    ax.set_ylim(0, 0.8)
    ax.set_xlabel("Ocular dominance class")
    ax.set_xticks(classes)
    ax.set_title(t, fontsize=9, loc="left")
axs[0].set_ylabel("Fraction of cells")

t = np.linspace(0, 80, 400)
inh = lambda t0, k, top: top / (1 + np.exp(-(t - t0) / k))
lo, hi = 0.35, 0.8
bx = axs[3]
wt = inh(26, 5, 1.0)
ko = inh(26, 5, 0.3)
dr = inh(40, 6, 1.0)
bx.plot(t, wt, color=P.edge("dna"), lw=2, label="wild type")
bx.plot(t, dr, color=P.edge("rna"), lw=2, ls="--", label="dark reared (delayed)")
bx.plot(t, ko, color=P.edge("negative"), lw=2, label="weak inhibition (GAD65 knockout)")
bx.axhline(lo, color=P.muted(), lw=0.8, ls=":")
bx.axhline(hi, color=P.muted(), lw=0.8, ls=":")
bx.text(1, lo + 0.02, "onset threshold", fontsize=7.5, color=P.muted())
bx.text(1, hi + 0.02, "closing threshold", fontsize=7.5, color=P.muted())
m = (wt > lo) & (wt < hi)
bx.fill_between(t, 0, 1.05, where=m, color=P.fill("dna"), alpha=0.25, lw=0)
bx.set_ylim(0, 1.1)
bx.set_xlabel("Postnatal day")
bx.set_ylabel("Inhibitory strength (relative)")
bx.legend(frameon=False, fontsize=7.5, loc="lower right")
bx.set_title("B  Window set by inhibition (schematic)", loc="left", fontsize=9)
fig.tight_layout()
