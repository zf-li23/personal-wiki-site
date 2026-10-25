---
title: The Three-Dimensional Structure of Proteins
description: Weak interactions and the planar peptide group; dihedral angles and a hard-sphere Ramachandran map computed from scratch; the α helix, β sheets and β turns; helical wheels and hydrophobic moments; α-keratin, collagen and silk; tertiary structure, motifs, domains and intrinsically disordered proteins; structural classification; quaternary structure and symmetry.
---

A protein chain of a few hundred residues could in principle adopt an astronomical number of shapes, yet under physiological conditions most proteins spend nearly all their time in one compact, specific structure, and that structure determines what they do. This chapter follows the main line of Part I of the course, *chemical properties → structure → function*: the partial double-bond character of the **peptide bond** and the steric bulk of the backbone restrict each residue to a few combinations of two **torsion angles**; within these limits, hydrogen bonds between backbone groups generate the regular secondary structures (the α helix and the β sheet); and the burial of nonpolar side chains, together with many weak interactions, packs these elements into the tertiary and quaternary structures of fibrous and globular proteins. The amino acids themselves and the chemistry of the peptide bond were treated in [7.1.3](/7.1.3) and in [6.5.33](/6.5.33#sec-33.5); the next chapter asks how a chain reaches its native structure and how that structure is determined experimentally, and [7.1.7](/7.1.7) shows how structure becomes function in myoglobin, hemoglobin and antibodies.

## 5.1. Overview of Protein Structure

### 5.1.1. Conformation and the Native State

The **conformation** of a protein is the spatial arrangement of its atoms; different conformations interconvert without breaking covalent bonds, mainly by rotation about single bonds. Of the enormous number of conformations available to a polypeptide, one or a small set is thermodynamically most stable (lowest Gibbs energy) under a given set of conditions.

**Definition 5.1.1 (Native Conformation)** A protein in any of its functional, folded conformations is called a **native protein**, and those conformations are its **native conformation**.

Native proteins are only marginally stable: the Gibbs energy difference between the folded and unfolded states of a typical protein under physiological conditions is only about $5$–$65\ \mathrm{kJ\,mol^{-1}}$ (the thermodynamics of this balance is the subject of [7.1.6](/7.1.6)). Marginal stability is not a defect. Most proteins must change conformation as they bind ligands or catalyze reactions, and a structure that could not flex would not work. Some proteins, or segments of them, have no stable structure at all (§5.4.3).

### 5.1.2. Weak Interactions Stabilize the Native Conformation

The unfolded chain has a large conformational entropy, and its polar groups are hydrogen-bonded to water; both favor unfolding. Folding is opposed by these effects and driven by the interactions summarized below.

| Interaction | Typical strength | Role in folded proteins |
|---|---|---|
| Covalent bond (for comparison) | $200$–$460\ \mathrm{kJ\,mol^{-1}}$ | sets the chain; not broken by folding |
| **Disulfide bond** | covalent, but rare inside cells | cross-links mainly secreted and extracellular proteins (insulin); common in thermophiles |
| Hydrophobic effect | entropic; dominant | clusters Leu, Ile, Val, Phe, Trp into a core away from water |
| **Hydrogen bond** | $\sim 4$–$20\ \mathrm{kJ\,mol^{-1}}$ each, but net $\approx 0$ | each one formed replaces one with water; cooperative networks in helices and sheets guide folding |
| Ion pair (salt bridge) | stronger in low-$\varepsilon$ interior | can stabilize or destabilize; buried ion pairs are enriched in thermophilic proteins |
| **van der Waals force** | $\sim 0.4$–$4\ \mathrm{kJ\,mol^{-1}}$ per contact, range $0.3$–$0.6\ \mathrm{nm}$ | individually weak, numerous in the densely packed core |

Three points deserve emphasis.

- *The hydrophobic effect predominates.* Water forms an ordered solvation shell around nonpolar groups; when these groups cluster in the protein interior the shell shrinks and the entropy of the water increases (the thermodynamics is developed in [7.1.2](/7.1.2)). This gain more than compensates for the loss of conformational entropy of the chain.
- *Hydrogen bonds and ion pairs contribute little net free energy, but unpaired polar groups are very costly.* A hydrogen bond formed inside the protein replaces one to water, so its net contribution is close to zero; but a hydrogen-bonding group buried without a partner costs so much that such conformations are essentially forbidden. The strength of an ion pair grows as it moves from water (dielectric constant $\varepsilon \approx 80$) into the protein interior ($\varepsilon \approx 4$).
- *Disulfide bonds are the exception.* The cytosol is highly reducing (millimolar glutathione), so intracellular proteins rarely contain disulfides; they are found mainly in proteins that function in the oxidizing extracellular space.

Most structural patterns in this chapter follow from two simple rules: hydrophobic residues are largely buried, and the number of hydrogen bonds and ionic interactions within the protein is maximized, so that few hydrogen-bonding or ionic groups are left without a partner. Membrane proteins ([7.1.13](/7.1.13)) and intrinsically disordered proteins follow different rules.

### 5.1.3. The Peptide Group Is Rigid and Planar

The covalent geometry of the backbone imposes the first constraint on conformation. In the late 1930s Linus Pauling and Robert Corey found, from crystal structures of amino acids and small peptides, that the peptide C–N bond ($0.132\ \mathrm{nm}$) is intermediate between a C–N single bond ($0.149\ \mathrm{nm}$) and a C=N double bond ($0.127\ \mathrm{nm}$), and that the six atoms $\mathrm{C}_\alpha$–C(=O)–N(H)–$\mathrm{C}_\alpha$ lie in one plane. Resonance between the two structures $\ce{O=C-NH <-> O^- -C=N^+H}$ gives the C–N bond partial double-bond character and prevents rotation about it (the chemistry of this resonance is in [6.5.33](/6.5.33#sec-33.5.2)). The oxygen carries a partial negative charge and the amide hydrogen a partial positive charge, so each peptide group is a small electric dipole. Note that quantum-chemical analyses give the amide nitrogen a net charge that is neutral or slightly negative; the "$\mathrm{N^+}$" of the resonance formula is a bookkeeping device.

The backbone is therefore a chain of rigid planes that share the $\mathrm{C}_\alpha$ atoms as swivels. In the planar peptide group the carbonyl oxygen is almost always *trans* to the amide hydrogen: more than $99.95\%$ of peptide bonds not involving proline are trans, whereas about $6\%$ of the X–Pro bonds (in which the nitrogen belongs to the proline ring) are cis, many of them in β turns.

**Definition 5.1.2 (Backbone Dihedral Angles)** The conformation of the backbone of residue $i$ is described by three **torsion angles** (dihedral angles), each defined by four consecutive backbone atoms: $\varphi$ (phi) by $\mathrm{C}_{i-1}$–$\mathrm{N}_i$–$\mathrm{C}_{\alpha,i}$–$\mathrm{C}_i$ (rotation about N–$\mathrm{C}_\alpha$), $\psi$ (psi) by $\mathrm{N}_i$–$\mathrm{C}_{\alpha,i}$–$\mathrm{C}_i$–$\mathrm{N}_{i+1}$ (rotation about $\mathrm{C}_\alpha$–C), and $\omega$ by $\mathrm{C}_{\alpha,i}$–$\mathrm{C}_i$–$\mathrm{N}_{i+1}$–$\mathrm{C}_{\alpha,i+1}$ (rotation about the peptide bond).

By convention $\varphi = \psi = \pm 180^\circ$ in the fully extended chain, and, looking along the central bond, the angle increases as the fourth atom rotates clockwise relative to the first. The planar trans peptide group fixes $\omega \approx 180^\circ$ ($\omega = 0^\circ$ for the rare cis bond), so the conformation of each residue is specified by the pair $(\varphi, \psi)$. The conformation $\varphi = \psi = 0^\circ$, in which the first and fourth atoms are eclipsed, is itself sterically impossible and serves only as the reference point.

## 5.2. Secondary Structure

### 5.2.1. Regular Local Structures

**Definition 5.2.1 (Secondary Structure)** The **secondary structure** of a segment of a polypeptide chain is the local spatial arrangement of its main-chain atoms, without regard to the positions of its side chains or its relation to other segments. The secondary structure is **regular** when $\varphi$ and $\psi$ remain the same, or nearly so, throughout the segment.

Two regular structures are especially stable and widespread: the α helix and the β conformation, both proposed by Pauling and Corey (1951) before any protein structure had been solved; the β turn is a common third type. Segments without a regular pattern are sometimes called "random coil", but the term is misleading: in a folded protein the path of such a segment is highly specific, merely not repetitive. A uniform chain in which every residue has the same $(\varphi, \psi)$ is always a helix in the geometric sense, with $n$ residues per turn and a rise $d$ per residue; the α helix, the β strand (a flattened helix with $n = 2$) and the polyproline II helix are particular solutions.

### 5.2.2. The α Helix

**Definition 5.2.2 (α Helix)** The **α helix** is a right-handed helical backbone conformation with $\varphi \approx -57^\circ$, $\psi \approx -47^\circ$, about $3.6$ residues per turn and a pitch of about $0.54\ \mathrm{nm}$ (rise $0.15\ \mathrm{nm}$ per residue), in which the C=O group of residue $i$ is hydrogen-bonded to the N–H group of residue $i+4$.

The helix is the simplest arrangement that uses every backbone N–H and C=O in an internal hydrogen bond: each successive turn is held to its neighbors by three to four hydrogen bonds, roughly parallel to the axis. Only the three or four N–H groups at the N-terminal end and C=O groups at the C-terminal end lack helical partners; they bond to water or are capped by other groups of the protein. The side chains project outward and slightly backward toward the N-terminus, and the interior of the helix is filled by the backbone atoms themselves. About a quarter of all residues in proteins are in α helices. Left-handed α helices ($\varphi, \psi \approx +57^\circ, +47^\circ$) are possible for single residues but have not been observed as extended segments: for L-amino acids they bring the side chain into contact with the backbone carbonyl.

**Example 5.2.1** A polypeptide of $80$ residues forms a single continuous α helix. With a rise of $0.54\ \mathrm{nm}/3.6 = 0.15\ \mathrm{nm}$ per residue, its length is $80 \times 0.15\ \mathrm{nm} = 12\ \mathrm{nm}$. The same chain fully extended in a β strand ($0.35\ \mathrm{nm}$ per residue) would be $28\ \mathrm{nm}$ long.

Related helices differ in the spacing of the hydrogen bonds. The $3_{10}$ helix ($i \to i+3$, $3.0$ residues per turn, rise $0.20\ \mathrm{nm}$) is tighter and occurs mostly as short pieces at the ends of α helices; the π helix ($i \to i+5$) is wider and rare.

*Sequence determines helix stability.* Not every sequence can form a stable α helix. Five kinds of constraint act together:

1. the intrinsic propensity of each residue: Ala is the strongest helix former in most model systems; Leu, Met, Glu and Lys are also favorable;
2. interactions between side chains three or four residues apart, which are neighbors on the same face of the helix: an oppositely charged pair at $i, i+3$ or $i, i+4$ forms a stabilizing ion pair, two aromatic side chains at that spacing pack together; a long run of Glu (or of Lys and Arg) at pH 7 cannot form a helix because the like charges repel;
3. the bulk and shape of adjacent side chains: Asn, Ser, Thr and Cys destabilize a helix when clustered;
4. Pro and Gly: in Pro the nitrogen is part of a rigid ring, so rotation about N–$\mathrm{C}_\alpha$ is impossible, and it has no amide hydrogen to donate, so Pro introduces a kink and is rare except in the first turn; Gly is so flexible that it favors other conformations;
5. interactions with the helix dipole (below).

*The helix dipole.* All peptide dipoles in an α helix point in the same direction along the axis, so they add up to a macroscopic dipole that grows with helix length: a partial positive charge near the N-terminus (from the uncapped N–H groups) and a partial negative charge near the C-terminus. Negatively charged residues are therefore often found in the first turn of a helix and positively charged residues near its C-terminus; the reverse placements destabilize it. Helix dipoles also help bind anions (for example phosphate) at the N-termini of helices in many enzymes.

*Amphipathic helices and the hydrophobic moment.* Projecting the residues of a helix onto a plane perpendicular to its axis, $100^\circ$ apart, gives a *helical wheel*. Many helices that lie on a protein surface or a membrane are amphipathic: hydrophobic residues on one face, polar and charged residues on the other. A quantitative measure is the *hydrophobic moment* (Eisenberg, 1982): if $H_k$ is the hydrophobicity of residue $k$ on some scale and $\delta$ the angle between successive residues,

$$
\mu_{\mathrm{H}}(\delta) = \frac{1}{N}\left\lvert \sum_{k=1}^{N} H_k\,\mathrm{e}^{\mathrm{i}k\delta} \right\rvert ,
$$
which is the magnitude of the vector sum of the residue hydrophobicities on the wheel. Computed as a function of $\delta$, it is a discrete Fourier transform of the hydrophobicity profile (compare the **discrete Fourier transform** in [4.4.4](/4.4.4)): a peak near $100^\circ$ reveals helical amphipathic periodicity, a peak near $160$–$180^\circ$ an amphipathic β strand with side chains alternating up and down.

![Amphipathic helices. A: helical wheel of residues 1–18 of the antimicrobial peptide magainin 2, viewed from the N-terminus (residue k at angle 100°·k; residues colored by class); the hydrophobic residues (blue) occupy one face, the lysines and the histidine the other, and the arrow is the hydrophobic moment vector (Eisenberg consensus scale), pointing to the hydrophobic face. B: hydrophobic moment per residue of the whole 23-residue peptide as a function of the assumed angle between residues: the maximum lies near 100°, the periodicity of an α helix (magainin is disordered in water and folds into an amphipathic helix on membranes). C: heptad wheel of the GCN4 leucine zipper, two parallel helices related by a twofold axis: the a and d positions (mostly Val and Leu, with one Asn at a) form the hydrophobic interface, the e and g positions flank it and form interhelical ion pairs (g–e′); residues of GCN4-p1 at each position are listed](./plots/helical-wheel.py)

### 5.2.3. The β Conformation and β Sheets

**Definition 5.2.3 (β Sheet)** In the **β conformation** the backbone is extended into a zigzag ($\varphi \approx -120^\circ$ to $-140^\circ$, $\psi \approx +115^\circ$ to $+135^\circ$; about $0.33$–$0.35\ \mathrm{nm}$ per residue). A single segment in this conformation is a **β strand**; several strands side by side, held together by hydrogen bonds between the backbones of adjacent strands, form a **β sheet**.

The planarity of the peptide groups and the tetrahedral $\mathrm{C}_\alpha$ give the sheet a pleated appearance, and the side chains of successive residues point alternately above and below the sheet. Adjacent strands may run in the same direction (parallel sheet) or in opposite directions (antiparallel sheet); the strands can be close together in sequence, far apart, or even in different polypeptides.

| | Antiparallel | Parallel |
|---|---|---|
| Ideal $(\varphi, \psi)$ | $(-139^\circ, +135^\circ)$ | $(-119^\circ, +113^\circ)$ |
| Repeat (two residues) | $0.70\ \mathrm{nm}$ | $0.65\ \mathrm{nm}$ |
| Interstrand hydrogen bonds | nearly linear, alternately narrow and wide pairs | inclined, evenly spaced |
| Typical connection | short hairpin (β turn) | long crossover, usually through an α helix |
| Occurrence | about twice as common | mostly buried, in α/β proteins |

Antiparallel sheets are somewhat more stable, because their hydrogen bonds are nearly in line, and they are easier to form, because neighboring strands can be joined by a two-residue turn; parallel strands must be connected by a crossover of at least $10$–$15$ residues. Real sheets are not flat: viewed along the strands, each strand has a right-handed twist, and the sheet as a whole is twisted.

### 5.2.4. β Turns

**Definition 5.2.4 (β Turn)** A **β turn** is a $180^\circ$ reversal of the chain over four residues $i$ to $i+3$, stabilized by a hydrogen bond from the C=O of residue $i$ to the N–H of residue $i+3$; the peptide groups of the two central residues do not form inter-residue hydrogen bonds.

β turns connect the ends of adjacent antiparallel strands and lie mostly on the protein surface, where the central peptide groups bond to water. They are classified by the $(\varphi, \psi)$ of residues $i+1$ and $i+2$. In the most common type I turn, Pro is frequent at position $i+1$ (the second residue); in type II, Gly is favored at position $i+2$ (the third residue), because that residue must adopt a conformation with positive $\varphi$. Type I turns are more than twice as frequent as type II. A three-residue γ turn, with an $i \to i+2$ hydrogen bond, is much rarer.

### 5.2.5. Dihedral Angles and the Ramachandran Plot

Every regular secondary structure is characterized by its $(\varphi, \psi)$, which makes the $(\varphi, \psi)$ plane a natural map of backbone conformations.

| Structure | $\varphi$ | $\psi$ | Residues per turn $n$ | Rise per residue |
|---|---|---|---|---|
| α helix (right-handed) | $-57^\circ$ | $-47^\circ$ | $3.6$ | $0.15\ \mathrm{nm}$ |
| $3_{10}$ helix | $-49^\circ$ | $-26^\circ$ | $3.0$ | $0.20\ \mathrm{nm}$ |
| Antiparallel β | $-139^\circ$ | $+135^\circ$ | $2.0$ | $0.35\ \mathrm{nm}$ |
| Parallel β | $-119^\circ$ | $+113^\circ$ | $2.0$ | $0.33\ \mathrm{nm}$ |
| Polyproline II (left-handed) | $-75^\circ$ | $+145^\circ$ | $-3.0$ | $0.31\ \mathrm{nm}$ |
| Collagen chain | $-51^\circ$ | $+153^\circ$ | $\approx -3.3$ | $\approx 0.29\ \mathrm{nm}$ |
| Type I β turn, residues $i+1$, $i+2$ | $-60^\circ$, $-90^\circ$ | $-30^\circ$, $0^\circ$ | — | — |
| Type II β turn, residues $i+1$, $i+2$ | $-60^\circ$, $+80^\circ$ | $+120^\circ$, $0^\circ$ | — | — |

(The $n$ and rise columns were computed from the idealized backbone geometry used for the figure below; a negative $n$ means a left-handed helix.)

**Definition 5.2.5 (Ramachandran Plot)** A **Ramachandran plot** is the $(\varphi, \psi)$ plane on which the sterically allowed combinations of backbone dihedral angles are marked, or on which the observed $(\varphi, \psi)$ of the residues of a protein structure are plotted.

G. N. Ramachandran and coworkers (1963) computed which combinations are allowed by treating atoms as hard spheres: a conformation is forbidden if any two atoms not bonded to a common atom come closer than the sum of their contact radii. They used two sets of contact distances, a "normal" limit and a slightly shorter "outer" limit (for example C⋯O $0.28$ and $0.27\ \mathrm{nm}$, O⋯H $0.24$ and $0.22\ \mathrm{nm}$, H⋯H $0.20$ and $0.19\ \mathrm{nm}$). The calculation is simple enough to redo from scratch: build a blocked residue from standard bond lengths and angles, rotate $\varphi$ and $\psi$, and test every pair of atoms whose distance depends on them.

![Hard-sphere Ramachandran maps computed from scratch for a blocked residue (acetyl-X-N-methylamide) with standard geometry (trans peptide bonds, N–Cα–C angle 111°), scanned on a 2° grid. Dark: conformations with no contact closer than the normal limits of Ramachandran and Sasisekharan; light: allowed only at the outer limits. A: L-alanine; the allowed regions are the β region (upper left, containing the antiparallel, parallel and polyproline II conformations), the right-handed α region (lower left; the ideal α helix lies at the outer limit, a few degrees from the fully allowed region) and a small left-handed α region; the map is asymmetric because the Cβ methyl lies on one side of the backbone. B: glycine, whose second Cα hydrogen replaces Cβ; it can adopt about three times as many conformations, including large regions with positive φ, and its map is symmetric under (φ, ψ) → (−φ, −ψ) because glycine is achiral. Points: ideal conformations; thin lines: contours of the number of residues per turn n of the helix generated when every residue has the same (φ, ψ) (positive n right-handed, negative left-handed)](./plots/ramachandran.py)

The computed maps reproduce the main features of real protein structures. Only a small fraction of the plane is available to residues with a $\mathrm{C}_\beta$; the α and β regions are the two large islands, and structures with these conformations are found in proteins precisely because they also satisfy the hydrogen-bonding requirement. Glycine, without a side chain, is the only residue frequently found outside these regions (especially with positive $\varphi$, as in type II turns), while proline is confined near $\varphi \approx -65^\circ$ by its ring. Experimental maps from high-resolution structures are more permissive than the hard-sphere map, because bond angles (especially $\tau$ = N–$\mathrm{C}_\alpha$–C) and $\omega$ flex by a few degrees and atoms are not truly hard; about $98\%$ of non-glycine residues in well-refined structures lie in the empirically "favored" regions. Residues outside the allowed regions are therefore a standard warning sign when a new structure is validated.

### 5.2.6. Secondary Structure Measured by Circular Dichroism

An ordered, chiral structure absorbs left- and right-circularly polarized light differently. In the far ultraviolet ($190$–$250\ \mathrm{nm}$) the chromophore is the peptide bond, and the **circular dichroism** spectrum reflects the backbone conformation (the spectroscopy is described in [6.4.9](/6.4.9)). The α helix has negative bands at $222$ and $208\ \mathrm{nm}$ and a positive band near $192\ \mathrm{nm}$; the β conformation has a weaker negative band near $218\ \mathrm{nm}$ and a positive band near $195\ \mathrm{nm}$; an unfolded chain has a strong negative band near $198\ \mathrm{nm}$. A measured spectrum can be decomposed into these reference spectra to estimate the fractions of helix and sheet, and the ellipticity at $222\ \mathrm{nm}$ is the standard probe for following unfolding ([7.1.6](/7.1.6)).

## 5.3. Fibrous Proteins

### 5.3.1. Tertiary Structure and the Main Classes of Proteins

**Definition 5.3.1 (Tertiary Structure)** The **tertiary structure** of a polypeptide is the overall three-dimensional arrangement of all its atoms, including long-range interactions between residues that are far apart in the sequence and lie in different secondary structures.

Proteins fall into four broad structural groups: fibrous proteins, with chains arranged in long strands or sheets and usually a single type of secondary structure; globular proteins, folded into compact shapes with several types of secondary structure; membrane proteins embedded in lipid bilayers ([7.1.13](/7.1.13)); and intrinsically disordered proteins (§5.4.3). Fibrous proteins provide support, shape and protection; they are insoluble because hydrophobic residues on their surfaces are buried by packing many chains into supramolecular assemblies. Their simplicity makes the relation between structure and mechanical function especially clear.

**Definition 5.3.2 (Fibrous and Globular Proteins)** A **fibrous protein** has polypeptide chains arranged in long strands or sheets, built from one repeating secondary structure; a **globular protein** has its chain folded back on itself into a compact, roughly spherical shape that contains several types of secondary structure.

### 5.3.2. α-Keratin and the Coiled Coil

The α-keratins of hair, wool, nails, claws, horns and the outer layer of skin belong to the intermediate-filament family, which also forms part of the cytoskeleton ([7.3](/7.3)). Each chain is a long right-handed α helix whose central segment has a seven-residue repeat.

**Definition 5.3.3 (Coiled Coil)** A **coiled coil** is a bundle of two or more α helices wound around each other into a supercoil; in the common left-handed coiled coil the sequence has a *heptad repeat* $(abcdefg)_n$ in which positions $a$ and $d$ are hydrophobic and form the interface between the helices.

Because a heptad corresponds to two turns of $3.5$ residues instead of $3.6$, the hydrophobic stripe of $a$ and $d$ residues winds slowly around each helix in a left-handed sense, and two helices pack along these stripes by winding around each other ("knobs into holes", Crick 1953). Positions $e$ and $g$ flank the interface and often carry opposite charges that form interhelical ion pairs (panel C of the helical-wheel figure). The same motif dimerizes the bZIP transcription factors ([7.2.14](/7.2.14)) and forms the tails of myosin (§7.5 of [7.1.7](/7.1.7)). The tilt of the helices in the supercoil also explains a puzzle of early fiber diffraction: hair shows a repeat of $0.515$–$0.52\ \mathrm{nm}$ instead of the $0.54\ \mathrm{nm}$ pitch of a straight α helix, because the pitch is projected onto the fiber axis (Question 3).

In hair, two-chain coiled coils (parallel, N-termini together) assemble into protofilaments, protofibrils and finally intermediate filaments of about $32$ chains. The strength of the assembly is increased by **disulfide bonds** between neighboring chains: up to $18\%$ of the residues of very hard keratins (rhinoceros horn) are cysteines in disulfides. A permanent wave exploits this chemistry: the hair is wrapped around a form, the disulfides are reduced by a thiol reagent, the helices are stretched by moist heat, and the hair is then reoxidized so that new disulfides lock in the new shape.

### 5.3.3. Collagen

**Definition 5.3.4 (Collagen)** **Collagen** is the family of fibrous proteins of connective tissue whose molecules are triple helices: three polypeptide chains ("α chains"), each with the repeating sequence Gly–X–Y and a left-handed polyproline-II-like helical conformation with about three residues per turn, are wound around each other into a right-handed superhelix.

Collagen is the most abundant protein of mammals ($25$–$35\%$ of total protein), in tendons, cartilage, the organic matrix of bone and the cornea; more than $30$ structural variants are known. Its unusual composition (about $35\%$ Gly, $11\%$ Ala and $21\%$ Pro plus 4-hydroxyproline, 4-Hyp) follows from the structure. Every third residue must be Gly, because only a side chain as small as hydrogen fits at the center of the triple helix where the three chains touch; Pro and 4-Hyp, frequent in the X and Y positions, favor the sharply twisted polyproline-II conformation of each chain.

```smiles
OC(=O)[C@@H]1CCCN1 Pro
OC(=O)[C@@H]1C[C@@H](O)CN1 4-Hyp
```

The hydroxyl group of (2*S*,4*R*)-4-hydroxyproline holds the pyrrolidine ring in the $\mathrm{C}_\gamma$-exo pucker required in the Y position, and this stereoelectronic effect, rather than extra hydrogen bonds, is the main reason that hydroxylation stabilizes the triple helix. 4-Hyp is not incorporated during translation: specific Pro residues of procollagen are hydroxylated afterwards by prolyl 4-hydroxylase, an $\mathrm{F\mathrm{e}^{2+}}$ enzyme that uses $\ce{O2}$ and α-ketoglutarate (which is decarboxylated to succinate and $\ce{CO2}$). Ascorbate (vitamin C) is not consumed in the normal reaction; it is needed to reduce the iron back to $\mathrm{F\mathrm{e}^{2+}}$ after occasional uncoupled cycles that oxidize it. Without vitamin C, hydroxylation fails and the resulting collagen is unstable: this is scurvy, with fragile blood vessels, bleeding gums, poor wound healing and the reopening of old wounds. Humans, other primates, guinea pigs and fruit bats lack the last enzyme of ascorbate synthesis and must obtain it in the diet.

The triple helix (molecule about $300\ \mathrm{nm}$ long and $1.5\ \mathrm{nm}$ thick, $M_\mathrm{r} \approx 300\,000$) has greater tensile strength than a steel wire of the same cross-section. Molecules assemble side by side, staggered by about a quarter of their length, into fibrils with the characteristic $64$–$67\ \mathrm{nm}$ banding seen in the electron microscope, and are covalently cross-linked through modified Lys and hydroxylysine side chains (after oxidation by lysyl oxidase). Cross-links accumulate with age, which makes connective tissue stiffer and more brittle.

Because Gly is required at every third position, replacing a single Gly by a bulkier residue (Cys, Ser, Arg and others) disrupts the triple helix around it; since each molecule contains three chains, one mutant allele poisons most of the molecules (a dominant-negative effect). Such substitutions in type I collagen cause the severe forms of *osteogenesis imperfecta* (brittle bones), and related mutations in other collagens cause some forms of *Ehlers–Danlos syndrome* (hypermobile joints, fragile skin). Other forms of both disorders arise from null alleles, from mutations in collagen-processing enzymes (lysyl hydroxylase, procollagen N-proteinase) or from other proteins.

### 5.3.4. Silk Fibroin

Silk fibroin, produced by insects and spiders, consists mainly of antiparallel β sheets. Its sequence is dominated by repeats such as (Gly–Ala–Gly–Ala–Gly–Ser)$_n$: in a β strand the side chains alternate between the two faces, so one face of each sheet carries only Gly (H) and the other mainly Ala ($\ce{CH3}$), and the sheets interdigitate with very close packing. The structure is held together by the hydrogen bonds within each sheet and by van der Waals contacts between sheets. Silk does not stretch, because the β conformation is already nearly fully extended, but it is flexible, because the sheets are joined only by weak interactions.

| Protein | Structure | Chemical basis | Mechanical property |
|---|---|---|---|
| α-Keratin | right-handed α helices in left-handed coiled coils, assembled into filaments | heptad repeat with hydrophobic $a$, $d$; interchain disulfides | strong, stretchable, hardness set by the number of disulfides |
| Collagen | left-handed Gly–X–Y chains in a right-handed triple helix, staggered fibrils | Gly at the center; Pro and 4-Hyp fix the chain conformation; Lys-derived cross-links | very high tensile strength, little stretch |
| Silk fibroin | stacked antiparallel β sheets | small Gly and Ala side chains allow close packing; hydrogen bonds and van der Waals contacts only | does not stretch, but soft and flexible |

## 5.4. Globular Proteins

### 5.4.1. Myoglobin, the First Protein Structure

The first breakthrough in understanding globular proteins came from the X-ray structure of sperm-whale myoglobin by John Kendrew and colleagues (low resolution 1958, atomic detail 1959–1960; the method is described in [7.1.6](/7.1.6#sec-6.6)). Myoglobin ($M_\mathrm{r}$ $16\,700$, $153$ residues) is a single chain carrying one heme; it stores $\ce{O2}$ and facilitates its diffusion in muscle (its function is the subject of [7.1.7](/7.1.7)). The structure revealed what is now known to be typical of globular proteins:

- *Compactness.* About $78\%$ of the residues are in eight right-handed α helices (A to H), the longest with $23$ residues and the shortest with $7$, joined by bends, some of which are β turns. The interior is so tightly packed that it has room for only about four water molecules; the packing density (fraction of space occupied by atoms) is about $0.75$, comparable to that of an organic crystal ($0.70$–$0.78$) and much higher than that of an organic liquid ($0.4$–$0.6$).
- *A nonpolar core and a polar surface.* Almost all hydrophobic side chains are inside; all but two polar side chains are on the surface and hydrated. The two exceptions are His residues that interact with the heme and its bound $\ce{O2}$.
- *Planar trans peptide groups and helices as predicted.* All peptide bonds are trans; three of the four Pro residues are at bends, and the fourth kinks a helix.
- *A pocket for the prosthetic group.* The flat heme sits in a crevice, shielded from the solvent, which prevents oxidation of its $\mathrm{F\mathrm{e}^{2+}}$.

Other small globular proteins have very different proportions of secondary structure (cytochrome c: $39\%$ α, $0\%$ β; lysozyme: $40\%$ α, $12\%$ β; ribonuclease: $26\%$ α, $35\%$ β; chymotrypsin: $14\%$ α, $45\%$ β), but all share these principles. Today the *Protein Data Bank* (PDB, www.rcsb.org), the archive of experimentally determined macromolecular structures, holds more than $200\,000$ entries, each with an identifier (for example 1MBO for oxymyoglobin) and the coordinates of its atoms.

### 5.4.2. Motifs and Domains

Complex structures become understandable when they are decomposed into recurring parts.

**Definition 5.4.1 (Motif)** A **motif**, also called a **fold** or supersecondary structure, is a recognizable folding pattern involving two or more elements of secondary structure and the connections between them.

A motif can be as simple as two elements folded against each other (the β-α-β unit, the β hairpin) or as elaborate as a barrel of many strands, and it may or may not be stable by itself. It is a folding pattern, not a level of the hierarchy between secondary and tertiary structure. The arrangement of the eight helices of myoglobin, conserved in all globins, is the *globin fold*.

**Definition 5.4.2 (Domain)** A **domain** is a part of a polypeptide chain that is independently stable or that can move as a single entity with respect to the rest of the protein (Jane Richardson, 1981).

Chains of more than a few hundred residues usually fold into two or more domains, often with different functions (binding a small molecule, binding another protein, catalysis); a domain cut out of a large protein by proteolysis often keeps its native structure. The calcium-binding muscle protein troponin C, for example, has two separate $\mathrm{Ca^{2+}}$-binding domains. Small proteins consist of a single domain.

The common folds obey a few rules that follow from the chemistry of §5.1:

1. Burying hydrophobic side chains requires at least two layers of secondary structure; the β-α-β unit already provides two.
2. Where α helices and β sheets occur together, they lie in different layers, because the backbone of a β strand cannot hydrogen-bond to an adjacent helix.
3. Segments adjacent in sequence are usually adjacent in the folded structure; long-range connections exist but are not the norm.
4. β strands are most stable with a slight right-handed twist. As a consequence, the crossover connection between two parallel strands is almost always right-handed (it is shorter and bends through smaller angles), and sheets and barrels are twisted.

![Topology diagrams of common motifs, with the sheet seen face-on (strands as arrows from N to C, helices as cylinders). A: β-α-β unit: two parallel strands joined by a crossover helix that packs against one face of the sheet. B: β hairpin: two antiparallel strands joined by a β turn; dotted lines indicate the interstrand hydrogen bonds. C: Greek key: four antiparallel strands in the sheet order 4–1–2–3; strands 1, 2 and 3 are joined by hairpins, and a long connection brings strand 4 back beside strand 1. D: up-and-down four-helix bundle, an all-α motif (ferritin is a bundle of this kind)](./plots/protein-folds.py)

Larger motifs are built from smaller ones. Eight β-α-β units whose parallel strands close into a barrel, each strand followed by a helix on the outside, form the α/β (TIM) barrel, the most common enzyme fold, with the active site at the C-terminal ends of the strands; a domain of pyruvate kinase is an example. The Rossmann fold that binds NAD is built from two β-α-β-α-β units.

### 5.4.3. Intrinsically Disordered Proteins

**Definition 5.4.3 (Intrinsically Disordered Protein)** An **intrinsically disordered protein** (or region) lacks a stable tertiary structure in solution under physiological conditions, yet is functional.

As many as a third of human proteins may be largely disordered or have long disordered segments. Their sequences are distinctive: they lack a hydrophobic core and are rich in charged residues (Lys, Arg, Glu), in small residues (Gly, Ala, Ser) and in Pro, which disrupts ordered structure. Predictors such as PONDR use these compositional signals to estimate, residue by residue, the probability of disorder. Disorder serves several functions:

- linkers and spacers between domains, and entropic "bristles";
- promiscuous binding: the cell-cycle inhibitor p27 is unstructured in solution but wraps around several different cyclin–kinase complexes and inhibits them; the C-terminal segment of p53 binds at least four partners and adopts a different structure in each complex (coupled folding and binding);
- hubs and scaffolds of signaling networks ([7.1.15](/7.1.15)), where a disordered region can carry many short binding motifs and phosphorylation sites;
- biomolecular condensates, in which multivalent disordered regions drive liquid–liquid phase separation ([7.2.21](/7.2.21)).

### 5.4.4. Structural Classification and Protein Families

The number of distinct folds is limited: the SCOP2 database (Structural Classification of Proteins) classifies the structures of the PDB into only about $1\,400$ folds, and new folds are now found only rarely. SCOP groups domains into four main classes: all α, all β, α/β (helices and strands interspersed or alternating, typically parallel β-α-β units) and α + β (helices and strands in separate parts of the chain, typically antiparallel sheets). CATH uses a parallel hierarchy of Class, Architecture, Topology (fold) and Homologous superfamily.

Tertiary structure is conserved much longer in evolution than amino acid sequence. Proteins with significant sequence similarity and/or similar structure and function form a *protein family* (the PDB contains roughly $4\,000$ families), and families with little sequence similarity but the same fold and related functions form a *superfamily*, whose members are probably related by descent. Families present in Bacteria, Archaea and Eukarya, such as many enzymes of intermediary metabolism, are ancient; others occur only in a narrow group of organisms and arose more recently. Structural comparison thus complements sequence comparison in tracing evolution ([7.1.4](/7.1.4), [7.8](/7.8)).

## 5.5. Quaternary Structure

### 5.5.1. Subunits and Protomers

**Definition 5.5.1 (Quaternary Structure)** In a protein made of two or more polypeptide chains, each chain is a **subunit**, and the spatial arrangement of the subunits and the nature of their interactions constitute the **quaternary structure**. A protein with several subunits is an **oligomer** (multimer); the repeating structural unit of an oligomer, whether one subunit or a group of different subunits, is its **protomer**.

Subunits assemble spontaneously through the same weak interactions that stabilize tertiary structure, with large buried interfaces. Oligomerization serves several purposes:

- regulation: the binding of a small molecule to one subunit changes the interactions between subunits and thereby the activity of the others, as in cooperative $\ce{O2}$ binding by hemoglobin ([7.1.7](/7.1.7)) and in allosteric enzymes ([7.1.9](/7.1.9));
- division of labor: separate catalytic and regulatory subunits (aspartate transcarbamoylase, protein kinase A);
- structure: fibers ([§5.3](#sec-5.3)) and virus coats;
- multistep machines: the ribosome contains dozens of proteins and several RNAs.

Hemoglobin was the first oligomeric protein whose structure was solved (Max Perutz and colleagues, 1959–1968). It has two α chains ($141$ residues) and two β chains ($146$ residues), each with a heme; the Greek letters name the types of subunit, not their secondary structure (both are all-α globin folds). Because the subunits are arranged as two symmetric αβ pairs, hemoglobin can be described as a tetramer or as a dimer of αβ protomers.

### 5.5.2. Symmetry

Oligomers of identical subunits are almost always symmetric, because a symmetric arrangement uses the same interface repeatedly and lets a few genetic instructions build a large structure.

| Symmetry | Arrangement | Examples |
|---|---|---|
| Cyclic $C_n$ | $n$ subunits around one $n$-fold axis | Cro repressor dimer ($C_2$), GroES ring ($C_7$) |
| Dihedral $D_n$ | two $C_n$ rings face to face, with twofold axes perpendicular to the main axis | tetramers with three perpendicular twofold axes ($D_2$), GroEL ($D_7$) |
| Helical | subunits along a helical path; open-ended | actin filaments, microtubules, tobacco mosaic virus |
| Icosahedral | $60$ equivalent positions (or a multiple) on a closed shell | many spherical virus capsids |

Hemoglobin has an exact twofold axis relating the two αβ protomers, and, since α and β are similar, an approximate $D_2$ symmetry. Note that because protein subunits are chiral, only rotational symmetries are possible; mirror planes and inversion centers do not occur.

## Summary

The levels of protein structure:

| Level | Definition | Stabilized by |
|---|---|---|
| Primary | amino acid sequence ([7.1.3](/7.1.3)) | covalent peptide and disulfide bonds |
| Secondary | local backbone conformation: α helix, β sheet, β turn (Definition 5.2.1) | backbone hydrogen bonds within allowed $(\varphi, \psi)$ |
| Tertiary | complete 3D structure of one chain (Definition 5.3.1); built from motifs and domains | hydrophobic effect, packing, hydrogen bonds, ion pairs, occasional disulfides |
| Quaternary | arrangement of subunits (Definition 5.5.1) | the same weak interactions at subunit interfaces |

Structure, chemical basis and function:

| Structural feature | Chemical property behind it | Biological consequence |
|---|---|---|
| Rigid planar peptide group (§5.1.3) | amide resonance; trans geometry | only $\varphi$, $\psi$ free per residue; Ramachandran map (Definition 5.2.5) |
| α helix (Definition 5.2.2) | $i \to i+4$ backbone hydrogen bonds; helix dipole | compact, stiff rods; amphipathic helices bind membranes or partners |
| β sheet (Definition 5.2.3) | interstrand hydrogen bonds; alternating side chains | flat or twisted sheets, barrels; amyloid when misassembled ([7.1.6](/7.1.6)) |
| Coiled coil (Definition 5.3.3) | heptad repeat, hydrophobic $a$ and $d$ | keratin, myosin tails, leucine-zipper dimers |
| Collagen triple helix (Definition 5.3.4) | Gly at every third residue, Pro and 4-Hyp | tensile strength; scurvy and osteogenesis imperfecta when chemistry fails |
| Hydrophobic core | hydrophobic effect | marginal stability of the native state (Definition 5.1.1) |
| Motifs and domains (Definitions 5.4.1, 5.4.2) | layering of helices and sheets, right-handed crossovers | modular evolution; about $1\,400$ folds |
| Intrinsic disorder (Definition 5.4.3) | charged, Pro-rich, no hydrophobic core | promiscuous binding, signaling hubs, condensates |
| Quaternary structure (Definition 5.5.1) | weak interactions at symmetric interfaces | allostery and cooperativity |

Key numbers: peptide C–N $0.132\ \mathrm{nm}$; α helix $3.6$ residues per turn, pitch $0.54\ \mathrm{nm}$, rise $0.15\ \mathrm{nm}$, $(\varphi, \psi) \approx (-57^\circ, -47^\circ)$; β strand $0.33$–$0.35\ \mathrm{nm}$ per residue; trans peptide bonds $>99.95\%$ (X–Pro: about $6\%$ cis); native stability $5$–$65\ \mathrm{kJ\,mol^{-1}}$; protein packing density $0.75$.

## Questions

1. Why is the α helix the predominant conformation of a long stretch of poly-L-glutamate at pH 3 but not at pH 7, and what happens to poly-L-lysine at pH 7 and pH 12?

   **Answer** At pH 7 the side-chain carboxyl groups of Glu (p$K_\mathrm{a}$ about 4.1) are deprotonated, and the negative charges at $i$, $i+3$ and $i+4$, which are neighbors on the helix surface, repel each other strongly enough to prevent the helix. At pH 3 most carboxyl groups are protonated and neutral, and the helix forms. Likewise poly-Lys (side-chain p$K_\mathrm{a}$ about 10.5) is positively charged and disordered at pH 7 but forms an α helix at pH 12, where the amino groups are neutral. Both transitions can be followed by circular dichroism at $222\ \mathrm{nm}$.
2. An X-ray fiber pattern of hair shows a strong repeat of $0.515\ \mathrm{nm}$ along the fiber axis, whereas the pitch of an α helix is $0.54\ \mathrm{nm}$. Estimate the angle between the helix axes and the axis of the coiled coil.

   **Answer** In a coiled coil each helix is tilted by an angle $\alpha$ relative to the supercoil axis, so the helical repeat projected onto the fiber axis is $0.54\ \mathrm{nm} \times \cos\alpha$. From $\cos\alpha = 0.515/0.54 = 0.954$ we get $\alpha \approx 17^\circ$, close to the tilt found in crystal structures of two-stranded coiled coils.
3. What would the Ramachandran plot of a protein made entirely of D-amino acids look like, and what handedness would its α helices have? Would such a mirror-image enzyme act on the natural substrate?

   **Answer** Mirror reflection changes the sign of every dihedral angle, so the allowed regions are inverted through the origin, $(\varphi, \psi) \to (-\varphi, -\psi)$: the β region moves to the lower right and the favored helix becomes the left-handed one at about $(+57^\circ, +47^\circ)$. The whole protein is the mirror image of the natural one (this was demonstrated with chemically synthesized D-HIV protease, 1992). It is fully active, but only toward the mirror image of the natural substrate when the substrate is chiral, and it is resistant to natural proteases, which is why mirror-image peptides are studied as drugs.
4. Glycine and proline are both "helix breakers". Explain why they act for different reasons, and why both are common in β turns.

   **Answer** Proline has its side chain bonded back to the backbone nitrogen, which fixes $\varphi$ near $-65^\circ$ (incompatible with the regular helix only in that it lacks an N–H for the $i \to i+4$ hydrogen bond and its ring clashes with the preceding turn); it therefore breaks or kinks helices except in the first turn. Glycine has no side chain; its map (panel B of the Ramachandran figure) allows many more conformations, so the entropy cost of fixing it in a helix is larger. In turns these properties are assets: Pro fits the $\varphi \approx -60^\circ$ of position $i+1$ of a type I turn and its X–Pro bond can be cis, and Gly can adopt the positive $\varphi$ required at position $i+2$ of a type II turn.
5. A missense mutation replaces one Gly of the Gly–X–Y repeat of the type I collagen α1 chain by Ser. Why is the disease dominant, and why is it usually more severe when the substitution lies near the C-terminal end of the triple helix?

   **Answer** Each collagen molecule contains three chains (two α1 and one α2 in type I collagen), so with one mutant allele most molecules contain at least one mutant α1 chain ($1 - (1/2)^2 = 3/4$ of them if both alleles are expressed equally). The bulky Ser cannot fit at the center of the triple helix and disrupts it locally; the mutant chain therefore poisons the normal ones (dominant negative). The triple helix folds from its C-terminal end toward the N-terminus like a zipper, so a defect near the C-terminus delays folding of most of the molecule, which is then overmodified and degraded; defects near the N-terminus affect only a short segment.
6. Using the helical wheel, explain why a peptide such as magainin 2 can kill bacteria at concentrations that do not damage human cells.

   **Answer** Magainin is unstructured in water but folds into an amphipathic α helix on membranes, with a hydrophobic face that inserts into the lipid core and a face carrying several Lys residues (a net positive charge). The positive face is attracted to the negatively charged outer surface of bacterial membranes (phosphatidylglycerol, lipopolysaccharide), whereas the outer leaflet of animal cell membranes is mainly zwitterionic and contains cholesterol. Accumulated peptides then disrupt the bacterial bilayer. The large hydrophobic moment at $\delta \approx 100^\circ$ is the quantitative signature of this amphipathic design.
