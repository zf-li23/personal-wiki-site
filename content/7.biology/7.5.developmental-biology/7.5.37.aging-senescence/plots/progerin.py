"""Processing of prelamin A and the origin of progerin in Hutchinson-Gilford progeria (Example 37.5.1).

Top: normal processing. Prelamin A ends in a CaaX motif (CSIM). (1) Farnesyltransferase (FTase) attaches a
farnesyl lipid to the cysteine; (2) the last three residues (SIM) are removed (ZMPSTE24 or RCE1) and (3) the
farnesylated cysteine is methylated (ICMT); (4) ZMPSTE24 cleaves off the last 15 residues including the
farnesyl group, giving mature, non-farnesylated lamin A, which joins the nuclear lamina. Bottom: the de novo
mutation c.1824C>T (p.G608G) in exon 11 is silent but activates a cryptic splice site, deleting 50 amino acids
that include the second ZMPSTE24 site. Progerin is farnesylated and methylated but cannot be cleaved; it stays
anchored in the inner nuclear membrane, and nuclei become misshapen (blebs). The farnesyltransferase inhibitor
lonafarnib blocks step 1.
"""

from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np
import wikibio as bio

P = bio.P
LW = bio.core.LINE
fig, ax = bio.canvas(32.0, 13.0)


def protein(x0, y, segs, cut=None):
    """segs: list of (length, token, label)."""
    x = x0
    out = {}
    for ln, tok, lab in segs:
        ax.add_patch(FancyBboxPatch((x, y - 0.35), ln, 0.7, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=P.fill(tok), ec=P.edge(tok), lw=LW * 0.8, zorder=6))
        if lab:
            bio.label(ax, (x + ln / 2, y), lab, size="tiny", color=P.on_fill(), zorder=8)
        out[lab] = (x, x + ln)
        x += ln
    return x


def farnesyl(x, y):
    ax.plot([x, x + 0.2, x + 0.4, x + 0.6, x + 0.8], [y + 0.35, y + 0.8, y + 0.55, y + 1.0, y + 0.75],
            color=P.edge("lipid"), lw=2.0, zorder=7)
    bio.label(ax, (x + 1.25, y + 0.95), "farnesyl", size="tiny", color=P.muted())


bio.panel(ax, "A", (0.3, 12.8))
bio.label(ax, (1.5, 12.5), "Normal lamin A", size="small", bold=True, ha="left")
rows = (11.0, 9.0, 7.0)
body = [(6.0, "protein", "rod domain"), (2.4, "enzyme", "tail"), (1.2, "receptor", "15 aa")]
labels = ("prelamin A (...CSIM)", "1 farnesylation, 2 -SIM, 3 methylation", "4 ZMPSTE24 cleavage")
for i, y in enumerate(rows):
    end = protein(1.5, y, body if i < 2 else body[:2])
    if i == 0:
        bio.label(ax, (end + 0.2, y), "CSIM", size="tiny", ha="left", bold=True)
    if i == 1:
        farnesyl(end - 0.3, y)
    if i == 2:
        protein(end + 1.0, y, [(1.2, "receptor", "15 aa")])
        farnesyl(end + 1.9, y)
        bio.label(ax, (end + 1.6, y - 0.75), "released", size="tiny", color=P.muted())
    bio.label(ax, (14.5, y), labels[i], size="tiny", ha="left")
    if i < 2:
        bio.arrow(ax, (5.0, y - 0.5), (5.0, y - 1.5), kind="process")
bio.label(ax, (4.5, 5.8), "mature lamin A joins the nuclear lamina", size="tiny", color=P.muted())

bio.panel(ax, "B", (0.3, 4.9))
bio.label(ax, (1.5, 4.6), "Progerin (HGPS, LMNA c.1824C>T)", size="small", bold=True, ha="left")
end = protein(1.5, 3.0, [(6.0, "protein", "rod domain"), (0.9, "enzyme", ""), (0.6, "negative", "Δ50"),
                         (0.4, "enzyme", "")])
farnesyl(end - 0.3, 3.0)
bio.label(ax, (14.5, 3.0), "farnesylated and methylated; second ZMPSTE24 site deleted:", size="tiny", ha="left")
bio.label(ax, (14.5, 2.3), "never cleaved, stays in the inner nuclear membrane", size="tiny", ha="left")
bio.label(ax, (14.5, 1.3), "lonafarnib (FTase inhibitor) reduces farnesylated progerin", size="tiny", ha="left",
          color=P.edge("positive"))

# nuclei
for cx, bleb, lab in ((28.5, False, "normal nucleus"), (28.5, True, "HGPS nucleus")):
    cy = 9.0 if not bleb else 3.0
    th = np.linspace(0, 2 * np.pi, 200)
    r = 1.6 + (0.25 * np.sin(5 * th) + 0.12 * np.sin(9 * th + 1) if bleb else 0)
    ax.fill(cx + r * np.cos(th), cy + 0.8 * r * np.sin(th), fc=P.fill("nucleus"), ec=P.edge("nucleus"), lw=LW,
            zorder=5)
    ax.plot(cx + (r - 0.12) * np.cos(th), cy + 0.8 * (r - 0.12) * np.sin(th), color=P.edge("protein"), lw=1.6,
            zorder=6)
    bio.label(ax, (cx, cy - 2.0), lab, size="tiny")
bio.label(ax, (28.5, 11.6), "purple rim: lamina", size="tiny", color=P.muted())
