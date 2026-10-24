"""Ireland-Claisen rearrangement of allyl propanoate. LDA forms the ester enolate at -78 C and
chlorotrimethylsilane traps it on oxygen as a silyl ketene acetal. This is an allyl vinyl ether, so it
undergoes the [3,3]-sigmatropic (Claisen) shift already at or below room temperature, through a
chair-like six-membered transition state (drawn flat here; the dashed line is the forming C-C bond).
The product is the silyl ester of 2-methylpent-4-enoic acid, hydrolysed to the acid on work-up."""

import math

from wikichem import Scheme


def ring_xy(cx, cy, angle):
    return (cx + math.cos(math.radians(angle)), cy + math.sin(math.radians(angle)))


s = Scheme(scale=0.42)
y = 0.0
s.molecule("C=CCOC(=O)CC", at=(0.0, y))
s.text((0.0, y - 2.0), "allyl propanoate")
s.arrow((2.6, y), (4.4, y), above="1. LDA, $-78$ °C", below=r"2. Me$_3$SiCl")
cx = 6.9
# CH2=, CH, CH2, O, C, =CH, Me, O, SiMe3 on a hexagon (O at the left, the forming bond on the right)
ka = [ring_xy(cx, y, a) for a in (0, 60, 120, 180, 240, 300)]
far = lambda a, r: (cx + r * math.cos(math.radians(a)), y + r * math.sin(math.radians(a)))
coords = [ka[0], ka[1], ka[2], ka[3], ka[4], ka[5], far(300, 2.0), far(240, 2.0), (cx - 1.0, y - 2.4)]
k = s.molecule("C=CCOC(=CC)O*", coords=coords, labels={8: r"SiMe$_3$"})
s.partial(k.atom(0), k.atom(5))
s.curly(k.bond(4, 5), (k.xy(0) + k.xy(5)) / 2, bend=0.5)
s.curly(k.bond(2, 3), k.bond(3, 4), bend=0.6)
s.curly(k.bond(0, 1), k.bond(1, 2), bend=0.6)
s.text((cx, y - 3.2), "silyl ketene acetal")
s.arrow((8.9, y), (10.3, y), above="[3,3]", below="rt")
s.molecule("C=CCC(C)C(=O)O*", at=(13.0, y), labels={8: r"SiMe$_3$"})
s.arrow((16.3, y), (17.7, y), above=r"H$_3$O$^+$")
s.molecule("C=CCC(C)C(=O)O", at=(20.4, y))
s.text((20.4, y - 2.0), "2-methylpent-4-enoic acid")
s.draw()
