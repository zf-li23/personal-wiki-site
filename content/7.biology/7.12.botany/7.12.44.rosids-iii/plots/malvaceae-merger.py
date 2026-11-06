# Malvaceae s.l. A: schematic longitudinal section of a Hibiscus flower: epicalyx outside the calyx,
# petals fused at the base to the staminal column (monadelphous stamens), unilocular anthers on the
# upper part of the column, the five-branched style emerging from its mouth, superior ovary.
# B: the nine subfamilies (Bayer et al. 1999; Judd et al. 2016); relationships within Malvadendrina
# are drawn as a polytomy except for Bombacoideae + Malvoideae (Malvatheca). Squares give the
# Cronquist family to which the genera of each subfamily belonged.
import numpy as np
from matplotlib.patches import Circle, Ellipse

import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(32, 14)

# ---------------- A: Hibiscus flower
bio.panel(ax, "A", (0.3, 13.8))
cx, y0 = 6.0, 2.2
bio.shape(ax, [(cx - 0.35, 0.4), (cx + 0.35, 0.4), (cx + 0.3, y0), (cx - 0.3, y0)], token="plant", lw=1.0)  # pedicel
# receptacle
bio.shape(ax, [(cx - 1.0, y0), (cx + 1.0, y0), (cx + 0.7, y0 + 0.6), (cx - 0.7, y0 + 0.6)], token="plant", lw=1.0)
for s in (-1, 1):
    # epicalyx bracts (narrow, outermost)
    bio.shape(ax, [(cx + s * 0.9, y0 + 0.2), (cx + s * 1.05, y0 + 0.3), (cx + s * 2.1, y0 + 1.9), (cx + s * 1.95, y0 + 2.0)],
              token="bract", lw=0.9, zorder=7)
    # calyx lobe
    bio.shape(ax, [(cx + s * 0.75, y0 + 0.5), (cx + s * 1.0, y0 + 0.55), (cx + s * 1.75, y0 + 2.8), (cx + s * 1.3, y0 + 3.0)],
              token="sepal", lw=0.9, zorder=6)
    # petal: base adnate to column, then spreading
    t = np.linspace(0, 1, 30)
    inner = np.c_[cx + s * (0.35 + 3.3 * t ** 1.6), y0 + 0.6 + 5.2 * t]
    outer = np.c_[cx + s * (0.5 + 4.6 * t ** 1.3), y0 + 0.6 + 4.6 * t]
    bio.shape(ax, np.vstack([inner, outer[::-1]]), token="petal", lw=1.0, zorder=5)
# ovary
bio.shape(ax, [(cx - 0.55, y0 + 0.6), (cx + 0.55, y0 + 0.6), (cx + 0.5, y0 + 1.5), (cx, y0 + 1.75), (cx - 0.5, y0 + 1.5)],
          token="ovary", lw=1.0, zorder=8)
for k, yy in enumerate((y0 + 0.95, y0 + 1.25)):
    for xx in (cx - 0.22, cx + 0.22):
        ax.add_patch(Circle((xx, yy), 0.1, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.5, zorder=9))
# staminal column around the style
top = y0 + 7.6
bio.shape(ax, [(cx - 0.22, y0 + 1.75), (cx + 0.22, y0 + 1.75), (cx + 0.16, top), (cx - 0.16, top)], token="anther", lw=0.9, zorder=8)
ax.plot([cx, cx], [y0 + 1.7, top + 1.0], color=P.edge("ovary"), lw=1.4, zorder=9)
for k in range(5):
    a = -0.9 + 0.45 * k
    ax.plot([cx, cx + 0.9 * np.sin(a)], [top + 1.0, top + 1.0 + 0.7 * np.cos(a)], color=P.edge("ovary"), lw=1.2, zorder=9)
    ax.add_patch(Circle((cx + 0.9 * np.sin(a), top + 1.0 + 0.7 * np.cos(a)), 0.13, facecolor=P.fill("ovary"),
                                 edgecolor=P.edge("ovary"), lw=0.6, zorder=10))
# free filament tips with kidney-shaped one-locular anthers on the upper column
for j, yy in enumerate(np.linspace(y0 + 4.3, top - 0.2, 7)):
    for s in (-1, 1):
        x1 = cx + s * (0.55 + 0.05 * (j % 2))
        ax.plot([cx + s * 0.18, x1], [yy, yy + 0.25], color=P.edge("anther"), lw=0.8, zorder=8)
        ax.add_patch(Ellipse((x1 + s * 0.1, yy + 0.3), 0.3, 0.2, facecolor=P.fill("anther"), edgecolor=P.edge("anther"),
                                      lw=0.6, zorder=9))
bio.callout(ax, (cx - 1.9, y0 + 1.8), (0.8, 3.0), "Epicalyx")
bio.callout(ax, (cx + 1.5, y0 + 2.6), (11.0, 3.3), "Calyx")
bio.callout(ax, (cx + 3.5, y0 + 4.6), (11.0, 6.0), "Petal (base fused to column)")
bio.callout(ax, (cx + 0.2, y0 + 3.2), (11.0, 4.6), "Staminal column")
bio.callout(ax, (cx + 0.65, y0 + 6.0), (11.0, 9.4), "Anthers (1-locular)")
bio.callout(ax, (cx + 0.6, top + 1.5), (11.0, 11.6), "Style branches (5)")
bio.callout(ax, (cx - 0.4, y0 + 1.1), (0.8, 1.2), "Superior ovary")

# ---------------- B: subfamilies
bio.panel(ax, "B", (15.0, 13.8))
NEWICK = ("((Grewioideae,Byttnerioideae)Byttneriina,(Sterculioideae,Tilioideae,Dombeyoideae,Brownlowioideae,"
          "Helicteroideae,(Bombacoideae,Malvoideae)Malvatheca)Malvadendrina)Malvaceae;")
t = phylo.tree(ax, NEWICK, origin=(15.6, 1.4), width=7.0, height=10.8, label_size="small", root_edge=0.4)
OLD = {"Grewioideae": ["Til"], "Byttnerioideae": ["Ste"], "Sterculioideae": ["Ste"], "Tilioideae": ["Til"],
       "Dombeyoideae": ["Ste"], "Brownlowioideae": ["Til"], "Helicteroideae": ["Ste", "Bom"],
       "Bombacoideae": ["Bom"], "Malvoideae": ["Mal", "Bom"]}
TOK = {"Mal": "petal", "Til": "plant", "Ste": "anther", "Bom": "dna"}
for tip in t.tips():
    x, y = tip.xy
    for i, fam in enumerate(OLD[tip.name]):
        bio.box(ax, (27.4 + 0.75 * i, y), 0.55, 0.45, token=TOK[fam], radius=0.08)
bio.label(ax, (27.8, 12.9), "Cronquist family", size="small")
NAMES = [("Mal", "Malvaceae s.s."), ("Til", "Tiliaceae"), ("Ste", "Sterculiaceae"), ("Bom", "Bombacaceae")]
for i, (k, name) in enumerate(NAMES):
    bio.box(ax, (16.2 + 3.6 * i, 0.45), 0.55, 0.45, token=TOK[k], radius=0.08)
    bio.label(ax, (16.6 + 3.6 * i, 0.45), name, size="small", ha="left")
