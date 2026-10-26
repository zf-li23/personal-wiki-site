"""The biological nitrogen cycle, with each species placed at the oxidation number of its nitrogen.

Nitrogen fixation (nitrogenase) reduces N2 to NH3. Assimilation incorporates NH4+ into organic nitrogen
(glutamine and glutamate), and ammonification returns it. Nitrification oxidizes NH3 through hydroxylamine
to nitrite and nitrate (ammonia- and nitrite-oxidizing bacteria and archaea). Assimilatory nitrate
reduction (plants, algae, fungi, bacteria) reduces nitrate to nitrite and NH4+ with 2 + 6 electrons.
Denitrification uses nitrate as an electron acceptor in anaerobic respiration and returns nitrogen to the
atmosphere through NO and N2O. Anammox bacteria oxidize NH4+ with nitrite through hydrazine to N2.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 15.0, scale=0.42)


def Y(ox):
    return 2.0 + 1.45 * (ox + 3)


ax.plot([1.2, 1.2], [Y(-3) - 0.5, Y(5) + 0.5], color=P.muted(), lw=0.9)
for ox in range(-3, 6):
    ax.plot([1.05, 1.35], [Y(ox), Y(ox)], color=P.muted(), lw=0.9)
    bio.label(ax, (0.85, Y(ox)), f"{ox:+d}" if ox else "0", size="tiny", ha="right", color=P.muted())
bio.label(ax, (1.2, Y(5) + 1.0), "oxidation number\nof N", size="tiny", color=P.muted())

nodes = {"org": (4.0, Y(-3), "organic N\n(amino acids)"), "nh4": (9.0, Y(-3), "NH₄⁺ / NH₃"),
         "nh2oh": (12.5, Y(-1), "NH₂OH"), "n2h4": (17.5, Y(-2), "N₂H₄"), "n2": (18.5, Y(0), "N₂"),
         "n2o": (22.0, Y(1), "N₂O"), "no": (22.0, Y(2), "NO"), "no2": (12.5, Y(3), "NO₂⁻"),
         "no3": (9.0, Y(5), "NO₃⁻")}
for k, (x, y, t) in nodes.items():
    bio.box(ax, (x, y), 2.4 if k != "org" else 3.0, 0.9 if k != "org" else 1.2,
            "metabolite" if k != "n2" else "highlight", text=t, size="small")


def pt(k, dx=0.0, dy=0.0):
    x, y, _ = nodes[k]
    return (x + dx, y + dy)


FIX, NIT, DEN, ANA, ASM = "positive", "enzyme", "negative", "dna", "plant"


def go(a, b, tok, bend=0.0, dashed=False):
    bio.arrow(ax, a, b, kind="process", color=P.edge(tok), lw=1.8, bend=bend, dashed=dashed)


go(pt("n2", -1.0, -0.5), pt("nh4", 1.3, 0.3), FIX, bend=-0.15)
go(pt("nh4", 0.6, 0.5), pt("nh2oh", -0.6, -0.5), NIT)
go(pt("nh2oh", 0, 0.5), pt("no2", 0, -0.5), NIT)
go(pt("no2", -0.9, 0.5), pt("no3", 0.6, -0.5), NIT, bend=-0.12)
go(pt("no3", 1.2, -0.25), pt("no2", 1.0, 0.5), DEN, bend=-0.2)
go(pt("no2", 1.25, 0.0), pt("no", -1.25, 0.1), DEN)
go(pt("no", 0, -0.5), pt("n2o", 0, 0.5), DEN)
go(pt("n2o", -0.6, -0.5), pt("n2", 0.7, 0.5), DEN)
go(pt("no2", 0.6, -0.5), pt("n2h4", -0.6, 0.5), ANA, bend=0.1)
go(pt("nh4", 1.25, 0.15), pt("n2h4", -1.25, -0.1), ANA)
go(pt("n2h4", 0.4, 0.5), pt("n2", -0.2, -0.5), ANA)
go(pt("no3", -0.4, -0.5), pt("nh4", -0.4, 0.5), ASM, dashed=True)
go(pt("nh4", -1.25, 0.2), pt("org", 1.55, 0.2), ASM)
go(pt("org", 1.55, -0.3), pt("nh4", -1.25, -0.3), "neutral")

lab = [((21.8, Y(-0.85)), "fixation (nitrogenase):\nN₂ + 8 e⁻ + 16 ATP → 2 NH₃ + H₂", FIX),
       ((11.0, Y(-2.1)), "nitrification", NIT), ((11.8, Y(4.2)), "nitrification", NIT),
       ((15.6, Y(3.35)), "denitrification", DEN), ((16.4, Y(-2.7)), "anammox", ANA),
       ((8.2, Y(1.0)), "assimilatory\nnitrate reduction\n(8 e⁻)", ASM),
       ((6.5, Y(-3) + 0.85), "assimilation (GS–GOGAT)", ASM), ((6.5, Y(-3) - 0.85), "ammonification", "neutral")]
for xy, t, tok in lab:
    bio.label(ax, xy, t, size="tiny", bold=True, color=P.edge(tok), ha="right" if "nitrate" in t else "center")
