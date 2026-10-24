# Positional information (Wolpert's French flag). A morphogen made at a source (x = 0), diffusing with
# coefficient D and degraded at rate k, settles into C(x) = C0 exp(-x / lambda) with decay length
# lambda = sqrt(D / k); here lambda = 0.2 L, close to the Bicoid gradient of the Drosophila embryo
# (about 20 % of egg length). Cells read two thresholds (T1 = 0.3 C0, T2 = 0.08 C0) and adopt three fates;
# boundaries lie at x_i = lambda ln(C0 / T_i). Doubling the source (dashed) shifts every boundary by
# lambda ln 2 = 0.14 L towards the sink: the pattern scales with the dose, which is why real embryos add
# feedback and opposing gradients for robustness. Right: on a log scale the profile is a straight line of
# slope -1 / lambda.

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import development as D

fig, ax = bio.canvas(19.5, 10.0)
P = bio.P
lam, T = 0.2, (0.3, 0.08)
fate_tok = ["na", "neutral", "negative"]
x = np.linspace(0, 1, 400)
b1 = D.boundaries(1.0, lam, T)
b2 = D.boundaries(2.0, lam, T)

X0, X1 = 1.6, 12.6
pax = C.axes_at(ax, (X0, 4.75, X1 - X0, 4.1))
for (a, b), tok in zip(((0, b1[0]), (b1[0], b1[1]), (b1[1], 1)), fate_tok):
    pax.axvspan(a, b, color=P.fill(tok), alpha=0.28, lw=0)
pax.plot(x, D.gradient(x, 1.0, lam), color=bio.P.ink(), lw=2.0, label="$C_0$")
pax.plot(x, D.gradient(x, 2.0, lam), color=bio.P.muted(), lw=1.6, ls=(0, (4, 3)), label="$2C_0$")
for t, name in zip(T, ("$T_1$", "$T_2$")):
    pax.axhline(t, color=P.edge("highlight"), lw=1.0, ls=(0, (2, 2)))
    pax.text(1.01, t, name, color=P.edge("highlight"), fontsize=bio.core.FONT["small"], va="center", transform=pax.get_yaxis_transform())
for xb in b1:
    pax.axvline(xb, color=P.muted(), lw=0.7)
pax.set_xlim(0, 1)
pax.set_ylim(0, 1.05)
pax.set_xticks([0, b1[0], b1[1], 1], ["0", "$x_1$", "$x_2$", "1"])
C.style_axes(pax, "position x / L", "concentration C / $C_0$")
pax.legend(loc="upper right", frameon=False, fontsize=bio.core.FONT["small"], labelcolor=P.ink())
bio.label(ax, (X0, 9.6), "Morphogen gradient and threshold readout", size="normal", bold=True, ha="left")
bio.label(ax, (X0 + 0.12, 8.65), "← source", size="tiny", ha="left", color=P.muted())

# rows of cells read the gradient: fate by threshold
n = 22
cx = (np.arange(n) + 0.5) / n
for row, (c0, yy, text, dashed) in enumerate(((1.0, 2.55, "$C_0$", False), (2.0, 1.35, "$2C_0$", True))):
    c = D.gradient(cx, c0, lam)
    fates = [0 if v > T[0] else 1 if v > T[1] else 2 for v in c]
    D.cell_row(ax, X0, X1, yy, fates, fate_tok, h=0.8, dashed=dashed)
    bio.label(ax, (X0 - 0.2, yy), text, size="small", ha="right")
bio.label(ax, (X0 - 0.2, 3.35), "fates:", size="small", ha="right", color=P.muted())
for k, (name, xb0, xb1) in enumerate((("blue", 0, b1[0]), ("white", b1[0], b1[1]), ("red", b1[1], 1))):
    bio.label(ax, (X0 + (xb0 + xb1) / 2 * (X1 - X0), 3.35), name, size="small", color=P.edge(fate_tok[k]), bold=True)
# shift arrow between the rows
xa, xb = X0 + b1[1] * (X1 - X0), X0 + b2[1] * (X1 - X0)
bio.arrow(ax, (xa, 0.55), (xb, 0.55), kind="process", head=0.18)
bio.label(ax, ((xa + xb) / 2, 0.25), "shift λ ln 2", size="tiny", va="top")

# log-scale panel
lax = C.axes_at(ax, (14.6, 4.75, 4.2, 4.1))
lax.semilogy(x, D.gradient(x, 1.0, lam), color=bio.P.ink(), lw=2.0)
lax.semilogy(x, D.gradient(x, 2.0, lam), color=bio.P.muted(), lw=1.6, ls=(0, (4, 3)))
for t in T:
    lax.axhline(t, color=P.edge("highlight"), lw=1.0, ls=(0, (2, 2)))
lax.set_xlim(0, 1)
lax.set_ylim(5e-3, 3)
C.style_axes(lax, "x / L", "C / $C_0$ (log)")
lax.text(0.12, 0.012, "slope $-1/\\lambda$", color=P.ink(), fontsize=bio.core.FONT["small"], rotation=-27)
bio.label(ax, (14.6, 9.6), "Log scale", size="normal", bold=True, ha="left")
bio.label(ax, (14.6, 3.0), f"λ = {lam} L,  x₁ = {b1[0]:.2f} L,  x₂ = {b1[1]:.2f} L", size="small", ha="left")
bio.label(ax, (14.6, 2.45), f"with 2C₀: x₁ = {b2[0]:.2f} L,  x₂ = {b2[1]:.2f} L", size="small", ha="left", color=P.muted())
