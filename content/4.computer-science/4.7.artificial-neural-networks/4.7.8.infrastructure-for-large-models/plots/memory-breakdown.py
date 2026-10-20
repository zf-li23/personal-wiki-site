"""Training memory of Llama 3 models without any splitting across GPUs:
model states at 16 bytes per parameter (mixed-precision Adam), activations of
one 8,192-token sequence with FlashAttention and no recomputation, and FP32
logits, compared with the 80 GB of one H100."""

import matplotlib.pyplot as plt

models = {  # parameters, layers, hidden size
    "Llama-3-8B": (8.03e9, 32, 4096),
    "Llama-3-70B": (70.55e9, 80, 8192),
    "Llama-3-405B": (405.9e9, 126, 16384),
}
tokens, vocab = 8192, 128256
parts = {
    "BF16 weights (2 B/param)": lambda n, l, h: 2 * n,
    "BF16 gradients (2 B/param)": lambda n, l, h: 2 * n,
    "FP32 master weights, Adam m and v (12 B/param)": lambda n, l, h: 12 * n,
    "activations (34 B x tokens x hidden per layer)": lambda n, l, h: 34 * tokens * h * l,
    "FP32 logits": lambda n, l, h: 4 * tokens * vocab,
}
colors = ["C0", "C9", "C1", "C2", "C7"]

fig, axes = plt.subplots(3, 1, figsize=(11, 4.2))
for ax, name in zip(axes, models):
    left = 0.0
    for (label, f), c in zip(parts.items(), colors):
        val = f(*models[name]) / 1e9
        ax.barh([0], [val], left=left, color=c, label=label, height=0.6)
        left += val
    ax.text(left * 1.01, 0, f"{left:,.0f} GB", va="center", fontsize=9)
    ax.axvline(80, color="C3", ls="--", lw=1.2)
    ax.set_xlim(0, left * 1.12)
    ax.set_yticks([0])
    ax.set_yticklabels([name])
    ax.grid(axis="x", alpha=0.3)
axes[0].text(83, 0.42, "one H100: 80 GB", color="C3", fontsize=8)
axes[-1].set_xlabel("memory (GB); each row has its own scale")
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, fontsize=7.5, loc="lower center", ncol=3)
fig.tight_layout(rect=(0, 0.12, 1, 1))
