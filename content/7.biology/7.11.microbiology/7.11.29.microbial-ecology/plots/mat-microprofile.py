"""Chemical microprofiles in a phototrophic microbial mat by day and by night (reaction-diffusion model).

One-dimensional steady state over depth z (mm, positive downward; z < 0 is the diffusive boundary layer of
the overlying water, where only diffusion acts). Both O2 and H2S diffuse with D = 1.5e-3 mm2 s-1. Rates in
micromolar per second:
  oxygenic photosynthesis (day only) P = 7 I/(I + 0.15) in the top 1 mm, light I = exp(-z / 0.5 mm);
  aerobic respiration (0.3 + 1.2 by day or 0.6 by night in the top 1.2 mm) * O/(O + 3);
  chemical and biological sulfide oxidation by O2, 0.05 O S (2 O2 per H2S);
  sulfate reduction 0.08 below 0.3 mm, inhibited by O2, 1/(1 + O/2);
  sulfide oxidation by anoxygenic phototrophs (day only) 6 I S/(S + 10)/(1 + O/2).
Boundaries: O2 = 250 uM (air-saturated water) and H2S = 0 in the water above; at 5 mm, no O2 flux and
H2S = 600 uM supplied from the sediment below. The steady state is found by implicit time stepping.
"""
import numpy as np
from scipy.linalg import solve_banded

import wikibio as bio
from wikibio import quant

P = bio.P
D, Ow, Sb = 1.5e-3, 250.0, 600.0
z = np.linspace(-0.4, 5.0, 271)
h, n = z[1] - z[0], z.size


def sm(x, w=0.05):
    return 0.5 * (1 + np.tanh(x / w))


inmat = sm(z)
light = np.exp(-np.clip(z, 0, None) / 0.5)


def rates(O, S, day):
    photo = 7.0 * light / (light + 0.15) * sm(1.0 - z, 0.1) * inmat if day else 0 * z
    kres = (0.3 + (1.2 if day else 0.6) * sm(1.2 - z, 0.1)) / (O + 3) * inmat
    srr = 0.08 * sm(z - 0.3, 0.1) * inmat / (1 + O / 2)
    kph = 6.0 * light / (S + 10) / (1 + O / 2) * inmat if day else 0 * z
    return photo, kres, srr, kph


def solve(day, dt=20.0, steps=6000):
    O = Ow * np.exp(-np.clip(z, 0, None))
    S = Sb * np.clip(z / 5, 0, 1)
    a = D * dt / h ** 2
    for _ in range(steps):
        photo, kres, srr, kph = rates(O, S, day)
        for which in (0, 1):
            ab = np.zeros((3, n))
            ab[0, 1:], ab[2, :-1] = -a, -a
            if which == 0:
                ab[1] = 1 + 2 * a + dt * (kres + 2 * 0.05 * S)
                rhs = O + dt * photo
                ab[2, -2] = -2 * a
                rhs[0] = Ow
            else:
                ab[1] = 1 + 2 * a + dt * (0.05 * O + kph)
                rhs = S + dt * srr
                ab[1, -1], ab[2, -2], rhs[-1] = 1, 0, Sb
                rhs[0] = 0.0
            ab[1, 0], ab[0, 1] = 1, 0
            new = np.clip(solve_banded((1, 1), ab, rhs), 0, None)
            if which == 0:
                O = new
            else:
                S = new
    return O, S


fig, ax = bio.canvas(26.0, 11.0)
zmax = 4.0
ybot, H = 1.3, 8.6
for k, (day, title) in enumerate([(True, "Day (light)"), (False, "Night (dark)")]):
    O, S = solve(day)
    x0 = 2.2 + k * 8.6
    bio.panel(ax, "AB"[k], (x0 - 2.0, 10.8))
    pl = quant.Plot(ax, (x0, ybot, 6.0, H), xlim=(0, 1200), ylim=(zmax, -0.4), xlabel="concentration / µM",
                    ylabel="depth / mm" if k == 0 else None, xticks=[0, 300, 600, 900, 1200],
                    yticks=[0, 1, 2, 3, 4], grid=True)
    pl.hline(0, token="muted", dashed=True, text="mat surface", side="left")
    if day:
        pl.line(light * 1000, z, "highlight", lw=1.2, dashed=True)
    pl.line(O, z, "dna", lw=1.9)
    pl.line(S, z, "atp", lw=1.9)
    bio.label(ax, (x0 + 3.0, ybot + H + 0.45), title, size="small", bold=True)
    if k == 0:
        pl.legend([("O₂", "dna", "-"), ("H₂S", "atp", "-"), ("light (relative)", "highlight", "--")],
                  at=(x0 + 3.4, ybot + 1.6))
    zo = z[np.argmax(z * (O > 1))]
    pl.hline(zo, token="dna", dashed=True, lw=0.7)
    pl.text(1180, zo + 0.15, f"O₂ penetration {zo:.1f} mm", ha="right", va="top", token="dna")

# C: process rates by day ---------------------------------------------------------------------------
O, S = solve(True)
photo, kres, srr, kph = rates(O, S, True)
x0 = 19.4
bio.panel(ax, "C", (x0 - 1.6, 10.8))
pl = quant.Plot(ax, (x0, ybot, 5.8, H), xlim=(0, 7.5), ylim=(zmax, -0.4), xlabel="rate / (µM s⁻¹)",
                xticks=[0, 2.5, 5, 7.5], yticks=[0, 1, 2, 3, 4], grid=True)
pl.line(photo, z, "plant", lw=1.8)
pl.line(kres * O, z, "enzyme", lw=1.6)
pl.line(0.05 * O * S, z, "neutral", lw=1.6)
pl.line(10 * kph * S, z, "receptor", lw=1.6)
pl.line(10 * srr, z, "atp", lw=1.6, dashed=True)
bio.label(ax, (x0 + 2.9, ybot + H + 0.45), "Process rates by day", size="small", bold=True)
pl.legend([("oxygenic photosynthesis", "plant", "-"), ("aerobic respiration", "enzyme", "-"),
           ("H₂S + O₂", "neutral", "-"), ("anoxygenic photosynthesis (×10)", "receptor", "-"),
           ("sulfate reduction (×10)", "atp", "--")], at=(x0 + 1.9, ybot + 1.8))
