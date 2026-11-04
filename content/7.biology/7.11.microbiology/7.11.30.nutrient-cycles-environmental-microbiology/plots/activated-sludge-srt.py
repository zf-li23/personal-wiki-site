"""Activated sludge as a chemostat with biomass recycle: the solids retention time (sludge age) decides
which organisms can stay in the plant.

A: schematic. Wastewater (flow Q, substrate S0) enters an aerated tank of volume V; the mixed liquor flows to
a clarifier, where flocs settle; most of the settled sludge is returned, a small waste stream removes
biomass. The hydraulic retention time is V/Q (hours); the solids retention time (SRT) is the biomass in
the system divided by the biomass removed per day (days), set by the waste flow.
B: steady-state effluent concentration of a substrate against SRT, S = Ks (1 + b SRT) / (SRT (mu_max - b) - 1)
(Monod growth with decay b; the net growth rate must equal 1/SRT). Heterotrophs on biodegradable organic
matter (BOD): mu_max = 6 d-1, Ks = 20 mg L-1, b = 0.12 d-1; ammonia-oxidizing bacteria on ammonium:
mu_max = 0.9 d-1, Ks = 0.5 mg N L-1, b = 0.17 d-1 (typical design values at 20 degrees C; temperature
corrections mu_max x 1.07^(T-20), b x 1.04^(T-20)). Influent 200 mg BOD L-1 and 35 mg NH4-N L-1. Below the
washout SRT the organisms are lost (effluent = influent, dotted). Heterotrophs wash out only below a fraction of a day;
nitrifiers wash out at about 1.4 d at 20 degrees C and 3 d at 10 degrees C, and their effluent ammonium
falls to low values only at several times that SRT, which is why nitrifying plants run at long sludge ages.
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27.0, 11.0)

# A: schematic --------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 10.8))
bio.box(ax, (3.4, 6.4), 4.0, 3.0, token="extracellular", radius=0.1)
bio.label(ax, (3.4, 7.5), "aeration tank", size="small", bold=True)
bio.label(ax, (3.4, 6.7), "volume V\nflocs + air", size="tiny")
for k in range(9):
    x = 1.9 + 0.38 * k
    ax.plot([x], [5.4 + 0.25 * (k % 3)], "o", ms=3, mfc="none", mec=P.edge("dna"), zorder=12)
ax.fill([6.4, 9.0, 8.2, 7.2], [7.9, 7.9, 4.9, 4.9], color=P.fill("extracellular"), ec=P.ink(), lw=1.0, zorder=5)
bio.label(ax, (7.7, 7.3), "clarifier", size="small", bold=True)
bio.arrow(ax, (0.2, 7.2), (1.3, 7.2), kind="process")
bio.label(ax, (0.2, 7.6), "Q, S₀", size="tiny", ha="left")
bio.arrow(ax, (5.5, 7.2), (6.6, 7.2), kind="process")
bio.arrow(ax, (9.0, 7.6), (10.4, 7.6), kind="process")
bio.label(ax, (9.6, 8.0), "effluent S", size="tiny")
bio.arrow(ax, (7.7, 4.8), (7.7, 3.6), kind="process", color=P.edge("bacterium"))
bio.arrow(ax, (7.5, 3.4), (3.4, 3.4), kind="process", color=P.edge("bacterium"))
bio.arrow(ax, (3.4, 3.4), (3.4, 4.8), kind="process", color=P.edge("bacterium"))
bio.label(ax, (5.5, 3.0), "return sludge", size="tiny", color=P.edge("bacterium"))
bio.arrow(ax, (7.9, 3.4), (10.2, 3.4), kind="process", color=P.edge("negative"))
bio.label(ax, (9.0, 3.0), "waste sludge", size="tiny", color=P.edge("negative"))
bio.label(ax, (0.3, 1.6), "HRT = V/Q  (hours)", size="small", ha="left")
bio.label(ax, (0.3, 0.9), "SRT = biomass in system / biomass wasted per day  (days)", size="tiny", ha="left")

# B, C: effluent vs SRT -------------------------------------------------------------------------------
def effluent(srt, mu, Ks, b, S0):
    den = srt * (mu - b) - 1
    S = np.where(den > 0, Ks * (1 + b * srt) / np.where(den > 0, den, 1), np.inf)
    return np.minimum(S, S0)


srt = np.logspace(-1, np.log10(40), 600)
cases = [("B", "heterotrophs: BOD", 6.0, 20.0, 0.12, 200.0, (1e-1, 300), "BOD / (mg L⁻¹)"),
         ("C", "nitrifiers: NH₄⁺-N", 0.9, 0.5, 0.17, 35.0, (1e-1, 60), "NH₄⁺-N / (mg L⁻¹)")]
for k, (lt, title, mu, Ks, b, S0, ylim, ylab) in enumerate(cases):
    x0 = 13.0 + k * 7.2
    bio.panel(ax, lt, (x0 - 1.6, 10.8))
    pl = quant.Plot(ax, (x0, 1.6, 5.2, 7.6), xlim=(0.1, 40), ylim=ylim, xlog=True, ylog=True,
                    xlabel="SRT / d", ylabel=ylab, xticks=[(0.1, "0.1"), (1, "1"), (10, "10")],
                    yticks=[(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100")] if ylim[1] > 100 else
                    [(0.1, "0.1"), (1, "1"), (10, "10")], grid=True)
    for T, tok, dash, fy in [(20, "dna", False, 1.6), (10, "receptor", True, 6.0)]:
        m = mu * 1.07 ** (T - 20)
        bb = b * 1.04 ** (T - 20)
        S = effluent(srt, m, Ks, bb, S0)
        pl.line(srt, S, tok, lw=1.9, dashed=dash)
        smin = 1 / (m * S0 / (Ks + S0) - bb)
        pl.vline(smin, token=tok, dashed=True, lw=0.7)
        pl.text(smin * 1.08, ylim[0] * fy, f"washout\n{smin:.1f} d", ha="left", va="bottom", token=tok)
    pl.hline(S0, token="muted", dashed=True, lw=0.7)
    pl.text(0.12, S0 * 1.15, "influent", ha="left", va="bottom", color=P.muted())
    bio.label(ax, (x0 + 2.6, 9.7), title, size="small", bold=True)
    if k == 1:
        pl.legend([("20 °C", "dna", "-"), ("10 °C", "receptor", "--")], at=(x0 + 3.2, 7.9))
