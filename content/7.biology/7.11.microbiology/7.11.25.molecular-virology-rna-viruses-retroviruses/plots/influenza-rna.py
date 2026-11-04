# Influenza virus RNA synthesis and reassortment.
# A: one vRNP - a (-) strand segment coated with nucleoprotein, the PB1-PB2-PA polymerase bound to both
#    ends; PB2 binds a host cap, PA cleaves 10-13 nucleotides downstream, PB1 extends the primer into mRNA,
#    which ends by stuttering on the template's U track. Replication is unprimed, passes through a
#    full-length cRNA and needs free nucleoprotein.
# B: coinfection: progeny package segments from either parent - the molecular event behind antigenic shift.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(17, 9.8)


def rnp(x0, x1, y, tok="rna", n=14, label=None):
    """A nucleocapsid: a strand coated with nucleoprotein beads."""
    ax.plot([x0, x1], [y, y], color=P.edge(tok), lw=2.0, solid_capstyle="round", zorder=6)
    for x in np.linspace(x0 + 0.2, x1 - 0.2, n):
        bio.protein(ax, (x, y), 0.26, 0.26, "protein", zorder=8)
    if label:
        bio.label(ax, ((x0 + x1) / 2, y - 0.55), label, size="tiny", color=P.muted())


# --- A  the three kinds of RNA -----------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.6))
bio.label(ax, (5.6, 9.55), "One segment, three RNAs", size="title", bold=True)

y = 7.4
rnp(1.4, 8.6, y)
bio.protein(ax, (1.1, y), 0.95, 0.75, "enzyme", text="P", size="tiny", zorder=11)
bio.label(ax, (1.1, y + 0.72), "PB1·PB2·PA", size="tiny", color=P.edge("enzyme"))
bio.label(ax, (8.95, y), "3′", size="tiny")
bio.label(ax, (5.0, y - 0.55), "(−) strand vRNA in a nucleocapsid", size="tiny", color=P.muted())

# cap snatching into mRNA
MB.backbone(ax, MB.track(np.arange(2.0, 4.4, 0.22), np.full(11, y + 1.15)), "mrna")
bio.molecule(ax, (1.9, y + 1.15), token="metabolite", r=0.15)
bio.label(ax, (4.6, y + 1.15), "host pre-mRNA", size="tiny", color=P.edge("mrna"), ha="left")
bio.arrow(ax, (2.6, y + 0.92), (1.7, y + 0.45), kind="process", color=P.muted(), bend=0.1)
bio.label(ax, (2.9, y + 0.72), "PA cuts 10–13 nt with the cap", size="tiny", color=P.edge("highlight"), ha="left")

ym = 5.6
bio.molecule(ax, (1.4, ym), token="metabolite", r=0.15)
MB.backbone(ax, MB.track(np.arange(1.6, 7.6, 0.22), np.full(28, ym)), "mrna")
bio.label(ax, (7.75, ym), "AAAA", size="tiny", bold=True, ha="left")
bio.label(ax, (4.4, ym - 0.5), "mRNA: capped primer, and a poly(A) tail made by stuttering\non the U track near the 5′ end of the template",
          size="tiny", color=P.muted())

yc = 3.8
rnp(1.4, 8.6, yc, n=14)
bio.label(ax, (5.0, yc + 0.6), "cRNA: a full-length (+) strand, unprimed, also encapsidated", size="tiny", color=P.muted())
bio.arrow(ax, (9.2, y - 0.3), (9.2, yc + 0.3), kind="process", color=P.muted(), bend=-0.25)
bio.label(ax, (9.45, 5.6), "replication\nneeds free\nnucleoprotein", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (1.1, y - 0.5), (1.1, ym + 0.35), kind="process", color=P.muted())
bio.label(ax, (5.6, 2.5), "transcription is nuclear, because the caps come from nascent host transcripts;\nα-amanitin, which stops host RNA polymerase II, therefore stops viral mRNA synthesis",
          size="tiny", color=P.muted())

# --- B  reassortment ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (11.0, 9.6))
bio.label(ax, (14.4, 9.55), "Reassortment", size="title", bold=True)
for cx, tok, name in ((12.4, "virus", "virus 1"), (16.4, "positive", "virus 2")):
    for k in range(8):
        ax.plot([cx - 0.45, cx + 0.45], [8.6 - 0.17 * k, 8.6 - 0.17 * k], color=P.edge(tok), lw=2.0,
                solid_capstyle="round", zorder=8)
    bio.label(ax, (cx, 9.0), name, size="tiny", color=P.edge(tok))
bio.cell(ax, (14.4, 6.0), 1.9, 1.2, kind="animal")
bio.label(ax, (14.4, 4.5), "one cell, both genomes", size="tiny", color=P.muted())
bio.arrow(ax, (12.7, 7.1), (13.8, 6.7), kind="process")
bio.arrow(ax, (16.1, 7.1), (15.0, 6.7), kind="process")
for j, cx in enumerate((12.6, 14.4, 16.2)):
    pat = [(0, 1, 0, 1, 1, 0, 1, 0), (1, 1, 1, 0, 1, 1, 1, 1), (0, 0, 1, 0, 0, 1, 0, 0)][j]
    for k in range(8):
        tok = "positive" if pat[k] else "virus"
        ax.plot([cx - 0.45, cx + 0.45], [3.5 - 0.17 * k, 3.5 - 0.17 * k], color=P.edge(tok), lw=2.0,
                solid_capstyle="round", zorder=8)
bio.arrow(ax, (14.4, 4.2), (14.4, 3.8), kind="process")
bio.label(ax, (14.4, 1.6), "progeny with new combinations of the eight segments:\na haemagglutinin new to the population is antigenic shift",
          size="tiny", color=P.muted())
