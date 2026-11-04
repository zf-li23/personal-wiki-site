"""Cardinal growth temperatures of hyperthermophilic archaea: the bar spans minimum to maximum, the dot is
the optimum. Data for the Thermoproteota (crenarchaea) from Madigan et al. 2019 (Table 17.5); for
Methanopyrus kandleri strain 116, the maximum of 122 C was measured under high pressure (Takai et al. 2008)
minimum and optimum (84 and 98 C) are those of the type strain (Kurr et al. 1991). The dashed line is the boiling point of water at sea
level."""
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
data = [  # genus, min, opt, max, order (colour)
    ("Sulfolobus", 55, 75, 87, "Sulfolobales"),
    ("Acidianus", 60, 88, 95, "Sulfolobales"),
    ("Thermoproteus", 60, 88, 96, "Thermoproteales"),
    ("Pyrobaculum", 74, 100, 102, "Thermoproteales"),
    ("Desulfurococcus", 70, 85, 95, "Desulfurococcales"),
    ("Ignicoccus", 65, 90, 103, "Desulfurococcales"),
    ("Hyperthermus", 75, 102, 108, "Desulfurococcales"),
    ("Pyrodictium", 82, 105, 110, "Desulfurococcales"),
    ("Pyrolobus", 90, 106, 113, "Desulfurococcales"),
    ("Methanopyrus", 84, 98, 122, "Methanopyri"),
]
tok = {"Sulfolobales": "enzyme", "Thermoproteales": "dna", "Desulfurococcales": "negative", "Methanopyri": "rna"}
fig, ax = plt.subplots(figsize=(8.4, 4.0))
for i, (g, lo, op, hi, order) in enumerate(data):
    y = len(data) - 1 - i
    c = charts.line(tok[order])
    ax.plot([lo, hi], [y, y], color=c, lw=5, solid_capstyle="round", alpha=0.55)
    ax.plot(op, y, "o", ms=6, color=c)
ax.set_yticks(range(len(data)))
ax.set_yticklabels([d[0] for d in data][::-1], fontsize=7.5, style="italic")
ax.axvline(100, color=P.muted(), ls="--", lw=0.9)
ax.set_xlim(50, 126)
for k, (o, t) in enumerate(tok.items()):
    ax.plot([], [], color=charts.line(t), lw=4, label=o)
ax.legend(fontsize=6.8, frameon=False, loc="upper left", bbox_to_anchor=(1.0, 1.0))
charts.style_axes(ax, "temperature / °C")
