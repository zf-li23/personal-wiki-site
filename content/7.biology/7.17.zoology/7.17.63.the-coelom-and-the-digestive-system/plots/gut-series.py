# Digestive tracts of six vertebrates as straightened tubes (regions coloured alike; not to scale), and a
# model of food retention time against body mass (Example 63.7.1). Model, not data.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 12.6)
REG = {"oesophagus": "neutral", "crop": "vesicle", "stomach": "enzyme", "proventriculus": "golgi", "gizzard": "muscle",
       "small intestine": "highlight", "spiral valve": "highlight", "caecum": "plant", "large intestine": "mitochondrion",
       "cloaca": "blood", "rectum": "blood"}

tracts = [
    ("A  Shark", [("oesophagus", 0.8, 0.35), ("stomach", 2.0, 0.8), ("small intestine", 0.5, 0.3),
                  ("spiral valve", 2.2, 0.75), ("large intestine", 0.6, 0.3), ("cloaca", 0.5, 0.55)], {"rectal gland": 7.0}),
    ("B  Teleost", [("oesophagus", 0.6, 0.35), ("stomach", 1.4, 0.7), ("small intestine", 5.0, 0.32), ("rectum", 0.5, 0.4)],
     {"pyloric caeca": 2.3}),
    ("C  Frog", [("oesophagus", 0.6, 0.35), ("stomach", 1.6, 0.75), ("small intestine", 3.5, 0.3),
                 ("large intestine", 1.0, 0.6), ("cloaca", 0.5, 0.5)], {}),
    ("D  Lizard", [("oesophagus", 1.4, 0.32), ("stomach", 1.6, 0.6), ("small intestine", 3.0, 0.3), ("caecum", 0.0, 0.0),
                   ("large intestine", 1.2, 0.5), ("cloaca", 0.5, 0.5)], {}),
    ("E  Bird", [("oesophagus", 0.7, 0.3), ("crop", 0.9, 0.8), ("oesophagus", 0.6, 0.3), ("proventriculus", 0.7, 0.5),
                 ("gizzard", 1.1, 0.95), ("small intestine", 3.0, 0.3), ("caecum", 0.0, 0.0), ("rectum", 0.6, 0.38),
                 ("cloaca", 0.5, 0.55)], {"paired": 1}),
    ("F  Rabbit", [("oesophagus", 0.8, 0.3), ("stomach", 1.6, 0.85), ("small intestine", 3.6, 0.3), ("caecum", 0.0, 0.0),
                   ("large intestine", 2.2, 0.45), ("rectum", 0.6, 0.32)], {"big caecum": 1}),
]

for i, (title, segs, extra) in enumerate(tracts):
    y = 11.6 - i * 1.85
    x = 2.6
    bio.label(ax, (0.3, y), title, size="small", ha="left")
    starts = {}
    for name, ln, w in segs:
        if name == "caecum":
            big = "big caecum" in extra
            n = 2 if "paired" in extra else 1
            for k in range(n):
                dy = 0.35 + 0.25 * k
                cv = bio.blob((x + 0.1 + 0.25 * k, y - dy - (0.35 if big else 0.15)), 0.18 + (0.35 if big else 0.0),
                              0.45 if big else 0.28, wobble=0.02, seed=k)
                bio.shape(ax, cv, token=REG["caecum"], zorder=4, lw=0.7)
            starts["caecum"] = (x + 0.1, y - 0.55)
            continue
        v = np.array([(x, y - w / 2), (x + ln, y - w / 2), (x + ln, y + w / 2), (x, y + w / 2)])
        bio.shape(ax, v, token=REG[name], zorder=5, lw=0.7)
        if name == "spiral valve":
            for xs in np.arange(x + 0.15, x + ln, 0.22):
                ax.plot([xs, xs + 0.16], [y - w / 2 + 0.05, y + w / 2 - 0.05], color=P.edge("highlight"), lw=0.8, zorder=6)
        starts.setdefault(name, (x + ln / 2, y))
        x += ln
    # liver and pancreas buds behind the stomach (or at start of small intestine)
    xi = starts["small intestine"][0] - 1.2 if "small intestine" in starts else x
    sx = [s for n, s in starts.items() if n in ("stomach", "gizzard")]
    xl = sx[-1][0] + 0.4 if sx else xi
    bio.shape(ax, bio.blob((xl, y + 0.75), 0.45, 0.22, wobble=0.04, seed=i), token="er", zorder=4, lw=0.6)
    bio.shape(ax, bio.blob((xl + 0.9, y - 0.55), 0.3, 0.13, wobble=0.04, seed=i + 7), token="lysosome", zorder=4, lw=0.6)
    if "pyloric caeca" in extra:
        x0 = 2.6 + 0.6 + 1.4
        for k in range(7):
            ax.plot([x0 + 0.1 + 0.12 * k, x0 + 0.0 + 0.12 * k], [y - 0.16, y - 0.75], color=P.edge("plant"), lw=2.4,
                    solid_capstyle="round", zorder=4)
        bio.label(ax, (x0 + 1.4, y - 0.7), "pyloric caeca", size="tiny", ha="left")
    if "rectal gland" in extra:
        bio.shape(ax, bio.blob((2.6 + 0.8 + 2.0 + 0.5 + 2.2 + 0.3, y + 0.5), 0.18, 0.25, seed=3), token="positive", zorder=4, lw=0.6)
        bio.label(ax, (2.6 + 0.8 + 2.0 + 0.5 + 2.2 + 0.6, y + 0.65), "rectal gland", size="tiny", ha="left")

# legend
lx, ly = 0.4, 0.55
for name in ("oesophagus", "crop", "stomach", "proventriculus", "gizzard", "small intestine", "caecum", "large intestine",
             "cloaca"):
    bio.shape(ax, np.array([(lx, ly), (lx + 0.35, ly), (lx + 0.35, ly + 0.28), (lx, ly + 0.28)]), token=REG[name], lw=0.6)
    lab = {"cloaca": "cloaca / rectum", "small intestine": "small intestine (spiral valve)"}.get(name, name)
    bio.label(ax, (lx + 0.45, ly + 0.14), lab, size="tiny", ha="left")
    lx += 0.9 + 0.13 * len(lab)
bio.shape(ax, np.array([(lx, ly), (lx + 0.35, ly), (lx + 0.35, ly + 0.28), (lx, ly + 0.28)]), token="er", lw=0.6)
bio.label(ax, (lx + 0.45, ly + 0.14), "liver", size="tiny", ha="left")
lx += 1.5
bio.shape(ax, np.array([(lx, ly), (lx + 0.35, ly), (lx + 0.35, ly + 0.28), (lx, ly + 0.28)]), token="lysosome", lw=0.6)
bio.label(ax, (lx + 0.45, ly + 0.14), "pancreas", size="tiny", ha="left")

# model
bio.panel(ax, "G", (15.2, 12.2))
p = quant.Plot(ax, (16.8, 3.0, 7.6, 8.4), xlim=(0.01, 2000), ylim=(1, 200), xlog=True, ylog=True,
               xlabel="body mass M / kg", ylabel="mean retention time / h",
               xticks=[(0.01, "0.01"), (0.1, "0.1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")],
               yticks=[1, 3, 10, 30, 100])
m = np.logspace(-2, np.log10(2000), 100)
p.line(m, 70 * (m / 500) ** 0.25, "plant", text=r"$\propto M^{1/4}$", at=0.15, dy=0.25)
p.hline(24, text="24 h: fibre digestion", side="left")
for name, mass in (("dik-dik", 4), ("sheep", 50), ("cattle", 500), ("rabbit", 2)):
    q = p.xy(mass, 70 * (mass / 500) ** 0.25)
    ax.plot([q[0]], [q[1]], "o", ms=4, color=quant.line_color("plant"), zorder=9)
    if name == "rabbit":
        bio.label(ax, (q[0] - 0.15, q[1] + 0.3), name, size="tiny", ha="right")
    else:
        bio.label(ax, (q[0] + 0.12, q[1] - 0.35), name, size="tiny", ha="left")
