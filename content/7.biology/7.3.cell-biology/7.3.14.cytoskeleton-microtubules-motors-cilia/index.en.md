---
title: "The Cytoskeleton II: Microtubules, Motors and Cilia"
description: "Tubulin and the microtubule lattice; dynamic instability, catastrophe and rescue, the GTP cap and the Dogterom–Leibler model; nucleation by the γ-tubulin ring complex, centrosomes, centrioles and other microtubule-organizing centers; microtubule-associated proteins, plus-end tracking proteins, depolymerases and severing enzymes; drugs; kinesins and dyneins, hand-over-hand stepping, force–velocity relation and processivity, axonal transport and teams of motors; cilia and flagella: the axoneme, sliding and bending, intraflagellar transport, primary cilia and ciliopathies, and the contrast with the bacterial flagellum."
---

Actin builds the cell's surface; microtubules build its interior. They are stiff hollow tubes that reach from the center of the cell to its edge, and they do three things that actin cannot: they define the long axes of the cell and the positions of its organelles, they serve as tracks for long-distance transport by kinesins and dyneins, and at mitosis they form the spindle that separates the chromosomes. The previous chapter developed the kinetics of polar polymers for actin ([7.3.13](/7.3.13)); microtubules follow the same rules with a twist, dynamic instability, which lets each microtubule search the cytoplasm by growing and shrinking at random. This chapter treats the microtubule, its nucleation at centrosomes and other organizing centers, the proteins that regulate its dynamics, the two families of microtubule motors and the most elaborate microtubule machines, cilia and flagella. Microtubules in the spindle are taken up in [7.3.21](/7.3.21), and intermediate filaments, cell polarity and migration in [7.3.15](/7.3.15).

## 14.1. The Structure of Microtubules

**Definition 14.1.1 (Tubulin and Microtubule)** **Tubulin** is a heterodimer of two related globular proteins, α-tubulin and β-tubulin (about $50\,\mathrm{kDa}$ each), each binding one GTP: the GTP on α-tubulin is buried in the dimer interface and never hydrolyzed, that on β-tubulin is exchangeable and hydrolyzed after assembly. A **microtubule** is a hollow cylinder, $25\,\mathrm{nm}$ in outer and about $15\,\mathrm{nm}$ in inner diameter, formed by usually 13 **protofilaments**: linear chains of αβ-dimers joined head to tail ($8\,\mathrm{nm}$ per dimer), with β-tubulin pointing towards the plus end and α-tubulin exposed at the minus end.

Lateral contacts between protofilaments, mainly α–α and β–β, make a helical B lattice in which neighboring protofilaments are offset by $0.9\,\mathrm{nm}$; going once around the tube this offset adds up to $1.5$ monomers, so that the lattice has one seam where α meets β. A micrometer of microtubule contains about $13 \times 125 = 1625$ dimers. The tubular structure explains the mechanical difference from actin: the flexural rigidity of a tube grows with the fourth power of its radius, and a microtubule is about 300 times stiffer than an actin filament (persistence length several millimeters; [7.3.15](/7.3.15#sec-15.3)).

Tubulin is as conserved as actin (human and yeast tubulins are about $75\,\%$ identical), and mammals have several genes for each subunit. Its fold is related to that of the bacterial cell-division protein FtsZ ([7.3.15](/7.3.15#sec-15.2)). A third member of the family, γ-tubulin, does not polymerize into microtubules but nucleates them (14.3). Microtubules are also marked by post-translational modifications that motors and MAPs read: removal of the C-terminal tyrosine of α-tubulin (detyrosination), acetylation of Lys40 inside the lumen in long-lived microtubules, and polyglutamylation and polyglycylation of the C-terminal tails, especially in axonemes, collectively called the tubulin code.

Microtubules were recognized only in 1963, when fixation with glutaraldehyde preserved them for electron microscopy, in the cnidarian *Hydra* (Slautterback) and in plant cells (Ledbetter and Porter); in earlier preparations with osmium tetroxide or at low temperature they had depolymerized. Their lability is itself a defining property. Purified tubulin assembles spontaneously above a critical concentration of about $1\,\mathrm{mg\,mL^{-1}}$ (some $10\,\mu\mathrm{M}$; much lower with MAPs) at $37\,^\circ\mathrm{C}$, in a slightly acidic buffer (about pH 6.8) with GTP and $\ce{Mg^2+}$ and with $\ce{Ca^2+}$ chelated; it depolymerizes in the cold, under high hydrostatic pressure and at micromolar $\ce{Ca^2+}$, and repeated cycles of warm assembly and cold disassembly are the classical method of purifying tubulin from brain. Microtubules assembled in vitro have between 10 and 16 protofilaments (most often 14), whereas the γ-tubulin template of cells sets the number at 13 (14.3.1). In the cell, tubulin builds three kinds of walls:

| Form | Structure | Where |
|---|---|---|
| Singlet | a complete tube of 13 protofilaments | cytoplasmic microtubules, spindle, central pair of the axoneme |
| Doublet | complete A tubule (13) and incomplete B tubule (10 protofilaments, sharing the wall of A) | outer microtubules of the axoneme of cilia and flagella (14.6) |
| Triplet | A tubule with incomplete B and C tubules | centrioles and basal bodies (14.3.2) |

![Microtubule structure (schematic). A: the αβ-tubulin heterodimer (β-tubulin towards the plus end) and a protofilament of dimers stacked head to tail. B: a cross-section with 13 protofilaments, 25 nm across; the seam of the B lattice is dashed. C: a growing microtubule with a cap of GTP-tubulin (gold) at its plus end and a slightly flared sheet; behind the cap β-tubulin carries GDP·Pi (pale gold) and GDP (blue). D: after a catastrophe the cap is lost and GDP protofilaments peel back in curls. E: a γ-tubulin ring complex templates the minus end of a new microtubule](./plots/microtubule-structure.py)

## 14.2. Dynamic Instability

### 14.2.1. Growth, Catastrophe and Rescue

Microtubules polymerize from GTP-tubulin, and GTP is hydrolyzed shortly after a dimer is incorporated. As for actin, two kinds of end can exist: one capped with GTP-tubulin and one exposing GDP-tubulin, which dissociates very fast. The difference between them is far larger than for actin. A GDP-tubulin end shrinks about a hundred times faster than a GTP end, and in vivo the two ends of a microtubule have similar critical concentrations, so that microtubules do not treadmill much; instead each end switches between two states.

**Definition 14.2.1 (Dynamic Instability)** **Dynamic instability** is the behavior of a microtubule end that, at constant free tubulin concentration, switches stochastically between prolonged phases of slow growth and rapid shrinkage. The switch from growth to shrinkage is a **catastrophe**; the switch from shrinkage to growth is a **rescue**.

Dynamic instability was discovered by Mitchison and Kirschner (1984), who noticed that, when microtubules nucleated from centrosomes were left in tubulin near steady state, their number fell while their mean length rose: some microtubules grew while others vanished. Video microscopy of single microtubules then showed the alternation directly (Walker and colleagues, 1988). In interphase cells, plus ends grow at $5$–$20\,\mu\mathrm{m\,min^{-1}}$ and shrink at $15$–$30\,\mu\mathrm{m\,min^{-1}}$; a microtubule lives for minutes, while its minus end is usually anchored and stable.

**Definition 14.2.2 (GTP Cap)** The **GTP cap** is the region of GTP-tubulin (and GDP·Pi-tubulin) at the growing end of a microtubule, formed because subunits are added faster than their GTP is hydrolyzed. The cap holds the end in the growing state; when it is lost by a stochastic fluctuation, the strained GDP lattice is exposed and the microtubule undergoes a catastrophe.

Several observations support the cap model. Microtubules grown from the slowly hydrolyzed analog GMPCPP are stable; cutting a growing microtubule with a laser or a microneedle makes the new plus end shrink at once, while the minus end usually survives (Walker, Inoué and Salmon, 1989). The size of the cap is small, tens to a few hundred dimers, and it is visualized in cells by EB proteins (14.4.2), which bind the lattice in its GTP and GDP·Pi states. Structurally, GTP-tubulin dimers assemble into protofilaments that are straight in the lattice; GTP hydrolysis compacts the lattice and stores strain, because GDP-tubulin prefers a curved conformation. Lateral bonds hold the GDP protofilaments straight; once the cap is lost they relax and peel outward, which is why shrinking ends show curled "ram's horns" in cryo-electron microscopy, and why a depolymerizing end can pull on an attached load, as at kinetochores ([7.3.21](/7.3.21)). Catastrophes in vitro become more likely as a microtubule ages, an effect attributed to the accumulation of defects at the tip, which shows that the cap is not a single all-or-none event.

### 14.2.2. A Two-State Model

The simplest quantitative description treats each plus end as a two-state Markov process.

**Formula 14.2.1 (Dogterom–Leibler Model)** Let a microtubule end grow at speed $v_{\mathrm{g}}$, shrink at speed $v_{\mathrm{s}}$, undergo catastrophes at rate $f_{\mathrm{cat}}$ and rescues at rate $f_{\mathrm{res}}$, and let microtubules that shrink to zero be renucleated. The densities $p_{\mathrm{g}}(L,t)$ and $p_{\mathrm{s}}(L,t)$ of growing and shrinking microtubules of length $L$ satisfy

$$
\frac{\partial p_{\mathrm{g}}}{\partial t} = -v_{\mathrm{g}}\frac{\partial p_{\mathrm{g}}}{\partial L} - f_{\mathrm{cat}}p_{\mathrm{g}} + f_{\mathrm{res}}p_{\mathrm{s}}, \qquad
\frac{\partial p_{\mathrm{s}}}{\partial t} = v_{\mathrm{s}}\frac{\partial p_{\mathrm{s}}}{\partial L} + f_{\mathrm{cat}}p_{\mathrm{g}} - f_{\mathrm{res}}p_{\mathrm{s}} .
\tag{14.1}
$$
If $v_{\mathrm{s}}f_{\mathrm{cat}} > v_{\mathrm{g}}f_{\mathrm{res}}$ (bounded growth), the steady-state length distribution is exponential with mean

$$
\langle L\rangle = \frac{v_{\mathrm{g}}v_{\mathrm{s}}}{v_{\mathrm{s}}f_{\mathrm{cat}} - v_{\mathrm{g}}f_{\mathrm{res}}} ;
\tag{14.2}
$$
otherwise (unbounded growth) the mean length increases without limit at the drift velocity $J = (v_{\mathrm{g}}f_{\mathrm{res}} - v_{\mathrm{s}}f_{\mathrm{cat}})/(f_{\mathrm{cat}} + f_{\mathrm{res}})$ (Dogterom and Leibler, 1993).

The drift follows from time averages: an end spends a fraction $f_{\mathrm{res}}/(f_{\mathrm{cat}} + f_{\mathrm{res}})$ of its time growing and the rest shrinking. Equation (14.2) shows how a cell can switch its microtubule array between two regimes by small changes of the parameters. In interphase, catastrophes are rare enough that microtubules reach the cell edge; at the entry into mitosis, Cdk1 activity raises the catastrophe frequency about tenfold, and the long interphase microtubules are replaced by a dense array of short, highly dynamic ones from which the spindle is built ([7.3.21](/7.3.21)). Locally, a stabilizing signal that lowers $f_{\mathrm{cat}}$ or raises $f_{\mathrm{res}}$ near a target selects microtubules that grow towards it: this "search and capture" mechanism lets microtubules find chromosomes, the cell cortex or a leading edge without any prior information about where they are.

![Dynamic instability in the two-state model (Formula 14.2.1; $v_{\mathrm{g}} = 10\,\mu\mathrm{m\,min^{-1}}$, $v_{\mathrm{s}} = 20\,\mu\mathrm{m\,min^{-1}}$, $f_{\mathrm{cat}} = 0.06\,\mathrm{s^{-1}}$, $f_{\mathrm{res}} = 0.05\,\mathrm{s^{-1}}$). A: Monte Carlo traces of three microtubules: phases of slow growth interrupted by catastrophes and rapid shrinkage, sometimes rescued, sometimes back to zero and renucleated. B: the steady-state length distribution of 4000 simulated microtubules (bars) is exponential with the mean of Eq. (14.2) (line). C: the mean length diverges as the rescue frequency approaches $v_{\mathrm{s}}f_{\mathrm{cat}}/v_{\mathrm{g}}$ (dashed), the transition to unbounded growth; the point marks the parameters of A and B](./plots/dynamic-instability.py)

### 14.2.3. Dynamic Instability and Treadmilling Compared

| | Actin filament | Microtubule |
|---|---|---|
| Nucleotide | ATP on each subunit | GTP on β-tubulin |
| Plus- and minus-end critical concentrations | very different in the ADP state | similar |
| Stability of the NDP lattice | ADP-actin depolymerizes slowly | GDP-tubulin depolymerizes very fast |
| Typical behavior | treadmilling; turnover by cofilin severing | dynamic instability of plus ends; minus ends anchored |
| Purpose | steady flux of subunits through a network | exploration of space by individual polymers |

Both behaviors use the same thermodynamic trick, a polymer built in a high-energy state that becomes unstable after hydrolysis, and both cost energy at steady state; the quantitative difference in the instability of the hydrolyzed polymer decides which one is seen. Plant cortical microtubules and some microtubules in cells also treadmill, with growing plus ends and slowly shrinking minus ends.

## 14.3. Microtubule-Organizing Centers

### 14.3.1. Nucleation by the γ-Tubulin Ring Complex

Spontaneous nucleation of microtubules is even slower than that of actin, and in cells microtubules almost never start without a template.

**Definition 14.3.1 (γ-Tubulin Ring Complex)** The **γ-tubulin ring complex** (γ-TuRC), about $2\,\mathrm{MDa}$, is a lock-washer-shaped ring of 14 γ-tubulin molecules on accessory proteins (GCPs) that presents 13 γ-tubulins in the geometry of a microtubule end; αβ-tubulin dimers bind it with α-tubulin down, so that a microtubule grows from it with its minus end capped by the complex.

**Definition 14.3.2 (Microtubule-Organizing Center)** A **microtubule-organizing center** (MTOC) is a cellular structure that nucleates microtubules and anchors their minus ends, typically by concentrating γ-TuRCs: the centrosome of animal cells, the basal bodies of cilia, the spindle pole body of fungi, and noncentrosomal sites such as the Golgi apparatus, the nuclear envelope and the walls of existing microtubules.

Microtubules can also branch from the sides of existing microtubules: the augmin complex recruits γ-TuRC to a mother microtubule, and the daughter grows at a shallow angle with the same polarity, which amplifies microtubule number in spindles and in plant cortical arrays.

### 14.3.2. The Centrosome and Centrioles

**Definition 14.3.3 (Centrosome and Centriole)** A **centriole** is a cylinder about $250\,\mathrm{nm}$ in diameter and $500\,\mathrm{nm}$ long, made of nine triplet microtubules (a complete A tubule and incomplete B and C tubules) arranged with ninefold symmetry around a cartwheel. The **centrosome**, the main MTOC of animal cells, consists of a pair of centrioles, mother and daughter, at right angles, surrounded by the **pericentriolar material**, a protein matrix that contains the γ-TuRCs and nucleates microtubules.

The ninefold symmetry comes from SAS-6, whose coiled-coil dimers assemble into a ring of nine at the cartwheel hub; a new centriole is built once per cell cycle next to each existing one, under the control of the kinase Plk4, beginning at the G1–S transition, so that a cell entering mitosis has two centrosomes that become the spindle poles ([7.3.21](/7.3.21)). The pericentriolar material expands several-fold before mitosis (maturation), and it may form partly by condensation of scaffold proteins such as pericentrin and CDK5RAP2 (compare **biomolecular condensates**, [7.2.21](/7.2.21)). The mother centriole carries distal and subdistal appendages; when a cell leaves the cycle, it docks at the plasma membrane and becomes the basal body of a primary cilium (14.6).

The centrosome is less indispensable than its central position suggests. Its function in nucleation is redundant with other MTOCs: cells whose centrioles are removed by laser ablation or by inhibiting Plk4 still build spindles, slowly and with more errors. Higher plants and many fungi have no centrioles, mouse oocytes build their meiotic spindles without them, and flies without centrioles develop almost normally but lack cilia and die because their sensory neurons fail. What centrioles are indispensable for is templating cilia.

### 14.3.3. Arrays in Different Cells

The arrangement of microtubules reflects what a cell needs from them:

- in a fibroblast or a leukocyte, a radial aster from the centrosome, with plus ends at the periphery, which positions the Golgi apparatus near the center and the nucleus, and which turns with the centrosome to face the leading edge in migration;
- in columnar epithelial cells, noncentrosomal bundles running from the apical cortex, where their minus ends are anchored by CAMSAP proteins, to the basal side, so that transport by minus-end and plus-end motors distinguishes apical and basolateral destinations;
- in neurons, uniformly plus-end-out microtubules in the axon and mixed orientations in mammalian dendrites, which lets motors sort cargoes into one compartment or the other; neuronal microtubules are released from the centrosome by severing (14.4.3) and stabilized by tau and MAP2;
- in plant cells, which have no centrosome, cortical arrays nucleated on existing microtubules and on the cortex, oriented by microtubule–microtubule interactions and katanin severing; they guide the cellulose synthase complexes in the membrane and thereby set the direction of cell expansion ([7.12](/7.12)).

![Microtubule-organizing centers and microtubule arrays (schematic). A: the centrosome: a mother and a daughter centriole at right angles in pericentriolar material with γ-tubulin ring complexes (gold dots); microtubules grow with their minus ends in the matrix and their plus ends (dots) outward. B: a centriole in cross-section: nine triplets (A, B, C tubules) around a cartwheel with its SAS-6 hub. C: arrays in a fibroblast (radial, from the centrosome), a columnar epithelial cell (minus ends apical), a neuron (axon uniformly plus-end out; mammalian dendrites mixed) and a plant cell (cortical, parallel)](./plots/centrosome-mt-arrays.py)

## 14.4. Proteins That Regulate Microtubules

### 14.4.1. Stabilizing MAPs

**Definition 14.4.1 (Microtubule-Associated Protein)** A **microtubule-associated protein** (MAP) is a protein that binds the lattice of microtubules and changes their stability, their spacing or their interactions with other structures; in the narrow sense, the term refers to the structural MAPs of neurons, which stabilize microtubules and space them in bundles.

Tau in axons and MAP2 in dendrites bind along protofilaments through repeated microtubule-binding motifs, suppress catastrophes and, through projection domains of different lengths, set the spacing between neighboring microtubules (tighter in axons). Hyperphosphorylated tau detaches from microtubules and aggregates into the paired helical filaments of the neurofibrillary tangles in Alzheimer disease and other tauopathies, which are **amyloid fibrils**. The polymerase XMAP215 (chTOG in humans) binds the plus end and adds tubulin dimers, accelerating growth up to tenfold; doublecortin and MAP7 have more specialized roles in neurons.

### 14.4.2. Plus-End Tracking Proteins

**Definition 14.4.2 (Plus-End Tracking Protein)** A **plus-end tracking protein** (+TIP) is a protein that accumulates specifically at the growing plus ends of microtubules. The core +TIPs, the EB proteins (EB1–EB3), recognize the GTP and GDP·Pi lattice near the tip and recruit other +TIPs (CLIP-170, CLASPs, APC, the dynein activator dynactin, and some kinesins and GEFs) through binding motifs.

Because EB proteins bind only the newly assembled lattice and leave it as hydrolysis proceeds, fluorescent EB1 appears as a comet at each growing plus end and disappears at catastrophe; EB comets are the standard readout of microtubule growth in cells. +TIPs let growing ends find targets: CLASPs promote rescue near the cell cortex and at focal adhesions, APC links plus ends to actin and adhesions in migrating cells, and plus-end-bound dynein, delivered by +TIPs to the cortex, pulls on astral microtubules to position the spindle ([7.3.21](/7.3.21)).

### 14.4.3. Destabilizers, Severing Enzymes and Drugs

Two kinds of proteins promote disassembly at ends. Kinesin-13 (MCAK) does not walk but diffuses along the lattice to the ends and uses ATP to bend terminal dimers into the curved conformation, removing them; it promotes catastrophes in mitosis and corrects attachments at kinetochores. Stathmin (Op18) binds two tubulin dimers in a curved complex, sequestering subunits and promoting catastrophes; phosphorylation turns it off.

**Definition 14.4.3 (Microtubule Severing)** **Microtubule severing** is the cutting of a microtubule within its lattice by an AAA ATPase of the katanin, spastin or fidgetin family: the hexameric enzyme pulls the C-terminal tail of a tubulin subunit through its central pore and extracts the dimer, creating a gap and two new ends.

Severing seems destructive but often multiplies microtubules, because the new ends can grow if they are rescued; katanin releases microtubules from the centrosome in neurons and amplifies the cortical arrays of plants, where severing at branch points reorients the array towards light. Mutations in spastin are the most common cause of hereditary spastic paraplegia, a degeneration of the longest axons of the corticospinal tract. Tubulin damaged in the lattice can also be repaired by incorporation of new GTP-tubulin, which leaves rescue sites behind.

The drugs listed in [7.3.13](/7.3.13#sec-13.1.3) act on tubulin at defined sites. Colchicine and nocodazole bind the curved dimer at the α–β interface; the drug–tubulin complex adds to ends and poisons further growth, so microtubules depolymerize. Vinblastine and vincristine bind between dimers and, at low concentration, suppress dynamics without depolymerization. Taxol (paclitaxel) binds a pocket in β-tubulin inside the lattice, stabilizing the straight conformation: microtubules no longer depolymerize. At the low concentrations used in therapy all these drugs mainly suppress dynamic instability, and since the spindle depends on it more than any other structure, they arrest dividing cells in mitosis (via the spindle assembly checkpoint, [7.3.21](/7.3.21)). Taxanes and vinca alkaloids are used against breast, ovarian, lung and blood cancers; their toxicity to the long axons of peripheral nerves, which depend on microtubule transport, is the main side effect. Colchicine treats gout by impairing the migration of neutrophils.

## 14.5. Microtubule Motors

### 14.5.1. The Discovery of Kinesin

Fast axonal transport, the movement of membrane organelles along axons at a few micrometers per second, was known since the 1960s, but the motor was elusive. Allen and colleagues watched organelles moving in extruded axoplasm of the squid giant axon by video-enhanced DIC microscopy (**differential interference contrast microscopy**, [7.3.2](/7.3.2)), and Vale, Reese and Sheetz (1985) used that system to purify the responsible protein: a soluble factor that moved beads and organelles along microtubules, and microtubules over glass, in the presence of ATP, and bound microtubules tightly in the presence of the nonhydrolyzable analog AMP-PNP. They named it kinesin. Retrograde transport was soon traced to cytoplasmic dynein, an enzyme related to the dyneins of cilia that Gibbons had discovered in 1963.

**Definition 14.5.1 (Kinesin)** A **kinesin** is a member of a superfamily of microtubule motor proteins that share a motor domain of about 350 residues with an ATP site and a microtubule-binding site; the rest of the molecule varies. Conventional kinesin, **kinesin-1**, is a tetramer of two heavy chains, whose N-terminal motor domains are joined by neck linkers and a coiled-coil stalk, and two light chains that bind cargo with the tail; it moves processively towards the plus end.

**Definition 14.5.2 (Dynein)** A **dynein** is a microtubule motor of the AAA+ family whose heavy chain (about $500\,\mathrm{kDa}$) folds into a ring of six AAA+ domains, with a long coiled-coil stalk that ends in the microtubule-binding domain and a linker that lies across the ring and swings during the cycle; dyneins move towards the minus end. Cytoplasmic dynein-1 carries cargoes in the cytoplasm, dynein-2 drives retrograde intraflagellar transport, and axonemal dyneins power ciliary beating.

**Definition 14.5.3 (Dynactin)** **Dynactin** is a $1\,\mathrm{MDa}$ complex built around a short filament of the actin-related protein Arp1 that binds cytoplasmic dynein and microtubules; together with an activating adaptor that also binds cargo (such as BICD2, HOOK3 or Spindly), it switches dynein from an autoinhibited, weakly processive state into a highly processive motor.

The requirement for an adaptor (McKenney and colleagues; Schlager and colleagues, 2014) explains how a single dynein gene serves dozens of cargoes: each adaptor links dynein–dynactin to a particular cargo (Rab6 vesicles, nuclear pores, kinetochores) and activates it only when the cargo is attached. Dynein is also unusual in its mechanics: its step size varies (8–32 nm), it takes side and backward steps, and a single mammalian dynein stalls at about $1\,\mathrm{pN}$ alone but at $3$–$4\,\mathrm{pN}$ with dynactin and an adaptor.

The kinesin superfamily has 45 genes in humans, grouped into 14 families. The position of the motor domain correlates with direction: N-terminal motors move towards plus ends, kinesin-14 with a C-terminal motor moves towards minus ends, and kinesin-13, with a central motor, depolymerizes.

| Motor | Structure | Direction | Functions |
|---|---|---|---|
| Kinesin-1 | dimer, light chains | plus end | anterograde transport of organelles, vesicles, mRNA |
| Kinesin-2 | heterotrimer | plus end | intraflagellar transport, melanosomes |
| Kinesin-3 (KIF1A) | dimer, fast and superprocessive | plus end | synaptic vesicle precursors in axons |
| Kinesin-5 (Eg5) | bipolar tetramer | plus end (both ends) | slides antiparallel spindle microtubules apart |
| Kinesin-13 (MCAK) | dimer | none (depolymerase) | catastrophes, kinetochore error correction |
| Kinesin-14 (Ncd, KIFC1) | dimer, C-terminal motor | minus end | spindle pole focusing |
| Cytoplasmic dynein-1 + dynactin + adaptor | AAA+ ring dimer | minus end | retrograde transport, Golgi positioning, spindle and nuclear positioning |
| Axonemal dyneins | one to three heads | minus end | ciliary and flagellar beating |

![Microtubule motors and their directions (schematic; plus ends on the right). A: kinesin-1 carries a vesicle towards the plus end; cytoplasmic dynein-1, with dynactin (grey rod) and an activating adaptor (pink coiled coil), carries one towards the minus end. B: kinesin-5, a bipolar tetramer, walks towards the plus ends of two antiparallel microtubules and slides each towards its minus end. C: kinesin-13 at a microtubule end bends terminal dimers off and depolymerizes it](./plots/motors-on-tracks.py)

### 14.5.2. How Kinesin Walks

Optical traps (*optical tweezers*: a laser focused to a diffraction-limited spot that holds a dielectric bead in a harmonic potential; theory in [7.6](/7.6)) measured kinesin stepping one molecule at a time. A bead carried by one kinesin moves in steps of $8.2\,\mathrm{nm}$, the length of a tubulin dimer (Svoboda and colleagues, 1993), and the number of steps equals the number of ATP hydrolyzed (Schnitzer and Block, 1997; Hua and colleagues, 1997). Kinesin-1 moves at about $0.8\,\mu\mathrm{m\,s^{-1}}$ without load (about 100 steps per second), stalls at $6$–$7\,\mathrm{pN}$, and takes on average about 100 steps before it detaches. The force times the step, $6\,\mathrm{pN} \times 8\,\mathrm{nm} \approx 50\,\mathrm{pN\,nm}$, is about half the free energy of ATP hydrolysis in the cell (about $100\,\mathrm{pN\,nm}$ per molecule).

**Definition 14.5.4 (Hand-Over-Hand Mechanism)** In the **hand-over-hand mechanism** of a two-headed motor, the two heads alternate: the rear head detaches and moves forward past the bound head to the next binding site, so that each head moves twice the step of the molecule, and at least one head is always bound.

For kinesin-1, a head labeled with one fluorophore moves alternately $16.6$ and $0\,\mathrm{nm}$, while the stalk moves $8.3\,\mathrm{nm}$ per step (Yildiz and colleagues, 2004), as for myosin V ([7.3.13](/7.3.13#sec-13.5.5)). The heads are coordinated through the neck linker: when ATP binds the front head, its neck linker docks onto the motor domain and throws the rear head forward; tension between the heads keeps the front head from binding ATP before the rear head has released, so that the two cycles stay out of phase. The result is high processivity, as defined for polymerases (**processivity**, [7.2.7](/7.2.7)).

**Formula 14.5.1 (A Two-Step Kinetic Model of Kinesin)** If each step requires ATP binding at rate $k_{\mathrm{b}}[\mathrm{ATP}]$ followed by an ATP-independent, load-dependent transition at rate $k_2(F) = k_2\,\mathrm{e}^{-Fx/k_{\mathrm{B}}T}$, where $x$ is the distance over which load acts on that transition, the forward stepping rate and velocity are

$$
k_{\mathrm{f}} = \left(\frac{1}{k_{\mathrm{b}}[\mathrm{ATP}]} + \frac{1}{k_2(F)}\right)^{-1}, \qquad v = d\,(k_{\mathrm{f}} - k_{\mathrm{r}}),
\tag{14.3}
$$
with $d = 8.2\,\mathrm{nm}$ and a backward stepping rate $k_{\mathrm{r}}$ that equals $k_{\mathrm{f}}$ at the stall force. Without load, $v$ follows the **Michaelis–Menten equation** in [ATP], with $v_{\max} = dk_2$ and $K_{\mathrm{M}} = k_2/k_{\mathrm{b}}$.

Load slows the mechanical transition, so it raises the apparent $K_{\mathrm{M}}$ for ATP: kinesin behaves as an enzyme whose kinetic constants depend on force. Since dwell times between steps are the sum of two exponential waiting times, their distribution is not exponential at intermediate [ATP]; the shape of the dwell-time distribution counts the rate-limiting steps per cycle, a method used throughout single-molecule enzymology ([7.6](/7.6)).

![Mechanics of kinesin-1. A: hand-over-hand stepping (schematic): with both heads bound, the rear head (marked) detaches, swings 16 nm forward past the bound head and binds the next tubulin dimer, while the stalk and its cargo advance 8 nm. B: force–velocity curves from the two-step model of Formula 14.5.1 at saturating and low ATP: velocity falls with load and reaches zero at the stall force of about 6 pN, beyond which backward steps dominate. C: run lengths of 2000 simulated molecules that detach with probability 1/125 per step: exponential, mean about 1 µm](./plots/kinesin-mechanics.py)

### 14.5.3. Axonal Transport and Teams of Motors

A motor neuron of the human leg has an axon a meter long, and all of its proteins except a few made locally are synthesized in the cell body. Diffusion cannot supply it: with $D = L^2/2t$, a vesicle with an effective diffusion coefficient of $0.01\,\mu\mathrm{m^2\,s^{-1}}$ in cytoplasm would need $5\times10^{13}\,\mathrm{s}$, more than a million years, to travel one meter, while a motor at $1\,\mu\mathrm{m\,s^{-1}}$ needs about 12 days.

**Definition 14.5.5 (Axonal Transport)** **Axonal transport** is the motor-driven movement of materials along the microtubules of an axon: anterograde transport from the cell body to the terminals by kinesins, and retrograde transport back to the cell body by dynein. Fast transport moves membrane organelles at $50$–$400\,\mathrm{mm\,d^{-1}}$ ($0.5$–$5\,\mu\mathrm{m\,s^{-1}}$); slow transport moves cytoskeletal proteins and soluble enzymes at $0.2$–$8\,\mathrm{mm\,d^{-1}}$.

Mitochondria move at intermediate average rates (tens of millimeters per day), because their fast runs in both directions alternate with long stationary periods. Slow transport is not a slower motor. Imaging of single neurofilaments showed that they move at fast-transport speeds in short bursts separated by long pauses, so that their average speed is low ("stop and go"; Brown and colleagues). Retrograde transport carries signaling endosomes with neurotrophin receptors from the terminals, telling the cell body that the axon has reached its target, as well as damaged organelles for degradation; rabies and herpes viruses use it to reach the cell body. Defects in transport cause neurodegeneration: mutations in KIF5A, KIF1A, dynein and dynactin cause forms of spastic paraplegia, Charcot–Marie–Tooth neuropathy and motor neuron disease.

Most cargoes carry several motors, often of opposite directions, and their movement is the result of a team. A single kinesin runs about $1\,\mu\mathrm{m}$, but a cargo detaches only when all its motors have let go, and a detached motor can rebind while its partners hold the cargo near the track.

**Formula 14.5.2 (Run Length of a Team of Motors)** For a cargo carried by up to $N$ identical motors that each unbind at rate $\varepsilon$ and rebind at rate $\pi$ while the cargo is attached, and move at velocity $v$, the mean run length without load is (Klumpp and Lipowsky, 2005)

$$
\langle \Delta x\rangle = \frac{v}{N\pi}\left[\left(1 + \frac{\pi}{\varepsilon}\right)^N - 1\right].
\tag{14.4}
$$
For $N = 1$ it reduces to $v/\varepsilon$; for $\pi \gg \varepsilon$ it grows roughly geometrically with $N$.

With $\pi/\varepsilon = 5$, two motors run 3.5 times and three motors 14 times as far as one. Teams of opposite-directed motors produce bidirectional movement: a tug of war in which the stronger side wins, stochastic switching between plus- and minus-end runs, and regulation by adaptors or by phosphorylation that tips the balance (for example of mitochondria, which stop at synapses where $\ce{Ca^2+}$ is high).

![Why cells need motors and why cargoes carry several. A: the time to move over a distance $L$ by diffusion ($t = L^2/2D$) for a small protein and for a vesicle hindered by the cytoskeleton, compared with transport by a motor at $1\,\mu\mathrm{m\,s^{-1}}$; dashed lines mark a cell, a dendrite and a one-meter axon. Below about $20\,\mu\mathrm{m}$ diffusion of small molecules suffices; over the length of an axon only motors work. B: mean run length of a cargo carried by $N$ kinesins (unbinding rate 1 s⁻¹, rebinding rate 5 s⁻¹): Gillespie simulations (points) and Formula 14.5.2 (line)](./plots/cargo-transport.py)

Motors also position organelles. The Golgi apparatus clusters around the centrosome because dynein pulls it inward; the endoplasmic reticulum spreads outward along microtubules, pulled by kinesins and by attachment to growing plus ends; lysosomes and endosomes move outward or inward depending on the balance of kinesin and dynein recruited by small GTPases (Arl8, Rab7) and their adaptors ([7.3.10](/7.3.10), [7.3.11](/7.3.11)). That these positions depend on microtubules is shown by depolymerizing them with colchicine or nocodazole: the ER network retracts towards the nucleus and the Golgi ribbon breaks up into ministacks scattered through the cytoplasm, mostly at ER exit sites; when the drug is washed out, microtubules regrow from the centrosome and dynein gathers the Golgi elements back to the cell center within an hour ([7.3.9](/7.3.9)). In melanophores of fish and frogs, hormones switch pigment granules between dynein-driven aggregation and kinesin-driven dispersion, changing the skin color within minutes.

## 14.6. Cilia and Flagella

### 14.6.1. The Axoneme

**Definition 14.6.1 (Cilium and Flagellum)** A **cilium** is a hairlike projection of a eukaryotic cell, about $0.25\,\mu\mathrm{m}$ wide and a few to tens of micrometers long, bounded by an extension of the plasma membrane and supported by a microtubule-based axoneme that grows from a basal body. A **flagellum** of a eukaryotic cell has the same structure; the names usually distinguish many short cilia that beat in coordinated waves (on epithelia and ciliates) from one or a few long flagella that propagate waves along their length (sperm, many protists).

**Definition 14.6.2 (Axoneme and Basal Body)** The **axoneme** is the microtubule core of a cilium. In motile cilia it has a **9 + 2** arrangement: nine outer doublet microtubules (a complete A tubule of 13 protofilaments fused to an incomplete B tubule of 10) around a central pair of singlet microtubules, with inner and outer dynein arms attached to each A tubule, radial spokes projecting to the central pair, and nexin–dynein regulatory complexes linking neighboring doublets. The **basal body** at its base is a centriole that templates the doublets from its triplets and anchors the cilium.

The axoneme is one of the most regular structures of the cell, assembled from more than 600 proteins with repeats of $96\,\mathrm{nm}$ along each doublet. It is conserved from *Chlamydomonas* to humans, which made that alga, with its two flagella and its many viable mutants, the main genetic model for cilia. Along its length a cilium has three zones: the basal body inside the cell, with nine triplets and no central pair (9 + 0 triplets), a transition zone (14.6.3), and the shaft (the axoneme proper) above the cell surface. Axonemes come in a few patterns. The 9 + 2 axoneme is the rule for motile cilia and flagella, and the 9 + 0 axoneme without dynein arms for nonmotile primary cilia (14.6.4); exceptions exist in both directions, the motile 9 + 0 cilia of the embryonic node with dynein arms (14.6.4) and the motile 9 + 0 sperm flagella of eels and 9 + 1 axonemes of flatworm sperm, and rarer variants such as 9 + 4 cilia have been described in the notochordal plate of the rabbit embryo.

Motile cilia work in large numbers. The epithelium of the human airways carries about 200 cilia on each ciliated cell, of the order of $10^9$ per square centimeter, which sweep a layer of mucus with trapped dust and bacteria towards the throat (the mucociliary escalator); cilia of the oviduct move the egg towards the uterus; and ciliates such as *Paramecium* use thousands of cilia, beating in metachronal waves, both to swim and to drive food into the oral groove.

### 14.6.2. From Sliding to Bending

The dynein arms on the A tubule of each doublet walk on the B tubule of the next doublet towards its minus end, at the base of the cilium, and thus push the neighbor towards the tip. If all doublets could slide freely, the axoneme would simply telescope. This is what Summers and Gibbons (1971) saw when they treated isolated sea urchin sperm axonemes briefly with trypsin and then added ATP: the axonemes fell apart into doublets that slid out of the bundle, up to nine times their original length. In the intact axoneme, the nexin links and the attachment at the basal body resist sliding, and sliding is converted into bending, as two strips glued at one end bend when one slides relative to the other.

A wave requires that dyneins on opposite sides of the axoneme be active at different times. The central pair and the radial spokes, which act as mechanochemical relays, switch dynein activity from one side to the other, and the curvature or sliding itself may feed back on dynein (the "geometric clutch" and related models), producing self-organized oscillation. Ciliary beating is fast: $10$–$60\,\mathrm{Hz}$, with the effective stroke and recovery stroke of airway cilia moving mucus at about $5\,\mathrm{mm\,min^{-1}}$.

![Cilia and flagella (schematic). A: a motile 9 + 2 axoneme in cross-section seen from the base: nine outer doublets with outer and inner dynein arms (purple) pointing to the neighboring doublet, radial spokes (gold) to the central sheath, nexin links between doublets, and the central pair. B: a primary cilium (9 + 0) without central pair and dynein arms. C: sliding becomes bending: after protease digestion of the links, dynein slides doublets apart (left); in the intact axoneme nexin links and the basal body resist sliding, which is converted into bending (right). D: intraflagellar transport: kinesin-2 carries IFT trains with cargo (gold) to the tip, dynein-2 returns them to the base; the transition zone above the basal body gates entry](./plots/axoneme.py)

### 14.6.3. Building and Maintaining a Cilium

Cilia have no ribosomes; every axonemal protein is made in the cytoplasm and delivered to the growing tip.

**Definition 14.6.3 (Intraflagellar Transport)** **Intraflagellar transport** (IFT) is the bidirectional movement of protein trains (IFT-A and IFT-B complexes with their cargoes) between the axoneme and the ciliary membrane: kinesin-2 carries them from the base to the tip (anterograde), and dynein-2 returns them (retrograde).

IFT was discovered in *Chlamydomonas* by Kozminski and Rosenbaum (1993). The length of a flagellum results from a balance between delivery by IFT, which decreases as the flagellum grows because a fixed number of trains must travel farther, and a length-independent disassembly at the tip, a balance-point mechanism of size control comparable to the limiting-pool model of [7.3.6](/7.3.6#sec-6.2). At the base, the transition zone, a ring of Y-shaped links between the doublets and the membrane, acts as a diffusion barrier and gate, and the BBSome adapts membrane proteins to IFT; this is why the ciliary membrane has a composition different from the plasma membrane around it.

### 14.6.4. Primary Cilia and Ciliopathies

**Definition 14.6.4 (Primary Cilium)** A **primary cilium** is a single nonmotile cilium with a 9 + 0 axoneme, grown from the mother centriole by most vertebrate cells when they are not dividing, whose membrane is enriched in receptors and channels and which serves as a sensory and signaling antenna.

Primary cilia were long considered vestigial, until defects in IFT genes were found to cause polycystic kidney disease in mice (Pazour and colleagues, 2000), and the Hedgehog pathway was found to require them (Huangfu and colleagues, 2003): in vertebrates the receptor Patched, the transducer Smoothened and the Gli transcription factors move into or out of the cilium as the pathway is switched on ([7.3.19](/7.3.19)). The cilia of kidney epithelial cells carry the polycystins PC1 and PC2, a mechanosensitive and $\ce{Ca^2+}$-permeable channel complex; photoreceptors of the retina are modified cilia, and so are the olfactory cilia that carry odorant receptors.

**Definition 14.6.5 (Ciliopathy)** A **ciliopathy** is a genetic disorder caused by defects in the structure or function of cilia or basal bodies. Defects of motile cilia cause primary ciliary dyskinesia; defects of primary cilia cause syndromes affecting kidney, retina, brain, skeleton and metabolism.

| Disorder | Defect | Main features |
|---|---|---|
| Primary ciliary dyskinesia (Kartagener syndrome when combined with situs inversus) | dynein arms, radial spokes, central pair | chronic sinusitis and bronchiectasis (no mucus clearance), male infertility, randomized left–right asymmetry |
| Autosomal dominant polycystic kidney disease | polycystin-1 or -2 | kidney cysts, the most common inherited kidney disease |
| Nephronophthisis, Joubert, Meckel–Gruber syndromes | transition-zone proteins | kidney cysts, cerebellar malformation, polydactyly; lethal in Meckel–Gruber |
| Bardet–Biedl syndrome | BBSome | obesity, retinal degeneration, polydactyly, kidney defects |

The left–right axis of the vertebrate body depends on motile cilia of a special kind: in the embryonic node, monocilia with a 9 + 0 axoneme and dynein arms rotate clockwise and, because they are tilted posteriorly, drive a leftward flow of extracellular fluid that is sensed by cilia at the left edge of the node (Nonaka and colleagues, 1998). Without this flow, as in mice lacking the kinesin-2 subunit KIF3B or dynein, the heart and visceral organs are placed randomly ([7.5](/7.5)).

### 14.6.5. Eukaryotic and Bacterial Flagella

The flagella of bacteria and eukaryotes share a name and nothing else:

| | Eukaryotic flagellum | Bacterial flagellum ([7.3.1](/7.3.1), [7.11](/7.11)) |
|---|---|---|
| Structure | 9 + 2 axoneme of microtubules inside the plasma membrane | extracellular helical filament of flagellin, a hook, and a rotary motor in the envelope |
| Motor | many axonemal dyneins distributed along the length | one rotary motor at the base (rotor MS and C rings, stator units MotA/MotB) |
| Energy | ATP | **proton-motive force** (Na⁺ gradient in some species), about 1000 protons per revolution |
| Movement | bending waves, $10$–$100\,\mathrm{Hz}$ | rigid rotation of a helical propeller, $100$–$300\,\mathrm{Hz}$, reversible |
| Assembly | at the tip, by intraflagellar transport | at the tip, by export of flagellin through the hollow filament (type III secretion) |

Both solve the same physical problem: swimming at low Reynolds number, where a reciprocal motion that retraces its path produces no net displacement (Purcell's scallop theorem). Waves that travel along a flexible flagellum and the rotation of a helix are both nonreciprocal. Archaea swim with yet a third structure, the archaellum, a rotating filament related to type IV pili and driven by ATP.

## Summary

| Topic | Key points |
|---|---|
| Structure (14.1, Definition 14.1.1) | αβ-tubulin dimer (GTP on α buried, on β exchangeable); 13 protofilaments, 25 nm tube, B lattice with a seam; 1625 dimers per µm; plus end = β exposed; discovered 1963 (glutaraldehyde); in vitro assembly at 37 °C with GTP and Mg²⁺, disassembly by cold, pressure, Ca²⁺; singlets, doublets (axonemes), triplets (centrioles); tubulin code (detyrosination, acetylation, polyglutamylation) |
| Dynamic instability (14.2, Definitions 14.2.1–14.2.2, Formula 14.2.1) | GTP cap; catastrophe and rescue; Mitchison–Kirschner 1984; GDP lattice strained, curved protofilaments; Dogterom–Leibler: $\langle L\rangle = v_{\mathrm{g}}v_{\mathrm{s}}/(v_{\mathrm{s}}f_{\mathrm{cat}} - v_{\mathrm{g}}f_{\mathrm{res}})$, exponential length distribution, unbounded growth at $v_{\mathrm{g}}f_{\mathrm{res}} > v_{\mathrm{s}}f_{\mathrm{cat}}$; mitosis raises $f_{\mathrm{cat}}$; search and capture; compared with treadmilling of actin |
| MTOCs (14.3, Definitions 14.3.1–14.3.3) | γ-TuRC (13 γ-tubulins, caps minus ends); augmin branching; centrosome: two orthogonal centrioles (nine triplets, SAS-6 cartwheel, Plk4 duplication once per cycle) in PCM; dispensable for spindles, essential for cilia; arrays in fibroblasts, epithelia, neurons, plants |
| Regulators (14.4, Definitions 14.4.1–14.4.3) | MAPs (tau, MAP2, XMAP215); +TIPs (EB1 comets, CLIP-170, CLASP, APC); kinesin-13, stathmin; severing by katanin, spastin (hereditary spastic paraplegia); colchicine, nocodazole, vinca alkaloids, taxol: mitotic arrest, cancer therapy |
| Motors (14.5, Definitions 14.5.1–14.5.5, Formulas 14.5.1–14.5.2) | Kinesin discovered in squid axoplasm (Vale 1985); 45 kinesin genes, direction by motor position (kinesin-14 minus, kinesin-13 depolymerase, kinesin-5 bipolar); dynein AAA+ ring, stalk, linker; dynactin and activating adaptors; kinesin-1: 8.2 nm steps, one ATP per step, $0.8\,\mu\mathrm{m\,s^{-1}}$, stall 6 pN, about 100 steps, hand-over-hand (16 nm head steps); two-step model, force-dependent $K_{\mathrm{M}}$; axonal transport fast vs slow (stop-and-go), mitochondria intermediate; ER and Golgi positions collapse with nocodazole; diffusion $L^2/2D$ vs $L/v$; teams: $\langle\Delta x\rangle = \frac{v}{N\pi}[(1+\pi/\varepsilon)^N - 1]$; tug of war; organelle positioning |
| Cilia (14.6, Definitions 14.6.1–14.6.5) | basal body, transition zone, shaft; 9 + 2 motile, 9 + 0 primary (exceptions: nodal, eel sperm); airway escalator; 9 + 2 axoneme, doublets A + B, dynein arms, radial spokes, nexin; basal body; sliding converted to bending (Summers–Gibbons 1971); IFT (kinesin-2, dynein-2; balance-point length control), transition zone; primary cilia (9 + 0) and Hedgehog, polycystins; ciliopathies (PCD/Kartagener, ADPKD, Bardet–Biedl); nodal flow and left–right asymmetry; bacterial flagellum: rotary, proton-driven |

## Questions

1. A microtubule in a cell grows at $12\,\mu\mathrm{m\,min^{-1}}$, shrinks at $24\,\mu\mathrm{m\,min^{-1}}$, has a catastrophe frequency of $0.05\,\mathrm{s^{-1}}$ and a rescue frequency of $0.02\,\mathrm{s^{-1}}$. (a) Is growth bounded? What is the mean length? (b) At mitosis the catastrophe frequency rises to $0.2\,\mathrm{s^{-1}}$. What happens to the mean length? (c) What rescue frequency would make growth unbounded in interphase?

   **Answer** In µm/s, $v_{\mathrm{g}} = 0.2$, $v_{\mathrm{s}} = 0.4$. (a) $v_{\mathrm{s}}f_{\mathrm{cat}} = 0.02 > v_{\mathrm{g}}f_{\mathrm{res}} = 0.004$: bounded, with $\langle L\rangle = 0.2 \times 0.4/(0.02 - 0.004) = 5\,\mu\mathrm{m}$. (b) $\langle L\rangle = 0.08/(0.08 - 0.004) \approx 1.05\,\mu\mathrm{m}$: microtubules become about five times shorter, and many more of them can be supported by the same tubulin pool. (c) $f_{\mathrm{res}} > v_{\mathrm{s}}f_{\mathrm{cat}}/v_{\mathrm{g}} = 0.1\,\mathrm{s^{-1}}$.

2. How would you show that a growing microtubule is stabilized by a cap at its plus end and not by its lattice? Describe two experiments and their expected results.

   **Answer** (1) Cut growing microtubules in the middle (with a laser or by ultraviolet microbeam): the new plus ends, which expose the GDP lattice without a cap, shrink immediately, while the new minus ends (which shrink slowly) often persist; this shows that the lattice itself is unstable. (2) Dilute growing microtubules abruptly to remove free tubulin: they undergo catastrophes after a delay of a few seconds, the time needed for the cap to be hydrolyzed, and the delay depends on the growth rate before dilution. Alternatively, polymerize with GMPCPP, a slowly hydrolyzable GTP analog: such microtubules do not undergo catastrophes; or image EB1 comets, whose size reports the cap and shrinks before catastrophe.

3. Kinesin-1 moves at $800\,\mathrm{nm\,s^{-1}}$ at saturating ATP and at $400\,\mathrm{nm\,s^{-1}}$ at $50\,\mu\mathrm{M}$ ATP. (a) Using Formula 14.5.1 without load, find $k_2$ and $k_{\mathrm{b}}$. (b) What is the maximal efficiency of the motor at a load of $5\,\mathrm{pN}$ if ATP hydrolysis provides $\Delta G = -100\,\mathrm{pN\,nm}$ per molecule?

   **Answer** (a) $v_{\max} = dk_2 = 800\,\mathrm{nm\,s^{-1}}$, so $k_2 = 800/8.2 \approx 98\,\mathrm{s^{-1}}$. Half-maximal velocity at $50\,\mu\mathrm{M}$ means $K_{\mathrm{M}} = k_2/k_{\mathrm{b}} = 50\,\mu\mathrm{M}$, so $k_{\mathrm{b}} \approx 2\,\mu\mathrm{M^{-1}\,s^{-1}}$. (b) Work per step $= 5\,\mathrm{pN} \times 8.2\,\mathrm{nm} = 41\,\mathrm{pN\,nm}$, one ATP per step: efficiency $41/100 \approx 40\,\%$, rising towards about $50\,\%$ near the stall force (where the velocity, and hence the power, is small).

4. Show from Formula 14.5.2 that two motors with $\pi/\varepsilon = 5$ give a run length 3.5 times that of one. Why might adding motors not increase run length under load as much as without load?

   **Answer** For $N = 2$: $\langle\Delta x\rangle = \frac{v}{2\pi}[(1+5)^2 - 1] = \frac{35v}{2\pi} = \frac{35v}{10\varepsilon} = 3.5\,v/\varepsilon$, compared with $v/\varepsilon$ for one motor. Under load, the force is shared among the bound motors; when one detaches, the remaining one carries the whole load, and since the unbinding rate increases with force, the last motor detaches faster than it would unloaded. The cascade makes teams less effective at high loads, and motors that are not mechanically coupled (for example on a fluid membrane) may share load unevenly.

5. A patient has chronic bronchitis, sinusitis and infertility, and the heart lies on the right side. (a) What is the likely diagnosis and which structures would you examine by electron microscopy? (b) Why is the position of the heart random rather than always reversed? (c) Why are the kidneys usually normal?

   **Answer** (a) Primary ciliary dyskinesia (Kartagener syndrome); cross-sections of respiratory cilia (from a nasal brush biopsy) and sperm flagella, looking for missing outer and/or inner dynein arms, radial spokes or central pair; high-speed video of ciliary beating and genetic testing confirm it. (b) Without nodal flow the left–right asymmetry is not determined at all: each embryo chooses at random, so about half of patients have situs inversus and half normal situs. (c) The kidney tubules depend on primary (nonmotile) cilia and their polycystin signaling, which do not need the motile machinery that is defective.

6. (Open) Compare the strategies by which a cell sets the length of (a) a flagellum, (b) its interphase microtubules, (c) an actin bundle in a stereocilium. Which use a balance between length-dependent and length-independent rates?

   **Answer** (a) Flagellum: balance point. IFT delivers precursors at a rate that falls with length (a fixed number of trains, each taking longer to travel), while disassembly at the tip is length-independent; the steady length is where they are equal, and severing one of two flagella shows the remaining one shortening while the cut one regrows, as expected from a shared, limited precursor pool and delivery. (b) Interphase microtubules: not one length but an exponential distribution set by the dynamic-instability parameters (Formula 14.2.1); the cell controls the mean through $f_{\mathrm{cat}}$ and $f_{\mathrm{res}}$, and length-dependent effects arise when motors such as kinesin-8 accumulate at plus ends of longer microtubules in proportion to their length and promote catastrophe. (c) Stereocilia: very slow turnover at the tips, with length set during development by tip-localized myosins (III, XV) that transport proteins promoting elongation, a length-dependent delivery against tip depolymerization, again a balance-point mechanism.
