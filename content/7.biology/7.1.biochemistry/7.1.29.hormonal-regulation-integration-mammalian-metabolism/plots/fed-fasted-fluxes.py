"""Fuel fluxes between organs in the well-fed and the fasted state.
A (well fed, insulin high, glucagon low): glucose and amino acids from the intestine reach the liver through the
portal vein; dietary fat travels as chylomicrons through the lymph to adipose tissue and muscle; the liver
stores glycogen, makes fatty acids and exports them as VLDL triacylglycerols to adipose tissue, and passes
glucose to the brain and to muscle, which takes it up through GLUT4 and stores glycogen.
B (fasting, glucagon high, insulin low): the liver releases glucose from glycogen and, after about a day, from
gluconeogenesis, using glycerol and fatty acids from adipose tissue, alanine, glutamine and lactate from muscle;
it oxidizes fatty acids and exports ketone bodies, which brain and muscle use alongside glucose and fatty acids."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 11.6)
ink = P.ink()


def flow(a, b, text, tok, bend=0.0, at=0.5, dx=0.0, dy=0.28, ha="center"):
    pts = bio.arrow(ax, a, b, kind="process", color=P.edge(tok), lw=2.0, head=0.24, bend=bend)
    m = pts[int(at * (len(pts) - 1))]
    bio.label(ax, (m[0] + dx, m[1] + dy), text, size="tiny", ha=ha, bold=True, color=P.edge(tok))


def organs(x0, gut=True):
    liver = (x0 + 6.0, 5.4)
    bio.icon(ax, "servier/liver", at=liver, height=2.2)
    bio.icon(ax, "servier/brain", at=(x0 + 6.0, 9.4), height=1.6)
    bio.icon(ax, "servier/muscle", at=(x0 + 10.4, 5.4), height=2.6)
    bio.icon(ax, "servier/adipose-tissue", at=(x0 + 1.6, 5.4), height=2.0)
    if gut:
        bio.icon(ax, "servier/small-intestine", at=(x0 + 6.0, 1.3), height=1.8)
    bio.label(ax, (x0 + 7.2, 9.4), "Brain", size="small", bold=True, ha="left")
    bio.label(ax, (x0 + 10.4, 3.7), "Muscle", size="small", bold=True)
    bio.label(ax, (x0 + 1.6, 3.9), "Adipose tissue", size="small", bold=True)
    return liver


# ---------- A: well fed ----------
bio.label(ax, (0.3, 11.1), "A  Well fed: insulin ↑, glucagon ↓", size="title", bold=True, ha="left")
liver = organs(0.0)
bio.label(ax, (4.5, 6.7), "Liver", size="small", bold=True)
bio.label(ax, (8.3, 4.6), "glycogen ↑, fatty acid\nsynthesis, VLDL", size="tiny", color=P.muted())
bio.label(ax, (7.2, 1.3), "Intestine", size="small", bold=True, ha="left")
flow((6.0, 2.3), (6.0, 4.4), "glucose,\namino acids", "carbohydrate", dx=0.25, dy=0.0, ha="left")
flow((5.0, 1.3), (1.6, 4.2), "chylomicrons\n(lymph)", "lipid", bend=-0.25, dx=-0.6, dy=0.0, ha="right")
flow((4.9, 5.0), (2.8, 5.0), "VLDL", "lipid", dy=-0.4)
flow((6.0, 6.6), (6.0, 8.5), "glucose", "carbohydrate", dx=0.25, dy=0.0, ha="left")
flow((7.1, 5.8), (9.2, 5.8), "glucose", "carbohydrate", dy=0.3)
flow((7.0, 1.5), (10.0, 4.2), "chylomicrons", "lipid", bend=0.25, dx=0.6, dy=-0.2, ha="left")
bio.label(ax, (10.4, 7.2), "GLUT4: glucose →\nglycogen; protein\nsynthesis", size="tiny", color=P.muted())
bio.label(ax, (1.6, 7.0), "LPL, TAG storage", size="tiny", color=P.muted())

# ---------- B: fasting ----------
X = 13.0
ax.plot([12.5, 12.5], [0.3, 11.2], color=P.muted(), lw=0.8, ls=":")
bio.label(ax, (X + 0.3, 11.1), "B  Fasting: glucagon ↑, insulin ↓", size="title", bold=True, ha="left")
liver = organs(X, gut=False)
bio.label(ax, (X + 7.6, 7.0), "Liver", size="small", bold=True)
bio.label(ax, (X + 6.0, 1.7), "liver: glycogenolysis,\ngluconeogenesis,\nβ oxidation, ketogenesis", size="tiny", color=P.muted())
flow((X + 2.8, 5.8), (X + 4.9, 5.8), "fatty acids,\nglycerol", "lipid", dy=0.45)
flow((X + 2.2, 3.4), (X + 9.8, 3.4), "fatty acids (albumin)", "lipid", bend=-0.25, dy=0.35)
flow((X + 9.2, 5.0), (X + 7.1, 5.0), "Ala, Gln,\nlactate", "protein", dy=-0.55)
flow((X + 5.6, 6.6), (X + 5.6, 8.5), "glucose", "carbohydrate", dx=-0.25, dy=0.0, ha="right")
flow((X + 6.4, 6.6), (X + 6.4, 8.5), "ketone\nbodies", "metabolite", dx=0.25, dy=0.0, ha="left")
flow((X + 7.1, 6.1), (X + 9.9, 6.3), "ketone bodies", "metabolite", dy=0.3)
bio.label(ax, (X + 10.6, 8.2), "uses fatty acids,\nketone bodies;\nproteolysis", size="tiny", color=P.muted())
bio.label(ax, (X + 1.6, 7.0), "lipolysis (ATGL, HSL)", size="tiny", color=P.muted())
bio.label(ax, (X + 6.0, 0.45), "kidney: gluconeogenesis, NH₄⁺ excretion\n(prolonged fasting)", size="tiny", color=P.muted())
