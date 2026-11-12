# Representatives of the three paraneopteran orders and of the suborders of Hemiptera (PhyloPic
# silhouettes, not to scale), with field characters and approximate numbers of described species.
import wikibio as bio
from wikibio.icons import size as icon_size

P = bio.P
CELLS = [
    ('Psocodea', 'bark lice', '~5,600', 'protein', 'phylopic/barklouse', 'bulging postclypeus; long\nantennae; wings roof-like'),
    ('Psocodea', 'lice', '~5,000', 'protein', 'phylopic/louse', 'flat, wingless ectoparasites;\nclaws grasp hair'),
    ('Thysanoptera', 'thrips', '~6,000', 'protein', 'phylopic/thrips', 'fringed strap wings;\nasymmetric mouth cone'),
    ('Hemiptera', 'cicadas', '~3,000', 'enzyme', 'phylopic/cicada', 'Auchenorrhyncha: short bristle\nantennae; male tymbals'),
    ('Hemiptera', 'leafhoppers', '~22,000', 'enzyme', 'phylopic/leafhopper', 'Auchenorrhyncha: spiny hind\ntibiae; jump'),
    ('Hemiptera', 'aphids', '~5,000', 'enzyme', 'phylopic/aphid', 'Sternorrhyncha: siphunculi;\ncyclical parthenogenesis'),
    ('Hemiptera', 'stink bugs', '~5,000', 'enzyme', 'phylopic/stink-bug', 'Heteroptera: hemelytra;\nlarge scutellum; scent glands'),
    ('Hemiptera', 'water striders', '~750', 'enzyme', 'phylopic/water-strider', 'Heteroptera: hydrofuge hairs;\nskate on the surface'),
]
NC, CW, CH = 4, 5.6, 5.4
NR = (len(CELLS) + NC - 1) // NC
W, H = NC * CW, NR * CH + 1.6
fig, ax = bio.canvas(W, H)
for i, (order, common, n, tok, icon, chars) in enumerate(CELLS):
    c, r = i % NC, i // NC
    x0, y0 = c * CW, H - 1.6 - (r + 1) * CH
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.35), order, size="normal", bold=True)
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.85), f"{common} ({n} spp.)", size="tiny", color=P.muted())
    iw, ih = icon_size(icon)
    w = min(CW - 1.2, 2.6 * iw / ih)
    bio.icon(ax, icon, at=(x0 + CW / 2, y0 + 2.75), width=w, color=tok)
    bio.label(ax, (x0 + CW / 2, y0 + 0.75), chars, size="tiny")
for k, (name, tok) in enumerate([('Psocodea and Thysanoptera', 'protein'), ('Hemiptera', 'enzyme')]):
    x = 1.0 + k * 9.0
    bio.box(ax, (x + 0.3, H - 0.8), 0.5, 0.5, token=tok)
    bio.label(ax, (x + 0.8, H - 0.8), name, size="small", ha="left")
bio.label(ax, (W - 0.3, H - 0.8), "Silhouettes not to scale", size="tiny", color=P.muted(), ha="right")
