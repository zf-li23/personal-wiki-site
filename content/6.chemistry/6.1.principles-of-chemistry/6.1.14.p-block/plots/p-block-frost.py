"""Frost diagrams (N E0 against oxidation number N) of p-block elements at pH 0 (and Cl at pH 14),
built from Latimer diagrams with E0 values from the CRC Handbook; the element has N E0 = 0."""

import matplotlib.pyplot as plt


# for species below N = 0 the E0 attached to the next-higher entry joins the two
data = {
    "a": [
        ("Cl (pH 0)", "C0", [(-1, "Cl$^-$", None), (0, "Cl$_2$", 1.358), (1, "HClO", 1.611),
                             (3, "HClO$_2$", 1.645), (5, "ClO$_3^-$", 1.214), (7, "ClO$_4^-$", 1.189)]),
        ("Br (pH 0)", "C3", [(-1, "Br$^-$", None), (0, "Br$_2$", 1.066), (1, "HBrO", 1.596),
                             (5, "BrO$_3^-$", 1.453), (7, "BrO$_4^-$", 1.853)]),
        ("I (pH 0)", "C2", [(-1, "I$^-$", None), (0, "I$_2$", 0.5355), (1, "HIO", 1.439),
                            (5, "IO$_3^-$", 1.134), (7, "H$_5$IO$_6$", 1.601)]),
    ],
    "b": [
        ("Cl (pH 0)", "C0", [(-1, "Cl$^-$", None), (0, "Cl$_2$", 1.358), (1, "HClO", 1.611),
                             (3, "HClO$_2$", 1.645), (5, "ClO$_3^-$", 1.214), (7, "ClO$_4^-$", 1.189)]),
        ("Cl (pH 14)", "C1", [(-1, "Cl$^-$", None), (0, "Cl$_2$", 1.358), (1, "ClO$^-$", 0.262),
                              (3, "ClO$_2^-$", 0.66), (5, "ClO$_3^-$", 0.33), (7, "ClO$_4^-$", 0.36)]),
    ],
    "c": [
        ("S (pH 0)", "C1", [(-2, "H$_2$S", None), (0, "S", 0.142), (2, "S$_2$O$_3^{2-}$", 0.50),
                            (4, "H$_2$SO$_3$", 0.40), (6, "SO$_4^{2-}$", 0.172)]),
        ("O (pH 0)", "C4", [(-2, "H$_2$O", None), (-1, "H$_2$O$_2$", 1.776), (0, "O$_2$", 0.695)]),
    ],
    "d": [
        ("N (pH 0)", "C0", [(-3, "NH$_4^+$", None), (-2, "N$_2$H$_5^+$", 1.275), (-1, "NH$_3$OH$^+$", 1.42),
                            (0, "N$_2$", -1.87), (1, "N$_2$O", 1.766), (2, "NO", 1.591),
                            (3, "HNO$_2$", 0.983), (4, "N$_2$O$_4$", 1.065), (5, "NO$_3^-$", 0.803)]),
        ("P (pH 0)", "C3", [(-3, "PH$_3$", None), (0, "P", -0.063), (1, "H$_3$PO$_2$", -0.508),
                            (3, "H$_3$PO$_3$", -0.499), (5, "H$_3$PO$_4$", -0.276)]),
    ],
}
titles = {"a": "(a) halogens, acidic", "b": "(b) chlorine: acid versus base",
          "c": "(c) oxygen and sulfur, acidic", "d": "(d) nitrogen and phosphorus, acidic"}


def points(chain):
    # y(N) = N E0(X(N)/X(0)); walk outwards from the element
    idx0 = [i for i, c in enumerate(chain) if c[0] == 0][0]
    ys = {0: 0.0}
    for i in range(idx0 + 1, len(chain)):
        ys[chain[i][0]] = ys[chain[i - 1][0]] + (chain[i][0] - chain[i - 1][0]) * chain[i][2]
    for i in range(idx0 - 1, -1, -1):
        hi = chain[i + 1]
        ys[chain[i][0]] = ys[hi[0]] - (hi[0] - chain[i][0]) * hi[2]
    return [(c[0], ys[c[0]], c[1]) for c in chain]


fig, axes = plt.subplots(2, 2, figsize=(10.5, 8.4))
for ax, key in zip(axes.flat, "abcd"):
    for j, (name, col, chain) in enumerate(data[key]):
        pts = points(chain)
        ax.plot([p[0] for p in pts], [p[1] for p in pts], "o-", color=col, lw=1.5, label=name)
        off = [(-6, 6), (6, -11), (8, -3)][j]
        for n, y, lab in pts:
            if n == 0 and j > 0 and key != "c":
                continue
            if key == "b" and j == 1 and n < 1:
                continue
            ax.annotate(lab, (n, y), xytext=off, textcoords="offset points", fontsize=8, color=col,
                        ha="right" if off[0] < 0 else "left")
    ax.axhline(0, color="0.6", lw=0.7, ls=":")
    ax.set_title(titles[key], fontsize=10)
    ax.set_xlabel("oxidation number $N$")
    ax.set_ylabel(r"$N E^\circ$ / V")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
