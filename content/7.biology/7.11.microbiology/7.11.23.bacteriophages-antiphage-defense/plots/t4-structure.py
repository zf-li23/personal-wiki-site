# Bacteriophage T4: the virion and the steps of adsorption and genome injection.
# A: the anatomy of the particle, with callouts.
# B-E: entry into a Gram-negative cell, drawn on cross-sections of the envelope (microbio.envelope):
#   B reversible binding by a long tail fibre; C commitment through the short fibres and the star-shaped
#   baseplate; D contraction of the sheath and local digestion of the peptidoglycan; E ejection of the DNA,
#   the empty capsid remaining outside.
# F: how phages without a contractile tail cross the envelope.
import numpy as np
from matplotlib.patches import Circle, Polygon

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(36, 13.6)
MUT = P.muted()


def t4(x, ybase, s=1.0, contracted=False, empty=False, zorder=14, fibres=True):
    """A T4 particle with the baseplate at (x, ybase); s scales it. Returns the head centre."""
    tok = "neutral" if empty else "virus"
    sheath_len = 1.1 * s if contracted else 2.0 * s
    hy = ybase + sheath_len + 1.5 * s
    pts = np.array([[-0.62, -0.75], [-0.62, 0.55], [0, 1.15], [0.62, 0.55], [0.62, -0.75], [0, -1.25]]) * s + [x, hy]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=zorder))
    # neck and tube
    ax.plot([x, x], [hy - 1.25 * s, ybase], color=P.edge("neutral"), lw=1.6 * s, zorder=zorder - 1)
    nrings = 4 if contracted else 7
    for i in range(nrings):
        yy = ybase + sheath_len - i * sheath_len / nrings
        hgt = sheath_len / nrings * 0.78
        wdt = 0.52 * s if contracted else 0.34 * s
        ax.add_patch(Polygon([[x - wdt, yy], [x + wdt, yy], [x + wdt, yy - hgt], [x - wdt, yy - hgt]], closed=True,
                             facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.5, zorder=zorder))
    bw = 0.75 * s if contracted else 0.55 * s
    ax.add_patch(Polygon([[x - bw, ybase], [x + bw, ybase], [x + bw * 0.7, ybase - 0.26 * s],
                          [x - bw * 0.7, ybase - 0.26 * s]], closed=True, facecolor=P.fill("protein"),
                         edgecolor=P.edge("protein"), lw=0.8, zorder=zorder + 1))
    if fibres:
        for sg in (-1, 1):
            ax.plot([x + sg * bw * 0.8, x + sg * (1.5 * s), x + sg * (1.9 * s)],
                    [ybase - 0.1 * s, ybase + 0.5 * s, ybase - 0.7 * s], color=P.edge("enzyme"), lw=1.0, zorder=zorder - 1)
            ax.plot([x + sg * bw * 0.6, x + sg * (0.9 * s)], [ybase - 0.2 * s, ybase - 0.75 * s],
                    color=P.edge("protein"), lw=1.0, zorder=zorder - 1)
    return (x, hy)


# ---------------------------------------------------------------- A: anatomy
bio.panel(ax, "A", (0.2, 13.3))
bio.label(ax, (0.9, 13.1), "The T4 virion", size="title", bold=True, ha="left")
hx, hy = t4(3.4, 4.6, s=1.5, zorder=14)
bio.callout(ax, (hx + 0.7, hy + 0.4), (0.3, 11.6), "prolate head,\n169 kbp dsDNA")
bio.callout(ax, (hx, hy - 1.5), (6.0, 10.1), "neck and collar")
bio.callout(ax, (3.4 + 0.5, 5.6), (6.3, 7.6), "contractile sheath")
bio.callout(ax, (3.4, 5.2), (0.3, 6.4), "central tube")
bio.callout(ax, (3.4 + 0.7, 4.5), (6.3, 5.2), "baseplate")
bio.callout(ax, (3.4 + 2.6, 3.6), (6.0, 3.0), "long tail fibre\n(receptor binding)")
bio.callout(ax, (3.4 - 1.2, 3.5), (0.3, 2.4), "short tail fibre")

# ---------------------------------------------------------------- B-E: entry
titles = [("B", "Reversible binding"), ("C", "Commitment"), ("D", "Contraction"), ("E", "Ejection")]
x0 = 8.4
for k, (letter, name) in enumerate(titles):
    xa = x0 + k * 5.0
    xb = xa + 4.3
    bio.panel(ax, letter, (xa - 0.1, 13.3))
    bio.label(ax, (xa + 0.55, 13.1), name, size="small", bold=True, ha="left")
    L = M.envelope(ax, xa, xb, 4.2, kind="gram-", top=8.6, seed=4 + k, zorder=4)
    xc = (xa + xb) / 2
    if k == 0:
        t4(xc, L["om_hi"] + 2.3, s=0.85, zorder=14)
        bio.label(ax, (xc, 1.5), "a fibre touches LPS or the porin OmpC\nand lets go again, so the particle\nsearches over the surface",
                  size="tiny", color=MUT)
    elif k == 1:
        t4(xc, L["om_hi"] + 1.1, s=0.85, zorder=14)
        bio.label(ax, (xc, 1.5), "two or three fibres bound: the baseplate\nchanges conformation and the short\nfibres bind irreversibly",
                  size="tiny", color=MUT)
    elif k == 2:
        t4(xc, L["om_hi"] + 0.75, s=0.85, contracted=True, zorder=14)
        ax.plot([xc, xc], [L["om_hi"] + 0.75, L["pg_hi"] - 0.1], color=P.edge("neutral"), lw=2.0, zorder=16)
        ax.add_patch(Circle((xc, L["pg_hi"] - 0.25), 0.3, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                            lw=0.7, zorder=15))
        bio.label(ax, (xc, 1.5), "the sheath contracts to half its length,\ndriving the tube through the outer membrane;\na lysozyme domain opens the wall",
                  size="tiny", color=MUT)
    else:
        t4(xc, L["om_hi"] + 0.75, s=0.85, contracted=True, empty=True, zorder=14)
        ax.plot([xc, xc], [L["om_hi"] + 0.75, L["im"] - 0.1], color=P.edge("neutral"), lw=2.0, zorder=16)
        t = np.linspace(0, 7 * np.pi, 220)
        ax.plot(xc + 0.4 * np.sin(t) + np.linspace(0, 0.9, 220), np.linspace(L["im"] - 0.2, L["bottom"] + 0.15, 220),
                color=P.edge("dna") if not P.is_dark() else P.fill("dna"), lw=1.4, zorder=16)
        bio.label(ax, (xc, 1.5), "the genome enters under pressure;\nthe empty capsid is left outside",
                  size="tiny", color=MUT)
    if k == 0:
        for nm, yy in (("outside", L["om_hi"] + 0.75), ("periplasm", (L["im_hi"] + L["pg_lo"]) / 2),
                       ("cytoplasm", L["im"] - 0.85)):
            bio.label(ax, (xa + 0.12, yy), nm, size="tiny", color=MUT, ha="left", zorder=19)

# ---------------------------------------------------------------- F: other entry routes
bio.panel(ax, "F", (28.6, 13.3))
bio.label(ax, (29.3, 13.1), "Entry without a contractile tail", size="small", bold=True, ha="left")
rows = [("siphovirus (λ, T5)", "the tail-tip complex inserts\nproteins that form a channel"),
        ("podovirus φ29", "a short tail knob digests the wall\nof its Gram-positive host"),
        ("podovirus T7", "internal core proteins are ejected\nand build a conduit through the periplasm"),
        ("microvirus φX174", "pilot protein H forms the channel;\nno tail at all")]
for i, (name, txt) in enumerate(rows):
    y = 11.4 - i * 2.9
    ax.plot([29.0, 35.6], [y + 0.95, y + 0.95], color=P.mix(MUT, P.surface(), 0.6), lw=0.6)
    bio.label(ax, (29.0, y + 0.45), name, size="small", ha="left")
    bio.label(ax, (29.0, y - 0.35), txt, size="tiny", color=MUT, ha="left")
