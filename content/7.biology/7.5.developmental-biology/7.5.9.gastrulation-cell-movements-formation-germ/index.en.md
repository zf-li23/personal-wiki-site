---
title: "Gastrulation: Cell Movements and the Formation of Germ Layers"
description: "How the blastula becomes a three-layered embryo. Germ layers and their derivatives; the six movements of epithelial sheets and their cellular engines; gastrulation in sea urchins, Drosophila, amphibians, fish, birds and mammals; mechanical models: the blastula as a Stokes drop driven by surface tension (Legendre modes, the gastrulation mode, the hollow blastula and the reversal of force at the blastopore), gastrulation as an instability and the finite-time steepening of tension, the strain field and bottle cells, the dissipation principle and a vertex model of invagination by apical constriction, epiboly as a spreading thin film; extraembryonic membranes and the placenta; inversion in Volvox and sponges."
---

"It is not birth, marriage, or death, but gastrulation, which is truly the most important time in your life." Lewis Wolpert's remark is literally true for the body plan. During gastrulation the cells of the **blastula** ([7.5.5](/7.5.5)) move as sheets and as individuals, so that those that will form the gut and its derivatives come to lie inside, those that will form the skin and nervous system cover the outside, and those that will form muscle, skeleton, blood and kidney lie between. At the same time the embryo acquires its axes, and cells that were far apart become neighbours, which allows the inductive interactions of the following chapters ([7.5.16](/7.5.16)–[7.5.18](/7.5.18)). This chapter describes the movements, compares how the model species perform them with very different eggs, and treats gastrulation as a problem in mechanics. The mechanical tools come from [7.5.7](/7.5.7) (adhesion and **tissue surface tension**) and [7.5.8](/7.5.8) (viscous flow of tissues); here they are applied: the amphibian blastula as a viscous drop whose surface tension varies with cell type, the steepening of that tension into a localized invagination, a **vertex model** of an epithelium bending by apical constriction, and the spreading of the fish blastoderm as a thin film. The signals that specify the germ layers and the organizer are the subject of [7.5.16](/7.5.16); the chapter ends with the extraembryonic membranes of amniotes and the placenta, which the mammalian embryo builds before and during gastrulation.

## 9.1. What Gastrulation Achieves

**Definition 9.1.1 (Gastrulation, Gastrula)** **Gastrulation** is the process of coordinated cell movements by which the cells of the blastula are rearranged into the germ layers of the embryo, the prospective endoderm and mesoderm moving inside and the prospective ectoderm spreading over the outside. The embryo during this process is the **gastrula**.

**Definition 9.1.2 (Germ Layers)** The **germ layers** are the three primary cell layers established by gastrulation in triploblastic animals: the **ectoderm** (outer), which forms the epidermis, the nervous system and the **neural crest**; the **endoderm** (inner), which forms the epithelial lining of the gut and respiratory tract and the organs that bud from them; and the **mesoderm** (middle), which forms muscle, skeleton, connective tissue, the heart, blood and blood vessels, the kidneys and gonads. Diploblastic animals (cnidarians, ctenophores) have only ectoderm and endoderm.

The main derivatives in vertebrates, which the chapters on organogenesis develop, are listed below.

| Germ layer | Main derivatives (vertebrates) | Chapters |
|---|---|---|
| Ectoderm | epidermis and its appendages (hair, feathers, scales, glands, tooth enamel); central nervous system; neural crest (peripheral nervous system, pigment cells, facial skeleton); **placodes** (lens, inner ear, olfactory epithelium) | [7.5.18](/7.5.18)–[7.5.22](/7.5.22) |
| Mesoderm | axial: notochord, prechordal plate; paraxial: **somites** (vertebrae, skeletal muscle, dermis); intermediate: kidney, gonads; lateral plate: heart, blood and vessels, body-wall connective tissue, limb skeleton | [7.5.23](/7.5.23)–[7.5.29](/7.5.29), [7.5.31](/7.5.31) |
| Endoderm | epithelium of the gut, from pharynx to rectum; lungs; liver, pancreas, thyroid, thymus; bladder | [7.5.30](/7.5.30) |

The germ layers are a reliable description, not a law: neural crest cells of ectodermal origin form bone and cartilage of the head that elsewhere come from mesoderm, and **primordial germ cells** are set aside outside the layers ([7.5.27](/7.5.27)). The term also has an evolutionary meaning. In most animals the opening through which cells move inside during gastrulation, the **blastopore** (9.5.1), becomes the mouth (protostomes, Greek "mouth first": molluscs, annelids, arthropods, nematodes), and in others the anus, the mouth forming separately (deuterostomes: echinoderms, hemichordates, chordates); the distinction is less clean than it seemed, since in several protostomes the blastopore forms both openings or the anus.

## 9.2. The Movements of Gastrulation

Cells in embryos are organized in two ways: epithelial cells, joined by junctions into sheets or tubes, with an apical and a basal surface, that move as a coherent tissue; and mesenchymal cells, loosely connected or isolated, that move independently. The **epithelial–mesenchymal transition** ([7.3.23](/7.3.23)) converts the first into the second, and the reverse transition (MET) the second into the first; both are used in gastrulation. Six kinds of movement are distinguished (figure below).

**Definition 9.2.1 (Movements of Gastrulation)** In **invagination** a region of an epithelial sheet folds inwards, like the indentation of a soft ball. In **involution** an expanding outer sheet rolls inwards over a lip and spreads along the inner surface of the remaining outer cells. In **epiboly** a sheet of cells spreads, usually thinning, to cover deeper layers or the yolk. In **ingression** individual cells leave an epithelium, by an **epithelial–mesenchymal transition**, and move into the interior. In **delamination** one cell sheet splits into two more or less parallel sheets. In **convergent extension** cells intercalate between their neighbours so that the tissue narrows (converges) in one direction and lengthens (extends) in the perpendicular one.

![The six cell movements of gastrulation (grey arrows: direction of movement). Invagination: a region of an epithelial sheet folds inwards. Involution: an expanding sheet rolls over a lip and spreads on the inner surface. Epiboly: a sheet thins and spreads over deeper layers or the yolk. Ingression: single cells leave the epithelium and move inside as mesenchyme. Delamination: one sheet splits into two. Convergent extension: cells intercalate, and the tissue narrows in one direction and lengthens in the perpendicular one (seen from above)](./plots/sheet-movements.py)

Each movement is produced by a small set of cellular engines, which are found in all embryos in different combinations:

- Apical constriction: contraction of an actomyosin network (**myosin II**, [7.3.13](/7.3.13)) under the apical surface narrows the apex of a cell and makes it wedge-shaped; a group of such cells bends the sheet (invagination; bottle cells).
- Cell intercalation: polarized cell rearrangements, guided by the planar **cell polarity** pathway (the non-canonical branch of Wnt signalling) in vertebrates or by planar-polarized **myosin** in *Drosophila*, drive convergent extension; radial intercalation of cells between those of an overlying layer thins the tissue and expands its area (epiboly of the amphibian animal cap).
- Directed migration: mesenchymal cells crawl on an **extracellular matrix** of **fibronectin** using **integrins** ([7.3.23](/7.3.23)), as the amphibian mesoderm does on the **blastocoel** roof.
- Changes of adhesion: loss of E-**cadherin** and of contact with the **basal lamina** release cells (ingression); differences in adhesion and **cortical tension** drive the sorting of tissues into layers ([7.5.7](/7.5.7)).
- Changes of cell shape and volume, and oriented cell division, which add tissue in a chosen direction.
- Forces from outside the moving tissue: swelling of the **extracellular matrix**, and, in fish, contraction of the yolk cell.

## 9.3. Sea Urchins

The sea urchin blastula is a single epithelial layer around the blastocoel, attached on the outside to the hyaline layer and lined inside by a **basal lamina** ([7.5.5](/7.5.5)). Gastrulation begins with the thickening and flattening of the vegetal plate and proceeds in three steps.

1. Ingression of the primary mesenchyme. The 32 descendants of the large micromeres (the **skeletogenic mesenchyme**, [7.5.6](/7.5.6)) lose their affinity for the hyaline layer and for their neighbours and gain one for the basal lamina and the fibronectin-containing matrix of the blastocoel wall; they lose **cadherin** and **β-catenin** from their junctions, extend filopodia and leave the epithelium by an epithelial–mesenchymal transition. In the blastocoel they migrate along the wall, guided by cues from the ectoderm (VEGF and FGF), and settle in a ring with two ventrolateral clusters, where they fuse into a syncytium and secrete the calcite spicules.
2. Primary invagination. The remaining vegetal plate bends inwards to form the archenteron, the primitive gut, which reaches about a quarter to a half of the way across the blastocoel. The bending is driven by apical constriction of the vegetal cells and by the swelling of the inner layer of the hyaline layer: the vegetal cells secrete a chondroitin sulfate **proteoglycan** into it, which takes up water, while the outer layer does not swell, so the bilayer bends like a bimetallic strip.
3. Extension and secondary invagination. The archenteron elongates to about three times its length by convergent extension, its cells rearranging so that a tube of about 30 cells in circumference becomes one of about 6–8. At its tip, the secondary mesenchyme cells extend long filopodia across the blastocoel to the animal wall; the filopodia attach, contract and pull the archenteron the last part of the way. Laser ablation of the secondary mesenchyme stops the final third of the elongation. Where the tip meets the wall, the mouth forms; the blastopore becomes the anus, as in all deuterostomes.

![Gastrulae of the model species in section, coloured by germ layer. Sea urchin: archenteron invaginated from the vegetal plate, primary mesenchyme in the blastocoel, secondary mesenchyme at the archenteron tip with filopodia. Frog (mid-gastrula, dorsal right): bottle cells at the dorsal lip, involuted mesoderm under the ectoderm, archenteron, shrinking blastocoel and yolk plug. Zebrafish (shield stage, dorsal right): blastoderm over about 60 % of the yolk, germ ring, shield, enveloping layer and yolk syncytial layer. Chick (transverse section through the primitive streak): epiblast cells ingress through the primitive groove and spread as mesoderm, or enter the lower layer as endoderm and displace the hypoblast. Mouse (egg cylinder at about E7, anterior left): epiblast cup, extraembryonic ectoderm, visceral endoderm and the anterior visceral endoderm, mesoderm leaving the primitive streak posteriorly, the node at the distal tip. Human (day 14): the bilaminar disc between amniotic cavity and yolk sac, suspended in the chorionic cavity by the connecting stalk, within the trophoblast invading the endometrium](./plots/gastrulae.py)

## 9.4. *Drosophila*

At the end of cellularization ([7.5.5](/7.5.5)) the *Drosophila* blastoderm is a single epithelium of about 6000 cells, and its **fate map** is already laid out by the gradients of [7.5.14](/7.5.14): a band of prospective mesoderm about 18 cells wide along the ventral midline, endoderm at the anterior and posterior ends, ectoderm in between, and dorsally the amnioserosa, an extraembryonic tissue.

- Ventral furrow. The mesoderm, specified by the transcription factors Twist and Snail under the control of the Dorsal gradient, invaginates in about 15 min. Twist induces the secreted protein Folded gastrulation (Fog) and the membrane protein T48, which activate RhoA and **myosin II** at the apical surface; Snail represses genes for junctional proteins and allows myosin to accumulate. Live imaging shows that the apical surfaces constrict in pulses: myosin contracts for a few tens of seconds, the cell surface shrinks, and the constriction is stabilized before the next pulse, like a ratchet. Because myosin is connected from cell to cell through **adherens junctions** into a supracellular network, the constriction creates a tension greater along the anterior–posterior axis than across it, and the tissue folds along the midline into a furrow and then a tube. The tube detaches, undergoes an epithelial–mesenchymal transition, and its cells spread as a monolayer on the inner surface of the ectoderm, guided by FGF.
- Endoderm. The posterior midgut invaginates as a pocket at the posterior pole, carrying the pole cells inside; the anterior midgut invaginates near the head. Fog-dependent apical constriction drives both.
- Germ-band extension. The ventrolateral ectoderm (the germ band) then doubles in length and halves in width in about 30 min, extending around the posterior end onto the dorsal side. It does so by cell intercalation: myosin II accumulates on cell boundaries oriented along the dorsal–ventral axis and shrinks them, while adherens junction proteins are enriched on the perpendicular boundaries; a shrinking boundary collapses to a vertex and a new one grows in the perpendicular direction, a T1 transition, or several cells meet in a rosette that resolves in the new direction. The planar polarity of myosin is set by the **pair-rule genes** ([7.5.15](/7.5.15)) through stripes of Toll-family receptors, whose different combinations in neighbouring cells mark the boundaries to be shrunk. In mutants lacking pair-rule pattern, the germ band does not extend properly.
- Amnioserosa and dorsal closure. The amnioserosa cells spread over the dorsal side; later the germ band retracts, and the epidermis closes over the amnioserosa at dorsal closure, which then degenerates.

## 9.5. Amphibians

### 9.5.1. The Process

In the late blastula of *Xenopus* the prospective ectoderm lies in the animal hemisphere, the prospective endoderm in the vegetal hemisphere, and the prospective mesoderm in a belt around the equator, the marginal zone, mostly in its deep layer. Gastrulation begins on the dorsal side, opposite the point of sperm entry ([7.5.16](/7.5.16)), and consists of several coordinated movements.

1. Bottle cells and the blastopore. A group of cells in the dorsal marginal zone constrict their apices and elongate into bottle cells, with narrow necks at the surface. This makes a groove, the dorsal lip of the **blastopore**. The groove spreads laterally and ventrally around the embryo, until the blastopore is a ring around the vegetal cells, which remain visible as the yolk plug, and then closes. The dorsal lip is the site of the **Spemann organizer** ([7.5.16](/7.5.16)).
2. Vegetal rotation. Before involution starts, the vegetal endoderm cells move upwards towards the blastocoel on the dorsal side, rotating the vegetal mass and pushing the marginal zone outwards towards the blastopore lip; this active movement of the endoderm, discovered in 1999, contributes much of the initial internalization.
3. Involution. The marginal zone rolls over the blastopore lip and moves animalwards along the inner surface of the outer layer. The first cells to involute dorsally are the prospective pharyngeal endoderm and the head mesoderm (prechordal plate), followed by the notochord and somitic mesoderm. The involuting mesoderm migrates on the blastocoel roof as a coherent mantle, attached to a matrix of **fibronectin** that the roof cells deposit; blocking fibronectin binding with peptides containing the RGD sequence stops mesoderm migration and the formation of the axis. Behind the leading cells, the archenteron opens between the involuted endoderm and the vegetal mass and expands, pushing the blastocoel to the ventral side, where it disappears.
4. Epiboly. The animal cap ectoderm expands and thins to cover the embryo, mostly by radial intercalation: cells of the deep layer move outwards between one another, reducing the number of layers from several to two.
5. Convergent extension. The dorsal mesoderm (notochord and somites) and the overlying **neural plate** narrow mediolaterally and lengthen anteroposteriorly by mediolateral intercalation: the cells become bipolar, aligned mediolaterally, and crawl between one another (Keller). This movement elongates the embryo along its axis and also helps close the blastopore. It is autonomous: explants of the dorsal marginal zone, cultured as a sandwich of two pieces, converge and extend in isolation. It requires the planar cell polarity pathway (Frizzled, Dishevelled, Wnt11), and its disruption gives short, wide embryos with an open blastopore.

**Definition 9.5.1 (Blastopore, Bottle Cells, Archenteron)** The **blastopore** is the opening or groove through which cells move into the interior during gastrulation. **Bottle cells** are flask-shaped cells, constricted at their apical surface, that line the blastopore of amphibians and initiate the groove. The **archenteron** is the primitive gut cavity formed by gastrulation, lined by endoderm.

At the end of gastrulation the endoderm lines the archenteron, the mesoderm lies between endoderm and ectoderm, and the ectoderm covers the embryo, which has kept its spherical shape and its original size.

### 9.5.2. Why a Mechanical Model

Many mechanisms have been proposed for the inward movement since the nineteenth century. Two early ones failed simple tests. The movement is not the buckling of a spherical shell under osmotic pressure: the **vegetal pole**, where invagination takes place, is the thickest and presumably strongest part of the wall, and the motions do not resemble those of a buckling shell. It is not driven by cell proliferation either: cell division can be blocked without stopping gastrulation. In 1902 Rhumbler proposed instead effective surface tension forces, derived from changes in cell shape; Holtfreter in the 1940s attributed the changes of shape to the cells' contact with a surface coat, and showed that isolated bottle cells adopt the bottle shape with their necks attached to glass. The idea was long dismissed because the measured surface tension of single cells was about a hundredth of what was needed. The objection is a fallacy: the tension of the surface of a single cell has no direct bearing on the effective tractions produced by many cells that adhere to each other and change shape. Think of sticky paper bags filled with fluid that can change shape on their own: the forces in an aggregate of them are set by their adhesion and shape changes, not by the tension of the paper. Today the forces are known to come mainly from actomyosin contractility and adhesion, which together give tissues an effective surface tension ([7.5.7](/7.5.7)), and from active cell intercalation.

The level of description matters. Many cellular mechanisms of shape change can be distinguished only at the cellular level; at the level of the whole aggregate they may all be equivalent to a differential adhesion model with an effective, position-dependent surface tension, in the way that many kinetic theories of gases give the same equation of state. The model that follows works at that level.

### 9.5.3. The Blastula as a Stokes Drop

Compare the blastula with the sorting of its cell types ([7.5.7](/7.5.7)): animal cap cells, marginal zone cells and vegetal cells, mixed, sort out with the vegetal cells inside and the animal cells outside. The initial arrangement, vegetal cells at one pole, is therefore far from the equilibrium of the **differential adhesion hypothesis**, which would be an onion with endoderm at the centre. If the surface tension at the vegetal (endodermal) pole is higher than at the animal (ectodermal) pole, surface forces should produce invagination at the vegetal pole, spreading of the animal cells, and a general flow towards the onion equilibrium. In this idealization gastrulation is a mechanical response to an initial layering that is not in equilibrium.

We make three simplifications: ignore the blastocoel and treat the blastula as a solid sphere of radius 1 filled with a viscous fluid of unit viscosity; assume that the surfaces of constant cell type are planes perpendicular to the animal–vegetal axis; and assume that all forces act at the surface $S$, which is justified if the energy density inside is constant (in the floating site model of [7.5.7](/7.5.7), if the surface tension $T = kN$ varies through the site density $k$ at constant $N$). Because tissue flows are slow and very viscous, inertia is negligible ([7.5.8](/7.5.8)), and the flow obeys the Stokes equations.

**Formula 9.5.1 (Axisymmetric Stokes Flow in a Sphere Driven by Surface Tension)** Let $\theta$ be the polar angle measured from the vegetal pole, and let the surface tension be expanded in **Legendre polynomials** ([2.5.5](/2.5.5)),

$$
T(\theta) = \sum_{n \ge 0} A_n P_n(\cos\theta).
\tag{9.1}
$$
Inside the unit sphere the velocity $\boldsymbol{u}$ and pressure $p$ satisfy $\nabla p = \nabla^2\boldsymbol{u}$ and $\nabla\cdot\boldsymbol{u} = 0$. In terms of the Stokes **stream function** $\psi$, $u_r = \psi_\theta/(r^2\sin\theta)$ and $u_\theta = -\psi_r/(r\sin\theta)$, and $\psi$ satisfies $E^2E^2\psi = 0$ with $E^2 = \partial_r^2 + (\sin\theta/r^2)\,\partial_\theta(\sin^{-1}\theta\,\partial_\theta)$. The solution regular at the centre is

$$
\psi = \sum_{n\ge1} \sin\theta\,\frac{\mathrm{d}P_n(\cos\theta)}{\mathrm{d}\theta}\,\bigl(B_n r^{n+3} + C_n r^{n+1}\bigr).
\tag{9.2}
$$
At the surface $r = 1$ the normal stress balances the Laplace pressure of the tension and the tangential stress balances its gradient:

$$
-p + 2\frac{\partial u_r}{\partial r} = -2T, \qquad r\frac{\partial}{\partial r}\left(\frac{u_\theta}{r}\right) + \frac1r\frac{\partial u_r}{\partial\theta} = \frac{\partial T}{\partial\theta}.
\tag{9.3}
$$

The second condition is a Marangoni stress: the surface is pulled towards regions of higher tension. Projecting (9.3) on $P_n$ and on $\mathrm{d}P_n/\mathrm{d}\theta$ gives two linear equations for $B_n$ and $C_n$ for each $n$,

$$
-2A_n = (n+1)(4n+6)B_n - 2n(n+1)\bigl[(n+1)B_n + (n-1)C_n\bigr],
\qquad
-A_n = n(n+3)B_n + (n+1)(n-2)C_n + n(n+1)(B_n + C_n).
$$

**Proposition 9.5.1 (Surface Velocities of the First Modes)** The solution of Formula 9.5.1 has $B_1 = -A_1/6$, with $C_1$ arbitrary; $B_2 = -\tfrac{2}{19}A_2$, $C_2 = \tfrac{13}{114}A_2$; $B_3 = -\tfrac{5}{66}A_3$, $C_3 = \tfrac{7}{88}A_3$. Choosing $C_1 = A_1/6$, so that the centre of the drop does not move, the initial surface velocity is

$$
u_r(1, \theta) = -\frac{A_2}{19}P_2(\cos\theta) - \frac{A_3}{22}P_3(\cos\theta),
\qquad
u_\theta(1, \theta) = -\frac{A_1}{3}\sin\theta + \frac{7A_2}{38}\frac{\mathrm{d}P_2}{\mathrm{d}\theta} + \frac{3A_3}{22}\frac{\mathrm{d}P_3}{\mathrm{d}\theta}.
\tag{9.4}
$$

**Proof** For $n = 1$ the two equations read $-2A_1 = 20B_1 - 8B_1 = 12B_1$ and $-A_1 = 4B_1 - 2C_1 + 2(B_1 + C_1) = 6B_1$, consistent, with $B_1 = -A_1/6$ and $C_1$ free (a uniform translation along the axis). For $n = 2$: $-2A_2 = 42B_2 - 12(3B_2 + C_2) = 6B_2 - 12C_2$ and $-A_2 = 10B_2 + 6(B_2 + C_2) = 16B_2 + 6C_2$; solving, $C_2 = \tfrac{13}{114}A_2$ and $B_2 = -\tfrac{2}{19}A_2$. For $n = 3$: $-2A_3 = 72B_3 - 24(4B_3 + 2C_3)$, i.e. $A_3 = 12B_3 + 24C_3$, and $-A_3 = 18B_3 + 4C_3 + 12(B_3 + C_3) = 30B_3 + 16C_3$; hence $42B_3 = -40C_3$, $C_3 = \tfrac{7}{88}A_3$, $B_3 = -\tfrac{5}{66}A_3$. From (9.2), $u_r(1, \theta) = -\sum n(n+1)(B_n + C_n)P_n$, which gives $-\tfrac{1}{19}A_2$ for $n = 2$, $-12(-\tfrac{5}{66} + \tfrac{7}{88})A_3 = -\tfrac{1}{22}A_3$ for $n = 3$, and for $n = 1$, $-2(B_1 + C_1)A_1 = 0$ with the chosen $C_1$. The tangential components follow from $u_\theta = -\psi_r/\sin\theta$ at $r = 1$, $-[(n+3)B_n + (n+1)C_n]\,\mathrm{d}P_n/\mathrm{d}\theta$. $\square$

The three modes have distinct effects (figure below).

- $P_1$ alone: the motion is purely tangential, with the surface streaming from the animal towards the vegetal pole ($u_\theta = -\tfrac13A_1\sin\theta$, towards smaller $\theta$, for $A_1 > 0$), and the shape does not change. This is the observed streaming of the surface cells towards the blastopore.
- $P_2$: symmetric in $\cos\theta$; it produces dimpling at both poles. It does not have the symmetry of gastrulation.
- $P_3$: invagination at the vegetal pole only ($u_r(1, 0) = -A_3/22 < 0$ for $A_3 > 0$), with bulging near the **animal pole**: a gastrulation mode.

The profile $T = A_1P_1 + A_3P_3$ decreases monotonically from the vegetal to the animal pole, as the cell affinities require, only if $-A_1/6 \le A_3 \le 2A_1/3$ (the derivative $-\sin\theta\,[A_1 + \tfrac32A_3(5\cos^2\theta - 1)]$ must not change sign). Within this range, a $P_3$ component of either moderate sign is allowed, and a positive one makes the vegetal pole invaginate. When $A_2$ and $A_3$ are comparable, the radial velocities of the $P_2$ and $P_3$ modes are of similar size ($1/19$ against $1/22$ of the amplitude): the gastrulation mode does not dominate by itself, and the question is how a $P_3$ component could arise from a profile that is initially mostly $P_1$, taken up in 9.5.5.

![The amphibian blastula as a Stokes drop driven by its surface tension (Formula 9.5.1, Proposition 9.5.1). A: tension profiles, θ measured from the vegetal pole. B–D: streamlines of the initial flow (contours of the stream function), arrows for the surface velocity, and the boundary after a short time (dashed, displacement exaggerated). B: P1 alone: the surface streams towards the vegetal pole and the shape does not change. C: P1 + P2: both poles dimple. D: P1 + P3: only the vegetal pole invaginates, the gastrulation mode. E: the hollow blastula (Formula 9.5.2): the coefficient of the tangential surface velocity for an outer tension b cos θ and an inner tension c cos θ on the blastocoel wall of radius a; streaming towards the vegetal pole persists for inner tensions of opposite sign down to c ≈ −(2 + 3a⁵)b/5a³](./plots/amphibian-stokes-modes.py)

### 9.5.4. The Blastocoel and the Reversal of Force at the Blastopore

The solid sphere ignores the blastocoel and the large endodermal mass that partly fills the interior. A better idealization is a spherical shell $a < r < 1$ whose surfaces of constant cell type lie on cones $\theta = \mathrm{const}$, with tension $T_1(\theta)$ on the outer surface and $T_0(\theta)$ on the inner one, facing the blastocoel. The layers of constant cell type are then ribbons around the axis under tension, which can be represented by a volume potential $\phi(\theta)$ and a body force $\boldsymbol{f} = -\nabla\phi\,\nabla\cdot(\nabla\phi/\lvert\nabla\phi\rvert) = -\lvert\phi'\rvert\cot\theta\,\boldsymbol{e}_\theta/r^2$; the stream function then satisfies $E^2E^2\psi = r^{-2}\lvert\phi'\rvert\cos\theta$, whose solution is $\psi = r^2F(\theta) + Q\cos\theta + \psi_{\mathrm{h}}$, with $F$ obtained from $\phi$ by quadrature, $\psi_{\mathrm{h}}$ the general homogeneous solution (now including the terms $r^{2-n}$ and $r^{-n}$, allowed because the origin is excluded), and $Q\cos\theta$ the stream function of a point sink, which allows the blastocoel to change volume. The constant terms of the boundary conditions relate $Q$ to the blastocoel pressure $p_0$: either $p_0$ is given and fixes the rate of change of the cavity volume, or the volume is held fixed and the conditions determine $p_0$.

**Formula 9.5.2 (Streaming of a Hollow Blastula)** For the first mode only and no volume potential, with outer tension $b\cos\theta$ on $r = 1$ and inner tension $c\cos\theta$ on $r = a$ (the inner boundary conditions are $\sigma_{rr} = 2T_0/a - p_0$ and $\sigma_{r\theta} = -a^{-1}\partial_\theta T_0$, because the fluid lies outside that surface), the coefficients are $B_1 = -(b + ca^3)/[6(1 - a^5)]$, $E_1 = a^3(c + ba^2)/[6(1 - a^5)]$, $D_1 = 0$, and the tangential velocity of the outer surface is

$$
u_\theta(1, \theta) = -\frac{(2 + 3a^5)\,b + 5a^3c}{6(1 - a^5)}\,\sin\theta.
\tag{9.5}
$$

For $a \to 0$ this reduces to $-\tfrac13 b\sin\theta$, the solid sphere. Streaming towards the vegetal pole persists as long as $(2 + 3a^5)b + 5a^3c > 0$, that is, even for an inner tension of the opposite sign, provided it is not too large. Such a negative $c$ is expected near the blastopore. In the floating site model with constant $k$ and variable $N$, if C engulfs B and B engulfs A, then $T_{AC} \ge T_{BC}$; with A the endoderm, the tension on the internal surface near the dorsal lip, where endoderm and mesoderm meet the blastocoel, points the opposite way to that on the external surface. The force on the involuting cells thus reverses as they pass round the lip, which is what is needed to carry them inside and along the blastocoel roof.

### 9.5.5. Gastrulation as an Instability

The problems above start from a layering that is not static; they are not instabilities of an equilibrium. One can enlarge the model so that the movement becomes part of an unstable system in two ways.

A surfactant that diffuses and is conserved on the surface couples the surface tension to the flow. Greenspan showed that a fluid sphere with uniform surfactant becomes unstable when the surfactant diffuses slowly enough and the tension increases with its concentration; the second mode to be excited is $P_2$, which produces a furrow at the equator: a mechanical model of cell **cleavage**, treated in [7.5.8](/7.5.8) together with its modern counterpart, the cortical flow towards the equatorial RhoA zone. Since linear theory allows either sign, the same mode could dimple both poles instead; neither has the symmetry of gastrulation.

Alternatively, the surface tension could follow a **morphogen** whose pattern arises by a diffusive instability ([7.5.12](/7.5.12)). Near the onset of a Turing instability on a spherical shell of radius $R$, the morphogen obeys $\partial_t m = \mathcal{F}(-\nabla^2)m$, with $\mathcal{F}$ having a single, slightly positive maximum at $-\nabla^2 = k_c^2$. The eigenfunctions of $-\nabla^2$ on the sphere are the **spherical harmonics** $P_n^m$ with eigenvalues $n(n+1)/R^2$, so mode $n$ becomes unstable when $n(n+1) \approx R^2k_c^2$. As the shell grows, $P_1$ is excited first, and if the morphogen raises the surface tension, this instability can initiate gastrulation as interpreted above. Turing's last, unpublished work studied exactly such patterns on spheres.

But the morphogen and the flow are not coupled in the linear theory, and the creation of the $P_3$ gastrulation mode is nonlinear. Suppose that the surface tension is carried with the cells, $\partial_tT + u_\theta\,\partial_\theta T = 0$. With the streaming $u_\theta = -\sin\theta$ of a $P_1$ profile, the advection generates $P_2$, $P_3$ and higher modes, $P_3$ with the right sign, but only algebraically. If, more realistically, the streaming continues to follow the tension gradient, $u_\theta = k\,\partial_\theta T$ with $k > 0$, the tension obeys

$$
\frac{\partial T}{\partial t} + k\left(\frac{\partial T}{\partial\theta}\right)^2 = 0,
\tag{9.6}
$$
whose linearization about a uniform state is trivial ($\partial_tT = 0$) but whose nonlinear behaviour is not.

**Proposition 9.5.2 (Finite-Time Steepening of the Tension)** Let $T$ satisfy (9.6) with a smooth initial profile $T_0(\theta)$ having a maximum at $\theta = 0$ with $T_0''(0) = -A < 0$. Then the slope $g = 2k\,\partial_\theta T$ satisfies the inviscid **Burgers' equation** $g_t + gg_\theta = 0$, and $\partial_\theta^2T$ at the maximum becomes infinite at time $t^* = 1/(2kA)$.

**Proof** Differentiating (9.6) with respect to $\theta$ gives $\partial_t(T_\theta) + 2kT_\theta T_{\theta\theta} = 0$, i.e. $g_t + gg_\theta = 0$. By the **method of characteristics** ([2.5.2](/2.5.2)), $g$ is constant along $\theta = \theta_0 + g_0(\theta_0)t$, and $g_\theta = g_0'(\theta_0)/(1 + g_0'(\theta_0)t)$. At the maximum $g_0' = 2kT_0''(0) = -2kA$, so $g_\theta$, and with it $T_{\theta\theta} = g_\theta/(2k)$, diverges at $t^* = 1/(2kA)$, when neighbouring characteristics first cross: a **shock wave** of $g$, that is a corner of $T$. $\square$

With the vegetal pole at the maximum of $T$, the characteristics converge on it and the tension develops a cusp there in finite time (figure below): a localized concentration of tension, and so of inward movement, at the vegetal pole grows from a smooth, linearly neutral initial state, a "catastrophic" change in the sense of [7.5.10](/7.5.10). The model is a caricature, but it shows how a nonlinear advection of cell properties can localize the movement without a localized initial cue.

![Finite-time steepening of the surface tension (Proposition 9.5.2), with T = cos θ at t = 0 and k = 1. A: characteristics converge on the vegetal pole and first cross at t* = 1/(2k). B: the tension profile sharpens into a cusp at the vegetal pole. C: the curvature at the pole, −T_θθ = 1/(1 − 2kt), diverges at t*](./plots/tension-shock.py)

### 9.5.6. The Strain Field and Bottle Cells

A fluid model hides the fact that cells need not move far. The movements can instead be read as a local strain field, which says how cells must change shape. Two two-dimensional flows tangential at the surface line $y = 0$, with stream function $\psi$ ($u = \psi_y$, $v = -\psi_x$) and stress tensor $\sigma = \begin{bmatrix} 2u_x & u_y + v_x \\ u_y + v_x & 2v_y\end{bmatrix}$, represent the two typical regions:

$$
\text{(a) } \psi = -\tfrac12 x(x^2 + y^2),\quad -\sigma = \begin{bmatrix}1 + 2y & x\\ x & -(1 + 2y)\end{bmatrix};
\qquad
\text{(b) } \psi = \tfrac12 y^2,\quad -\sigma = \begin{bmatrix}0 & 1\\ 1 & 0\end{bmatrix}.
$$

Flow (a), near the site of invagination, stretches material perpendicularly to the surface and compresses it along the surface: a square element just below the surface becomes tall and narrow, with its narrowest part at the surface. That is the shape of a bottle cell, which is thus what the cells must do to produce the local flow of the gastrulation mode, or what they would be made to do by it. Flow (b), a simple shear, is typical of the region of surface streaming, where cells are stretched along the direction of streaming, as observed. Whether the bottle cells cause the movement or follow it cannot be decided from shapes alone; experiments decide: removing the bottle cells after they form does not stop involution, although they are needed to initiate the groove, and vegetal rotation and convergent extension supply most of the later force.

### 9.5.7. A Vertex Model of Invagination

The same questions can be asked at the level of cells. The variational principle of [7.5.8](/7.5.8) gives the dynamics: the motion maximizes the rate of decrease of the tension energy $T$ at a given rate of dissipation $\Phi$, which leads to $\delta(\dot T + \tfrac12\Phi) = 0$ for all variations of the velocities.

**Proposition 9.5.3 (Gradient Dynamics from the Dissipation Principle)** If the dissipation is $\Phi = \sum_k \eta\,\lvert\dot{\boldsymbol{x}}_k\rvert^2$ for points $\boldsymbol{x}_k$ (the vertices of cells moving against a uniform friction), the principle $\delta(\dot T + \tfrac12\Phi) = 0$ gives $\eta\,\dot{\boldsymbol{x}}_k = -\partial T/\partial\boldsymbol{x}_k$.

**Proof** $\dot T = \sum_k(\partial T/\partial\boldsymbol{x}_k)\cdot\dot{\boldsymbol{x}}_k$. Varying the velocity $\dot{\boldsymbol{x}}_k$ gives $\partial T/\partial\boldsymbol{x}_k + \eta\,\dot{\boldsymbol{x}}_k = 0$. $\square$

Two examples follow from this principle.

**Example 9.5.1 (A Columnar Cell Spreading on a Substrate)** Model a two-dimensional cell as a rectangle of fixed area $A$ on a substrate between $x_1$ and $x_2$, with membrane tension $\tau$ per unit length on its free surfaces and an energy $\sigma$ per unit length of contact with the substrate: $T = \tau\left(x_2 - x_1 + 2A/(x_2 - x_1)\right) + \sigma(x_2 - x_1)$, the term $2A/(x_2 - x_1)$ being the two side walls of height $h = A/(x_2 - x_1)$. The equilibrium width is $x_2 - x_1 = (2A\tau/(\tau + \sigma))^{1/2}$ and the height $h = ((\tau + \sigma)A/2\tau)^{1/2}$: adhesion ($\sigma < 0$) makes the cell spread and flatten, tension makes it columnar. For the dynamics, interpolate the velocity linearly inside the cell, $u_x = [u_1(x_2 - x) + u_2(x - x_1)]/(x_2 - x_1)$, $u_y = -(u_2 - u_1)\,y/(x_2 - x_1)$, an incompressible and irrotational flow, whose viscous dissipation is $\Phi = 2\eta A(u_2 - u_1)^2/(x_2 - x_1)^2$. The principle gives $u_2 = -u_1$, and for a symmetric cell ($x_1 = -x_2$)

$$
\frac{\mathrm{d}x_2}{\mathrm{d}t} = \frac{2\tau A - 4(\tau + \sigma)x_2^2}{8\eta A},
\qquad
x_2(t) = \left(\frac{\tau A}{2(\tau + \sigma)}\right)^{1/2}\tanh\left(\frac{\sqrt{2\tau(\tau+\sigma)}}{4\eta\sqrt{A}}\,t + C\right),
$$
so the half-width relaxes to its equilibrium value $(\tau A/2(\tau + \sigma))^{1/2}$ on a time scale of order $\eta\sqrt{A}/\sqrt{\tau(\tau + \sigma)}$.

For a ring of epithelial cells, a two-dimensional section of a blastula wall, each cell $i$ is a wedge of fixed area with an outer (apical) side, an inner (basal) side and lateral sides, with their tensions, and the dissipation includes friction against the substrate and the internal viscosity of the cells. Percus and Childress found numerically that enhancing the outer tension of a group of cells makes the ring invaginate, until neighbouring cells collide (the model has no exclusion between cells). The figure below shows the same result in a vertex model: each of 40 cells is a quadrilateral whose apical and basal edges are contractile springs with preferred lengths, whose lateral edges carry a tension, and whose area is elastic; the blastocoel resists changes of its area weakly; the vertices move by the gradient dynamics of Proposition 9.5.3. Shortening the preferred apical length of five cells at the vegetal pole, as apical constriction does, makes them wedge-shaped and dimples the outer surface, forming a pit about one cell height deep within the time the constriction takes. The model shows that apical constriction of a small group of cells suffices to start an invagination; it also shows its limits: the pit stays shallow, and the deep invagination of real embryos needs further forces, such as the swelling of the hyaline layer in the sea urchin, vegetal rotation in the frog, or basal relaxation and tissue-scale tension in the *Drosophila* furrow.

![Invagination of an epithelial ring by apical constriction (vertex model with the gradient dynamics of Proposition 9.5.3). A: snapshots; the five constricting cells (red) at the vegetal pole become wedges, and the outer surface dimples into a pit. B: depth of the pit (in cell heights) and apical width of the constricting cells over time](./plots/epithelial-ring.py)

### 9.5.8. Assessment

The continuum model captures the direction of surface streaming, the possibility of localized invagination at the vegetal pole, the reversal of force at the blastopore, and the shape of bottle cells, from the single assumption that tissue tension varies with cell type. It does not include active intercalation, which in *Xenopus* is now known to provide much of the force for convergent extension and for closing the blastopore; nor vegetal rotation; nor the fact that the involuting mesoderm crawls on a matrix rather than flowing as a passive fluid. Its value is to show which features of gastrulation follow from the generic mechanics of a viscous, adhesive tissue, and which require specific cell behaviours. Measurements of **tissue surface tension** and viscosity in *Xenopus* explants (viscosities of order $10^4$–$10^6\,\mathrm{Pa\,s}$, depending on tissue and method) now provide the parameters that a quantitative test of the premise needs (Question 10).

## 9.6. Fish

The zebrafish blastoderm sits on top of a large yolk cell ([7.5.5](/7.5.5)). Gastrulation starts with **epiboly**: at about 4 h after fertilization the yolk cell bulges up into the blastoderm (the dome stage), and the blastoderm thins and spreads over the yolk, covering half of it at about 5.3 h (50 % epiboly) and closing over the vegetal pole at about 10 h. Three tissues contribute: the yolk syncytial layer (YSL), which spreads ahead of the blastoderm under the margin; the enveloping layer (EVL), attached to the YSL at its margin by **tight junctions**; and the deep cells, which follow. The main force comes from the yolk cell: an actomyosin ring in the external YSL, just ahead of the EVL margin, contracts and pulls the EVL towards the vegetal pole, both by constriction around the yolk (like a purse string, once past the equator) and by a cortical flow towards the ring that generates friction and tension (flow-friction). Microtubules in the yolk cell guide the movement of the YSL nuclei. The deep cells spread by radial intercalation.

At 50 % epiboly the deep cells at the margin involute or ingress, forming a thickened ring, the germ ring, with an outer layer, the epiblast, and an inner layer, the hypoblast (here the involuted mesendoderm, not the extraembryonic tissue that has the same name in amniotes). On the dorsal side cells converge to form the embryonic shield, the zebrafish equivalent of the Spemann organizer ([7.5.16](/7.5.16)). The hypoblast and epiblast cells then converge dorsally and extend along the axis, the axial hypoblast forming the notochord and prechordal plate, the paraxial hypoblast the somites. The epiblast forms the ectoderm. Mutants lacking maternal Huluwa or nuclear β-catenin have no shield, and their lateral and ventral mesendoderm, after involuting, fails to converge dorsally and accumulates in one place, constricting the yolk ([7.5.16](/7.5.16)).

### 9.6.1. Epiboly as a Spreading Film

The resemblance of epiboly to the wetting of a solid by a liquid suggests a differential adhesion model. A layer of B cells (the blastoderm) spreads on a substrate of A cells (the yolk cell), with the interfacial tensions $T_{AO}$, $T_{BO}$ and $T_{AB}$ of [7.5.7](/7.5.7) against the medium O and each other. Because the layer is thin, lubrication theory applies: if the thickness $\ell$ is small compared with the lateral scale $L$, $\varepsilon = \ell/L \ll 1$, rescaling $z$ by $\varepsilon$, the vertical velocity by $\varepsilon$ and the pressure by $\varepsilon^{-2}$ reduces the Stokes equations at leading order to

$$
\frac{\partial p}{\partial z} = 0, \qquad \nabla_2 p = \frac{\partial^2\boldsymbol{u}}{\partial z^2}, \qquad \nabla_2\cdot\boldsymbol{u} + \frac{\partial w}{\partial z} = 0,
$$
where $\boldsymbol{u}$ is the horizontal velocity and $\nabla_2$ the horizontal gradient: the pressure penetrates the layer, the horizontal velocity is a parabola in $z$, and the vertical velocity only responds to its divergence. The general solution is $\boldsymbol{u} = \tfrac12\nabla_2p\,z^2 + \boldsymbol{F}z + \boldsymbol{G}$.

Boundary conditions close the problem. At the free surface $z = h(x, y, t)$ there is no tangential stress (no gradient of surface tension, small slope): $\partial\boldsymbol{u}/\partial z = 0$; the normal stress balances the curvature, $p = -T_{BO}\nabla_2^2h$, since the mean curvature of a nearly flat surface is $-\nabla_2^2h$. At the substrate a strict no-slip condition would prevent relative movement of the two cell types; following Greenspan, slip proportional to the shear stress is allowed, $\boldsymbol{u} = K(h)\,\partial\boldsymbol{u}/\partial z$ at $z = 0$, with $K(h) = k^2/3h$ and $k$ small. At the moving edge, with small slope and small equilibrium contact angle $\theta_0$, the edge velocity is $\boldsymbol{u}_e = k_e(\theta - \theta_0)\boldsymbol{n}_2$, $\boldsymbol{n}_2$ the outward normal of the edge; since $\theta \approx \lvert\nabla_2h\rvert$, this is $\boldsymbol{u}_e = -K_e\nabla_2h\,(1 - \theta_0/\lvert\nabla_2h\rvert)$.

**Formula 9.6.1 (Greenspan's Thin-Film Equation)** Integrating the continuity equation across the layer, with the free surface moving with the fluid, gives $\partial_th + \nabla_2\cdot(\boldsymbol{U}h) = 0$ with the mean velocity $\boldsymbol{U} = \tfrac13T_{BO}(h^2 + k^2)\nabla_2(\nabla_2^2h)$, hence

$$
\frac{\partial h}{\partial t} + \frac13 T_{BO}\,\nabla_2\cdot\bigl[(h^3 + k^2h)\,\nabla_2\nabla_2^2h\bigr] = 0,
\tag{9.7}
$$
with the edge condition $\boldsymbol{u}_e = \tfrac13T_{BO}k^2\nabla_2(\nabla_2^2h) = -K_e\nabla_2h\,(1 - \theta_0/\lvert\nabla_2h\rvert)$.

The edge equilibrium, Young's force balance $T_{AO} = T_{AB} + T_{BO}\cos\theta_0$ (**Young equation**, [6.3.19](/6.3.19)), with the tensions expressed by the adhesion energies of [7.5.7](/7.5.7), becomes $\tfrac12(1 - \cos\theta_0) \approx \theta_0^2/4 = 1 - E_{AB}/E_{BB}$: a small contact angle means that A–B adhesion nearly equals B–B adhesion, so the derivation assumes near-total **engulfment** of the A aggregate by B cells. Epiboly is wetting.

Equation (9.7) is hard to solve, but a quasi-steady approximation works well: take the profile $h_0$ to satisfy $\nabla_2\nabla_2^2h_0 = 0$ at each instant, conserving the number of cells, and move the edge by the edge condition.

**Example 9.6.1 (Spreading of a Ribbon)** For a ribbon of cells spreading in one dimension, the quasi-steady profile of unit cross-section with half-width $a$ is $h_0 = \frac{1}{2a}(1 - x^2/a^2)$, whose slope at the edge is $1/a^2$. The edge law becomes

$$
\dot a = K_e\left(\frac{1}{a^2} - \theta_0\right).
\tag{9.8}
$$
For complete wetting ($\theta_0 = 0$), $a^3 = a_0^3 + 3K_et$: the ribbon spreads as $t^{1/3}$, its edge slowing as $t^{-2/3}$. For $\theta_0 > 0$ the half-width approaches $\theta_0^{-1/2}$, the spreading stopping when the edge reaches the equilibrium angle; with $\bar a = a\theta_0^{1/2}$, separation of variables gives $-\bar a + \tfrac12\ln\lvert(1 + \bar a)/(1 - \bar a)\rvert = \theta_0^{3/2}K_et + \mathrm{const}$.

A simpler lubrication calculation shows how a gradient of tension in the substrate, rather than wetting, can move cells. For a layer of constant cell density, incompressible ($\nabla\cdot\boldsymbol{u} = 0$) and in **Stokes flow**, with no slip on the substrate and the substrate supplying a tangential traction $-\nabla T(\boldsymbol{x})$ at $z = 0$, neglecting pressure, $\boldsymbol{v} = -z\nabla T/\eta$ and

$$
\dot h = \frac{1}{2\eta}h^2\nabla^2T, \qquad h(\boldsymbol{x}, t) = \frac{h(\boldsymbol{x}, 0)}{1 - \dfrac{t}{2\eta}h(\boldsymbol{x}, 0)\nabla^2T(\boldsymbol{x})}.
\tag{9.9}
$$
Cells accumulate where $\nabla^2T > 0$, in a trough of tension, as anticipated; the solution blows up in finite time, which marks the end of the thin-film approximation, not a physical singularity.

![Epiboly as the spreading of a thin film. A: quasi-steady profiles of a spreading ribbon for complete wetting (Example 9.6.1). B: the half-width a(t) from the edge law (9.8): for θ0 = 0 it is exactly (a0³ + 3K_e t)^(1/3) (dotted); for θ0 > 0 it approaches θ0^(−1/2) (dashed). C: the lubrication solution (9.9) for a layer driven by a trough of substrate tension (T = −exp(−x²), dashed, h0 = 0.2, η = 1): cells accumulate at the trough, and the approximation fails at t = 5](./plots/epiboly-thin-film.py)

The film model treats the blastoderm as a passive wetting fluid, while the real driving force comes largely from the **contractile ring** of the yolk cell, pulling the EVL margin; the model is better seen as a statement about how a sheet of adherent cells spreads under a pull at its edge, given its viscosity and its adhesion to the substrate. In both pictures the spreading speed is set by a balance between a force at the edge and viscous resistance in the sheet, and in both it slows as the sheet thins; but in zebrafish the margin speeds up after the equator, when the ring constricts around the yolk, which only the active model explains.

## 9.7. Birds

The chick blastoderm at laying is a disc of epiblast over the subgerminal cavity, with hypoblast beneath it and Koller's sickle at the posterior margin ([7.5.5](/7.5.5)). Gastrulation is organized around the primitive streak.

**Definition 9.7.1 (Primitive Streak, Hensen's Node)** The **primitive streak** is a thickening of the epiblast along the future anterior–posterior midline of amniote embryos, through which epiblast cells ingress to form the mesoderm and endoderm. At its anterior end lies **Hensen's node** (the node in mammals), a thickened knot of cells with organizer activity; a depression along the streak, the primitive groove, and one in the node, the primitive pit, are the routes by which cells pass inside.

The streak forms from cells in the posterior marginal zone and Koller's sickle, by a large-scale counter-rotating movement of the epiblast, the "polonaise", in which cells on both sides flow towards the posterior midline and then forwards along it. These flows are generated by the epiblast cells themselves: myosin-dependent, directionally organized cell intercalations in a crescent of the posterior epiblast pull tissue into the midline, as live imaging of whole embryos has shown. Within about 16 h of incubation the streak extends to 60–75 % of the length of the area pellucida (figure below). Its formation requires Vg1 and Wnt8c from the posterior marginal zone and Nodal in the epiblast; the overlying hypoblast secretes the Nodal antagonist Cerberus, which prevents the formation of additional streaks, and only when the hypoblast is displaced anteriorly can the streak form ([7.5.16](/7.5.16)). Removing the hypoblast causes several streaks to form; its position, rather than the position of the epiblast cells, determines where the streak goes.

The streak defines the axes: the node is anterior, the end of the streak posterior; the side on which the epiblast is facing upwards is dorsal. Cells ingress through the streak by an epithelial–mesenchymal transition. The first to pass through the node move anteriorly and form the foregut endoderm, the prechordal plate and the head mesoderm; as they enter the lower layer, they displace the hypoblast forwards to the margin of the area pellucida, where it forms the germinal crescent, in which the primordial germ cells lie before entering the blood ([7.5.27](/7.5.27)). Later cells passing through the node form the notochord; cells passing through the streak at progressively more posterior levels and later times form somites, **intermediate mesoderm**, lateral plate and extraembryonic mesoderm. Cells from the anterior streak move laterally only a short distance and form paraxial mesoderm by convergent extension, while cells from the posterior streak migrate far laterally first; some ingressing cells join the lower layer and form the definitive endoderm. The FGF signalling of the streak attracts some mesoderm cells and repels others, a chemotactic guidance treated in [7.5.13](/7.5.13). Meanwhile the epiblast remaining on the surface, the prospective ectoderm, spreads by epiboly over the yolk, its margin crawling on the inner surface of the vitelline membrane, a process that takes about four days.

After the streak has reached its full length, the node moves posteriorly (regression), laying down the notochord in its wake; the somites form on each side, and head structures develop anteriorly while the posterior is still gastrulating: amniote embryos develop in an anterior-to-posterior wave. The streak finally becomes the tail bud.

![Gastrulation in the chick. A: the blastoderm seen from above at the definitive-streak stage (anterior up): the primitive streak runs from the posterior margin of the area pellucida to Hensen's node, and epiblast cells converge on it (arrows). B: the fate of ingressing cells depends on the level of the streak through which they pass, and on the time (schematic). C: regression of the node, which lays down the notochord as somites form on both sides](./plots/chick-streak.py)

## 9.8. Mammals

### 9.8.1. The Mouse Egg Cylinder

After **implantation** at E4.5 ([7.5.5](/7.5.5)), the mouse epiblast forms a cup-shaped epithelium, the egg cylinder, enclosing the proamniotic cavity. Above it (proximally) the polar **trophectoderm** forms the extraembryonic ectoderm and the ectoplacental cone, which invades the uterus; the primitive endoderm forms the visceral endoderm, which covers the egg cylinder, and the parietal endoderm, which lines the mural trophectoderm. By E5.5 a group of visceral endoderm cells at the distal tip (the distal visceral endoderm) migrates to one side, which becomes anterior (the anterior visceral endoderm, AVE); it secretes the Nodal antagonists Lefty1 and Cerberus-like and the Wnt antagonist Dkk1, and so restricts Nodal and Wnt3 signalling, and hence primitive streak formation, to the opposite, posterior side ([7.5.16](/7.5.16)). At E6.5 the streak forms there and extends to the distal tip by E7.5, where the node lies.

Cells ingress through the streak by an epithelial–mesenchymal transition, which requires the transcription factor Snail and loss of E-cadherin; they move laterally and anteriorly between the epiblast and the visceral endoderm as a mesoderm layer. Some ingressing cells enter the visceral endoderm and become definitive endoderm; contrary to the earlier view that they displace it entirely, visceral endoderm cells are intercalated into the gut endoderm and contribute to it. Cells passing through the node form the notochord, and the somites form behind it. Because the mouse egg cylinder is cup-shaped, the germ layers are "inside out" relative to other mammals: the endoderm is on the outside. Between E8.5 and E9.0 the embryo turns, rotating around its axis, so that it lies inside its membranes with the endoderm inside and the ectoderm outside, as in other vertebrates; by then it is surrounded by the amnion and the visceral yolk sac.

### 9.8.2. Human

The human **blastocyst** begins to implant on day 6–7 and is entirely embedded in the endometrium by day 10. The trophoblast differentiates into an inner cytotrophoblast, whose cells divide, and an outer syncytiotrophoblast, formed by cell fusion, which invades the maternal tissue, erodes the maternal capillaries and opens lacunae filled with maternal blood. The **inner cell mass** meanwhile forms a bilaminar disc: the epiblast, facing the future amniotic cavity, and the hypoblast, facing the blastocoel (equivalent to the primitive endoderm of the mouse). Spaces within the epiblast merge into the amniotic cavity, lined on its roof by amnion; hypoblast cells spread over the inner surface of the trophoblast, forming the primary yolk sac, which is later pinched off and replaced by the smaller secondary yolk sac. Extraembryonic mesoderm, from the hypoblast or the epiblast, fills the space between the yolk sac and the trophoblast and then splits to form the chorionic cavity; the embryo hangs in it by the connecting stalk, the future umbilical cord.

Gastrulation starts with the appearance of the primitive streak at the posterior end of the epiblast at about day 14–15. Epiblast cells ingress through the streak; the first displace the hypoblast and form the definitive endoderm; the next spread between epiblast and endoderm as mesoderm; the epiblast that remains forms the ectoderm. The disc becomes trilaminar by about day 16, and gastrulation is complete by the end of the third week, when the neural plate forms. The appearance of the streak is the basis of the 14-day rule, which limits the culture of human embryos in research to 14 days or the formation of the streak, whichever comes first; the International Society for Stem Cell Research relaxed its recommendation in 2021 to allow, under strict review, proposals to go beyond it, while many countries keep it in law.

Because human gastrulation is inaccessible, primate models have become important. Cynomolgus monkey blastocysts have been cultured in vitro to day 20 and beyond: they implant on the dish, form the bilaminar disc, the amniotic cavity, the yolk sac and the primitive streak, and begin to form the three germ layers, with gene expression changes similar to those of the human embryos that are available. Such cultures, together with stem-cell models of the embryo ([7.5.36](/7.5.36)), showed, for example, that in primates the amnion forms early from the epiblast and that primordial germ cells appear first in the amnion ([7.5.27](/7.5.27)).

### 9.8.3. Comparing the Vertebrates

The vertebrate gastrulae look very different, but their fate maps are topologically similar: in each, the prospective endoderm and mesoderm lie near the site of internalization (vegetal hemisphere and marginal zone in the frog; margin of the blastoderm in fish; the posterior epiblast that will enter the streak in amniotes), and the organizer lies at its dorsal or anterior end (dorsal lip, shield, Hensen's node, node). The blastopore of the frog, the germ ring of the fish and the primitive streak of amniotes are equivalent: if the streak is imagined as a blastopore whose lips have been brought together along the midline in a flat, yolk-rich embryo, the movements correspond. The differences are mostly consequences of yolk: in the frog the vegetal yolky cells are moved inside; in fish and birds the yolk is too large and is enveloped by epiboly while the embryo forms on its surface; mammals, which lost their yolk but kept the flat-disc geometry of their reptilian ancestors, gastrulate through a streak.

## 9.9. Extraembryonic Membranes and the Placenta

Amniotes (reptiles, birds and mammals) develop in a fluid environment of their own, made by tissues that do not form part of the embryo.

**Definition 9.9.1 (Extraembryonic Membranes)** The **extraembryonic membranes** of amniotes are four sheets of tissue formed outside the embryo: the **amnion**, which encloses the embryo in a fluid-filled cavity; the **chorion**, the outermost membrane, which mediates gas exchange (in mammals, together with the trophoblast, it forms the fetal part of the placenta); the **allantois**, an outgrowth of the hindgut that stores waste and, fused with the chorion, forms the vascularized chorioallantoic membrane (in mammals, the umbilical vessels); and the **yolk sac**, which surrounds the yolk and is the first site of blood formation. The amnion and chorion consist of ectoderm (in mammals, trophoblast for the chorion) and somatic mesoderm; the yolk sac and allantois of endoderm and splanchnic mesoderm.

In the bird (figure below), the amnion and chorion form from folds of the extraembryonic ectoderm and mesoderm that rise around the embryo and fuse above it; the allantois spreads under the shell, where its vessels exchange gases through the pores of the shell, and stores nitrogenous waste as uric acid; the yolk sac grows over the yolk and transfers nutrients to the embryo through its vessels.

**Definition 9.9.2 (Placenta)** The **placenta** is an organ formed by the apposition of fetal extraembryonic tissues and maternal tissues of the uterus, through which the fetus exchanges gases, nutrients and waste with the mother and which secretes hormones that maintain the pregnancy.

The human placenta is haemochorial: the syncytiotrophoblast has eroded the maternal vessels, so maternal blood bathes the chorionic villi directly. From about the fourth week, the villi consist of a core of extraembryonic mesoderm with fetal capillaries, covered by cytotrophoblast and syncytiotrophoblast. Maternal blood enters the intervillous space in jets from the spiral arteries of the endometrium, which the invading trophoblast has remodelled into wide, low-resistance vessels, and drains through endometrial veins. Fetal blood arrives through the two umbilical arteries, carrying deoxygenated blood from the fetus, flows through the capillaries of the villi, and returns oxygenated through the umbilical vein. The fetal and maternal circulations do not connect: no fetal vessel opens into the intervillous space, and exchange occurs across the villous membrane, a few micrometres thick at term, by diffusion (oxygen, carbon dioxide), facilitated diffusion (glucose), active transport (amino acids, calcium) and receptor-mediated transcytosis (IgG antibodies). The syncytiotrophoblast secretes human chorionic gonadotropin, which maintains the corpus luteum and is the basis of pregnancy tests, and later progesterone. Failure of trophoblast invasion and spiral artery remodelling underlies preeclampsia and fetal growth restriction. Mouse and human placentas differ in structure (the mouse placenta has a labyrinth of trophoblast and fetal vessels), which limits the mouse as a model for human placental disease.

![Extraembryonic membranes and the placenta. A: a bird egg at about day 5: the embryo in the amnion; the chorion under the shell; the allantois, an outgrowth of the hindgut, spreading under the chorion; the yolk sac with its vessels over the yolk; albumen in the remaining space. B: a chorionic villus of the human placenta: maternal blood enters the intervillous space from spiral arteries and drains through endometrial veins; fetal blood arrives through the umbilical arteries (deoxygenated, blue) and returns through the umbilical vein (oxygenated, red) in capillaries inside the villi, covered by syncytiotrophoblast. The two circulations do not mix; oxygen and nutrients cross the villous membrane into fetal blood, carbon dioxide and waste the other way](./plots/extraembryonic-placenta.py)

## 9.10. Inversion in Volvox and Sponges

Movements resembling gastrulation occur in organisms with very simple patterns. The green alga *Volvox carteri* is a sphere of about 2000 biflagellate somatic cells with 16 large reproductive cells. Each reproductive cell divides into an embryo, a hollow sphere of cells whose flagellar ends point inwards; to become motile, the embryo turns itself inside out through an opening, the phialopore. The inversion is driven by a wave of cell shape changes: the cells near the opening become spindle- and then flask-shaped, with narrow tips at the outer surface, and move their cytoplasmic bridges, which bends the sheet backwards; the wave spreads around the sphere until it is everted, and the new colony later escapes from its mother. Mechanical models of inversion, in which the active bending of the cell sheet and its stretching are the only ingredients, reproduce the observed shapes, a counterpart of 9.5.7 in a sheet without any **cell migration**. Some sponges show a similar inversion: in calcareous sponges such as *Sycon*, the embryo forms with its flagella facing the inside and inverts through an opening to bring them to the surface of the larva (the amphiblastula). The comparison shows how much of the mechanics of epithelial bending is generic; it is not a historical sequence, since *Volvox* is an alga and its inversion evolved independently of the movements of animal embryos.

## Summary

| Topic | Main points |
|---|---|
| Germ layers (Definitions 9.1.1–9.1.2) | ectoderm, mesoderm, endoderm and their derivatives; blastopore becomes mouth (protostomes) or anus (deuterostomes) |
| Movements (Definition 9.2.1) | invagination, involution, epiboly, ingression, delamination, convergent extension; engines: apical constriction, intercalation (PCP), migration on fibronectin, adhesion changes and EMT, external forces |
| Sea urchin (9.3) | primary mesenchyme ingression by EMT; primary invagination by apical constriction and swelling of the hyaline layer; convergent extension and secondary mesenchyme filopodia complete the archenteron |
| *Drosophila* (9.4) | ventral furrow by pulsed, ratcheted apical constriction (Twist, Snail, Fog); germ-band extension by planar-polarized myosin and T1 transitions set by pair-rule genes and Toll receptors |
| Amphibians (9.5) | bottle cells and blastopore (Definition 9.5.1), vegetal rotation, involution on fibronectin, epiboly by radial intercalation, convergent extension |
| Stokes drop (Formula 9.5.1, Proposition 9.5.1) | P1 tension: streaming to the vegetal pole; P2: both poles; P3: vegetal invagination (gastrulation mode), $u_r = -A_3P_3/22$; monotonic for $-A_1/6 \le A_3 \le 2A_1/3$ |
| Hollow blastula (Formula 9.5.2) | streaming coefficient $[(2 + 3a^5)b + 5a^3c]/[6(1 - a^5)]$; reversal of force near the blastopore |
| Instability (Proposition 9.5.2) | Turing modes on a sphere, $n(n+1) \approx R^2k_c^2$; advected tension $T_t + kT_\theta^2 = 0$ steepens into a cusp at $t^* = 1/(2kA)$ |
| Cell level (9.5.6–9.5.7) | strain field of invagination makes bottle cells; dissipation principle gives gradient dynamics (Proposition 9.5.3); columnar cell (Example 9.5.1); vertex model: apical constriction starts a shallow invagination |
| Fish (9.6) | epiboly driven by the YSL actomyosin ring; germ ring and shield; thin-film equation (Formula 9.6.1), edge law $a \propto t^{1/3}$ (Example 9.6.1), accretion in a tension trough (9.9) |
| Amniotes (9.7–9.8) | primitive streak and Hensen's node (Definition 9.7.1), polonaise flows, fate by level and time of ingression, regression; mouse egg cylinder, AVE, turning; human bilaminar and trilaminar disc, 14-day rule, monkey embryo culture; common fate-map topology |
| Membranes (Definitions 9.9.1–9.9.2) | amnion, chorion, allantois, yolk sac; haemochorial human placenta, separate circulations, exchange across the villus |

## Questions

1. Classify each of the following as invagination, involution, epiboly, ingression, delamination or convergent extension: (a) primary mesenchyme entering the sea urchin blastocoel; (b) the zebrafish blastoderm covering the yolk; (c) the formation of the chick hypoblast islands; (d) the lengthening of the frog notochord; (e) the marginal zone of the frog rolling over the dorsal lip; (f) the *Drosophila* ventral furrow.

   **Answer** (a) Ingression; (b) epiboly; (c) delamination (cells leave the epiblast as small sheets attached beneath it); (d) convergent extension; (e) involution; (f) invagination (followed by an epithelial–mesenchymal transition of the internalized tube).

2. Using Proposition 9.5.1, compute the initial radial velocity at the vegetal pole, the equator and the animal pole for $T = P_1 + 0.6P_3$. Does the blastula keep its volume?

   **Answer** $u_r(1, \theta) = -\tfrac{0.6}{22}P_3(\cos\theta)$. At the vegetal pole ($P_3 = 1$): $-0.027$, inward; at the equator ($P_3(0) = 0$): $0$; at the animal pole ($P_3 = -1$): $+0.027$, outward. Since $\int_0^\pi P_3(\cos\theta)\sin\theta\,\mathrm{d}\theta = 0$, the net volume flux through the surface vanishes: the volume is conserved, as it must be for an incompressible fluid.

3. Verify the bound $A_3 \le 2A_1/3$ for a monotonically decreasing tension $T = A_1P_1 + A_3P_3$, and state what would happen to the gastrulation mode if the bound were exceeded.

   **Answer** $\mathrm{d}T/\mathrm{d}\theta = -\sin\theta\,[A_1 + A_3\tfrac{\mathrm{d}P_3}{\mathrm{d}x}]$ with $\tfrac{\mathrm{d}P_3}{\mathrm{d}x} = \tfrac32(5x^2 - 1)$, $x = \cos\theta$, which ranges from $-\tfrac32$ (at $x = 0$) to $6$ (at $x = \pm1$). Monotonic decrease requires $A_1 + A_3\tfrac32(5x^2 - 1) \ge 0$ for all $x$: for $A_3 > 0$ the binding case is $x = 0$, giving $A_3 \le \tfrac23A_1$; for $A_3 < 0$, $x = \pm1$, giving $A_3 \ge -A_1/6$. If $A_3$ exceeded $2A_1/3$, $T$ would have a minimum near the equator, implying an intermediate tissue of lower tension than the ectoderm, which contradicts the sorting order; the surface flow would converge on the equator as well, producing a ring-shaped movement rather than a vegetal invagination.

4. In the hollow-blastula model (Formula 9.5.2), find the most negative inner tension $c$ (relative to $b$) compatible with streaming towards the vegetal pole when the blastocoel radius is $a = 0.6$.

   **Answer** The condition is $(2 + 3a^5)b + 5a^3c > 0$. With $a = 0.6$, $a^3 = 0.216$, $a^5 = 0.0778$: $2 + 0.233 = 2.233$; $5a^3 = 1.08$. So $c > -2.233b/1.08 = -2.07b$. An inner tension of opposite sign up to about twice the outer one still allows vegetal streaming.

5. For Proposition 9.5.2 with $T_0 = A\cos\theta$, estimate the time $t^*$ in hours if $k$, the ratio of streaming speed to tension gradient, is such that the surface moves at $10\,\mathrm{\mu m\,min^{-1}}$ at the equator in a blastula of radius 0.6 mm, with $A$ in the same units of tension.

   **Answer** $u_\theta = kT_\theta = -kA\sin\theta$; at the equator its magnitude, in angular units, is $kA = v/R = (10\,\mathrm{\mu m/min})/(600\,\mathrm{\mu m}) = 1/60\,\mathrm{min^{-1}}$. Then $t^* = 1/(2kA) = 30\,\mathrm{min}$. The steepening would occur on the time scale of the first hour of gastrulation, consistent with the time over which the blastopore groove forms; the estimate shows only that the mechanism is fast enough, not that it operates.

6. Design an experiment to test whether bottle cells are necessary for amphibian gastrulation, and state the possible outcomes.

   **Answer** Remove the bottle cells surgically at different times after their formation (early, as the groove first appears, and later), or prevent their apical constriction locally by injecting a dominant-negative regulator of myosin or RhoA into the dorsal marginal zone precursors, and follow involution, archenteron formation and blastopore closure. If bottle cells are necessary only to initiate the groove, early removal delays or prevents involution while later removal has little effect; if they drive the whole process, involution stops after removal at any time. The observed result is the first: removed after the groove forms, they are dispensable, because vegetal rotation, involution of the marginal zone and convergent extension provide the force.

7. In the ribbon model (Example 9.6.1) with $\theta_0 = 0$ and $a_0 = 0.5$, $K_e = 1$, how long does the ribbon take to double its width, and then to double it again? What does this imply for the observed speeding-up of zebrafish epiboly after the equator?

   **Answer** $a^3 = 0.125 + 3t$. Doubling to $a = 1$: $1 = 0.125 + 3t$, $t = 0.29$. Doubling again to $a = 2$: $8 = 0.125 + 3t$, $t = 2.63$, so the second doubling takes about nine times longer: a wetting-driven film slows continually. Zebrafish epiboly speeds up after 50 % epiboly, which the passive model cannot produce; it requires the active contractile ring in the yolk cell, which constricts around the yolk once past the equator and pulls the margin.

8. Why does removing the hypoblast from a chick blastoderm produce multiple primitive streaks, and what does this tell us about where the streak normally forms?

   **Answer** The hypoblast secretes Cerberus, a Nodal antagonist, which prevents streak formation in the epiblast beneath it; the streak forms only where the hypoblast has been displaced by the endoblast growing from Koller's sickle, at the posterior. Without hypoblast, Nodal signalling is uninhibited everywhere that Vg1 and Wnt8c from the marginal zone can induce it, and several streaks form. The position of the streak is therefore determined by the inhibitory hypoblast and the posterior inducing signals together, not by a **prepattern** of the epiblast cells.

9. A woman's fetus is found to have **trisomy** in chorionic villus samples but not in amniotic fluid cells. Using the origin of these tissues, explain the result.

   **Answer** Chorionic villi are sampled from the placenta, mostly trophoblast and extraembryonic mesoderm, which derive from the trophectoderm and from extraembryonic lineages; amniotic fluid cells come largely from the fetus (skin, urinary and respiratory tracts) and the amnion, derived from the epiblast. A trisomy present in the trophoblast lineage but not in the epiblast lineage (confined placental mosaicism, as in Question 10 of [7.5.5](/7.5.5)) gives an abnormal villus result with a normal fetal **karyotype**. The amniocentesis result is the better guide to the fetus, although confined placental mosaicism can still affect placental function.

10. (Open question) The amphibian model of 9.5.3 assumes that cell types differ only in surface tension. Propose one measurement and one perturbation that would test whether this assumption accounts for the direction of the surface streaming in a *Xenopus* gastrula.

    **Answer** Measurement: map the effective tissue surface tension of explants from animal cap, marginal zone and vegetal regions (by compression of aggregates, [7.5.7](/7.5.7)) and the viscosity of each; fit the Legendre coefficients $A_n$ of the measured profile and predict the initial surface velocities from Proposition 9.5.1, to be compared with particle-image velocimetry of the surface flow at the onset of gastrulation. Perturbation: raise or lower the surface tension of one region locally, for example by expressing a constitutively active myosin regulator or extra cadherin in the animal cap, or by reducing cortical tension with a Rho kinase inhibitor in the vegetal cells, and test whether the streaming changes direction or speed as the model predicts. A mismatch even after including the blastocoel would point to active forces (intercalation, vegetal rotation) that the model omits.
