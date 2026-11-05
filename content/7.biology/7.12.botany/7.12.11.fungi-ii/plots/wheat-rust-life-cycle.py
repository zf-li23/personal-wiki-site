"""Life cycle of the wheat stem rust Puccinia graminis, a heteroecious macrocyclic rust with five spore
stages (0-IV). Blue band: dikaryotic (n + n) phase; orange band: haploid (n) phase."""
import wikibio as bio
from wikibio import ecology

P = bio.P
fig, ax = bio.canvas(22, 16)
c = (11.0, 8.0)
st = [
    dict(text="II  Urediniospores (n + n)\nred rust on wheat; repeat\ncycles every 7-12 days", icon="phylopic/wheat",
         icon_size=1.3, icon_color="plant", size="small", extent=(4.2, 2.6)),
    dict(text="III  Teliospores (n + n)\ntwo-celled, thick-walled;\nblack rust; karyogamy (2n)", size="small", shape="box"),
    dict(text="IV  Basidium and\nbasidiospores (n), + and -", size="small", shape="box"),
    dict(text="0  Spermogonia (n) on upper\nside of barberry leaf;\nspermatia, receptive hyphae", size="small", shape="box"),
    dict(text="I  Aecia (n + n) on lower\nside of barberry leaf;\naeciospores", size="small", shape="box"),
]
ecology.cycle(ax, c, 5.6, st, start=90, gap=0.25,
              arrow_labels=["Late season", dict(text="Meiosis (spring)", bold=True, color=P.edge("rna")),
                            "Wind to barberry", dict(text="Plasmogamy (insects)", bold=True, color=P.edge("dna")),
                            "Wind to wheat"],
              sectors=[dict(start=3.5, end=6.5, token="dna", text="", r0=3.4, r1=7.6),
                       dict(start=1.5, end=3.5, token="rna", text="", r0=3.4, r1=7.6)])
bio.label(ax, (11.0, 9.6), "Wheat (primary host)", size="title", bold=True, color=P.edge("plant"))
bio.label(ax, (11.0, 6.4), "Barberry (alternate host)", size="title", bold=True, color=P.edge("plant"))
bio.label(ax, (11.0, 8.0), "Puccinia graminis", size="normal", italic=True, color=P.muted())
bio.label(ax, (0.4, 0.5), "Blue: dikaryotic (n + n)   Orange: haploid (n)", size="tiny", ha="left", color=P.muted())
