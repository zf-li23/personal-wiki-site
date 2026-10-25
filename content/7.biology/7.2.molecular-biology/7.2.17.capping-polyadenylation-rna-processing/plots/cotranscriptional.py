# Cotranscriptional processing and termination by RNA polymerase II.
# A: one gene with Pol II at three stages. Near the promoter the CTD is phosphorylated on Ser5 and binds the
# capping enzyme, which caps the RNA before it is about 30 nt long; in the gene body Ser2 phosphorylation
# rises and splicing factors are recruited to exons as they emerge; after the poly(A) signal (PAS) the
# CPSF/CstF complex transferred from the CTD cleaves the RNA, the upstream product is polyadenylated, and the
# 5'-monophosphate end of the downstream RNA, still attached to Pol II, is degraded 5'->3' by Xrn2, which
# catches the polymerase and releases it (torpedo); PAS-dependent dephosphorylation of Spt5 slows Pol II.
# B: catch-up model. Cleavage occurs a time tau = 0.5 min after Pol II passes the PAS; Pol II then moves at v,
# Xrn2 at u > v. Termination occurs at x* = v tau u / (u - v) downstream of the PAS. Curves for u = 5 and
# 10 kb/min (illustrative values); the slowing of Pol II after the PAS shortens the termination zone.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 8.6)

bio.panel(ax, "A", (0.1, 8.45))
yd = 3.0
bio.dna(ax, (0.6, yd), (15.8, yd), style="duplex")
# gene features
bio.box(ax, (1.4, yd - 0.75), 1.2, 0.4, token="highlight", text="promoter", size="tiny", radius=0.05)
bio.box(ax, (11.2, yd - 0.75), 0.9, 0.4, token="negative", text="PAS", size="tiny", radius=0.05)
for a, b in ((2.0, 3.6), (6.0, 7.2), (9.2, 10.8)):
    bio.box(ax, ((a + b) / 2, yd - 0.75), b - a, 0.3, token="mrna", radius=0.04)
bio.label(ax, (4.8, yd - 0.75), "exons on the gene", size="tiny", color=P.muted())


def pol(x, text):
    MB.polymerase(ax, (x, yd + 0.35), 1.5, 1.2, "enzyme", text)


def ctd(x, marks, token):
    t = np.linspace(0, 1, 60)
    xx = x + 0.6 + 1.0 * t
    yy = yd + 0.9 + 1.3 * t + 0.12 * np.sin(t * 14)
    ax.plot(xx, yy, color=P.edge("enzyme"), lw=1.4, zorder=6)
    for k in range(5):
        i = 10 + k * 11
        bio.molecule(ax, (xx[i], yy[i]), token=token, r=0.11)
    bio.label(ax, (xx[-1] + 0.15, yy[-1] + 0.2), marks, size="tiny", color=P.edge(token), ha="left")
    return xx[-1], yy[-1]


# stage 1: capping
pol(2.4, "Pol II")
ctd(2.4, "Ser5-P", "highlight")
r = np.c_[np.linspace(1.9, 0.9, 30), yd + 1.3 + np.linspace(0, 1.4, 30)]
MB.backbone(ax, r, "mrna", lw=2.0)
ax.add_patch(bio.core.Circle(r[-1], 0.16, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=12))
bio.label(ax, (r[-1][0], r[-1][1] + 0.4), "m⁷G cap", size="tiny")
bio.protein(ax, (3.9, yd + 3.75), 2.0, 0.8, "positive", text="capping enzyme", size="tiny")
bio.label(ax, (2.4, yd - 1.5), "< 30 nt: cap", size="tiny", bold=True)

# stage 2: splicing
pol(7.4, "Pol II")
ctd(7.4, "Ser2-P", "antibody")
r2 = np.c_[np.linspace(6.9, 5.2, 40), yd + 1.3 + 1.6 * np.sin(np.linspace(0, 1.3, 40))]
MB.backbone(ax, r2, "mrna", lw=2.0)
bio.protein(ax, (8.4, yd + 3.75), 2.4, 0.8, "protein", text="U1, SR proteins", size="tiny")
bio.label(ax, (7.4, yd - 1.5), "gene body: splicing", size="tiny", bold=True)

# stage 3: cleavage and torpedo
pol(14.2, "Pol II")
ctd(14.2, "Ser2-P", "antibody")
x_cut = 11.6
up = np.c_[np.linspace(x_cut, 10.4, 20), yd + 1.4 + np.linspace(0, 1.2, 20)]
MB.backbone(ax, up, "mrna", lw=2.0)
bio.label(ax, (10.35, yd + 2.95), "AAAA…", size="tiny", color=P.edge("mrna"))
down = np.c_[np.linspace(12.3, 13.6, 20), yd + 1.3 + 0.1 * np.sin(np.linspace(0, 6, 20))]
MB.backbone(ax, down, "rna", lw=1.6, dashed=True)
bio.protein(ax, (12.1, yd + 1.35), 0.75, 0.6, "negative", text="Xrn2", size="tiny")
bio.arrow(ax, (12.6, yd + 2.0), (13.6, yd + 2.0), kind="process", color=P.edge("negative"))
bio.label(ax, (13.0, yd + 2.35), "5′→3′", size="tiny", color=P.edge("negative"))
bio.protein(ax, (12.2, yd + 3.75), 2.0, 0.8, "receptor", text="CPSF · CstF", size="tiny")
ax.plot([x_cut, x_cut], [yd + 1.0, yd + 1.7], color=P.edge("negative"), lw=1.0, ls=(0, (2, 1.4)))
bio.label(ax, (13.0, yd - 1.5), "after PAS: cleave, chase, release", size="tiny", bold=True)
bio.label(ax, (8.0, 8.1), "The CTD as a platform for processing factors", size="small", bold=True)

# --- B: torpedo catch-up ----------------------------------------------------------------------------------
bio.panel(ax, "B", (17.0, 8.45))
tau = 0.5
v = np.linspace(0.2, 4.5, 300)
pl = Q.Plot(ax, (18.6, 1.6, 5.8, 5.9), xlim=(0, 4.5), ylim=(0, 6), xlabel="Pol II speed after PAS / (kb min⁻¹)",
            ylabel="x* / kb", xticks=[0, 1, 2, 3, 4], yticks=[0, 2, 4, 6])
for u, tok, at in ((5.0, "negative", 0.75), (10.0, "dna", 0.85)):
    x = v * tau * u / (u - v)
    pl.line(v, x, tok, text=f"Xrn2 {u:g} kb/min", at=at, dx=(-0.3 if u < 6 else 0.2), dy=(0.35 if u < 6 else -0.45), ha=("right" if u < 6 else "left"))
pl.points([2.0], [2.0 * tau * 5 / 3], "negative")
pl.text(2.1, 1.35, "≈1.7 kb", ha="left")
bio.label(ax, (21.5, 8.1), "Torpedo: catch-up distance", size="small", bold=True)
