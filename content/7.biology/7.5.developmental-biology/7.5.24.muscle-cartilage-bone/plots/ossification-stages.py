"""Endochondral ossification of a long bone in seven stages (longitudinal sections, proximal up)."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(25.8, 9.2)
P = bio.P
stages = ("condensation", "cartilage", "hypertrophy", "collar", "primary", "secondary", "mature")
names = ("Condensation", "Cartilage model", "Hypertrophy", "Bone collar", "Primary centre", "Secondary centres",
         "Growth complete")
for k, st in enumerate(stages):
    x = 1.9 + k * 3.55
    a = M.ossification(ax, (x, 4.6), 6.4, st)
    bio.label(ax, (x - 1.5, 8.6), "ABCDEFG"[k], bold=True, ha="left")
    bio.label(ax, (x, 0.65), names[k], size="small")
    if st == "cartilage":
        bio.callout(ax, a["perichondrium"], (x + 1.4, 7.9), "Perichondrium")
    if st == "collar":
        bio.callout(ax, a["collar"], (x + 1.5, 2.0), "Bone collar")
    if st == "primary":
        bio.callout(ax, a["vessel"], (x + 1.4, 3.0), "Vessel")
        bio.callout(ax, a["marrow"], (x - 0.4, 1.5), "Marrow")
    if st == "secondary":
        bio.callout(ax, a["secondary"], (x + 1.0, 8.4), "Secondary centre")
        bio.callout(ax, a["growth_plate"], (x + 1.6, 6.9), "Growth plate")
