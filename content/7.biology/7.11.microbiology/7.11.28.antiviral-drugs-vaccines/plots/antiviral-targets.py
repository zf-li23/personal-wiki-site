# Antiviral drug classes placed on the steps of the replication cycle.
# The cycle is drawn as a ring of steps; each inhibited step carries its drug class and examples.
import wikibio as bio
from wikibio import ecology

P = bio.P
fig, ax = bio.canvas(17.6, 9.4)

bio.label(ax, (5.2, 9.15), "Where antiviral drugs act", size="title", bold=True)

STEPS = ["Attachment\nand entry", "Uncoating", "Genome\nreplication", "Integration\n(retroviruses)",
         "Protein synthesis\nand processing", "Assembly", "Release"]
ecology.cycle(ax, (5.2, 4.5), 2.9, STEPS, token="virus", size="small", start=100, clockwise=True)

DRUGS = [
    ("Attachment and entry", "maraviroc (CCR5, host-directed)\nenfuvirtide (gp41 heptad repeat)", 8.55),
    ("Uncoating", "amantadine (influenza A M2 channel)", 7.25),
    ("Genome replication", "nucleoside and nucleotide analogues:\nacyclovir, tenofovir, sofosbuvir, remdesivir\n"
     "non-nucleoside RT inhibitors: nevirapine\nbaloxavir (cap-snatching endonuclease)", 5.55),
    ("Integration", "raltegravir, dolutegravir\n(strand-transfer inhibitors)", 3.65),
    ("Polyprotein processing", "protease inhibitors: darunavir (HIV-1),\nglecaprevir (HCV), nirmatrelvir (SARS-CoV-2)",
     2.25),
    ("Release", "oseltamivir, zanamivir\n(neuraminidase inhibitors)", 0.95),
]
x_box = 13.2
for title, drugs, y in DRUGS:
    bio.box(ax, (x_box, y), 7.4, 1.0 if drugs.count("\n") < 2 else 1.55, token="drug", radius=0.18)
    bio.label(ax, (x_box - 3.5, y + (0.55 if drugs.count("\n") > 1 else 0.28)), title, size="small",
              bold=True, ha="left", color=P.on_fill())
    bio.label(ax, (x_box - 3.5, y - (0.18 if drugs.count("\n") > 1 else 0.18)), drugs, size="tiny",
              color=P.on_fill(), ha="left")

bio.label(ax, (5.2, 4.5), "one\nreplication\ncycle", size="small", color=P.muted())
bio.label(ax, (5.2, 0.5), "a host-directed drug cannot be escaped by mutating the target,\n"
                           "but necessarily interferes with a cellular function", size="tiny", color=P.muted())
bio.label(ax, (13.2, 9.15), "Drug classes and examples", size="small", bold=True)
