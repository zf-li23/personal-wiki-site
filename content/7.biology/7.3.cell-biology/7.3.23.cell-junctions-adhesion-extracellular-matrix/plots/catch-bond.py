"""Integrin activation and the force dependence of adhesive bonds.

A: three conformations of an integrin: bent (inactive, the headpiece faces the membrane), extended with
the legs and cytoplasmic tails together (closed headpiece, intermediate affinity), and extended-open with the
tails separated by talin and kindlin bound to the beta tail (inside-out activation); a matrix ligand
binds the open headpiece, and force on the bond stabilizes this state.
B: mean lifetime of a single bond against the pulling force F. Slip bond (Bell 1978): k(F) = k0 exp(F x / kBT),
tau = 1/k, with k0 = 1 per s and x = 0.5 nm. Catch-slip bond (two-pathway model):
k(F) = kc exp(-F xc / kBT) + ks exp(F xs / kBT) with kc = 10 per s, xc = 1.2 nm, ks = 0.05 per s, xs = 0.8 nm,
kBT = 4.28 pN nm (310 K): force first slows dissociation (catch regime) and then speeds it up; the lifetime
peaks at F* = kBT ln(kc xc / (ks xs)) / (xc + xs), about 12 pN. These illustrative values are of the order measured
for P-selectin with PSGL-1 (Marshall and colleagues 2003). C: the fraction of catch-slip bonds surviving
after time t at three forces, exp(-k(F) t): bonds last longest at intermediate force.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant
from wikibio import junctions as J

P = bio.P
fig, ax = bio.canvas(28.0, 9.2)

bio.panel(ax, "A", (0.1, 9.1))
y = 6.4
J.band(ax, [(0.4, y), (9.4, y)])
ax.add_patch(__import__("matplotlib").patches.Rectangle((0.4, y + J.MT / 2), 9.0, 1.9, facecolor=P.fill("cytoplasm"),
             edgecolor="none", zorder=0))
names = ("Bent\n(inactive)", "Extended,\nclosed", "Extended, open,\nligand bound")
for k, st in enumerate(("bent", "closed", "open")):
    x = 1.6 + 3.0 * k
    r = J.integrin(ax, (x, y), state=st, scale=1.25, ligand=J.tok("fibronectin") if st == "open" else None)
    bio.label(ax, (x + (0.2 if st == "bent" else 0.0), 2.3), names[k], size="tiny")
    if st == "open":
        bt = r["beta_tail"]
        J.globule(ax, bt + np.array([-0.05, 0.12]), 0.26, 0.16, "talin", seed=3)
        J.globule(ax, bt + np.array([0.3, -0.12]), 0.15, 0.12, "kindlin", seed=4)
        bio.callout(ax, bt + np.array([-0.05, 0.2]), (8.0, 8.1), "Talin head", size="tiny")
        bio.callout(ax, bt + np.array([0.36, -0.1]), (9.1, 7.4), "Kindlin", size="tiny")
        bio.callout(ax, r["ligand"], (8.9, 3.4), "Ligand (RGD)", size="tiny")
        ax.annotate("", xy=(x, 3.0), xytext=(x, 3.7), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.0))
        bio.label(ax, (x + 0.15, 3.35), "F", size="small", italic=True, ha="left")
for k in range(2):
    bio.arrow(ax, (2.5 + 3.0 * k, 4.6), (3.6 + 3.0 * k, 4.6), kind="process")
bio.label(ax, (0.6, 8.5), "Cytoplasm", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (9.3, 5.9), "Extracellular", size="tiny", color=P.muted(), ha="right")
bio.label(ax, (5.0, 8.65), "Inside-out activation →", size="tiny", color=P.muted())

kT = 4.28
F = np.linspace(0, 40, 400)
k_slip = 1.0 * np.exp(F * 0.5 / kT)
kc, xc, ks, xs = 10.0, 1.2, 0.05, 0.8


def kcs(f):
    return kc * np.exp(-f * xc / kT) + ks * np.exp(f * xs / kT)


bio.panel(ax, "B", (10.6, 9.1))
pb = charts.axes_at(ax, (12.0, 1.4, 6.6, 6.8))
pb.plot(F, 1 / k_slip, color=quant.line_color("neutral"), lw=1.8, ls=(0, (4, 2)), label="slip bond (Bell)")
pb.plot(F, 1 / kcs(F), color=quant.line_color("receptor"), lw=2.2, label="catch-slip bond")
Fs = kT * np.log(kc * xc / (ks * xs)) / (xc + xs)
pb.axvline(Fs, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pb.text(Fs + 0.8, 1.38, f"F* ≈ {Fs:.0f} pN", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.set_xlim(0, 40)
pb.set_ylim(0, 1.5)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.9))
charts.style_axes(pb, "force F / pN", "mean bond lifetime τ / s")
charts.title(pb, "Force can prolong a bond")

bio.panel(ax, "C", (19.8, 9.1))
pc = charts.axes_at(ax, (21.2, 1.4, 6.4, 6.8))
t = np.linspace(0, 4, 300)
for f, tk in ((0, "neutral"), (12, "receptor"), (35, "drug")):
    pc.plot(t, np.exp(-kcs(f) * t), color=quant.line_color(tk), lw=2.0, label=f"F = {f} pN")
pc.set_xlim(0, 4)
pc.set_ylim(0, 1.02)
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pc, "time t / s", "fraction of bonds intact")
charts.title(pc, "Catch-slip bonds under constant force")
