"""The six cell movements of gastrulation (grey arrows: direction of movement). Invagination: a region of an
epithelial sheet folds inwards (sea urchin vegetal plate, Drosophila ventral furrow). Involution: an
expanding sheet rolls over a lip and spreads on the inner surface of the outer layer (amphibian marginal
zone at the blastopore). Epiboly: a sheet thins and spreads to cover deeper layers or the yolk (amphibian
animal cap, fish blastoderm). Ingression: single cells leave an epithelium and move inside as mesenchyme
(sea urchin primary mesenchyme, amniote primitive streak). Delamination: one sheet splits into two roughly
parallel sheets (hypoblast of birds and mammals). Convergent extension: cells intercalate, and the tissue
narrows in one direction and lengthens in the perpendicular one (seen from above)."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(24, 11.4)
kinds = [("invagination", "Invagination"), ("involution", "Involution"), ("epiboly", "Epiboly"),
         ("ingression", "Ingression"), ("delamination", "Delamination"), ("convergent-extension", "Convergent extension")]
for k, (kind, name) in enumerate(kinds):
    x = 4.0 + 8.0 * (k % 3)
    y = 8.4 if k < 3 else 3.0
    E.sheet(ax, (x, y), 5.2, kind)
    bio.label(ax, (x, y - 2.6), name, size="normal", bold=True)
