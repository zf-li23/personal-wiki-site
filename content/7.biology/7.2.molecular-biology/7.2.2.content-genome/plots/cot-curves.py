# Reassociation (C0t) curves. Denatured DNA fragments re-pair by second-order kinetics: the single-stranded
# fraction of a component is 1 / (1 + k C0 t). The half-time C0t_1/2 of a sequence family is proportional to
# its complexity (the length of distinct sequence), so it scales as G / r for a genome of size G whose family
# is repeated r times. The C0t axis is given in units of the C0t_1/2 of E. coli DNA (4.6 Mb, unique).
# Curves: phage T4 (0.17 Mb), E. coli, and a model mammalian genome of 3 Gb with 10 % highly repetitive DNA
# (about 10^6 copies), 20 % moderately repetitive DNA (about 10^3 copies) and 70 % unique DNA (the mouse
# proportions quoted in the course slides).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
EC = 4.6e6
cot = np.logspace(-5, 5, 600)


def single(components):
    """Single-stranded fraction for components [(fraction, C0t_1/2 in E. coli units)]."""
    return sum(f / (1 + cot / c) for f, c in components)


G = 3e9
mammal = [(0.10, G / EC / 1e6), (0.20, G / EC / 1e3), (0.70, G / EC)]
fig, ax = bio.canvas(16, 8.4)
a = C.axes_at(ax, (1.8, 1.4, 13.4, 6.2))
a.set_xscale("log")
a.plot(cot, single([(1.0, 1.7e5 / EC)]), color=C.line("virus"), lw=1.6, label="Phage T4 (0.17 Mb)")
a.plot(cot, single([(1.0, 1.0)]), color=C.line("bacterium"), lw=1.6, label=r"$\it{E.\ coli}$ (4.6 Mb)")
a.plot(cot, single(mammal), color=C.line("animal"), lw=2.0, label="Mammal (3 Gb), three components")
a.set_xlim(1e-5, 1e5)
a.set_ylim(0, 1.02)
a.set_xticks([1e-4, 1e-2, 1, 1e2, 1e4], ["10⁻⁴", "10⁻²", "1", "10²", "10⁴"])
a.minorticks_off()
a.set_yticks([0, 0.25, 0.5, 0.75, 1])
C.style_axes(a, r"C₀t (in units of C₀t₁/₂ of $\it{E.\ coli}$ DNA)", "Fraction single-stranded")
leg = a.legend(loc="lower left", frameon=False, fontsize=bio.core.FONT["tiny"])
for t in leg.get_texts():
    t.set_color(P.ink())
for x, y, text in ((6.5e-4, 0.95, "highly repetitive\n10 %"), (0.65, 0.82, "moderately\nrepetitive 20 %"),
                   (650, 0.45, "unique\n70 %")):
    a.annotate(text, (x, y), xytext=(0, 14), textcoords="offset points", ha="center", va="bottom",
               fontsize=bio.core.FONT["tiny"], color=P.ink(),
               arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
