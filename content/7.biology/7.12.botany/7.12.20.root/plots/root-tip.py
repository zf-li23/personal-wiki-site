# Zones of the root tip (longitudinal section, tip down): root cap, meristematic zone (apical
# meristem with the quiescent centre), elongation zone and maturation zone (root hairs); lateral roots
# emerge further back. Template from bioicons (root longitudinal section), zones coloured.
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(16.0, 14.0)
s = PM.specimen(ax, "bioicons/root-longitudinal", at=(6.0, 7.0), height=13.0,
                parts={"root-cap": "highlight", "meristematic-zone": "negative", "elongation-zone": "channel",
                       "maturation-zone": "plant", "lateral-root": "plant"},
                labels=[dict(part="lateral-root", text="Lateral root emerging", side="right"),
                        dict(part="maturation-zone", text="Maturation zone (root hairs)", side="right"),
                        dict(part="elongation-zone", text="Elongation zone (2-5 mm)", side="right"),
                        dict(part="meristematic-zone", text="Meristematic zone (1-2 mm)", side="right"),
                        dict(part="root-cap", text="Root cap", side="right")], right=8.6)
