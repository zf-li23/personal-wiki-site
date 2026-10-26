# Binding energetics of activators (computed from simple equilibrium models).
# A: occupancy of a palindromic site vs total protein concentration c (monomer units). Monomer: c/(c + 1 uM).
# Preformed dimer, Eq. (14.1): K2 = K1^2 c_eff with K1 = 1e6 /M, c_eff = 1 mM -> KD = 1 nM; dimer concentration c/2.
# Dimerization on DNA: two monomers bind the two half-sites with K1 each and a contact factor w = 1000 between them;
# statistical weights 1, 2x, w x^2 (x = c K1), occupancy of the full site = w x^2 / (1 + 2x + w x^2).
# B: synergy, Eq. (14.2), F = ((1 + w x)/(1 + x))^n with w = 4 at x = 10 (nearly full) and x = 1 (half occupancy),
# compared with additive activation 1 + n (w - 1) (each activator adding its own increment).
# C: four-site enhanceosome model: sites filled independently with weight x each and a cooperativity factor q for
# every pair of filled neighbouring sites; P(all four filled) by enumeration of the 16 states; Hill coefficient
# of the mean fractional occupancy theta from the maximum slope of log(theta/(1-theta)) vs log x.
import itertools

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(27.0, 8.0)
FS = bio.core.FONT["tiny"]

# ---- A
a = C.axes_at(ax, (1.5, 1.3, 6.6, 5.3))
c = np.logspace(-11, -4, 400)
K1, ceff = 1e6, 1e-3
x = c * K1
mono = x / (1 + x)
K2 = K1 ** 2 * ceff
dimer = (c / 2 * K2) / (1 + c / 2 * K2)
w = 1e3
coop = w * x ** 2 / (1 + 2 * x + w * x ** 2)
a.plot(c, mono, color=C.line("neutral"), lw=2.0, label="monomer, $K_D$ = 1 µM")
a.plot(c, dimer, color=C.line("receptor"), lw=2.0, label="preformed dimer, $K_D$ = 1 nM")
a.plot(c, coop, color=C.line("enzyme"), lw=2.0, ls=(0, (4, 2)), label="dimerizes on DNA (cooperative)")
a.set_xscale("log")
a.set_xlim(1e-11, 1e-4)
a.set_ylim(0, 1.4)
a.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
a.set_xticks([1e-11, 1e-9, 1e-7, 1e-5], ["10 pM", "1 nM", "100 nM", "10 µM"])
C.style_axes(a, "protein concentration", "site occupancy")
a.legend(fontsize=FS, frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.1, 7.9))
bio.label(ax, (0.6, 7.55), "Dimerization and affinity", size="normal", bold=True, ha="left")

# ---- B
b = C.axes_at(ax, (10.5, 1.3, 6.6, 5.3))
n = np.arange(0, 6)
om = 4.0
for xx, tok, name in [(10.0, "positive", "recruitment, $x$ = 10"), (1.0, "drug", "recruitment, $x$ = 1")]:
    F = ((1 + om * xx) / (1 + xx)) ** n
    b.plot(n, F, "o-", color=C.line(tok), lw=1.8, ms=4.5, mfc=P.fill(tok), label=name)
b.plot(n, 1 + n * (om - 1), "s--", color=C.line("neutral"), lw=1.4, ms=4, mfc=P.fill("neutral"), label="additive")
b.set_yscale("log")
b.set_xlim(-0.2, 5.2)
b.set_ylim(0.8, 2000)
C.style_axes(b, "number of activator sites $n$", "fold activation $F$")
b.legend(fontsize=FS, frameon=False, labelcolor=P.ink(), loc="upper left")
b.text(5.0, 1.3, "ω = 4 per activator", ha="right", fontsize=FS, color=P.muted())
bio.panel(ax, "B", (9.1, 7.9))
bio.label(ax, (9.6, 7.55), "Synergy by recruitment", size="normal", bold=True, ha="left")


# ---- C
def p_full(x, q, m=4):
    """Probability that all m sites are filled and mean fractional occupancy."""
    Z = np.zeros_like(x)
    K = np.zeros_like(x)
    for s in itertools.product((0, 1), repeat=m):
        k = sum(s)
        pairs = sum(s[i] * s[i + 1] for i in range(m - 1))
        wgt = x ** k * q ** pairs
        Z = Z + wgt
        K = K + k * wgt
    return x ** m * q ** (m - 1) / Z, K / Z / m


cc = C.axes_at(ax, (19.5, 1.3, 6.6, 5.3))
xg = np.logspace(-3, 2, 500)
for q, tok in [(1.0, "neutral"), (50.0, "enzyme")]:
    pf, th = p_full(xg, q)
    lg = np.log(th / (1 - th))
    nh = np.max(np.gradient(lg, np.log(xg)))
    cc.plot(xg, pf, color=C.line(tok), lw=2.0, label=f"cooperativity {q:g}: Hill coefficient ≈ {nh:.1f}")
cc.set_xscale("log")
cc.set_xlim(1e-3, 1e2)
cc.set_ylim(0, 1.3)
cc.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
C.style_axes(cc, "[factor] / $K_D$", "P(all four sites filled)")
cc.legend(fontsize=FS, frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (18.1, 7.9))
bio.label(ax, (18.6, 7.55), "Cooperative enhanceosome assembly", size="normal", bold=True, ha="left")
