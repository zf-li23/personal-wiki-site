---
title: "The Machinery of Vesicle Traffic: Coats, Rabs and SNAREs"
description: How membrane-enclosed compartments exchange material while keeping their identity. Budding, transport, tethering and fusion; the COPII, COPI and clathrin coats, their GTPase switches (Sar1, Arf1), adaptors and dynamin, and the mechanics and energetics of budding; compartment identity encoded by phosphoinositides and Rab proteins, Rab cascades and a model of Rab5-to-Rab7 conversion; tethering factors, SNARE zippering, NSF and SM proteins; retrieval by the KDEL receptor and the balance of membrane flow; motor-driven transport; diseases of the machinery and new routes such as migrasomes.
---

The compartments of the endomembrane system ([7.3.6](/7.3.6)) are not static: membrane and lumenal content flow continuously from the ER through the Golgi apparatus to the plasma membrane, from the plasma membrane to endosomes and lysosomes, and back along each of these routes. Most of this traffic is carried by vesicles and tubules that bud from one compartment and fuse with another. Two requirements pull in opposite directions. The flow is enormous: a cultured fibroblast internalizes about 1 % of its plasma membrane every minute, the equivalent of its whole surface in less than two hours, and a pancreatic acinar cell secretes its own mass of protein each day. Yet each compartment keeps a distinct composition, as if the membranes never mixed. The machinery described in this chapter reconciles the two: coats select what leaves a compartment and shape the carrier (8.2); phosphoinositides and Rab proteins label each membrane with its identity (8.3); tethers and SNAREs make sure that a carrier fuses only with the right target (8.4); retrieval pathways return what escaped and keep the flows in balance (8.5); and motors move carriers over long distances (8.6). The last section takes up diseases of the machinery and routes that bypass it (8.7). The ER, where the secretory pathway begins, is the subject of [7.3.7](/7.3.7); the Golgi apparatus and secretion of [7.3.9](/7.3.9); endocytosis of [7.3.10](/7.3.10). The **SNARE** proteins were introduced as a family of membrane proteins in [7.1.13](/7.1.13), and the GTPase switches as signaling molecules in [7.1.15](/7.1.15).

## 8.1. The Logic of Vesicle Traffic

**Definition 8.1.1 (Transport Vesicle)** A **transport vesicle** is a small membrane-enclosed carrier, typically 50–150 nm in diameter, that buds from a donor compartment, carrying membrane and lumenal content selected there, and fuses with a target compartment, delivering them. Transport carriers can also be tubules or larger, irregular membrane fragments.

Every round of vesicle transport passes through the same steps:

1. Budding. A coat assembles on the cytosolic face of the donor membrane, collects cargo and bends the membrane into a bud, which is then pinched off.
2. Uncoating. The coat is shed shortly after budding, exposing the proteins that will recognize the target.
3. Transport. The vesicle diffuses or is carried along microtubules or actin filaments by motor proteins.
4. Tethering. Long proteins or protein complexes on the target capture the vesicle at a distance.
5. Docking and fusion. SNARE proteins on the two membranes zipper together and fuse the bilayers; the SNAREs are then separated and recycled.

Three consequences follow from this mechanism. First, topology is preserved: budding and fusion never expose the lumen to the cytosol, so the lumen of every compartment of the pathway is topologically equivalent to the outside of the cell, and a protein's cytosolic and lumenal domains keep their sides from synthesis in the ER to the plasma membrane. Second, only material that a coat collects, or that happens to be in the lumen or membrane of the bud, moves; selection is done at budding. Third, every forward flow of membrane must be balanced by a return flow, or the donor would be consumed and the target would grow without limit (8.5.2). The five steps also define the experimental logic of the field: yeast secretion mutants blocked at each step ([7.3.9](/7.3.9)) and cell-free systems that reconstitute budding or fusion from purified components allowed the machinery to be identified biochemically, work recognized by the 2013 Nobel Prize to James Rothman, Randy Schekman and Thomas Südhof.

## 8.2. Coats

**Definition 8.2.1 (Coat Protein)** A **coat protein** is a cytosolic protein that assembles, usually as part of a lattice with other coat proteins, on the cytosolic face of a membrane, where it concentrates specific membrane proteins (cargo and cargo receptors) and deforms the membrane into a bud. Coats are typically organized in two layers: an inner layer that binds the membrane and cargo, and an outer layer that forms a cage.

The three best-understood coats act on different routes (figure). Each is recruited by a membrane signal (an activated GTPase, a phosphoinositide, or both) and each is shed after budding, because the same signal is reversed.

![The three main vesicle coats. A: their routes in an animal cell: COPII (green) on vesicles from ER exit sites to the Golgi; COPI (blue) on vesicles returning from the Golgi to the ER and moving between Golgi cisternae; clathrin (yellow) with the adaptor AP1 on vesicles from the trans-Golgi network to endosomes and with AP2 on endocytic vesicles from the plasma membrane. B: the coats in section, with their GTPase, inner layer, outer layer and route: COPII (Sar1; Sec23/24; Sec13/31), COPI (Arf1; the two subcomplexes of coatomer), clathrin (Arf1 for AP1 or PI(4,5)P2 for AP2; adaptor complexes; clathrin triskelia).](./plots/coats.py)

| Coat | GTPase (GEF) | Inner layer, cargo binding | Outer layer | Route | Typical signals read |
|---|---|---|---|---|---|
| COPII | Sar1 (Sec12) | Sec23/24; Sec24 binds cargo | Sec13/31 | ER → ERGIC/Golgi | cytosolic di-acidic (DxE), di-hydrophobic (FF, LL) motifs; cargo receptors for lumenal cargo |
| COPI | Arf1 (GBF1) | coatomer F-subcomplex (β, γ, δ, ζ) | coatomer B-subcomplex (α, β′, ε) | Golgi → ER; between cisternae | C-terminal KKXX of ER membrane proteins; the KDEL receptor |
| Clathrin–AP1 | Arf1 | AP1 | clathrin | trans-Golgi network → endosomes | YXXΦ, [DE]XXXL[LI]; mannose 6-phosphate receptors |
| Clathrin–AP2 | none (PI(4,5)P₂) | AP2 | clathrin | plasma membrane → endosomes | YXXΦ, [DE]XXXL[LI], NPXY (other adaptors) |
| AP3 | Arf1 | AP3 | clathrin in animal cells (its role is debated); none in yeast | TGN and endosomes → lysosomes, lysosome-related organelles, yeast and plant vacuoles | [DE]XXXL[LI] of LIMP-2, tyrosinase and the yeast vacuolar alkaline phosphatase |
| Retromer | Rab7 | SNX dimers | Vps35–Vps29–Vps26 | endosomes → TGN, plasma membrane | Φ-X-[LMV] and others ([7.3.10](/7.3.10)) |

(Φ is a bulky hydrophobic residue, X any residue.)

### 8.2.1. COPII: Leaving the ER

**Definition 8.2.2 (COPII)** **COPII** is the coat of vesicles that bud from ER exit sites and carry cargo from the ER towards the Golgi apparatus. It is assembled in sequence from the GTPase Sar1, activated on the ER membrane by its exchange factor Sec12; the inner coat complex Sec23/Sec24, which binds Sar1-GTP and cargo; and the outer coat complex Sec13/Sec31, which polymerizes into a cage.

The order of assembly was worked out by reconstituting budding from ER membranes or synthetic liposomes with the five purified cytosolic proteins and GTP (Schekman and colleagues, 1994). Sar1-GDP is a soluble **small G protein**; the **guanine nucleotide-exchange factor** Sec12, an ER membrane protein, loads it with GTP, which exposes an N-terminal amphipathic helix that inserts into the cytosolic leaflet, both anchoring Sar1 and beginning to bend the membrane. Sar1-GTP recruits Sec23/24, a bow-tie-shaped heterodimer whose concave face matches the curvature of a vesicle. Sec24 has several distinct binding sites for export signals of transmembrane cargo; soluble lumenal cargo is collected by transmembrane receptors such as the mannose lectin ERGIC-53, which links the folded glycoproteins released by the calnexin cycle ([7.3.7](/7.3.7)) to the coat. Sec13/31 rods then join at their ends into a cuboctahedral cage that clamps the inner layer together. Sec23 is also the **GTPase-activating protein** for Sar1, and Sec31 stimulates it further. The coat therefore carries the timer of its own disassembly: once the cage is built, GTP hydrolysis begins to release Sar1 and loosen the coat, so that coats that fail to capture cargo turn over quickly, while cargo binding stabilizes them.

COPII vesicles are 60–90 nm across, too small for procollagen fibrils (about 300 nm) or chylomicrons. Large cargo leaves the ER through enlarged carriers organized at exit sites by TANGO1, which binds procollagen in the lumen and holds the COPII machinery on the cytosolic side so that the carrier grows before it is cut. ER exit sites are long-lived domains of the ER, a few hundred in a mammalian cell, organized by the scaffold Sec16; their number scales with secretory load.

### 8.2.2. COPI: Returning and Recycling

**Definition 8.2.3 (COPI)** **COPI** is the coat of vesicles that carry membrane and escaped ER proteins from the Golgi apparatus back to the ER and between Golgi cisternae. It consists of the GTPase Arf1 and coatomer, a seven-subunit complex that is recruited en bloc from the cytosol.

Arf1 resembles Sar1 but carries an N-terminal myristoyl group in addition to its amphipathic helix. Its Golgi exchange factor GBF1 is the target of the fungal metabolite brefeldin A, which blocks COPI assembly: within minutes the Golgi apparatus loses its coat, and its membranes are absorbed back into the ER through tubules, showing that the existence of the Golgi as a separate compartment depends on continuous balanced traffic. Coatomer binds the C-terminal KKXX motif of ER membrane proteins directly, and soluble ER proteins through the KDEL receptor (8.5.1). Its Arf GAP (ArfGAP1) is most active on highly curved membranes, through an amphipathic lipid-packing sensor motif that inserts only where the lipids are loosely packed: GTP hydrolysis is thus coupled to bud formation, again a timer built into the coat. COPI vesicles were first isolated from Golgi membranes incubated with the non-hydrolyzable analog GTPγS, which arrests the cycle at the coated stage (Rothman, Orci and colleagues).

### 8.2.3. Clathrin and Its Adaptors

**Definition 8.2.4 (Clathrin)** **Clathrin** is a coat protein that forms the outer layer of coated pits and vesicles at the plasma membrane and the trans-Golgi network. Its assembly unit, the triskelion, consists of three heavy chains (about 190 kDa) joined at their C-terminal ends, each with a bound light chain; triskelia assemble into a polyhedral lattice of hexagons and pentagons.

**Definition 8.2.5 (Adaptor Protein Complex)** An **adaptor protein complex** (AP complex) is one of five related heterotetrameric complexes (AP1–AP5) that form the inner layer of clathrin coats or related coats: each binds membrane phosphoinositides and the sorting signals of cargo through its subunits, and recruits clathrin. AP1 acts at the trans-Golgi network and endosomes, AP2 at the plasma membrane, and AP3 on the route to lysosomes and lysosome-related organelles.

These complexes should not be confused with the signaling **adaptor proteins** such as Grb2 ([7.1.15](/7.1.15)), which link activated receptors to downstream enzymes. AP2, the best studied, consists of two large subunits (α and β2), a medium subunit (μ2) and a small one (σ2). It is recruited by PI(4,5)P₂ in the plasma membrane and is initially closed; binding to PI(4,5)P₂ and cargo opens it, exposing the binding site of μ2 for YXXΦ signals and of σ2–α for [DE]XXXL[LI] signals. Many other adaptors (epsin, Dab2, ARH, arrestins, FCHo) bind clathrin, AP2 and further sorting signals; endocytic sites are built by a network of weak, multivalent interactions rather than a fixed complex.

![Formation of a clathrin-coated vesicle. A: a clathrin triskelion: three heavy chains joined at the hub, each with a light chain on its proximal segment, a knee and an N-terminal domain that binds adaptors. B: triskelia assemble with one hub at each vertex of a polyhedral cage; any closed cage of hexagons and pentagons in which three edges meet at each vertex has exactly 12 pentagons, and the number of hexagons sets its size (here the 60-triskelion "soccer ball" with 20 hexagons around its vesicle). C: budding at the plasma membrane: AP2 and other adaptors bind cargo and PI(4,5)P2 and recruit clathrin to a flat patch, the lattice curves into a pit and then a deep pit, and dynamin forms a helical collar around the narrow neck. Bottom: the released vesicle is uncoated by the ATPase Hsc70 and its cofactor auxilin, and the triskelia are reused.](./plots/clathrin-coat.py)

The pentagons are the geometric source of curvature. A flat lattice of hexagons has zero curvature; replacing hexagons by pentagons introduces positive curvature, and Euler's polyhedron formula fixes the number of pentagons in a closed cage. For a cage in which three edges meet at each of $V$ vertices, with $p$ pentagons and $h$ hexagons, the counts of edges ($E = 3V/2$) and faces ($F = p + h$) satisfy $V - E + F = 2$, and counting edges from the faces gives $2E = 5p + 6h$. Eliminating $V$ and $E$ gives $p = 12$, whatever $h$ is. Clathrin cages from 28 triskelia ($h = 4$) to more than 100 have been seen; the diameter of the vesicle depends on how many hexagons the lattice incorporates before it closes. Whether clathrin assembles first as a flat lattice that then bends (which requires rearranging hexagons into pentagons) or curves from the start was long debated; correlative light and electron microscopy shows that both happen, depending on the cell type and on how quickly the membrane is bent.

### 8.2.4. Pinching Off and Uncoating

**Definition 8.2.6 (Dynamin)** **Dynamin** is a large GTPase (about 100 kDa) that assembles into a helical collar around the neck of a budding vesicle; GTP hydrolysis drives a conformational change of the helix that constricts the neck until the membrane undergoes fission, releasing the vesicle.

Dynamin has a GTPase domain, a stalk that drives its polymerization, and a pleckstrin homology (PH) domain that binds PI(4,5)P₂. It is recruited to necks by proteins with BAR domains (amphiphysin, endophilin, SNX9), crescent-shaped dimers that bind and stabilize curved membranes. The *shibire* mutant of *Drosophila*, a temperature-sensitive dynamin, is paralyzed within seconds at the restrictive temperature: synaptic vesicles are not recycled, and the nerve terminals fill with coated pits with long necks wrapped in dynamin rings. Dynamin-related proteins perform fission and fusion elsewhere: Drp1 divides mitochondria and peroxisomes ([7.3.12](/7.3.12)), atlastin fuses ER tubules ([7.3.7](/7.3.7)).

After release, the coat must be removed before the vesicle can fuse. COPII and COPI lose their coats when their GTPases hydrolyze GTP (8.2.1, 8.2.2). The clathrin coat is removed by the ATPase Hsc70, recruited by its cofactor auxilin, which arrives once the vesicle is free; at the same time the phosphatase synaptojanin hydrolyzes PI(4,5)P₂, so that AP2 loses its membrane anchor. The change of phosphoinositide converts the vesicle from a "plasma membrane" identity to an early endocytic one (8.3.1).

### 8.2.5. The Energetics of Budding

Why does budding need an elaborate coat? Bending a lipid bilayer costs energy ([7.3.4](/7.3.4)). In the Helfrich model the bending energy of a membrane is $\int \frac{\kappa}{2}(2H - c_0)^2\,\mathrm{d}A$, where $H$ is the mean curvature, $c_0$ the spontaneous curvature and $\kappa$ the bending rigidity, about $20\,k_{\mathrm{B}}T$ for a typical biological membrane. A sphere of radius $R$ has $H = 1/R$ and area $4\pi R^2$, so for a membrane without spontaneous curvature

$$
E_{\mathrm{sphere}} = \frac{\kappa}{2}\left(\frac{2}{R}\right)^2 4\pi R^2 = 8\pi\kappa \approx 500\,k_{\mathrm{B}}T,
\tag{8.1}
$$

independent of the radius. A small vesicle costs no more bending energy than a large one; what changes with size is everything proportional to area. If the coat binds the membrane with an energy $w$ per unit area and the membrane is under tension $\sigma$, the total energy of a closed bud is

$$
E(R) = 8\pi\kappa - 4\pi R^2 (w - \sigma),
\tag{8.2}
$$

which becomes negative, so that budding is favorable, when $R$ exceeds $R^* = \sqrt{2\kappa/(w - \sigma)}$. For $R = 30\,\mathrm{nm}$ the coat must provide $w - \sigma \approx 2\kappa/R^2 \approx 0.04\,k_{\mathrm{B}}T\,\mathrm{nm}^{-2}$, about $1\,k_{\mathrm{B}}T$ per $25\,\mathrm{nm}^2$ of membrane, which is a small fraction of the binding energy of one adaptor. Coats also impose a preferred curvature: a rigid lattice of a given geometry corresponds to a spontaneous curvature $c_0$, and with it the bending energy becomes $8\pi\kappa(1 - c_0R/2)^2$, which is minimal (zero) at $R = 2/c_0$. The shape of the coat proteins thus selects the size of the vesicle, which is why each coat makes vesicles of a characteristic diameter.

![The energy of forming a spherical bud of radius R (Helfrich model, energies in units of kBT, κ = 20 kBT). A: the bending energy of a closed sphere is 8πκ ≈ 500 kBT for any R (dashed); a coat that binds with energy w per unit area against a membrane tension σ = 0.005 kBT/nm² lowers the total energy in proportion to the area, so that budding becomes favorable beyond the radius marked by a dot, R* = (2κ/(w − σ))^(1/2); stronger binding allows smaller vesicles. B: a coat that imposes a spontaneous curvature c0 makes the bending energy minimal at R = 2/c0 (here 30, 45 and 60 nm), selecting the vesicle size; without spontaneous curvature (dashed) no size is preferred.](./plots/budding-energy.py)

Two further costs matter at the end of budding. The neck must be narrowed to a few nanometers before the two leaflets can rearrange; this is the step that dynamin, or in other systems ESCRT-III ([7.3.10](/7.3.10)) or the amphipathic helices of Sar1 and Arf1, provides. And membrane tension resists the whole process: when the plasma membrane is stretched, clathrin pits stall as shallow, flat structures and actin polymerization is recruited to complete them. The model explains why the curvature-generating proteins of the cell (coats, BAR domains, amphipathic helices, reticulons) act together: none alone supplies the $\sim 500\,k_{\mathrm{B}}T$ of a closed sphere at physiological tension.

## 8.3. The Identity of Compartments

A vesicle must find its target among many membranes. The cytosolic faces of compartments therefore carry combinations of markers that act like addresses. Two families of markers dominate: phosphoinositides in the lipid bilayer and Rab GTPases bound to it.

### 8.3.1. Phosphoinositides

Phosphatidylinositol can be phosphorylated at positions 3, 4 and 5 of its inositol ring, alone or in combination, to give seven phosphoinositides. Kinases and phosphatases that produce and remove each species are localized to particular compartments, so each compartment has a characteristic phosphoinositide on its cytosolic face:

| Phosphoinositide | Main location | Made by | Read by (examples) |
|---|---|---|---|
| PI(4,5)P₂ | plasma membrane | PIP5K (from PI(4)P) | AP2, dynamin PH domain, epsin, exocyst; also substrate of phospholipase C |
| PI(3,4,5)P₃ | plasma membrane, transiently after signals | **phosphoinositide 3-kinase** class I | PH domains of Akt, PDK1 ([7.1.15](/7.1.15)) |
| PI(4)P | Golgi (especially TGN), also plasma membrane | PI4KIIIβ, PI4KIIα | AP1, GGAs, FAPP, OSBP, CERT |
| PI(3)P | early endosomes, autophagosome precursors | Vps34 (class III PI3K) | FYVE domains (EEA1), PX domains of sorting nexins |
| PI(3,5)P₂ | late endosomes, lysosomes | PIKfyve (from PI(3)P) | lysosomal channels (TRPML1), ESCRT-related proteins |

**Definition 8.3.1 (Phosphoinositide Code)** The **phosphoinositide code** is the use of the compartment-specific distribution of phosphoinositides, set by localized kinases and phosphatases, to label membranes: proteins with domains that bind particular phosphoinositides (PH, FYVE, PX, ENTH and others) are recruited to the compartment whose phosphoinositide they recognize, often only in combination with a second signal such as an active Rab or Arf GTPase.

Because the head groups can be modified within seconds, the code can change as a membrane matures. The clathrin-coated vesicle described above loses PI(4,5)P₂ through synaptojanin, the newly fused early endosome acquires PI(3)P from Vps34, and conversion of PI(3)P into PI(3,5)P₂ accompanies the maturation of late endosomes. Coincidence detection, the requirement that a protein bind both a lipid and a protein marker at once, makes recruitment much more specific than either signal alone.

### 8.3.2. Rab Proteins

**Definition 8.3.2 (Rab Protein)** A **Rab protein** is a member of the largest family of small GTPases of the Ras superfamily, about 60 in humans (11 in budding yeast), that are bound to specific membranes through C-terminal geranylgeranyl groups. In its GTP-bound form a Rab recruits effector proteins that mediate vesicle formation, movement, tethering and fusion; each Rab is enriched on a particular compartment and helps define its identity.

| Rab | Compartment or route |
|---|---|
| Rab1 | ER → Golgi (yeast Ypt1) |
| Rab6 | Golgi, retrograde and exocytic carriers |
| Rab5 | early endosomes, plasma membrane → early endosome |
| Rab7 | late endosomes, lysosomes |
| Rab11 | recycling endosomes, ciliogenesis |
| Rab3, Rab27 | synaptic vesicles, secretory granules, melanosomes |
| Rab8 (yeast Sec4) | post-Golgi carriers to the plasma membrane, primary cilia |

Like other GTPases ([7.1.14](/7.1.14), [7.1.15](/7.1.15)), a Rab is a switch whose state is set by a **guanine nucleotide-exchange factor** and a **GTPase-activating protein**, but its cycle adds a membrane step (figure). After synthesis, Rab escort protein (REP) presents the new Rab to Rab geranylgeranyltransferase, which attaches two geranylgeranyl groups. In the cytosol the GDP-bound Rab is held by GDP dissociation inhibitor (GDI), which hides the lipid anchors. GDI delivers Rab-GDP to membranes; a membrane-bound GEF then exchanges GDP for GTP, which locks the Rab on that membrane because GDI does not bind Rab-GTP. Rab-GTP recruits effectors; a GAP stimulates hydrolysis, and GDI extracts the inactive Rab for another cycle. The localization of a Rab is therefore set mainly by where its GEF is, not by the Rab itself: GEFs placed artificially on mitochondria bring their Rabs there. Loss of REP1 causes choroideremia, a degeneration of the retina, whose cells depend on REP1 to prenylate Rab27.

![Two GTPase switches of vesicle traffic (GDP form left, GTP form right; exchange catalyzed by the GEF above, hydrolysis stimulated by the GAP below; open circles mark catalysis). A: Sar1 is soluble in its GDP form; the ER membrane protein Sec12 loads it with GTP, Sar1-GTP inserts into the membrane and recruits the inner COPII coat Sec23/24, and Sec23 together with Sec31 stimulates GTP hydrolysis, so the coat carries its own timer. B: a Rab protein is delivered to a membrane by GDI, activated there by a compartment-specific GEF, recruits effectors (tethers, motors, kinases, GEFs of other Rabs) while bound to GTP, and after GAP-stimulated hydrolysis is extracted again by GDI.](./plots/gtpase-switches.py)

The effectors of a single Rab can cover every step of transport. Rab5-GTP on early endosomes recruits the long tether EEA1 (8.4.1), the PI 3-kinase Vps34, which makes the PI(3)P that EEA1 also binds, motor adaptors, and Rabaptin-5, which brings in the Rab5 GEF Rabex-5. This last interaction is a positive feedback loop: Rab5-GTP recruits more of its own activator, so that Rab5 domains are self-reinforcing and sharply bounded. Rab5 domains on early endosomes can be seen as discrete patches that persist while the membrane under them exchanges with other compartments.

### 8.3.3. Rab Cascades and Rab Conversion

**Definition 8.3.3 (Rab Cascade)** A **Rab cascade** is a sequence of Rab proteins acting along a pathway in which an active upstream Rab recruits the GEF of the next Rab, and the downstream Rab recruits the GAP of the upstream one; it links successive identities of a membrane or route so that one replaces the other in a defined order.

**Definition 8.3.4 (Rab Conversion)** **Rab conversion** is the replacement of one Rab by another on the same membrane through a Rab cascade, as when Rab5 on an early endosome is replaced by Rab7 as it matures into a late endosome.

In the exocytic pathway of yeast, Ypt31/32 on late Golgi membranes recruit Sec2, the GEF of Sec4, and Sec4 on secretory vesicles recruits a GAP for Ypt31/32. On endosomes, Rab5-GTP recruits the Mon1–Ccz1 complex (SAND-1 in *C. elegans*), the GEF for Rab7, and Mon1 displaces Rabex-5; as Rab7 becomes active, it recruits a Rab5 GAP. Live imaging of endosomes in human cells (Rink and colleagues, 2005) showed that Rab5 is lost and Rab7 gained abruptly, within a few minutes, on each endosome, rather than by gradual sorting of membrane into separate Rab5 and Rab7 vesicles. Del Conte-Zerial and colleagues (2008) showed that this behavior follows from the network of feedbacks, which they called a cut-out switch.

A minimal version of their model describes the fractions $r_5$ and $r_7$ of Rab5 and Rab7 that are active on one endosome (time in minutes):

$$
\begin{aligned}
\frac{\mathrm{d}r_5}{\mathrm{d}t} &= \left(k_5 + f_5\frac{r_5^2}{K_5^2 + r_5^2}\right)(1 - r_5) - \left(g_5 + h\frac{r_7^4}{K_h^4 + r_7^4}\right) r_5,\\
\frac{\mathrm{d}r_7}{\mathrm{d}t} &= \left(k_7 + c\,\frac{r_5^4}{K_c^4 + r_5^4} + f_7\frac{r_7^2}{K_7^2 + r_7^2}\right)(1 - r_7) - g_7 r_7.
\end{aligned}
\tag{8.3}
$$

| Term | Biological meaning |
|---|---|
| $k_5$, $k_7$ | basal activation (delivery by GDI, basal GEF activity) |
| $f_5\,r_5^2/(K_5^2 + r_5^2)$ | Rab5 positive feedback: Rab5-GTP recruits Rabaptin-5–Rabex-5 |
| $c\,r_5^4/(K_c^4 + r_5^4)$ | Rab5-GTP recruits the Rab7 GEF Mon1–Ccz1 (cooperative, threshold-like) |
| $f_7\,r_7^2/(K_7^2 + r_7^2)$ | Rab7 self-recruitment through its effectors |
| $h\,r_7^4/(K_h^4 + r_7^4)$ | the cut-out: Rab7-GTP recruits a Rab5 GAP and removes Rabex-5 |
| $g_5$, $g_7$ | basal GAP activity |

With the cut-out, the model behaves like the endosomes in the movies (figure): Rab5 is activated first and holds a plateau while Rab7 builds up slowly through the cooperative coupling; once Rab7 crosses a threshold its own positive feedback and the inhibition of Rab5 make the switch abrupt and irreversible. Without the cut-out ($h = 0$), both Rabs stay on, and the endosome would be a stable hybrid. The duration of the early-endosome stage, during which cargo is sorted and receptors recycled ([7.3.10](/7.3.10)), is set mainly by the strength $c$ of the coupling and falls steeply as $c$ increases, so the cell can tune it by regulating the Rab7 GEF. The design combines two motifs that recur in the cell-cycle oscillator ([7.3.20](/7.3.20)): positive feedback, which makes each state self-sustaining, and delayed negative feedback, which ends the first state once the second is established.

![The cut-out switch model of Rab5-to-Rab7 conversion, Eq. (8.3), with k5 = 0.02, f5 = 1, K5 = 0.5, g5 = 0.15, k7 = 0.001, c = 0.02, Kc = 0.7, f7 = 0.6, K7 = 0.5, g7 = 0.1, Kh = 0.4 and h = 1.5 (per minute where applicable). A: active Rab5 (green) rises by positive feedback, Rab7 (red) is activated with a delay, and Rab5 is then switched off within a few minutes (solid lines); without the Rab7-to-Rab5-GAP cut-out (h = 0, dotted) both stay active. B: the time of conversion (when active Rab7 first exceeds active Rab5) falls steeply as the recruitment of the Rab7 GEF by Rab5, c, is increased.](./plots/rab-conversion.py)

## 8.4. Tethering and Fusion

### 8.4.1. Tethers

**Definition 8.4.1 (Tethering Factor)** A **tethering factor** is a protein or protein complex on a target membrane, usually recruited by an active Rab or Arf GTPase, that captures an incoming vesicle at a distance and holds it close to the membrane before SNARE complexes form. Tethers are either long coiled-coil proteins or multisubunit tethering complexes.

Long coiled-coil tethers, such as the golgins of the Golgi apparatus (GM130, giantin, golgin-84) and EEA1 on early endosomes, extend 100–300 nm into the cytosol and catch vesicles with their tips; GM130 and golgin-84 select different classes of vesicles, so the tethers themselves contribute to specificity. Multisubunit tethering complexes act closer to the membrane and often also chaperone SNARE assembly: the exocyst (eight subunits) on the plasma membrane for post-Golgi carriers; COG on the Golgi for intra-Golgi COPI vesicles; the Dsl1 complex on the ER for retrograde vesicles; GARP for endosome-to-TGN carriers; HOPS and CORVET on late and early endosomes and vacuoles; and TRAPP, which is also the GEF of Rab1, for COPII vesicles. Tethers thus convert the long-range diffusive search of a vesicle into a short-range, oriented encounter.

### 8.4.2. SNAREs and Their Zippering

**Definition 8.4.2** The SNARE on the membrane of a transport vesicle that pairs with SNAREs on the target is called the **v-SNARE**, and the SNAREs on the target membrane the **t-SNAREs**. Structurally, each SNARE contributes one α helix to a four-helix bundle whose central layer contains three glutamines and one arginine: SNAREs are classified as Q-SNAREs (Qa, Qb, Qc) or R-SNAREs, and a functional complex contains one helix of each class. A complex that bridges two membranes is called a trans-SNARE complex; after fusion, the same complex lies in one membrane as a cis-SNARE complex.

Humans have about 38 SNAREs (yeast 24). The neuronal complex is the prototype: the R-SNARE synaptobrevin (VAMP2) on synaptic vesicles pairs with the Qa-SNARE syntaxin-1 and with SNAP-25, which provides both the Qb and the Qc helix and is attached to the plasma membrane by palmitoylated cysteines. Zippering starts at the membrane-distal N-terminal ends of the SNARE motifs and proceeds towards the transmembrane domains, pulling the membranes together (figure). Optical-tweezers measurements on single neuronal complexes give a total free energy of zippering of about $65\,k_{\mathrm{B}}T$, released in stages, the largest part in the C-terminal half next to the membranes. The barrier for fusion of two bilayers, through a hemifused intermediate in which the outer leaflets have merged, and then a fusion pore, is of the order of tens of $k_{\mathrm{B}}T$; one to three SNARE complexes per fusion event are sufficient in different measurements. Weber, Rothman and colleagues (1998) showed that liposomes carrying only v-SNAREs and t-SNAREs fuse with each other, and that SNARE proteins are thus the minimal fusion machine. Botulinum and tetanus toxins are proteases that cleave neuronal SNAREs and block neurotransmitter release ([7.1.13](/7.1.13)).

Enveloped viruses solve the same problem with a single protein. Influenza hemagglutinin, triggered by the acidic pH of endosomes, and HIV gp41, triggered by binding to CD4 and a coreceptor, insert a hydrophobic fusion peptide into the target membrane and then fold back into a hairpin, a bundle of six helices, that draws the viral and cellular membranes together through a hemifused intermediate. As with SNAREs, the free energy of protein folding pays for the fusion barrier; the difference is that a viral fusion protein is used only once, whereas SNAREs are taken apart and reused (8.4.3). Peptides that block the hairpin, such as the drug enfuvirtide for gp41, inhibit viral entry.

![SNARE-driven membrane fusion. A: the v-SNARE on the vesicle and the t-SNAREs syntaxin (with its N-terminal Habc domain) and SNAP-25 (two helices, anchored by palmitoyl groups) on the target begin to zipper from their membrane-distal N-terminal ends into a four-helix bundle (left); as zippering proceeds towards the transmembrane domains the membranes are pulled into contact (right). B: an illustrative free-energy profile of one fusion cycle (in kBT, of the order of the values measured for neuronal SNAREs): docking and zippering of the trans complex release about 65 kBT, which pays for the barriers of hemifusion and fusion-pore opening; after fusion the stable cis complex lies in one membrane, and NSF with α-SNAP uses ATP hydrolysis to separate the SNAREs again.](./plots/snare-fusion.py)

### 8.4.3. Recycling SNAREs: NSF and α-SNAP

**Definition 8.4.3 (NSF)** **NSF** (N-ethylmaleimide-sensitive factor) is a hexameric AAA+ ATPase that, together with its adaptor α-SNAP (soluble NSF attachment protein), binds cis-SNARE complexes and uses the energy of ATP hydrolysis to unwind them, releasing the individual SNAREs for another round of fusion.

NSF was discovered by Rothman and colleagues as the factor, inactivated by the sulfhydryl reagent N-ethylmaleimide, that was needed for transport between Golgi cisternae in a cell-free system; the receptors for its adaptor SNAP were then purified from brain and turned out to be syntaxin, SNAP-25 and synaptobrevin, giving the SNAREs ("SNAP receptors") their name. NSF is not needed for fusion itself but to reset the system: zippering is energetically downhill, and without NSF the SNAREs would accumulate in inactive cis complexes. The same ATP-driven disassembly prevents the premature formation of nonproductive complexes on the same membrane.

### 8.4.4. SM Proteins and the Origin of Specificity

**Definition 8.4.4 (Sec1/Munc18 Protein)** **Sec1/Munc18 proteins** (SM proteins) are cytosolic proteins of about 65 kDa that bind syntaxin-family Qa-SNAREs and the assembling SNARE complex; they act as templates that align the v-SNARE and the Qa-SNARE in the correct register and are essential for fusion at every step of the secretory and endocytic pathways.

Each fusion step has its SM protein: Sec1 in yeast exocytosis, Munc18-1 at synapses, Vps45 on early endosomes, Vps33 in HOPS, Sly1 at the ER and Golgi. Mice lacking Munc18-1 have no neurotransmitter release at all. In neurons Munc18-1 first holds syntaxin in a closed conformation in which its Habc domain covers its SNARE motif; Munc13 opens it, and Munc18-1 then templates the complex with synaptobrevin, a sequence that makes fusion both precise and fast once $\ce{Ca^2+}$ triggers it through synaptotagmin (neurotransmitter release belongs to [7.16](/7.16)).

How specific is pairing? In liposome assays, of the many possible combinations of yeast SNAREs only those that correspond to known transport steps fused efficiently (McNew and colleagues, 2000), suggesting that SNAREs encode part of the specificity. In cells, however, several SNAREs can substitute for each other, and the specificity of a transport step is the product of several layers acting in sequence: the coat selects the cargo and the v-SNARE; the Rab and phosphoinositide code of the target recruits the tether, which captures the right vesicle; the SM protein and the cognate SNAREs allow fusion only between compatible partners. Each layer is imperfect; their combination makes mistargeting rare, much as kinetic proofreading combines several imperfect steps in translation ([7.2.19](/7.2.19)).

## 8.5. Retrieval and the Balance of Flows

### 8.5.1. The KDEL Receptor

**Definition 8.5.1 (KDEL Receptor)** The **KDEL receptor** is a seven-transmembrane protein of the ERGIC and the cis Golgi that binds soluble ER-resident proteins carrying the C-terminal tetrapeptide Lys-Asp-Glu-Leu (KDEL; HDEL in yeast, where the receptor is Erd2) in the slightly acidic lumen of these compartments, is packaged into COPI vesicles, and releases its ligands at the neutral pH of the ER.

ER-resident proteins such as BiP and PDI are soluble and leave the ER constantly by bulk flow in COPII vesicles. The ER retains them not by preventing their exit but by returning them: the KDEL receptor captures them in the Golgi and carries them back. The pH difference drives the cycle: the receptor binds KDEL when a histidine in its binding pocket is protonated at the pH of the cis Golgi (about 6.5) and lets it go in the ER (about 7.2), where the proton is lost. Binding also changes the conformation of the receptor so that its cytosolic tail is recognized by COPI. ER membrane proteins carry their own retrieval signals, the C-terminal KKXX motif bound directly by coatomer. Retrieval explains an old observation: adding KDEL to the C-terminus of a secreted protein makes it accumulate in the ER, while removing KDEL from BiP causes it to be secreted. The system is saturable, and when large amounts of a KDEL protein are overexpressed some of it escapes to the cell surface. Many sorting steps in the cell use the same pH-dependent logic: the mannose 6-phosphate receptor binds its cargo in the TGN and releases it in acidic endosomes ([7.3.11](/7.3.11)), and the LDL receptor releases LDL in endosomes ([7.3.10](/7.3.10)).

### 8.5.2. Membrane Flow and Compartment Size

The area of a compartment changes by the difference between the membrane delivered to it and the membrane removed from it:

$$
\frac{\mathrm{d}A}{\mathrm{d}t} = J_{\mathrm{in}} - J_{\mathrm{out}},
\tag{8.4}
$$

so a compartment of constant size requires an exact balance of forward and return flows. The flows are large. A cultured fibroblast internalizes about 1 % of its plasma membrane per minute (MBoC 7e, Chapter 13; in the stereological measurements of Steinman, Brodie and Cohn (1976), mouse L-cell fibroblasts internalized 54 % of their surface per hour and macrophages 186 %). For a plasma membrane area of about $3000\,\mathrm{\mu m^2}$ this is $30\,\mathrm{\mu m^2\,min^{-1}}$. An endocytic vesicle whose membrane has a diameter of $80\,\mathrm{nm}$ (about $100\,\mathrm{nm}$ including a clathrin coat) has area $\pi d^2 \approx 0.020\,\mathrm{\mu m^2}$, so the flow corresponds to about 1500 vesicles per minute, some 25 per second, the same order as the roughly 2500 clathrin-coated vesicles per minute counted in cultured fibroblasts ([7.3.10](/7.3.10), Example 10.1.1); the same area must be returned to the surface by recycling and secretion. A macrophage, at about 3 % per minute, internalizes the equivalent of its entire surface in about 30 minutes. The Golgi apparatus behaves in the same way: when ER exit is blocked, it shrinks within minutes as its membrane continues to leave; when COPI is blocked by brefeldin A, it merges with the ER. Compartments are steady states of flows, not containers, and their size is a readout of the balance of opposing transport steps. Because transport is selective (8.2), the steady state also has a composition that differs from that of the inflow, maintained by retrieving what should not move on.

## 8.6. Moving Vesicles

Over the distances of a large cell, diffusion of a vesicle in the crowded cytoplasm is too slow: a 100 nm vesicle has a diffusion coefficient in cytoplasm of the order of $10^{-2}\,\mathrm{\mu m^2\,s^{-1}}$ or less, so it would take about half an hour to diffuse $10\,\mathrm{\mu m}$ (time $\sim L^2/6D$), and a motor neuron carries vesicles over a meter of axon. Vesicles are therefore carried by motor proteins: kinesins move most of them towards the plus ends of microtubules, which lie at the cell periphery; cytoplasmic dynein moves them towards the minus ends at the centrosome and the Golgi; and myosin V carries them along actin filaments in the cortex for the last micrometer before fusion. Like most myosins, myosin V walks towards the plus (barbed) ends of actin filaments, which face the plasma membrane; myosin VI, the only known minus-end-directed myosin, moves endocytic vesicles inward from the cortex. Speeds are around $1\,\mathrm{\mu m\,s^{-1}}$, so the 10 µm trip takes seconds. Rabs and their effectors connect cargo to motors: Rab6 recruits dynein through the adaptor BICD2, Rab7 recruits dynein through RILP and kinesin through FYCO1, and Rab27a on melanosomes recruits myosin Va through melanophilin. Defects in this last link (Griscelli syndrome, with mutations in *RAB27A*, *MYO5A* or *MLPH*) leave pigment granules clumped around the nucleus of melanocytes and the hair silvery. The mechanisms of motor proteins are the subject of [7.3.13](/7.3.13) and [7.3.14](/7.3.14).

## 8.7. Diseases of the Machinery and Unconventional Routes

Because the coats, Rabs, tethers and SNAREs are each represented by many paralogs, most mutations in them cause tissue-specific diseases rather than lethality: the affected tissue is the one that depends most on a particular paralog or carries the largest load.

| Disease | Gene | Defect |
|---|---|---|
| Cranio-lenticulo-sutural dysplasia | *SEC23A* | COPII inner coat; fibroblasts and chondrocytes fail to export procollagen, so the skull sutures close late |
| Congenital dyserythropoietic anemia type II | *SEC23B* | defective erythroid precursors with double nuclear membranes |
| Chylomicron retention disease | *SAR1B* | intestinal cells cannot export chylomicrons, so fat and fat-soluble vitamins are malabsorbed |
| Choroideremia | *CHM* (REP1) | Rab prenylation in the retina |
| Griscelli syndrome type 2 | *RAB27A* | melanosome transport and cytotoxic granule secretion |
| Charcot–Marie–Tooth disease type 2B | *RAB7A* | peripheral axonal neuropathy |
| Centronuclear myopathy | *DNM2* (dynamin 2) | muscle weakness |
| Hermansky–Pudlak syndrome | *AP3B1* and others | lysosome-related organelles (melanosomes, platelet granules) |

Not all traffic follows the coat–Rab–SNARE route. Several cytosolic proteins without signal sequences, including the cytokine IL-1β and FGF2, leave the cell by unconventional secretion, either directly across the plasma membrane or through membrane carriers derived from the ER–Golgi intermediate compartment; the THU lab of Liang Ge has identified TMED10 as a channel through which such cargo enters this route ([7.3.6](/7.3.6)). A different carrier was found by Li Yu and colleagues (2015): migrasomes, vesicular structures up to a few micrometers across that form on the retraction fibers left behind by migrating cells, grow on tetraspanin-enriched membrane domains, and are released when the fibers break. Migrasomes carry signaling molecules to the cells that later pass the same spot, and they can remove damaged mitochondria from the cell (mitocytosis): a mode of transport between cells defined by cell migration rather than by a target membrane.

## Summary

- Vesicle traffic (Definition 8.1.1) proceeds by budding, uncoating, transport, tethering and fusion; it preserves topology, selects cargo at budding, and requires balanced forward and return flows.
- Coats (Definition 8.2.1) select cargo and bend membranes; each is recruited by a membrane signal and carries a timer for its removal:

  | | COPII (Definition 8.2.2) | COPI (Definition 8.2.3) | Clathrin (Definitions 8.2.4, 8.2.5) |
  |---|---|---|---|
  | Switch | Sar1–Sec12; GAP Sec23/Sec31 | Arf1–GBF1 (brefeldin A); ArfGAP1 senses curvature | Arf1 (AP1), PI(4,5)P₂ (AP2) |
  | Layers | Sec23/24 / Sec13/31 | coatomer F / B | AP complexes / triskelia |
  | Route | ER → Golgi | Golgi → ER, intra-Golgi | TGN, plasma membrane → endosomes |
  | Release | GTP hydrolysis | GTP hydrolysis | dynamin (Definition 8.2.6); Hsc70–auxilin, synaptojanin |

- Budding energetics: a sphere costs $8\pi\kappa \approx 500\,k_{\mathrm{B}}T$ regardless of size (Eq. (8.1)); coat binding pays in proportion to area (Eq. (8.2)), and coat-imposed spontaneous curvature selects $R = 2/c_0$; a clathrin cage of pentagons and hexagons always contains 12 pentagons.
- Identity: the phosphoinositide code (Definition 8.3.1) and Rab proteins (Definition 8.3.2), whose location is set by their GEFs; Rab cascades (Definition 8.3.3) and Rab conversion (Definition 8.3.4) order successive identities, and the cut-out switch model (Eq. (8.3)) explains the abrupt Rab5 → Rab7 transition by positive feedback plus delayed inhibition.
- Fusion: tethering factors (Definition 8.4.1) capture vesicles; v- and t-SNAREs (Definition 8.4.2) zipper into a Qa-Qb-Qc-R bundle, releasing about $65\,k_{\mathrm{B}}T$; NSF and α-SNAP (Definition 8.4.3) recycle SNAREs with ATP; SM proteins (Definition 8.4.4) template assembly. Specificity is the product of coat, Rab, tether, SM and SNARE layers.
- Retrieval: the KDEL receptor (Definition 8.5.1) binds in the acidic Golgi and releases in the neutral ER; compartment size is a steady state of membrane flows (Eq. (8.4)): a fibroblast internalizes about 1 % of its surface per minute, some 25 endocytic vesicles per second.
- Motors (kinesin outward, dynein inward, myosin V in the cortex) linked by Rab effectors move vesicles about $1\,\mathrm{\mu m\,s^{-1}}$; paralog-specific diseases (Sec23A, Sar1B, Rab27A and others) and unconventional routes (TMED10-dependent secretion, migrasomes) complete the picture.

## Questions

1. Brefeldin A inhibits the Arf1 GEF GBF1. Predict what happens within minutes to the Golgi apparatus and to a secretory protein, and why the effect shows that the Golgi is a steady state.

   **Answer** Without active Arf1, COPI (and Arf-dependent clathrin–AP1) coats dissociate from the Golgi. COPII vesicles continue to bring membrane to the Golgi, but retrograde COPI traffic stops and the Golgi membranes, which are still fusogenic, form tubules that fuse with the ER: within about 10 minutes Golgi enzymes are found in the ER. A secretory protein then accumulates in this hybrid ER–Golgi compartment, where it may receive some Golgi modifications, but it does not reach the trans-Golgi network or the cell surface. Washing out the drug restores a normal Golgi within an hour. The Golgi exists as a separate compartment only because its inflow is balanced by COPI-dependent outflow and recycling.

2. Use Euler's formula to show that a closed clathrin cage, in which three edges meet at each vertex and all faces are pentagons or hexagons, has exactly 12 pentagons. How many triskelia are in a cage with 8 hexagons?

   **Answer** With $V$ vertices, $E$ edges and $F = p + h$ faces, each vertex has three edges and each edge two vertices, so $E = 3V/2$; each edge borders two faces, so $2E = 5p + 6h$. Euler: $V - E + F = 2$, that is $\frac{2E}{3} - E + p + h = 2$, so $-\frac{E}{3} + p + h = 2$, and substituting $E = (5p + 6h)/2$ gives $-\frac{5p + 6h}{6} + p + h = 2$, so $p/6 = 2$ and $p = 12$. With $h = 8$, $2E = 60 + 48 = 108$, $E = 54$, $V = 2E/3 = 36$: 36 triskelia (the "hexagonal barrel").

3. Using Eq. (8.2) with $\kappa = 20\,k_{\mathrm{B}}T$ and negligible tension, what minimal binding energy per unit area must a coat provide to make a closed bud of radius 40 nm favorable? If one adaptor occupies about $100\,\mathrm{nm}^2$, how much binding energy per adaptor is that?

   **Answer** $w > 2\kappa/R^2 = 40/1600 = 0.025\,k_{\mathrm{B}}T\,\mathrm{nm}^{-2}$, which over the area $4\pi R^2 \approx 2.0 \times 10^4\,\mathrm{nm}^2$ adds up to $8\pi\kappa \approx 500\,k_{\mathrm{B}}T$. Per adaptor of $100\,\mathrm{nm}^2$, about $2.5\,k_{\mathrm{B}}T$, much less than the binding energy of a protein to a membrane through several lipid and cargo contacts. The difficulty of budding lies less in the total energy than in coordinating curvature and overcoming tension and the neck, which is why coats, BAR proteins and dynamin cooperate.

4. In the Rab conversion model (Eq. (8.3)), what happens if the Rab5 positive feedback is removed ($f_5 = 0$)? What if the Rab7 GEF cannot be recruited ($c = 0$)? Relate each to a possible mutant phenotype.

   **Answer** With $f_5 = 0$, Rab5 is activated only by its basal rate and stays low ($r_5 \approx k_5/(k_5 + g_5) \approx 0.12$); it then cannot activate Rab7 strongly through the cooperative term, so conversion is very slow or does not happen, corresponding to a loss of Rabex-5 or Rabaptin-5, with small, poorly fused early endosomes. With $c = 0$, Rab5 is activated normally but Rab7 never rises above its basal level and the cut-out is never triggered: endosomes stay Rab5-positive, as in cells lacking Mon1–Ccz1 (SAND-1 mutants in *C. elegans*), which accumulate enlarged early endosomes and fail to deliver cargo to lysosomes.

5. A cell line secretes a KDEL-tagged reporter when it is overexpressed but retains it at low expression. Explain. What would you expect if the pH of the Golgi were raised to 7.2 with a drug?

   **Answer** Retrieval is receptor-mediated and saturable: each KDEL receptor carries a limited amount of ligand per cycle, and at high expression most reporter molecules leaving the ER do not find a free receptor in the Golgi and continue to the cell surface. If Golgi pH is raised to that of the ER, the receptor's binding histidine is no longer protonated and it binds KDEL poorly in the Golgi, so retrieval fails and even endogenous ER proteins such as BiP are secreted, while any receptor that does bind would also fail to release its cargo in the ER.

6. Estimate how long a 100 nm vesicle would take to reach the cell surface 10 µm away by diffusion alone if its diffusion coefficient in cytoplasm is $0.01\,\mathrm{\mu m^2\,s^{-1}}$, and compare with kinesin transport at $1\,\mathrm{\mu m\,s^{-1}}$. What does the comparison mean for a neuron with a 1 m axon?

   **Answer** In three dimensions the mean squared displacement is $6Dt$, so $t \approx L^2/6D = 100/0.06 \approx 1700\,\mathrm{s}$, about half an hour, and much longer to find a particular site; kinesin covers 10 µm in 10 s. Over 1 m, diffusion would take $10^{12}/0.06\,\mathrm{s}$, about $5 \times 10^5$ years, whereas fast axonal transport at about 1 µm/s (roughly 10 cm per day) takes about 10 days. Long-range traffic in large cells is impossible without motors.

7. Why is it advantageous for COPII to contain the GAP of its own GTPase, and for ArfGAP1 to be activated by membrane curvature?

   **Answer** Both arrangements make coat disassembly automatic and coupled to the progress of budding. Coats are assembled only where the GEF is (Sec12 at exit sites, GBF1 on the Golgi), but they must not persist after the vesicle has formed, because a coated vesicle cannot fuse. If the GAP is part of the coat, hydrolysis begins as soon as the coat is complete, and the residence time of a coat is limited unless cargo binding stabilizes it, which also gives kinetic proofreading of cargo selection. A curvature-activated GAP hydrolyzes GTP preferentially on highly curved buds and vesicles, leaving flat membranes coated long enough to collect cargo. In both cases the cell avoids a separate signal to "finish".
