# One framework for the transport processes of this course: flux = conductance x driving force
# (= driving force / resistance), the plant analogue of Ohm's law. Each row shows a path from source to sink
# with its driving force and main resistances.
# Water: soil -> roots -> xylem -> leaf -> air; driving force a difference of water potential (liquid) and of
#   water-vapour concentration (gas); resistances of soil, root, xylem, leaf, stomata and boundary layer.
# CO2: air -> stomata -> intercellular spaces -> chloroplast; concentration difference; boundary layer,
#   stomatal and mesophyll resistances.
# Sucrose: source leaf -> sieve tubes -> sink; pressure difference generated osmotically; sieve plates.
# Ions: soil solution -> cytosol; electrochemical potential difference; channels, carriers and pumps.
import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 12.0)


def resistor(x0, x1, y, tok):
    L = x1 - x0
    xs = [x0, x0 + 0.2 * L]
    ys = [y, y]
    for k in range(6):
        xs.append(x0 + 0.2 * L + (k + 0.5) * 0.6 * L / 6)
        ys.append(y + (0.18 if k % 2 == 0 else -0.18))
    xs += [x0 + 0.8 * L, x1]
    ys += [y, y]
    ax.plot(xs, ys, color=P.edge(tok), lw=1.4, zorder=8)


rows = [
    ("Water", "soil", "air", "ΔΨ (liquid), Δc_wv (vapour)", ["root", "xylem", "leaf", "stomata"], "dna", "Ch. 2-3, 10"),
    ("CO₂", "air", "chloroplast", "Δc (CO₂)", ["boundary layer", "stomata", "mesophyll"], "metabolite", "Ch. 9-10"),
    ("Sucrose", "source leaf", "sink", "ΔΨp (osmotically generated)", ["loading", "sieve tubes", "unloading"], "carbohydrate", "Ch. 11"),
    ("Ions", "soil solution", "cytosol", "Δμ̃ (electrochemical)", ["channels, carriers, pumps"], "k", "Ch. 4-5"),
]
bio.label(ax, (13.0, 11.4), "flux = conductance × driving force = driving force / resistance", size="normal", bold=True)
for k, (name, src, snk, force, res, tok, ch) in enumerate(rows):
    y = 9.3 - 2.4 * k
    bio.label(ax, (0.4, y), name, size="normal", bold=True, ha="left")
    bio.box(ax, (4.4, y), 2.8, 1.0, tok, text=src, size="small")
    bio.box(ax, (21.0, y), 2.8, 1.0, tok, text=snk, size="small")
    xs = np.linspace(5.8, 19.6, len(res) + 1)
    for i, r in enumerate(res):
        resistor(xs[i], xs[i + 1], y, tok)
        bio.label(ax, ((xs[i] + xs[i + 1]) / 2, y - 0.55), r, size="tiny", color=P.muted())
    bio.label(ax, (12.7, y + 0.6), force, size="tiny")
    bio.label(ax, (23.0, y), ch, size="tiny", ha="left", color=P.muted())
