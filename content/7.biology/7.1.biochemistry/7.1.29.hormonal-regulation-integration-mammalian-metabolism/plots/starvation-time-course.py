"""Metabolic adaptation to total fasting.
(A) Plasma fuels during six weeks of starvation in man, drawn as smooth curves through the magnitudes reported
by G. F. Cahill (Annu. Rev. Nutr. 26:1, 2006): glucose falls within two days from about 4.8 to 3.5-4 mM and
then stays constant; fatty acids rise to about 1.5 mM within days; beta-hydroxybutyrate rises from almost
nothing to about 6 mM after two to three weeks, acetoacetate to about 1.5 mM. Schematic, not data.
(B) A reserve-depletion model with the fuel stores of Lehninger Table 23-5 (70 kg man: triacylglycerol 590 MJ,
protein 100 MJ, glycogen 3.8 MJ; 140 kg man: 3100 MJ and 130 MJ). Energy expenditure 7.5 MJ/day (the 1800
kcal/day assumed in that table); glycogen is used first-order with a time constant of half a day; protein
supplies a fraction p(t) = s (0.04 + 0.12 exp(-t/7)) of the energy (mainly as gluconeogenic amino acids),
which falls as ketone bodies replace glucose in the brain; the factor s = sqrt(r/r0), with r the ratio of
protein to fat stores (r0 that of the lean man), expresses that a larger fat store spares protein
(Forbes's rule). Fat supplies the rest. Curves end when triacylglycerol is exhausted."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

fig, ax = bio.canvas(19.0, 7.8)
a = charts.axes_at(ax, (1.6, 1.3, 7.0, 5.8))
t = np.linspace(0, 42, 400)
curves = [("glucose", 4.8 - 1.1 * (1 - np.exp(-t / 1.5)), "carbohydrate"),
          ("fatty acids", 0.5 + 1.0 * (1 - np.exp(-t / 2.0)), "lipid"),
          ("β-hydroxybutyrate", 6.0 * (1 - np.exp(-(t / 7.0) ** 1.6)), "metabolite"),
          ("acetoacetate", 1.4 * (1 - np.exp(-(t / 5.0) ** 1.6)), "receptor")]
for name, y, tok in curves:
    a.plot(t, y, color=charts.line(tok), lw=2.0, label=name)
a.set_xlim(0, 42)
a.set_ylim(0, 8.2)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=bio.P.ink(), loc="upper right", ncol=2)
charts.style_axes(a, "days of fasting", "plasma concentration / mM")
charts.title(a, "A  Plasma fuels (schematic, after Cahill)")


def run(tag0, prot0):
    sc = np.sqrt((prot0 / tag0) / (100.0 / 590.0))

    def f(tt, y):
        tag, prot, gly = y
        e = 7.5
        use_gly = 2.0 * gly
        p = sc * (0.04 + 0.12 * np.exp(-tt / 7.0))
        rest = max(e - use_gly, 0.0)
        return [-(1 - p) * rest, -p * rest, -use_gly]
    def ev(tt, y):
        return y[0]
    ev.terminal = True
    return solve_ivp(f, (0, 600), [tag0, prot0, 3.8], events=ev, max_step=0.5)


b = charts.axes_at(ax, (11.2, 1.3, 7.0, 5.8))
for (tag0, prot0, name, tok) in [(590.0, 100.0, "70 kg", "positive"), (3100.0, 130.0, "140 kg", "negative")]:
    s = run(tag0, prot0)
    d = s.t
    b.plot(d, 100 * s.y[0] / tag0, color=charts.line(tok), lw=2.0, label=f"{name}: fat ({d[-1]:.0f} days)")
    b.plot(d, 100 * s.y[1] / prot0, color=charts.line(tok), lw=1.6, ls="--", label=f"{name}: protein")
b.set_xlim(0, 450)
b.set_ylim(0, 105)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=bio.P.ink(), loc="upper right")
charts.style_axes(b, "days of fasting", "reserve remaining / %")
charts.title(b, "B  Depletion of fuel reserves (model)")
