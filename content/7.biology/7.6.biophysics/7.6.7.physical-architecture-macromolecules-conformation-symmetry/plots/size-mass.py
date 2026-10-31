"""Size against mass for macromolecules and assemblies (Formula 7.6.1).

Line: diameter of a compact sphere of protein density 1.35 g/cm^3, d = 2 (3 M / (4 pi rho N_A))^(1/3).
Points: approximate largest dimensions of real objects (rounded literature values); elongated or
hollow objects lie above the line. Right axis: the corresponding number of amino-acid residues
(110 Da per residue).
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
NA = 6.022e23

DATA = [  # name, mass in Da, largest dimension in nm, kind
    ("lysozyme", 14.3e3, 4.5, "compact"),
    ("myoglobin", 17.8e3, 4.4, "compact"),
    ("hemoglobin", 64.5e3, 6.5, "compact"),
    ("nucleosome core", 2.06e5, 11.0, "compact"),
    ("RNA polymerase II", 5.1e5, 15.0, "compact"),
    ("GroEL-GroES", 8.9e5, 18.5, "hollow"),
    ("70S ribosome", 2.5e6, 21.0, "compact"),
    ("80S ribosome", 4.3e6, 28.0, "compact"),
    ("26S proteasome", 2.5e6, 45.0, "elongated"),
    ("myosin II", 4.8e5, 160.0, "elongated"),
    ("fibrinogen", 3.4e5, 46.0, "elongated"),
    ("TMV", 4.0e7, 300.0, "elongated"),
    ("adenovirus", 1.5e8, 95.0, "hollow"),
    ("nuclear pore complex", 1.1e8, 120.0, "hollow"),
]


def sphere_d(M, rho=1.35):
    V = M / (rho * NA) * 1e21           # nm^3 (1 cm^3 = 1e21 nm^3)
    return 2 * (3 * V / (4 * np.pi)) ** (1 / 3)


fig, ax = bio.canvas(15.0, 9.6)
pax = charts.axes_at(ax, (1.6, 1.3, 12.9, 7.6))
M = np.logspace(3.6, 8.6, 100)
pax.loglog(M, sphere_d(M), color=P.ink(), lw=1.4)
pax.text(2.2e7, sphere_d(2.2e7) * 0.62, "compact sphere\n" + r"$d \propto M^{1/3}$", fontsize=FT["tiny"], color=P.ink())
tok = {"compact": "protein", "hollow": "virus", "elongated": "enzyme"}
for name, m, d, kind in DATA:
    pax.plot(m, d, "o", ms=6, mfc=P.fill(tok[kind]), mec=P.edge(tok[kind]), mew=0.8)
    dx = 1.18
    ha = "left"
    if name in ("fibrinogen", "nuclear pore complex", "adenovirus", "80S ribosome", "lysozyme", "GroEL-GroES"):
        dx, ha = 1 / 1.18, "right"
    pax.text(m * dx, d * (0.93 if name == "70S ribosome" else 1.0), name, fontsize=FT["tiny"], color=P.ink(), va="center", ha=ha)
for kind in ("compact", "hollow", "elongated"):
    pax.plot([], [], "o", ms=6, mfc=P.fill(tok[kind]), mec=P.edge(tok[kind]), label=kind)
pax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
pax.set_xlim(4e3, 4e8)
pax.set_ylim(2, 500)
charts.style_axes(pax, "mass M / Da", "largest dimension / nm", box=True)
top = pax.secondary_xaxis("top", functions=(lambda x: x / 110.0, lambda n: n * 110.0))
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=FT["tiny"])
top.set_xlabel("equivalent number of residues", fontsize=FT["small"], color=P.ink())
for sp in top.spines.values():
    sp.set_color(P.muted())
