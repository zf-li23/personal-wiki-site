"""Cell biology, genetics and development as one system, arranged around the animal life cycle.

The ring is the life cycle with the chapters of this course (7.5.n) at each stage; the dashed chord
is the germ line, set aside early and carried to the next generation (7.5.27). Beside each stage:
the cellular machinery it uses (7.3, filled boxes) and the genetic logic that analyses it (7.4,
open boxes).
"""

import math

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(26, 15.5)
C, R = (13.0, 7.6), 4.3

stages = [  # angle (degrees), name, chapters, token
    (90, "Gametes", "26, 27", "neutral"),
    (30, "Zygote", "4", "positive"),
    (-30, "Blastula", "5, 6", "ectoderm"),
    (-90, "Gastrula, body plan", "9, 14-17", "mesoderm"),
    (-150, "Organs", "18-33", "endoderm"),
    (150, "Adult: growth, renewal, aging", "34-37", "enzyme"),
]
cell = {
    "Gametes": "meiosis (7.3.21)",
    "Zygote": "Ca2+ signals, cell cycle restart (7.3.18, 7.3.20)",
    "Blastula": "cycles without growth, polarity, Hippo (7.3.20, 7.3.22)",
    "Gastrula, body plan": "adhesion, EMT, actomyosin (7.3.13, 7.3.23)",
    "Organs": "signalling, differentiation, apoptosis (7.3.19, 7.3.24, 7.3.25)",
    "Adult: growth, renewal, aging": "stem cells, senescence, cancer (7.3.24-7.3.26)",
}
gen = {
    "Gametes": "segregation, recombination, imprinting (7.4.5, 7.4.18)",
    "Zygote": "maternal-effect genes (7.4.20)",
    "Blastula": "maternal and zygotic mutants (7.4.20)",
    "Gastrula, body plan": "screens, epistasis, homeotic genes (7.4.19, 7.4.20)",
    "Organs": "mosaics, sex chromosomes (7.4.6, 7.4.9)",
    "Adult: growth, renewal, aging": "two hits in cancer; heritability (7.4.21, 7.4.24)",
}

pos = {}
MARGIN = {"Gametes": 24, "Gastrula, body plan": 29}
for ang, name, chs, tok in stages:
    a = math.radians(ang)
    p = (C[0] + R * math.cos(a), C[1] + R * math.sin(a))
    pos[name] = p
    w = 4.6 if len(name) > 14 else 3.4
    bio.box(ax, p, w, 1.25, tok)
    bio.label(ax, (p[0], p[1] + 0.22), name, size="small", color=P.on_fill())
    bio.label(ax, (p[0], p[1] - 0.3), "7.5." + chs.replace(", ", ", 7.5.").replace("-", "-7.5."), size="tiny",
              color=P.on_fill())

for k in range(len(stages)):
    nxt = stages[(k + 1) % len(stages)]
    a0 = math.radians(stages[k][0] - MARGIN.get(stages[k][1], 17))
    a1 = math.radians(nxt[0] + MARGIN.get(nxt[1], 17))
    p0 = (C[0] + R * math.cos(a0), C[1] + R * math.sin(a0))
    p1 = (C[0] + R * math.cos(a1), C[1] + R * math.sin(a1))
    bio.arrow(ax, p0, p1, kind="process", bend=-0.25)

bio.arrow(ax, (pos["Gastrula, body plan"][0], pos["Gastrula, body plan"][1] + 0.6),
          (pos["Gametes"][0], pos["Gametes"][1] - 0.8), kind="process", dashed=True)
bio.label(ax, (C[0] + 0.25, C[1] + 0.4), "germ line", size="small", ha="left", italic=False)
bio.label(ax, (C[0] + 0.25, C[1] - 0.2), "set aside (7.5.27)", size="tiny", ha="left", color=P.muted())

side = {"Gametes": (0, 2.05), "Zygote": (1, 0), "Blastula": (1, 0), "Gastrula, body plan": (0, -2.05),
        "Organs": (-1, 0), "Adult: growth, renewal, aging": (-1, 0)}
for ang, name, chs, tok in stages:
    p = pos[name]
    sx, dy = side[name]
    if sx == 0:
        y1 = p[1] + dy
        y2 = y1 + (0.7 if dy > 0 else -0.7)
        anchors = [((p[0], y1), "center"), ((p[0], y2), "center")]
    else:
        x = p[0] + sx * 2.7
        anchors = [((x, p[1] + 0.35), "left" if sx > 0 else "right"), ((x, p[1] - 0.35), "left" if sx > 0 else "right")]
    (c_xy, ha), (g_xy, _) = anchors
    for xy, text, filled in ((c_xy, cell[name], True), (g_xy, gen[name], False)):
        t = bio.label(ax, xy, text, size="tiny", ha=ha)
        tok_ = "lipid_head" if filled else "neutral"
        t.set_bbox(dict(boxstyle="round,pad=0.25", facecolor=P.fill(tok_) if filled else "none",
                        edgecolor=P.edge(tok_), lw=0.6))
        if filled:
            t.set_color(P.on_fill())

bio.box(ax, (2.2, 0.75), 0.5, 0.35, "lipid_head")
bio.label(ax, (2.6, 0.75), "cell machinery (7.3)", size="tiny", ha="left")
ax.add_patch(__import__("matplotlib.patches", fromlist=["FancyBboxPatch"]).FancyBboxPatch(
    (6.95, 0.575), 0.5, 0.35, boxstyle="round,pad=0,rounding_size=0.1", facecolor="none",
    edgecolor=P.edge("neutral"), lw=0.6))
bio.label(ax, (7.6, 0.75), "genetic analysis (7.4)", size="tiny", ha="left")
