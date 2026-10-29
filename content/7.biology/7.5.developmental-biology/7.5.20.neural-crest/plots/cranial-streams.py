"""Cranial neural crest streams and the Hox code of the pharyngeal arches (schematic lateral view, anterior left).
Crest from the midbrain and rhombomeres r1-r2 fills the frontonasal region and the first pharyngeal arch, crest
from r4 the second arch, crest from r6-r7 the third and fourth arches; r3 and r5 release few crest cells, which
join the neighbouring streams, so the streams stay separate. The crest carries a Hox code matching its origin: the
first arch is Hox-free, the second expresses Hoxa2 (and Hoxb2), the third and fourth add group 3 and 4 genes. The
code selects the skeletal derivatives: first arch, the jaws (Meckel's cartilage, maxilla, malleus and incus);
second arch, the stapes and hyoid; third and fourth arches, the rest of the hyoid and the laryngeal cartilages."""
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(22, 10.2)
P = bio.P
ne, nc = N.TISSUE["neural"], N.TISSUE["crest"]
# brain: forebrain, midbrain, rhombomeres
bio.box(ax, (1.7, 8.4), 2.4, 1.1, token=ne, text="Forebrain", size="small")
bio.box(ax, (4.4, 8.4), 2.6, 1.1, token=ne, text="Midbrain", size="small")
xs = {}
for k in range(7):
    x = 7.0 + k * 1.75
    xs[k + 1] = x
    bio.box(ax, (x, 8.4), 1.6, 1.1, token=ne, text=f"r{k + 1}", size="small")
ax.add_patch(__import__("matplotlib").patches.Ellipse((xs[5], 6.75), 1.1, 0.8, facecolor=P.fill(N.TISSUE["placode"]), edgecolor=P.edge(N.TISSUE["placode"]), lw=1.0))
bio.label(ax, (xs[5], 6.05), "otic vesicle", size="tiny", color=P.muted())
# pharyngeal arches
arches = [("PA1", 6.2, "Hox-free", "jaws: Meckel's cartilage, maxilla, malleus, incus"),
          ("PA2", 10.6, "Hoxa2, Hoxb2", "stapes, styloid, upper hyoid"),
          ("PA3", 14.2, "Hox group 3", "lower hyoid"),
          ("PA4", 17.4, "Hox group 4", "laryngeal cartilages")]
for k, (name, x, hox, derv) in enumerate(arches):
    bio.box(ax, (x, 3.6), 2.2, 2.4, token=nc, text=name, size="normal")
    bio.label(ax, (x, 2.0), hox, size="small", italic=True)
    for j, part in enumerate(derv.split(": ")[-1].split(", ")):
        bio.label(ax, (x, 1.45 - 0.42 * j), part, size="tiny", color=P.muted())
bio.box(ax, (2.4, 3.6), 2.6, 2.4, token=nc, text="Frontonasal", size="small")
bio.label(ax, (2.4, 2.0), "Hox-free", size="small", italic=True)
bio.label(ax, (2.4, 1.45), "nasal, frontal bones", size="tiny", color=P.muted())
crest = P.edge(nc)
for a, b in (((4.2, 7.8), (2.8, 4.85)), ((4.8, 7.8), (5.8, 4.85)), ((xs[1], 7.8), (6.3, 4.85)), ((xs[2], 7.8), (6.8, 4.85)),
             ((xs[4], 7.8), (10.6, 4.85)), ((xs[6], 7.8), (14.0, 4.85)), ((xs[7], 7.8), (17.2, 4.85))):
    bio.arrow(ax, a, b, kind="process", color=crest, lw=2.2, head=0.2)
for r in (3, 5):
    bio.label(ax, (xs[r], 7.5), "few crest", size="tiny", color=P.muted())
bio.label(ax, (11.0, 9.6), "Hindbrain rhombomeres", size="small", bold=True)
