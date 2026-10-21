import matplotlib.pyplot as plt

# Schedules of the worked examples (job, start, end), computed by the simulator in the text.
panels = [
    ("FIFO, Example 3.2.1", [("A", 0, 100), ("B", 100, 110), ("C", 110, 120)], 120),
    ("SJF, Example 3.2.1", [("B", 0, 10), ("C", 10, 20), ("A", 20, 120)], 120),
    ("SJF, Example 3.2.2 (B, C arrive at 10)", [("A", 0, 100), ("B", 100, 110), ("C", 110, 120)], 120),
    ("STCF, Example 3.2.2 (B, C arrive at 10)",
     [("A", 0, 10), ("B", 10, 20), ("C", 20, 30), ("A", 30, 120)], 120),
    ("SJF, Example 3.3.1", [("A", 0, 5), ("B", 5, 10), ("C", 10, 15)], 15),
    ("RR (time slice 1), Example 3.3.1",
     [(j, t, t + 1) for t, j in enumerate("ABC" * 5)], 15),
]
colors = {"A": "C0", "B": "C1", "C": "C2"}
rows = {"A": 2, "B": 1, "C": 0}

fig, axes = plt.subplots(3, 2, figsize=(9, 6.4))
for ax, (title, slices, horizon) in zip(axes.flat, panels):
    for job, start, end in slices:
        ax.broken_barh([(start, end - start)], (rows[job] - 0.35, 0.7),
                       facecolors=colors[job], edgecolor="none")
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["C", "B", "A"])
    ax.set_xlim(0, horizon)
    ax.set_ylim(-0.6, 2.6)
    ax.set_title(title, fontsize=10)
    ax.grid(axis="x", alpha=0.3)
for ax in axes[-1]:
    ax.set_xlabel("time")
fig.tight_layout()
