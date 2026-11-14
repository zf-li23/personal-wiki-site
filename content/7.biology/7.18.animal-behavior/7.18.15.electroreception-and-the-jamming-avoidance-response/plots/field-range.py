"""How far can an electroreceptive animal sense? Steep decay of quasi-static fields.

A: the bioelectric field of a small prey (a dipole, field proportional to r^-3) taking 10 uV/cm
at 1 cm, an illustrative value for a small fish or crustacean; compared with a monopole (r^-2)
of the same field at 1 cm. Horizontal lines: approximate behavioral thresholds of elasmobranch
ampullae of Lorenzini (5 nV/cm) and of teleost ampullary organs (about 1 uV/cm).
B: active electrolocation. The fish's own field at a small object falls with distance (here a
dipole of body length 10 cm), and the object's induced dipole field at the skin falls again with
distance, so the electric image falls roughly as r^-3 close to the body and much faster beyond
one body length (computed for a sphere of radius 0.5 cm, conductor, normalized at 1 cm).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
r = np.logspace(-0.3, 2, 300)  # cm
Ed = 10e-6 * r ** -3   # V/cm
Em = 10e-6 * r ** -2
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
a.loglog(r, Ed, color=P.edge("dna"), lw=2, label="dipole source (prey), ∝ r⁻³")
a.loglog(r, Em, color=P.edge("neutral"), lw=1.4, ls="--", label="monopole, ∝ r⁻²")
for thr, lab, col in ((5e-9, "shark ampullae ≈ 5 nV/cm", P.edge("negative")),
                      (1e-6, "teleost ampullary organs ≈ 1 µV/cm", P.edge("rna"))):
    a.axhline(thr, color=col, lw=1, ls=":")
    a.text(30, thr * 1.4, lab, fontsize=7.5, color=col, ha="center")
    rr = (10e-6 / thr) ** (1 / 3)
    a.plot(rr, thr, "o", color=col, ms=5)
    a.annotate(f"{rr:.0f} cm", (rr, thr), (rr * 0.45, thr * 0.12), fontsize=7.5, color=col,
               arrowprops=dict(arrowstyle="-", color=col, lw=0.6))
a.set_xlabel("Distance from source / cm")
a.set_ylabel("Field strength / V cm$^{-1}$")
a.set_ylim(1e-10, 1e-4)
a.legend(frameon=False, fontsize=7.5, loc="upper right")
a.set_title("A  Passive: prey fields", loc="left", fontweight="bold", fontsize=10)
# B: fish dipole of separation 10 cm along x, object at lateral distance d from midpoint
d = np.logspace(-0.3, 1.7, 200)


def fish_field(x, y, L=10.0):
    ex = ey = 0.0
    for sx, q in ((L / 2, 1.0), (-L / 2, -1.0)):
        dx, dy = x - sx, y
        rr = np.hypot(dx, dy)
        ex = ex + q * dx / rr ** 3
        ey = ey + q * dy / rr ** 3
    return np.hypot(ex, ey)


E0 = fish_field(2.0, d)
img = E0 * 0.5 ** 3 / d ** 3
img = img / np.interp(1.0, d, img)
b.loglog(d, img, color=P.edge("dna"), lw=2, label="electric image of a small conductor")
b.loglog(d, d ** -3.0, color=P.muted(), lw=0.8, ls="--", label="∝ d⁻³")
b.axvline(10, color=P.muted(), lw=0.6)
b.text(10.5, 0.3, "one body\nlength", fontsize=7.5, color=P.muted())
b.set_xlabel("Lateral distance of the object / cm")
b.set_ylabel("Image amplitude (relative to 1 cm)")
b.legend(frameon=False, fontsize=7.5, loc="lower left")
b.set_title("B  Active: electric image", loc="left", fontweight="bold", fontsize=10)
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
