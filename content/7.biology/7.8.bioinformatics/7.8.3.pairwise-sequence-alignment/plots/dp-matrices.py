# Dynamic-programming matrices for x = HEAGAWGHEE (columns) and y = PAWHEAE (rows), BLOSUM50 scores and
# a linear gap penalty d = 8. A: Needleman-Wunsch (global): the traceback runs from the bottom-right cell
# (score 1) to the top-left corner. B: Smith-Waterman (local): negative values are replaced by 0, and the
# traceback runs from the maximum (28) to the first zero, giving AWGHE / AW-HE.
import numpy as np
import wikibio as bio

P = bio.P
B50 = {"AA": 5, "AE": -1, "AG": 0, "AH": -2, "AP": -1, "AW": -3, "EE": 6, "EG": -3, "EH": 0, "EP": -1, "EW": -3,
       "GG": 8, "GH": -2, "GP": -2, "GW": -3, "HH": 10, "HP": -2, "HW": -3, "PP": 10, "PW": -4, "WW": 15}


def s(a, b):
    return B50["".join(sorted(a + b))]


x, y, d = "HEAGAWGHEE", "PAWHEAE", 8


def fill(local):
    F = np.zeros((len(y) + 1, len(x) + 1))
    if not local:
        F[0, :] = -d * np.arange(len(x) + 1)
        F[:, 0] = -d * np.arange(len(y) + 1)
    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
            v = max(F[i - 1, j - 1] + s(y[i - 1], x[j - 1]), F[i - 1, j] - d, F[i, j - 1] - d)
            F[i, j] = max(v, 0) if local else v
    if local:
        i, j = np.unravel_index(np.argmax(F), F.shape)
    else:
        i, j = len(y), len(x)
    path = [(i, j)]
    while (i > 0 or j > 0) and not (local and F[i, j] == 0):
        if i > 0 and j > 0 and F[i, j] == F[i - 1, j - 1] + s(y[i - 1], x[j - 1]):
            i, j = i - 1, j - 1
        elif i > 0 and F[i, j] == F[i - 1, j] - d:
            i -= 1
        else:
            j -= 1
        path.append((i, j))
    return F, path


fig, ax = bio.canvas(26.0, 11.8)
cw = 1.0
for k, (local, x0, title) in enumerate([(False, 1.4, "global (Needleman-Wunsch)"), (True, 13.8, "local (Smith-Waterman)")]):
    F, path = fill(local)
    top = 9.4
    bio.label(ax, (x0 + 0.5 + (len(x) + 1) * cw / 2, top + 1.55), title, size="small", bold=True)
    for j, c in enumerate("-" + x):
        bio.label(ax, (x0 + 0.5 + (j + 0.5) * cw, top + 0.75), c, size="small", bold=True)
    for i, c in enumerate("-" + y):
        bio.label(ax, (x0, top - (i + 0.5) * cw), c, size="small", bold=True)
    on = set(path)
    for i in range(len(y) + 1):
        for j in range(len(x) + 1):
            cx, cy = x0 + 0.5 + (j + 0.5) * cw, top - (i + 0.5) * cw
            if (i, j) in on:
                ax.add_patch(__import__("matplotlib.patches", fromlist=["x"]).Rectangle(
                    (cx - 0.48, cy - 0.48), 0.96, 0.96, facecolor=P.light("protein"), edgecolor=P.edge("protein"), lw=0.8))
            bio.label(ax, (cx, cy), f"{int(F[i, j])}", size="tiny",
                      color=P.ink() if (i, j) in on else P.muted(), bold=(i, j) in on)
    for (i1, j1), (i0, j0) in zip(path[:-1], path[1:]):
        a = (x0 + 0.5 + (j1 + 0.5) * cw, top - (i1 + 0.5) * cw)
        b = (x0 + 0.5 + (j0 + 0.5) * cw, top - (i0 + 0.5) * cw)
        bio.arrow(ax, a, b, kind="process", color=P.edge("protein"), shrink=0.3, head=0.14, lw=0.9)
bio.label(ax, (7.4, 0.55), "HEAGAWGHE-E / --P-AW-HEAE, score 1", size="small")
bio.label(ax, (19.8, 0.55), "AWGHE / AW-HE, score 28", size="small")
bio.panel(ax, "A", (0.2, 11.4))
bio.panel(ax, "B", (12.6, 11.4))
