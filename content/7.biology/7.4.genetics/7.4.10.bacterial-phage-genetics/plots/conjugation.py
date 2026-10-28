# F+ x F- and Hfr x F- conjugation (schematic)
import numpy as np
import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(24, 10.5)


def ring(c, r, tok, lw=2.2):
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(c[0] + r * np.cos(t), c[1] + r * np.sin(t), color=P.edge(tok), lw=lw, zorder=12)


def pair(y, label_l, label_r, hfr):
    M.bacillus(ax, (4.0, y), 5.2, 2.6, token="bacterium", zorder=5)
    M.bacillus(ax, (11.0, y), 5.2, 2.6, token="bacterium", zorder=5)
    ax.plot([6.6, 8.4], [y + 0.15, y + 0.15], color=P.edge("bacterium"), lw=5, zorder=4)  # mating bridge (pilus)
    ring((3.6, y), 0.95, "dna")
    ring((11.0, y), 0.95, "receptor")
    bio.label(ax, (4.0, y - 1.7), label_l, size="small")
    bio.label(ax, (11.0, y - 1.7), label_r, size="small")
    if hfr:
        t = np.linspace(-0.2, 0.25, 30)
        ax.plot(3.6 + 0.95 * np.cos(t), y + 0.95 * np.sin(t), color=P.edge("highlight"), lw=4, zorder=13)
        xs = np.linspace(4.6, 9.9, 40)
        ax.plot(xs, y + 0.15 + 0.05 * np.sin(xs * 6), color=P.edge("dna"), lw=1.6, zorder=14)
        ax.plot(xs[-6:], y + 0.15 + 0.05 * np.sin(xs[-6:] * 6), color=P.edge("highlight"), lw=2.2, zorder=15)
        bio.label(ax, (7.5, y + 0.6), "chromosome strand,\nstarting inside F", size="tiny")
    else:
        ring((5.3, y + 0.6), 0.35, "highlight", lw=2.4)
        bio.label(ax, (5.3, y + 1.15), "F", size="tiny", bold=True)
        xs = np.linspace(5.65, 9.6, 30)
        ax.plot(xs, y + 0.15 + 0.05 * np.sin(xs * 6), color=P.edge("highlight"), lw=1.6, zorder=14)
        ring((10.0, y + 0.6), 0.3, "highlight", lw=1.4)
        bio.label(ax, (7.5, y + 0.6), "single strand of F", size="tiny")


bio.panel(ax, "A", (0.2, 10.3))
pair(7.6, "F+ donor", "F- recipient", False)
bio.arrow(ax, (14.2, 7.6), (15.4, 7.6))
bio.label(ax, (19.6, 7.6), "both cells F+\n(F spreads; chromosomal\ngenes rarely transferred)", size="small")

bio.panel(ax, "B", (0.2, 4.9))
pair(2.6, "Hfr donor (F integrated)", "F- recipient", True)
bio.arrow(ax, (14.2, 2.6), (15.4, 2.6))
bio.label(ax, (19.6, 2.6), "linear donor fragment, genes in a\nfixed order; recombination by two\ncrossovers; recipient stays F-", size="small")
