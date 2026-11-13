"""Five threads of vertebrate comparative anatomy in one table (rows) across the seven traditional columns of
the comparative chapters (7.17.56, Section 56.8.1; bony fishes = teleosts, reptiles = living non-avian reptiles).

Cells are coloured with the homology colours of vertskel, so that one element keeps its colour along a row:
the palatoquadrate gold becomes the quadrate and the incus, Meckel's coral the articular and the malleus, the
hyoid magenta the hyomandibula and the stapes. Grey cells: element absent or not applicable. Entries follow the
tables of 7.17.58 (arch fates), 7.17.59 (bone counts, approximate ranges), 7.17.65 (aortic arches), 7.17.66
(kidneys and ducts) and 7.17.68 (middle ear).
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
import vertskel as vs

P = bio.P
GROUPS = ["Cyclostomes", "Sharks", "Teleosts", "Amphibians", "Reptiles", "Birds", "Mammals"]
NA = None
# (thread, row label, key, [cell text or (text, key) or NA for each group])
ROWS = [
    ("1 Pharyngeal arches", "Arch 1, upper element", "palatoquadrate",
     [NA, "palatoquadrate:\nupper jaw", "quadrate", "quadrate", "quadrate", "quadrate", "incus"]),
    ("", "Arch 1, lower element", "meckel",
     [NA, "Meckel's cartilage:\nlower jaw", "articular", "articular", "articular", "articular", "malleus"]),
    ("", "Arch 2, dorsal element", "hyomandibula",
     [NA, "hyomandibula:\nsuspends jaw", "hyomandibula,\nsymplectic", "stapes", "columella", "columella", "stapes"]),
    ("2 Skull bones", "Bones in the skull", "parietal",
     [("cartilage only", "chondrocranium"), ("cartilage only", "chondrocranium"), "100-180", "about 30-50",
      "50-90", "many, fused\nin the adult", "about 30-35\n(human 22)"]),
    ("3 Aortic arches", "Arches in the adult", "aortic_4",
     ["gill arteries", "II-VI, gills", "III-VI, gills", "III, IV both,\nVI", "III, IV both,\nVI", "III, right IV,\nVI",
      "III, left IV,\nVI"]),
    ("4 Kidney and ducts", "Adult kidney", "mesonephros",
     ["opisthonephros", "opisthonephros", "opisthonephros", "opisthonephros", ("metanephros", "metanephros"),
      ("metanephros", "metanephros"), ("metanephros", "metanephros")]),
    ("", "Male genital duct", "archinephric_duct",
     [NA, "archinephric\nduct", ("own sperm duct", "gonad"), "archinephric\nduct", "vas deferens\n(Wolffian)",
      "vas deferens\n(Wolffian)", "vas deferens\n(Wolffian)"]),
    ("5 Middle ear", "Ossicles", "stapes",
     [NA, NA, ("none (Weberian\nossicles in some)", "vertebra"), "1: stapes", "1: columella", "1: columella",
      "3: malleus,\nincus, stapes"]),
]

fig, ax = bio.canvas(25.0, 11.6)
x0, cw, top, rh = 6.2, 2.68, 10.4, 1.12
for j, g in enumerate(GROUPS):
    bio.label(ax, (x0 + j * cw + cw / 2, top + 0.45), g, size="small", bold=True)
for i, (thread, lab, key, cells) in enumerate(ROWS):
    yc = top - i * rh - rh / 2
    if thread:
        bio.label(ax, (0.3, yc + 0.28), thread, size="tiny", bold=True, ha="left", color=P.muted())
    bio.label(ax, (0.3, yc - 0.15 if thread else yc), lab, size="tiny", ha="left")
    for j, c in enumerate(cells):
        xa = x0 + j * cw + 0.06
        if c is NA:
            fc, ec, text, tc = "none", P.muted(), "-", P.muted()
        else:
            text, k = (c if isinstance(c, tuple) else (c, key))
            fc, ec, tc = vs.color(k), vs.edge(k), P.on_fill()
        ax.add_patch(FancyBboxPatch((xa, yc - rh / 2 + 0.06), cw - 0.12, rh - 0.12,
                                    boxstyle="round,pad=0,rounding_size=0.12", fc=fc, ec=ec, lw=0.6, zorder=4))
        bio.label(ax, (xa + (cw - 0.12) / 2, yc), text, size="tiny", color=tc, zorder=6)
    if thread and i:
        ax.plot([0.3, x0 + 7 * cw], [yc + rh / 2, yc + rh / 2], color=P.muted(), lw=0.5, zorder=3)
bio.label(ax, (0.3, 0.55), "Cells coloured by homology (vertskel scheme): one element keeps its colour along a row. "
          "Grey: absent. Bone counts are approximate ranges.", size="tiny", ha="left", color=P.muted())
