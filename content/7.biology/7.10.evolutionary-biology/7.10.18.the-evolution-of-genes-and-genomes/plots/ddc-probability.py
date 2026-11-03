"""Probability of preservation by subfunctionalization in the DDC model (Force et al. 1999), against the
ratio r = u_r/u_c of the loss rate of one regulatory subfunction to the null-mutation rate of the coding
region, for z = 1..5 subfunctions. Monte Carlo of the sequence of permissible degenerative mutations; the
exact result for z = 2 is 2r^2/(1 + 2r)^2."""
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)


def simulate(z, r, reps):
    """Fraction of duplicate pairs that end subfunctionalized."""
    sub = 0
    for _ in range(reps):
        A = np.ones(z, bool)
        B = np.ones(z, bool)
        while True:
            # permissible events: (copy, kind, index, rate)
            ev = []
            for X, Y, c in ((A, B, 0), (B, A, 1)):
                if not X.any():
                    continue
                if np.all(~X | Y):          # null allowed if the other copy covers all of X's subfunctions
                    ev.append((c, -1, 1.0))
                for i in np.nonzero(X & Y)[0]:
                    ev.append((c, i, r))
            rates = np.array([e[2] for e in ev])
            c, i, _ = ev[rng.choice(len(ev), p=rates / rates.sum())]
            X = A if c == 0 else B
            if i < 0:
                X[:] = False
            else:
                X[i] = False
            if not A.any() or not B.any():
                break
            if np.any(A & ~B) and np.any(B & ~A):
                # each copy carries a subfunction the other lacks: both are now indispensable
                sub += 1
                break
    return sub / reps


fig, ax = bio.canvas(14, 9)
pax = charts.axes_at(ax, (2.0, 1.6, 11.2, 6.8))
rs = np.array([0.1, 0.2, 0.5, 1, 2, 5, 10])
toks = ["neutral", "dna", "rna", "positive", "protein"]
for z, tok in zip(range(1, 6), toks):
    ps = [simulate(z, r, 4000) for r in rs]
    pax.plot(rs, ps, "o", color=charts.line(tok), ms=5, label=f"z = {z}", zorder=5)
    pax.plot(rs, ps, "-", color=charts.line(tok), lw=0.8, alpha=0.5)
rr = np.logspace(-1, 1, 200)
pax.plot(rr, 2 * rr ** 2 / (1 + 2 * rr) ** 2, color=charts.line("dna"), lw=1.8, label="z = 2, exact")
pax.set_xscale("log")
pax.set_ylim(-0.02, 1)
pax.set_xlim(0.08, 12)
charts.style_axes(pax, r"$r = u_{\mathrm{r}}/u_{\mathrm{c}}$ (subfunction loss rate / null rate)",
                  "probability of subfunctionalization")
pax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
