"""Formation of the autophagosome and the LC3 conjugation system (schematic).
(A) Macroautophagy in a mammalian cell. Induction: the ULK1 complex (ULK1, ATG13, FIP200, ATG101), released
from mTORC1 inhibition, assembles at an ER subdomain. Nucleation: the class III PI 3-kinase complex I
(VPS34, VPS15, Beclin 1, ATG14) makes PI(3)P, which marks the omegasome and recruits WIPI2. Expansion: the
phagophore, a flattened double-membrane cisterna, grows by lipid transfer from the ER through the bridge-like
protein ATG2 with the scramblase ATG9, while the ATG12-ATG5-ATG16L1 complex attaches LC3 to
phosphatidylethanolamine on both faces. Closure by ESCRT-III gives the autophagosome, which fuses with a
lysosome (SNARE complex STX17-SNAP29-VAMP8, tether HOPS); in the autolysosome the inner membrane and the
cargo are digested and the products exported to the cytosol.
(B) The two ubiquitin-like conjugation reactions: ATG4 cleaves pro-LC3 to expose a C-terminal glycine (LC3-I);
ATG7 (E1-like) activates LC3 and ATG12; ATG10 (E2-like) joins ATG12 to ATG5; ATG3 (E2-like), guided by
ATG12-ATG5-ATG16L1 (E3-like), joins LC3 to PE (LC3-II); ATG4 can remove LC3 from PE again."""

import numpy as np

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(23.0, 11.0, scale=0.42)
TH = 0.1


def arc(c, r, a0, a1, n=60):
    a = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + r * np.cos(a), c[1] + r * np.sin(a)]


def band(pts, token="membrane", zorder=6, closed=False):
    q, nrm, _ = bio.core.polyline(pts, n=500, closed=closed)
    o, i = q + nrm * TH / 2, q - nrm * TH / 2
    bio.shape(ax, np.vstack([o, i[::-1]]), token, lw=0, zorder=zorder)
    for ln in (o, i):
        ax.plot(ln[:, 0], ln[:, 1], color=P.edge(token), lw=0.7, zorder=zorder + 1)


def cup(c, r, a0, a1, gap=0.2):
    """A phagophore: a flattened cisterna (two membranes joined at the rims) bent into an arc."""
    outer = arc(c, r, a0, a1)
    inner = arc(c, r - gap, a1, a0)
    rim1 = arc((c[0] + (r - gap / 2) * np.cos(np.radians(a1)), c[1] + (r - gap / 2) * np.sin(np.radians(a1))), gap / 2,
               a1, a1 + 180, 12)
    rim0 = arc((c[0] + (r - gap / 2) * np.cos(np.radians(a0)), c[1] + (r - gap / 2) * np.sin(np.radians(a0))), gap / 2,
               a0 + 180, a0 + 360, 12)
    band(np.vstack([outer, rim1, inner, rim0]), closed=True)


def lc3(points):
    for p in points:
        ax.add_patch(bio.core.Circle(p, 0.07, color=P.edge("positive"), lw=0, zorder=12))


def cargo(c, k=6, rr=0.5, seed=1):
    rng = np.random.default_rng(seed)
    for _ in range(k):
        a, d = rng.uniform(0, 2 * np.pi), rr * np.sqrt(rng.uniform())
        ax.add_patch(bio.core.Circle((c[0] + d * np.cos(a), c[1] + d * np.sin(a)), 0.09, facecolor=P.fill("protein"),
                                     edgecolor=P.edge("protein"), lw=0.5, zorder=9))


# ---- A ------------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.9))
# ER strip along the bottom
er_y = 5.2
xs = np.linspace(0.4, 14.0, 200)
er = np.c_[xs, er_y + 0.08 * np.sin(xs * 1.3)]
bio.shape(ax, np.vstack([er + (0, 0.18), (er - (0, 0.18))[::-1]]), "er", lw=0.8, zorder=4)
bio.label(ax, (0.5, er_y - 0.6), "ER", size="small", bold=True, ha="left")

# 1 induction
bio.box(ax, (1.6, 6.3), 1.6, 0.55, "enzyme", text="ULK1 cx", size="tiny", radius=0.12, zorder=12)
bio.label(ax, (1.6, 7.0), "1  induction", size="tiny", bold=True)
# 2 nucleation: omegasome
om = (4.5, er_y + 0.75)
band(arc(om, 0.45, 200, 340 + 360 * 0, 40))
bio.box(ax, (4.5, 7.05), 1.75, 0.5, "protein", text="VPS34 cx", size="tiny", radius=0.12, zorder=12)
for x in (4.1, 4.5, 4.9):
    ax.add_patch(bio.core.Circle((x, er_y + 0.33), 0.06, color=P.edge("lipid"), lw=0, zorder=12))
bio.label(ax, (4.5, 7.65), "2  nucleation: PI(3)P", size="tiny", bold=True)
# 3 expansion: cup with ATG2 bridge, ATG9 vesicles, LC3
c3 = (8.0, 7.4)
cup(c3, 1.25, 150, 390)
lc3(arc(c3, 1.38, 160, 380, 9))
lc3(arc(c3, 0.95, 165, 375, 8))
ax.plot([7.3, 7.4], [er_y + 0.2, 6.25], color=P.edge("drug"), lw=2.2, zorder=11, solid_capstyle="round")
bio.label(ax, (6.9, 5.95), "ATG2", size="tiny", color=P.edge("drug"), ha="right")
for p in ((9.7, 6.0), (10.0, 6.5)):
    bio.vesicle(ax, p, 0.13, token="vesicle", zorder=10)
bio.label(ax, (10.25, 6.0), "ATG9\nvesicles", size="tiny", ha="left", color=P.muted())
cargo(c3, 6, 0.55, 2)
bio.label(ax, (8.0, 9.35), "3  expansion: LC3-PE (green)", size="tiny", bold=True)
# 4 closed autophagosome
c4 = (12.2, 8.0)
band(arc(c4, 1.1, 0, 360), closed=True)
band(arc(c4, 0.88, 0, 360), closed=True)
lc3(arc(c4, 1.2, 0, 330, 12))
cargo(c4, 7, 0.55, 3)
bio.label(ax, (12.2, 9.55), "4  closure (ESCRT-III)", size="tiny", bold=True)
# 5 fusion with lysosome and autolysosome
ly = (13.0, 3.4)
bio.lysosome(ax, ly, 0.75)
bio.label(ax, (13.0, 2.3), "lysosome", size="tiny")
al = (10.0, 2.6)
bio.vesicle(ax, al, 1.1, token="lysosome")
band(arc(al, 0.75, 0, 360), closed=True, zorder=9)
cargo(al, 5, 0.4, 4)
bio.label(ax, (10.0, 1.1), "5  autolysosome: digestion", size="tiny", bold=True)
bio.label(ax, (14.2, 6.0), "STX17–SNAP29–VAMP8\nHOPS", size="tiny", color=P.muted(), ha="right")
A = dict(kind="process", head=0.18)
bio.arrow(ax, (2.4, 6.3), (3.8, 6.3), **A)
bio.arrow(ax, (5.3, 6.4), (6.6, 6.9), **A)
bio.arrow(ax, (9.45, 7.8), (10.95, 8.0), **A)
bio.arrow(ax, (12.3, 6.8), (12.85, 4.25), **A)
bio.arrow(ax, (12.25, 3.2), (11.2, 2.85), **A)
bio.arrow(ax, (9.0, 1.9), (7.6, 1.7), **A)
bio.label(ax, (7.5, 1.95), "amino acids,\nsugars, lipids", size="tiny", ha="right", color=P.muted())
bio.label(ax, (0.5, 10.3), "Cytosol", size="small", ha="left", color=P.muted(), bold=True)

# ---- B ------------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (15.2, 10.9))
bx = 16.0


def node(c, text, token="protein", w=2.3):
    bio.box(ax, c, w, 0.6, token, text=text, size="tiny", radius=0.12, zorder=12)


# LC3 branch
node((bx + 1.1, 9.9), "pro-LC3")
node((bx + 1.1, 8.5), "LC3-I (Gly)")
node((bx + 1.1, 7.1), "ATG7~LC3", "enzyme")
node((bx + 1.1, 5.7), "ATG3~LC3", "enzyme")
node((bx + 1.1, 4.3), "LC3-II = LC3–PE", "positive", w=2.6)
# ATG12 branch
node((bx + 4.6, 9.9), "ATG12")
node((bx + 4.6, 8.5), "ATG7~ATG12", "enzyme")
node((bx + 4.6, 7.1), "ATG10~ATG12", "enzyme")
node((bx + 4.6, 5.7), "ATG12–ATG5–ATG16L1", "drug", w=3.1)
D = dict(kind="process", head=0.15)
for y0, y1 in ((9.6, 8.8), (8.2, 7.4), (6.8, 6.0), (5.4, 4.6)):
    bio.arrow(ax, (bx + 1.1, y0), (bx + 1.1, y1), **D)
for y0, y1 in ((9.6, 8.8), (8.2, 7.4), (6.8, 6.0)):
    bio.arrow(ax, (bx + 4.6, y0), (bx + 4.6, y1), **D)
lab = dict(size="tiny", color=P.muted(), ha="left")
bio.label(ax, (bx + 1.25, 9.2), "ATG4", **lab)
bio.label(ax, (bx + 1.25, 7.8), "ATG7 (E1)", **lab)
bio.label(ax, (bx + 1.25, 6.4), "ATG3 (E2)", **lab)
bio.label(ax, (bx + 0.95, 5.0), "+ PE", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (bx + 4.75, 9.2), "ATG7 (E1)", **lab)
bio.label(ax, (bx + 4.75, 7.8), "ATG10 (E2)", **lab)
bio.label(ax, (bx + 4.75, 6.4), "+ ATG5, ATG16L1", **lab)
bio.arrow(ax, (bx + 3.0, 5.4), (bx + 1.22, 5.0), kind="catalysis", head=0.15)
bio.label(ax, (bx + 3.3, 4.85), "E3-like", size="tiny", color=P.edge("drug"), ha="left")
bio.arrow(ax, (bx - 0.25, 4.3), (bx - 0.25, 8.5), kind="process", head=0.15, dashed=True, bend=0.25, color=P.muted())
bio.label(ax, (bx - 1.2, 6.4), "ATG4\n(delipidation)", size="tiny", color=P.muted(), ha="center", rotation=90)
bio.label(ax, (bx + 2.9, 3.2), "LC3-II on both membranes of the phagophore:\noutside recruits fusion machinery, inside binds\ncargo receptors (LIR motifs); marker of autophagosomes",
          size="tiny", color=P.ink())
