# Neutral buoyancy of a chambered shell, Eq. (14.2) (model). rho_t = 1.06, rho_w = 1.026 g/cm3.
# A: gas volume / tissue volume needed for neutral buoyancy against shell volume / tissue volume, for three
# shell densities. B: weight in water of an animal with 1 kg of tissue (shell 10% of tissue volume, chamber
# volume 25% larger than needed when empty) against the fraction of the chambers filled with liquid.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
rt, rw = 1.06, 1.026
fig, ax = bio.canvas(24, 9.6)

bio.panel(ax, "A", (0.2, 9.4))
pa = quant.Plot(ax, (2.2, 1.6, 8.6, 6.8), (0, 0.3), (0, 0.6), xlabel="Shell volume / tissue volume",
                ylabel="Gas volume / tissue volume", xticks=[0, 0.1, 0.2, 0.3], yticks=[0, 0.2, 0.4, 0.6])
s = np.linspace(0, 0.3, 100)
for rs, tok, at in ((2.2, "dna2", 0.85), (2.6, "dna", 0.7), (2.9, "protein", 0.55)):
    g = ((rt - rw) + (rs - rw) * s) / rw
    pa.line(s, g, token=tok, lw=1.8, text=f"ρ$_s$ = {rs}", at=at)
g10 = ((rt - rw) + (2.6 - rw) * 0.1) / rw
pa.points([0.1], [g10], token="dna", r=0.1)
pa.text(0.105, g10 - 0.05, f"{g10:.2f}", size="tiny", color=P.muted(), ha="left")

bio.panel(ax, "B", (12.4, 9.4))
Vt = 1.0 / rt * 1000            # cm3 of tissue for 1 kg
Vs = 0.1 * Vt
Vg = 1.25 * ((rt - rw) * Vt + (2.6 - rw) * Vs) / rw
f = np.linspace(0, 1, 100)
mass = rt * Vt + 2.6 * Vs + f * Vg * rw   # liquid assumed to have the density of seawater
W = mass - rw * (Vt + Vs + Vg)          # grams-force: positive = sinks
pb = quant.Plot(ax, (14.6, 1.6, 8.6, 6.8), (0, 1), (-60, 200), xlabel="Fraction of chambers filled with liquid",
                ylabel="Weight in water / g", xticks=[0, 0.25, 0.5, 0.75, 1.0], yticks=[-50, 0, 50, 100, 150, 200])
pb.hline(0, dashed=True, text="neutral", side="right")
pb.line(f, W, token="negative", lw=2.0)
pb.text(0.25, -45, "floats", size="tiny", color=P.muted(), ha="left")
pb.text(0.45, 150, "sinks", size="tiny", color=P.muted(), ha="left")
f0 = float(np.interp(0, W, f))
pb.points([f0], [0], token="negative", r=0.1)
pb.text(f0 + 0.03, 12, f"neutral at {f0:.2f}", size="tiny", color=P.muted(), ha="left")
