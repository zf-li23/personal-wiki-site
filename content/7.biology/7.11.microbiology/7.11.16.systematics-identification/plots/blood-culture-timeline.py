# Time to result for a blood culture, by three laboratory routes (typical, rounded times; individual
# cases vary widely). All routes start with incubation of blood-culture bottles in an automated system until
# growth is signalled (here 20 h; most clinically significant bacteria within 1-2 days) and a Gram stain of
# the positive broth (about 1 h). Conventional: subculture on plates overnight (18 h), then biochemical
# identification and antimicrobial susceptibility testing (AST) in parallel (18 h). MALDI-TOF: the same
# subculture, identification in minutes from the first colonies, AST as before. Direct molecular: a multiplex
# PCR panel on the positive broth identifies common species and key resistance genes in about 1.5 h;
# phenotypic AST is still needed for the full antibiogram.
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
steps = {
    "incubation": "neutral", "Gram stain": "protein", "subculture": "bacterium",
    "biochemical ID": "enzyme", "MALDI-TOF": "highlight", "PCR panel": "dna", "AST": "drug",
}
routes = [
    ("Conventional", [("incubation", 0, 20), ("Gram stain", 20, 1), ("subculture", 21, 18),
                      ("biochemical ID", 39, 18), ("AST", 39, 18)], 57, 57),
    ("MALDI-TOF", [("incubation", 0, 20), ("Gram stain", 20, 1), ("subculture", 21, 18),
                   ("MALDI-TOF", 39, 0.6), ("AST", 39, 18)], 39.6, 57),
    ("Direct molecular", [("incubation", 0, 20), ("Gram stain", 20, 1), ("PCR panel", 21, 1.5),
                          ("subculture", 21, 18), ("AST", 39, 18)], 22.5, 57),
]
fig, ax = plt.subplots(figsize=(11.0, 3.6))
for k, (name, bars, t_id, t_ast) in enumerate(routes):
    y = 2 - k
    seen = {}
    for step, t0, dt in bars:
        lane = 0.17 if step in ("biochemical ID", "MALDI-TOF", "PCR panel") else (-0.17 if step == "AST" else 0)
        if step == "subculture" and name == "Direct molecular":
            lane = -0.17
            t0, dt = 21, 18
        h = 0.3 if lane else 0.55
        ax.barh(y + lane, max(dt, 0.6), left=t0, height=h, color=P.fill(steps[step]), edgecolor=P.edge(steps[step]), lw=0.8)
    ax.plot(t_id, y + 0.42, "v", ms=7, color=charts.line("positive"))
    ax.text(t_id, y + 0.52, f"species ID {t_id:.0f} h", ha="center", va="bottom", fontsize=6.8, color=P.ink())
    ax.plot(t_ast, y - 0.42, "^", ms=7, color=charts.line("drug"))
    ax.text(t_ast + 0.8, y - 0.42, f"full AST {t_ast:.0f} h", ha="left", va="center", fontsize=6.8, color=P.ink())
ax.set_yticks([2, 1, 0])
ax.set_yticklabels([r[0] for r in routes], fontsize=7.5)
ax.set_xlim(0, 68)
ax.set_ylim(-0.75, 2.95)
handles = [plt.Rectangle((0, 0), 1, 1, facecolor=P.fill(t), edgecolor=P.edge(t)) for t in steps.values()]
ax.legend(handles, list(steps), fontsize=6.8, frameon=False, ncol=7, loc="upper center", bbox_to_anchor=(0.5, -0.17))
charts.style_axes(ax, "hours after the blood is drawn")
charts.title(ax, "From blood culture to report")
