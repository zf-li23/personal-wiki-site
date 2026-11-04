"""The thermodynamic window of syntrophy: Gibbs energy of the partner reactions as a function of H2 pressure.

Delta G = Delta G'° + RT ln Q at 25 °C, with 1 mM butyrate, propionate and acetate, 50 mM bicarbonate and
0.5 bar CH4 (gases in bar, solutes in mol/L; pH 7 is included in Delta G'°). Reactions and Delta G'° (Thauer
et al. 1977; Schink 1997):
butyrate- + 2 H2O -> 2 acetate- + H+ + 2 H2                   +48.1 kJ
propionate- + 3 H2O -> acetate- + HCO3- + H+ + 3 H2           +76.1 kJ
4 H2 + HCO3- + H+ -> CH4 + 3 H2O                              -135.6 kJ
The methanogenic reaction is scaled to the H2 produced by one butyrate (x 1/2) or one propionate (x 3/4) so
that each pair shares one H2 budget. Shaded: the H2 partial pressures at which both partners gain energy,
about 2e-6 to 2e-3 bar for butyrate and 2e-6 to 1e-4 bar for propionate.
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24.0, 10.4)
RT = 8.314e-3 * 298.15
lp = np.linspace(-7, -1, 601)
p = 10.0 ** lp
but = 48.1 + RT * np.log((1e-3) ** 2 * p ** 2 / 1e-3)
pro = 76.1 + RT * np.log(1e-3 * 0.05 * p ** 3 / 1e-3)
meth = -135.6 + RT * np.log(0.5 / (p ** 4 * 0.05))


def window(a, b):
    ok = (a < 0) & (b < 0)
    return lp[ok].min(), lp[ok].max()


def panel(x0, title, letter, g, m, name, tok):
    bio.panel(ax, letter, (x0 - 1.8, 10.2))
    bio.label(ax, (x0 + 4.6, 9.8), title, size="small", bold=True)
    pl = quant.Plot(ax, (x0, 1.6, 9.4, 7.4), xlim=(-7, -1), ylim=(-80, 80), xlabel="log₁₀ (p(H₂) / bar)",
                    ylabel="ΔG / (kJ per reaction)", xticks=[-7, -6, -5, -4, -3, -2, -1],
                    yticks=[-80, -40, 0, 40, 80], grid=True)
    lo, hi = window(g, m)
    pl.span(lo, hi, "positive", strength=0.2)
    pl.hline(0, token="ink", dashed=False, lw=0.9)
    pl.line(lp, g, tok, lw=1.8)
    pl.line(lp, m, "neutral", lw=1.8)
    pl.text(-6.9, 72, name, size="tiny", token=tok, ha="left")
    pl.text(-6.9, 62, "methanogen (H₂ consumer)", size="tiny", token="neutral", ha="left")
    pl.text((lo + hi) / 2, -72, "window", size="tiny", token="positive")
    return pl


panel(2.2, "Butyrate oxidation + methanogenesis", "A", but, meth / 2, "butyrate → acetate + H₂ (syntroph)", "rna")
panel(14.0, "Propionate oxidation + methanogenesis", "B", pro, meth * 3 / 4, "propionate → acetate + CO₂ + H₂", "protein")
