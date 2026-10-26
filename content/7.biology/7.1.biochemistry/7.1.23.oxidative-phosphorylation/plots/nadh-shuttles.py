"""Shuttles for cytosolic NADH (the outer membrane is freely permeable, so the cytosol reaches the inner membrane).
(A) Malate-aspartate shuttle (liver, kidney, heart): cytosolic malate dehydrogenase reduces oxaloacetate with
NADH; malate enters the matrix on the malate-alpha-ketoglutarate antiporter and is reoxidized by matrix malate
dehydrogenase, regenerating NADH for Complex I; oxaloacetate returns as aspartate (aspartate aminotransferase,
AAT, on both sides) on the glutamate-aspartate antiporter. Reversible; about 2.5 ATP per cytosolic NADH.
(B) Glycerol 3-phosphate shuttle (skeletal muscle, brain): cytosolic glycerol 3-phosphate dehydrogenase reduces
dihydroxyacetone phosphate; the mitochondrial isozyme, a flavoprotein on the outer face of the inner membrane,
passes the electrons via FAD to ubiquinone, bypassing Complex I. Irreversible; about 1.5 ATP per NADH."""

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(21.0, 9.6)
y = 4.6
be.inner_membrane(ax, (0.3, 11.4), y, ims=4.0, matrix=4.0, ims_text="Cytosol", matrix_text="Matrix")
be.inner_membrane(ax, (12.0, 20.7), y, ims=4.0, matrix=4.0, ims_text="Cytosol", matrix_text="Matrix")
bio.panel(ax, "A", (0.1, 9.5))
bio.panel(ax, "B", (11.8, 9.5))

# ---- A: malate-aspartate -----------------------------------------------------------------------------
pw = M.Pathway(ax, size="tiny")
pw.node("mal_c", (3.0, 6.7), "Malate")
pw.node("oaa_c", (5.9, 7.9), "Oxaloacetate")
pw.node("asp_c", (8.8, 6.7), "Aspartate")
pw.node("mal_m", (3.0, 2.5), "Malate")
pw.node("oaa_m", (5.9, 1.3), "Oxaloacetate")
pw.node("asp_m", (8.8, 2.5), "Aspartate")
pw.step("oaa_c", "mal_c", enzyme="MDH", side=("NADH + H⁺", "NAD⁺"), reversible=True, side_reach=0.5)
pw.step("asp_c", "oaa_c", enzyme="AAT", side=("α-KG", "Glu"), reversible=True, side_reach=0.5, flip=True)
pw.step("mal_m", "oaa_m", enzyme="MDH", side=("NAD⁺", "NADH + H⁺"), reversible=True, side_reach=0.5, flip=True)
pw.step("oaa_m", "asp_m", enzyme="AAT", side=("Glu", "α-KG"), reversible=True, side_reach=0.5)
be.carrier(ax, 3.0, y, token="metabolite", width=0.8)
be.carrier(ax, 8.8, y, token="metabolite", width=0.8)
ink = P.ink()
bio.arrow(ax, (3.0, 6.3), (3.0, 2.9), kind="process", color=ink, head=0.16)
bio.arrow(ax, (3.55, 3.2), (3.55, 6.0), kind="process", color=ink, head=0.16, dashed=True)
bio.label(ax, (3.7, 6.05), "α-KG", size="tiny", ha="left")
bio.arrow(ax, (8.8, 2.9), (8.8, 6.3), kind="process", color=ink, head=0.16)
bio.arrow(ax, (8.25, 6.0), (8.25, 3.2), kind="process", color=ink, head=0.16, dashed=True)
bio.label(ax, (8.1, 3.15), "Glu", size="tiny", ha="right")
bio.label(ax, (1.6, y + 0.85), "malate–α-KG\nantiporter", size="tiny", ha="center", color=P.muted())
bio.label(ax, (10.3, y + 0.85), "Glu–Asp\nantiporter", size="tiny", ha="center", color=P.muted())
bio.label(ax, (0.8, 9.2), "matrix NADH → Complex I (≈ 2.5 ATP)", size="tiny", bold=True, ha="left")

# ---- B: glycerol 3-phosphate ---------------------------------------------------------------------------
pb = M.Pathway(ax, size="tiny")
pb.node("dhap", (13.9, 7.7), "DHAP")
pb.node("g3p", (18.6, 7.7), "Glycerol 3-P")
pb.step("dhap", "g3p", enzyme="cytosolic G3PDH", side=("NADH + H⁺", "NAD⁺"), side_reach=0.55)
enz = (16.25, y + be.MH + 0.5)
bio.protein(ax, enz, 2.9, 0.85, token="enzyme", text="mitochondrial G3PDH", size="tiny")
bio.molecule(ax, (16.25, y + be.MH + 0.05), token="highlight", text="FAD", r=0.24, zorder=14)
bio.arrow(ax, (18.4, 7.35), (17.45, y + be.MH + 0.75), kind="process", color=P.ink(), head=0.16, bend=-0.15)
bio.arrow(ax, (15.05, y + be.MH + 0.75), (14.1, 7.35), kind="process", color=P.ink(), head=0.16, bend=-0.15)
q = be.ubiquinone(ax, (16.25, y - 0.05), reduced=True, label_dy=0.55)
be.electron_arrow(ax, (16.25, y + be.MH - 0.2), (16.25, y + 0.2), lw=1.3, head=0.14)
be.electron_arrow(ax, (16.95, y - 0.05), (19.9, y - 0.05), lw=1.3)
bio.label(ax, (20.0, y - 0.6), "→ Complex III", size="tiny", ha="right")
bio.label(ax, (12.5, 9.2), "electrons enter at Q, bypassing Complex I (≈ 1.5 ATP)", size="tiny", bold=True, ha="left")
