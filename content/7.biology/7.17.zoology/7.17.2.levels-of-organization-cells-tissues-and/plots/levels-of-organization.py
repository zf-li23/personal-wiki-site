"""Grades of organization in animals, illustrated by living representatives (silhouettes from PhyloPic).

A choanoflagellate is a single cell (some species form colonies of similar cells). Sponges are at the
cellular grade: several cell types, but no tissues in the strict sense and no organs. Cnidarians are at
the tissue grade: two epithelia (with a nerve net and epitheliomuscular cells) separated by mesoglea.
Flatworms have organs (pharynx, protonephridia, gonads) built of several tissues; annelids and
vertebrates have organ systems (circulatory, excretory, nervous). The sequence is a series of grades,
not a line of descent: the living species are not ancestors of one another.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 10.2)
STEPS = [
    ("Unicellular", "Choanoflagellate", "one cell; colonies of\nsimilar cells", "phylopic/choanoflagellate", dict(width=2.0)),
    ("Cellular grade", "Sponge (Porifera)", "several cell types,\nno true tissues", "phylopic/sponge", dict(height=2.2)),
    ("Tissue grade", "Hydra (Cnidaria)", "two epithelia,\nnerve net", "phylopic/hydra", dict(height=2.4)),
    ("Organ grade", "Planarian (Platyhelminthes)", "organs of several\ntissues", "phylopic/planarian", dict(width=2.6)),
    ("Organ-system grade", "Earthworm (Annelida)", "organs linked into\nsystems", "phylopic/earthworm", dict(width=3.0)),
]
X = [2.4 + 5.05 * i for i in range(5)]
for k, (x, (grade, name, note, icon, size)) in enumerate(zip(X, STEPS)):
    y_step = 1.6 + 0.9 * k
    bio.box(ax, (x, y_step), 4.3, 0.75, token="animal" if k else "neutral", text=grade, size="small")
    bio.label(ax, (x, 9.8), name, size="small", bold=True)
    bio.label(ax, (x, 0.55), note, size="tiny", color=P.muted(), va="center")
    if k < 4:
        bio.arrow(ax, (x + 2.2, y_step + 0.1), (X[k + 1] - 2.2, y_step + 0.8), kind="process", color=P.muted())
_ = ["phylopic/choanoflagellate", "phylopic/sponge", "phylopic/hydra", "phylopic/planarian", "phylopic/earthworm"]
bio.icon(ax, "phylopic/choanoflagellate", at=(X[0], 7.6), width=2.0, color="neutral")
bio.icon(ax, "phylopic/sponge", at=(X[1], 7.6), height=2.2, color="animal")
bio.icon(ax, "phylopic/hydra", at=(X[2], 7.6), height=2.4, color="animal")
bio.icon(ax, "phylopic/planarian", at=(X[3], 7.6), width=2.6, color="animal")
bio.icon(ax, "phylopic/earthworm", at=(X[4], 7.6), width=3.0, color="animal")
