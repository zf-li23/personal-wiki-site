"""The glyoxylate cycle in a germinating oilseed: three compartments convert fatty acids to sugar.

Glyoxysome: fatty acids are beta-oxidized to acetyl-CoA; citrate synthase and aconitase act as in the
citric acid cycle, but isocitrate lyase splits isocitrate into succinate and glyoxylate, and malate synthase
condenses glyoxylate with a second acetyl-CoA; malate dehydrogenase regenerates oxaloacetate. Net:
2 acetyl-CoA + NAD+ + 2 H2O -> succinate + 2 CoA + NADH + H+. Mitochondrion: succinate is oxidized to malate
by succinate dehydrogenase and fumarase; malate is exported. Cytosol: malate dehydrogenase and PEP
carboxykinase give phosphoenolpyruvate, which gluconeogenesis converts to hexose phosphates and sucrose.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(26.0, 15.0, scale=0.4)


def box(x0, y0, x1, y1, token, text, edge=None):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.7",
                                facecolor=P.fill(token), edgecolor=P.edge(edge or token), lw=1.3, zorder=1))
    bio.label(ax, (x0 + 0.4, y1 - 0.45), text, size="small", bold=True, ha="left", color=P.edge(edge or token))


box(0.3, 0.3, 13.2, 14.7, "peroxisome", "Glyoxysome")
box(14.0, 7.6, 25.7, 14.7, "mitochondrion", "Mitochondrion")
bio.label(ax, (14.3, 6.9), "Cytosol", size="small", bold=True, ha="left", color=P.muted())

pw = M.Pathway(ax, size="small")
c, r = (6.6, 6.0), 3.7
names = [("oaa", "Oxaloacetate"), ("cit", "Citrate"), ("icit", "Isocitrate"), ("glx", "Glyoxylate"), ("mal", "Malate")]
pos = M.ring(c, r, 5, start=126, clockwise=True)
for (id, t), p in zip(names, pos):
    pw.node(id, p, t)
steps = [("oaa", "cit", "Citrate\nsynthase", None, False), ("cit", "icit", "Aconitase", None, True),
         ("icit", "glx", "Isocitrate\nlyase", None, False), ("glx", "mal", "Malate\nsynthase", None, False),
         ("mal", "oaa", "Malate DH", ("NAD⁺", "NADH"), True)]
mids = {}
for a, b, e, side, rev in steps:
    mids[a], _, _ = pw.step(a, b, enzyme=e, side=side, reversible=rev, enzyme_offset=0.45, side_reach=0.5,
                            bend=M.cycle_bend(pw.nodes[a][0], pw.nodes[b][0], c, clockwise=True))
bio.label(ax, c, "Glyoxylate\ncycle", size="normal", bold=True, color=P.edge("peroxisome"))

pw.node("fa", (6.6, 13.4), "Fatty acids (triacylglycerols)", bold=True)
pw.node("acoa", (6.6, 11.3), "Acetyl-CoA", token="highlight", bold=True)
pw.step("fa", "acoa", enzyme="β oxidation", enzyme_offset=0.2)
bio.arrow(ax, pw.anchor("acoa", "l") + (-0.05, -0.1), mids["oaa"] + (0, 0.25), kind="process", bend=0.25)
pw.node("acoa2", (2.3, 1.4), "Acetyl-CoA", token="highlight")
bio.arrow(ax, pw.anchor("acoa2", "t") + (0.3, 0.05), mids["glx"] + (-0.2, -0.15), kind="process", bend=-0.2)
bio.label(ax, (2.3, 0.75), "second acetyl-CoA", size="tiny", color=P.muted())

# succinate out to the mitochondrion
pw.node("suc_g", (11.4, 2.2), "Succinate")
pw.step("icit", "suc_g", bend=-0.2)
pw.node("suc", (16.0, 11.0), "Succinate")
pw.node("fum", (19.6, 11.0), "Fumarate")
pw.node("mal_m", (23.2, 11.0), "Malate")
pw.step("suc_g", "suc", bend=0.25)
pw.step("suc", "fum", enzyme="Succinate DH", side=("FAD", "FADH₂"), reversible=True, enzyme_offset=0.2)
pw.step("fum", "mal_m", enzyme="Fumarase", side=("H₂O", None), reversible=True, enzyme_offset=0.2)

# cytosol: malate -> oxaloacetate -> PEP -> sugars
pw.node("mal_c", (23.2, 6.0), "Malate")
pw.node("oaa_c", (23.2, 3.0), "Oxaloacetate")
pw.node("pep", (17.8, 3.0), "Phosphoenolpyruvate")
pw.node("suc_rose", (16.4, 1.1), "Hexose phosphates → sucrose", bold=True, token="carbohydrate")
pw.step("mal_m", "mal_c")
pw.step("mal_c", "oaa_c", enzyme="Malate DH\n(NAD⁺ → NADH)", reversible=True, enzyme_offset=0.2)
pw.step("oaa_c", "pep", enzyme="PEP carboxykinase", side=("GTP", "GDP + CO₂"), enzyme_offset=0.2, flip=True)
pw.step("pep", "suc_rose", enzyme="gluconeogenesis", enzyme_offset=0.15, enzyme_flip=True)
