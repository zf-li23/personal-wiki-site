"""Ontogenetic growth model of West, Brown and Enquist (2001).

dm/dt = a m^(3/4) [1 - (m/M)^(1/4)], with the same a = 1 (units g^(1/4) per day) for four species of adult mass
M = 10, 1e3, 1e5 and 1e7 g, birth mass m0 = 0.01 M. A: growth curves m(t)/M on a logarithmic time axis.
B: the universal curve: with r = (m/M)^(1/4) and tau = a t / (4 M^(1/4)) - ln(1 - (m0/M)^(1/4)), every species
satisfies 1 - r = exp(-tau). Points: numerical solutions of the four species; line: exp(-tau).
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio

P = bio.P
a = 1.0
toks = ["dna", "plant", "highlight", "negative"]
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.5))
for Mad, tok, name in zip([1e1, 1e3, 1e5, 1e7], toks, ["10 g", "1 kg", "100 kg", "10 t"]):
    m0 = 0.01 * Mad
    tmax = 40 * Mad ** 0.25 / a
    t = np.logspace(-2, np.log10(tmax) - 1e-9, 300)
    sol = solve_ivp(lambda tt, m: a * m ** 0.75 * (1 - (m / Mad) ** 0.25), (0, tmax), [m0], t_eval=t,
                    rtol=1e-8, atol=1e-12 * Mad)
    m = sol.y[0]
    ax.plot(t, m / Mad, color=P.edge(tok), lw=2.0, label=f"$M$ = {name}")
    r = (m / Mad) ** 0.25
    tau = a * t / (4 * Mad ** 0.25) - np.log(1 - (m0 / Mad) ** 0.25)
    sel = slice(None, None, 15)
    bx.plot(tau[sel], 1 - r[sel], "o", ms=4, color=P.fill(tok), mec=P.edge(tok))
tau = np.linspace(0, 10, 100)
bx.plot(tau, np.exp(-tau), color=P.ink(), lw=1.5, label="$1 - r = \\mathrm{e}^{-\\tau}$")
ax.set_xscale("log")
ax.set_xlabel("age $t$ / days")
ax.set_ylabel("relative mass $m/M$")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Larger species grow longer", loc="left", fontsize=10)
bx.set_yscale("log")
bx.set_xlim(0, 10)
bx.set_ylim(3e-5, 1.2)
bx.set_xlabel("dimensionless time $\\tau$")
bx.set_ylabel("$1 - (m/M)^{1/4}$")
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  One universal growth curve", loc="left", fontsize=10)
for x in (ax, bx):
    for s in ("top", "right"):
        x.spines[s].set_visible(False)
fig.tight_layout()
