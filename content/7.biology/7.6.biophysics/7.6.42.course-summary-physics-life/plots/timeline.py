"""Experiments and models that shaped biophysics, 1912-2024, with the chapters (7.6.n) where they appear.

Left of the time axis: molecular biophysics (structures, methods, single molecules); right: cell
biophysics and quantitative biology, and the physicists' early arguments about the gene (grey).
Years as given in the chapters: Laue 1912 and the Braggs 1913 (10); the three-man paper 1935 and
What Is Life? 1944 (1); the fluctuation test 1943 (32); Hodgkin and Huxley 1952 (30); the double
helix 1953 (10); myoglobin at 6 A 1957 (10); the growth observations of Schaechter, Maaloe and Kjeldgaard
1958 (39); MWC 1965 (4); FRET as a ruler 1967 (11); the PDB 1971 (1); kinetic proofreading 1974
(17); low-dose electron crystallography 1975 (14); the patch clamp 1976 (30); Berg and Purcell 1977
(35); vitrification 1982 (14); NMR structures 1985 (13); optical tweezers 1986 (17); kinesin steps
1993 (27); smFRET 1996 (12); F1 rotation and robust adaptation 1997 (28, 35); the repressilator
2000 (33); the Jarzynski equality tested and intrinsic and extrinsic noise 2002 (17, 32); PALM
2006 (12); liquid P granules 2009 (29); the cryo-EM resolution revolution 2013 (14); the 2017
Nobel Prize (14); AlphaFold2 2020 (15); the 2024 Nobel Prize (15)."""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT
M, C, Q, G = "protein", "membrane", "dna", "neutral"

events = [
    (1912, "Laue: X-ray diffraction by crystals (10)", M),
    (1913, "the Braggs: Bragg's law (10)", M),
    (1935, "three-man paper: the gene is a molecule (1)", G),
    (1943, "Luria–Delbrück fluctuation test (32)", Q),
    (1944, "Schrödinger, What Is Life? (1)", G),
    (1952, "Hodgkin–Huxley model of the action potential (30)", C),
    (1953, "double helix from fiber diffraction (10)", M),
    (1957, "myoglobin at 6 Å, the first protein map (10)", M),
    (1958, "growth rate sets ribosome content (39)", Q),
    (1965, "MWC model of allostery (4)", M),
    (1967, "FRET as a spectroscopic ruler (11)", M),
    (1971, "Protein Data Bank founded (1)", M),
    (1974, "kinetic proofreading (17, 38)", Q),
    (1975, "low-dose electron crystallography (14)", M),
    (1976, "patch clamp: one channel at a time (30)", C),
    (1977, "Berg–Purcell limit of sensing (35)", Q),
    (1982, "vitrified specimens for cryo-EM (14)", M),
    (1985, "protein structures by NMR (13)", M),
    (1986, "optical tweezers (17)", M),
    (1993, "8 nm steps of single kinesins (27)", C),
    (1996, "single-molecule FRET (12)", M),
    (1997, "rotation of F₁-ATPase seen (28)", C),
    (1997, "robust perfect adaptation (35, 40)", Q),
    (2000, "repressilator (33)", Q),
    (2002, "Jarzynski equality tested on RNA (17)", M),
    (2002, "intrinsic and extrinsic noise (32)", Q),
    (2006, "PALM localization microscopy (12)", M),
    (2009, "P granules are liquid droplets (29)", C),
    (2013, "cryo-EM resolution revolution (14)", M),
    (2017, "Nobel Prize for cryo-EM (14)", M),
    (2020, "AlphaFold2 (15)", M),
    (2024, "Nobel Prize for structure prediction and design (15)", M),
]

Y0, Y1 = 1908, 2028
H = 9.2  # figure height in inches
fig, ax = plt.subplots(figsize=(8.6, H))
fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.03)
ax.set_xlim(-1, 1)
ax.set_ylim(Y1, Y0)
ax.axis("off")
ax.plot([0, 0], [Y0 + 2, Y1 - 2], color=P.ink(), lw=1.0)
for y in range(1910, 2030, 10):
    ax.plot([-0.012, 0.012], [y, y], color=P.ink(), lw=0.8)
    ax.text(-0.99, y, str(y), fontsize=F["tiny"], color=P.muted(), ha="left", va="center")
    ax.plot([-0.93, -0.9], [y, y], color=P.muted(), lw=0.6)

# spread labels on each side so that neighbours keep a minimum gap (in years)
GAP = 3.1


def spread(ys):
    out = []
    for y in ys:
        out.append(max(y, out[-1] + GAP) if out else y)
    # shift back up if the bottom overflows
    over = out[-1] - (Y1 - 1) if out else 0
    if over > 0:
        out = [y - over for y in out]
        for i in range(len(out) - 2, -1, -1):
            out[i] = min(out[i], out[i + 1] - GAP)
    return out


left = [e for e in events if e[2] == M]
right = [e for e in events if e[2] != M]
for side, evs in ((-1, left), (1, right)):
    ys = spread([e[0] for e in evs])
    for (year, text, tok), yl in zip(evs, ys):
        ax.plot([0], [year], "o", ms=5, mfc=P.fill(tok), mec=P.edge(tok), mew=0.9, zorder=5)
        xl = side * 0.12
        ax.plot([0, side * 0.05, xl], [year, year, yl], color=P.edge(tok), lw=0.6, zorder=4)
        ax.text(xl + side * 0.01, yl, f"{year}  {text}" if side > 0 else f"{text}  {year}", fontsize=F["tiny"],
                color=P.ink(), ha="left" if side > 0 else "right", va="center")
ax.text(-0.5, Y0 - 1, "molecular biophysics", fontsize=F["small"], color=charts.line(M), ha="center", weight="bold")
ax.text(0.5, Y0 - 1, "cell biophysics, quantitative biology", fontsize=F["small"], color=charts.line(Q),
        ha="center", weight="bold")
