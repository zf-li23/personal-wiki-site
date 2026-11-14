# Vision calibrates the auditory space map of the barn owl (schematic after Knudsen and Brainard 1991;
# Brainard and Knudsen 1998; illustrative data). In the optic tectum each site has a visual receptive
# field and a best interaural time difference; normally best ITD changes by about 2.2 us per degree of
# azimuth. Juvenile owls reared with prisms that shift the visual field 23 deg to the right develop
# best ITDs shifted to match the displaced visual field (about 50 us); owls first fitted as adults
# shift little. A: tectal sites; B: time course of the shift.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
slope, shift = 2.2, 23.0
fig, ax = bio.canvas(23, 9.4)

pa = quant.Plot(ax, (2.2, 1.8, 8.4, 6.4), xlim=(-40, 40), ylim=(-140, 140),
                xlabel="Azimuth of visual receptive field (through prisms) / deg",
                ylabel="Best ITD of tectal site / µs", xticks=[-40, -20, 0, 20, 40], yticks=[-100, -50, 0, 50, 100])
az = np.linspace(-40, 40, 9)
for lab, s, tok in (("normal", 0.0, "neutral"), ("prisms from adulthood", 0.25 * shift, "channel"),
                    ("prisms from youth", shift, "receptor")):
    x = rng.uniform(-30, 22, 16)
    y = slope * (x + s) + rng.normal(0, 8, x.size)
    p_line = slope * (az + s)
    pa.points(x, y, tok, r=0.08)
    pa.line(az, p_line, tok, lw=1.4)
pa.legend([("normal", "neutral", "-"), ("prisms fitted to adults", "channel", "-"),
           ("prisms fitted to juveniles", "receptor", "-")], at=(2.8, 7.8), step=0.42)
bio.label(ax, (6.4, 8.9), "A  Auditory tuning aligns with the displaced visual field", size="small", bold=True)

pb = quant.Plot(ax, (14.0, 1.8, 8.0, 6.4), xlim=(0, 200), ylim=(0, 60), xlabel="Days with prisms",
                ylabel="Shift of best ITD / µs", xticks=[0, 50, 100, 150, 200], yticks=[0, 20, 40, 60])
t = np.linspace(0, 200, 200)
pb.line(t, slope * shift * (1 - np.exp(-t / 35)), "receptor", text="juvenile", at=0.35, dy=-0.45)
pb.line(t, 0.25 * slope * shift * (1 - np.exp(-t / 50)), "channel", text="adult", at=0.7, dy=0.25)
pb.hline(slope * shift, token="muted", text="full compensation of 23°", side="right")
bio.label(ax, (18.0, 8.9), "B  Time course", size="small", bold=True)
