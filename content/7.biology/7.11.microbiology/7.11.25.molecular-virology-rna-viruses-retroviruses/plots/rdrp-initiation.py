# Four ways an RNA-dependent RNA polymerase starts a chain.
# A de novo (a loop of the thumb domain holds the first nucleotide); B prime and realign (initiation at an
# internal residue, then slippage, leaving an unpaired 5' end); C protein priming (VPg-pUpU, picornaviruses);
# D cap snatching (a capped fragment cut from a host pre-mRNA, influenza virus and bunyaviruses).
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(17, 10.6)


def template(y, x0, x1, seq, tok="rna"):
    xs = np.arange(x0, x1, 0.22)
    pts = MB.track(xs, np.full_like(xs, y))
    MB.backbone(ax, pts, tok)
    MB.stubs(ax, pts, (0, 1), MB.sequence(len(xs), seq, "ACGU"), length=0.14)
    bio.label(ax, (x0 - 0.3, y), "3′", size="tiny")
    bio.label(ax, (x1 + 0.15, y), "5′", size="tiny")
    return pts


def product(x0, x1, y, tok="negative"):
    xs = np.arange(x0, x1, 0.22)
    MB.backbone(ax, MB.track(xs, np.full_like(xs, y)), tok)


def title(xy, text):
    bio.label(ax, xy, text, size="title", bold=True)


def note(xy, text):
    bio.label(ax, xy, text, size="tiny", color=P.muted())


# --- A  de novo -------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.4))
title((4.0, 10.2), "De novo initiation")
y = 8.4
MB.polymerase(ax, (3.8, 8.7), 5.6, 2.0, "enzyme", "RdRp", alpha=0.75, text_at=(1.6, 9.25))
template(y, 1.0, 6.6, "template")
product(6.0, 6.7, y + 0.5)
bio.protein(ax, (5.6, y + 0.95), 1.0, 0.4, "positive", text="priming loop", size="tiny")
note((3.6, 7.3), "the first two nucleotides are joined on a protein platform,\nwhich swings aside once the product can leave")
note((4.0, 6.6), "hepatitis C virus, reoviruses, bacteriophage φ6")

# --- B  prime and realign ----------------------------------------------------------------------------------
bio.panel(ax, "B", (8.6, 10.4))
title((13.0, 10.2), "Prime and realign")
y = 8.4
template(y, 9.6, 15.0, "realign")
product(13.2, 14.2, y + 0.5)
bio.arrow(ax, (13.4, y + 1.0), (14.7, y + 1.0), kind="process", color=P.muted())
bio.label(ax, (14.05, y + 1.35), "slip back", size="tiny", color=P.muted())
ax.plot([14.8, 15.3], [y + 0.5, y + 0.5], color=P.edge("negative"), lw=2.4, zorder=9)
bio.label(ax, (15.5, y + 0.5), "unpaired 5′ G", size="tiny", ha="left")
note((12.8, 7.3), "initiation at an internal residue, then slippage of the\nnascent strand: the 5′ end is left unpaired")
note((13.0, 6.6), "bunyaviruses, arenaviruses")

# --- C  protein priming -------------------------------------------------------------------------------------
bio.panel(ax, "C", (0.1, 5.9))
title((4.0, 5.7), "Protein priming (VPg)")
y = 4.0
template(y, 1.0, 6.2, "vpg")
bio.protein(ax, (1.2, y + 0.95), 0.62, 0.42, "enzyme", text="VPg", size="tiny")
ax.plot([1.5, 1.95], [y + 0.5, y + 0.5], color=P.edge("negative"), lw=2.6, zorder=9)
bio.label(ax, (2.45, y + 0.95), "pUpU", size="tiny", color=P.edge("negative"))
bio.arrow(ax, (2.1, y + 0.5), (3.4, y + 0.5), kind="process", color=P.edge("negative"))
note((4.0, 3.0), "uridylylated on a tyrosine by the polymerase, templated by the poly(A) tail or by the\ncre hairpin; the protein stays on the 5′ end of every new genome")
note((4.0, 2.2), "picornaviruses, caliciviruses; also adenovirus and hepatitis B virus DNA")

# --- D  cap snatching ------------------------------------------------------------------------------------------
bio.panel(ax, "D", (8.6, 5.9))
title((13.0, 5.7), "Cap snatching")
y = 4.0
template(y, 9.6, 15.0, "snatch")
MB.backbone(ax, MB.track(np.arange(9.8, 12.6, 0.22), np.full(13, y + 1.2)), "mrna")
bio.molecule(ax, (9.7, y + 1.2), token="metabolite", r=0.16)
bio.label(ax, (9.7, y + 1.55), "cap", size="tiny")
bio.label(ax, (12.75, y + 1.2), "host pre-mRNA", size="tiny", color=P.edge("mrna"), ha="left")
ax.plot([11.1, 11.1], [y + 0.95, y + 1.45], color=P.edge("highlight"), lw=2.2, zorder=12)
bio.label(ax, (10.6, y + 0.7), "endonuclease (PA)", size="tiny", color=P.edge("highlight"))
bio.arrow(ax, (11.4, y + 1.05), (12.9, y + 0.65), kind="process", color=P.muted(), bend=-0.15)
MB.backbone(ax, MB.track(np.arange(13.0, 14.0, 0.22), np.full(5, y + 0.5)), "mrna")
bio.molecule(ax, (12.9, y + 0.5), token="metabolite", r=0.15)
product(14.0, 15.0, y + 0.5)
note((12.9, 3.0), "10–13 nucleotides with their cap prime viral mRNA synthesis")
note((13.0, 2.2), "influenza virus (in the nucleus), bunyaviruses (in the cytoplasm)")

bio.label(ax, (8.5, 1.4), "None of these polymerases proofreads: error rates are $10^{-3}$ to $10^{-5}$ per nucleotide",
          size="small", color=P.muted())
