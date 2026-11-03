"""Cis and trans components of an expression difference (Formula 19.1.1). A: in each parent expression
depends on its own enhancer (cis) and its transcription factors (trans); in the F1 hybrid both alleles share
one trans environment. B: simulated genes, hybrid allelic ratio H against parental ratio P (log2)."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
fig, ax = bio.canvas(24, 9.5)
bio.panel(ax, "A", (0.2, 9.3))
bio.panel(ax, "B", (13.0, 9.3))


def locus(x, y, tok_enh, tok_tf, label, n_tf=2):
    ax.plot([x, x + 3.6], [y, y], color=P.muted(), lw=1.0)
    bio.box(ax, (x + 0.6, y), 0.9, 0.42, tok_enh, radius=0.08, lw=0.7)
    bio.box(ax, (x + 2.5, y), 1.6, 0.48, "protein", radius=0.08, lw=0.7)
    for k in range(n_tf):
        ax.add_patch(bio.core.Circle((x + 0.35 + 0.5 * k, y + 0.55), 0.2, facecolor=P.fill(tok_tf),
                                     edgecolor=P.edge(tok_tf), lw=0.7, zorder=12))
    bio.label(ax, (x + 4.0, y), label, size="tiny", ha="left")


bio.label(ax, (3.2, 8.6), "Parents", size="small", bold=True)
locus(0.8, 7.5, "dna", "positive", "species 1", n_tf=3)
locus(0.8, 6.0, "rna", "highlight", "species 2", n_tf=1)
bio.label(ax, (6.2, 6.75), "P = log2(E1/E2)\n= cis + trans", size="tiny", ha="left", color=P.muted())
bio.label(ax, (3.2, 4.7), "F1 hybrid: one nucleus", size="small", bold=True)
ax.add_patch(bio.core.FancyBboxPatch((0.4, 1.3), 10.4, 3.0, boxstyle="round,pad=0,rounding_size=0.4",
                                     facecolor="none", edgecolor=P.muted(), lw=0.9, ls=(0, (3, 2))))
locus(0.8, 3.4, "dna", "positive", "allele 1")
locus(0.8, 2.1, "rna", "highlight", "allele 2")
bio.label(ax, (6.2, 2.75), "shared trans factors:\nH = log2(A1/A2) = cis", size="tiny", ha="left", color=P.muted())

pax = charts.axes_at(ax, (15.0, 1.6, 7.6, 7.0))
m = 80
cis_only = rng.normal(0, 1.2, m)
trans_only = rng.normal(0, 1.2, m)
both_c, both_t = rng.normal(0, 0.9, m), rng.normal(0, 0.9, m)
noise = lambda k: rng.normal(0, 0.12, k)
pax.plot(cis_only + noise(m), cis_only + noise(m), "o", ms=3.5, color=charts.line("dna"), label="cis only")
pax.plot(trans_only + noise(m), noise(m), "o", ms=3.5, color=charts.line("rna"), label="trans only")
pax.plot(both_c + both_t + noise(m), both_c + noise(m), "o", ms=3.5, color=charts.line("neutral"), label="cis + trans")
lim = 4
pax.plot([-lim, lim], [-lim, lim], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pax.axhline(0, color=P.muted(), lw=0.8)
pax.set_xlim(-lim, lim)
pax.set_ylim(-lim, lim)
charts.style_axes(pax, r"parental ratio $P$ ($\log_2$)", r"hybrid allelic ratio $H$ ($\log_2$)")
pax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
