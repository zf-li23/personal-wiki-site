# Representatives of Neuropterida, of major beetle families and of Strepsiptera (PhyloPic silhouettes,
# not to scale), with field characters and approximate numbers of described species.
import wikibio as bio
from wikibio.icons import size as icon_size

P = bio.P
CELLS = [
    ('Megaloptera', 'dobsonflies', '~380', 'enzyme', 'phylopic/dobsonfly', 'broad hind-wing base; huge\nmandibles in males'),
    ('Raphidioptera', 'snakeflies', '~260', 'enzyme', 'phylopic/snakefly', 'long neck-like prothorax;\nlong ovipositor'),
    ('Neuroptera', 'lacewings', '~6,000', 'enzyme', 'phylopic/lacewing', 'veins forked at margin;\nwings roof-like'),
    ('Neuroptera', 'antlions', '~2,000', 'enzyme', 'phylopic/antlion', 'clubbed antennae; larva\nbuilds pit traps'),
    ('Coleoptera', 'ground beetles', '~40,000', 'protein', 'phylopic/ground-beetle', 'Carabidae: 5-5-5 tarsi;\nfiliform antennae'),
    ('Coleoptera', 'scarabs', '~35,000', 'protein', 'phylopic/scarab', 'Scarabaeidae: lamellate\nantennal club'),
    ('Coleoptera', 'ladybirds', '~6,000', 'protein', 'phylopic/ladybird', 'Coccinellidae: domed;\n4-4-4 (pseudotrimerous)'),
    ('Coleoptera', 'longhorn beetles', '~38,000', 'protein', 'phylopic/longhorn-beetle', 'Cerambycidae: very long\nantennae'),
    ('Coleoptera', 'weevils', '~65,000', 'protein', 'phylopic/weevil2', 'Curculionidae: rostrum;\ngeniculate clubbed antennae'),
    ('Strepsiptera', 'twisted-wing parasites', '~600', 'protein', 'phylopic/strepsipteran', 'male: club-like forewings,\nfan hind wings'),
]
NC, CW, CH = 5, 5.6, 5.4
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
for k, (name, tok) in enumerate([('Neuropterida', 'enzyme'), ('Coleopterida', 'protein')]):
    x = 1.0 + k * 9.0
    bio.box(ax, (x + 0.3, H - 0.8), 0.5, 0.5, token=tok)
    bio.label(ax, (x + 0.8, H - 0.8), name, size="small", ha="left")
bio.label(ax, (W - 0.3, H - 0.8), "Silhouettes not to scale", size="tiny", color=P.muted(), ha="right")
