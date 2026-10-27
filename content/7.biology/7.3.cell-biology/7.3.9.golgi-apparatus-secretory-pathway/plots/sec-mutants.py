# Ordering the secretory pathway with yeast sec mutants (Novick, Field and Schekman 1980; Novick, Ferro and
# Schekman 1981). At the restrictive temperature (37 C) each temperature-sensitive mutant stops secreting
# invertase and acid phosphatase and accumulates the membrane compartment just before its block: ER (class B,
# e.g. sec12, sec13, sec16, sec17, sec18, sec23), Golgi-like Berkeley bodies (sec7, sec14) or 80-100 nm
# secretory vesicles (class A, e.g. sec1, sec2, sec4, sec6, sec8, sec15). In double mutants the compartment
# of the earlier block accumulates (epistasis), which orders the steps ER -> Golgi -> vesicles -> plasma
# membrane. Molecular identities found later are given beside the genes.
import wikibio as bio

fig, ax = bio.canvas(22, 8.6)
P = bio.P
steps = [("ER", "er", 2.0), ("Golgi", "golgi", 8.0), ("Secretory\nvesicles", "vesicle", 14.0), ("Cell surface\n(invertase out)", "extracellular", 20.0)]
y = 6.6
for name, tok, x in steps:
    bio.box(ax, (x, y), 3.2, 1.2, token=tok if tok != "extracellular" else "neutral", text=name, size="small")
blocks = [(5.0, "ER → Golgi blocked", "accumulate ER",
           "sec12 (Sar1 GEF), sec13, sec23 (COPII),\nsec16 (exit-site scaffold), sec17 (α-SNAP),\nsec18 (NSF), sec22 (SNARE)"),
          (11.0, "Golgi exit blocked", "accumulate Golgi\n(Berkeley bodies)", "sec7 (Arf GEF), sec14\n(PI/PC transfer protein)"),
          (17.0, "Fusion with plasma\nmembrane blocked", "accumulate vesicles",
           "sec4 (Rab), sec2 (Sec4 GEF), sec1 (SM),\nsec6, sec8, sec15 (exocyst), sec9 (SNARE)")]
for x, title, acc, genes in blocks:
    bio.arrow(ax, (x - 1.25, y), (x + 1.25, y), kind="process")
    ax.plot([x - 0.3, x + 0.3], [y - 0.55, y + 0.55], color=P.edge("negative"), lw=3)
    ax.plot([x - 0.3, x + 0.3], [y + 0.55, y - 0.55], color=P.edge("negative"), lw=3)
    bio.label(ax, (x, y + 1.15), title, size="tiny", va="bottom")
    bio.label(ax, (x, y - 1.0), acc, size="tiny", va="top", color=P.edge("negative"))
    bio.label(ax, (x, y - 2.0), genes, size="tiny", va="top", italic=True)
# epistasis table
bio.label(ax, (1.0, 2.3), "Double mutant", size="small", bold=True, ha="left")
bio.label(ax, (8.5, 2.3), "Accumulates", size="small", bold=True, ha="left")
bio.label(ax, (13.5, 2.3), "Conclusion", size="small", bold=True, ha="left")
rows = [("ER-class × vesicle-class (e.g. sec18 sec1)", "ER", "the ER step precedes vesicle fusion"),
        ("Golgi-class × vesicle-class (sec7 sec1)", "Golgi", "Golgi exit precedes vesicle fusion"),
        ("ER-class × Golgi-class (sec18 sec7)", "ER", "ER exit precedes Golgi exit")]
for k, (a, b, c) in enumerate(rows):
    yy = 1.6 - 0.55 * k
    bio.label(ax, (1.0, yy), a, size="tiny", ha="left")
    bio.label(ax, (8.5, yy), b, size="tiny", ha="left")
    bio.label(ax, (13.5, yy), c, size="tiny", ha="left")
