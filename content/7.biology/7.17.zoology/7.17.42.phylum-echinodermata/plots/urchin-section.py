# Regular sea urchin in vertical section (Wikimedia template "Sea Urchin Anatomy.svg"), parts highlighted and labelled.
import wikibio as bio

fig, ax = bio.canvas(18.0, 9.6)
ID = "wikimedia/sea-urchin-section"
kw = dict(at=(9.0, 4.8), height=8.6)
bio.icon(ax, "wikimedia/sea-urchin-section", **kw)
pt = lambda part, where="center": bio.icon_part(ID, part, where=where, **kw)
bio.callout(ax, (4.75, 4.9), (1.2, 7.6), "Test (stereom plates)")
bio.callout(ax, pt("tube-foot", "left"), (1.0, 2.0), "Tube feet")
bio.callout(ax, pt("water-vascular"), (16.8, 7.9), "Water vascular system")
bio.callout(ax, pt("aristotles-lantern"), (15.8, 0.6), "Aristotle's lantern")
bio.callout(ax, pt("intestine"), (16.8, 3.6), "Intestine")
bio.callout(ax, pt("gonad"), (2.0, 9.2), "Gonad")
