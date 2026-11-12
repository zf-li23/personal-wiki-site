# Erwin's (1982) extrapolation of global arthropod species richness and the propagation of parameter
# uncertainty (Monte Carlo). Chain: beetle species per tree species x fraction host-specific x number of
# tropical tree species / fraction of canopy arthropods that are beetles / fraction of the fauna living in
# the canopy. Erwin's point values give about 30 million. The ranges below are illustrative assumptions
# spanning values discussed by later critics (Stork 1988, Odegaard 2000, Stork 2018), not measurements.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
n = 200000
beetles = rng.uniform(600, 1200, n)          # beetle species per tree species (Erwin: 1200 on Luehea)
spec = rng.uniform(0.02, 0.136, n)           # effective host-specific fraction (Erwin: 163/1200)
trees = rng.uniform(40000, 60000, n)         # tropical tree species (Erwin: 50000)
fbeetle = rng.uniform(0.2, 0.4, n)           # beetles among canopy arthropods (Erwin: 0.4)
fcanopy = rng.uniform(0.33, 0.67, n)         # canopy share of the fauna (Erwin: 2/3)
N = beetles * spec * trees / fbeetle / fcanopy
erwin = 1200 * 163 / 1200 * 50000 / 0.4 / (2 / 3)

fig, ax = bio.canvas(22, 10)
pax = charts.axes_at(ax, (2.0, 1.6, 12.0, 7.6))
bins = np.logspace(5.5, 8.0, 70)
pax.hist(N, bins=bins, color=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.4)
pax.set_xscale("log")
lo, med, hi = np.percentile(N, [5, 50, 95])
ymax = pax.get_ylim()[1]
pax.axvline(erwin, color=charts.line("negative"), lw=1.4)
pax.text(erwin * 1.06, ymax * 0.92, "Erwin 1982\nabout 30 million", fontsize=8, color=P.ink(), va="top")
pax.axvspan(2.6e6, 7.8e6, color=P.fill("positive"), alpha=0.35, lw=0)
pax.text(4.5e6, ymax * 0.98, "Stork 2018:\ninsects 5.5 M\n(2.6-7.8 M)", fontsize=8, color=P.ink(), va="top", ha="center")
for v in (lo, med, hi):
    pax.axvline(v, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
charts.style_axes(pax, "Estimated arthropod species (log scale)", "Simulations")
txt = ("Parameter ranges (uniform)\n"
       "beetle spp. per tree sp.: 600-1200\n"
       "host-specific fraction: 0.02-0.14\n"
       "tropical tree spp.: 40-60 thousand\n"
       "beetles / canopy arthropods: 0.2-0.4\n"
       "canopy share of fauna: 0.33-0.67\n\n"
       "Monte Carlo, n = 200000\n"
       "median %.1f M\n90%% interval %.1f-%.1f M" % (med / 1e6, lo / 1e6, hi / 1e6))
bio.label(ax, (15.2, 8.9), txt, size="small", ha="left", va="top")
