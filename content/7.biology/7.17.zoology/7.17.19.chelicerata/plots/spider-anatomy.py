# Internal anatomy of a female spider (lateral view, anterior to the left), from a public-domain
# Wikimedia template. Prosoma: simple eyes, chelicerae with venom glands; opisthosoma, joined by the narrow
# pedicel: the tubular heart, the branched midgut diverticula that fill most of it, the ovary, a book lung
# in front and silk glands opening on the spinnerets behind.
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(20, 10.5)
s = AM.Specimen("wikimedia/spider-internal", at=(10, 5.4), width=14.0)
# note: in this template the part named "malpighian-tubule" is the book lung with its lamellae
s.draw(ax, parts={"heart": "blood", "digestive-tubules": "golgi", "silk-gland": "positive", "malpighian-tubule": "channel",
                  "venom-gland": "drug", "ovary": "ovary", "simple-eye": "dna", "spinneret": "protein"}, mute="neutral")
sx, sy, sw, sh = s.box
AM.callouts(ax, [(s.point("simple-eye"), "Simple eyes", "left"),
                 (s.point("venom-gland"), "Venom gland", "left"),
                 (s.point("malpighian-tubule"), "Book lung", "left"),
                 (s.frac(0.69, 0.88), "Heart", "right"),
                 (s.point("digestive-tubules"), "Midgut diverticula", "right"),
                 (s.point("ovary"), "Ovary", "right"),
                 (s.point("silk-gland"), "Silk glands", "right"),
                 (s.point("spinneret"), "Spinnerets", "right")],
            left=sx - 0.2, right=sx + sw + 0.2, gap=0.55)
AM.bracket(ax, (sx + 0.06 * sw, sy - 0.3), (sx + 0.43 * sw, sy - 0.3), "Prosoma", side=-1, depth=0.22)
AM.bracket(ax, (sx + 0.47 * sw, sy - 0.3), (sx + 0.99 * sw, sy - 0.3), "Opisthosoma", side=-1, depth=0.22)
