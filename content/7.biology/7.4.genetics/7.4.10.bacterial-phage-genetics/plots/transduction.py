# Generalized and specialized transduction (schematic)
import numpy as np
import wikibio as bio
from wikibio import transmission as T

P = bio.P
fig, ax = bio.canvas(26, 11)


def phage(c, tok, label=None, scale=1.0):
    h = 0.55 * scale
    hexa = [(c[0] + h * np.cos(a), c[1] + h * np.sin(a)) for a in np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, 7)[:-1]]
    bio.shape(ax, hexa, token="virus", zorder=6)
    t = np.linspace(0, 2 * np.pi, 50)
    ax.plot(c[0] + 0.25 * scale * np.cos(t), c[1] + 0.22 * scale * np.sin(t), color=P.edge(tok), lw=2.2, zorder=7)
    ax.plot([c[0], c[0]], [c[1] - h, c[1] - h - 0.7 * scale], color=P.edge("virus"), lw=3, zorder=5)
    for dx in (-0.3, 0.3):
        ax.plot([c[0], c[0] + dx * scale], [c[1] - h - 0.7 * scale, c[1] - h - 1.0 * scale], color=P.edge("virus"), lw=1.2)
    if label:
        bio.label(ax, (c[0], c[1] - h - 1.35 * scale), label, size="tiny")


# A generalized
bio.panel(ax, "A", (0.2, 10.8))
bio.label(ax, (6.5, 10.4), "Generalized transduction (P1, P22)", size="normal", bold=True)
T.chromatid_bar(ax, 0.8, 6.2, 8.4, [(0, 0.4, "dna"), (0.4, 0.62, "highlight"), (0.62, 1, "dna")], height=0.3,
                loci=[(0.5, "a+")])
bio.label(ax, (3.5, 7.7), "donor chromosome, fragmented\nduring lytic growth", size="tiny")
phage((7.9, 8.8), "rna", "phage DNA\n(most particles)")
phage((11.2, 8.8), "highlight", "host DNA\n(rare)")
bio.arrow(ax, (11.2, 6.6), (11.2, 5.5))
bio.label(ax, (11.5, 6.1), "infects recipient", size="tiny", ha="left")
T.chromatid_bar(ax, 7.4, 13.0, 4.6, [(0, 0.38, "receptor"), (0.38, 0.6, "highlight"), (0.6, 1, "receptor")], height=0.3,
                loci=[(0.49, "a+")])
for xx in (7.4 + 0.38 * 5.6, 7.4 + 0.6 * 5.6):
    ax.plot([xx - 0.15, xx + 0.15], [4.95, 4.25], color=P.ink(), lw=1.4)
    ax.plot([xx - 0.15, xx + 0.15], [4.25, 4.95], color=P.ink(), lw=1.4)
bio.label(ax, (10.2, 3.8), r"two crossovers: $\it{a}^{-}$ replaced by $\it{a}^{+}$", size="tiny")

# B specialized
bio.panel(ax, "B", (14.2, 10.8))
bio.label(ax, (20.2, 10.4), r"Specialized transduction ($\lambda$)", size="normal", bold=True)
T.chromatid_bar(ax, 14.8, 25.0, 8.4, [(0, 0.3, "dna"), (0.3, 0.42, "highlight"), (0.42, 0.72, "rna"), (0.72, 0.84, "antibody"),
                                       (0.84, 1, "dna")], height=0.3, loci=[(0.36, "gal"), (0.78, "bio")])
bio.label(ax, (14.8 + 0.57 * 10.2, 7.85), "prophage", size="tiny")
bio.arrow(ax, (17.4, 7.4), (17.4, 6.2))
bio.label(ax, (17.8, 6.8), "aberrant excision", size="tiny", ha="left")
T.chromatid_bar(ax, 15.6, 21.4, 5.4, [(0, 0.3, "highlight"), (0.3, 1, "rna")], height=0.3, loci=[(0.15, "gal+")])
bio.label(ax, (18.5, 4.8), r"$\lambda\it{dgal}$: carries $\it{gal}$, lacks some phage genes", size="tiny")
phage((23.6, 5.4), "highlight", "transducing particle")
bio.arrow(ax, (23.6, 3.7), (23.6, 2.6))
T.chromatid_bar(ax, 15.6, 25.0, 1.6, [(0, 0.45, "receptor"), (0.45, 0.62, "highlight"), (0.62, 1, "receptor")], height=0.3,
                loci=[(0.53, "gal+")])
bio.label(ax, (20.3, 0.8), r"$\it{gal}^{-}$ recipient becomes Gal$^{+}$ (often partially diploid for $\it{gal}$)", size="tiny")
