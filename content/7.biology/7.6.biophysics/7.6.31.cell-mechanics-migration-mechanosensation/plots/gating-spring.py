"""The gating-spring model of hair-cell mechanotransduction (Howard and Hudspeth 1988). Each of N
transduction channels is attached to a gating spring; opening a channel shortens its spring by a
gating swing and reduces the bundle force by a gating force z per channel, so that
F(x) = K_inf x - N z p_o(x) + F_0 with p_o(x) = 1 / (1 + exp(-z (x - x_0)/k_B T)). Parameters similar
to bullfrog sacculus bundles: K_inf = 1 pN/nm, z = 0.7 pN, k_B T = 4.1 pN nm. A: open probability
against bundle displacement. B: force-displacement relations for N = 0, 25, 50 and 80 channels: the
channels make the bundle softer near x_0 (gating compliance), and for N z^2/(4 k_B T) > K_inf the
stiffness becomes negative and the relation non-monotonic. C: bundle stiffness dF/dx; the dotted line
marks zero stiffness."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.87)
Kinf, z, kT = 1.0, 0.7, 4.1
x = np.linspace(-60, 60, 600)
po = 1 / (1 + np.exp(-z * x / kT))
ax = axs[0]
ax.plot(x, po, color=charts.line("channel"), lw=1.7)
charts.style_axes(ax, "bundle displacement $x$ / nm", "open probability $p_o$")
charts.title(ax, "A  Channel gating")
toks = {0: "neutral", 25: "dna", 50: "bacterium", 80: "blood"}
for N, tok in toks.items():
    F = Kinf * x - N * z * po + N * z / 2
    K = Kinf - N * z ** 2 / kT * po * (1 - po)
    axs[1].plot(x, F, color=charts.line(tok), lw=1.6, label=f"N = {N}")
    axs[2].plot(x, K, color=charts.line(tok), lw=1.6, label=f"N = {N}")
axs[2].axhline(0, color=P.muted(), lw=0.8, ls=":")
axs[1].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(axs[1], "bundle displacement $x$ / nm", "force / pN")
charts.title(axs[1], "B  Force-displacement")
axs[2].legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[2], "bundle displacement $x$ / nm", "stiffness / pN nm$^{-1}$")
charts.title(axs[2], "C  Negative stiffness")
