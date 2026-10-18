"""Sequential decomposition of SSTO for the body fat data in the two possible orders."""

import matplotlib.pyplot as plt

ssto = 495.39
sse12 = 109.95
orders = [
    ("X1 first", [("SSR(X1)", 352.27), ("SSR(X2 | X1)", 33.17)]),
    ("X2 first", [("SSR(X2)", 381.97), ("SSR(X1 | X2)", 3.47)]),
]
fig, ax = plt.subplots(figsize=(7.5, 5))
for pos, (label, parts) in enumerate(orders):
    bottom = 0.0
    ax.bar(pos, sse12, bottom=bottom, width=0.5, color="0.75", edgecolor="0.3")
    ax.text(pos, sse12 / 2, f"SSE(X1, X2)\n{sse12:.2f}", ha="center", va="center", fontsize=9)
    bottom = sse12
    colors = ["C0", "C3"]
    for (name, val), col in zip(reversed(parts), colors[::-1]):
        ax.bar(pos, val, bottom=bottom, width=0.5, color=col, alpha=0.8, edgecolor="0.3")
        y = bottom + val / 2
        if val > 20:
            ax.text(pos, y, f"{name}\n{val:.2f}", ha="center", va="center", fontsize=9)
        else:
            ax.annotate(f"{name} = {val:.2f}", xy=(pos + 0.25, y), xytext=(pos + 0.4, y + 40),
                        arrowprops=dict(arrowstyle="->"), fontsize=9)
        bottom += val
ax.axhline(ssto, color="0.3", ls="--", lw=1)
ax.text(1.55, ssto + 6, f"SSTO = {ssto:.2f}", ha="right", fontsize=9)
ax.set_xticks([0, 1], [o[0] for o in orders])
ax.set_xlim(-0.6, 1.9)
ax.set_ylim(0, 540)
ax.set_ylabel("sum of squares")
ax.set_title("Extra sums of squares depend on what is already in the model")
fig.tight_layout()
