"""The three biochemical subtypes of C4 photosynthesis, named after the bundle-sheath decarboxylase.

Each panel: a mesophyll cell (left) and a bundle-sheath cell (right) joined by plasmodesmata. In all three,
PEP carboxylase in the mesophyll cytosol fixes HCO3- into oxaloacetate (OAA), and the CO2 released in the
bundle sheath is refixed by rubisco in the Calvin cycle. A: NADP-malic enzyme type (maize, sorghum,
sugarcane): OAA is reduced to malate in mesophyll chloroplasts; NADP-ME in bundle-sheath chloroplasts
releases CO2 and NADPH; pyruvate returns and pyruvate phosphate dikinase (PPDK) regenerates PEP.
B: NAD-malic enzyme type (proso millet, amaranth, Atriplex): OAA is transaminated to aspartate; in
bundle-sheath mitochondria aspartate is converted back to OAA, reduced to malate and decarboxylated by
NAD-ME; alanine returns and is converted to pyruvate and PEP. C: PEP carboxykinase type (guinea grass):
aspartate is converted to OAA, which PEPCK decarboxylates in the bundle-sheath cytosol at the cost of
one ATP; PEP (or alanine/pyruvate) returns. Dashed arrows: transport between the cells.
"""
from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import metabolism as M
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(31.5, 12.6, scale=0.4)


def cell(x0, y0, x1, y1, txt, tok):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.5",
                                facecolor=ps.tint(tok, 0.5, 0.82), edgecolor=P.edge("cell_wall"), lw=2.0, zorder=1))
    bio.label(ax, (x0 + 0.3, y1 - 0.4), txt, size="small", bold=True, ha="left", color=P.edge("cell_wall"))


def organelle(xy, w, h, txt, tok):
    ax.add_patch(FancyBboxPatch((xy[0] - w / 2, xy[1] - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.4",
                                facecolor=ps.tint(tok, 0.25, 0.65), edgecolor=P.edge(tok), lw=1.0, ls="--", zorder=2))
    bio.label(ax, (xy[0] - w / 2 + 0.2, xy[1] + h / 2 - 0.3), txt, size="tiny", ha="left", color=P.edge(tok))


def enz(xy, txt):
    bio.label(ax, xy, txt, size="tiny", bold=True, color=P.edge("enzyme"))


def frame(x0, letter, title):
    bio.panel(ax, letter, (x0 + 0.1, 12.4))
    bio.label(ax, (x0 + 0.8, 12.35), title, size="title", ha="left", va="top")
    cell(x0 + 0.2, 0.4, x0 + 4.8, 11.2, "Mesophyll", "cytoplasm")
    cell(x0 + 5.3, 0.4, x0 + 10.1, 11.2, "Bundle sheath", "chloroplast")
    bio.label(ax, (x0 + 5.05, 0.15), "plasmodesmata", size="tiny", color=P.muted())


def common(pw, x0):
    pw.node("co2", (x0 + 1.4, 10.0), "CO₂ → HCO₃⁻", token="neutral")
    pw.node("pep", (x0 + 1.4, 4.6), "PEP")
    pw.node("oaa", (x0 + 1.4, 7.6), "OAA")
    pw.step("co2", "oaa")
    pw.step("pep", "oaa")
    enz((x0 + 2.75, 6.1), "PEPC")
    pw.node("cal", (x0 + 7.7, 2.0), "Calvin cycle", token="carbohydrate")


# ---- A: NADP-ME
x0 = 0.0
frame(x0, "A", "NADP-ME type")
organelle((x0 + 3.55, 8.75), 2.0, 2.1, "chloroplast", "chloroplast")
organelle((x0 + 7.9, 7.0), 3.4, 5.8, "chloroplast", "chloroplast")
pa = M.Pathway(ax, size="small")
common(pa, x0)
pa.node("mal", (x0 + 3.55, 8.5), "Malate", bold=True)
pa.step("oaa", "mal")
enz((x0 + 3.0, 7.25), "NADP-MDH")
pa.node("malb", (x0 + 7.4, 8.6), "Malate", bold=True)
pa.node("co2b", (x0 + 8.4, 5.6), "CO₂", token="highlight", bold=True)
pa.node("pyrb", (x0 + 6.4, 5.6), "Pyruvate")
pa.node("pyrm", (x0 + 3.4, 2.4), "Pyruvate")
pa.step("mal", "malb", color=P.muted(), dashed=True)
pa.step("malb", "co2b")
pa.step("malb", "pyrb")
enz((x0 + 9.15, 7.0), "NADP-ME\n(→ NADPH)")
pa.step("co2b", "cal", enzyme="rubisco", enzyme_offset=0.12)
pa.step("pyrb", "pyrm", color=P.muted(), dashed=True)
pa.step("pyrm", "pep", enzyme="PPDK", enzyme_offset=0.12, enzyme_flip=True)
bio.label(ax, (x0 + 2.4, 1.3), "2 ATP equiv.", size="tiny", color=P.muted())

# ---- B: NAD-ME
x0 = 10.7
frame(x0, "B", "NAD-ME type")
organelle((x0 + 7.0, 7.0), 2.8, 4.4, "mitochondrion", "mitochondrion")
pb = M.Pathway(ax, size="small")
common(pb, x0)
pb.node("asp", (x0 + 3.5, 8.6), "Aspartate", bold=True)
pb.step("oaa", "asp")
pb.node("aspb", (x0 + 6.6, 10.2), "Aspartate", bold=True)
pb.node("oaab", (x0 + 6.6, 8.3), "OAA")
pb.node("malb", (x0 + 6.6, 6.6), "Malate")
pb.node("pyrb", (x0 + 6.6, 5.25), "Pyruvate")
pb.node("co2b", (x0 + 9.0, 6.6), "CO₂", token="highlight", bold=True)
pb.node("ala_b", (x0 + 6.6, 3.4), "Alanine")
pb.node("alam", (x0 + 3.5, 3.4), "Alanine")
pb.node("pyrm", (x0 + 3.5, 1.7), "Pyruvate")
pb.step("asp", "aspb", color=P.muted(), dashed=True)
pb.step("aspb", "oaab")
pb.step("oaab", "malb")
pb.step("malb", "co2b")
pb.step("malb", "pyrb")
enz((x0 + 7.75, 5.95), "NAD-ME")
pb.step("pyrb", "ala_b")
pb.step("co2b", "cal", enzyme="rubisco", enzyme_offset=0.12)
pb.step("ala_b", "alam", color=P.muted(), dashed=True)
pb.step("alam", "pyrm")
pb.step("pyrm", "pep", enzyme="PPDK", enzyme_offset=0.12, enzyme_flip=True)

# ---- C: PEPCK
x0 = 21.4
frame(x0, "C", "PEPCK type")
pc = M.Pathway(ax, size="small")
common(pc, x0)
pc.node("asp", (x0 + 3.5, 8.6), "Aspartate", bold=True)
pc.step("oaa", "asp")
pc.node("aspb", (x0 + 7.0, 10.0), "Aspartate", bold=True)
pc.node("oaab", (x0 + 7.0, 7.8), "OAA")
pc.node("co2b", (x0 + 8.6, 5.2), "CO₂", token="highlight", bold=True)
pc.node("pepb", (x0 + 6.2, 5.2), "PEP")
pc.step("asp", "aspb", color=P.muted(), dashed=True)
pc.step("aspb", "oaab")
pc.step("oaab", "co2b")
pc.step("oaab", "pepb")
enz((x0 + 6.9, 4.2), "PEPCK (ATP → ADP)")
pc.step("co2b", "cal", enzyme="rubisco", enzyme_offset=0.12)
pc.step("pepb", "pep", color=P.muted(), dashed=True)
bio.label(ax, (x0 + 2.6, 2.4), "PEP returns directly\n(part as alanine/pyruvate)", size="tiny", color=P.muted())
