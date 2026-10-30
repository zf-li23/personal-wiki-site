"""The cardinals in increasing order (Section 4.7): the finite cardinals, aleph_0 = card N, the
continuum 2^aleph_0 = card R, and 2^(2^aleph_0), each step up justified by Cantor's theorem k < 2^k. The
continuum hypothesis asserts that there is no cardinal strictly between aleph_0 and 2^aleph_0; it can be
neither proved nor refuted in ZFC (Godel 1940, Cohen 1963)."""

import matplotlib.pyplot as plt

steps = [r"$0$", r"$1$", r"$2$", r"$\cdots$", r"$n$", r"$\cdots$", r"$\aleph_0$", r"$2^{\aleph_0}$",
         r"$2^{2^{\aleph_0}}$", r"$\cdots$"]
fig, ax = plt.subplots(figsize=(9.5, 4.6))
for i, s in enumerate(steps):
    c = "C0" if i < 6 else "C1"
    h = 0.35 + 0.33 * i
    ax.add_patch(plt.Rectangle((i, 0), 0.9, h, fc=c, alpha=0.3, ec=c, lw=1.2))
    ax.text(i + 0.45, h + 0.12, s, ha="center", va="bottom", fontsize=13)
ax.annotate("", (7.45, 3.35), (6.45, 3.05), arrowprops=dict(arrowstyle="-|>", color="C3", lw=1.5,
                                                             connectionstyle="arc3,rad=-0.5"))
ax.text(6.9, 4.05, "continuum hypothesis:\nno cardinal in between", ha="center", va="bottom", fontsize=10, color="C3")
ax.text(2.4, 3.0, "finite cardinals", ha="center", fontsize=11, color="C0")
ax.text(2.4, 4.0, r"each step up: $k < 2^{k}$ (Cantor's theorem)", ha="center", fontsize=10)
ax.set_xlim(-0.2, 10.2)
ax.set_ylim(0, 5.0)
ax.axis("off")
