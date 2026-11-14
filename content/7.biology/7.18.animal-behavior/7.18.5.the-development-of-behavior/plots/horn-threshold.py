"""A developmental switch: horn length against body size in a dung beetle (simulated, after Onthophagus taurus).

Horn length follows a steep sigmoid in pronotum width with a threshold near 5.2 mm, so a unimodal body-size
distribution yields a bimodal distribution of horn lengths. Simulated data, illustrative parameters.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)
n = 400
x = rng.normal(5.15, 0.42, n)
h = 0.15 + 5.0 / (1 + np.exp(-(x - 5.2) / 0.09)) + rng.normal(0, 0.25, n) * (0.3 + 0.7 / (1 + np.exp(-(x - 5.2) / 0.09)))
h = np.clip(h, 0, None)
fig, ax = bio.canvas(26.0, 10.0)
pa = C.axes_at(ax, (2.4, 1.6, 12.0, 7.2))
minor = h < 2.5
pa.plot(x[minor], h[minor], "o", ms=3.5, color=C.line("dna"), alpha=0.8)
pa.plot(x[~minor], h[~minor], "o", ms=3.5, color=C.line("negative"), alpha=0.8)
xx = np.linspace(3.8, 6.6, 300)
pa.plot(xx, 0.15 + 5.0 / (1 + np.exp(-(xx - 5.2) / 0.09)), color=P.ink(), lw=1.2)
pa.axvline(5.2, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.text(5.25, 0.3, "threshold", color=P.muted(), fontsize=FS["tiny"])
pa.text(4.0, 1.2, "hornless: sneak into tunnels", color=C.line("dna"), fontsize=FS["tiny"])
pa.text(5.35, 6.0, "horned: guard tunnels", color=C.line("negative"), fontsize=FS["tiny"])
pa.set_xlim(3.8, 6.6)
pa.set_ylim(0, 6.8)
C.style_axes(pa, "body size (pronotum width) / mm", "horn length / mm")
bio.panel(ax, "A", (0.4, 9.7))
pb = C.axes_at(ax, (18.0, 1.6, 7.2, 7.2))
pb.hist(h, bins=np.linspace(0, 6.5, 27), orientation="horizontal", color=C.line("neutral"), alpha=0.7, lw=0)
pb.set_ylim(0, 6.8)
C.style_axes(pb, "number of males", "horn length / mm")
bio.panel(ax, "B", (16.4, 9.7))
