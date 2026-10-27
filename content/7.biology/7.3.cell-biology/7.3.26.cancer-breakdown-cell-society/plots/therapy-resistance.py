"""Why tumors relapse after targeted monotherapy and why combinations help (Goldie-Coldman and
Luria-Delbruck reasoning).

(A) A tumor grows from one cell to N cells; resistance to a drug arises by mutation at rate mu per division
(about N divisions in total), so the expected number of resistance mutations before treatment is about mu N
and the probability that at least one resistant cell exists is P = 1 - exp(-mu N). For a single drug with
mu = 1e-7 a tumor of 1e9 cells (about 1 cm^3, near the limit of clinical detection) almost certainly
contains resistant cells; resistance to two drugs with independent mechanisms requires two mutations,
rate mu^2 = 1e-14, and becomes likely only when the tumor holds about 1e14 cells.
(B) Treatment of a detected tumor (1e9 cells). With one drug, sensitive cells die at net rate 0.1 per day,
but about 100 pre-existing resistant cells grow at 0.03 per day: the tumor shrinks below detection
(remission) and returns (relapse) from the resistant clone. With two drugs, cells resistant to one drug
are killed by the other; double-resistant cells are absent (expected number 1e-5), and the tumor is
eradicated (below one cell).
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(20.0, 9.0)

bio.panel(ax, "A", (0.2, 8.8))
A = charts.axes_at(ax, (1.8, 1.5, 6.8, 6.6))
N = np.geomspace(1e5, 1e15, 300)
for m, tok, lab in ((1e-7, "negative", "one drug (rate 1e-7)"), (1e-14, "positive", "two drugs (rate 1e-14)")):
    A.semilogx(N, 1 - np.exp(-m * N), color=charts.line(tok), lw=1.8, label=lab)
A.axvline(1e9, color=P.muted(), ls="--", lw=0.8)
A.text(1.3e9, 0.55, "detection\n(about 1e9 cells)", fontsize=FT["tiny"], color=P.muted())
A.set_ylim(0, 1.05)
A.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(A, "tumor size N (cells)", "probability of pre-existing resistance")

bio.panel(ax, "B", (10.4, 8.8))
B = charts.axes_at(ax, (12.2, 1.5, 7.0, 6.6))
t = np.linspace(0, 600, 601)
S0, R0, k, g = 1e9, 100.0, 0.1, 0.03
mono = S0 * np.exp(-k * t) + R0 * np.exp(g * t)
combo = S0 * np.exp(-k * t) + 1e-5 * np.exp(g * t) + 2 * R0 * np.exp(-k * t)
B.semilogy(t, mono, color=charts.line("negative"), lw=1.8, label="one drug: remission, then relapse")
B.semilogy(t, np.where(np.cumsum(combo < 1) == 0, combo, np.nan), color=charts.line("positive"), lw=1.8,
           label="two drugs: eradication")
B.semilogy(t, R0 * np.exp(g * t), color=charts.line("negative"), lw=0.8, ls=":", label="resistant clone")
B.axhline(1e9, color=P.muted(), ls="--", lw=0.8)
B.text(380, 1.6e9, "detection limit", fontsize=FT["tiny"], color=P.muted())
B.axhline(1, color=P.muted(), ls=":", lw=0.8)
B.text(380, 1.6, "one cell", fontsize=FT["tiny"], color=P.muted())
B.set_ylim(0.1, 1e11)
B.set_xlim(0, 600)
B.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(B, "time after start of treatment / days", "tumor cells")
