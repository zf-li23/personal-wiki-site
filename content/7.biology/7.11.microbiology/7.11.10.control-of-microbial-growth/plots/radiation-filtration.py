# Ionizing radiation and filtration.
# A: survival against dose of ionizing radiation, drawn from the D10 values (dose for a tenfold reduction;
#    data from Madigan et al. 2019): Salmonella enterica 200 Gy, Escherichia coli 300 Gy, Bacillus subtilis
#    600 Gy, Clostridium botulinum (spores) 3300 Gy, Coxsackie virus 4500 Gy. Most curves are drawn as straight
#    lines on the log scale (single-hit kinetics). Deinococcus radiodurans is drawn with the multitarget model
#    S = 1 - (1 - exp(-D/D0))^n, with a terminal D10 of 2200 Gy (the cited value) and a shoulder of about 5 kGy
#    (illustrative) over which survival hardly falls, because damage is repaired.
# B: sizes of microorganisms and viruses against the pores of sterilizing filters (log scale): membrane filters
#    of 0.45 um and 0.2 (0.22) um pores retain bacteria but not viruses, and small or flexible cells
#    (mycoplasmas, about 0.2 to 0.3 um and without a wall, and the thin spirochete Leptospira, about 0.1 um wide) can pass a 0.2 um filter. HEPA filters
#    are tested at about 0.3 um, the particle size that penetrates a fibrous filter most easily.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(13.5, 4.3), gridspec_kw=dict(width_ratios=[1.0, 1.25], wspace=0.3))

ax = axs[0]
dose = np.linspace(0, 15000, 600)
lines = [("Salmonella enterica", 200, "negative"), ("Escherichia coli", 300, "positive"),
         ("Bacillus subtilis", 600, "highlight"), ("Clostridium botulinum spores", 3300, "dna"),
         ("Coxsackie virus", 4500, "virus")]
for name, d10, tok in lines:
    S = 10 ** (-dose / d10)
    ax.plot(dose / 1000, S, color=charts.line(tok), lw=1.9, label=f"{name} ({d10:,} Gy)".replace(",", " "),)
D0 = 2200 / np.log(10)
n = np.exp(5000 / D0)
S = 1 - (1 - np.exp(-dose / D0)) ** n
ax.plot(dose / 1000, S, color=P.ink(), lw=2.2, label="Deinococcus radiodurans (shoulder)")
ax.axhline(0.1, color=P.muted(), lw=0.7, ls=":")
ax.text(14.8, 0.13, "10 % survival", ha="right", fontsize=6.8, color=P.muted())
ax.set_yscale("log")
ax.set_ylim(1e-8, 2)
ax.set_xlim(0, 15)
leg = ax.legend(fontsize=6.6, frameon=False, loc="lower left", bbox_to_anchor=(0.35, 0.0))
for txt in leg.get_texts():
    if not txt.get_text().startswith("Coxsackie"):
        txt.set_fontstyle("italic")
charts.style_axes(ax, "absorbed dose / kGy", "surviving fraction")
charts.title(ax, "A   Radiation survival curves")

ax = axs[1]
items = [("small viruses (e.g. poliovirus)", 0.025, 0.032, "virus"),
         ("large viruses (e.g. poxviruses)", 0.2, 0.36, "virus"),
         ("Leptospira (width)", 0.1, 0.15, "bacterium"),
         ("mycoplasmas (cells about 0.2 to 0.3 µm)", 0.2, 0.3, "bacterium"),
         ("typical bacteria (width to length)", 0.5, 5.0, "bacterium"),
         ("yeast cells", 3.0, 10.0, "plant"),
         ("protozoan cysts and oocysts", 4.0, 15.0, "neutral")]
for k, (name, a, b, tok) in enumerate(items):
    y = len(items) - k
    ax.plot([a, b], [y, y], color=charts.line(tok), lw=6, solid_capstyle="butt")
    ax.text(b * 1.15, y, name, va="center", fontsize=6.8, color=P.ink(),
            style="italic" if name.startswith("Lepto") else "normal")
for x, lab, ls, ha, dy in ((0.2, "0.2 µm membrane ", "-", "right", 1.2), (0.45, " 0.45 µm membrane", "--", "left", 1.2),
                          (0.3, "HEPA test", ":", "center", 0.55)):
    ax.axvline(x, color=P.muted(), lw=0.9, ls=ls, ymax=(len(items) + dy - 0.1 - 0.3) / (len(items) + 1.7))
    ax.text(x, len(items) + dy, lab, ha=ha, va="bottom", fontsize=6.6, color=P.muted())
ax.set_xscale("log")
ax.set_xlim(0.015, 60)
ax.set_ylim(0.3, len(items) + 2.0)
ax.set_yticks([])
charts.style_axes(ax, "size / µm (log scale)", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "B   What a filter retains")
