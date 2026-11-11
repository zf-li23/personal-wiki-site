"""The hypothetical temporal order of Alzheimer's disease biomarkers (after Jack et al. 2010, 2013).

Each biomarker is drawn as a logistic curve of abnormality against time relative to dementia onset:
amyloid (CSF Abeta42 and amyloid PET) mid-point -15 y, tau (CSF p-tau and tau PET) -8 y, neurodegeneration
(MRI atrophy, FDG-PET hypometabolism) -4 y, memory impairment -1 y, clinical function 0 y; slopes
0.35-0.55 per year. Schematic: the curves illustrate an ordering hypothesis, not fitted data.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
t = np.linspace(-30, 10, 400)
curves = [
    ("Amyloid (CSF A$\\beta$42, amyloid PET)", -15, 0.35, "negative"),
    ("Tau (CSF p-tau, tau PET)", -8, 0.45, "protein"),
    ("Neurodegeneration (MRI atrophy, FDG-PET)", -4, 0.45, "dna"),
    ("Memory impairment", -1, 0.5, "enzyme"),
    ("Clinical function", 0, 0.55, "rna"),
]
fig, ax = plt.subplots(figsize=(8.5, 4.0))
for name, mid, k, tok in curves:
    ax.plot(t, 1 / (1 + np.exp(-k * (t - mid))), color=P.edge(tok), lw=2.0, label=name)
ax.axvspan(-30, -10, color=P.fill("neutral"), alpha=0.35, lw=0)
ax.axvspan(-10, 0, color=P.fill("highlight"), alpha=0.35, lw=0)
ax.text(-20, 1.05, "preclinical", ha="center", fontsize=8, color=P.muted())
ax.text(-5, 1.05, "prodromal (MCI)", ha="center", fontsize=8, color=P.muted())
ax.text(5, 1.05, "dementia", ha="center", fontsize=8, color=P.muted())
ax.axvline(0, color=P.muted(), lw=0.8, ls="--")
ax.set_ylim(-0.02, 1.12)
ax.set_xlabel("Years relative to onset of dementia")
ax.set_ylabel("Biomarker abnormality (normalized)")
ax.legend(frameon=False, fontsize=7.5, loc="center left", bbox_to_anchor=(0.0, 0.55))
ax.grid(True, alpha=0.3)
fig.tight_layout()
