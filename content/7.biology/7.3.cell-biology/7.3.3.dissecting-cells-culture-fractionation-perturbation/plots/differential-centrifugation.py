# Differential centrifugation as a sieve on the sedimentation coefficient.
# A particle starting at the top of the liquid (radius r1) reaches the bottom (r2) after
#     t = ln(r2/r1) / (omega^2 s),
# so a spin at relative centrifugal force RCF = omega^2 r2 / g for a time t pellets everything with
#     s > s_min = ln(r2/r1) / (omega^2 t).
# Rotor geometry r1 = 4 cm, r2 = 8 cm. The four steps of a standard scheme (1000 g 10 min; 20,000 g 20 min;
# 80,000 g 1 h; 150,000 g 3 h) give s_min of roughly 1e5, 2e3, 2e2 and 35 S (dashed lines). Bars:
# order-of-magnitude ranges of s for the components of a liver homogenate. A particle is pelleted in the
# first step whose s_min lies below its range; overlapping ranges are why each pellet is impure.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
g, r1, r2 = 9.81, 0.04, 0.08
steps = [(1000, 600, "1 000 g, 10 min"), (20000, 1200, "20 000 g, 20 min"), (80000, 3600, "80 000 g, 1 h"),
         (150000, 10800, "150 000 g, 3 h")]
parts = [("nuclei", 1e6, 1e7, "nucleus"), ("mitochondria", 1e4, 7e4, "mitochondrion"),
         ("lysosomes, peroxisomes", 4e3, 2e4, "lysosome"), ("microsomes (ER vesicles)", 1e2, 2e4, "er"),
         ("ribosomes, viruses", 80, 1000, "rrna"), ("soluble proteins", 2, 20, "protein")]

fig, ax = plt.subplots(figsize=(9.5, 4.0))
for k, (txt, lo, hi, tok) in enumerate(parts):
    y = len(parts) - k
    ax.barh(y, hi - lo, left=lo, height=0.55, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.9)
    ax.text(lo / 1.25, y, txt, fontsize=7.5, color=P.ink(), ha="right", va="center")
for k, (rcf, t, txt) in enumerate(steps):
    w2 = rcf * g / r2
    smin = np.log(r2 / r1) / (w2 * t) / 1e-13
    ax.axvline(smin, color=P.muted(), lw=1.0, ls="--")
    ax.text(smin * 1.1, 7.0 - 0.0 * k, f"step {k + 1}\n{txt}\ns > {float('%.2g' % smin):,.0f} S", fontsize=6.8, color=P.ink(), va="top")
ax.set_xscale("log")
ax.set_xlim(0.05, 3e7)
ax.set_ylim(0.3, 7.2)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
charts.style_axes(ax, "sedimentation coefficient s / S (1 S = 10⁻¹³ s)")
ax.spines["left"].set_visible(False)
fig.tight_layout()
