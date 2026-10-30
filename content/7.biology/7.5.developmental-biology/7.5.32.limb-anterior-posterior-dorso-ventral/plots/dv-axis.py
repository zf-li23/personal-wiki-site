"""The dorso-ventral axis of the limb (schematic sections through the bud along the proximo-distal and
dorso-ventral axes; dorsal up, distal right). A: wild type: Wnt7a in the dorsal ectoderm induces Lmx1b in the dorsal
mesenchyme; Engrailed-1 in the ventral ectoderm represses Wnt7a there; the AER sits at their boundary. B: Wnt7a
mutant: no Lmx1b, ventral structures on both sides (double-ventral paw, footpads on the dorsum), and reduced
posterior Shh. C: En1 mutant: Wnt7a and Lmx1b are expressed ventrally as well, giving double-dorsal distal
structures (and a ventrally widened AER). D: integration of the axes: AER-FGF, ZPA-Shh and dorsal Wnt7a maintain
one another.
"""

import wikibio as bio
from wikibio import limbdev as LD

P = bio.P
fig, ax = bio.canvas(30.0, 9.0)
cases = [("A", "Wild type", dict(), "dorsal and ventral distinct"),
         ("B", "Wnt7a –/–", dict(dorsal="(no Wnt7a)", mes="none", dorsal_token="dna", ventral="En1"), "double ventral"),
         ("C", "En1 –/–", dict(ventral="Wnt7a", mes="both", ventral_token="receptor"), "double dorsal")]
for k, (lt, title, kw, res) in enumerate(cases):
    x0 = 0.8 + 7.3 * k
    bio.panel(ax, lt, (x0 - 0.5, 8.8))
    bio.label(ax, (x0 + 2.7, 8.4), title, size="small", bold=True, italic=(k > 0))
    s = LD.bud_section(ax, (x0 + 0.3, 4.6), 5.0, 4.0, **kw)
    bio.label(ax, (x0 + 2.7, 1.2), res, size="small", color=P.muted())
    if k == 0:
        bio.callout(ax, s["aer"], (x0 + 6.2, 6.6), "AER", size="tiny")
bio.panel(ax, "D", (22.4, 8.8))
N = {"fgf": (24.6, 6.6, "AER-FGF", "ectoderm"), "shh": (28.0, 6.6, "ZPA-Shh", "protein"), "wnt": (26.3, 3.2, "Wnt7a", "receptor")}
for kk, (x, y, t, tk) in N.items():
    bio.box(ax, (x, y), 2.6, 0.95, tk, t, size="small")
bio.arrow(ax, (25.95, 6.8), (26.65, 6.8), kind="activation", lw=1.0)
bio.arrow(ax, (26.65, 6.4), (25.95, 6.4), kind="activation", lw=1.0)
bio.arrow(ax, (26.6, 3.7), (27.6, 6.1), kind="activation", lw=1.0)
bio.label(ax, (26.3, 1.8), "dorsal ectoderm", size="tiny", color=P.muted())
