# The four classes of myriapods compared. Chilopoda (centipedes): one pair of legs per trunk segment, the
# first trunk limbs modified into venom claws (forcipules); fast predators. Diplopoda (millipedes): most
# trunk rings are diplosegments with two pairs of legs; mostly detritivores, many with a calcified cuticle
# and defensive glands. Symphyla: small, pale, 12 pairs of legs, spinnerets on the penultimate segment.
# Pauropoda: minute, 9 (8-11) pairs of legs, branched antennae. Chilopoda are the sister group of the
# other three (Progoneata, with the gonopores near the front of the trunk). Drawings: schematic dorsal views
# (not to scale; segment and leg numbers reduced in centipedes and millipedes).
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(26, 12.2)
from matplotlib.patches import FancyBboxPatch, Ellipse
import numpy as np


def myriapod(x, y, n, legs, seg_w, h, antenna="simple", forcipules=False, spinnerets=False, collum=False):
    """Schematic dorsal view, head to the left: head, n trunk tergites, legs per tergite."""
    L = n * seg_w
    x0 = x - L / 2
    ax.add_patch(Ellipse((x0 - 0.22, y), 0.5, h * 0.9, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=6))
    for s in (1, -1):  # antennae
        a = np.array([x0 - 0.4, y + s * 0.12])
        b = a + np.array([-0.9, s * 0.55])
        ax.plot([a[0], b[0]], [a[1], b[1]], color=P.edge("animal"), lw=1.0, zorder=5)
        if antenna == "branched":
            for k in (0.6, 0.85):
                m = a + (b - a) * k
                ax.plot([m[0], m[0] - 0.35], [m[1], m[1] + s * 0.05], color=P.edge("animal"), lw=0.8, zorder=5)
        if forcipules:
            c = np.array([x0 + 0.05, y + s * h * 0.35])
            ax.plot([c[0], c[0] - 0.35, c[0] - 0.55], [c[1], c[1] + s * 0.25, c[1] + s * 0.05], color=P.edge("drug"), lw=2.0, zorder=7)
    for i in range(n):
        xi = x0 + i * seg_w
        tok = "neutral" if (collum and i == 0) else "animal"
        ax.add_patch(FancyBboxPatch((xi + 0.02, y - h / 2), seg_w - 0.04, h, boxstyle="round,pad=0,rounding_size=0.08",
                                    facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=6))
        k = legs[i] if isinstance(legs, list) else legs
        for j in range(k):
            xl = xi + seg_w * (j + 1) / (k + 1)
            for s in (1, -1):
                ax.plot([xl, xl + 0.12, xl + 0.2], [y + s * h / 2, y + s * (h / 2 + 0.3), y + s * (h / 2 + 0.5)],
                        color=P.edge("animal"), lw=0.9, zorder=5)
    if spinnerets:
        for s in (1, -1):
            ax.plot([x0 + L, x0 + L + 0.35], [y + s * 0.08, y + s * 0.25], color=P.edge("protein"), lw=2.0, zorder=5)


cols = [("Chilopoda", "centipedes"), ("Diplopoda", "millipedes"), ("Symphyla", "symphylans"), ("Pauropoda", "pauropods")]
X = [4.0, 10.3, 16.6, 22.9]
for (t, sub), x in zip(cols, X):
    bio.label(ax, (x, 11.7), t, size="title", bold=True)
    bio.label(ax, (x, 11.2), sub, size="small", color=P.muted())
myriapod(X[0] + 0.4, 9.4, 15, 1, 0.3, 0.42, forcipules=True)
myriapod(X[1] + 0.4, 9.4, 14, [0, 1, 1, 1] + [2] * 10, 0.3, 0.5, collum=True)
myriapod(X[2] + 0.3, 9.4, 13, [1] * 12 + [0], 0.28, 0.34, spinnerets=True)
myriapod(X[3] + 0.3, 9.4, 6, [1, 2, 2, 2, 2, 0], 0.5, 0.5, antenna="branched")
bio.label(ax, (X[0], 8.3), "venom claws on trunk segment 1", size="tiny", color=P.muted())
bio.label(ax, (X[1], 8.3), "collum legless; diplosegments", size="tiny", color=P.muted())
bio.label(ax, (X[2], 8.3), "spinnerets at the rear", size="tiny", color=P.muted())
bio.label(ax, (X[3], 8.3), "branched antennae; tergites span 2 segments", size="tiny", color=P.muted())
rows = [["", "Chilopoda", "Diplopoda", "Symphyla", "Pauropoda"],
        ["Species", "about 3 300", "about 12 000", "about 200", "about 900"],
        ["Legs", "1 pair per segment; 15 to 191 pairs", "2 pairs per diplosegment; up to 1 306 legs", "12 pairs", "usually 9 pairs"],
        ["First trunk limbs", "venom claws (forcipules)", "legs on rings 2-4 (collum legless)", "legs", "legs"],
        ["Mouthparts", "mandibles, 2 pairs of maxillae", "mandibles, gnathochilarium", "mandibles, maxillae, labium", "mandibles, gnathochilarium"],
        ["Gonopores", "posterior (opisthogoneate)", "trunk ring 3 (progoneate)", "trunk segment 4", "trunk segment 3"],
        ["Feeding", "predators", "mostly detritivores", "roots, detritus", "fungal hyphae"],
        ["Defense", "venom", "calcified rings, coiling, repugnatorial glands", "escape", "escape"]]
AM.table(ax, (0.4, 7.6), col_w=[3.4, 5.6, 6.0, 5.0, 5.0], row_h=[0.7] + [0.85] * 7, cells=rows)
AM.bracket(ax, (X[1] - 2.6, 0.45), (X[3] + 2.6, 0.45), "Progoneata", side=-1, depth=0.2)
