# C3 and C4 leaf anatomy in transverse section, built cell by cell (wikibio.botany). (A) A C3 eudicot leaf
# (dorsiventral): cuticle and upper epidermis, one layer of columnar palisade mesophyll rich in
# chloroplasts, spongy mesophyll with large intercellular air spaces, veins in a pale parenchymatous
# bundle sheath (xylem towards the upper side, phloem below) and stomata in the lower epidermis opening into
# substomatal cavities; veins are far apart and Rubisco works in every mesophyll cell. (B) A C4 grass leaf
# with Kranz ("wreath") anatomy (e.g. Zea mays, NADP-malic enzyme type): veins are close together (about two
# mesophyll cells between bundle sheaths); each vein sits in a sheath of large, chloroplast-rich bundle
# sheath cells (chloroplasts towards the outer walls) wrapped by a ring of radially arranged mesophyll cells.
# Mesophyll cells fix HCO3- with PEP carboxylase into C4 acids, which diffuse through plasmodesmata into the
# bundle sheath and release CO2 next to Rubisco. Groups of large bulliform cells in the upper epidermis
# (they roll the leaf when it loses water) and stomata on both surfaces are typical of grasses.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(25.0, 13.6)
W, H = 17.0, 4.2

bio.panel(ax, "A", (0.2, 13.4))
bio.label(ax, (0.85, 13.37), "C3 leaf (dorsiventral eudicot)", size="title", ha="left", va="top")
a = B.leaf_anatomy(ax, (0.6, 7.7, W, H), kind="C3", veins=2)
bio.panel(ax, "B", (0.2, 6.5))
bio.label(ax, (0.85, 6.47), "C4 leaf (Kranz anatomy, grass)", size="title", ha="left", va="top")
b = B.leaf_anatomy(ax, (0.6, 0.7, W, H), kind="C4")
X = W + 1.6


def labels(an, items, y0, y1):
    pts = [(name, an[key]) for key, name in items if an.get(key) is not None]
    pts.sort(key=lambda t: (-round(float(t[1][1]), 1), -float(t[1][0])))
    for k, (name, p) in enumerate(pts):
        y = y0 - k * (y0 - y1) / max(1, len(pts) - 1)
        bio.callout(ax, p, (X, y), name)


labels(a, [("cuticle", "Cuticle"), ("upper_epidermis", "Upper epidermis"), ("palisade", "Palisade mesophyll"),
           ("xylem", "Xylem"), ("sheath", "Bundle sheath"), ("phloem", "Phloem"), ("spongy", "Spongy mesophyll"),
           ("air_space", "Substomatal cavity"), ("guard_cell", "Guard cell (stoma)"), ("lower_epidermis", "Lower epidermis")],
       12.6, 7.4)
labels(b, [("bulliform", "Bulliform cells"), ("upper_epidermis", "Upper epidermis"), ("mesophyll", "Mesophyll (PEP carboxylase)"),
           ("sheath", "Bundle sheath (Rubisco)"), ("xylem", "Xylem"), ("phloem", "Phloem"), ("guard_cell", "Stoma"),
           ("lower_epidermis", "Lower epidermis")], 5.6, 0.6)
# interveinal distance
v = b["veins"]
if len(v) > 2:
    y = 0.25
    ax.annotate("", xy=(v[1][0], y), xytext=(v[2][0], y),
                arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9, shrinkA=0, shrinkB=0))
    bio.label(ax, ((v[1][0] + v[2][0]) / 2, y - 0.02), "interveinal distance", size="tiny", color=P.muted(), va="top")
