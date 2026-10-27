# Processing of proinsulin in the regulated secretory pathway of pancreatic beta cells. Preproinsulin (110
# residues) loses its signal peptide (24 residues) in the ER; proinsulin folds with three disulfide bonds
# (A6-A11 within the A chain, A7-B7 and A20-B19 between the chains). In immature secretory granules leaving the
# TGN, the acidic, Ca2+-rich lumen activates the proprotein convertases PC1/3, which cuts after Arg31-Arg32 at
# the B-C junction, and PC2, which cuts after Lys64-Arg65 at the C-A junction; carboxypeptidase E removes the
# exposed basic residues. The granule then holds equimolar insulin (A + B chains, crystallized with Zn2+ as
# hexamers) and C-peptide, which are secreted together (C-peptide in blood reports endogenous insulin secretion).
import wikibio as bio

fig, ax = bio.canvas(22, 7.2)
P = bio.P
u = 0.14  # canvas units per residue
y1, y2, y3 = 6.0, 4.0, 1.6
x0 = 1.0
bio.label(ax, (x0, y1 + 0.6), "Preproinsulin (ER)", size="small", bold=True, ha="left")
parts1 = [("signal 24", 24 * u, "neutral"), ("B chain 30", 30 * u, "channel"), ("C peptide 31 (+RR, KR)", 35 * u, "antibody"),
          ("A chain 21", 21 * u, "receptor")]
end = bio.domains(ax, x0, y1, parts1, height=0.45)
bio.arrow(ax, (x0 + 24 * u, y1 - 0.4), (x0 + 24 * u, y1 - 0.9), kind="process", head=0.15)
bio.label(ax, (x0 + 24 * u + 0.15, y1 - 0.65), "signal peptidase", size="tiny", ha="left")

xp = x0 + 24 * u + 0.05
bio.label(ax, (x0, y2 + 0.6), "Proinsulin (ER folding, 3 disulfides)", size="small", bold=True, ha="left")
parts2 = parts1[1:]
bio.domains(ax, xp, y2, parts2, height=0.45)
xb, xc = xp + 30 * u, xp + 30 * u + 0.05 + 35 * u
for xx, txt in ((xb, "PC1/3 (after R31-R32)"), (xc, "PC2 (after K64-R65)")):
    bio.arrow(ax, (xx, y2 + 1.25), (xx, y2 + 0.3), kind="process", head=0.15)
    bio.label(ax, (xx, y2 + 1.4), txt, size="tiny", va="bottom")
# disulfides as brackets under the chains
xa = xc + 0.05
for (pa, pb, txt) in ((xp + 7 * u, xa + 7 * u, "A7-B7"), (xp + 19 * u, xa + 20 * u, "A20-B19")):
    yy = y2 - 0.25
    ax.plot([pa, pa, pb, pb], [yy, yy - 0.35 - 0.2 * (txt == "A20-B19"), yy - 0.35 - 0.2 * (txt == "A20-B19"), yy],
            color=P.edge("highlight"), lw=1.3)
ax.plot([xa + 6 * u, xa + 6 * u, xa + 11 * u, xa + 11 * u], [y2 + 0.25, y2 + 0.5, y2 + 0.5, y2 + 0.25], color=P.edge("highlight"), lw=1.3)
bio.label(ax, (xa + 8.5 * u, y2 + 0.68), "A6-A11", size="tiny")
bio.label(ax, (xp + 2.0, y2 - 1.05), "S–S: A7–B7, A20–B19", size="tiny", color=P.muted())

bio.label(ax, (x0, y3 + 0.6), "In the granule (+ carboxypeptidase E)", size="small", bold=True, ha="left")
bio.domains(ax, xp, y3, [("B chain", 30 * u, "channel")], height=0.45)
bio.domains(ax, xp, y3 - 0.6, [("A chain", 21 * u, "receptor")], height=0.45)
ax.plot([xp + 7 * u] * 2, [y3 - 0.22, y3 - 0.38], color=P.edge("highlight"), lw=2)
ax.plot([xp + 19 * u] * 2, [y3 - 0.22, y3 - 0.38], color=P.edge("highlight"), lw=2)
bio.label(ax, (xp + 30 * u + 0.3, y3 - 0.3), "insulin\n(Zn²⁺ hexamers)", size="tiny", ha="left")
bio.domains(ax, 12.6, y3, [("C peptide", 31 * u, "antibody")], height=0.45)
bio.label(ax, (12.6 + 31 * u / 2, y3 - 0.6), "C-peptide (equimolar)", size="tiny")
for k, (xy, r) in enumerate((((19.6, 5.3), 1.0), ((20.2, 2.0), 1.0))):
    bio.vesicle(ax, xy, r, token="vesicle")
ax.add_patch(bio.core.Circle((20.2, 2.0), 0.55, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.8, zorder=9))
for k in range(6):
    ax.add_patch(bio.core.Circle((19.3 + 0.35 * (k % 3), 5.1 + 0.4 * (k // 3)), 0.12, facecolor=P.fill("antibody"),
                                 edgecolor=P.edge("antibody"), lw=0.6, zorder=9))
bio.label(ax, (19.6, 6.55), "immature granule\n(proinsulin)", size="tiny")
bio.label(ax, (20.2, 0.6), "mature granule\n(dense core)", size="tiny")
bio.arrow(ax, (19.8, 4.2), (20.1, 3.1), kind="process")
bio.label(ax, (20.3, 3.6), "acidify,\ncleave", size="tiny", ha="left")
