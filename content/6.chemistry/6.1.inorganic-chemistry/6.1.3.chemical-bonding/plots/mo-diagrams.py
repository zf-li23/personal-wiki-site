"""Valence molecular-orbital energy diagrams (schematic): O2 without s-p mixing, N2 with s-p mixing, and CO."""

import matplotlib.pyplot as plt


def level(ax, x, y, n, label=None, w=0.5, side="right", gap=0.18):
    """Draw a degenerate set of n levels centred at x with given electron count list; returns x positions."""
    xs = [x + (k - (len(n) - 1) / 2) * (w + gap) for k in range(len(n))]
    for xc, e in zip(xs, n):
        ax.plot([xc - w / 2, xc + w / 2], [y, y], color="black", lw=1.6)
        if e >= 1:
            ax.annotate("", xy=(xc - 0.08, y + 0.32), xytext=(xc - 0.08, y - 0.12),
                        arrowprops=dict(arrowstyle="-|>", color="C3", lw=1.2, mutation_scale=8))
        if e == 2:
            ax.annotate("", xy=(xc + 0.08, y - 0.12), xytext=(xc + 0.08, y + 0.32),
                        arrowprops=dict(arrowstyle="-|>", color="C3", lw=1.2, mutation_scale=8))
    if label:
        if side == "right":
            ax.text(xs[-1] + w / 2 + 0.12, y, label, va="center", fontsize=9.5)
        else:
            ax.text(xs[0] - w / 2 - 0.12, y, label, va="center", ha="right", fontsize=9.5)
    return xs


def link(ax, x0, y0, x1, y1):
    ax.plot([x0, x1], [y0, y1], color="0.55", lw=0.8, ls="--")


def diagram(ax, title, left, right, mos, atom_names):
    """left/right: dict name -> (y, electrons list); mos: list of (y, electrons list, label, partners)."""
    xa, xm, xb = 0.0, 3.0, 6.0
    for name, (y, e) in left.items():
        level(ax, xa, y, e, name, side="left")
    for name, (y, e) in right.items():
        level(ax, xb, y, e, name, side="right")
    for y, e, lab, partners in mos:
        xs = level(ax, xm, y, e, lab)
        for side, name in partners:
            if side == "L":
                ya = left[name][0]
                xedge = xa + (len(left[name][1]) - 1) / 2 * 0.68 + 0.25
                link(ax, xedge, ya, xs[0] - 0.25, y)
            else:
                yb = right[name][0]
                xedge = xb - (len(right[name][1]) - 1) / 2 * 0.68 - 0.25
                link(ax, xs[-1] + 0.25, y, xedge, yb)
    for x, name in zip((xa, xm, xb), atom_names):
        ax.text(x, -3.4, name, ha="center", fontsize=11)
    ax.set_title(title, fontsize=11)
    ax.set_xlim(-2.2, 8.2)
    ax.axis("off")


both = [("L", "2p"), ("R", "2p")]
bs = [("L", "2s"), ("R", "2s")]
fig, axes = plt.subplots(1, 3, figsize=(13, 6.2), sharey=True)

# O2: 2s and 2p far apart, no s-p mixing: sigma(2p) below pi(2p).
diagram(axes[0], "O$_2$ (also F$_2$): no s-p mixing",
        {"2s": (0, [2]), "2p": (6, [2, 1, 1])}, {"2s": (0, [2]), "2p": (6, [2, 1, 1])},
        [(-1.2, [2], r"$\sigma_{\mathrm{2s}}$", bs), (1.2, [2], r"$\sigma^*_{\mathrm{2s}}$", bs),
         (4.0, [2], r"$\sigma_{\mathrm{2p}}$", both), (5.0, [2, 2], r"$\pi_{\mathrm{2p}}$", both),
         (7.2, [1, 1], r"$\pi^*_{\mathrm{2p}}$", both), (9.2, [0], r"$\sigma^*_{\mathrm{2p}}$", both)],
        ("O", "O$_2$", "O"))

# N2: s-p mixing pushes sigma(2p) above pi(2p).
diagram(axes[1], "N$_2$ (also Li$_2$ to C$_2$): s-p mixing",
        {"2s": (0.5, [2]), "2p": (5.5, [1, 1, 1])}, {"2s": (0.5, [2]), "2p": (5.5, [1, 1, 1])},
        [(-0.9, [2], r"$\sigma_{\mathrm{2s}}$", bs), (1.9, [2], r"$\sigma^*_{\mathrm{2s}}$", bs),
         (4.0, [2, 2], r"$\pi_{\mathrm{2p}}$", both), (4.9, [2], r"$\sigma_{\mathrm{2p}}$", both),
         (7.2, [0, 0], r"$\pi^*_{\mathrm{2p}}$", both), (9.2, [0], r"$\sigma^*_{\mathrm{2p}}$", both)],
        ("N", "N$_2$", "N"))

# CO: O orbitals lower than C orbitals; valence numbering 3sigma...6sigma.
diagram(axes[2], "CO (isoelectronic with N$_2$)",
        {"2s": (1.6, [2]), "2p": (6.6, [1, 1, 0])}, {"2s": (-1.2, [2]), "2p": (4.6, [2, 1, 1])},
        [(-1.8, [2], r"$3\sigma$", bs), (1.0, [2], r"$4\sigma$", bs),
         (3.6, [2, 2], r"$1\pi$", both), (5.4, [2], r"$5\sigma$ (HOMO)", both),
         (7.6, [0, 0], r"$2\pi$ (LUMO)", both), (9.6, [0], r"$6\sigma$", both)],
        ("C", "CO", "O"))

axes[0].set_ylim(-4.2, 10.2)
axes[0].annotate("", xy=(-1.9, 10), xytext=(-1.9, -2.5), arrowprops=dict(arrowstyle="-|>", color="0.5", lw=1))
axes[0].text(-2.1, 3.5, "energy", rotation=90, va="center", ha="right", fontsize=10)
fig.tight_layout()
