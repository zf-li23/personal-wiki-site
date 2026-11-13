# The three vertebrate wings, left forelimb in dorsal view (shoulder at the top), bones in course-wide colours,
# membranes and feathers schematic. Pterosaur drawn with vertskel primitives (wing digit IV, pteroid); bird and bat
# from wikibio zoomorph.forelimb. After Witton (2013), Kardong (2019). Not to scale.
import wikibio as bio
import vertskel as vs
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(24, 11)
# pterosaur
o = (0.5, 0.5)
parts = [("humerus", vs.rod((2.0, 9.6), (2.4, 8.0), 0.45)),
         ("radius", vs.rod((2.3, 7.9), (2.9, 5.6), 0.22)), ("ulna", vs.rod((2.6, 7.9), (3.2, 5.6), 0.25)),
         ("carpals", vs.oval((3.1, 5.3), 0.35, 0.25)),
         ("radials", vs.rod((2.9, 5.3), (1.8, 6.4), 0.12), {"text": None}),
         ("metacarpals", vs.rod((3.2, 5.1), (3.6, 3.9), 0.2))]
for k in range(3):
    parts.append(("phalanges", vs.rod((3.4 + 0.15 * k, 4.0), (3.2 + 0.25 * k, 3.4), 0.08)))
wf = [(3.6, 3.9), (4.4, 2.4), (5.0, 1.0), (5.4, 0.1), (5.6, -0.3)]
for a_, b_ in zip(wf[:-1], wf[1:]):
    parts.append(("phalanges", vs.rod((a_[0], a_[1] + 0.5), (b_[0], b_[1] + 0.5), 0.16)))
memb = [(2.2, 9.0), (3.0, 5.6), (3.6, 4.4), (4.4, 2.9), (5.0, 1.5), (5.6, 0.2), (1.4, 2.0), (0.6, 6.5), (1.2, 9.0)]
bio.shape(ax, [(o[0] + x, o[1] + y) for x, y in memb], token="neutral", alpha=0.6, zorder=2, lw=0.8)
a = vs.draw(ax, parts, at=o)
vs.callout(ax, (o[0] + 4.8, o[1] + 1.7), (o[0] + 6.3, o[1] + 3.0), "digit IV (wing finger)")
vs.callout(ax, (o[0] + 2.3, o[1] + 5.9), (o[0] + 0.2, o[1] + 9.9), "pteroid")
bio.label(ax, (o[0] + 3.2, 10.6), "Pterosaur", size="small", bold=True)
# bird and bat
zm.forelimb(ax, (11.5, 5.3), 9.0, taxon="bird", width=3.0)
bio.label(ax, (11.5, 10.6), "Bird", size="small", bold=True)
bio.label(ax, (11.5, 0.3), "feathers on ulna and hand", size="tiny", color=P.muted())
zm.forelimb(ax, (19.0, 5.3), 9.0, taxon="bat", width=6.0)
bio.label(ax, (19.0, 10.6), "Bat", size="small", bold=True)
bio.label(ax, (19.0, 0.3), "membrane on digits II-V", size="tiny", color=P.muted())
