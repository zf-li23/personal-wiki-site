# A North Atlantic pelagic food web: organisms in rows by trophic level, arrows in the direction of
# energy flow (from food to consumer). Baleen whales feed mainly on krill and so sit with the
# secondary consumers; killer whales and great white sharks are apex predators.
import wikibio as bio
from wikibio import ecology

GREY = bio.P.muted()  # dark silhouettes for the large vertebrates

NODES = {
    "diatom": dict(level=0, x=0.5, text="Phytoplankton (diatoms)", icon="phylopic/diatom", token="thylakoid", size=0.9),
    "copepod": dict(level=1, x=0.28, text="Copepods", icon="phylopic/copepod", token="rna"),
    "krill": dict(level=1, x=0.72, text="Krill", icon="phylopic/krill", token="rna"),
    "herring": dict(level=2, x=0.25, text="Herring", icon="phylopic/herring", token="dna"),
    "squid": dict(level=2, x=0.58, text="Squid", icon="phylopic/squid", token="receptor", icon_opts={"rotate": 90}),
    "whale": dict(level=2, x=0.9, text="Baleen whales", icon="phylopic/baleen-whale", token=GREY,
                  icon_opts={"width": 2.6}),
    "cod": dict(level=3, x=0.1, text="Cod", icon="phylopic/cod", token="dna"),
    "seal": dict(level=3, x=0.45, text="Seals", icon="phylopic/harbour-seal", token="animal"),
    "tuna": dict(level=3, x=0.78, text="Bluefin tuna", icon="phylopic/bluefin-tuna", token="dna"),
    "orca": dict(level=4, x=0.32, text="Killer whale", icon="phylopic/orca", token=GREY, icon_opts={"width": 2.2}),
    "shark": dict(level=4, x=0.72, text="Great white shark", icon="phylopic/great-white-shark", token=GREY,
                  icon_opts={"width": 2.2}),
}
LINKS = [
    ("diatom", "copepod"), ("diatom", "krill"),
    ("copepod", "herring"), ("krill", "herring"), ("copepod", "squid"), ("krill", "squid"), ("krill", "whale"),
    ("herring", "whale", dict(bend=-0.2)),
    ("herring", "cod"), ("herring", "seal"), ("herring", "tuna", dict(bend=0.08)), ("squid", "tuna"), ("squid", "seal"),
    ("squid", "cod", dict(bend=0.1)), ("cod", "seal"),
    ("seal", "orca"), ("seal", "shark"), ("tuna", "orca", dict(bend=0.1)), ("tuna", "shark"),
]

fig, ax = bio.canvas(17, 12.4)
ecology.food_web(ax, NODES, LINKS, box=(0.3, 0.3, 16.4, 11.8), icon_size=0.95,
                 levels=["Primary producers", "Primary consumers", "Secondary consumers", "Tertiary consumers",
                         "Apex predators"])
