"""Catabolism and anabolism coupled through ATP and NAD(P)H.

Left: the three stages of catabolism converge (I: macromolecules hydrolyzed to building blocks;
II: building blocks degraded to acetyl-CoA; III: citric acid cycle and oxidative phosphorylation,
ending in CO2, H2O and NH3). Right: anabolism diverges from a few precursors to the macromolecules
of the cell. Centre: the energy released by catabolism is carried as ATP and as reducing power
(NADH, NADPH) to biosynthesis and other work, which return ADP + Pi and NAD(P)+."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.0, 12.6)

# --- catabolism (left, converging) -----------------------------------------------------------------
bio.label(ax, (4.6, 12.15), "Catabolism (converging)", size="title", bold=True)
top = [("Proteins", 1.6), ("Polysaccharides", 4.6), ("Lipids", 7.6)]
mid = [("Amino acids", 1.6), ("Hexoses", 4.6), ("Fatty acids,\nglycerol", 7.6)]
for (t, x) in top:
    bio.box(ax, (x, 10.9), 2.6, 0.8, "protein", t, size="small")
for (t, x), (t2, _) in zip(top, mid):
    bio.box(ax, (x, 8.7), 2.6, 0.95 if "\n" in t2 else 0.8, "metabolite", t2, size="small")
    bio.arrow(ax, (x, 10.45), (x, 9.25), kind="process")
bio.box(ax, (4.6, 6.3), 2.8, 0.8, "highlight", "Acetyl-CoA", size="small")
for (_, x) in mid:
    bio.arrow(ax, (x, 8.15), (4.6 + (x - 4.6) * 0.25, 6.75), kind="process")
bio.box(ax, (4.6, 4.3), 3.4, 0.8, "mitochondrion", "Citric acid cycle", size="small")
bio.arrow(ax, (4.6, 5.85), (4.6, 4.75), kind="process")
bio.box(ax, (4.6, 2.4), 4.0, 0.8, "mitochondrion", "Oxidative phosphorylation", size="small")
bio.arrow(ax, (4.6, 3.85), (4.6, 2.85), kind="process")
bio.label(ax, (5.15, 3.35), "NADH, FADH₂", size="tiny", ha="left", color=P.muted())
bio.box(ax, (4.6, 0.7), 3.6, 0.75, "neutral", "CO₂ + H₂O + NH₃", size="small")
bio.arrow(ax, (4.6, 1.95), (4.6, 1.12), kind="process")
for y, t in ((9.8, "Stage I"), (7.5, "Stage II"), (3.3, "Stage III")):
    bio.label(ax, (0.1, y), t, size="small", bold=True, ha="left", color=P.muted())

# --- anabolism (right, diverging) ------------------------------------------------------------------
bio.label(ax, (17.6, 12.15), "Anabolism (diverging)", size="title", bold=True)
bio.box(ax, (17.6, 2.2), 5.4, 1.15, "highlight", "Precursors: pyruvate, acetyl-CoA,\ncycle intermediates, ribose 5-P", size="small")
blocks = [("Amino acids", 14.6), ("Sugars", 17.6), ("Fatty acids,\nnucleotides", 20.6)]
macro = [("Proteins", 14.6), ("Polysaccharides", 17.6), ("Lipids,\nnucleic acids", 20.6)]
for (t, x) in blocks:
    bio.box(ax, (x, 6.3), 2.6, 0.95 if "\n" in t else 0.8, "metabolite", t, size="small")
    bio.arrow(ax, (17.6 + (x - 17.6) * 0.3, 2.8), (x, 5.8), kind="process")
for (t, x) in macro:
    bio.box(ax, (x, 10.0), 2.6, 0.95 if "\n" in t else 0.8, "protein", t, size="small")
    bio.arrow(ax, (x, 6.8), (x, 9.5), kind="process")

# --- the two currencies (centre) -------------------------------------------------------------------
cx = 11.1
bio.box(ax, (cx, 9.2), 2.2, 0.85, "atp", "ATP", size="normal")
bio.box(ax, (cx, 6.4), 2.2, 0.85, "neutral", "ADP + Pᵢ", size="normal")
bio.box(ax, (cx, 4.4), 2.4, 0.85, "enzyme", "NAD(P)H", size="normal")
bio.box(ax, (cx, 1.7), 2.4, 0.85, "neutral", "NAD(P)⁺", size="normal")
# regeneration by catabolism (left side of the loops, upward) and use by anabolism (right, downward)
bio.arrow(ax, (cx - 0.7, 6.85), (cx - 0.7, 8.75), kind="process", bend=-0.25)
bio.arrow(ax, (cx + 0.7, 8.75), (cx + 0.7, 6.85), kind="process", bend=-0.25)
bio.arrow(ax, (cx - 0.7, 2.15), (cx - 0.7, 3.95), kind="process", bend=-0.25)
bio.arrow(ax, (cx + 0.7, 3.95), (cx + 0.7, 2.15), kind="process", bend=-0.25)
# energy flow from catabolism and to anabolism
bio.arrow(ax, (6.7, 4.3), (cx - 1.25, 7.4), kind="activation", dashed=True)
bio.arrow(ax, (6.7, 2.6), (cx - 1.4, 2.9), kind="activation", dashed=True)
bio.arrow(ax, (cx + 1.25, 7.6), (13.2, 7.5), kind="activation", dashed=True)
bio.arrow(ax, (cx + 1.4, 3.0), (14.8, 3.0), kind="activation", dashed=True)
bio.label(ax, (7.3, 6.4), "energy\nconserved", size="tiny", color=P.muted())
bio.label(ax, (cx + 2.35, 8.65), "energy for\nbiosynthesis", size="tiny", color=P.muted())
bio.label(ax, (cx, 11.0), "Chemical, osmotic and\nmechanical work", size="small", color=P.ink())
bio.arrow(ax, (cx, 9.65), (cx, 10.45), kind="activation", dashed=True)
bio.label(ax, (cx + 2.5, 2.35), "reductive\nbiosynthesis", size="tiny", color=P.muted())
