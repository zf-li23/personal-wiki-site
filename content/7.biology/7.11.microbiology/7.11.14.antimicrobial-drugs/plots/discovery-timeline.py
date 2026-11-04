# Approximate year of discovery (first report of antibacterial activity) of the main classes of
# antibacterial drugs, coloured by origin (natural product or synthetic). The shaded band marks the
# "golden age" of discovery from soil microorganisms (about 1940-1962); after 1987 few new classes
# were found, and the only post-2000 class shown (diarylquinolines, bedaquiline) is used only against
# tuberculosis. Years after Silver (2011) and standard histories; they are rounded and approximate.
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P

classes = [
    ("Penicillins", 1928, "natural"),
    ("Sulfonamides", 1932, "synthetic"),
    ("Aminoglycosides", 1943, "natural"),
    ("Cephalosporins", 1945, "natural"),
    ("Polymyxins", 1947, "natural"),
    ("Chloramphenicol", 1947, "natural"),
    ("Tetracyclines", 1948, "natural"),
    ("Isoniazid", 1952, "synthetic"),
    ("Macrolides", 1952, "natural"),
    ("Glycopeptides", 1953, "natural"),
    ("Rifamycins", 1957, "natural"),
    ("Quinolones", 1962, "synthetic"),
    ("Lincosamides", 1962, "natural"),
    ("Fosfomycin", 1969, "natural"),
    ("Mupirocin", 1971, "natural"),
    ("Carbapenems", 1976, "natural"),
    ("Monobactams", 1981, "natural"),
    ("Oxazolidinones", 1987, "synthetic"),
    ("Lipopeptides", 1987, "natural"),
    ("Diarylquinolines", 2005, "synthetic"),
]

fig, ax = plt.subplots(figsize=(8.6, 5.4))
ax.axvspan(1940, 1962, color=P.mix(P.fill("highlight"), P.surface(), 0.7), lw=0, zorder=0)
ax.text(1951, len(classes) - 0.1, "golden age", ha="center", va="bottom", fontsize=8, color=P.ink(), style="italic")
ax.axvspan(1988, 2020, color=P.mix(P.fill("neutral"), P.surface(), 0.75), lw=0, zorder=0)
ax.text(2004, 9.0, "discovery void:\nfew new classes", ha="center", va="center", fontsize=8, color=P.muted(), style="italic")
col = {"natural": charts.line("bacterium"), "synthetic": charts.line("drug")}
for i, (name, year, origin) in enumerate(classes):
    y = len(classes) - 1 - i
    ax.plot([1925, year], [y, y], color=P.mix(P.muted(), P.surface(), 0.55), lw=0.7, zorder=1)
    ax.plot(year, y, "o", ms=7, color=col[origin], mec=P.ink(), mew=0.5, zorder=3)
    ax.text(year + 1.2, y, name, va="center", fontsize=7.5, color=P.ink())
for origin, lab in (("natural", "natural product (or derivative)"), ("synthetic", "synthetic")):
    ax.plot([], [], "o", ms=7, color=col[origin], mec=P.ink(), mew=0.5, label=lab)
ax.legend(fontsize=7.5, frameon=False, loc="upper right", labelcolor=P.ink())
ax.set_xlim(1925, 2020)
ax.set_ylim(-0.8, len(classes) + 0.6)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
charts.style_axes(ax, "year of discovery")
