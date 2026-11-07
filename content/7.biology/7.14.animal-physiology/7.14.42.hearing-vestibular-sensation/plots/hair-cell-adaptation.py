"""Adaptation of hair-cell mechanotransduction shifts the operating curve (schematic model).

Two-state gating (gating-spring model): P_o = 1 / (1 + exp(-z (X - X_a - X_0) / kT)),
z = 0.7 pN (gating force), kT = 4.1 pN nm, X_0 = 12.9 nm so that P_o = 0.1 at rest.
Adaptation moves the curve along the displacement axis: X_a = X_f + X_s, with a fast component
(Ca2+-dependent, tau 0.5 ms) and a slow component (myosin-1c motors, tau 20 ms), each relaxing
towards 0.4 X; adaptation is therefore 80 % complete.
A: P_o(X) at rest and after adapting to steady deflections of +20 and +50 nm (and -20 nm).
B: P_o after step deflections at t = 0 (+10, +20, +40 nm and -15 nm).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
z, kT, X0 = 0.7, 4.1, 12.9
tf, ts, ext = 0.5e-3, 20e-3, 0.4


def po(X, Xa=0.0):
    return 1 / (1 + np.exp(-z * (X - Xa - X0) / kT))


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.2))
X = np.linspace(-60, 110, 500)
ax.plot(X, po(X), color=P.ink(), lw=2.2, label="at rest")
for hold, c in ((20, P.edge("dna")), (50, P.edge("rna")), (-20, P.edge("enzyme"))):
    ax.plot(X, po(X, 0.8 * hold), color=c, lw=1.8, label=f"adapted to {hold:+d} nm")
    ax.plot(hold, po(hold, 0.8 * hold), "o", color=c, ms=5)
ax.axhline(0.1, color=P.muted(), lw=0.6, ls=":")
ax.set_xlabel("Bundle deflection X / nm  (positive: towards the tallest stereocilia)")
ax.set_ylabel(r"Open probability $P_{\mathrm{o}}$")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Adaptation resets the operating point", loc="left", fontsize=10)

dt = 2e-5
t = np.arange(-5e-3, 80e-3, dt)
for step, c in ((10, P.edge("enzyme")), (20, P.edge("dna")), (40, P.edge("rna")),
                (-15, P.edge("protein"))):
    xf = xs = 0.0
    out = np.empty_like(t)
    for k, tk in enumerate(t):
        Xk = step if tk >= 0 else 0.0
        xf += dt * (ext * Xk - xf) / tf
        xs += dt * (ext * Xk - xs) / ts
        out[k] = po(Xk, xf + xs)
    bx.plot(t * 1e3, out, color=c, lw=1.8, label=f"step {step:+d} nm")
bx.axhline(0.1, color=P.muted(), lw=0.6, ls=":")
bx.set_xlabel("Time / ms")
bx.set_ylabel(r"$P_{\mathrm{o}}$")
bx.set_ylim(0, 1.02)
bx.legend(frameon=False, fontsize=8, loc="upper right")
bx.set_title("B  Fast and slow adaptation after a step", loc="left", fontsize=10)
fig.tight_layout()
