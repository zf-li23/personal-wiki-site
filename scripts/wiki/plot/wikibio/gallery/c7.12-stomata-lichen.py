# Demo: stomata (types, open/closed), epidermal peels, lichen sections, extra inflorescences (wikibio.botany).
import wikibio as bio
from wikibio import botany as B

fig, ax = bio.canvas(26, 20)
types = ["anomocytic", "anisocytic", "paracytic", "diacytic", "tetracytic", "actinocytic"]
for i, t in enumerate(types):
    s = B.stoma(ax, (2 + i * 3.6, 18.2), 1.6, subsidiary=t, state="open")
    bio.label(ax, (2 + i * 3.6, 16.6), t.capitalize(), size="small")
s = B.stoma(ax, (23.5, 18.6), 1.6, state="closed")
bio.label(ax, (23.5, 17.6), "Closed", size="small")
g = B.stoma(ax, (2, 15), 2.0, kind="dumbbell", state="open")
B.stoma(ax, (5.5, 15), 2.0, kind="dumbbell", state="closed")
bio.callout(ax, g["subsidiary"][0], (1, 16.3), "Subsidiary cell")
bio.callout(ax, g["guard"][1], (7.6, 14.0), "Guard cell")
e1 = B.epidermis(ax, (0.5, 8.5, 8.5, 13.5), kind="eudicot", stomata=6)
e2 = B.epidermis(ax, (9.0, 8.5, 17.0, 13.5), kind="monocot", stomata=2, subsidiary="paracytic")
e3 = B.epidermis(ax, (17.5, 8.5, 25.5, 13.5), kind="grass", stomata=2)
bio.callout(ax, e1["pavement"], (3, 14.2), "Pavement cell")
L = B.lichen_section(ax, (0.5, 0.5, 12.5, 7.5))
for k, y in [("upper_cortex", 7.2), ("algal_layer", 6.2), ("medulla", 4.6), ("lower_cortex", 3.0), ("rhizine", 1.4)]:
    bio.callout(ax, L[k], (13.3, y), k.replace("_", " ").capitalize())
B.lichen_section(ax, (17.5, 4.6, 25.5, 7.5), kind="homoiomerous")
for i, k in enumerate(["compound spike", "pleiochasium", "verticillaster", "hypanthodium"]):
    B.inflorescence(ax, (18 + i * 2.2, 0.4), 3.6, kind=k)
