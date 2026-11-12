"""Schematic of the higher-taxon method of Mora et al. (2011, PLoS Biol. 9: e1001127) for estimating the
total number of species. Panel A: the cumulative number of described taxa of one rank (here families)
against the year of description levels off, and an asymptotic regression gives the number expected
when description is complete. Panel B: the asymptotic totals of phyla, classes, orders, families and
genera fall on a straight line when their logarithm is plotted against rank; extrapolating the line one
step gives the expected number of species. All numbers in both panels are illustrative (schematic);
the published estimate for animals is about 7.8 million species, of which about 12% were described.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22.0, 9.0)

# --- A: accumulation curve with an asymptotic fit (illustrative)
pa = quant.Plot(ax, (1.6, 1.4, 8.0, 6.2), xlim=(1750, 2050), ylim=(0, 1.15), xlabel="year of description",
                ylabel="cumulative families (relative)", xticks=[1750, 1850, 1950, 2050], yticks=[0, 0.5, 1.0])
years = np.arange(1758, 2011, 6)
rng = np.random.default_rng(0)
K, r, t0 = 1.0, 0.017, 1758
fit = lambda t: K * (1 - np.exp(-r * (t - t0)))
obs = np.clip(fit(years) + rng.normal(0, 0.012, years.size), 0, None)
obs = np.maximum.accumulate(obs)
pa.points(years, obs, "dna", r=0.07)
tt = np.linspace(1758, 2050, 200)
pa.line(tt, fit(tt), "negative", dashed=True)
pa.hline(K, dashed=True, text="asymptote", side="left")
bio.panel(ax, "A", (0.6, 8.4))
bio.label(ax, (5.6, 8.4), "Description of one higher rank levels off", size="small", bold=True)

# --- B: log number of taxa against rank, extrapolated to species (illustrative values)
pb = quant.Plot(ax, (13.8, 1.4, 7.6, 6.2), xlim=(0.5, 6.5), ylim=(1, 7.5), xlabel=None,
                ylabel="log$_{10}$ (asymptotic number of taxa)", xticks=[1, 2, 3, 4, 5, 6], yticks=[1, 3, 5, 7])
ranks = np.arange(1, 6)
logn = np.array([1.5, 2.1, 3.0, 3.9, 4.9])
coef = np.polyfit(ranks, logn, 1)
xs = np.linspace(1, 6, 50)
pb.line(xs[xs <= 5], np.polyval(coef, xs[xs <= 5]), "dna")
pb.line(xs[xs >= 5], np.polyval(coef, xs[xs >= 5]), "negative", dashed=True)
pb.points(ranks, logn, "dna", r=0.1)
y6 = np.polyval(coef, 6)
pb.points([6], [y6], "negative", r=0.12, hollow=True)
for k, name in enumerate(["phylum", "class", "order", "family", "genus", "species"]):
    bio.label(ax, (pb.X(k + 1), 0.9), name, size="tiny", rotation=30, va="top")
bio.callout(ax, pb.xy(6, y6), (pb.X(4.0), pb.Y(7.0)), "predicted species", size="tiny")
bio.panel(ax, "B", (11.4, 8.4))
bio.label(ax, (17.0, 8.4), "Totals per rank extrapolated to species", size="small", bold=True)
bio.label(ax, (11.2, 0.3), "schematic: illustrative values", size="tiny", color=P.muted())
