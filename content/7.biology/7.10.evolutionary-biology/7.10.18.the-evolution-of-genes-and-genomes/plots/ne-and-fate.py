"""Relative substitution rate k/mu = 4 Ne s / (1 - exp(-4 Ne s)) of weakly selected mutations against the
effective population size, for s = -1e-4, -1e-5, -1e-6 and +1e-5, with bands for typical Ne of large
vertebrates, invertebrates and plants, and free-living bacteria."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(14, 9)
pax = charts.axes_at(ax, (2.0, 1.6, 11.2, 6.8))
Ne = np.logspace(2, 9, 400)


def rel(s):
    x = 4 * Ne * s
    out = np.where(np.abs(x) < 1e-8, 1.0, x / -np.expm1(-np.clip(x, -700, 700)))
    return out


for s, tok, ls in ((1e-5, "positive", "-"), (-1e-6, "rna", "-"), (-1e-5, "negative", "-"), (-1e-4, "protein", "-")):
    lab = f"s = {'+' if s > 0 else '−'}10$^{{{int(np.log10(abs(s)))}}}$"
    pax.plot(Ne, rel(s), color=charts.line(tok), lw=1.8, ls=ls, label=lab)
pax.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pax.text(1.5e2, 1.15, "neutral", fontsize=FT["tiny"], color=P.muted())
for lo, hi, txt, tok in ((1e4, 1e5, "large\nvertebrates", "dna"), (1e5, 1e7, "invertebrates,\nplants", "positive"),
                         (1e8, 1e9, "free-living\nbacteria", "rna")):
    pax.axvspan(lo, hi, color=P.light(tok), zorder=0)
    pax.text(np.sqrt(lo * hi), 3e-6, txt, fontsize=FT["tiny"], color=P.ink(), ha="center", va="bottom")
pax.set_xscale("log")
pax.set_yscale("log")
pax.set_ylim(1e-6, 1e4)
pax.set_xlim(1e2, 1e9)
charts.style_axes(pax, r"effective population size $N_{\mathrm{e}}$", r"substitution rate relative to neutral, $k/\mu$")
pax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
