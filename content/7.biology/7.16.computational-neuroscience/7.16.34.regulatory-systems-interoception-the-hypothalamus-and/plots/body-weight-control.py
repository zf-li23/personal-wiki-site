"""Body-weight control with and without appetite feedback (Example 34.5.1).

rho dW/dt = I - E(W),  E(W) = E0 + k (W - W0),  rho = 32 MJ/kg, k = 0.092 MJ kg^-1 d^-1.
Appetite feedback (leptin, proportional in fat mass): I = I0 - g (W - W0), g = 0.5 MJ kg^-1 d^-1.
Integral controller: I = I0 - g (W - W0) + z, dz/dt = -kappa (W - W0), kappa = 0.002 MJ kg^-1 d^-2.
A: intake clamped 2.1 MJ/d below baseline for 100 days, then free.
B: expenditure raised by 1 MJ/d from day 0 (sustained disturbance).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rho, k, g, kappa = 32.0, 0.092, 0.5, 0.002
W0, I0 = 70.0, 10.0
dt = 0.5
t = np.arange(-50, 600, dt)


def run(mode, clamp=None, dE=0.0):
    W, z = W0, 0.0
    out = np.empty_like(t)
    for i, ti in enumerate(t):
        E = I0 + k * (W - W0) + (dE if ti >= 0 else 0.0)
        if clamp is not None and 0 <= ti < clamp:
            I = I0 - 2.1
        elif mode == "none":
            I = I0
        else:
            I = I0 - g * (W - W0) + (z if mode == "integral" else 0.0)
        W += dt * (I - E) / rho
        if mode == "integral" and ti >= 0:
            z += dt * (-kappa * (W - W0))
        out[i] = W
    return out


fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
styles = [("none", "No appetite feedback", "neutral", "-"),
          ("prop", "Leptin feedback (proportional)", "dna", "-"),
          ("integral", "Proportional + integral", "negative", "--")]
for mode, lab, tok, ls in styles[:2]:
    axs[0].plot(t, run(mode, clamp=100), color=P.edge(tok), lw=2, ls=ls, label=lab)
axs[0].axvspan(0, 100, color=P.light("highlight"), zorder=0)
axs[0].text(50, 70.4, "restricted\nintake", ha="center", va="bottom", fontsize=8.5, color=P.muted())
axs[0].set_title("A  Recovery after a 100-day restriction", loc="left", fontsize=10)
for mode, lab, tok, ls in styles:
    axs[1].plot(t, run(mode, dE=1.0), color=P.edge(tok), lw=2, ls=ls, label=lab)
axs[1].set_title("B  Sustained rise in expenditure (+1 MJ/d)", loc="left", fontsize=10)
for ax in axs:
    ax.axhline(W0, color=P.muted(), lw=0.8, ls=":")
    ax.set_xlabel("Time / d")
    ax.set_ylabel("Body mass / kg")
    ax.set_xlim(-50, 600)
    ax.grid(True, alpha=0.3)
axs[0].set_ylim(62, 71.5)
axs[1].set_ylim(58, 71.5)
axs[1].legend(frameon=False, fontsize=8, loc="lower right")
fig.tight_layout()
