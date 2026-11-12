# Model: the share of oxygen uptake through the skin in a bimodal (skin + lung) breather. Cutaneous uptake
# is limited by diffusion and scales with skin area, ~ M^(2/3), almost independent of temperature
# (Q10 ~ 1.2); metabolic demand scales as M^0.75 with Q10 = 2.2. Skin share = min(1, c*M^(2/3) Q10s^(T/10)
# / (M^0.75 Q10m^(T/10))), with c chosen so that a 10 g animal at 15 C takes half its oxygen through the
# skin. Schematic model, not a fit to data; the observed values of particular species are given in the text.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 8.5)
M = np.logspace(-1, 4.5, 300)  # g


def share(m, T, c):
    return np.minimum(1.0, c * m ** (2 / 3) * 1.2 ** (T / 10) / (m ** 0.75 * 2.2 ** (T / 10)))


c = 0.5 / share(10.0, 15, 1.0)
p = quant.Plot(ax, (1.8, 1.4, 8.6, 6.0), xlim=(-1, 4.5), ylim=(0, 1.05), xlabel="log10 body mass / g",
               ylabel="share of O2 uptake via skin", xticks=[-1, 0, 1, 2, 3, 4], yticks=[0, 0.25, 0.5, 0.75, 1.0])
for T, tok in ((5, "dna"), (15, "metabolite"), (25, "negative")):
    p.line(np.log10(M), share(M, T, c), tok, text=f"{T} °C", at=0.75)
bio.panel(ax, "A", (0.4, 8.1))

T = np.linspace(0, 30, 200)
q = quant.Plot(ax, (13.4, 1.4, 8.0, 6.0), xlim=(0, 30), ylim=(0, 1.05), xlabel="temperature / °C",
               ylabel="share of O2 uptake via skin", xticks=[0, 10, 20, 30], yticks=[0, 0.25, 0.5, 0.75, 1.0])
for m, tok in ((1, "lipid"), (100, "dna")):
    q.line(T, share(m, T, c), tok, text=f"{m} g", at=0.7)
q.text(1.0, 0.12, "lungless salamanders: 100 % (no lungs)", size="tiny", ha="left")
bio.panel(ax, "B", (12.2, 8.1))
