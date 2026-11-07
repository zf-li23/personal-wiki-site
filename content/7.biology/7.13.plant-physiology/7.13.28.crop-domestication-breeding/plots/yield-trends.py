# Cereal yields since 1961 (FAOSTAT data as distributed by Our World in Data, file fao-yields.csv;
# rice is paddy rice, yields in tonnes per hectare).
# A: world yields of rice, wheat and maize; the semi-dwarf varieties of the Green Revolution were
#    released from the mid-1960s (IR8 rice 1966; Mexican semi-dwarf wheats in India from 1965).
# B: national examples: wheat in India and Mexico, rice in China (hybrid rice from 1976).
# Dashed lines are straight-line fits over 1961-2024; the slope is the mean absolute gain per year.
import csv

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

rows = list(csv.DictReader(open("fao-yields.csv")))
year = np.array([int(r["year"]) for r in rows])


def col(name):
    return np.array([float(r[name]) for r in rows])


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2))
series_a = [("world_rice", "Rice (paddy)", "highlight"), ("world_wheat", "Wheat", "protein"),
            ("world_maize", "Maize", "plant")]
for key, name, token in series_a:
    y = col(key)
    c = charts.line(token)
    ax.plot(year, y, color=c, lw=2.0, label=name)
    b, a = np.polyfit(year, y, 1)
    ax.plot(year, a + b * year, color=c, lw=0.9, ls="--")
    ax.text(2025, y[-1], f"{1000 * b:.0f} kg/ha per yr", fontsize=7.5, color=c, va="center")
ax.axvspan(1965, 1975, color=bio.P.light("neutral"), zorder=0)
ax.text(1970, 0.15, "semi-dwarf\nvarieties spread", fontsize=7.5, ha="center", va="bottom", color=bio.P.muted())
ax.set_xlim(1960, 2040)
ax.set_ylim(0, 6.3)
ax.set_xticks(range(1960, 2030, 10))
charts.style_axes(ax, "Year", "World yield / (t ha$^{-1}$)")
ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.2, 1.0))

series_b = [("india_wheat", "Wheat, India", "protein"), ("mexico_wheat", "Wheat, Mexico", "enzyme"),
            ("china_rice", "Rice (paddy), China", "highlight")]
for key, name, token in series_b:
    bx.plot(year, col(key), color=charts.line(token), lw=2.0, label=name)
bx.axvline(1966, color=bio.P.muted(), lw=0.8, ls=":")
bx.text(1967, 0.3, "IR8 (1966)", fontsize=7.5, color=bio.P.muted())
bx.axvline(1976, color=bio.P.muted(), lw=0.8, ls=":")
bx.text(1977, 0.75, "hybrid rice\nin China (1976)", fontsize=7.5, color=bio.P.muted())
bx.set_xlim(1960, 2025)
bx.set_ylim(0, 7.6)
charts.style_axes(bx, "Year", "Yield / (t ha$^{-1}$)")
bx.legend(frameon=False, fontsize=8, loc="upper left")

for a, letter in zip((ax, bx), "AB"):
    a.text(-0.12, 1.03, letter, transform=a.transAxes, fontsize=12, weight="bold", color=bio.P.ink())
fig.tight_layout()
