# Fruit types. A fruit is a ripened ovary (with any accessory parts); its wall, the pericarp, may be
# fleshy or dry and is often divided into exocarp, mesocarp and endocarp. Simple fleshy fruits (from one
# pistil): drupe (stony endocarp, peach), berry (fleshy throughout, many seeds, kiwifruit), pome (the
# fleshy part is the floral cup or receptacle around a papery core of five carpels, apple), hesperidium
# (leathery rind, segments filled with juice hairs, citrus). Simple dry fruits: dehiscent legume (one
# carpel opening along two sutures, pea) and capsule (several carpels, here loculicidal), indehiscent
# achene (one seed free from the thin pericarp; a cypsela in Asteraceae), samara (winged; maple has a
# pair) and caryopsis (pericarp fused with the seed coat, grasses). Compound fruits: aggregate (many
# pistils of one flower: drupelets of raspberry), accessory aggregate (achenes on a swollen receptacle,
# strawberry) and multiple fruits (the fused ovaries of a whole inflorescence, pineapple).
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(31.0, 19.9)
TOP = 19.3
CW, CH = 6.0, 5.6
X0 = 1.0


def cell(col, row):
    return (X0 + (col + 0.5) * CW, TOP - 0.9 * (row + 1) - (row + 0.5) * CH)


def title(c, name, note):
    bio.label(ax, (c[0], c[1] - CH / 2 + 1.25), name, size="normal", bold=True)
    bio.label(ax, (c[0], c[1] - CH / 2 + 0.88), note, size="tiny", color=P.muted())


for row, text in enumerate(("Simple fleshy fruits", "Simple dry fruits", "Compound fruits")):
    y = TOP - row * (CH + 0.9)
    bio.label(ax, (0.4, y - 0.15), text, size="title", bold=True, ha="left")
    if row:
        ax.plot([0.4, 30.6], [y + 0.45, y + 0.45], color=P.muted(), lw=0.6)

# ---- simple fleshy ---------------------------------------------------------------------------------
c = cell(0, 0)
PM.specimen(ax, "wikimedia/fruit-drupe", at=(c[0] - 0.4, c[1] + 0.45), height=3.4, right=c[0] + 1.75, gap=0.5, labels=[
    dict(at=(0.93, 0.6), text="Exocarp", side="right"),
    dict(at=(0.78, 0.4), text="Mesocarp", side="right"),
    dict(at=(0.62, 0.45), text="Endocarp (stone)", side="right"),
    dict(at=(0.52, 0.55), text="Seed", side="right"),
], size="tiny")
title(c, "Drupe", "peach (Prunus persica)")
c = cell(1, 0)
PM.specimen(ax, "wikimedia/fruit-berry-kiwi", at=(c[0] - 0.4, c[1] + 0.45), height=3.4, right=c[0] + 1.75, gap=0.5, labels=[
    dict(part="skin", text="Exocarp", side="right", where="right"),
    dict(at=(0.8, 0.35), text="Fleshy pericarp", side="right"),
    dict(part="seed", text="Seeds", side="right"),
    dict(at=(0.5, 0.5), text="Columella", side="right"),
], size="tiny")
title(c, "Berry", "kiwifruit (Actinidia), cross-section")
c = cell(2, 0)
PM.specimen(ax, "wikimedia/fruit-pome-apple", at=(c[0] - 0.4, c[1] + 0.45), height=3.4, right=c[0] + 1.75, gap=0.5, labels=[
    dict(at=(0.85, 0.45), text="Receptacle (flesh)", side="right"),
    dict(at=(0.62, 0.62), text="Core (pericarp)", side="right"),
    dict(part="seed", text="Seed", side="right"),
    dict(part="calyx", text="Calyx remnant", side="right", where="bottom"),
], size="tiny")
title(c, "Pome", "apple (Malus), longitudinal section")
c = cell(3, 0)
a = PM.fruit(ax, (c[0] - 0.4, c[1] + 0.45), 3.2, kind="hesperidium")
PM.callouts(ax, [(a["flavedo"], "Flavedo", "right"), (a["albedo"], "Albedo", "right"), (a["vesicle"], "Juice vesicles", "right"),
                 (a["seed"], "Seed", "right")], right=c[0] + 1.75, gap=0.5, size="tiny")
title(c, "Hesperidium", "orange (Citrus), cross-section")

# ---- simple dry --------------------------------------------------------------------------------------
c = cell(0, 1)
PM.specimen(ax, "wikimedia/fruit-legume-pod", at=(c[0] - 0.3, c[1] + 0.6), width=3.8, right=c[0] + 2.0, labels=[
    dict(at=(0.6, 0.75), text="Pericarp (pod)", side="right")], size="tiny")
bio.label(ax, (c[0], c[1] - 0.6), "opens along two sutures", size="tiny", color=P.muted())
title(c, "Legume", "pea (Pisum), dehiscent")
c = cell(1, 1)
a = PM.fruit(ax, (c[0] - 0.4, c[1] + 0.45), 3.0, kind="capsule")
PM.callouts(ax, [(a["valve"], "Valve (carpel wall)", "right"), (a["locule"], "Locule", "right"), (a["seed"], "Seed", "right")],
            right=c[0] + 1.65, gap=0.5, size="tiny")
title(c, "Capsule", "3 carpels, loculicidal, dehiscent")
c = cell(2, 1)
a = PM.fruit(ax, (c[0] - 0.4, c[1] + 0.45), 3.4, kind="achene")
PM.callouts(ax, [(a["pericarp"], "Pericarp", "right"), (a["seed"], "Seed", "right")], right=c[0] + 1.4, gap=0.5, size="tiny")
title(c, "Achene", "sunflower (Helianthus), indehiscent")
c = cell(3, 1)
a = PM.fruit(ax, (c[0], c[1] + 0.75), 3.0, kind="samara")
PM.callouts(ax, [(a["wing"], "Wing", "right"), (a["nutlet"], "Seed (nutlet)", "right")], right=c[0] + 1.9, gap=0.5, size="tiny")
title(c, "Samara", "maple (Acer), indehiscent")
c = cell(4, 1)
a = PM.fruit(ax, (c[0] - 0.3, c[1] + 0.45), 3.2, kind="caryopsis")
PM.callouts(ax, [(a["pericarp"], "Pericarp + seed coat", "right"), (a["endosperm"], "Endosperm", "right"), (a["embryo"], "Embryo", "left")],
            left=c[0] - 1.9, right=c[0] + 1.3, gap=0.5, size="tiny")
title(c, "Caryopsis", "maize (Zea), grain")

# ---- compound ----------------------------------------------------------------------------------------
c = cell(0, 2)
PM.specimen(ax, "wikimedia/fruit-aggregate-rubus", at=(c[0], c[1] + 0.5), width=4.6, left=c[0] - 2.75, gap=0.5, labels=[
    dict(at=(0.2, 0.75), text="Drupelet", side="left"),
    dict(part="sepal", text="Calyx", side="left", where="left"),
    dict(part="seed", text="Drupelet in section", side="right"),
], right=c[0] + 2.75, size="tiny")
title(c, "Aggregate", "raspberry (Rubus): drupelets")
c = cell(1, 2)
PM.specimen(ax, "wikimedia/fruit-accessory-strawberry", at=(c[0], c[1] + 0.5), width=4.2, right=c[0] + 2.7, left=c[0] - 2.7,
            gap=0.5, labels=[dict(at=(0.3, 0.45), text="Receptacle", side="right"),
                             dict(part="achene", text="Achene", side="right", where="right")], size="tiny")
title(c, "Accessory aggregate", "strawberry (Fragaria)")
c = cell(2, 2)
PM.specimen(ax, "wikimedia/fruit-multiple-pineapple", at=(c[0], c[1] + 0.8), height=3.6, right=c[0] + 2.75, left=c[0] - 2.75, gap=0.5,
            labels=[dict(part="bract", text="Crown of bracts", side="right", where="right"),
                    dict(at=(0.15, 0.4), text="Fruitlets", side="left"), dict(part="axis", text="Axis", side="right")], size="tiny")
title(c, "Multiple", "pineapple (Ananas): whole inflorescence")
