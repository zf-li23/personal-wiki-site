"""Methyl transfer from S-adenosylmethionine (SAM), as catalysed by catechol O-methyltransferase
(COMT). SAM is a sulfonium salt: Ado = 5'-deoxyadenosyl, R = the CH2CH2CH(NH3+)CO2- chain of
methionine. The phenoxide oxygen of dopamine (bound to Mg2+ in the enzyme, not shown) attacks the
methyl carbon from the side opposite to sulfur in an SN2 reaction; the neutral thioether
S-adenosylhomocysteine (SAH) is the leaving group."""

from wikichem import Scheme

import math


def facing(smiles, k, angle):
    """Rotation that makes atom k point in direction ``angle`` from the centre of the drawing."""
    m = Scheme().molecule(smiles)
    v = m.xy(k) - m.coords.mean(axis=0)
    return angle - math.degrees(math.atan2(v[1], v[0]))


s = Scheme()
CAT = "[O-]c1ccc(CCN)cc1O"
cat = s.molecule(CAT, at=(0, 0), rotate=facing(CAT, 0, 0), lone_pairs=[0])
sam = s.molecule("C[S+](*)*", coords=[(3.8, 0.0), (4.8, 0.0), (5.3, 0.87), (5.3, -0.87)], labels={2: "Ado", 3: "R"})
s.curly(cat.atom(0), sam.atom(0), bend=-0.4)
s.curly(sam.bond(0, 1), sam.atom(1), bend=-0.6)
s.arrow((6.4, 0), (8.0, 0), above="SN2")
x = 12.4
PROD = "COc1ccc(CCN)cc1O"
s.molecule(PROD, at=(x, 0), rotate=facing(PROD, 1, 0))
s.plus((x + 3.6, 0))
s.molecule("S(*)*", coords=[(0, 0), (0.87, 0.5), (-0.87, 0.5)], at=(x + 5.2, 0), labels={1: "Ado", 2: "R"})
s.text((x + 5.2, -1.0), "SAH", size=12)
s.draw()
