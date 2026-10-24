"""Heats of hydrogenation to cyclohexane (gas phase, Kistiakowsky et al.): cyclohexene -119.7,
cyclohexa-1,3-diene -231.8, benzene -208.4 kJ/mol; a hypothetical cyclohexatriene with three
isolated double bonds would release 3 x 119.7 = 359.1 kJ/mol. The difference, about 151 kJ/mol,
is the aromatic stabilization energy of benzene."""

import matplotlib.pyplot as plt

ink = plt.rcParams["text.color"]
levels = [("cyclohexene", 119.7, "C0"), ("cyclohexa-1,3-diene", 231.8, "C0"),
          ("benzene", 208.4, "C2"), ("cyclohexatriene\n(hypothetical)", 359.1, "C3")]
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.hlines(0, -0.4, 3.4, color=ink, lw=2)
ax.text(3.45, 0, "cyclohexane", va="center", fontsize=9)
for i, (name, dh, color) in enumerate(levels):
    ls = "--" if "hypothetical" in name else "-"
    ax.hlines(dh, i - 0.3, i + 0.3, color=color, lw=2.5, ls=ls)
    ax.annotate("", xy=(i, 4), xytext=(i, dh - 4), arrowprops=dict(arrowstyle="->", color=color, lw=1.2))
    ax.text(i + 0.06, dh / 2, f"{dh:.1f}", fontsize=9, color=color, va="center")
    ax.text(i, dh + 10, name, ha="center", va="bottom", fontsize=9)
ax.annotate("", xy=(2.55, 208.4), xytext=(2.55, 359.1), arrowprops=dict(arrowstyle="<->", color="C2", lw=1.2))
ax.hlines(359.1, 2.3, 2.75, color="0.6", lw=0.8, ls=":")
ax.hlines(208.4, 2.3, 2.75, color="0.6", lw=0.8, ls=":")
ax.text(2.48, 284, "stabilization\n151 kJ/mol", fontsize=9, color="C2", va="center", ha="right")
ax.set_xlim(-0.6, 4.3)
ax.set_ylim(-15, 420)
ax.set_xticks([])
ax.set_ylabel(r"$-\Delta_{\mathrm{hyd}}H$ / kJ mol$^{-1}$ (energy above cyclohexane + H$_2$)")
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
