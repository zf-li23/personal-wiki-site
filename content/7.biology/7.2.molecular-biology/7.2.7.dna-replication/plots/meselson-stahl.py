# The Meselson-Stahl experiment computed for the three models of replication. Each row is a CsCl
# equilibrium density gradient after g generations in 14N medium, drawn as the absorbance profile:
# Gaussian bands of equal width at the buoyant densities of heavy (1.724), hybrid (1.717) and light
# (1.710 g/mL) DNA, with areas proportional to the amount of DNA (discrete generations).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(19, 11.6)

RHO_L, RHO_H = 1.710, 1.724
SIG = 0.00075
rho = np.linspace(1.703, 1.731, 600)
gens = [0, 1, 2, 3, 4]


def band(center, amount):
    return amount * np.exp(-0.5 * ((rho - center) / SIG) ** 2)


def profile(model, g):
    if model == "conservative":
        heavy = 2.0 ** (-g)
        return band(RHO_H, heavy) + band(RHO_L, 1 - heavy)
    if model == "semiconservative":
        if g == 0:
            return band(RHO_H, 1.0)
        hyb = 2.0 ** (1 - g)
        return band(0.5 * (RHO_H + RHO_L), hyb) + band(RHO_L, 1 - hyb)
    # dispersive: every duplex carries the same heavy fraction 2^-g
    return band(RHO_L + (RHO_H - RHO_L) * 2.0 ** (-g), 1.0)


models = [("conservative", "Conservative"), ("semiconservative", "Semiconservative (observed)"),
          ("dispersive", "Dispersive")]
x0s = [2.2, 7.9, 13.6]
w, h, top = 5.0, 1.55, 9.9
for col, (key, title) in enumerate(models):
    x0 = x0s[col]
    bio.label(ax, (x0 + w / 2, top + 1.1), title, size="normal", bold=True)
    for r, g in enumerate(gens):
        y0 = top - (r + 1) * (h + 0.32)
        last = r == len(gens) - 1
        p = quant.Plot(ax, (x0, y0, w, h), xlim=(rho[0], rho[-1]), ylim=(0, 1.15), frame=None,
                       xticks=[(RHO_L, "1.710"), (0.5 * (RHO_L + RHO_H), "1.717"), (RHO_H, "1.724")] if last else None,
                       xlabel="Buoyant density / (g mL⁻¹)" if last else None)
        ax.plot([x0, x0 + w], [y0, y0], color=P.muted(), lw=0.8, zorder=6)
        y = profile(key, g)
        ax.fill_between(p.X(rho), y0, p.Y(y), color=P.fill("dna"), lw=0, zorder=5)
        ax.plot(p.X(rho), p.Y(y), color=quant.line_color("dna"), lw=1.3, zorder=7)
        for c in (RHO_L, 0.5 * (RHO_L + RHO_H), RHO_H):
            ax.plot([p.X(c)] * 2, [y0, y0 + h], color=P.muted(), lw=0.5, ls=(0, (2, 2)), zorder=4)
        if col == 0:
            bio.label(ax, (0.9, y0 + h / 2), f"g = {g}", size="small", ha="center")
# light / hybrid / heavy names above the top row
for x0 in x0s:
    p = quant.Plot(ax, (x0, top - (h + 0.32), w, h), xlim=(rho[0], rho[-1]), ylim=(0, 1.15), frame=None)
    for c, t in ((RHO_L, "L/L"), (0.5 * (RHO_L + RHO_H), "H/L"), (RHO_H, "H/H")):
        bio.label(ax, (p.X(c), top + 0.35), t, size="tiny", color=P.muted())
bio.label(ax, (0.9, top + 1.1), "Generations", size="small", bold=True)
