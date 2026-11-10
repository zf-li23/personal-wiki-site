# Herd-immunity threshold with an imperfect vaccine. If a fraction p of the population is vaccinated with a vaccine that
# protects a fraction E of the recipients (efficacy against infection), the effective reproduction number is
#   R = R0 (1 - E p),
# so transmission cannot be sustained (R < 1) when the coverage exceeds
#   p_c = (1 - 1/R0) / E,
# which is only attainable (p_c <= 1) if E > 1 - 1/R0. Typical R0 ranges are rough literature values.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
r0 = np.linspace(1.0, 20.0, 400)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
ax = axs[0]
for e, tok in ((1.0, "neutral"), (0.95, "protein"), (0.85, "receptor"), (0.70, "negative")):
    pc = (1 - 1 / r0) / e
    ok = pc <= 1
    ax.plot(r0[ok], pc[ok] * 100, color=charts.line(tok), lw=1.6, label=f"efficacy E = {int(round(e * 100))}%")
    if (~ok).any():
        ax.plot([r0[ok][-1]], [pc[ok][-1] * 100], marker="x", color=charts.line(tok), ms=5)
for lo, hi, name in ((1.3, 2.0, "seasonal\ninfluenza"), (5, 7, "polio"), (12, 18, "measles")):
    ax.axvspan(lo, hi, color=P.muted(), alpha=0.15, lw=0)
    ax.text((lo + hi) / 2 + (0.7 if lo < 2 else 0), 8, name, fontsize=7, color=P.muted(), ha="center")
ax.set_xlim(1, 20)
ax.set_ylim(0, 105)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower right", bbox_to_anchor=(1.0, 0.12))
charts.style_axes(ax, "basic reproduction number $R_0$", "coverage needed, $p_c$ (%)")
charts.title(ax, "A")

ax = axs[1]
p = np.linspace(0, 1, 200)
R0 = 15.0
for e, tok, lab in ((1.0, "neutral", "E = 100%"), (0.97, "protein", "E = 97%"), (0.90, "negative", "E = 90%")):
    ax.plot(p * 100, R0 * (1 - e * p), color=charts.line(tok), lw=1.6, label=lab)
ax.axhline(1, color=P.muted(), lw=0.9, ls="--")
ax.text(2, 1.5, "R = 1", fontsize=7, color=P.muted())
ax.set_xlim(0, 100)
ax.set_ylim(0, 16)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "vaccination coverage $p$ (%)", "effective reproduction number $R$ ($R_0 = 15$)")
charts.title(ax, "B")
fig.tight_layout()
