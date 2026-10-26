"""Where the carbon skeletons of the 20 amino acids enter central metabolism (Lehninger 8e, Fig. 18-15).
Six entry points: pyruvate (A, C, G, S, T, W), acetyl-CoA (I, L, T, W) and acetoacetyl-CoA (F, K, L, W, Y),
alpha-ketoglutarate (E, H, P, Q, R), succinyl-CoA (I, M, T, V), fumarate (F, Y) and oxaloacetate (D, N).
Amino acids listed twice give parts of their skeletons to two entry points. Colour: glucogenic (skeleton can
become glucose through oxaloacetate and gluconeogenesis), ketogenic (only acetyl-CoA / acetoacetyl-CoA:
ketone bodies or fatty acids), both. Leucine and lysine are the only purely ketogenic amino acids."""

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(19.0, 16.4)
KIND = {"L": "keto", "K": "keto", "F": "both", "Y": "both", "W": "both", "T": "both", "I": "both"}
TOK = {"gluco": "carbohydrate", "keto": "lipid", "both": "drug"}

pw = M.Pathway(ax, size="small")
c, r = (9.5, 6.6), 3.3
cyc = [("oaa", "Oxaloacetate"), ("cit", "Citrate"), ("icit", "Isocitrate"), ("akg", "α-Ketoglutarate"),
       ("scoa", "Succinyl-CoA"), ("suc", "Succinate"), ("fum", "Fumarate"), ("mal", "Malate")]
pos = M.ring(c, r, 8, start=112.5, clockwise=True)
for (id, text), p in zip(cyc, pos):
    pw.node(id, p, text, bold=id in ("oaa", "akg", "scoa", "fum"))
for a, b in zip([x[0] for x in cyc], [x[0] for x in cyc][1:] + ["oaa"]):
    pw.step(a, b, bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True))
bio.label(ax, c, "Citric acid\ncycle", size="normal", bold=True, color=P.muted())
pw.node("acoa", (9.5, 11.3), "Acetyl-CoA", bold=True, token="highlight")
pw.node("pyr", (4.6, 12.9), "Pyruvate", bold=True)
pw.node("aacoa", (14.4, 12.9), "Acetoacetyl-CoA", bold=True, token="highlight")
pw.step("pyr", "acoa", enzyme="PDH")
pw.step("aacoa", "acoa", enzyme="thiolase", enzyme_flip=True)
pw.step("acoa", "cit", bend=-0.15)
pw.step("pyr", "oaa", enzyme="pyruvate carboxylase", bend=0.12, dashed=True)
bio.label(ax, (1.0, 7.0), "oxaloacetate → PEP → glucose\n(gluconeogenesis, 7.1.19)", size="tiny", ha="left", color=P.muted())
bio.label(ax, (17.9, 12.1), "→ ketone bodies, fatty acids", size="tiny", ha="right", color=P.muted())


def chips(letters, at, dx=0.72, dy=0.0, cols=None):
    """A row (or grid) of one-letter amino-acid discs coloured by fate; returns the group centre."""
    cols = cols or len(letters)
    x0, y0 = at
    pts = []
    for k, aa in enumerate(letters):
        row, col = divmod(k, cols)
        p = (x0 + col * dx, y0 - row * 0.72 + col * dy)
        tok = TOK[KIND.get(aa, "gluco")]
        bio.molecule(ax, p, token=tok, text=aa, r=0.31, size="small")
        pts.append(p)
    xs, ys = [q[0] for q in pts], [q[1] for q in pts]
    return ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)


def feed(group, node, side, gap=0.45):
    tip = pw.anchor(node, side)
    bio.arrow(ax, group, tip, kind="process", color=P.edge("enzyme"), lw=1.4, shrink=gap, head=0.2)


g = chips("ACGSTW", (2.8, 15.2))
feed((g[0], g[1] - 0.3), "pyr", "t", gap=0.3)
g = chips("FKLWY", (12.95, 15.2))
feed((g[0], g[1] - 0.3), "aacoa", "t", gap=0.3)
g = chips("ILTW", (12.6, 10.4), cols=2)
feed((g[0] - 0.55, g[1] + 0.2), "acoa", "r", gap=0.3)
g = chips("EHPQR", (15.6, 9.0), cols=3)
feed((g[0] - 0.5, g[1] - 0.6), "akg", "t", gap=0.4)
g = chips("IMTV", (15.4, 3.1), cols=2)
feed((g[0] - 0.4, g[1] + 0.2), "scoa", "r", gap=0.4)
g = chips("FY", (2.6, 3.2))
feed((g[0] + 0.3, g[1] + 0.2), "fum", "l", gap=0.4)
g = chips("DN", (2.4, 10.0))
feed((g[0] + 0.4, g[1] - 0.3), "oaa", "l", gap=0.4)

# legend
for k, (name, kind) in enumerate((("glucogenic", "gluco"), ("ketogenic", "keto"), ("both", "both"))):
    x = 5.6 + k * 3.0
    bio.molecule(ax, (x, 0.6), token=TOK[kind], r=0.22)
    bio.label(ax, (x + 0.35, 0.6), name, size="small", ha="left")
