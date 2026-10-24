"""Schematic free-energy profiles of SEAr (qualitative energy scale).
Left: benzene + E+ forms the sigma complex through the highest transition state (rate-determining);
losing H+ gives the aromatic substitution product (downhill), whereas adding a nucleophile would give
a non-aromatic addition product of higher energy.
Right: substituent effects. An electron donor (OCH3, attack para) lowers the sigma complex and, by the
Hammond postulate, the transition state leading to it; an electron acceptor (NO2, attack meta) raises
both, relative to benzene. Each profile is drawn from its own reactants, placed at a common zero."""

import numpy as np
import matplotlib.pyplot as plt


def profile(xs, ys):
    """Smooth curve through stationary points (xs, ys): cosine segments with zero slope at each point."""
    px, py = [], []
    for (x0, x1), (y0, y1) in zip(zip(xs, xs[1:]), zip(ys, ys[1:])):
        x = np.linspace(x0, x1, 50)
        px.append(x)
        py.append(y0 + (y1 - y0) * (1 - np.cos(np.pi * (x - x0) / (x1 - x0))) / 2)
    return np.concatenate(px), np.concatenate(py)


fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2))
x, y = profile([0, 0.7, 1.2, 1.55, 2.2], [0, 16, 10, 12, -6])
a1.plot(x, y, color="C0", lw=2, label="substitution")
x, y = profile([1.2, 1.6, 2.2], [10, 13.5, 5])
a1.plot(x, y, color="C3", lw=2, ls="--", label="addition")
a1.text(0, -1.2, "ArH + E$^+$", ha="center", va="top", fontsize=9)
a1.text(1.2, 9.2, "sigma\ncomplex", ha="center", va="top", fontsize=9)
a1.text(2.25, -6, "ArE + H$^+$", va="center", fontsize=9, color="C0")
a1.text(2.25, 5, "addition product\n(not aromatic)", va="center", fontsize=9, color="C3")
a1.text(0.7, 16.8, "TS1 (slow)", ha="center", fontsize=9)
a1.set_title("SEAr: substitution, not addition", fontsize=10)
a1.legend(fontsize=8, loc="lower left", frameon=False)

for (r, c, ts, color, name) in ((0, 7, 11, "C2", "anisole (para)"), (0, 11, 15, "C0", "benzene"),
                                (0, 16, 20.5, "C3", "nitrobenzene (meta)")):
    x, y = profile([0, 0.6, 1.0, 1.25, 1.8], [r, ts, c, c + 1.5, c - 14])
    a2.plot(x, y, color=color, lw=2, label=name)
a2.text(1.0, 22.5, "sigma complexes", ha="center", fontsize=9)
a2.text(0, -1.2, "ArH + E$^+$\n(common zero)", ha="center", va="top", fontsize=9)
a2.set_title("substituent effect on the rate", fontsize=10)
a2.legend(fontsize=8, loc="lower left", frameon=False)
for ax in (a1, a2):
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("reaction coordinate")
    ax.set_ylabel("G")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
a1.set_xlim(-0.3, 2.9)
a2.set_xlim(-0.2, 2.0)
a1.set_ylim(-9, 19)
a2.set_ylim(-14, 25)
fig.tight_layout()
