# Iron-responsive elements: one RNA-binding switch, two opposite outputs.
# A: at low iron the iron-regulatory proteins (IRP1 as apo-protein, IRP2 stable) bind IREs. On the ferritin
# mRNA a single IRE in the 5' UTR near the cap blocks recruitment of the 43S preinitiation complex (no ferritin
# made); on the transferrin-receptor (TfR) mRNA five IREs in the 3' UTR are covered and protected from an
# endonuclease (TfR made). At high iron IRP1 acquires a [4Fe-4S] cluster and becomes cytosolic aconitase, IRP2
# is degraded (FBXL5), the IREs are free: ferritin is translated and TfR mRNA is cut in its 3' UTR and decays.
# B: steady-state model. Active IRP falls with iron as a = 1/(1 + (Fe/K)^2); IRE occupancy
# theta = rho a/(1 + rho a) with rho = 100 (IRP in excess over K_d); ferritin translation proportional to
# 1 - theta; TfR mRNA m* proportional to 1/(k0 + kc (1 - theta)) with (k0 + kc)/k0 = 20, so its level varies
# 20-fold while synthesis is constant. Both outputs normalized to their maxima.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 10.0)


def hairpin(x, y, h=0.9, w=0.28, token="mrna"):
    ax.plot([x - w / 2, x - w / 2], [y, y + h], color=P.edge(token), lw=1.6, zorder=6)
    ax.plot([x + w / 2, x + w / 2], [y + h, y], color=P.edge(token), lw=1.6, zorder=6)
    th = np.linspace(np.pi, 0, 30)
    ax.plot(x + w / 2 * np.cos(th) * 1.4, y + h + 0.2 * np.sin(th) + 0.0, color=P.edge(token), lw=1.6, zorder=6)
    for yy in np.linspace(y + 0.12, y + h - 0.1, 4):
        ax.plot([x - w / 2, x + w / 2], [yy, yy], color=P.muted(), lw=0.6, zorder=5)


def mrna(x0, x1, y, cds, label, ires, irp=False, cut=False, ribo=False):
    bio.label(ax, (x0 - 0.35, y), "5′", size="tiny", bold=True)
    ax.add_patch(bio.core.Circle((x0, y), 0.13, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=8))
    ax.plot([x0, x1], [y, y], color=P.edge("mrna"), lw=1.8, zorder=4)
    bio.box(ax, ((cds[0] + cds[1]) / 2, y), cds[1] - cds[0], 0.42, token="mrna", text=label, size="tiny", radius=0.05, zorder=6)
    bio.label(ax, (x1 + 0.45, y), "AAAA", size="tiny", color=P.edge("mrna"))
    for xi in ires:
        hairpin(xi, y + 0.05)
        if irp:
            bio.protein(ax, (xi, y + 1.35), 0.55, 0.5, "receptor", size="tiny")
    if cut:
        ax.plot([ires[1] + 0.25] * 2, [y - 0.4, y + 0.4], color=P.edge("negative"), lw=1.1, ls=(0, (2, 1.4)), zorder=8)
        bio.label(ax, (ires[1] + 0.25, y - 0.6), "endonuclease", size="tiny", color=P.edge("negative"))
    if ribo:
        bio.protein(ax, (cds[0] + 0.5, y + 0.55), 1.0, 0.6, "rrna", text="80S", size="tiny")


bio.panel(ax, "A", (0.1, 9.85))
bio.label(ax, (3.7, 9.5), "Low iron: IRPs bound", size="small", bold=True)
bio.label(ax, (10.3, 9.5), "High iron: IREs free", size="small", bold=True)
# ferritin
y = 7.0
mrna(1.0, 6.2, y, (2.4, 5.4), "ferritin", [1.6], irp=True)
bio.label(ax, (3.9, y - 0.8), "43S blocked: no ferritin", size="tiny", color=P.edge("negative"))
mrna(7.8, 13.0, y, (9.2, 12.2), "ferritin", [8.4], ribo=True)
bio.label(ax, (10.7, y - 0.8), "translated: iron stored", size="tiny", color=P.edge("positive"))
# TfR
y = 3.4
mrna(1.0, 6.2, y, (1.6, 3.4), "TfR", [3.9, 4.4, 4.9, 5.4, 5.9], irp=True)
bio.label(ax, (3.9, y - 0.8), "stable: TfR made, iron taken up", size="tiny", color=P.edge("positive"))
mrna(7.8, 13.0, y, (8.4, 10.2), "TfR", [10.7, 11.2, 11.7, 12.2, 12.7], cut=True)
bio.label(ax, (10.0, y - 1.25), "t½ ≈ 20-fold shorter", size="tiny", color=P.edge("negative"))
bio.label(ax, (6.9, 1.2), "IRP1 + [4Fe-4S] → aconitase; IRP2 degraded", size="tiny", color=P.muted())
ax.plot([6.9, 6.9], [1.6, 9.2], color=P.muted(), lw=0.6, ls=(0, (2, 2)))

# --- B ---
bio.panel(ax, "B", (14.6, 9.85))
fe = np.logspace(-1.5, 1.5, 300)
a = 1 / (1 + fe ** 2)
rho = 100.0
theta = rho * a / (1 + rho * a)
ferr = 1 - theta
k0, kc = 1.0, 19.0
tfr = 1 / (k0 + kc * (1 - theta))
tfr = tfr / tfr.max()
ferr = ferr / ferr.max()
pl = Q.Plot(ax, (16.4, 1.8, 7.8, 6.8), xlim=(10 ** -1.5, 10 ** 1.5), ylim=(0, 1.05), xlog=True,
            xlabel="cellular iron / K (log scale)", ylabel="output (relative to maximum)",
            xticks=[(0.1, "0.1"), (1, "1"), (10, "10")], yticks=[0, 0.5, 1])
pl.line(fe, tfr, "receptor", text="TfR mRNA (stability)", at=0.25, dx=0.0, dy=0.3)
pl.line(fe, ferr, "positive")
pl.text(0.04, 0.08, "ferritin synthesis (translation)", token="positive", ha="left")
pl.line(fe, a, "neutral", dashed=True)
pl.text(0.5, 0.62, "active IRP", token="neutral", ha="right")
