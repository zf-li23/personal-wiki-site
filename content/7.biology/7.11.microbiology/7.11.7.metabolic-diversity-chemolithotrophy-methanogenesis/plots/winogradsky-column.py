"""The Winogradsky column as a redox gradient: schematic and a one-dimensional reaction-diffusion model.

A: a column of mud enriched with cellulose (shredded paper), CaSO4 and CaCO3 under water, incubated in the
light for weeks. From the top: algae and cyanobacteria in the oxic water; colourless sulfur oxidizers
(Beggiatoa, Thiobacillus) where O2 and H2S meet; purple and then green sulfur bacteria in the anoxic,
sulfidic, illuminated zone (purple nonsulfur bacteria between); below, fermenters, sulfate reducers
(black FeS) and methanogens.
B: steady state of a dimensionless model on depth z in [0, 1] (top to bottom):
O2'' = 2 k O S + q O/(K + O) e^(-z/0.3)        (sulfide oxidation by O2, aerobic respiration near the top)
S''  = k O S + a e^(-z/lambda) S/((Ks + S)(1 + O/0.01)) (sulfide oxidation by O2 and by anoxygenic phototrophs)
with O = 1 at the top (air-saturated water, about 0.25 mM), no O2 flux at the bottom, sulfide S = 2 at the
bottom (supplied by sulfate reduction) and no sulfide flux at the top; k = 3000, q = 0.5, K = 0.05, a = 5,
lambda = 0.5 (light attenuation length), Ks = 0.1. Curves: O2 and sulfide (each scaled to its maximum),
light, and the two sulfide-consuming rates, which locate the colourless sulfur bacteria at the oxic-anoxic
interface and the phototrophs below it.
"""
import numpy as np
from scipy.integrate import solve_bvp

import wikibio as bio
from wikibio import quant

P = bio.P
k, q, K, a, lam, Ks, Sb, zr = 3000.0, 0.5, 0.05, 5.0, 0.5, 0.1, 2.0, 0.3


def f(z, y):
    O, dO, S, dS = y
    O = np.clip(O, 0, None)
    S = np.clip(S, 0, None)
    r = k * O * S
    resp = q * O / (K + O) * np.exp(-z / zr)
    ph = a * np.exp(-z / lam) * S / (Ks + S) / (1 + O / 0.01)
    return np.vstack([dO, 2 * r + resp, dS, r + ph])


def bc(ya, yb):
    return np.array([ya[0] - 1, yb[1], ya[3], yb[2] - Sb])


z = np.linspace(0, 1, 400)
y0 = np.zeros((4, z.size))
y0[0] = np.clip(1 - z / 0.3, 0, 1)
y0[2] = Sb * z
sol = solve_bvp(f, bc, z, y0, max_nodes=100000, tol=1e-4)
O, S = np.clip(sol.sol(z)[0], 0, None), np.clip(sol.sol(z)[2], 0, None)
light = np.exp(-z / lam)
r_ox = k * O * S
r_ph = a * light * S / (Ks + S) / (1 + O / 0.01)

fig, ax = bio.canvas(24.0, 14.0)

# A: schematic column -----------------------------------------------------------------------------
bio.panel(ax, "A", (0.3, 13.8))
x0, w, ytop, ybot = 2.0, 3.4, 12.4, 1.0
H = ytop - ybot


def Yc(zz):
    return ytop - zz * H


z_int = z[np.argmax(r_ox)]
z_ph = z[np.argmax(r_ph * (O < 0.01))]
layers = [  # (z0, z1, token, label)
    (0.00, 0.12, "extracellular", "water: algae, cyanobacteria"),
    (0.12, z_int - 0.03, "enzyme", "cyanobacteria, aerobic heterotrophs"),
    (z_int - 0.03, z_int + 0.03, "neutral", "colourless sulfur oxidizers (O₂ + H₂S)"),
    (z_int + 0.03, z_int + 0.08, "receptor", "purple nonsulfur bacteria"),
    (z_int + 0.08, z_int + 0.18, "protein", "purple sulfur bacteria"),
    (z_int + 0.18, z_int + 0.28, "plant", "green sulfur bacteria"),
    (z_int + 0.28, 1.00, "animal", "fermenters, sulfate reducers (FeS),\nmethanogens"),
]
for z0, z1, tok, txt in layers:
    bio.box(ax, (x0 + w / 2, (Yc(z0) + Yc(z1)) / 2), w, Yc(z0) - Yc(z1), token=tok, radius=0.0, zorder=4)
    bio.label(ax, (x0 + w + 0.3, (Yc(z0) + Yc(z1)) / 2), txt, size="tiny", ha="left")
ax.plot([x0, x0, x0 + w, x0 + w], [ytop + 0.5, ybot, ybot, ytop + 0.5], color=P.ink(), lw=1.4, zorder=6)
bio.label(ax, (x0 + w / 2, ytop + 0.9), "light", size="small", color=P.edge("highlight"))
bio.arrow(ax, (x0 + w / 2, ytop + 0.65), (x0 + w / 2, ytop - 0.1), kind="process", color=P.edge("highlight"), lw=1.6)
bio.arrow(ax, (x0 - 0.5, ytop - 0.3), (x0 - 0.5, Yc(z_int) + 0.2), kind="process", color=P.edge("dna"))
bio.label(ax, (x0 - 0.7, (ytop + Yc(z_int)) / 2), "O₂", size="small", ha="right", color=P.edge("dna"))
bio.arrow(ax, (x0 - 0.5, ybot + 0.3), (x0 - 0.5, Yc(z_int) - 0.2), kind="process", color=P.edge("atp"))
bio.label(ax, (x0 - 0.7, (ybot + Yc(z_int)) / 2), "H₂S", size="small", ha="right", color=P.edge("atp"))

# B: model ----------------------------------------------------------------------------------------
bio.panel(ax, "B", (14.2, 13.8))
pl = quant.Plot(ax, (16.0, ybot, 7.2, H), xlim=(0, 1.05), ylim=(1, 0), xlabel="relative value",
                ylabel="depth (relative)", xticks=[0, 0.5, 1], yticks=[0, 0.25, 0.5, 0.75, 1], grid=True)
pl.line(O, z, "dna", lw=1.8)
pl.line(S / S.max(), z, "atp", lw=1.8)
pl.line(light, z, "highlight", lw=1.2, dashed=True)
pl.line(r_ox / r_ox.max(), z, "neutral", lw=1.6)
pl.line(r_ph / r_ph.max(), z, "plant", lw=1.6)
pl.legend([("O₂", "dna", "-"), ("H₂S", "atp", "-"), ("light", "highlight", "--"),
           ("H₂S oxidation by O₂", "neutral", "-"), ("H₂S oxidation by phototrophs", "plant", "-")], at=(10.4, 3.0))
