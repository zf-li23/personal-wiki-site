# Holdridge life-zone system on rectangular logarithmic axes.
# Latitudinal regions are bounded by mean annual biotemperature 1.5, 3, 6, 12, 24 C (doubling);
# humidity provinces by the potential evapotranspiration ratio PET/P with PET = 58.93 * Tbio (mm),
# at 0.25, 0.5, ..., 16. Each cell (a parallelogram in log P - log Tbio space) is one life zone;
# precipitation is limited to 62.5-16000 mm as in Holdridge's chart.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import wikibio as bio

P = bio.P
K = 58.93
PMIN, PMAX = 62.5, 16000.0
REGIONS = [  # (lower T, upper T, name, zones from wettest to driest)
    (1.5, 3, "Subpolar", ["rain tundra", "wet tundra", "moist tundra", "dry tundra"]),
    (3, 6, "Boreal", ["rain forest", "wet forest", "moist forest", "dry scrub", "desert"]),
    (6, 12, "Cool temperate", ["rain forest", "wet forest", "moist forest", "steppe", "desert scrub", "desert"]),
    (12, 24, "Warm temperate", ["rain forest", "wet forest", "moist forest", "dry forest", "thorn steppe",
                                "desert scrub", "desert"]),
    (24, 48, "Tropical", ["rain forest", "wet forest", "moist forest", "dry forest", "very dry forest",
                          "thorn woodland", "desert scrub", "desert"]),
]
# humidity provinces by PET ratio interval [r, 2r]
_PROV = [(0.125, "superhumid", "dna"), (0.25, "perhumid", "channel"), (0.5, "humid", "plant"),
        (1, "subhumid", "carbohydrate"), (2, "semiarid", "lipid"), (4, "arid", "antibody"),
        (8, "perarid", "membrane"), (16, "superarid", "rna")]

fig, ax = plt.subplots(figsize=(10.4, 6.2))
lx = np.log2
for t0, t1, rname, zones in REGIONS:
    for j, zone in enumerate(zones):
        r0 = 0.125 * 2 ** j if j else 0.0  # the wettest cell is open towards low PET ratio
        r1 = 0.25 * 2 ** j if j < len(zones) - 1 else np.inf  # the driest cell is open towards high PET ratio
        # corners in (P, T): P = K*T/r
        pts = []
        for T in np.geomspace(t0, t1, 30):
            pts.append((min(PMAX, K * T / r0) if r0 else PMAX, T))
        for T in np.geomspace(t1, t0, 30):
            pts.append((max(PMIN, K * T / r1) if np.isfinite(r1) else PMIN, T))
        pts = [(lx(p), lx(T)) for p, T in pts]
        key = 0.25 * 2 ** j
        prov_tok = {0.25: "channel", 0.5: "plant", 1: "carbohydrate", 2: "lipid", 4: "antibody", 8: "membrane",
                    16: "rna", 32: "rna"}.get(key, "rna")
        ax.add_patch(Polygon(pts, closed=True, facecolor=P.mix(P.surface(), P.fill(prov_tok), 0.5), edgecolor=P.edge("neutral"), lw=0.7))
        # label at geometric centre of the cell, clipped to the precipitation range
        Tc = np.sqrt(t0 * t1)
        rk = 0.25 * 2 ** j
        rc = np.sqrt(rk * (r0 if r0 else rk / 2))
        pc = np.clip(K * Tc / rc, PMIN * 1.15, PMAX / 1.4)
        ax.text(lx(pc), lx(Tc), zone.replace(" ", "\n", 1) if len(zone) > 10 else zone, ha="center",
                va="center", fontsize=6.6, color=P.ink())
    ax.text(lx(PMAX) + 0.15, lx(np.sqrt(t0 * t1)), rname, ha="left", va="center", fontsize=8.5,
            color=P.ink(), weight="bold")
# polar region
pts = [(lx(PMIN), lx(0.75)), (lx(PMAX), lx(0.75)), (lx(PMAX), lx(1.5)), (lx(PMIN), lx(1.5))]
ax.add_patch(Polygon(pts, closed=True, facecolor=P.mix(P.surface(), P.fill("neutral"), 0.5), edgecolor=P.edge("neutral"), lw=0.7))
ax.text(lx(1000), lx(1.06), "polar desert", ha="center", va="center", fontsize=7, color=P.ink())
ax.text(lx(PMAX) + 0.15, lx(1.06), "Polar", ha="left", va="center", fontsize=8.5, color=P.ink(), weight="bold")
# PET-ratio lines labelled inside the tropical row, next to each line
for r in [0.25, 0.5, 1, 2, 4, 8, 16]:
    Tl = 44.0
    p_at = K * Tl / r
    if PMIN <= p_at <= PMAX:
        ax.text(lx(p_at) + 0.06, lx(Tl), f"{r:g}", ha="left", va="center", fontsize=7, color=P.muted())
ax.text(lx(PMIN) + 0.05, lx(0.85), "numbers at the bottom: PET ratio of each diagonal line", ha="left",
        va="center", fontsize=7, color=P.muted())

ticksP = [62.5, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
ax.set_xticks([lx(p) for p in ticksP], [f"{p:g}" for p in ticksP])
ticksT = [0.75, 1.5, 3, 6, 12, 24, 48]
ax.set_yticks([lx(t) for t in ticksT], [f"{t:g}" for t in ticksT])
ax.set_xlim(lx(PMIN), lx(PMAX))
ax.set_ylim(lx(48), lx(0.75))
ax.set_xlabel("Mean annual precipitation / mm (log scale)")
ax.set_ylabel("Mean annual biotemperature / °C (log scale)")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
