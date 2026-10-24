"""Fischer indole synthesis from phenylhydrazine and acetone. Top: the phenylhydrazone tautomerizes to
the ene-hydrazine; after protonation of the aryl-bearing nitrogen, a [3,3]-sigmatropic shift breaks
the weak N-N bond and forms a C-C bond to the ortho carbon, giving a di-imine. Bottom: tautomerization
restores the aromatic ring, the aniline nitrogen adds to the imine carbon to close the five-membered
ring, and loss of ammonia gives 2-methylindole."""

from wikichem import Scheme

s = Scheme()
s.molecule("CC(C)=NNc1ccccc1", at=(0, 0))
s.arrow((2.4, 0), (3.8, 0), kind="equilibrium", above="tautomerize", below=r"$+\mathrm{H^+}$")
eh = s.molecule(
    "[CH2:1]=[C:2]([CH3:7])[NH:3][NH2+:4][C:5]1=[CH:6][CH:8]=[CH:9][CH:10]=[CH:11]1",
    at=(6.6, 0),
    coords=[(1.0, 0.87), (1.5, 0.0), (2.5, 0.0), (1.0, -0.87), (0.0, -0.87), (-0.5, 0.0), (0.0, 0.87),
            (-0.5, 1.74), (-1.5, 1.74), (-2.0, 0.87), (-1.5, 0.0)],
)
s.partial(eh.xy(1), eh.xy(6))
s.curly(eh.bond(1, 2), eh.bond(1, 6), bend=-0.6)
s.curly(eh.bond(3, 4), eh.bond(2, 3), bend=-0.6)
s.curly(eh.bond(5, 6), eh.bond(4, 5), bend=0.6)
s.arrow((9.6, 0), (11.0, 0), above="[3,3]")
s.molecule("CC(=N)CC1C=CC=CC1=[NH2+]", at=(13.4, 0))
s.draw()

s = Scheme()
s.molecule("CC(=N)CC1C=CC=CC1=[NH2+]", at=(0, 0))
s.arrow((2.3, 0), (3.7, 0), above="tautomerize")
s.molecule("CC(=N)Cc1ccccc1N", at=(6.3, 0))
s.arrow((8.8, 0), (10.2, 0), above="ring", below="closure")
s.molecule("CC1(N)Cc2ccccc2N1", at=(12.4, 0))
s.arrow((15.1, 0), (16.5, 0), above=r"$\mathrm{H^+}$", below=r"$-\mathrm{NH_3}$")
s.molecule("Cc1cc2ccccc2[nH]1", at=(18.5, 0))
s.draw()
