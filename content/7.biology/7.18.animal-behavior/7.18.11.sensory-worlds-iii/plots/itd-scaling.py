# Head size limits the interaural time difference: for a source on the interaural axis the maximum ITD
# is about d_eff / c (air, c = 343 m/s). Effective acoustic separations d_eff are computed from measured or
# estimated maximum ITDs: Ormia ochracea about 1.5 us (tympana 0.5 mm apart), field cricket about 30 us
# (about 1 cm, Bradbury and Vehrencamp), Mongolian gerbil about 135 us, barn owl about 200 us,
# human about 660 us, African elephant about 3 ms. Dotted lines: smallest ITDs discriminated
# behaviorally by humans (about 10 us) and by Ormia (about 50 ns, Mason et al. 2001).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
c = 343.0
SP = [("Ormia (fly)", 1.5e-6, "phylopic/horse-fly", "negative"),
      ("Cricket", 30e-6, "phylopic/cricket", "enzyme"),
      ("Gerbil", 135e-6, "phylopic/mouse", "channel"),
      ("Barn owl", 200e-6, "phylopic/owl", "protein"),
      ("Human", 660e-6, "phylopic/human", "receptor"),
      ("Elephant", 3e-3, "phylopic/african-elephant", "animal")]
fig, ax = bio.canvas(19, 10.4)
p = quant.Plot(ax, (2.4, 1.8, 15.0, 7.4), xlim=(1e-4, 2), ylim=(1e-8, 1e-2), xlog=True, ylog=True,
               xlabel="Effective separation of the ears d / m", ylabel="Maximum interaural time difference",
               xticks=[(1e-4, "0.1 mm"), (1e-3, "1 mm"), (1e-2, "1 cm"), (0.1, "10 cm"), (1, "1 m")],
               yticks=[(1e-8, "10 ns"), (1e-7, "100 ns"), (1e-6, "1 µs"), (1e-5, "10 µs"), (1e-4, "100 µs"),
                       (1e-3, "1 ms"), (1e-2, "10 ms")], ylabel_offset=1.6)
d = np.logspace(-4, np.log10(2), 100)
p.line(d, d / c, "ink", lw=1.2)
p.text(2.5e-3, 3e-6, "ITD = d / c", ha="left")
p.hline(10e-6, token="receptor", dashed=True, text="human threshold, 10 µs", side="right")
p.hline(50e-9, token="negative", dashed=True, text="Ormia threshold, 50 ns", side="right")
for name, itd, icon, tok in SP:
    x = itd * c
    p.points([x], [itd], tok, r=0.12)
    X, Y = p.xy(x, itd)
    dx = {"Gerbil": -0.9, "Barn owl": 0.2}.get(name, -0.25)
    bio.icon(ax, icon, at=(X + dx, Y + 0.75), height=0.6, width=0.8 if name in ("Gerbil", "Elephant", "Ormia (fly)") else None,
             color=tok)
    bio.label(ax, (X + 0.25, Y - 0.32), name, size="tiny", ha="left")
