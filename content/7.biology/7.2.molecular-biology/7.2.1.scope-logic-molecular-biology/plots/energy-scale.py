# Energies of molecular biology in units of the thermal energy kB T (310 K: 1 kB T = 4.28 pN nm = 2.58 kJ/mol).
# A: typical ranges (order of magnitude): a van der Waals contact, a hydrogen bond or salt bridge in water,
# stacking and pairing of one base pair (nearest-neighbour free energies), unfolding of a small protein,
# ATP hydrolysis under cellular conditions, sequence-specific binding of a transcription factor to its site
# (K_D = 10^-8 to 10^-12 M, relative to the 1 M standard state), a 500-nm photon and a C-C covalent bond.
# B: the Boltzmann factor exp(-E / kB T): the relative probability of a state lying E above another.
import numpy as np
from matplotlib.ticker import NullLocator
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(19, 8.4)
rows = [
    ("van der Waals contact", 0.2, 0.5, "neutral"),
    ("H bond / salt bridge in water", 1, 3, "neutral"),
    ("One base pair (stacking + pairing)", 1, 5, "dna"),
    ("Unfolding a small protein", 5, 25, "protein"),
    ("ATP hydrolysis in the cell", 19, 24, "atp"),
    ("Transcription factor on its site", 18, 28, "receptor"),
    ("Photon, 500 nm", 93, 93, "highlight"),
    ("C–C covalent bond", 136, 136, "negative"),
]
a = C.axes_at(ax, (6.0, 1.4, 5.6, 6.2))
a.set_xscale("log")
n = len(rows)
for k, (name, lo, hi, tok) in enumerate(rows):
    y = n - 1 - k
    if hi > lo:
        a.barh(y, hi - lo, left=lo, height=0.55, color=P.fill(tok), edgecolor=C.line(tok), lw=0.9)
    else:
        a.plot([lo], [y], "D", ms=6, mfc=P.fill(tok), mec=C.line(tok), mew=0.9)
a.axvline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.set_yticks(range(n), [r[0] for r in rows][::-1])
a.set_ylim(-0.6, n - 0.4)
a.set_xlim(0.1, 300)
a.set_xticks([0.1, 1, 10, 100], ["0.1", "1", "10", "100"])
a.minorticks_off()
a.tick_params(axis="y", length=0)
C.style_axes(a, r"$E\,/\,k_{\mathrm{B}}T$", None)
top = a.secondary_xaxis("top", functions=(lambda e: e * 2.58, lambda q: q / 2.58))
top.set_xticks([1, 10, 100], ["1", "10", "100"])
top.xaxis.set_minor_locator(NullLocator())
top.tick_params(colors=P.muted(), labelsize=bio.core.FONT["tiny"])
top.set_xlabel(r"$E$ / (kJ mol$^{-1}$)", color=P.ink(), fontsize=bio.core.FONT["small"])
top.spines["top"].set_color(P.muted())
bio.panel(ax, "A", (0.2, 8.1))

b = C.axes_at(ax, (14.0, 1.4, 4.6, 6.2))
E = np.linspace(0, 30, 300)
b.semilogy(E, np.exp(-E), color=C.line("dna"), lw=1.8)
for e, text in ((1, "0.37"), (5, "0.0067"), (10, r"$4.5\times10^{-5}$"), (20, r"$2.1\times10^{-9}$")):
    b.plot([e], [np.exp(-e)], "o", ms=4.5, mfc=P.fill("dna"), mec=C.line("dna"))
    b.annotate(text, (e, np.exp(-e)), xytext=(6, 4),
               textcoords="offset points", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_xlim(0, 30)
b.set_ylim(1e-13, 2)
b.set_xticks([0, 10, 20, 30])
b.set_yticks([1, 1e-4, 1e-8, 1e-12], ["1", "10⁻⁴", "10⁻⁸", "10⁻¹²"])
b.minorticks_off()
C.style_axes(b, r"$E\,/\,k_{\mathrm{B}}T$", r"$\mathrm{e}^{-E/k_{\mathrm{B}}T}$")
bio.panel(ax, "B", (12.4, 8.1))
