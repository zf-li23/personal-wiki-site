# From damage to mutation.
# A: lesions per genome for a constant damage rate kd = 1e4 per day and first-order repair with
#    half-lives of 1, 2 and 8 h (Eq. 8.2), starting from zero.
# B: de novo mutations in a child versus parental age at conception, approximate linear fits to the
#    Icelandic trio data of Jonsson et al. (Nature 2017): about 1.5 paternal and 0.4 maternal mutations
#    per year of age.
# C: somatic single-base substitutions in adult stem cells of colon, small intestine and liver, about
#    40 per genome per year (Blokzijl et al., Nature 2016), drawn as the fitted line.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(25, 7.8)
FT = bio.core.FONT["tiny"]

# A
a = C.axes_at(ax, (1.8, 1.4, 6.0, 5.2))
kd = 1e4 / 24.0                      # per hour
t = np.linspace(0, 48, 400)
for th, tok, ls in ((1, "dna", "-"), (2, "enzyme", "--"), (8, "negative", ":")):
    kr = np.log(2) / th
    n = kd / kr * (1 - np.exp(-kr * t))
    a.plot(t, n, color=C.line(tok), lw=1.8, ls=ls, label=f"t½ = {th} h")
    a.text(47, kd / kr * 1.04, f"N* = {kd / kr:,.0f}", fontsize=FT, color=C.line(tok), ha="right", va="bottom")
a.set_xlim(0, 48)
a.set_ylim(0, 5600)
a.set_xticks([0, 12, 24, 36, 48])
C.style_axes(a, "Time / h", "Lesions per genome")
a.legend(fontsize=FT, frameon=False, loc="center right", labelcolor=P.ink())
bio.panel(ax, "A", (0.5, 7.4))
bio.label(ax, (1.1, 7.4), "Lesion steady state", size="normal", bold=True, ha="left")

# B
b = C.axes_at(ax, (10.3, 1.4, 6.0, 5.2))
age = np.linspace(15, 45, 50)
pat = 6 + 1.51 * age
mat = 2.5 + 0.37 * age
b.plot(age, pat, color=C.line("channel"), lw=1.8, label="paternal")
b.plot(age, mat, color=C.line("receptor"), lw=1.8, ls="--", label="maternal")
b.set_xlim(15, 45)
b.set_ylim(0, 80)
C.style_axes(b, "Parental age at conception / years", "De novo mutations in the child")
b.legend(fontsize=FT, frameon=False, loc="upper left", labelcolor=P.ink())
b.text(44, 6 + 1.51 * 44 - 16, "+1.5 per year", fontsize=FT, color=C.line("channel"), ha="right")
b.text(44, 2.5 + 0.37 * 44 + 3, "+0.4 per year", fontsize=FT, color=C.line("receptor"), ha="right")
bio.panel(ax, "B", (9.0, 7.4))
bio.label(ax, (9.6, 7.4), "Germline mutations", size="normal", bold=True, ha="left")

# C
c = C.axes_at(ax, (18.8, 1.4, 5.6, 5.2))
yrs = np.linspace(0, 90, 50)
c.plot(yrs, 40 * yrs, color=C.line("dna"), lw=1.8)
c.set_xlim(0, 90)
c.set_ylim(0, 4000)
c.text(8, 3300, "about 40 per year\ncolon, small intestine, liver", fontsize=FT, color=P.ink())
C.style_axes(c, "Age / years", "Somatic mutations per stem cell")
bio.panel(ax, "C", (17.4, 7.4))
bio.label(ax, (18.0, 7.4), "Somatic mutations", size="normal", bold=True, ha="left")
