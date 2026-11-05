# Demo: floral formulae (Chinese style), diagrams generated from formulae, life-cycle types (wikibio.plant).
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(28, 22)
formulae = [("* K5 C5 A∞ G_(5:5:2)", "Malus-like"), ("↑ K(5) C1+2+(2) A(9)+1 G_1", "Pea"), ("* P3+3 A3+3 G_(3:3:∞)", "Lily"),
            ("* K4 C4 A2+4 G_(2:2:∞)", "Mustard"), ("* K(5) [C(5) A5] G_(2:2:∞)", "Nightshade"), ("* K5 C5 A∞ G∞", "Buttercup")]
for i, (f, name) in enumerate(formulae):
    x = 2.4 + (i % 3) * 4.6
    y = 19.2 - (i // 3) * 6.2
    plant.floral_diagram_from_formula(ax, (x, y), 1.5, f)
    plant.floral_formula(ax, (x, y - 2.7), f, size="normal", style="cn")
    bio.label(ax, (x, y - 3.3), name, size="small")
plant.floral_formula(ax, (21, 20.5), "* K5 C(5) A5 G^(2:1:∞)", style="cn")
plant.floral_formula(ax, (21, 19.3), "* K5 C(5) A5 G^(2:1:∞)")
bio.label(ax, (21, 18.3), plant.floral_formula_tex("* K5 C(5) A5 G^(2:1:∞)").replace("\\", "/"), size="tiny")
for i, k in enumerate(["haplontic", "diplontic", "haplodiplontic"]):
    plant.life_cycle(ax, (4.8 + i * 9.0, 4.6), 2.6, kind=k, gap=0.2)
    bio.label(ax, (4.8 + i * 9.0, 0.4), k.capitalize(), size="title", bold=True)
plant.life_cycle(ax, (24.0, 13.3), 2.5, kind="triphasic", gap=0.2, size="small")
