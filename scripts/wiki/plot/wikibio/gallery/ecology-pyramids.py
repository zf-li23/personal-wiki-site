# Ecological pyramids. (A) Energy flow at Silver Springs, Florida (Odum 1957), in kcal m^-2 yr^-1:
# widths on a log scale, transfer efficiencies at the left. (B) The inverted biomass pyramid of the
# English Channel (Harvey 1950), standing crop in g dry mass m^-2: a small but fast-growing
# phytoplankton stock supports a larger zooplankton stock. (C) Age-sex pyramids of an expanding and a
# contracting population (illustrative stationary-model shapes, % of the population per 5-year class).
import numpy as np

import wikibio as bio
from wikibio import ecology

fig, ax = bio.canvas(28.6, 11.5)

bio.panel(ax, "A", (0.3, 11.2))
bio.label(ax, (5.2, 11.0), "Energy (Silver Springs)", size="normal", bold=True)
ecology.pyramid(ax, (5.0, 6.2), [
    dict(text="Producers", value=20810, token="plant"),
    dict(text="Herbivores", value=3368, token="positive"),
    dict(text="Carnivores", value=383, token="highlight"),
    dict(text="Top carnivores", value=21, token="rna"),
], width=7.0, height=1.0, scale="log", unit="kcal m⁻² yr⁻¹", transfer=True)

bio.panel(ax, "B", (0.3, 5.0))
bio.label(ax, (5.2, 4.8), "Biomass (English Channel)", size="normal", bold=True)
ecology.pyramid(ax, (4.6, 1.4), [
    dict(text="Phytoplankton", value=4, token="plant"),
    dict(text="Zooplankton", value=21, token="rna"),
], width=6.0, height=1.2, scale="linear", unit="g m⁻²", min_width=1.8)

ages = [f"{a}–{a + 4}" for a in range(0, 80, 5)] + ["80+"]
mid = np.arange(2.5, 85, 5)


def structure(growth, b=0.0002, g=0.085, female_mortality=0.7):
    # stable age structure with growth rate r: n(a) ~ exp(-r a) * l(a), with Gompertz survivorship l(a)
    # (lower mortality in females); returns % of the whole population per class for males, females
    def l(bb):
        return np.exp(-(bb / g) * (np.exp(g * mid) - 1))

    m, f = np.exp(-growth * mid) * l(b), np.exp(-growth * mid) * l(b * female_mortality)
    total = m.sum() + f.sum()
    return 100 * m / total, 100 * f / total


for k, (title, r) in enumerate((("Expanding (r = 3% / yr)", 0.03), ("Contracting (r = −1% / yr)", -0.01))):
    cx = 16.4 + k * 8.0
    m, f = structure(r)
    ecology.age_pyramid(ax, (cx, 1.2), ages, m, f, scale=0.36, bar=0.42, gap=1.15, ticks=[0, 2, 4, 6, 8], title=title)
bio.panel(ax, "C", (12.4, 11.2))
