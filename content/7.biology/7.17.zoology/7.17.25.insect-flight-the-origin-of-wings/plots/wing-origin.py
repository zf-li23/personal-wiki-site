# Three hypotheses for the origin of insect wings, shown on a schematic transverse section of a thoracic
# segment (left half; dorsal up, tergum blue, pleuron green, leg teal, sternum grey, the proto-wing tissue pink).
# A: paranotal (tergal) hypothesis: wings grew from fixed lateral extensions of the tergum (paranota),
# later acquiring an articulation and muscles. B: exite (pleural, gill) hypothesis: wings derive from an
# exite, a lateral outgrowth of a basal leg segment (epicoxa) that became incorporated into the body wall,
# perhaps first a gill or a gliding flap. C: dual origin: the wing combines tergal tissue (the blade) with a
# pleural, appendage-derived contribution (the hinge, muscles and part of the gene network, e.g. vestigial
# and apterous expression), as suggested by gene-expression studies in crustaceans and insects.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 9.6)
titles = [("A", "Paranotal (tergal) origin"), ("B", "Exite (pleural) origin"), ("C", "Dual origin")]
for i, (L, t) in enumerate(titles):
    x0 = i * 9.0
    bio.panel(ax, L, (x0 + 0.2, 9.3))
    bio.label(ax, (x0 + 4.6, 9.2), t, size="normal", bold=True)
    bio.shape(ax, [(x0 + 4.0, 7.4), (x0 + 7.8, 7.4), (x0 + 7.8, 6.8), (x0 + 4.0, 6.6)], "channel", lw=0.9, zorder=4)  # tergum
    bio.shape(ax, [(x0 + 3.6, 6.5), (x0 + 4.2, 6.5), (x0 + 4.4, 3.6), (x0 + 3.8, 3.6)], "positive", lw=0.9, zorder=4)  # pleuron
    bio.shape(ax, [(x0 + 4.4, 3.6), (x0 + 7.8, 3.4), (x0 + 7.8, 2.8), (x0 + 4.6, 3.0)], "neutral", lw=0.9, zorder=4)  # sternum
    leg = [(x0 + 3.8, 3.5), (x0 + 3.2, 3.0), (x0 + 2.6, 1.8), (x0 + 2.2, 0.6)]
    for (ax0, ay0), (ax1, ay1) in zip(leg[:-1], leg[1:]):
        ax.plot([ax0, ax1], [ay0, ay1], color=P.edge("enzyme"), lw=5, solid_capstyle="round", zorder=5)
    bio.label(ax, (x0 + 6.0, 7.0), "tergum", size="tiny")
    bio.label(ax, (x0 + 4.8, 5.0), "pleuron", size="tiny", ha="left")
    bio.label(ax, (x0 + 1.6, 1.0), "leg", size="tiny")
    if i == 0:
        bio.shape(ax, [(x0 + 4.0, 7.3), (x0 + 0.8, 7.0), (x0 + 0.8, 6.75), (x0 + 4.0, 6.7)], "petal", lw=0.9, zorder=5)
        bio.label(ax, (x0 + 2.0, 7.55), "paranotal lobe", size="tiny")
        bio.label(ax, (x0 + 1.0, 6.0), "later hinged\nand muscled", size="tiny", ha="left")
    elif i == 1:
        bio.shape(ax, [(x0 + 3.4, 3.2), (x0 + 1.2, 4.2), (x0 + 1.0, 3.9), (x0 + 3.3, 2.9)], "petal", lw=0.9, zorder=6)
        bio.label(ax, (x0 + 1.6, 4.6), "exite of epicoxa", size="tiny")
        bio.arrow(ax, (x0 + 1.4, 5.0), (x0 + 2.4, 6.9), kind="process", color=P.muted(), bend=-0.25)
        bio.label(ax, (x0 + 0.6, 6.4), "moves dorsally", size="tiny")
    else:
        bio.shape(ax, [(x0 + 4.0, 7.3), (x0 + 0.8, 7.0), (x0 + 0.8, 6.75), (x0 + 4.0, 6.7)], "channel", lw=0.9, zorder=5)
        bio.shape(ax, [(x0 + 4.2, 6.8), (x0 + 3.4, 6.8), (x0 + 3.2, 6.4), (x0 + 4.0, 6.3)], "petal", lw=0.9, zorder=6)
        bio.label(ax, (x0 + 2.0, 7.55), "tergal blade", size="tiny")
        bio.callout(ax, (x0 + 3.6, 6.5), (x0 + 1.0, 5.4), "pleural (appendage)\ncontribution: hinge", size="tiny")
