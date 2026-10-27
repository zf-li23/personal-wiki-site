---
title: Mitosis, Cytokinesis and the Mechanics of Meiosis
description: The machinery that M-Cdk sets in motion; the stages of mitosis; cohesin and condensin; the mitotic spindle, its three classes of microtubules, its motors and the search-and-capture problem with a quantitative model; kinetochores, error correction by Aurora B and a model of the spindle assembly checkpoint; anaphase A and B; cytokinesis in animal and plant cells; asymmetric division; and the cell mechanics of meiosis, from the synaptonemal complex and chiasmata to cohesin protection, oocyte divisions and the maternal age effect.
---

The previous chapter described the control system that decides when a cell enters and leaves mitosis; this one describes the machines that do the work. In about an hour a human cell condenses 46 replicated chromosomes, each a DNA molecule centimeters long, into compact rods, builds a spindle of tens of thousands of microtubules, attaches every one of 92 kinetochores to the correct pole, waits until the last attachment is made, separates the sisters and pulls them apart, and cuts itself in two between them. The error rate is about one chromosome missegregated per hundred divisions in cultured cells, and lower in tissues. Three systems built earlier in this course cooperate: microtubules and their motors ([7.3.14](/7.3.14)) build and move the spindle, actin and myosin II ([7.3.13](/7.3.13)) divide the cytoplasm, and the nuclear envelope is taken apart and rebuilt ([7.3.16](/7.3.16#sec-16.6)). Their timing comes from the Cdk–APC/C system of [7.3.20](/7.3.20). The second half of the chapter treats meiosis as a variation on mitosis that segregates homologues before sisters; its genetic consequences (independent assortment, linkage, recombination maps) belong to genetics ([7.4](/7.4)), the molecular mechanism of recombination to [7.2.9](/7.2.9), and gametogenesis as a developmental process to [7.5](/7.5) and [7.14](/7.14).

## 21.1. An Overview of M Phase

### 21.1.1. The Stages of Mitosis

**Definition 21.1.1 (Mitosis and Its Stages)** **Mitosis** is the division of a eukaryotic nucleus in which the replicated chromosomes are separated into two daughter nuclei with identical sets of chromosomes. It is divided, from the behavior of the chromosomes in the light microscope, into five stages: **prophase**, in which the chromosomes condense and the centrosomes separate; **prometaphase**, which begins with the breakdown of the nuclear envelope and in which chromosomes attach to the spindle; **metaphase**, in which all chromosomes are bi-oriented and aligned at the spindle equator; **anaphase**, in which the sister chromatids separate and move to opposite poles; and **telophase**, in which nuclear envelopes re-form around the two sets of chromosomes.

The stages are familiar from general biology, so one table suffices; the interest of this chapter lies in the mechanisms.

| Stage | Chromosomes | Spindle and centrosomes | Membranes | Triggered by |
|---|---|---|---|---|
| Prophase | condense (condensin), sister arms resolve; kinetochores mature | the two centrosomes mature and separate along the nuclear envelope (dynein, kinesin-5) | nuclear envelope intact; Golgi fragments | M-Cdk, Plk1, Aurora A |
| Prometaphase | attach to microtubules, first laterally, then end-on; congress to the equator | spindle assembles; microtubules very dynamic | nuclear envelope breaks down (in animals), absorbed into the ER | M-Cdk phosphorylation of lamins and nucleoporins |
| Metaphase | bi-oriented on the metaphase plate; oscillate; under tension | steady-state spindle with poleward flux | | spindle assembly checkpoint satisfied |
| Anaphase | sisters separate (A); poles move apart (B) | kinetochore microtubules shorten, midzone forms | | APC/C–Cdc20: securin and cyclin B destroyed |
| Telophase | decondense | spindle disassembles; central spindle remains | nuclear envelopes and pores re-form; ER and Golgi reorganize | dephosphorylation (PP2A-B55, PP1) |
| Cytokinesis | | midbody; abscission | contractile ring, membrane insertion | RhoA at the equator |

![The stages of M phase in an animal cell (schematic; three chromosomes shown). 1, prophase: chromosomes condense inside the intact nucleus while the duplicated centrosomes nucleate asters and move apart. 2, prometaphase: the nuclear envelope breaks down (dashed fragments) and microtubules from the two poles capture kinetochores (red), at first laterally. 3, metaphase: all chromosomes are bi-oriented, their sister kinetochores attached to opposite poles by kinetochore microtubules, and aligned on the metaphase plate; interpolar microtubules overlap at the equator and astral microtubules radiate from the poles. 4, anaphase: the sister chromatids separate and move to the poles, kinetochores first, while the poles move apart. 5, telophase: nuclear envelopes re-form around the decondensing chromosomes, the central spindle remains between them, and the contractile ring (dark red) begins to constrict the equator. 6, cytokinesis: the furrow has narrowed to a bridge containing the midbody, which is cut at abscission; each daughter has one nucleus and one centrosome](./plots/m-phase-stages.py)

### 21.1.2. Cohesin and Condensin

Two related ring-shaped complexes prepare the chromosomes for segregation. Both are SMC complexes, whose ATPase heads and coiled-coil arms were described with **loop extrusion** in [7.2.4](/7.2.4); the architecture of the mitotic chromosome they produce is described in [7.3.17](/7.3.17#sec-17.6).

**Definition 21.1.2 (Cohesin and Condensin)** **Cohesin** is the SMC complex (Smc1, Smc3, the kleisin Scc1/Rad21 and SA1 or SA2) that holds sister chromatids together from S phase until anaphase by topologically entrapping both sister DNAs, and that in interphase extrudes chromatin loops. **Condensin** is the related complex (Smc2, Smc4, a kleisin and two HEAT-repeat subunits) that compacts and individualizes mitotic chromatids by loop extrusion; vertebrates have condensin II, which acts in the nucleus from prophase, and condensin I, which gains access to chromosomes after nuclear envelope breakdown.

Cohesion is established during replication (Section 20.4.3 of [7.3.20](/7.3.20#sec-20.4.3)): cohesin rings loaded in G1 come to embrace both sisters as the fork passes, and acetylation of Smc3 with the binding of sororin prevents the releasing factor Wapl from opening them. Topoisomerase II removes the remaining catenation of the sister DNAs during G2 and prophase. In vertebrates cohesin is then removed in two steps: in prophase, phosphorylation of SA2 and sororin by Plk1, Aurora B and Cdk1 lets Wapl open the rings on the arms (the prophase pathway), while at centromeres shugoshin (Sgo1) recruits the phosphatase PP2A-B56, which keeps cohesin dephosphorylated and protected; at anaphase onset separase cleaves the Scc1 subunit of the cohesin that remains. Two-step removal resolves the arms early, which helps condensin to separate them, and keeps the strongest cohesion where it is needed, at the centromeres, which resist the poleward pull on the kinetochores and generate tension. Yeasts lack the prophase pathway and cleave all their cohesin at anaphase.

Condensation is not merely shortening. The arms of human mitotic chromatids are about 10 000 times shorter than the DNA they contain, and condensin compacts each chromatid into a stiff rod whose loops are anchored to a central axis, so that the two sisters become separate, untangled bodies that can be pulled apart without breaking. Cells depleted of condensin still condense their chromosomes partly but form floppy chromatids that stretch and bridge in anaphase.

![Cohesin and the cycle of sister-chromatid cohesion. A: cohesin is a ring of about 50 nm formed by the long coiled-coil arms of Smc1 and Smc3, joined at a hinge and at their ATPase heads, which are bridged by the kleisin Scc1 (Rad21) bound to SA1 or SA2; cohesive cohesin entraps the two sister DNAs, and separase opens the ring by cutting Scc1. B: cohesion through the cycle. In G1, cohesin is loaded by Scc2–Scc4 and released again by Wapl (grey rings, dynamic). In S and G2 it entraps both sisters and becomes cohesive (acetylated Smc3, sororin). In prophase the prophase pathway (Plk1-dependent phosphorylation and Wapl) removes cohesin from the arms (dashed rings), while shugoshin–PP2A (yellow) protects it at the centromere. In metaphase the sisters are held mainly at the centromere and their kinetochores are under tension. In anaphase separase cleaves the remaining Scc1 (red cross) and the sisters move apart](./plots/cohesin-cycle.py)

## 21.2. The Mitotic Spindle

### 21.2.1. Three Classes of Microtubules

**Definition 21.2.1 (Mitotic Spindle)** The **mitotic spindle** is the bipolar array of microtubules and associated proteins that segregates the chromosomes. Its microtubules have their minus ends at or near the two poles and fall into three classes: **kinetochore microtubules**, whose plus ends are embedded in kinetochores and which are bundled into kinetochore fibers (K-fibers); **interpolar microtubules** (non-kinetochore microtubules), the most numerous class, which overlap antiparallel at the spindle equator and give the spindle its structure; and **astral microtubules**, which radiate from the poles toward the cell cortex and position the spindle.

A metaphase spindle of a mammalian cell is about $10$–$15\,\mu\mathrm{m}$ long and contains tens of thousands of microtubules, most of which turn over in seconds: non-kinetochore microtubules have half-lives of 15–30 s, about ten times shorter than in interphase, because M-Cdk and Aurora kinases raise the catastrophe frequency and lower the rescue frequency (MAPs are phosphorylated, the depolymerizing kinesin-13 MCAK and kinesin-8 are active). The spindle is therefore a steady state, not a fixed structure: tubulin subunits in kinetochore fibers flow continuously toward the poles (poleward flux), at about $0.5$–$2\,\mu\mathrm{m\,min^{-1}}$ depending on the cell, adding at plus ends and leaving at minus ends.

### 21.2.2. The Centrosome Cycle and Pole Separation

Most animal cells enter mitosis with two centrosomes, produced by the once-per-cycle duplication started at G1/S ([7.3.20](/7.3.20#sec-20.4.3); structure of centrosomes and centrioles in [7.3.14](/7.3.14#sec-14.3.2)). In late G2 the centrosomes mature: they recruit more pericentriolar material and γ-tubulin ring complexes, which multiplies their nucleating capacity several-fold, under the control of Plk1 and Aurora A. At the G2/M transition the linker between them is dissolved (Nek2 phosphorylates the linker proteins) and they move to opposite sides of the nucleus, pushed by kinesin-5 sliding the antiparallel microtubules between them and pulled by dynein on the nuclear envelope and the cortex. Inhibiting kinesin-5 with the small molecule monastrol prevents separation, so the cell forms a monopolar spindle, a rosette of chromosomes around a single pair of centrosomes.

### 21.2.3. Motors and Forces

The spindle is held in shape by a balance of opposing motor forces acting on its microtubules (figure below):

| Motor | Direction | Location | Effect |
|---|---|---|---|
| Kinesin-5 (Eg5) | plus end; bipolar tetramer | antiparallel overlaps | slides interpolar microtubules apart: pushes poles outward; essential for bipolarity |
| Kinesin-14 (HSET, Ncd) | minus end | cross-links antiparallel microtubules | pulls poles together; focuses minus ends |
| Cytoplasmic dynein with dynactin and NuMA | minus end | at the poles; at the cortex; on unattached kinetochores | focuses poles; pulls astral microtubules and the poles toward the cortex; moves chromosomes poleward during capture |
| Kinesin-4/10 (chromokinesins) | plus end | chromosome arms | push arms away from the poles (polar ejection force) |
| Kinesin-7 (CENP-E) | plus end | kinetochores | slides laterally attached chromosomes toward the equator (congression) |
| Kinesin-13 (MCAK), kinesin-8 (Kif18A) | depolymerases | microtubule ends, kinetochores | regulate microtubule length; damp chromosome oscillations |

Forces on the chromosomes come from three sources: depolymerization of kinetochore microtubules at their plus ends, which pulls the kinetochore poleward without needing ATP at the kinetochore; poleward flux, which carries the whole fiber toward the pole; and the polar ejection force. In metaphase the poleward forces on the two sister kinetochores are balanced against each other through cohesin, so a bi-oriented pair is stretched: the distance between sister kinetochores increases from about $0.7\,\mu\mathrm{m}$ at rest to $1$–$1.5\,\mu\mathrm{m}$ under tension. The length of the spindle is set by the balance between kinesin-5 and kinesin-14 and dynein, and between nucleation, transport and depolymerization; in *Xenopus* extracts, where cytoplasm can be confined in droplets of controlled size, spindle length scales with the volume of cytoplasm available, a limiting-component mechanism like those of organelle size ([7.3.6](/7.3.6)).

![The mitotic spindle and its forces. A: a metaphase spindle in an animal cell. Kinetochore microtubules, bundled into K-fibers, run from the spindle poles (centrosomes) to the kinetochores of the bi-oriented chromosomes; interpolar microtubules overlap at the equator; astral microtubules radiate to the cortex. Arrows show the main forces: kinesin-5 slides interpolar microtubules apart, cortical dynein pulls the astral microtubules and poles outward, chromokinesins on the chromosome arms push them away from the poles (polar ejection), and depolymerization at the kinetochore together with poleward flux pulls each kinetochore toward its pole, resisted by cohesin, so that sister kinetochores are under tension. B: idealized kinematics of anaphase in a mammalian cell. After anaphase onset, kinetochores approach their poles at about 1 µm per minute (anaphase A) while, starting slightly later, the poles move apart from about 12 to about 22 µm (anaphase B)](./plots/spindle-forces.py)

### 21.2.4. Assembling a Spindle: Search and Capture and Self-Organization

How do microtubules growing from two poles find the 92 kinetochores scattered through a nucleus that has just broken down? Kirschner and Mitchison (1986) proposed that they do not need to be guided: dynamic instability lets each pole explore space by repeated trials.

**Definition 21.2.2 (Search-and-Capture Model)** The **search-and-capture model** of spindle assembly holds that microtubules nucleated at the spindle poles grow in random directions, undergo catastrophe and shrink if they miss a target, and are stabilized when their plus ends are captured by a kinetochore, so that dynamic instability alone allows the poles to search the cytoplasm and attach every chromosome.

The idea can be made quantitative (Holy and Leibler 1994). Suppose each pole keeps $n$ microtubules, each growing at speed $v_{\mathrm{g}}$ in a random direction, undergoing catastrophe at rate $f$ without rescue, shrinking at $v_{\mathrm{s}}$ and being renucleated. A kinetochore with capture radius $a$ at distance $d$ is hit in one growth phase with probability $(a/2d)^2\,\mathrm{e}^{-fd/v_{\mathrm{g}}}$, the fraction of directions that point at it times the probability of growing that far. One growth–shrinkage cycle lasts $(1/f)(1 + v_{\mathrm{g}}/v_{\mathrm{s}})$ on average, so the capture rate of one kinetochore is

$$
\lambda(f, d) = \frac{n f}{1 + v_{\mathrm{g}}/v_{\mathrm{s}}}\left(\frac{a}{2d}\right)^2 \mathrm{e}^{-fd/v_{\mathrm{g}}}.
\tag{21.1}
$$

**Proposition 21.2.1 (Optimal Catastrophe Frequency)** For fixed $n$, $v_{\mathrm{g}}$, $v_{\mathrm{s}}$, $a$ and $d$, the capture rate (21.1) is maximal when $f = v_{\mathrm{g}}/d$, that is, when the mean length of a growing microtubule equals the distance to the target.

**Proof** As a function of $f$, $\lambda$ is proportional to $f\,\mathrm{e}^{-fd/v_{\mathrm{g}}}$, whose derivative $\mathrm{e}^{-fd/v_{\mathrm{g}}}(1 - fd/v_{\mathrm{g}})$ vanishes only at $f = v_{\mathrm{g}}/d$ and changes sign from positive to negative there. $\square$

Too few catastrophes waste time on microtubules that grow far in wrong directions; too many kill microtubules before they arrive. With realistic numbers ($n = 250$, $v_{\mathrm{g}} = 0.2\,\mu\mathrm{m\,s^{-1}}$, $a = 0.25\,\mu\mathrm{m}$, $d$ = 4–10 µm) the mean capture time of a single kinetochore is tens of minutes, and capturing all 92, a maximum of 92 waiting times, takes hours (figure below). Human cells complete prometaphase in 10–20 minutes, so unbiased search is too slow (Wollman et al. 2005). Several mechanisms bias and accelerate it:

1. The RanGTP gradient. Chromosomes carry RCC1, the exchange factor of the GTPase Ran ([7.3.16](/7.3.16#sec-16.5.3)), so RanGTP is high around chromatin. RanGTP releases spindle assembly factors such as TPX2 and NuMA from importins; TPX2 activates Aurora A and nucleation, and microtubules near chromosomes are stabilized. Microtubules growing toward chromosomes therefore survive longer.
2. Kinetochore- and chromatin-nucleated microtubules. Short microtubules form near kinetochores and are later incorporated into the spindle and captured by pole microtubules, and augmin nucleates new microtubules on the sides of existing ones with the same polarity, amplifying the number of plus ends within the spindle.
3. Lateral capture and the corona. Unattached kinetochores expand a fibrous corona (dynein, CENP-E, the RZZ complex and Mad1–Mad2) that enlarges the target several-fold and captures microtubule walls, after which dynein moves the chromosome poleward and CENP-E toward the equator.
4. Prometaphase rosette. In human cells, chromosomes move to a ring around the spindle shortly after nuclear envelope breakdown, which shortens and equalizes the distances to be searched.

In cells without centrosomes, such as higher-plant cells and the oocytes of many animals, the spindle self-organizes from the chromosomes: microtubules nucleated around chromatin are sorted by kinesin-5 into antiparallel bundles and their minus ends focused into poles by dynein and kinesin-14. Centrosomes accelerate assembly and supply astral microtubules for positioning, but they are not required to build a bipolar spindle: flies without centrioles develop to adulthood, though their divisions are slower and less accurate.

![Search and capture, Eq. (21.1). A: capture rate of one kinetochore as a function of the catastrophe frequency for targets at 4, 7 and 10 µm (250 microtubules per pole, growth 0.2 µm per s, shrinkage 0.3 µm per s, capture radius 0.25 µm); each curve peaks at f = v_g/d (circles, Proposition 21.2.1). B: fraction of the 92 kinetochores of a human cell captured over time (distances drawn uniformly from 4 to 10 µm, f = 0.03 per s; mean of 200 simulated cells) for unbiased search, for search with a RanGTP zone of 3 µm around the chromosomes in which catastrophes are suppressed, and for the zone combined with the expanded corona of unattached kinetochores (capture radius 0.6 µm). Dashed lines mark the median time at which the last kinetochore is captured; the shaded band is the 10–20 minutes that prometaphase actually takes. Random search alone needs hours, and even the biased versions leave a gap that kinetochore-nucleated microtubules and chromosome movements close](./plots/search-capture.py)

## 21.3. Kinetochores and Attachment

### 21.3.1. The Kinetochore

**Definition 21.3.1 (Kinetochore)** A **kinetochore** is the protein complex assembled on the **centromere** of each sister chromatid that attaches the chromatid to spindle microtubules, couples chromosome movement to the growth and shortening of their plus ends, and generates the signal of the spindle assembly checkpoint. It is built on centromeric nucleosomes containing the histone H3 variant CENP-A; the inner kinetochore (the 16-protein constitutive centromere-associated network, CCAN, including CENP-C and CENP-T) binds this chromatin, and the outer kinetochore (the KMN network of Knl1, the Mis12 complex and the Ndc80 complex) binds microtubules.

Kinetochores are specified epigenetically: the position of CENP-A nucleosomes, not the DNA sequence, marks the centromere, and new CENP-A is deposited next to old CENP-A in G1 ([7.3.17](/7.3.17#sec-17.2.1)). A budding yeast kinetochore, on a 125 bp point centromere with one CENP-A nucleosome, binds a single microtubule; a human kinetochore, on a regional centromere of megabases of α-satellite repeats, binds 15–25 microtubules. The Ndc80 complex is a $60\,\mathrm{nm}$ rod whose calponin-homology domains bind the microtubule wall near the plus end, at the junction between tubulin subunits, and whose disordered N-terminal tail strengthens the binding when it is not phosphorylated. Many weak Ndc80 contacts let the kinetochore hold on to a microtubule end that is growing or shrinking, by a kind of biased diffusion: as the end shortens, the kinetochore slides to maintain the larger number of contacts, and so it is pulled toward the pole. Purified kinetochores in a test tube follow depolymerizing microtubule ends without ATP (Koshland, Mitchison and Kirschner 1988); in yeast the ring-shaped Dam1 complex, and in vertebrates the Ska complex, help couple the kinetochore to the curling protofilaments of the shrinking end.

### 21.3.2. Bi-Orientation by Trial and Error

Sister kinetochores sit back to back, which favors attachment to opposite poles, but errors are common in prometaphase:

| Attachment | Description | Tension | Consequence |
|---|---|---|---|
| Unattached | neither sister attached | none | checkpoint signal |
| Monotelic | one sister attached | low | checkpoint signal; common early in prometaphase |
| Syntelic | both sisters to the same pole | low | corrected by Aurora B |
| Merotelic | one kinetochore attached to both poles | yes | not detected by the checkpoint; a lagging chromosome in anaphase; main source of chromosome missegregation in cultured human cells |
| Amphitelic | sisters to opposite poles (bi-orientation) | high | stable; correct |

Bruce Nicklas showed with a micromanipulation needle in grasshopper spermatocytes that tension itself stabilizes attachments: pulling on a wrongly attached chromosome to create tension made the attachment stable, whereas releasing tension made it detach (Nicklas and Koch 1969). The kinase that destabilizes tensionless attachments is Aurora B.

**Definition 21.3.2 (Aurora B)** **Aurora B** is a Ser/Thr protein kinase that, with INCENP, survivin and borealin, forms the chromosomal passenger complex, which is located at the inner centromere from prophase to metaphase and moves to the spindle midzone in anaphase. At the centromere it phosphorylates outer-kinetochore proteins, above all the N-terminal tail of Ndc80, reducing their affinity for microtubules and so releasing attachments that are not under tension; at the midzone it controls cytokinesis.

In the spatial separation model, Aurora B at the inner centromere phosphorylates substrates within its reach. When the sisters are not under tension, the outer kinetochore is close to the inner centromere and is phosphorylated, so the attachment is released and the kinetochore tries again; when bi-orientation stretches the kinetochore, the microtubule-binding sites move out of reach, PP1 and PP2A-B56 dephosphorylate them, and the attachment is stabilized and recruits more microtubules into a full K-fiber. Tension also acts directly: the binding of kinetochore proteins to microtubules behaves as a catch bond that lasts longer under moderate force (Akiyoshi et al. 2010). The relative importance of the two mechanisms is still debated. Correction requires a period of instability, which is why microtubules in prometaphase turn over so fast.

![The kinetochore, kinds of attachment and error correction. A: layers of a human kinetochore: centromeric chromatin with CENP-A nucleosomes (yellow), the inner kinetochore (CCAN, with CENP-C and CENP-T) and the outer kinetochore (KMN network), whose rod-shaped Ndc80 complexes bind the sides of the microtubule near its embedded plus end; Aurora B sits at the inner centromere between the sisters. B: attachment states of a pair of sister kinetochores: unattached and monotelic attachments generate the checkpoint signal; syntelic attachments lack tension and are corrected; merotelic attachments are under tension and escape the checkpoint; amphitelic attachment (bi-orientation) is the stable, correct state. C: the spatial separation model of tension sensing. Without tension the outer kinetochore lies within reach of Aurora B (shaded), which phosphorylates Ndc80 and weakens binding, so the attachment is released; under tension the outer kinetochore is pulled out of reach, Ndc80 is dephosphorylated and the attachment is stabilized](./plots/kinetochore-attachment.py)

### 21.3.3. The Spindle Assembly Checkpoint

Drugs that depolymerize microtubules (colchicine, nocodazole) or stabilize them (paclitaxel, taxol) arrest cells in mitosis for hours. Genetic screens in budding yeast for mutants that failed to arrest in the microtubule poison benomyl identified the *MAD* (mitotic arrest deficient) and *BUB* (budding uninhibited by benzimidazole) genes (Hoyt et al. 1991; Li and Murray 1991).

**Definition 21.3.3 (Spindle Assembly Checkpoint)** The **spindle assembly checkpoint** (SAC, mitotic checkpoint) is the signaling pathway that prevents the metaphase-to-anaphase transition until every kinetochore is attached to spindle microtubules. Unattached kinetochores catalyze the formation of the **mitotic checkpoint complex** (MCC), made of Cdc20 bound to the closed conformer of **Mad2**, BubR1 (Mad3 in yeast) and Bub3, which binds APC/C–Cdc20 and blocks the ubiquitylation of securin and cyclin B.

Mad2 is a protein with two stable folds. Open Mad2 (O-Mad2) is free; closed Mad2 (C-Mad2) wraps its "safety belt" around a peptide of its ligand, Mad1 or Cdc20. At an unattached kinetochore, recruited there by the kinase Mps1, Bub1 and the RZZ complex, a Mad1–C-Mad2 complex acts as a template: it binds O-Mad2 from the cytosol and catalyzes its conversion to C-Mad2 bound to Cdc20, which then joins BubR1–Bub3 to form the MCC (the template model; De Antoni et al. 2005). Attached kinetochores lose Mad1–Mad2 (stripped off by dynein along the attached microtubules), and the MCC is continuously disassembled in the cytosol by p31comet and the AAA ATPase TRIP13. The checkpoint is remarkably sensitive: Rieder and colleagues showed that a single unattached kinetochore delays anaphase, and that destroying it with a laser beam lets the cell enter anaphase on schedule (Rieder et al. 1995). Anaphase starts about 20 minutes after the last kinetochore attaches.

This behavior can be captured in a small model. Let $I$ be the fraction of Cdc20 held in the MCC, $U$ the number of unattached kinetochores and $S$ the level of securin:

$$
\begin{aligned}
\frac{\mathrm{d}I}{\mathrm{d}t} &= (k_{\mathrm{u}}U + k_{\mathrm{amp}}I)(1 - I) - k_{\mathrm{off}}I, \\
\frac{\mathrm{d}S}{\mathrm{d}t} &= k_{\mathrm{s}} - \left(k_{\mathrm{d}0} + k_{\mathrm{d}}(1 - I)\right)S,
\end{aligned}
\tag{21.2}
$$
where $k_{\mathrm{u}}$ is the catalytic activity of one kinetochore template, $k_{\mathrm{amp}}$ a possible amplification of MCC formation in solution, $k_{\mathrm{off}}$ the rate of MCC disassembly, and $1 - I$ the active fraction of APC/C–Cdc20. With $k_{\mathrm{u}} = 5$, $k_{\mathrm{amp}} = 0.3$ and $k_{\mathrm{off}} = 0.5\,\mathrm{min^{-1}}$, a single unattached kinetochore keeps about 90% of Cdc20 inhibited. Two design constraints follow. The template must be strong (large $k_{\mathrm{u}}/k_{\mathrm{off}}$), or one kinetochore would not suffice; and amplification in solution must be weaker than disassembly ($k_{\mathrm{amp}} < k_{\mathrm{off}}$), or the MCC would sustain itself after the last attachment and the checkpoint could never be switched off. The second constraint is why MCC disassembly by p31comet and TRIP13 is essential, and the disassembly rate sets the delay between the last attachment and anaphase.

![A minimal model of the spindle assembly checkpoint, Eq. (21.2). A: a simulated prometaphase in which 91 kinetochores attach at random times within 25 minutes of nuclear envelope breakdown and the last one attaches at 30 minutes (grey: number of unattached kinetochores, right axis). While a single kinetochore remains unattached, active APC/C–Cdc20 stays below 10% and securin stays high; after the last attachment the MCC disassembles, APC/C–Cdc20 becomes active and securin is destroyed, and anaphase (securin below 10%) follows about 14 minutes later. B: steady-state APC/C–Cdc20 activity as a function of the number of unattached kinetochores for a strong and a weak kinetochore template: only a strong catalytic template lets one kinetochore hold the checkpoint on](./plots/sac-model.py)

The checkpoint has limits. It detects attachment, not correct attachment, so merotelic attachments escape it. It cannot hold cells forever: during a prolonged arrest cyclin B is slowly degraded despite the checkpoint, and cells eventually exit mitosis without dividing (mitotic slippage), becoming tetraploid; whether a cancer cell treated with taxol or vinca alkaloids dies in mitosis or slips out determines the success of these drugs ([7.3.26](/7.3.26)). Mutations that weaken the checkpoint cause aneuploidy; complete loss of it is lethal in mammalian cells.

## 21.4. Chromosome Segregation

### 21.4.1. Anaphase A and Anaphase B

When APC/C–Cdc20 destroys securin and cyclin B, separase cleaves the remaining cohesin and the sisters, released together within a minute, begin to move apart.

**Definition 21.4.1 (Anaphase A and Anaphase B)** **Anaphase A** is the movement of the separated chromatids toward the spindle poles, accompanied by shortening of the kinetochore microtubules. **Anaphase B** is the separation of the spindle poles themselves, accompanied by elongation of the interpolar microtubules and of the spindle.

Anaphase A is driven mainly by depolymerization at the kinetochore (the "Pac-Man" mechanism, in which the kinetochore holds on to a shrinking end) and by poleward flux with depolymerization at the poles; their relative contributions vary, flux dominating in *Xenopus* extract spindles and kinetochore depolymerization in human cells. Chromosomes move at about $1\,\mu\mathrm{m\,min^{-1}}$, a speed set by microtubule depolymerization rather than by motor velocity, against a viscous drag so small (on the order of $0.1\,\mathrm{pN}$) that a single motor could provide it; the spindle can generate forces of hundreds of piconewtons per chromosome when obstructed (Nicklas 1983), so it is a strongly overpowered, speed-governed machine. Anaphase B is driven by kinesin-5 and other kinesins sliding the antiparallel midzone microtubules apart while they polymerize, and by cortical dynein pulling on astral microtubules. Mammalian spindles about double in length in anaphase B, while yeast spindles, which rely almost entirely on anaphase B, elongate up to fifteenfold. The completion of anaphase requires cyclin B destruction: dephosphorylation of Cdk substrates stabilizes the midzone, relocates the chromosomal passenger complex and the phosphatases and allows the spindle to elongate normally.

### 21.4.2. Telophase and the Re-formation of Nuclei

In telophase the chromosomes cluster at the poles and decondense, and nuclear envelopes form around them from the ER: membrane sheets carrying inner-nuclear-membrane proteins bind chromatin through BAF and LEM-domain proteins, nuclear pores assemble, gaps around spindle microtubules are sealed by ESCRT-III with spastin, and the lamina re-forms (details in [7.3.16](/7.3.16#sec-16.6.3)). The chromosome periphery protein Ki-67 keeps chromosomes separate as surfactant-like brushes in prometaphase and then helps cluster them in telophase, so that a single nucleus forms around each set. A chromosome that lags behind in anaphase may be enclosed in its own small nuclear envelope, a micronucleus, whose fragile envelope often ruptures; the DNA inside is then damaged and can be shattered and rejoined in a single catastrophic event (chromothripsis), a source of the complex rearrangements of cancer genomes ([7.3.26](/7.3.26)).

## 21.5. Cytokinesis

### 21.5.1. The Contractile Ring and Its Position

**Definition 21.5.1 (Cytokinesis and the Contractile Ring)** **Cytokinesis** is the division of the cytoplasm of a cell into two daughter cells, normally after mitosis. In animal and fungal cells it is carried out by the **contractile ring**, a band of actin filaments, bipolar myosin II filaments and associated proteins (anillin, septins) that assembles under the plasma membrane at the cell equator in anaphase and constricts it to form a cleavage furrow.

The ring must form at the right time (after the chromosomes have separated) and in the right place (between them). Its position is specified by the anaphase spindle, as classic experiments on marine eggs showed: when Rappaport (1961) pushed a glass bead through a sand dollar egg to make it horseshoe-shaped, a furrow formed not only between the asters with a spindle between them but also between two asters that shared no spindle, so the asters alone can signal a furrow. Three mechanisms, the subject of the course slides' "three models", are now known to combine:

1. Central spindle stimulation. In anaphase the chromosomal passenger complex and centralspindlin (the kinesin-6 MKLP1 with the RhoGAP Cyk4) accumulate on the antiparallel overlaps of the spindle midzone; centralspindlin binds and activates the RhoGEF Ect2.
2. Astral stimulation. Astral microtubules deliver activators to the equatorial cortex, where the asters of the two poles overlap, as in Rappaport's experiment.
3. Polar relaxation. Astral microtubules near the poles inhibit cortical contractility, so the equator, farthest from both poles, contracts.

All three converge on the small G protein RhoA. Ect2 activates RhoA in a narrow equatorial zone of the cortex; RhoA-GTP activates formins, which nucleate the long unbranched actin filaments of the ring ([7.3.13](/7.3.13#sec-13.3.2)), and the Rho kinase ROCK and citron kinase, which phosphorylate the regulatory light chain of myosin II and activate it; anillin and septins scaffold the ring on the membrane. Cdk1 inhibits Ect2 and myosin II until anaphase, which is how the fall of Cdk activity times cytokinesis. As the ring constricts, at a roughly constant rate, it loses material, remaining about as thick as it was, and new membrane is added from vesicles of the recycling endosomes and Golgi, because a sphere dividing into two spheres of half its volume needs about 26% more surface ($2^{1/3} - 1$).

### 21.5.2. The Midbody and Abscission

**Definition 21.5.2 (Midbody and Abscission)** The **midbody** is the dense structure at the center of the intercellular bridge left at the end of furrowing, formed by the compacted antiparallel microtubules of the central spindle with centralspindlin, the chromosomal passenger complex and the protein CEP55. **Abscission** is the final cutting of this bridge, by which the two daughter cells separate.

The bridge, about $1\,\mu\mathrm{m}$ wide, can persist for an hour or more. CEP55 recruits ALIX and TSG101, which nucleate polymers of ESCRT-III subunits (CHMP4B and others) that form helices beside the midbody, constrict the membrane to the point of scission and are remodeled by the ATPase VPS4; the microtubules are cut by spastin. This is the same membrane-scission machinery that buds intralumenal vesicles in the **ESCRT** pathway of the endosome ([7.3.10](/7.3.10)) and reseals the nuclear envelope, and it acts on membrane necks in the topology opposite to that of dynamin. If a chromatin bridge or a lagging chromosome remains in the midbody, Aurora B delays abscission (the abscission checkpoint), preventing the chromatin from being cut. The midbody remnant is inherited by one daughter or released, and has been reported to carry signals that influence cell fate.

### 21.5.3. Cytokinesis in Plant Cells

Plant cells are enclosed by a rigid wall and cannot furrow; they build a new wall from the inside out.

**Definition 21.5.3 (Preprophase Band, Phragmoplast and Cell Plate)** The **preprophase band** is a cortical ring of microtubules and actin filaments that forms in G2 in the cells of land plants and marks the future division plane; it disassembles before metaphase but leaves a cortical division zone. The **phragmoplast** is the array of antiparallel microtubules and actin filaments that forms from spindle remnants in telophase, with plus ends overlapping at the equator, along which Golgi-derived vesicles are carried to the division plane. The **cell plate** is the new wall-to-be formed by fusion of these vesicles in the phragmoplast; it expands centrifugally as the phragmoplast moves outward, and fuses with the parental wall at the cortical division zone.

The cell plate begins as a tubular network of fused vesicles filled with callose and pectins, which is later replaced by cellulose and matures into the middle lamella and primary walls of the two daughters ([7.3.23](/7.3.23)); plasmodesmata form where ER strands are trapped in it. Because plant cells cannot move, the orientation of division planes set by the preprophase band, together with the direction of cell expansion, determines the shape of the plant body ([7.12](/7.12)). Plant spindles have no centrosomes and assemble around the chromosomes from microtubules nucleated on the nuclear surface.

![Cytokinesis. A: in an animal cell in anaphase, centralspindlin with Ect2 at the overlaps of the spindle midzone (green dots) signals to the equatorial cortex, while astral microtubules inhibit contractility at the poles; a narrow zone of RhoA-GTP (pink) forms at the equator, and RhoA activates formins (actin filament assembly) and ROCK (myosin II activation), so that the contractile ring (dark red) assembles and contracts. B: abscission: after furrowing the daughters remain connected by a narrow bridge around the midbody; ESCRT-III polymerizes as a helix beside the midbody and constricts and cuts the membrane. C: a plant cell in telophase: the phragmoplast, two sets of microtubules with their plus ends at the equator, guides Golgi-derived vesicles (beige) to the cell plate (green), which grows outward (arrows) to fuse with the parental wall at the site marked earlier by the preprophase band (yellow)](./plots/cytokinesis.py)

### 21.5.4. Mitosis Without Cytokinesis, and Organelle Inheritance

Nuclear division is not always followed by cytokinesis. The *Drosophila* embryo runs 13 nuclear cycles in a syncytium before a single round of cellularization encloses some 6000 nuclei at once; mammalian megakaryocytes, many hepatocytes and cardiomyocytes become binucleate or polyploid; the plasmodium of *Physarum* contains millions of synchronously dividing nuclei. Failure of cytokinesis in a proliferating cell produces a tetraploid cell with two centrosomes, which in later divisions can form multipolar spindles; p53 normally arrests such cells ([7.3.22](/7.3.22)), and tetraploidization is a frequent step in the evolution of aneuploid tumors.

Organelles that cannot be made anew are partitioned with the cytoplasm. Mitochondria and chloroplasts, present in many copies, are inherited approximately evenly by chance ([7.3.12](/7.3.12)); the ER remains continuous and is cut by the furrow; the Golgi apparatus fragments in prophase into vesicles and clusters that are distributed with the spindle poles and reassembled in each daughter. Budding yeast, which divides asymmetrically, actively transports organelles into the bud along actin cables with myosin V ([7.3.13](/7.3.13)).

## 21.6. Asymmetric Cell Division

**Definition 21.6.1 (Asymmetric Cell Division)** An **asymmetric cell division** is a division that produces two daughter cells that differ in size, in the cytoplasmic components they inherit, or in their fates. It requires a polarity axis in the mother cell, the asymmetric localization of cell-fate determinants along it, and an orientation of the spindle that places the cleavage plane so that the determinants go to one daughter.

The mechanism is best understood in two systems:

- The *C. elegans* zygote. The sperm centrosome marks the posterior pole and triggers the segregation of PAR proteins into an anterior domain (PAR-3, PAR-6, PKC-3) and a posterior domain (PAR-1, PAR-2) by cortical flow and mutual inhibition ([7.3.15](/7.3.15#sec-15.4.2)). The spindle is then displaced toward the posterior because cortical force generators, Gα with GPR-1/2 and LIN-5 anchoring dynein, are more active on the posterior cortex and pull harder on the astral microtubules. The first division gives a larger anterior AB cell and a smaller posterior P1 cell that inherits the germline P granules.
- *Drosophila* neuroblasts. The Par complex (Bazooka, Par-6, aPKC) at the apical cortex recruits Inscuteable, Pins (LGN in mammals) and Gαi, which bind Mud (NuMA) and dynein and orient the spindle along the apical–basal axis. aPKC phosphorylates the determinants Numb, Prospero and Brat, which are excluded from the apical cortex and, with their adaptors Miranda and Partner of Numb, segregate to the basal cortex. The large apical daughter remains a neuroblast; the small basal daughter, a ganglion mother cell, inherits Prospero, which enters its nucleus and stops self-renewal, and Numb, which inhibits Notch signaling. Mutations that mislocalize these determinants make neuroblasts overproliferate and form tumors.

Asymmetry can also be imposed from outside, by the orientation of division relative to a signaling niche. A stem cell that divides perpendicular to its niche keeps one daughter in contact with the niche signals and pushes the other away to differentiate. In the *Drosophila* testis the mother centrosome remains anchored near the hub cells of the niche and is always inherited by the germline stem cell (Yamashita et al. 2007); in cultured mouse embryonic stem cells, a bead carrying immobilized Wnt3a orients the spindle, and the daughter next to the bead retains the Wnt response and pluripotency, while the distal daughter begins to differentiate (Habib et al. 2013). In the intestinal crypt, Paneth cells supply Wnt to the neighboring Lgr5 stem cells. The roles of these divisions in stem-cell maintenance are the subject of [7.3.24](/7.3.24), and their use in embryos that of [7.5](/7.5).

## 21.7. The Cell Mechanics of Meiosis

### 21.7.1. Two Divisions After One Replication

**Definition 21.7.1 (Meiosis)** **Meiosis** is the specialized pair of nuclear divisions by which a diploid cell produces haploid nuclei: after one round of DNA replication, homologous chromosomes pair, recombine and separate in meiosis I, and sister chromatids separate in meiosis II without an intervening S phase.

Meiosis uses the same machines as mitosis (cohesin, kinetochores, spindles, APC/C, separase) with four changes that make homologues, rather than sisters, segregate first:

| Feature | Mitosis | Meiosis I | Meiosis II |
|---|---|---|---|
| Pairing of homologues | none | pair, synapse, recombine | none |
| Link that resists spindle forces | sister cohesion at centromeres | chiasmata + arm cohesion | centromeric cohesion |
| Sister kinetochores | bi-oriented | co-oriented (fused, same pole) | bi-oriented |
| Cohesin cleaved at anaphase | all remaining (Scc1) | arm cohesin (Rec8); centromeric protected | centromeric (Rec8) |
| Separated | sister chromatids | homologues | sister chromatids |
| Products | two diploid cells, identical | two cells with one (replicated) homologue each | four haploid cells, each different |
| Replication before | S phase | premeiotic S phase | none (Cdk kept partly active between the divisions) |

The meiotic kleisin Rec8 replaces Scc1, and its cleavage by separase requires its prior phosphorylation (by casein kinase 1 and DDK), which is what lets a phosphatase protect it.

### 21.7.2. Pairing, Synapsis and Crossing-Over

Meiotic prophase I is long (hours in yeast, days in mice, weeks in plants; in human oocytes it is interrupted for decades) and is divided into five stages by the behavior of the homologues. The cohesin-rich axes of the replicated homologues condense in leptotene, and the topoisomerase-like enzyme Spo11 makes hundreds of programmed double-strand breaks, concentrated at hotspots (set by PRDM9 in most mammals). The broken ends invade the homologous chromosome, which is how homologues find each other in most organisms; in many species the telomeres cluster on the nuclear envelope in a "bouquet", moved by LINC complexes ([7.3.16](/7.3.16#sec-16.2.3)) and cytoplasmic motors, which shakes the chromosomes and helps align them.

**Definition 21.7.2 (Synaptonemal Complex, Bivalent and Chiasma)** The **synaptonemal complex** is the zipper-like protein structure that holds the axes of paired homologous chromosomes about $100\,\mathrm{nm}$ apart along their length in pachytene of meiosis I, formed by lateral elements on the homologue axes joined by transverse filaments (SYCP1 in mammals, Zip1 in yeast) through a central element. A pair of synapsed or chiasma-linked homologues, with four chromatids, is a **bivalent** (tetrad). A **chiasma** is the cross-shaped connection between non-sister chromatids of the two homologues, visible from diplotene after the synaptonemal complex disassembles, that is the cytological result of a crossover.

| Stage | Events |
|---|---|
| Leptotene | axes form; Spo11 double-strand breaks; homology search |
| Zygotene | synapsis begins at sites of recombination; bouquet |
| Pachytene | complete synapsis; crossovers are completed in recombination nodules |
| Diplotene | synaptonemal complex disassembles; homologues held by chiasmata; long arrest of oocytes (dictyate) with active transcription (lampbrush chromosomes, [7.3.17](/7.3.17#sec-17.5.2)) |
| Diakinesis | chromosomes condense further; nuclear envelope breaks down |

The synaptonemal complex is not required for homology recognition or for initiating recombination, but it is needed to complete most crossovers and to space them (crossover interference: a crossover inhibits others nearby). Most breaks are repaired without crossover (as noncrossovers), but every bivalent receives at least one crossover, the obligatory crossover, and in humans usually two or three; the enzymology of how double Holliday junctions are resolved as crossovers is described with **homologous recombination** in [7.2.9](/7.2.9). For the cell, the point of crossing over is mechanical: a chiasma, combined with cohesion between the sister chromatid arms distal to it, ties the two homologues together, so that they can bi-orient on the meiosis I spindle exactly as sister kinetochores do in mitosis. A bivalent without a chiasma (an achiasmate bivalent) falls apart into two univalents that segregate at random, which is why mutants defective in recombination are sterile or produce aneuploid gametes. Checkpoints monitor recombination and synapsis in pachytene and eliminate defective spermatocytes and oocytes by apoptosis.

### 21.7.3. Co-orientation and the Protection of Centromeric Cohesion

Two adaptations make meiosis I reductional. First, the two sister kinetochores of each homologue are fused into a single unit that attaches to one pole (mono-orientation, or co-orientation).

**Definition 21.7.3 (Monopolin and Shugoshin)** **Monopolin** is the protein complex of budding yeast (Mam1, Csm1, Lrs4) that cross-links the sister kinetochores in meiosis I so that they attach to the same pole; in mammals the protein Meikin and in fission yeast Moa1 serve the same function. **Shugoshin** ("guardian spirit" in Japanese) is a centromeric protein that recruits PP2A-B56, which dephosphorylates centromeric cohesin and so protects it from separase: in meiosis I it preserves the centromeric Rec8 that holds sisters together until meiosis II, and in vertebrate mitosis (Sgo1) it protects centromeric cohesin from the prophase pathway.

At anaphase I, APC/C–Cdc20 activates separase, which cleaves phosphorylated Rec8 on the arms: the chiasmata slide off the ends of the chromosomes and the homologues separate, each still a pair of sisters joined at the centromere. Shugoshin is removed or redistributed after meiosis I, so that in meiosis II, as in mitosis, the sister kinetochores bi-orient and the centromeric cohesin is cleaved. Between the two divisions the cell does not replicate its DNA: it does not destroy all its cyclin B and keeps enough Cdk1 activity to prevent origin licensing, while still disassembling the spindle (in frog oocytes the Mos–MAP kinase pathway contributes).

![The cell mechanics of meiosis. A: prophase I of one pair of homologues (blue, paternal; red, maternal). In leptotene the homologues condense along protein axes and recombination begins; in zygotene the synaptonemal complex (grey rungs) starts to zip the axes together; in pachytene they are fully synapsed and crossovers mature in recombination nodules (yellow); in diplotene the synaptonemal complex disassembles and the homologues remain joined at a chiasma, where two non-sister chromatids have exchanged segments; in diakinesis the bivalent condenses further. B: at metaphase I the sister kinetochores of each homologue face the same pole (co-orientation) and the homologues bi-orient, held together by the chiasma and arm cohesion; at anaphase I arm cohesin is cleaved and the homologues separate while centromeric cohesin (yellow) is protected by shugoshin; at metaphase II the sisters bi-orient; at anaphase II the centromeric cohesin is cleaved and the sisters separate. C: an illustrative cohesion-decay model of the maternal age effect. If cohesin loaded before birth decays at 3.5% per year without replacement (dashed) and a bivalent missegregates when its cohesin falls below a threshold, with the starting amount varying between the 23 bivalents, the fraction of eggs with at least one missegregating bivalent rises from about 10% at 25 years to about half at 40, the shape of the observed increase](./plots/meiosis-mechanics.py)

### 21.7.4. Oocytes, Polar Bodies and Gametes

Gametogenesis is described as a developmental and physiological process in [7.5](/7.5) and [7.14](/7.14); the cell-biological points are these:

| | Spermatogenesis (human) | Oogenesis (human) |
|---|---|---|
| Timing | continuous from puberty; one round takes about 64–74 days | oocytes enter prophase I in the fetal ovary and arrest in diplotene (dictyate); one resumes meiosis at each ovulation, up to about 50 years later |
| Products of one meiosis | four spermatids of equal size, connected by cytoplasmic bridges until spermiogenesis | one egg and two or three polar bodies |
| Arrests | none prolonged | prophase I (decades); metaphase II until fertilization (CSF: Mos–MAPK–Emi2 inhibits APC/C) |
| Spindle | centrosomal | acentrosomal; assembled from many microtubule-organizing centers and chromatin (RanGTP) |

**Definition 21.7.4 (Polar Body)** A **polar body** is the small cell produced by the highly asymmetric divisions of an oocyte in meiosis I and meiosis II, which receives one set of chromosomes but almost no cytoplasm and normally degenerates.

The oocyte divides asymmetrically to keep its stockpile of cytoplasm. Its spindle forms in the center of the cell without centrosomes and migrates to the cortex, pushed by an actin network made by formin-2 and Spire; the cortex above the spindle is remodeled into an actin cap by a RanGTP signal from the chromosomes, and a tiny polar body is extruded. In mammals the second polar body is extruded after fertilization, when the $\ce{Ca^2+}$ wave triggered by the sperm destroys Emi2 and activates APC/C. The paternal and maternal pronuclei then replicate their DNA separately and meet on the first mitotic spindle, which in most animals is organized by the centrosome brought by the sperm (in the mouse, which lacks sperm centrioles, it forms without centrosomes).

### 21.7.5. Aneuploidy and the Maternal Age Effect

**Definition 21.7.5 (Aneuploidy)** **Aneuploidy** is the state of a cell or organism whose chromosome number is not an exact multiple of the haploid set, because it has gained or lost one or more chromosomes; it results from nondisjunction (the failure of homologues or sisters to separate) or from premature separation of sister chromatids in meiosis or mitosis.

Human meiosis is error-prone, and almost all errors occur in oocytes: in women in their twenties perhaps a tenth to a fifth of eggs are aneuploid, and after 40 more than half; in sperm the rate is a few percent at most and depends little on age. Most aneuploid embryos die, so aneuploidy is the leading cause of miscarriage; among those that survive, trisomy 21 (Down syndrome) most often originates in maternal meiosis I, and its risk rises from about 1 in 1500 births at a maternal age of 20 to about 1 in 100 at 40. The genetics of nondisjunction and of the resulting syndromes is treated in [7.4](/7.4). Several cellular causes combine:

- Cohesion decays with age. Cohesin is loaded onto oocyte chromosomes during premeiotic S phase in the fetus and is not replaced for decades (deleting the cohesin subunit after birth in mouse oocytes has no effect, so new cohesin is not loaded; Tachibana-Konwalski et al. 2010). Rec8 levels on the chromosomes of old mouse oocytes are much lower than in young ones, and in old oocytes chiasmata slip off, bivalents fall apart into univalents, and sister centromeres separate prematurely. Panel C of the figure above shows how a slow loss of cohesin with variation between chromosomes produces a steep rise of errors with age.
- The human oocyte spindle is unstable. Without centrosomes it takes about 16 hours to assemble and often passes through multipolar intermediates, with frequent wrong attachments (Holubcová et al. 2015).
- The checkpoint in oocytes is weak: a large oocyte cannot hold APC/C off with a few unattached kinetochores, and anaphase I begins with some chromosomes misaligned.
- Crossover position matters: chiasmata too close to the centromere or to the telomere, or their absence, make bivalents more likely to missegregate, which links the recombination patterns of 7.4 to the errors of the oocyte.

## Summary

| Process | Key mechanisms |
|---|---|
| Stages (Definition 21.1.1) | prophase, prometaphase, metaphase, anaphase, telophase; then cytokinesis; timed by M-Cdk and APC/C ([7.3.20](/7.3.20)) |
| Cohesin and condensin (Definition 21.1.2) | cohesion established in S; prophase pathway removes arm cohesin; Sgo1–PP2A protects centromeres; separase cleaves Scc1; condensin builds rigid chromatids |
| Spindle (Definition 21.2.1) | kinetochore, interpolar and astral microtubules; fast turnover and flux; kinesin-5 out, kinesin-14 and dynein in, chromokinesins eject |
| Assembly | search and capture (Definition 21.2.2) with optimal catastrophe frequency $f^* = v_{\mathrm{g}}/d$ (Eq. 21.1, Proposition 21.2.1); too slow alone; RanGTP, augmin, kinetochore nucleation and the corona bias it; acentrosomal self-organization |
| Kinetochore (Definition 21.3.1) | CENP-A, CCAN, KMN/Ndc80; couples to dynamic ends; attachment types; tension stabilizes; Aurora B releases tensionless attachments (Definition 21.3.2) |
| Checkpoint (Definition 21.3.3) | Mad2 template model, MCC inhibits APC/C–Cdc20; one kinetochore suffices; MCC disassembly ends it (Eq. 21.2); misses merotelic attachments; slippage |
| Segregation | anaphase A (depolymerization, flux) and B (sliding, cortical pulling) (Definition 21.4.1); nuclear re-formation; micronuclei |
| Cytokinesis (Definitions 21.5.1–21.5.3) | central spindle, astral stimulation and polar relaxation converge on Ect2–RhoA; formins and myosin II; ESCRT-III abscission; plants: preprophase band, phragmoplast, cell plate |
| Asymmetry (Definition 21.6.1) | PAR polarity, spindle orientation by LGN/NuMA/dynein, basal determinants (Numb, Prospero); niche-oriented stem-cell divisions |
| Meiosis (Definitions 21.7.1–21.7.5) | synaptonemal complex and obligatory crossover; chiasmata tie homologues; monopolin/Meikin co-orientation; shugoshin protects centromeric Rec8; asymmetric oocyte divisions and polar bodies; age-related loss of cohesion and aneuploidy |

## Questions

1. Using Eq. (21.1), estimate the optimal catastrophe frequency for capturing a kinetochore 8 µm from a pole if microtubules grow at 12 µm per minute. Why is a single optimum not really achievable for all chromosomes, and how does the RanGTP gradient help?

   **Answer** $f^* = v_{\mathrm{g}}/d = (12\,\mu\mathrm{m\,min^{-1}})/(8\,\mu\mathrm{m}) = 1.5\,\mathrm{min^{-1}}$, a mean lifetime of growth of 40 s. Kinetochores lie at different distances (about 2–12 µm), and the optimum differs for each, so a single cytoplasmic catastrophe rate is a compromise. The RanGTP gradient makes the catastrophe rate position-dependent: high far from chromosomes (microtubules growing in wrong directions are recycled quickly) and low near chromatin (those growing toward chromosomes survive to reach them), which is better than any uniform value.

2. A cell treated with monastrol, an inhibitor of kinesin-5, forms a monopolar spindle and arrests in mitosis. Explain both observations. What would you expect if kinesin-14 were also inhibited?

   **Answer** Kinesin-5 slides antiparallel microtubules between the two centrosomes apart; without it the inward forces of dynein and kinesin-14 dominate and the centrosomes stay together, so all microtubules radiate from one pole. Chromosomes can attach only syntelically or monotelically, there is no tension, Aurora B keeps detaching them and unattached kinetochores keep the spindle assembly checkpoint on, so the cell stays in mitosis. Inhibiting kinesin-14 at the same time removes part of the inward force and can partly restore bipolarity, as observed: spindle bipolarity reflects a balance of opposing motors, not a single essential one.

3. Why does a merotelically attached chromosome not activate the spindle assembly checkpoint, and what happens to it in anaphase? How do cells nevertheless keep such errors rare?

   **Answer** A merotelic kinetochore is attached to microtubules (so it does not generate MCC) and is under tension (because the majority attachment to one pole is opposed by the sister's attachment to the other pole). In anaphase it is pulled toward both poles and lags at the equator; it may end up in the wrong daughter or in a micronucleus. Cells reduce merotely by Aurora B-dependent correction during prometaphase (merotelic sites are often less stretched and near Aurora B), by back-to-back kinetochore geometry, by the prophase-to-metaphase time allowed for correction, and by Aurora B at the midzone, which can still promote resolution of lagging chromatids in anaphase.

4. In the model of Eq. (21.2), what would happen if $k_{\mathrm{amp}}$ were larger than $k_{\mathrm{off}}$? Relate your answer to the role of p31comet and TRIP13.

   **Answer** With $U = 0$ the $I$ equation becomes $\mathrm{d}I/\mathrm{d}t = I\left(k_{\mathrm{amp}}(1 - I) - k_{\mathrm{off}}\right)$. If $k_{\mathrm{amp}} > k_{\mathrm{off}}$, the state $I = 0$ is unstable and there is a stable state $I^* = 1 - k_{\mathrm{off}}/k_{\mathrm{amp}} > 0$: once formed, MCC would sustain itself after all kinetochores had attached and APC/C–Cdc20 would stay partly inhibited indefinitely, so the checkpoint could not be switched off. Active disassembly of the MCC by p31comet and TRIP13 keeps $k_{\mathrm{off}}$ above any amplification in solution, so the checkpoint signal depends continuously on unattached kinetochores and turns off within minutes of the last attachment.

5. A dividing sphere of radius $R$ forms two spheres of equal volume. By how much must the surface area increase? Where does the extra membrane come from?

   **Answer** Each daughter has volume $\frac{1}{2}\cdot\frac{4}{3}\pi R^3$, so radius $r = R/2^{1/3}$. Total area $2\cdot4\pi r^2 = 4\pi R^2\cdot2^{1/3}$, an increase of $2^{1/3} - 1 \approx 26\%$. Part of the extra area comes from unfolding microvilli and membrane reserves of the rounded mitotic cell, and the rest from exocytosis of vesicles from recycling endosomes and the Golgi at the furrow; in plants, essentially all the membrane of the cell plate is delivered by Golgi vesicles.

6. Explain why a homologue pair that has not formed a crossover is likely to missegregate in meiosis I, although each homologue has normal kinetochores and normal cohesion.

   **Answer** Bi-orientation of the homologues on the meiosis I spindle requires a physical link between them that resists the poleward pulling forces and generates tension, just as sister cohesion does in mitosis. That link is the chiasma together with sister-arm cohesion distal to it. Without a crossover the two homologues are independent univalents; their co-oriented sister kinetochores attach to whichever pole they happen to face, tension is never generated across a pair, and both homologues may go to the same pole (nondisjunction), or a univalent may divide its sisters prematurely.

7. Cohesin protection by shugoshin is essential in meiosis I but not in yeast mitosis. Why? Why would a cell whose shugoshin persisted into meiosis II also produce aneuploid gametes?

   **Answer** In yeast mitosis all cohesin is cleaved at once at anaphase and there is no later division that needs residual cohesion; in meiosis I centromeric cohesion must survive anaphase I to keep sisters together until they bi-orient on the meiosis II spindle. If shugoshin and PP2A persisted in meiosis II, centromeric Rec8 would remain protected and could not be cleaved, so sisters would fail to separate (or be torn apart randomly), again producing aneuploid gametes.

8. (Open question, from the course slides.) In principle, could a diploid germ cell produce haploid gametes with exchange of genetic information by some other scheme than one replication followed by two divisions? Discuss one alternative and its mechanical difficulties.

   **Answer** One alternative is "inverted meiosis", observed in some organisms with holocentric chromosomes (some plants and insects), in which sisters separate in the first division and homologues in the second; recombination still occurs before the divisions. Another conceivable scheme is a single reductional division without replication, pairing and recombining unreplicated homologues and separating them directly. Its difficulty is mechanical and informational: crossing over between unreplicated homologues would leave no sister to hold each recombined chromosome together, so chiasmata could not be stabilized by sister cohesion, and DNA breaks could not be repaired from a sister. Replication before division provides both the cohesion that holds homologues together via chiasmata and a template for repair, which is probably why one replication followed by two divisions is nearly universal.
