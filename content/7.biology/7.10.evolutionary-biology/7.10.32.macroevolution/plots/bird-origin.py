"""The origin of birds (Section 32.1.3): a schematic cladogram of some fossil theropods and early birds,
with crocodiles as the outgroup. Tips are labelled with the approximate age of the fossils (Mya).
Numbered bars mark where characters of living birds evolved: 1, hollow bones and a furcula (Theropoda);
2, filamentous feathers (Coelurosauria); 3, vaned feathers (Pennaraptora); 4, long feathered forelimbs
forming wings (Paraves); 5, a pygostyle; 6, a keeled sternum and an alula (Ornithothoraces). Red slashes:
loss of teeth, independently in Confuciusornis and in the ancestor of crown birds. The positions of
Anchiornis and Archaeopteryx near the base of Avialae are debated."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ink, muted = P.ink(), P.muted()
fig, ax = plt.subplots(figsize=(10.8, 4.8))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.97)

# (name, italic, age label, group colour token)
TAXA = [("Crocodylia", False, "living", "neutral"),
        ("Allosaurus", True, "~150", "neutral"),
        ("Sinosauropteryx", True, "~125", "rna"),
        ("Caudipteryx", True, "~125", "rna"),
        ("Microraptor", True, "~120", "rna"),
        ("Anchiornis", True, "~160", "rna"),
        ("Archaeopteryx", True, "~150", "dna"),
        ("Jeholornis", True, "~120", "dna"),
        ("Sapeornis", True, "~120", "dna"),
        ("Confuciusornis", True, "~125", "dna"),
        ("Enantiornithes", False, "131-66", "dna"),
        ("Yanornis", True, "~120", "dna"),
        ("crown birds", False, "living", "dna")]
n = len(TAXA)
x_end = n - 0.2
ax.plot([0, x_end], [0, 0], color=ink, lw=1.6)
tips = []
for k, (name, it, age, tok) in enumerate(TAXA):
    x = k + 0.3
    if k == n - 1:
        # crown birds: terminal continuation of the stem
        x0, x1 = x_end, x_end + 0.9
        ax.plot([x0, x1], [0, 1.0], color=charts.line("dna"), lw=2.2)
        tip = (x1, 1.0)
    elif k == n - 2:
        # Yanornis branches from the ornithuromorph node, sister to crown birds
        ax.plot([x, x + 0.9], [0, 1.0], color=ink, lw=1.3)
        tip = (x + 0.9, 1.0)
    else:
        ax.plot([x, x + 0.9], [0, 1.0], color=ink, lw=1.3)
        tip = (x + 0.9, 1.0)
    tips.append(tip)
    ax.plot([tip[0]], [tip[1]], "o", ms=6, color=P.edge(tok))
    ax.text(tip[0], tip[1] + 0.15, name, rotation=40, ha="left", va="bottom",
            fontsize=FT["small"], color=ink, style="italic" if it else "normal")
    ax.text(tip[0] + 0.05, tip[1] - 0.1, age, ha="left", va="top", fontsize=FT["tiny"], color=muted)

# numbered synapomorphy bars on the stem (x positions between successive branch points)
TRAITS = [(0.8, "hollow bones, furcula (Theropoda)"),
          (1.8, "filamentous feathers (Coelurosauria)"),
          (2.8, "vaned (pennaceous) feathers (Pennaraptora)"),
          (3.8, "long feathered forelimbs: wings (Paraves)"),
          (7.8, "pygostyle"),
          (9.8, "keeled sternum, alula (Ornithothoraces)")]
for k, (x, txt) in enumerate(TRAITS):
    ax.plot([x, x], [-0.18, 0.18], color=P.edge("highlight"), lw=3.2, solid_capstyle="butt")
    ax.text(x, -0.26, str(k + 1), ha="center", va="top", fontsize=FT["tiny"], color=ink, weight="bold")
    ax.text(0.0, -0.8 - 0.3 * k, f"{k + 1}  {txt}", ha="left", va="center", fontsize=FT["tiny"], color=ink)

# open bars: independent loss of teeth
for (bx, by) in [(9.3 + 0.45, 0.5), (x_end + 0.45, 0.5)]:
    ax.plot([bx - 0.12, bx + 0.12], [by + 0.12, by - 0.12], color=P.edge("negative"), lw=3.0,
            solid_capstyle="butt", alpha=0.9)
ax.text(5.6, -0.8, "red slashes  loss of teeth (twice, independently)", ha="left", va="center",
        fontsize=FT["tiny"], color=P.edge("negative"))
ax.text(5.6, -1.1, "numbers below tips: approximate age of the fossils (Mya)", ha="left", va="center",
        fontsize=FT["tiny"], color=muted)

# bracket for Avialae
ax.annotate("", xy=(6.3, -2.55), xytext=(x_end + 1.0, -2.55),
            arrowprops=dict(arrowstyle="-", color=charts.line("dna"), lw=2.0))
ax.text((6.3 + x_end + 1.0) / 2, -2.75, "Avialae (birds in the broad sense)", ha="center", va="top",
        fontsize=FT["tiny"], color=ink)

ax.set_xlim(-0.3, x_end + 2.6)
ax.set_ylim(-3.1, 2.75)
ax.axis("off")
