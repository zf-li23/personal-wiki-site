"""Predictive values depend on prevalence. Positive (A) and negative (B) predictive value against the
prevalence of disease among those tested, for low-dose CT screening for lung cancer at the first round of
the National Lung Screening Trial (sensitivity 93.8 %, specificity 73.4 %) and for rapid antigen tests for
SARS-CoV-2 in symptomatic people (pooled sensitivity 73.0 %, specificity 99.1 %). Dots: the prevalence of
about 1.1 % in the screening trial, where the PPV of a positive CT is only 3.8 %.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
tests = [("low-dose CT (Se 0.938, Sp 0.734)", 0.938, 0.734, "dna"),
         ("antigen test (Se 0.730, Sp 0.991)", 0.73, 0.991, "rna")]
p = np.logspace(-4, np.log10(0.6), 400)


def ppv(se, sp, p):
    return se * p / (se * p + (1 - sp) * (1 - p))


def npv(se, sp, p):
    return sp * (1 - p) / (sp * (1 - p) + (1 - se) * p)


fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.6))
fig.subplots_adjust(left=0.07, right=0.99, bottom=0.16, top=0.88, wspace=0.25)
for name, se, sp, tok in tests:
    axs[0].semilogx(p, ppv(se, sp, p), color=charts.line(tok), lw=1.8, label=name)
    axs[1].semilogx(p, npv(se, sp, p), color=charts.line(tok), lw=1.8, label=name)
axs[0].plot(0.011, ppv(0.938, 0.734, 0.011), "o", color=charts.line("dna"), ms=5)
axs[0].annotate(f"PPV {ppv(0.938, 0.734, 0.011):.3f} at 1.1 %", (0.011, ppv(0.938, 0.734, 0.011)), xytext=(0.03, 0.1),
                fontsize=FT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
axs[1].plot(0.011, npv(0.938, 0.734, 0.011), "o", color=charts.line("dna"), ms=5)
axs[0].set_ylim(0, 1.02)
axs[1].set_ylim(0.6, 1.005)
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
for ax in axs:
    ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1, 0.5])
    ax.set_xticklabels(["0.01 %", "0.1 %", "1 %", "10 %", "50 %"])
charts.style_axes(axs[0], "prevalence among those tested", "P(disease | test +)")
charts.style_axes(axs[1], "prevalence among those tested", "P(no disease | test -)")
charts.title(axs[0], "A  Positive predictive value")
charts.title(axs[1], "B  Negative predictive value")
