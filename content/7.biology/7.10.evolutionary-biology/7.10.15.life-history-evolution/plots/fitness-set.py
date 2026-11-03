"""Levins's fitness set with a linear adaptive function (Theorem 15.4.1).

W1 = 1 - (1 - x)^k, W2 = 1 - x^k for x in [0, 1]; mean fitness 0.6 W1 + 0.4 W2. k = 2 (convex set) and
k = 0.5 (concave set).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
q = 0.6
x = np.linspace(0, 1, 1001)
fig, ax = bio.canvas(30.0, 11.0)
for j, (k, title, x0) in enumerate(((2.0, "Weak trade-off: generalist", 2.4), (0.5, "Strong trade-off: specialist", 17.6))):
    W1 = 1 - (1 - x) ** k
    W2 = 1 - x ** k
    W = q * W1 + (1 - q) * W2
    i = int(np.argmax(W))
    p = C.axes_at(ax, (x0, 1.6, 8.0, 8.0))
    p.plot(W1, W2, color=C.line("protein"), lw=2.0, label="fitness set")
    for c in np.linspace(0.2, 1.2, 6):
        w1 = np.linspace(0, 1.2, 10)
        p.plot(w1, (c - q * w1) / (1 - q), color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    p.plot([W1[i]], [W2[i]], "o", ms=6, color=C.line("negative"))
    p.text(W1[i] + 0.03, W2[i] + 0.03, f"optimum x = {x[i]:.2f}", fontsize=FS["tiny"], color=P.ink())
    p.set_xlim(0, 1.05)
    p.set_ylim(0, 1.05)
    C.style_axes(p, "fitness in environment 1, W₁", "fitness in environment 2, W₂")
    bio.panel(ax, "AB"[j], (x0 - 2.2, 10.8))
    bio.label(ax, (x0, 10.4), title, size="small", bold=True, ha="left")
