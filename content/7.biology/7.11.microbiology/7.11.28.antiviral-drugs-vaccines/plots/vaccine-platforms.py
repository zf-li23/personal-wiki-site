# Vaccine platforms: what is given, where the antigen is made, and what follows from that.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 8.6)

bio.label(ax, (9.5, 8.35), "Vaccine platforms: what is injected, and what the cell does with it",
          size="title", bold=True)

COLS = [
    (2.0, "Inactivated\nwhole virus", "virus",
     "killed virus particle", "taken up by antigen-\npresenting cells",
     "antibody; little CD8\nadjuvant and boosters\nneeded", "hepatitis A, rabies,\ninactivated polio"),
    (5.4, "Subunit protein", "protein",
     "purified antigen", "taken up by antigen-\npresenting cells",
     "defined and very safe\nadjuvant needed", "hepatitis B surface\nantigen, zoster gE"),
    (8.8, "Virus-like particle", "receptor",
     "capsid without a genome", "repetitive surface cross-\nlinks B-cell receptors",
     "strong antibody response\nnon-infectious", "HPV (L1), hepatitis B"),
    (12.2, "Live attenuated\nor viral vector", "positive",
     "replicating or antigen-\nexpressing virus", "antigen made inside\nthe cell",
     "antibody and CD8\ncold chain; care in\nimmunodeficiency", "measles, yellow fever;\nadenovirus-vectored"),
    (15.9, "mRNA in a lipid\nnanoparticle", "mrna",
     "modified mRNA,\nionizable lipid", "translated by the\nrecipient's own cells",
     "native conformation\nantibody and CD8\nnew antigen = new sequence", "COVID-19 mRNA\nvaccines"),
]

for x, name, token, what, where, props, examples in COLS:
    bio.label(ax, (x, 7.75), name, size="small", bold=True)
    bio.box(ax, (x, 6.55), 3.1, 1.0, token=token, radius=0.18)
    bio.label(ax, (x, 6.55), what, size="tiny", color=P.on_fill())
    bio.arrow(ax, (x, 5.95), (x, 5.55), kind="process")
    bio.box(ax, (x, 4.95), 3.1, 1.0, token="cytoplasm", radius=0.18)
    bio.label(ax, (x, 4.95), where, size="tiny")
    bio.arrow(ax, (x, 4.35), (x, 3.95), kind="process")
    bio.box(ax, (x, 3.25), 3.3, 1.35, token="highlight", radius=0.18)
    bio.label(ax, (x, 3.25), props, size="tiny", color=P.on_fill())
    bio.label(ax, (x, 2.1), examples, size="tiny", color=P.edge("virus"))

bio.label(ax, (0.25, 6.55), "given", size="tiny", color=P.muted(), ha="left", rotation=90)
bio.label(ax, (0.25, 4.95), "handled", size="tiny", color=P.muted(), ha="left", rotation=90)
bio.label(ax, (0.25, 3.25), "consequence", size="tiny", color=P.muted(), ha="left", rotation=90)

bio.box(ax, (9.5, 1.05), 17.4, 1.0, token="neutral", radius=0.18)
bio.label(ax, (9.5, 1.25), color=P.on_fill(), text="Antigen made inside a cell enters the MHC class I pathway and primes CD8 T cells; "
                           "antigen taken up from outside mainly gives antibody.", size="tiny")
bio.label(ax, (9.5, 0.85), "Adjuvants — alum, MF59, AS01, CpG 1018 — supply the innate signal that a purified "
                           "antigen does not carry; a live vaccine supplies its own.", size="tiny",
          color=P.on_fill())
