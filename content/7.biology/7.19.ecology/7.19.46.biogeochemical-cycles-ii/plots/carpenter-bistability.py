# Carpenter's lake phosphorus model in dimensionless form, dx/dt = a - x + r x^q / (1 + x^q)
# (a: external loading, x: phosphorus in the water, r: maximum recycling from the sediment, q: steepness).
# A: the rate balance for r = 1, q = 8: loss x (line) against supply a + r f(x) for three loadings.
# B: potential V(x) = -integral of the rate, for the same loadings.
# C: region of bistability in the (a, r) plane for q = 2, 4 and 8 (between the two fold curves);
#    to the right of a = 0 at the lower fold the clear state cannot be recovered by reducing loading.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
f = lambda x, q: x ** q / (1 + x ** q)
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.2, 4.1))
x = np.linspace(0, 2.2, 600)
r, q = 1.0, 8
toks = ["dna", "highlight", "negative"]
for L, tok in zip((0.3, 0.52, 0.75), toks):
    col = P.edge(tok) if tok == "highlight" else P.fill(tok)
    a.plot(x, L + r * f(x, q), color=col, lw=1.8, label=f"supply, a = {L}")
    dx = L - x + r * f(x, q)
    s = np.where(np.diff(np.sign(dx)))[0]
    for i in s:
        xs = x[i]
        stable = dx[i] > 0
        a.plot([xs], [xs], "o", color=col, ms=6, mfc=col if stable else P.surface())
    V = -np.cumsum(dx) * (x[1] - x[0])
    b.plot(x, V - V[0], color=col, lw=1.8, label=f"a = {L}")
a.plot(x, x, color=P.ink(), lw=1.8, label="loss x")
a.set_xlim(0, 2.2)
a.set_ylim(0, 2.2)
a.set_xlabel("Phosphorus in water x")
a.set_ylabel("Rate")
a.legend(frameon=False, fontsize=7.5, loc="upper left")
a.set_title("A  Supply and loss", loc="left", fontweight="bold")
b.set_xlim(0, 2.2)
b.set_xlabel("Phosphorus in water x")
b.set_ylabel("Potential V(x)")
b.legend(frameon=False, fontsize=7.5, loc="lower left")
b.set_title("B  Stability landscape", loc="left", fontweight="bold")

for qq, tok in ((2, "dna"), (4, "highlight"), (8, "negative")):
    col = P.edge(tok) if tok == "highlight" else P.fill(tok)
    xs = np.linspace(1e-3, 6, 4000)
    fp = qq * xs ** (qq - 1) / (1 + xs ** qq) ** 2
    rr = 1 / fp                                  # fold condition r f'(x) = 1
    aa = xs - rr * f(xs, qq)                     # loading at the fold
    ok = rr < 3
    c.plot(aa[ok], rr[ok], color=col, lw=1.8, label=f"q = {qq}")
c.axvline(0, color=P.muted(), lw=0.8, ls=":")
c.text(-0.62, 2.7, "irreversible:\nlower fold at a < 0", fontsize=7.5, color=P.muted())
c.text(-0.62, 0.25, "one equilibrium", fontsize=7.5, color=P.muted())
c.set_xlim(-0.7, 1.2)
c.set_ylim(0, 3)
c.set_xlabel("External loading a")
c.set_ylabel("Maximum recycling r")
c.legend(frameon=False, fontsize=7.5, loc="lower right")
c.set_title("C  Bistable region (inside cusps)", loc="left", fontweight="bold")
for ax in (a, b, c):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
