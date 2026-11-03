"""Schematic history of atmospheric oxygen relative to the present level (log scale; qualitative band after
reviews such as Lyons et al. 2014): Archean trace levels, GOE 2.4-2.3 Ga, low Proterozoic levels,
Neoproterozoic oxygenation, near-modern Phanerozoic."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(22, 9)
pax = charts.axes_at(ax, (2.6, 2.2, 18.6, 6.0))
# (age Ga, log10 lower, log10 upper) as qualitative anchor points
pts = [(4.0, -7, -5), (2.5, -7, -5), (2.4, -5, -2), (2.2, -3, -0.7), (2.0, -3.5, -1), (0.85, -3.5, -1),
       (0.7, -2.5, -0.5), (0.55, -1.3, -0.1), (0.4, -0.6, 0.1), (0.3, -0.3, 0.2), (0.0, -0.05, 0.05)]
a = np.array([p[0] for p in pts]); lo = np.array([p[1] for p in pts]); hi = np.array([p[2] for p in pts])
pax.fill_between(a, lo, hi, color=P.light("dna"), lw=0)
pax.plot(a, (lo + hi) / 2, color=charts.line("dna"), lw=1.2, ls=(0, (3, 2)))
pax.set_xlim(4.0, 0.0); pax.set_ylim(-7.5, 0.8)
pax.set_yticks([-6, -4, -2, 0]); pax.set_yticklabels(["10⁻⁶", "10⁻⁴", "10⁻²", "1"])
charts.style_axes(pax, "billions of years ago (Ga)", "O₂ relative to present (PAL)")
for x, t in ((2.35, "Great Oxidation\nEvent"), (0.65, "Neoproterozoic\noxygenation")):
    pax.annotate(t, (x, -3.0 if x > 1 else -1.5), xytext=(x + (0.45 if x > 1 else 0.6), -5.8 if x > 1 else -4.6),
                 fontsize=FT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pax.text(3.9, 0.3, "schematic: levels before the Phanerozoic uncertain by orders of magnitude", fontsize=FT["tiny"],
         color=P.muted(), va="center")
for x, t in ((3.45, "stromatolites"), (1.65, "eukaryote\nfossils"), (0.57, "Ediacaran"), (0.53, "")):
    if t:
        pax.text(x, -7.3, t, fontsize=FT["tiny"], color=P.muted(), ha="center", va="bottom")
