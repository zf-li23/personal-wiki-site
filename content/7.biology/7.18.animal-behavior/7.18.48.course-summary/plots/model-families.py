"""The core models of the course in five families, with the main links between them.

Each box is a model or result; the number below the name is the section of 7.18 where it is
derived. Each column reads downward from the general result to its applications; horizontal
arrows mark where one family builds on another, and notes after a colon give further links.
Families: optimality with fixed payoffs, games with frequency-dependent payoffs, inclusive
fitness, information and signaling, learning rules.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 17.5)

cols = {
    "opt": (3.2, "Optimality", "fixed payoffs", "positive"),
    "game": (9.1, "Games", "payoffs depend on others", "highlight"),
    "kin": (15.0, "Inclusive fitness", "payoffs weighted by r", "rna"),
    "info": (20.9, "Information", "receivers as decision makers", "receptor"),
    "learn": (26.8, "Learning rules", "decisions from experience", "neuron"),
}
W, H = 5.3, 1.35
rows_y = [14.3, 11.9, 9.8, 7.7, 5.6, 3.5, 1.4]

models = {
    "opt": [("optimality model", "2.4"), ("prey model", "22.5"), ("marginal value theorem", "22.5, 20.4"),
            ("energy budget rule", "23.2"), ("dynamic programming", "23.3"), ("Gilliam's rule, FID", "23.6, 24.6"),
            ("Lack clutch, parent's optimum", "31.3")],
    "game": [("ESS, Nash, replicators", "25.1"), ("hawk-dove, bourgeois", "25.1, 25.2"), ("war of attrition, RHP", "25.2, 26.4"),
             ("ideal free distribution", "25.3"), ("producer-scrounger", "25.4"), ("switch point, RPS", "28.3"),
             ("care, desertion, negotiation", "32.2, 32.3")],
    "kin": [("Hamilton's rule", "33.2"), ("kin competition, dispersal", "33.5, 26.6"), ("spite", "33.7"),
            ("parent-offspring conflict", "32.4"), ("sex ratio conflict 3:1", "36.7"), ("worker policing", "36.8"),
            ("reproductive skew", "35.5")],
    "info": [("Bayes, red line", "37.3"), ("value of information", "37.3"), ("signal detection", "8.3, 24.4, 33.4"),
             ("index signals", "39.3"), ("costly signals (Grafen)", "39.4: an ESS"), ("Sir Philip Sidney game", "39.4: uses r"),
             ("cheap talk, deception", "39.5, 39.6")],
    "learn": [("value of learning", "41.1"), ("Rescorla-Wagner, Pearce-Hall", "41.3"), ("matching law", "41.4: = ideal free distribution"),
              ("exploration-exploitation", "23.1: cf. patch leaving"), ("song perturbation rule", "17.3"), ("Rogers' paradox", "46.2"),
              ("conformist bias", "46.6")],
}

pos = {}
for key, (x, title, sub, tok) in cols.items():
    bio.label(ax, (x, 16.9), title, size="normal", bold=True)
    bio.label(ax, (x, 16.15), sub, size="small", color=P.muted())
    for i, (name, sec) in enumerate(models[key]):
        y = rows_y[i]
        bio.box(ax, (x, y), W, H, token=tok)
        bio.label(ax, (x, y + 0.25), name, size="small", color=P.on_fill(), zorder=12)
        bio.label(ax, (x, y - 0.33), sec, size="tiny", color=P.on_fill(), zorder=12)
        pos[(key, i)] = (x, y)
    # vertical spine: each model builds on the one above
    for i in range(len(models[key]) - 1):
        a, b = pos[(key, i)], pos[(key, i + 1)]
        bio.arrow(ax, (a[0], a[1] - H / 2), (b[0], b[1] + H / 2), kind="process", color=P.muted(), lw=0.9, head=0.16)


def side(a, b, dashed=False, bend=0.0):
    (ka, ia), (kb, ib) = a, b
    xa, ya = pos[a]
    xb, yb = pos[b]
    s = 1 if xb > xa else -1
    bio.arrow(ax, (xa + s * W / 2, ya), (xb - s * W / 2, yb), kind="activation", color=P.ink(),
              lw=1.0, dashed=dashed, bend=bend, head=0.2)


side(("opt", 0), ("game", 0))            # optimality becomes a game when payoffs are frequency dependent
side(("game", 0), ("kin", 0))            # inclusive fitness weights the payoffs of a game by relatedness
side(("info", 2), ("learn", 1))          # prediction errors and detection thresholds
