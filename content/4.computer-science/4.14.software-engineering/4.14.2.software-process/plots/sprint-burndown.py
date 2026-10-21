"""Burndown chart of the example two-week sprint (17 story points)."""

import matplotlib.pyplot as plt

days = list(range(11))
# remaining story points at the end of each working day; a story counts only when done
remaining = [17, 17, 17, 14, 14, 11, 10, 10, 5, 5, 0]
ideal = [17 - 17 * d / 10 for d in days]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, ideal, "--", color="0.55", label="ideal burndown")
ax.step(days, remaining, where="post", marker="o", label="remaining story points")
events = {3: "S1 done", 5: "S2 done", 6: "S6 done", 8: "S3 done", 10: "S4 done"}
for d, text in events.items():
    offset = (-48, 6) if d == 10 else (4, 8)
    ax.annotate(text, (d, remaining[d]), textcoords="offset points", xytext=offset, fontsize=8)
ax.set_xlabel("working day of the sprint")
ax.set_ylabel("story points remaining")
ax.set_xticks(days)
ax.set_ylim(0, 19)
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()
