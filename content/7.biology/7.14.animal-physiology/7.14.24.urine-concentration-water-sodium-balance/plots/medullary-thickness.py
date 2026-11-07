# Maximum urine concentration against relative medullary thickness (RMT) in mammals.
# RMT = 10 x medullary thickness / kidney size (Sperber's index). Approximate values compiled in
# Schmidt-Nielsen & O'Dell (1961, Am J Physiol 200: 1119) and later textbooks; values vary between studies,
# so the points are indicative. Line: least-squares fit, Umax = a + b RMT.
import matplotlib.pyplot as plt
import numpy as np

data = [
    ("Beaver", 1.3, 520),
    ("Pig", 1.6, 1100),
    ("Human", 3.0, 1400),
    ("Dog", 4.3, 2400),
    ("Cat", 4.8, 3100),
    ("Rat", 5.8, 2900),
    ("Kangaroo rat", 8.5, 5500),
    ("Jerboa", 9.3, 6500),
    ("Sand rat (Psammomys)", 10.7, 6300),
]
names = [d[0] for d in data]
rmt = np.array([d[1] for d in data])
umax = np.array([d[2] for d in data])
b, a = np.polyfit(rmt, umax, 1)
r = np.corrcoef(rmt, umax)[0, 1]

fig, ax = plt.subplots(figsize=(6.6, 4.4))
xx = np.linspace(0, 12, 50)
ax.plot(xx, a + b * xx, color="#9e9e9e", lw=1.2, ls="--")
ax.scatter(rmt, umax, s=36, color="#2f6fb5", zorder=3)
for n, x, y in data:
    dx, ha = (0.25, "left") if n not in ("Rat", "Sand rat (Psammomys)") else (-0.25, "right")
    dy = -260 if n == "Rat" else 0
    ax.text(x + dx, y + dy, n, fontsize=8.5, ha=ha, va="center")
ax.axhline(300, color="#c0392b", lw=0.8, ls=":")
ax.text(11.8, 380, "plasma, ~300", fontsize=8.5, ha="right", color="#c0392b")
ax.text(0.3, 6700, f"Umax = {a:.0f} + {b:.0f} RMT,  r = {r:.2f}", fontsize=8.5)
ax.set_xlim(0, 12)
ax.set_ylim(0, 7200)
ax.set_xlabel("Relative medullary thickness")
ax.set_ylabel("Maximum urine osmolality (mOsm/kg)")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
