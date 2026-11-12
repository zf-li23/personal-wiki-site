# Homology of the anterior (head) segments and their appendages across the panarthropods (after BG 4e
# Table 20.2, with Hox and engrailed expression data). Each row is one segment, identified by its brain
# neuromere; cells in a row are homologous and share a colour. The deutocerebral appendages (onychophoran
# jaws, chelifores, chelicerae, myriapod and insect antennae, crustacean first antennae) are homologous;
# the tritocerebral segment carries pedipalps in chelicerates and second antennae in crustaceans, but no
# appendage in myriapods and hexapods (the intercalary segment). Dash: segment without appendage.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 9.2)
cols = ["Onychophora", "Pycnogonida", "Euchelicerata", "Myriapoda", "Crustacea", "Hexapoda"]
rows = [("1  Protocerebral (ocular)", "neutral", ["Antennae", "–", "–", "–", "–", "–"]),
        ("2  Deutocerebral", "dna", ["Jaws", "Chelifores", "Chelicerae", "Antennae", "First antennae", "Antennae"]),
        ("3  Tritocerebral", "rna", ["Slime papillae", "Palps", "Pedipalps", "–", "Second antennae", "–"]),
        ("4", "enzyme", ["Legs", "Ovigers", "Leg 1", "Mandibles", "Mandibles", "Mandibles"]),
        ("5", "protein", ["Legs", "Leg 1", "Leg 2", "First maxillae", "First maxillae", "Maxillae"]),
        ("6", "petal", ["Legs", "Leg 2", "Leg 3", "Second maxillae", "Second maxillae", "Labium"])]
x0, w, h, y0 = 6.4, 3.15, 1.0, 7.6
bio.label(ax, (0.3, y0 + 0.9), "Segment (brain neuromere)", size="small", bold=True, ha="left")
for j, c in enumerate(cols):
    bio.label(ax, (x0 + j * w + w / 2, y0 + 0.9), c, size="small", bold=True)
for i, (name, tok, cells) in enumerate(rows):
    y = y0 - i * (h + 0.15)
    bio.label(ax, (0.3, y), name, size="small", ha="left")
    for j, txt in enumerate(cells):
        xc = x0 + j * w + w / 2
        if txt == "–":
            bio.label(ax, (xc, y), "–", size="normal", color=P.muted())
        else:
            bio.box(ax, (xc, y), w - 0.2, h - 0.1, tok, text=txt, size="small")
# brackets: mandibulate head and chelicerate prosoma
ax.plot([x0 + 3 * w + 0.1, x0 + 6 * w - 0.1], [0.75, 0.75], color=P.muted(), lw=1.0)
bio.label(ax, (x0 + 4.5 * w, 0.4), "Mandibulata: mandible on segment 4", size="tiny", color=P.muted())
ax.plot([x0 + 1 * w + 0.1, x0 + 3 * w - 0.1], [0.75, 0.75], color=P.muted(), lw=1.0)
bio.label(ax, (x0 + 2 * w, 0.4), "Chelicerata: no antennae", size="tiny", color=P.muted())
