"""A minimal chaperone-titration model of the heat shock response.

U: fraction of client proteins unfolded; H: chaperone (HSP) level; total HSF = 1.
Free chaperone Hf = H Ku / (Ku + U) (unfolded proteins sequester chaperone); free, active HSF F = 1 / (1 + Hf / KF)
(free chaperone binds and inactivates HSF).
dU/dt = kd(T) (1 - U) - kr Hf U;   dH/dt = b0 + b F^n / (KA^n + F^n) - d H
kr = 5, Ku = 0.05, KF = 0.2, KA = 0.5, n = 2, b = 12, b0 = 0.05, d = 0.1 per h; unfolding rate kd = 0.005 per h at
the normal temperature and 1.0 per h during a heat shock. Cells start at steady state.
Primed cells: shocks at 2-4 h and 8-10 h; naive cells: only the shock at 8-10 h.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio

P = bio.P
kr, Ku, KF, KA, n, b, b0, d = 5.0, 0.05, 0.2, 0.5, 2, 12.0, 0.05, 0.1


def model(shocks):
    def kd(t):
        return 1.0 if any(a <= t < c for a, c in shocks) else 0.005

    def rhs(t, y):
        U, H = y
        Hf = H * Ku / (Ku + U)
        F = 1 / (1 + Hf / KF)
        return [kd(t) * (1 - U) - kr * Hf * U, b0 + b * F ** n / (KA ** n + F ** n) - d * H]

    return rhs


def synthesis(U, H):
    Hf = H * Ku / (Ku + U)
    F = 1 / (1 + Hf / KF)
    return b0 + b * F ** n / (KA ** n + F ** n)


y0 = solve_ivp(model([]), (0, 400), [0.0, 1.0], max_step=0.2).y[:, -1]
t = np.linspace(0, 16, 1601)
runs = {}
for name, sh in (("primed", [(2, 4), (8, 10)]), ("naive", [(8, 10)])):
    s = solve_ivp(model(sh), (0, 16), y0, max_step=0.005, dense_output=True)
    runs[name] = s.sol(t)

fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.2), gridspec_kw={"width_ratios": [1.0, 1.2, 1.2]})
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
boxes = {"heat": (5, 9.0, "heat shock", "negative"), "U": (5, 6.6, "unfolded proteins", "protein"),
         "H": (2.0, 3.6, "HSP (chaperone)", "enzyme"), "F": (8.0, 3.6, "free HSF", "receptor"),
         "gene": (5, 0.9, "HSP genes", "dna")}
for x, y, txt, tok in boxes.values():
    ax.text(x, y, txt, ha="center", va="center", fontsize=8.5, color=P.ink(),
            bbox=dict(boxstyle="round,pad=0.35", fc=P.fill(tok), ec=P.edge(tok), lw=1.0, alpha=0.9))


def arrow(a, c, color, style="-|>", rad=0.0, text=None, tx=None):
    ax.annotate("", xy=c, xytext=a, arrowprops=dict(arrowstyle=style, color=color, lw=1.4,
                                                    connectionstyle=f"arc3,rad={rad}", shrinkA=2, shrinkB=2))
    if text:
        ax.text(*tx, text, fontsize=7.5, color=color, ha="center")


arrow((5, 8.5), (5, 7.1), P.edge("negative"))
arrow((2.6, 4.1), (4.2, 6.1), P.edge("negative"), style="-[", rad=-0.2, text="refolds", tx=(2.6, 5.4))
arrow((3.4, 3.6), (6.9, 3.6), P.edge("negative"), style="-[", text="binds, inactivates", tx=(5.15, 3.9))
arrow((5.9, 6.1), (7.6, 4.1), P.edge("positive"), rad=-0.2, text="titrates HSP away", tx=(7.9, 5.4))
arrow((8.0, 3.1), (5.9, 1.3), P.edge("positive"), rad=-0.2, text="activates", tx=(7.9, 2.0))
arrow((4.1, 1.3), (2.0, 3.1), P.edge("positive"), rad=-0.2, text="expression", tx=(2.1, 2.0))
ax.set_title("A  Negative feedback through chaperone titration", loc="left", fontsize=10)

bx = axes[1]
for a, c in ((2, 4), (8, 10)):
    bx.axvspan(a, c, color=P.fill("negative"), alpha=0.18, lw=0)
bx.plot(t, runs["primed"][0], color=P.edge("dna"), lw=2.0, label="primed (two shocks)")
bx.plot(t, runs["naive"][0], color=P.edge("rna"), lw=1.8, ls="--", label="naive (second shock only)")
bx.text(3.0, 0.235, "shock 1", ha="center", fontsize=8, color=P.edge("negative"))
bx.text(9.0, 0.235, "shock 2", ha="center", fontsize=8, color=P.edge("negative"))
bx.set_xlim(0, 16)
bx.set_ylim(0, 0.25)
bx.set_xlabel("time / h")
bx.set_ylabel("fraction of proteins unfolded, $U$")
bx.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1.0, 0.85))
bx.set_title("B  Acquired thermotolerance", loc="left", fontsize=10)

cx = axes[2]
for a, c in ((2, 4), (8, 10)):
    cx.axvspan(a, c, color=P.fill("negative"), alpha=0.18, lw=0)
U, H = runs["primed"]
cx.plot(t, synthesis(U, H), color=P.edge("highlight"), lw=2.0, label="HSP synthesis rate")
cx.plot(t, H, color=P.edge("enzyme"), lw=2.0, ls="--", label="HSP level $H$")
cx.set_xlim(0, 16)
cx.set_ylim(0, 6)
cx.set_xlabel("time / h")
cx.set_ylabel("rate (per h) or level (relative)")
cx.legend(frameon=False, fontsize=8, loc="upper right")
cx.set_title("C  A transient burst of synthesis", loc="left", fontsize=10)
for a in (bx, cx):
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
