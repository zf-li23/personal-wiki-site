# The size scale of cell biology on one logarithmic axis, from a covalent bond to the largest single cells,
# with the ranges resolved by the naked eye, the light microscope (diffraction-limited and super-resolution)
# and the electron microscope. Sizes are typical linear dimensions (diameter or length).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P

objects = [  # (size in m, label, token)
    (1.5e-10, "C-C bond", "neutral"),
    (1e-9, "glucose", "metabolite"),
    (2e-9, "DNA helix width", "dna"),
    (4e-9, "GFP", "positive"),
    (2.5e-8, "ribosome", "rrna"),
    (3e-8, "poliovirus", "virus"),
    (1.2e-7, "HIV", "virus"),
    (3e-7, "Mycoplasma", "bacterium"),
    (1e-6, "mitochondrion", "mitochondrion"),
    (2e-6, "E. coli", "bacterium"),
    (7.5e-6, "red blood cell", "blood"),
    (1.5e-5, "HeLa cell", "cytoplasm"),
    (1.2e-4, "human oocyte", "animal"),
    (7.5e-4, "Thiomargarita", "bacterium"),
    (1.2e-3, "frog egg", "animal"),
    (1e-1, "squid giant axon (length)", "neuron"),
]

fig, ax = plt.subplots(figsize=(11.5, 4.2))
ax.set_xscale("log")
ax.set_xlim(8e-11, 0.3)
ax.set_ylim(-3.2, 3.6)

bands = [  # (from, to, label, token, row)
    (2e-4, 0.3, "naked eye", "neutral", -1.6),
    (2e-7, 2e-3, "light microscope", "highlight", -2.1),
    (2e-8, 2e-7, "super-resolution", "positive", -2.1),
    (1e-10, 1e-5, "electron microscope", "channel", -2.6),
]
for a, b, txt, tok, y in bands:
    ax.fill_between([a, b], y - 0.2, y + 0.2, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    ax.text(np.sqrt(a * b), y, txt, ha="center", va="center", fontsize=7.5, color=P.on_fill())

ax.axhline(0, color=P.muted(), lw=1.0)
for k, (s, txt, tok) in enumerate(objects):
    up = k % 2 == 0
    y = 0.55 + 1.05 * ((k // 2) % 3) if up else -0.45 - 0.45 * ((k // 2) % 2)
    if not up:
        y = -0.5 if (k // 2) % 2 == 0 else -1.0
    ax.plot([s, s], [0, y - (0.12 if up else -0.12)], color=P.muted(), lw=0.6)
    ax.plot([s], [0], "o", ms=6, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=5)
    ax.text(s, y, txt, ha="center", va="bottom" if up else "top", fontsize=7.5, color=P.ink(),
            style="italic" if txt in ("Mycoplasma", "E. coli", "Thiomargarita") else "normal")

ticks = [1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
names = ["0.1 nm", "1 nm", "10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "1 cm", "10 cm"]
ax.set_xticks(ticks)
ax.set_xticklabels(names)
ax.minorticks_off()
ax.set_yticks([])
charts.style_axes(ax, "linear size (logarithmic scale)")
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_position(("data", -3.1))
fig.tight_layout()
