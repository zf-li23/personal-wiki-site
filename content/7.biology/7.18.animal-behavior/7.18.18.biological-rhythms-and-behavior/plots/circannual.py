"""Model: a circannual rhythm free-running in constant conditions (schematic, after Gwinner and Dittami 1990,
European stonechat). Testis width (blue) and moult (bars) of a male kept for 7.5 years at constant photoperiod
(12L:12D) and temperature: the cycle persists with a period of about 10 months (tau = 0.83 year), so it drifts
earlier in the calendar every year (the months of successive peaks are listed above). A free-living bird (gray) is
entrained to exactly 12 months by the annual change of photoperiod."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 8.6)
yrs = np.linspace(0, 7.5, 2000)
tau = 0.83
p = quant.Plot(ax, (2.2, 2.6, 20.6, 5.2), xlim=(0, 7.5), ylim=(0, 1.3), xlabel="Years in constant conditions",
               ylabel="Testis width", xticks=[0, 1, 2, 3, 4, 5, 6, 7], yticks=None)
free = np.clip(np.sin(2 * np.pi * yrs / tau), 0, None) ** 1.5
nat = np.clip(np.sin(2 * np.pi * yrs / 1.0), 0, None) ** 1.5
p.line(yrs, nat, "neutral", lw=1.2)
p.line(yrs, free, "dna", lw=1.8)
p.legend([("constant conditions (about 10 months)", "dna", "-"), ("free-living (12 months)", "neutral", "-")], at=(15.5, 8.25))
peaks = tau * (np.arange(10) + 0.25)
for k, pk in enumerate(peaks):
    a = pk + tau * 0.32
    b = a + tau * 0.18
    if b < 7.5:
        X0, Y0 = p.xy(a, 1.12)
        X1, _ = p.xy(b, 1.12)
        bio.box(ax, ((X0 + X1) / 2, Y0), X1 - X0, 0.3, "highlight", radius=0.04)
bio.label(ax, (p.X(7.5) + 0.1, p.Y(1.12)), "moult", size="tiny", ha="left")
cal = np.mod(peaks, 1.0)
bio.label(ax, (2.3, 8.25), "month of the testis peak in successive cycles: " +
          ", ".join("JFMAMJJASOND"[int(c * 12)] for c in cal[:9]), size="tiny", ha="left")
ax.set_ylim(1.4, 8.6)
