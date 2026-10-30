"""Model of nephron number (tips times induction rate) and single-nephron GFR versus nephron number."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
w = np.linspace(5, 40, 600)


def tips(w, scale=1.0, after=None):
    T = 3500 / (1 + np.exp(-(w - 20) / 3.0))
    if after is not None:
        T = np.where(w > after, T * (1 - 0.3 * scale * np.clip((w - after) / 4, 0, 1)), T)
    return T


rho = None
base = tips(w)
mask = (w >= 9) & (w <= 36)
rho = 900000 / np.trapezoid(base * mask, w)
fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.33)
a = axs[0]
cases = (("normal", base, 36, "positive", "-"), ("growth restriction", tips(w, 1.0, 20), 36, "drug", "-"),
         ("preterm, stops at 30 wk", base, 30, "dna", "-"))
for lab, T, end, tok, ls in cases:
    m = (w >= 9) & (w <= end)
    N = np.cumsum(rho * T * m) * (w[1] - w[0])
    a.plot(w, N / 1e3, color=charts.line(tok), lw=1.7, ls=ls, label="%s (%.0fk)" % (lab, N[-1] / 1e3))
a2 = a.twinx()
a2.plot(w, base, color=P_.muted(), lw=1.0, ls="--")
a2.set_ylabel("ureteric tips (dashed)", fontsize=FT["small"], color=P_.ink())
a2.tick_params(colors=P_.ink(), labelsize=FT["tiny"])
for sp in ("top", "left", "bottom"):
    a2.spines[sp].set_visible(False)
a2.spines["right"].set_color(P_.muted())
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(a, "gestational age (weeks)", "nephrons per kidney (thousands)")
charts.title(a, "A  Nephrogenesis")
b = axs[1]
N = np.linspace(1e5, 3e6, 300)
b.plot(N / 1e3, 120 / (2 * N) * 1e6, color=charts.line("drug"), lw=1.7)
b.axvspan(210, 2700, color=P_.light("neutral"), lw=0)
b.set_ylim(0, 400)
charts.style_axes(b, "nephrons per kidney (thousands)", "SNGFR (nL/min)")
charts.title(b, "B  Single-nephron filtration")
