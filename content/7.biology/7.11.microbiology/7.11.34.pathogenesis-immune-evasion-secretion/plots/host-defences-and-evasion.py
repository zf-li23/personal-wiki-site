# Four host defences a bacterium must survive, with the counter-strategy under each.
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(19.0, 8.6)
bio.label(ax, (9.5, 8.35), "Four defences, and what the pathogen does about each", size="title", bold=True)

W = 4.3
columns = [
    ("Antimicrobial peptides", "lysis", "cationic defensins and cathelicidins\nbind the negatively charged surface",
     "modify lipid A: aminoarabinose and\nphosphoethanolamine lower the charge\n(PhoP–PhoQ; the $\\it{mcr}$-1 gene)"),
    ("Complement", "lysis", "C3b opsonizes, C5a recruits,\nC5b–C9 lyses the outer membrane",
     "recruit factor H to the capsule;\ncleave C3b and C5a with proteases;\nlong O-antigen holds C5b–C9 away"),
    ("Phagocytes", "engulfment", "binding, engulfment, acidification,\nhydrolases and the oxidative burst",
     "capsule and M protein block binding;\nleukocidins kill the phagocyte;\ncatalase, SOD and peroxiredoxins"),
    ("Antibody", "opsonization", "neutralizes toxins and adhesins,\nopsonizes, activates complement",
     "IgA protease cuts secretory IgA;\nprotein A binds IgG by its Fc;\nantigenic and phase variation"),
]

for i, (title, _kind, attack, counter) in enumerate(columns):
    x = 0.4 + i * (W + 0.35)
    bio.box(ax, (x + W / 2, 7.55), W, 0.72, token="negative", radius=0.16)
    bio.label(ax, (x + W / 2, 7.55), title, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (x + W / 2, 6.55), attack, size="tiny", color=P.muted())

    # the bacterium under attack
    M.bacillus(ax, (x + W / 2, 4.55), 1.9, 0.78, gram="-")
    for s in (-1, 1):
        bio.arrow(ax, (x + W / 2 + s * 1.85, 5.35), (x + W / 2 + s * 0.95, 4.85), kind="process",
                  color=P.edge("negative"))

    bio.arrow(ax, (x + W / 2, 3.95), (x + W / 2, 3.55), kind="inhibition", color=P.edge("positive"))
    bio.box(ax, (x + W / 2, 2.45), W, 1.9, token="positive", radius=0.18)
    bio.label(ax, (x + W / 2, 3.05), "Counter-strategy", size="small", bold=True, color=P.on_fill())
    bio.label(ax, (x + W / 2, 2.25), counter, size="tiny", color=P.on_fill())

bio.label(ax, (9.5, 0.9), "A successful pathogen uses several at once: $\\it{Streptococcus\\ pneumoniae}$ has a capsule "
                          "(phagocytes and complement),\nbinds factor H, and secretes an IgA protease; the same factors "
                          "also let it colonize the nasopharynx harmlessly",
          size="tiny", color=P.muted())
