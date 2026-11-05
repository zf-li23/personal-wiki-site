# Demo: fern sori and indusia, leptosporangium stages, conifer cone scales and strobili (wikibio.plant).
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(26, 18)
combos = [("round", None, "Round, naked"), ("round", "reniform", "Reniform indusium"), ("round", "peltate", "Peltate indusium"),
          ("linear", "linear", "Linear"), ("costal", "linear", "Costal"), ("marginal", "false", "Marginal, false indusium"),
          ("terminal", "cup", "Terminal, cup"), ("terminal", "false", "Terminal, false flaps"), ("acrostichoid", None, "Acrostichoid")]
for i, (s, ind, t) in enumerate(combos):
    x = 1.4 + i * 2.75
    a = plant.pinnule(ax, (x, 12.5), 4.6, angle=90, sorus=s, indusium=ind)
    bio.label(ax, (x, 12.0), t, size="tiny")
for i, st in enumerate(["closed", "open", "ejected"]):
    l = plant.leptosporangium(ax, (2.5 + i * 4.2, 8.5), 2.6, stage=st)
    bio.label(ax, (2.5 + i * 4.2, 6.1), st.capitalize(), size="small")
bio.callout(ax, l["annulus"], (14, 10.5), "Annulus")
bio.callout(ax, l["stomium"], (6.5, 10.7), "Stomium")
plant.cone_scale(ax, (15.5, 6.5), 3.2, "ovulate", view="adaxial")
plant.cone_scale(ax, (18, 6.5), 3.2, "ovulate", view="adaxial", seeds=True)
s = plant.cone_scale(ax, (19.6, 8.2), 3.4, "ovulate", view="section", angle=20)
for k, xy in [("bract", (21, 6.8)), ("ovule", (20.5, 11)), ("micropyle", (18.8, 10.6)), ("scale", (24, 10.5))]:
    bio.callout(ax, s[k], xy, k.capitalize())
plant.cone_scale(ax, (24, 6.5), 2.4, "pollen", view="abaxial")
plant.cone_scale(ax, (24.6, 10.8), 1.8, "pollen", view="section", angle=0)
for i, k in enumerate(plant.CONES):
    plant.cone(ax, (1.6 + i * 3.1, 0.3), 4.6, kind=k)
    bio.label(ax, (1.5 + i * 3.2, 0.1), k, size="tiny")
for i, k in enumerate(["seed", "pollen", "lycopod", "equisetum"]):
    plant.cone(ax, (17.5 + i * 2.4, 0.3), 4.5, kind=k, section=False)
