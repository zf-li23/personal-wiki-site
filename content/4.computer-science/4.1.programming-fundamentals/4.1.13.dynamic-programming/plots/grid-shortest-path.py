import matplotlib.pyplot as plt

# h[i][j]: length of the horizontal road from (i, j) to (i, j + 1)
h = [[3, 2, 3], [2, 1, 4], [3, 4, 5], [3, 1, 2]]
# v[i][j]: length of the vertical road from (i, j) to (i + 1, j)
v = [[2, 2, 3, 4], [4, 1, 2, 4], [1, 2, 2, 3]]
n = 4

# Shortest distances from (0, 0), moving only up or right; keep the predecessor.
d = [[0] * n for _ in range(n)]
prev = [[None] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        options = []
        if i > 0:
            options.append((d[i - 1][j] + v[i - 1][j], (i - 1, j)))
        if j > 0:
            options.append((d[i][j - 1] + h[i][j - 1], (i, j - 1)))
        d[i][j], prev[i][j] = min(options)

# Recover the optimal route back from the target.
route = [(n - 1, n - 1)]
while prev[route[-1][0]][route[-1][1]] is not None:
    route.append(prev[route[-1][0]][route[-1][1]])
on_route = set(zip(route, route[1:])) | set(zip(route[1:], route))

fig, ax = plt.subplots(figsize=(5.2, 5.2))
for i in range(n):
    for j in range(n - 1):
        best = ((i, j), (i, j + 1)) in on_route
        ax.plot([j, j + 1], [i, i], color="C1" if best else "0.6", lw=3.5 if best else 1.5, zorder=1)
        ax.text(j + 0.5, i + 0.07, str(h[i][j]), ha="center", va="bottom", fontsize=10)
for i in range(n - 1):
    for j in range(n):
        best = ((i, j), (i + 1, j)) in on_route
        ax.plot([j, j], [i, i + 1], color="C1" if best else "0.6", lw=3.5 if best else 1.5, zorder=1)
        ax.text(j + 0.07, i + 0.5, str(v[i][j]), ha="left", va="center", fontsize=10)
for i in range(n):
    for j in range(n):
        ax.scatter(j, i, s=520, color="C0", zorder=2)
        ax.text(j, i, str(d[i][j]), ha="center", va="center", color="white", fontsize=11, weight="bold", zorder=3)
ax.annotate("start", (0, 0), xytext=(-0.45, -0.42), fontsize=10)
ax.annotate("target", (n - 1, n - 1), xytext=(n - 1.25, n - 0.6), fontsize=10)
ax.set_xlim(-0.6, n - 0.3)
ax.set_ylim(-0.6, n - 0.3)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Shortest distance from the start to every crossing")
fig.tight_layout()
