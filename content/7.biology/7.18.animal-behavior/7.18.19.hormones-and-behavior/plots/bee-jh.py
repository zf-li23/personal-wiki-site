"""Model: social regulation of the age at onset of foraging in honeybee workers (after the activator-inhibitor
model of Huang and Robinson 1992 and the JH-vitellogenin double repressor of Amdam and Omholt 2003; schematic).
Each worker's juvenile hormone titer J rises with age, opposed by vitellogenin V, which J suppresses and which
suppresses J:  dJ/dt = r (1 + 0.08 t) / (1 + V^2) - J/2 - i (r about 1.2, varying among workers),  dV/dt = 1 / (1 + J^4) - V/2, with an inhibitory input i from
contact with older foragers (ethyl oleate). A worker starts foraging when J exceeds the threshold 1.6. A: a
typical colony (i = 0.25): J switches from low to high after about three weeks. B: a single-cohort colony with no
foragers (i = 0): the switch comes about one to two weeks earlier, so some bees become precocious foragers."""
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P


def worker(r, i):
    f = lambda t, y: [r * (1 + 0.08 * t) / (1 + y[1] ** 2) - y[0] / 2 - i, 1 / (1 + y[0] ** 4) - y[1] / 2]
    return solve_ivp(f, (0, 40), [0.0, 1.9], max_step=0.05, dense_output=True)


rng = np.random.default_rng(3)
fig, ax = bio.canvas(24, 9.8)
t = np.linspace(0, 40, 400)
onset = {}
for k, (i, title) in enumerate([(0.25, "Colony with foragers"), (0.0, "No foragers present")]):
    x0 = 1.9 + k * 11.6
    bio.panel(ax, "AB"[k], (x0 - 1.5, 9.5))
    bio.label(ax, (x0 + 4.6, 9.2), title, size="small", bold=True)
    p = quant.Plot(ax, (x0, 1.8, 9.2, 6.6), xlim=(0, 40), ylim=(0, 10), xlabel="Worker age / days",
                   ylabel="Juvenile hormone (a.u.)", xticks=[0, 10, 20, 30, 40], yticks=[0, 2, 4, 6, 8, 10])
    p.hline(1.6, token="negative", text="foraging threshold", side="right")
    ons = []
    for j in range(12):
        r = rng.normal(1.2, 0.06)
        s = worker(r, i)
        J = s.sol(t)[0]
        p.line(t, J, "dna" if k == 0 else "rna", lw=0.7)
        cross = t[np.argmax(J > 1.6)] if (J > 1.6).any() else np.nan
        ons.append(cross)
    ons = np.array(ons)
    p.text(2, 9.4, f"median onset of foraging: {np.nanmedian(ons):.0f} days", ha="left", size="small")
ax.set_ylim(0.3, 9.8)
