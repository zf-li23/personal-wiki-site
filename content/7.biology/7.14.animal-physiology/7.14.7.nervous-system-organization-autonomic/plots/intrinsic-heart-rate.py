"""Tonic vagal restraint of the heart: intrinsic versus resting heart rate.

Intrinsic heart rate (after combined block of muscarinic and beta-adrenergic receptors with atropine
and propranolol) falls with age, IHR = 118.1 - 0.57 x age (beats per minute; Jose and Collison 1970),
with 95 % limits of about +-14 % below age 45 and +-18 % above. The band 60-80 per minute is a typical
resting rate of healthy adults. Resting rate lies below the intrinsic rate: at rest vagal (parasympathetic)
tone outweighs sympathetic tone; the gap narrows with age as the intrinsic rate falls.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
age = np.linspace(20, 80, 200)
ihr = 118.1 - 0.57 * age
band = np.where(age < 45, 0.14, 0.18)

fig, ax = plt.subplots(figsize=(6.8, 4.2))
ax.fill_between(age, ihr * (1 - band), ihr * (1 + band), color=P.fill("negative"), alpha=0.3, lw=0,
                label="95 % range of intrinsic rate")
ax.plot(age, ihr, color=P.edge("negative"), lw=2.2, label="intrinsic rate (autonomic block)")
ax.axhspan(60, 80, color=P.fill("dna"), alpha=0.35, lw=0, label="typical resting rate")
ax.annotate("", xy=(30, 72), xytext=(30, 118.1 - 0.57 * 30), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.4))
ax.text(31.5, 88, "net vagal tone", fontsize=9, color=P.ink())
ax.set_xlim(20, 80)
ax.set_ylim(40, 140)
ax.set_xlabel("Age / years")
ax.set_ylabel("Heart rate / min$^{-1}$")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.grid(True, alpha=0.3)
fig.tight_layout()
