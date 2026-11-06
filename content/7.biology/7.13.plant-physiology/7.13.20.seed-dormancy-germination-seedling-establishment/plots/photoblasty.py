# Phytochrome control of germination in light-requiring seeds. (A) Red/far-red reversibility in the style of
# Borthwick et al. (1952) for lettuce cv. Grand Rapids: germination after a sequence of brief red (R) and
# far-red (FR) pulses is decided by the last pulse (values illustrative). (B) Germination as a function of the
# phytochrome photoequilibrium Pfr/Ptot set by the light (approximately 0.85 after red, 0.03 after far red):
# a population threshold model, G = Phi((phi - mu) / s), with thresholds for a light-requiring, an
# intermediate and a shade-sensitive population (mu = 0.30, 0.15, 0.55; s = 0.08).
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw=dict(width_ratios=[1.1, 1]))
seqs = ["dark", "R", "R FR", "R FR R", "R FR R FR", "R FR R FR R"]
vals = [8, 92, 7, 90, 9, 89]
cols = ["0.6" if s == "dark" else ("#c0504d" if s.split()[-1] == "R" else "#7b3f9e") for s in seqs]
a.barh(range(len(seqs)), vals, color=cols)
a.set_yticks(range(len(seqs)))
a.set_yticklabels(seqs)
a.invert_yaxis()
a.set_xlim(0, 100)
a.set_xlabel("Germination / %")
a.set_title("A   The last pulse decides", loc="left", fontsize=10)
for i, v in enumerate(vals):
    a.text(v + 1.5, i, f"{v}", va="center", fontsize=8.5)
phi = np.linspace(0, 0.9, 300)
for mu, c, name in ((0.15, "#2f6fb5", "low threshold"), (0.30, "#c0504d", "light-requiring"), (0.55, "#3a9a5b", "canopy-sensitive")):
    b.plot(phi, norm.cdf((phi - mu) / 0.08) * 100, color=c, lw=2.2, label=f"{name} (μ = {mu})")
for x, name in ((0.03, "after FR"), (0.85, "after R"), (0.15, "under canopy")):
    b.axvline(x, color="0.6", lw=0.8, ls=":")
    b.text(x + 0.01, 104, name, fontsize=8, color="0.4", rotation=0)
b.set_xlabel("Phytochrome photoequilibrium Pfr/Ptot")
b.set_ylabel("Germination / %")
b.set_xlim(0, 0.9)
b.set_ylim(0, 112)
b.legend(frameon=False, fontsize=8.5, loc="lower right")
b.set_title("B   Threshold model", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
