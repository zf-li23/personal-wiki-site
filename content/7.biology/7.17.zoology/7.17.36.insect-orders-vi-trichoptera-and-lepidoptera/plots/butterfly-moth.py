# Characters used to tell butterflies from moths (schematic). (A) Antennae: clubbed in butterflies, with a
# hooked club in skippers; filiform or pectinate (feathery, especially in males) in most moths. (B) Wing
# coupling: in most moths a bristle on the hind wing (frenulum) is caught under a hook or a tuft of scales on
# the underside of the forewing (retinaculum); in butterflies and some large moths the frenulum is lost and
# the enlarged humeral lobe of the hind wing simply overlaps the forewing (amplexiform coupling). Exceptions
# occur in both directions.
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(26, 10.5)
bio.panel(ax, "A", (0.2, 10.3))
bio.label(ax, (6.2, 10.1), "Antennae", size="normal", bold=True)
ANT = [("clavate", 3.4, "butterfly:\nclubbed"), ("clavate", 2.8, "skipper:\nclub with hook"),
       ("filiform", 3.4, "moth:\nfiliform"), ("pectinate", 3.0, "moth (male):\npectinate")]
for i, (kind, L, t) in enumerate(ANT):
    x = 1.6 + i * 3.0
    a = zm.antenna(ax, (x, 3.0), 85, L, kind, colored=True)
    if i == 1:
        tip = (x + 0.3, 3.0 + L)
        ax.plot([tip[0] - 0.05, tip[0] + 0.5], [tip[1] - 0.1, tip[1] - 0.35], color=P.edge(zm.ANT["flagellum"]), lw=2.0)
    bio.label(ax, (x + 0.15, 1.9), t, size="tiny")

bio.panel(ax, "B", (13.0, 10.3))
bio.label(ax, (19.4, 10.1), "Wing coupling", size="normal", bold=True)
# frenate moth
f = zm.wing(ax, (14.0, 6.4), 5.0, "lepidoptera_fore", angle=10)
h = zm.wing(ax, (14.0, 6.0), 3.6, "lepidoptera_hind", angle=-25)
ax.plot([14.25, 15.4], [6.1, 6.55], color=P.edge("negative"), lw=1.6, zorder=12)
bio.callout(ax, (15.2, 6.5), (15.4, 9.3), "frenulum (hind wing)\ncaught by retinaculum", size="small")
bio.label(ax, (16.2, 1.6), "frenate (most moths)", size="small")
# amplexiform butterfly
f2 = zm.wing(ax, (21.0, 6.4), 5.0, "lepidoptera_fore", angle=10)
h2 = zm.wing(ax, (21.0, 6.0), 3.9, "lepidoptera_hind", angle=-15, chord=1.25)
bio.callout(ax, (22.0, 6.2), (22.6, 9.3), "humeral lobe overlaps\nforewing; no frenulum", size="small")
bio.label(ax, (23.2, 1.6), "amplexiform (butterflies)", size="small")
