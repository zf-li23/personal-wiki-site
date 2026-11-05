"""Main fruit types. Row 1, fleshy fruits: berry (kiwifruit, cross-section), hesperidium (citrus,
cross-section), drupe (longitudinal section), pome (apple, longitudinal section). Row 2, dry fruits:
legume, loculicidal capsule (three carpels, from above), samara (maple double samara), caryopsis
(grass grain, section), achene. Row 3, aggregate and multiple fruits: strawberry (achenes on a fleshy
receptacle), raspberry (aggregate of drupelets), pineapple (multiple fruit).
"""
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(25.0, 19.0)


def name(x, y, title, sub):
    bio.label(ax, (x, y), title, size="normal", bold=True)
    bio.label(ax, (x, y - 0.55), sub, size="small", color=P.muted())


row1, row2, row3 = 15.0, 8.9, 2.9
bio.label(ax, (0.3, 18.5), "Fleshy fruits", size="title", ha="left")
bio.icon(ax, "wikimedia/fruit-berry-kiwi", at=(3.2, row1 + 0.4), height=3.6)
name(3.2, row1 - 2.0, "Berry", "kiwifruit")
PM.fruit(ax, (9.3, row1 + 0.4), 3.6, kind="hesperidium")
name(9.3, row1 - 2.0, "Hesperidium", "citrus")
bio.icon(ax, "wikimedia/fruit-drupe", at=(15.5, row1 + 0.4), height=3.6)
name(15.5, row1 - 2.0, "Drupe", "peach type")
bio.icon(ax, "wikimedia/fruit-pome-apple", at=(21.6, row1 + 0.4), height=3.6)
name(21.6, row1 - 2.0, "Pome", "apple")

bio.label(ax, (0.3, 12.0), "Dry fruits", size="title", ha="left")
bio.icon(ax, "wikimedia/fruit-legume-pod", at=(2.9, row2 + 0.5), width=4.4)
name(2.9, row2 - 1.6, "Legume", "dehiscent, one carpel")
PM.fruit(ax, (8.0, row2 + 0.5), 2.8, kind="capsule")
name(8.0, row2 - 1.6, "Capsule", "dehiscent, fused carpels")
PM.fruit(ax, (12.9, row2 + 0.5), 3.4, kind="samara")
name(12.9, row2 - 1.6, "Samara", "winged, indehiscent")
PM.fruit(ax, (17.6, row2 + 0.5), 2.6, kind="caryopsis")
name(17.6, row2 - 1.6, "Caryopsis", "pericarp fused to seed")
PM.fruit(ax, (22.2, row2 + 0.5), 2.6, kind="achene")
name(22.2, row2 - 1.6, "Achene", "pericarp free from seed")

bio.label(ax, (0.3, 6.0), "Aggregate and multiple fruits", size="title", ha="left")
bio.icon(ax, "wikimedia/fruit-accessory-strawberry", at=(4.5, row3 + 0.3), height=3.0)
name(4.5, row3 - 1.75, "Aggregate of achenes", "strawberry: fleshy receptacle")
bio.icon(ax, "wikimedia/fruit-aggregate-rubus", at=(12.5, row3 + 0.3), height=3.0)
name(12.5, row3 - 1.75, "Aggregate of drupelets", "raspberry")
bio.icon(ax, "wikimedia/fruit-multiple-pineapple", at=(20.5, row3 + 0.5), height=3.6)
name(20.5, row3 - 1.75, "Multiple fruit", "pineapple")
