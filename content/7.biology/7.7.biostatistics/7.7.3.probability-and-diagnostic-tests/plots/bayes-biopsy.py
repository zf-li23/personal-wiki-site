"""Bayes' theorem with three diagnoses. A 60-year-old man with chronic cough has a lung biopsy that is
consistent with lung cancer or with sarcoidosis; P(findings | normal) = 0.001 and P(findings | cancer) =
P(findings | sarcoidosis) = 0.9 (a textbook example). Prior and posterior probabilities for a man who has
never smoked (priors 0.99, 0.001, 0.009) and for a heavy smoker (priors 0.98, 0.015, 0.005): the same
findings point to sarcoidosis (0.81) in the first man and to lung cancer (0.71) in the second.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
states = ["normal", "lung cancer", "sarcoidosis"]
lik = np.array([0.001, 0.9, 0.9])
priors = {"never smoker": np.array([0.99, 0.001, 0.009]), "heavy smoker": np.array([0.98, 0.015, 0.005])}
fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.4), sharey=True)
fig.subplots_adjust(left=0.08, right=0.99, bottom=0.14, top=0.87, wspace=0.08)
x = np.arange(3)
w = 0.38
for ax, (name, pr) in zip(axs, priors.items()):
    post = lik * pr / (lik * pr).sum()
    ax.bar(x - w / 2, pr, w, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, label="prior")
    ax.bar(x + w / 2, post, w, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.8, label="posterior")
    for xi, a, b in zip(x, pr, post):
        ax.text(xi - w / 2, a + 0.02, f"{a:.3g}", ha="center", fontsize=FT["tiny"], color=P.ink())
        ax.text(xi + w / 2, b + 0.02, f"{b:.3f}", ha="center", fontsize=FT["tiny"], color=P.ink())
    ax.set_xticks(x)
    ax.set_xticklabels(states)
    ax.set_ylim(0, 1.1)
    charts.style_axes(ax, None, "probability" if ax is axs[0] else None)
    charts.title(ax, f"{'A' if ax is axs[0] else 'B'}  {name}")
axs[0].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
