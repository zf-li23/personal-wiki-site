---
title: "Drosophila II: Segmentation and Homeotic Genes"
description: "How the maternal coordinates of the Drosophila embryo are turned into fourteen segments with distinct identities. Parasegments and segments; the gap genes, their cross-repressive network and a gene-circuit model; multilevel switches as a readout; the pair-rule genes, modular stripe enhancers and a thermodynamic model of eve stripe 2; the segment-polarity genes and the bistable Wingless-Hedgehog loop that maintains parasegment boundaries; the Hox genes of the Antennapedia and bithorax complexes, homeotic transformations, colinearity and the regulatory regions of the bithorax complex; maintenance of Hox expression by Polycomb and Trithorax group proteins and a model of chromatin memory; the Cartesian coordinate model."
---

At the end of the maternal phase ([7.5.14](/7.5.14)) the *Drosophila* embryo carries a few smooth gradients along its anterior–posterior axis. Within the next two hours it acquires fourteen sharp, periodic subdivisions, each with its own identity. This chapter follows the **zygotic genes** that do this: the **gap genes**, **pair-rule genes**, **segment-polarity genes** and **homeotic genes** whose mutant phenotypes defined the genetic hierarchy of [7.4.20](/7.4.20). There the question was the order of the tiers; here it is the mechanism of each step. Three ideas recur. Cross-repression between transcription factors converts graded inputs into sharp, abutting domains. Modular **enhancers** let one gene be expressed in a periodic pattern by reading a different combination of non-periodic inputs for each stripe. And positive feedback, between neighbouring cells or within the **chromatin** of a single locus, turns a transient instruction into a stable state that outlives the gradients that set it up. Each idea is stated as a quantitative model and simulated. The vertebrate counterparts appear in [7.5.17](/7.5.17) (*Hox* genes) and [7.5.23](/7.5.23) (segmentation by a clock).

## 15.1. The Segmentation Hierarchy

The genes act in a cascade that lasts from nuclear cycle 10 to the extended germ band, about 2–5 h after **fertilization** at 25 °C:

| Tier | Main genes | Molecular class | Expression | Read by |
|---|---|---|---|---|
| Maternal | *bicoid*, *nanos*, *caudal*, *torso* | TF, RNA-binding, RTK | gradients | gap genes |
| Gap | *hunchback*, *Krüppel*, *knirps*, *giant*, *tailless*, *huckebein* | TFs (zinc finger, nuclear receptor, bZIP) | 1–2 broad domains | pair-rule and *Hox* genes |
| Pair-rule | *hairy*, *even-skipped*, *runt* (primary); *fushi tarazu*, *odd-skipped*, *paired*, *sloppy-paired* (secondary) | TFs | 7 stripes, then 14 for some | segment-polarity genes |
| Segment polarity | *engrailed*, *wingless*, *hedgehog*, *patched*, *armadillo*, … | TF, Wnt and Hedgehog pathway components | 14 stripes | epidermal fates within each segment |
| Homeotic (*Hox*) | *labial* … *Abdominal-B* | homeodomain TFs | broad domains with parasegmental borders | segment-specific target genes |

The first periodic pattern is not aligned with the segments of the larva. Its unit is the parasegment, which is out of register with the segment by about half a segment.

**Definition 15.1.1 (Parasegment)** A **parasegment** is a metameric unit of the *Drosophila* embryo comprising the posterior part of one segment and the anterior part of the next. The 14 parasegments are delimited by the expression of the **pair-rule genes**; each begins with a row of *engrailed*-expressing cells at its anterior and ends with a row of *wingless*-expressing cells, and the parasegment boundary lies between the two.

The parasegments are the units of early gene expression: the stripes of *even-skipped* coincide with the odd-numbered parasegments, those of *fushi tarazu* with the even-numbered ones, and the *Hox* genes have their anterior borders at parasegment boundaries. They are visible only transiently, as shallow grooves on the germ band; the segment grooves that appear later lie just posterior to the *engrailed* row, so that each segment consists of the posterior part of one parasegment (which becomes the segment's anterior compartment) and the *engrailed*-expressing anterior part of the next (its posterior **compartment**, [7.5.33](/7.5.33)). Muscles and the ventral nerve cord retain the parasegmental register, the cuticle the segmental one.

![Parasegments and segments in the *Drosophila* germ band (schematic, four cell rows per parasegment, anterior to the left). even-skipped (pink) is expressed in the odd-numbered and fushi tarazu (purple) in the even-numbered parasegments; engrailed and hedgehog (blue) mark the anterior row of each parasegment and wingless (green) the posterior row, so each parasegment boundary (dashed) lies between a wingless row and an engrailed row. The segment boundaries (solid) lie posterior to the engrailed rows: each segment consists of an anterior compartment (A) derived from the posterior part of one parasegment and a posterior compartment (P) of engrailed-expressing cells from the next](./plots/parasegments.py)

## 15.2. The Gap Genes

### 15.2.1. Domains and Their Regulation

The gap genes are the first zygotic genes to read the maternal gradients. All encode transcription factors; they are transcribed from cycle 10–11 in the syncytium, so their proteins diffuse between nuclei; their mRNAs and proteins are short-lived, with half-lives of minutes to tens of minutes, so their patterns follow changes in their regulation closely; and each is expressed in one or two broad domains. By cycle 14 the trunk gap genes are arranged in the order *hunchback* (anterior half), *Krüppel* (centred at about 45 % of egg length), *knirps* (about 65 %) and the posterior domain of *giant* (about 80 %), with *tailless* and *huckebein* at the poles and a second, anterior *giant* domain in the head.

The domains are initiated by the maternal inputs and refined by the gap proteins themselves:

- *hunchback* is activated by Bicoid through a cluster of **binding sites** in its proximal **enhancer**, cooperatively, so that its boundary is sharp ([7.5.14](/7.5.14)); its maternal component is graded by Nanos.
- *knirps* and posterior *giant* are activated by Caudal and by low Bicoid; their anterior limits are set by repression by Hunchback.
- *Krüppel* is activated in the middle of the embryo; Hunchback represses it at high concentration (and at low concentration contributes to its activation), Giant represses it from both sides and Knirps from behind.
- Tailless and Huckebein, activated by the terminal system, repress the trunk gap genes near the poles.

The interactions among the gap genes are all repressive, and their strengths follow a rule: repression is strong between genes whose domains do not overlap (Hunchback and Knirps, Krüppel and Giant) and weaker between neighbours. Strong mutual repression between non-neighbours creates the alternating arrangement; weak repression between neighbours lets adjacent domains overlap by a few nuclei, which is what the pair-rule enhancers need (15.3). Mutants confirm the logic: in *Krüppel* mutants the *knirps* domain expands anteriorly into the vacated region and the posterior *giant* domain shifts with it; in *knirps* mutants the *Krüppel* domain expands posteriorly. The interactions are also asymmetric. During cycle 14 the posterior gap domains move anteriorly by up to 10 % of the egg length, because the repression of each gene by its posterior neighbour is stronger than that by its anterior neighbour (Jaeger and colleagues, 2004). The final positions thus depend on the dynamics of the network, not only on the maternal gradients.

### 15.2.2. A Gene-Circuit Model

Reinitz, Sharp and colleagues formulated the gap system as a gene circuit whose parameters can be fitted to quantitative expression data.

**Formula 15.2.1 (Gene circuit)** Let $g_a(x, t)$ be the concentration of the product of gap gene $a$ in the nucleus at position $x$. Then

$$
\frac{\partial g_a}{\partial t} = R_a\,\Phi\!\left(\sum_b W_{ab}\,g_b + \sum_m E_{am}\,v_m(x) + h_a\right) - \lambda_a g_a + D_a\,\frac{\partial^2 g_a}{\partial x^2},
\tag{15.1}
$$

where $W_{ab}$ is the regulatory effect of gap protein $b$ on gene $a$ (positive for activation, negative for repression), $v_m$ are the maternal inputs (Bicoid, Caudal, Tailless) with weights $E_{am}$, $h_a$ is a threshold, $R_a$ the maximal synthesis rate, $\lambda_a$ the decay rate and $D_a$ the diffusion coefficient between nuclei; $\Phi(u) = \tfrac12\bigl(1 + u/\sqrt{1 + u^2}\bigr)$ is a sigmoid. Eq. (15.1) sums the inputs linearly before the nonlinearity: it is a coarse-grained description in which each regulator contributes an increment of log-odds of activation, not a model of binding.

Fitted to data from fixed embryos, circuits of this form reproduce the gap domains and their anterior shifts and predict the effects of mutants that were not used in the fit; they also identified which interactions are needed. The figure shows a hand-built circuit of the same form, with strong repression between non-neighbours and an exponential Bicoid gradient: the four domains form in the right order, and removing *Krüppel* or *knirps* reproduces the expansions of the neighbouring domains seen in the mutants.

![The gap-gene network and a gene circuit (Formula 15.2.1). A: Bicoid activates hunchback, Caudal activates knirps and giant, Tailless represses the trunk gap genes near the poles; strong mutual repression links the non-adjacent pairs hb–kni and Kr–gt (thick bars), weaker repression links neighbours. B: steady state of the four-gene circuit on 100 nuclei (dimensionless rates, sigmoid response, weak diffusion), driven by an exponential Bicoid gradient with decay length 0.2 L (dashed), a posterior Caudal ramp and terminal Tailless: hb, Kr, kni and gt form ordered, abutting domains. C, D: removing Kr or kni from the circuit lets the neighbouring domains expand into the vacated region, as in the mutant embryos](./plots/gap-network.py)

### 15.2.3. Multilevel Switches

The gap system is one answer to a general problem: how a smooth gradient is converted into several discrete, mutually exclusive states. Percus and Childress analysed a simpler answer, in which several self-activating genes share a common **repressor**.

**Formula 15.2.2 (Multilevel switch with a common repressor)** Let genes $g_1, \dots, g_n$ activate themselves cooperatively and produce a common repressor $r$:

$$
\dot g_i = \frac{c_i\,g_i^2}{r} - \gamma g_i, \qquad \dot r = \sum_i c_i\,g_i^2 - \beta r, \qquad \beta > \gamma .
\tag{15.2}
$$

**Proposition 15.2.1** The stationary states of Eq. (15.2) with $r > 0$ are those in which exactly one gene $i$ is on, $g_i = \beta/\gamma$, $r = \beta c_i/\gamma^2$, with $g_j = 0$ for $j \ne i$ (states with two genes on require $c_i = c_j$). Each of these $n$ states is locally stable.

**Proof** At a stationary state each $g_i$ is $0$ or satisfies $c_i g_i/r = \gamma$. If $g_i$ and $g_j$ were both nonzero, $c_i g_i = c_j g_j = \gamma r$; substituting into $\dot r = 0$ gives $\gamma r (g_i + g_j) = \beta r$, and the conditions for $g_i, g_j$ to be stationary are then compatible only for $c_i = c_j$. With one gene on, $\gamma g_i r = \beta r$ gives $g_i = \beta/\gamma$ and then $r = c_i g_i/\gamma = \beta c_i/\gamma^2$. For stability, the Jacobian is block-structured. For $j \ne i$, $\partial\dot g_j/\partial g_j = 2c_j g_j/r - \gamma = -\gamma < 0$ at $g_j = 0$, and $g_j$ does not enter the other equations to first order. In the $(g_i, r)$ block,

$$
J = \begin{bmatrix} 2c_i g_i/r - \gamma & -c_i g_i^2/r^2 \\ 2c_i g_i & -\beta \end{bmatrix} = \begin{bmatrix} \gamma & -\gamma^2/c_i \\ 2c_i\beta/\gamma & -\beta \end{bmatrix},
$$

with $\operatorname{tr} J = \gamma - \beta < 0$ and $\det J = -\gamma\beta + 2\gamma\beta = \gamma\beta > 0$, so both eigenvalues have negative real parts ([2.4.11](/2.4.11)). $\square$

The switch is therefore winner-take-all and multistable: once one gene has won, its repressor level keeps all others off, because an off gene, starting from zero, has a production term $c_j g_j^2/r$ that is quadratic in $g_j$ and cannot grow against linear decay. Which gene wins is decided by the history: by which grows fastest from small initial values. Percus and Childress made the coefficients depend on an activator $a$, $c_i \mapsto c_i(1 + a/r)$, and argued that as $a$ rises successive genes reach a maximum and shut off, so that a graded activator would select one gene per level. Proposition 15.2.1 shows what such a scheme requires: since every pure state is stable once reached, the activator must act on the competition while the genes are still growing, and the genes must differ in how strongly the activator favours them at each level (in the language of enhancers, different affinities for the activator). The gap system uses a version of this: the gap genes are not autocatalytic through a common repressor, but they repress each other, which also makes the off state of each gene self-reinforcing where its competitor is on, and the competition is biased in a position-dependent way by the maternal gradients while the domains are forming. The general analysis of such switches and of their readout of a **morphogen**, including the hysteretic two-level switch, is in [7.5.11](/7.5.11).

**Remark 15.2.1** In a commentary on pattern-formation models, Percus and Childress contrasted the economy of the mechanisms that Meinhardt proposed for segmentation, in which a few self-organizing interactions generate a periodic sequence of states, with the system that genetics revealed: dozens of genes, each stripe of each pair-rule gene positioned by its own enhancer and its own combination of gap repressors. The contrast is real. Evolution did not design the cascade; it accumulated repressors and enhancers on an ancestral system, very likely one with a segmentation clock as in short-germ insects (15.3.3), and the result is redundant and hard to compress. The redundancy is not useless: shadow enhancers and overlapping inputs make expression robust to temperature and genetic variation, and modular enhancers let individual stripes change in evolution without disturbing the others.

## 15.3. The Pair-Rule Genes

### 15.3.1. Seven Stripes from Non-Periodic Inputs

The pair-rule genes give the first periodic pattern: during cycle 14 each is expressed in seven stripes, three to four cells wide, one per pair of parasegments. Mutants lack alternate segmental units (the phenotype that named them, [7.4.20](/7.4.20)), and the deleted parts correspond to the domains where the gene is normally expressed: in *fushi tarazu* (Japanese for "not enough segments") mutants the even-numbered parasegments are missing, in *even-skipped* mutants the odd-numbered ones.

The primary pair-rule genes, *hairy*, *even-skipped* (*eve*) and *runt*, read the gap genes directly. Their regulatory regions are modular: separate enhancers, each a few hundred base pairs, drive one or two stripes. The *eve* locus has enhancers for stripe 1, stripe 2, stripes 3 and 7, stripes 4 and 6, and stripe 5, distributed over about 12 kb on both sides of the gene. Each was identified by fusing fragments of the locus to a reporter gene (*lacZ*) and introducing them into embryos; each fragment drives only its own stripes, and deleting an enhancer removes only those stripes.

The best-studied is the stripe 2 enhancer, defined by Small, Blair and Levine (1992) as a minimal element of about 480 bp. It contains five binding sites for Bicoid and one for Hunchback, its activators, and several sites for Krüppel and Giant, its repressors. The activators are present throughout the anterior half of the embryo; stripe 2 forms where they are present and both repressors are absent, in the narrow gap between the anterior *giant* domain and the *Krüppel* domain. The experiments that established this are of the form "remove one input, watch the border move": in *Krüppel* mutants the posterior border of stripe 2 expands posteriorly, in *giant* mutants its anterior border expands anteriorly, and mutating the Bicoid sites abolishes the stripe. The repressors act only over short distances, about 100 bp: a repressor bound in one enhancer silences that enhancer but not a neighbouring one, which is what allows each enhancer of the locus to work independently (short-range repression, or quenching). Other stripes use other combinations: the stripe 3/7 enhancer is activated by ubiquitous factors and repressed by Hunchback anteriorly and Knirps in between, so that it is on in the two gaps that flank the *knirps* domain.

### 15.3.2. A Thermodynamic Model of the Stripe 2 Enhancer

The **thermodynamic model** of transcription ([7.2.11](/7.2.11)) assumes that factors bind and unbind fast compared with transcription, so that the expression of a gene is a function of the equilibrium occupancies of its binding sites.

**Formula 15.3.1 (A quenching enhancer)** Let an enhancer have $n_{\mathrm{B}}$ Bicoid and $n_{\mathrm{H}}$ Hunchback sites and $n_{\mathrm{K}}$ Krüppel and $n_{\mathrm{G}}$ Giant sites, bound independently with occupancies $\theta_X = [X]/([X] + K_X)$. If the enhancer is active when at least two activator sites are occupied and no repressor site is occupied (each bound repressor quenches the whole element),

$$
P_{\mathrm{on}}(x) = \Bigl[1 - P_0(x) - P_1(x)\Bigr]\,(1 - \theta_{\mathrm{K}})^{n_{\mathrm{K}}}\,(1 - \theta_{\mathrm{G}})^{n_{\mathrm{G}}},
\tag{15.3}
$$

where $P_0 = (1 - \theta_{\mathrm{B}})^{n_{\mathrm{B}}}(1 - \theta_{\mathrm{H}})^{n_{\mathrm{H}}}$ and $P_1$, the probability that exactly one activator site is occupied, are binomial terms. All concentrations, and hence $P_{\mathrm{on}}$, depend on the position $x$ through the gap and maternal profiles.

The model contains the logic of the enhancer in a form that can be computed. The requirement of two activators makes the response to Bicoid cooperative, which keeps the enhancer off in the posterior where Bicoid is low; the product of repressor terms implements an AND-NOT logic; and because each repressor term is a high power of $(1 - \theta)$, a few sites make repression strong. In the figure, the stripe forms between the anterior Giant and the Krüppel domains, and removing either repressor or the Bicoid sites reproduces the three mutant results. Models of this kind, with binding energies estimated from sequence, cooperative interactions between neighbouring sites and distance-dependent quenching, have been fitted to quantitative expression data of reporter genes and predict the expression of modified enhancers moderately well, an indication that the logic of the element is largely encoded in the arrangement of its sites (Janssens and colleagues, 2006; Fakhouri and colleagues, 2010).

![The even-skipped stripe 2 enhancer as a thermodynamic switch (Formula 15.3.1). A: the minimal stripe 2 element (about 480 bp) with binding sites for Bicoid and Hunchback above the line (activators) and for Krüppel and Giant below it (repressors); the order is schematic. B: input profiles (dashed; Bicoid, Hunchback, the anterior Giant domain, Krüppel and an anterior repressor, Sloppy-paired) and the predicted probability that the enhancer is active (solid): activators define a broad anterior region, anterior Giant cuts it from the front and Krüppel from the back, leaving one stripe. C: removing Giant extends the stripe anteriorly, removing Krüppel extends it posteriorly and removing the Bicoid sites abolishes it, as in the corresponding mutant or mutated reporter constructs](./plots/eve-stripe2.py)

### 15.3.3. From Seven Stripes to Fourteen

The secondary pair-rule genes, including *fushi tarazu*, *odd-skipped*, *paired* and *sloppy-paired*, are regulated mainly by the primary ones, and the pair-rule proteins regulate each other, refining the stripes and fixing their phase relations. By the end of cycle 14 each row of cells within a double-segment unit expresses a distinct combination of pair-rule proteins. Several genes then switch to a 14-stripe pattern. The switch is timed by Odd-paired, a uniformly expressed factor that appears at **gastrulation** and changes the regulatory interactions among the pair-rule genes (Clark and Akam, 2016): the same proteins that position seven stripes position fourteen once its partner is present. The result is a set of combinations that defines the anterior and posterior rows of every parasegment, read by the segment-polarity genes.

This simultaneous, gap-gene-dependent way of making stripes is a derived feature of long-germ insects such as *Drosophila*, in which all segments are specified at the blastoderm stage. In short-germ insects such as the flour beetle *Tribolium castaneum*, most segments are added sequentially from a posterior growth zone, and the pair-rule genes there oscillate like the segmentation clock of vertebrates ([7.5.23](/7.5.23)); the *Drosophila* system is thought to have evolved from such a clock, with the gap genes taking over the spatial role of the oscillation ([7.5.39](/7.5.39)).

## 15.4. The Segment-Polarity Genes

### 15.4.1. Initiation by the Pair-Rule Genes

The segment-polarity genes define the anterior and posterior parts of every segment. *engrailed* (*en*), a homeodomain transcription factor, is activated in the cells with high levels of Eve or Ftz and is repressed by Odd-skipped, Runt and Sloppy-paired: it comes on in the anterior row of each parasegment, 14 stripes in all, the odd-numbered ones depending on Eve and the even-numbered on Ftz. *wingless* (*wg*), encoding the *Drosophila* Wnt, is activated in the cells that have Sloppy-paired but neither Eve nor Ftz, the row just anterior to each *engrailed* row. *hedgehog* (*hh*) is activated by Engrailed, so the *engrailed* cells secrete Hedgehog.

### 15.4.2. A Bistable Loop Between Neighbouring Cells

The pair-rule proteins disappear shortly after gastrulation, but the *engrailed* and *wingless* stripes remain and the boundary between them persists, as the posterior compartment boundary, until the adult. Their maintenance is by mutual signalling. Wingless secreted by the *wg* cells binds Frizzled receptors on the neighbouring *engrailed* cells and, through the **Wnt signaling pathway** (Armadillo, the fly **β-catenin**), maintains *engrailed* expression. Hedgehog secreted by the *engrailed* cells binds Patched on the neighbouring *wg* cells and, through the **Hedgehog signaling pathway** (Cubitus interruptus), maintains *wingless* expression ([7.3.19](/7.3.19)). Two asymmetries make the loop work in one direction only: Engrailed represses *cubitus interruptus*, so the *engrailed* cells themselves cannot respond to Hedgehog, and only cells with Sloppy-paired are competent to express *wingless*. In *wingless* or *hedgehog* mutants, *engrailed* is initiated normally but fades from about 1 h after gastrulation, and the cuticle shows the lawn of denticles of the segment-polarity class.

**Formula 15.4.1 (The Wingless–Hedgehog loop)** On a row of cells $i$, let $E_i$ be the level of Engrailed (and Hedgehog) and $W_i$ that of Wingless. With competence masks $\kappa^E_i, \kappa^W_i \in \{0, 1\}$ set by the pair-rule genes, transient pair-rule inputs $p^E_i(t), p^W_i(t)$ and a cooperative response $f(u) = u^m/(K^m + u^m)$,

$$
\dot E_i = \kappa^E_i\, f\bigl(\alpha(W_{i-1} + W_{i+1}) + p^E_i(t)\bigr) - E_i, \qquad \dot W_i = \kappa^W_i\, f\bigl(\alpha(E_{i-1} + E_{i+1}) + p^W_i(t)\bigr) - W_i .
\tag{15.4}
$$

With $m > 1$ and $\alpha$ large enough, a neighbouring pair ($E_i$, $W_{i-1}$) has two stable states, both on or both off: the loop is a **bistable** switch made of two cells, and the transient pair-rule inputs only choose the state ([7.3.18](/7.3.18)).

The simulation shows the three consequences. In the **wild type** the pattern persists after the inputs vanish. Without Wingless, *engrailed* fades when the input ends. If Hedgehog signalling is blocked only transiently, the loop falls into the off state and does not recover when signalling returns, because the off state is stable too: the stripes are a memory of the pair-rule pattern stored in cell–cell signalling. Von Dassow, Meir, Munro and Odell (2000) built a much larger model of the segment-polarity network, with 136 parameters, and found that about one random parameter set in two hundred reproduced the wild-type pattern, a fraction far higher than expected for a finely tuned system; analysis of the model showed that the robustness comes largely from **bistability** of the individual cells (Ingolia, 2004).

![Maintenance of the parasegment boundary by the Wingless–Hedgehog loop (Formula 15.4.1), as kymographs of a row of 16 cells (four parasegments of four cells; time upward). engrailed with hedgehog in blue, wingless in green. Pair-rule inputs switch engrailed on in the first cell of each parasegment and wingless in the last until t = 5 (dotted line) and then vanish. A: wild type; the pattern persists. B: wingless mutant; engrailed fades once the pair-rule input ends. C: Hedgehog signalling blocked for 5 < t < 9 (shaded); both genes switch off and do not recover, because the off state of the loop is also stable](./plots/wg-hh-loop.py)

### 15.4.3. Patterning Within the Segment

The boundary between the *wingless* and *engrailed* rows is a signalling centre. On the ventral epidermis each segment secretes a cuticle with a belt of denticles, small hooks of several types, followed by naked cuticle, and the pattern of types along each segment is set by Wingless and Hedgehog acting at a distance from the boundary. Wingless spreads mainly anteriorly, because it is degraded rapidly in the *engrailed* cells posterior to its source, while Hedgehog acts on cells anterior to the *engrailed* row as well. In *wingless* mutants all cells make denticles; in *naked cuticle* or with ubiquitous Wingless all make naked cuticle. The segment-polarity genes thus play, within each segment, the role that the maternal gradients play for the whole embryo; the same pair of signals, Wingless and Hedgehog, organizes the imaginal discs ([7.5.33](/7.5.33)).

## 15.5. The Homeotic (Hox) Genes

### 15.5.1. Two Complexes and Their Mutants

The segment-polarity genes make every segment alike; the **homeotic genes** make them different. In *Drosophila* most of them lie in two clusters on the right arm of chromosome 3: the Antennapedia complex (ANT-C), with *labial* (*lab*), *proboscipedia* (*pb*), *Deformed* (*Dfd*), *Sex combs reduced* (*Scr*) and *Antennapedia* (*Antp*), and the bithorax complex (BX-C), with *Ultrabithorax* (*Ubx*), *abdominal-A* (*abd-A*) and *Abdominal-B* (*Abd-B*). All encode **homeodomain** transcription factors, and all are expressed in broad domains with anterior limits at parasegment boundaries.

**Definition 15.5.1 (Hox gene)** A **Hox gene** is a member of a family of homeobox genes, related by descent from a single ancestral cluster, that are arranged in one or a few clusters in the genomes of bilaterian animals and specify regional identity along the anterior–posterior axis; the homeotic genes of the Antennapedia and bithorax complexes of *Drosophila* and the genes of the four *Hox* clusters of mammals are Hox genes.

Their loss or misexpression causes **homeotic transformations**:

- Loss of *Ubx* function in the third thoracic segment transforms it into a copy of the second: the halteres, small balancing organs, become wings. Combining three mutations in the regulatory regions of *Ubx* (*abx*, *bx*, *pbx*) produces the four-winged fly of Lewis (1978). Ubx does not instruct the haltere; it represses a subset of the targets of the wing-development pathway in the haltere disc (Weatherbee and colleagues, 1998).
- Dominant *Antennapedia* **alleles**, caused by rearrangements that put *Antp* under the control of a regulatory region active in the head, express it in the antennal disc and transform antennae into legs; Antp represses *homothorax* and *eyeless* there, genes needed for antenna and eye. Loss of *Antp* in clones of the second thoracic segment gives the reverse, antenna-like structures in place of legs.
- *Abd-B* and *abd-A* specify abdominal identity; in embryos lacking the whole bithorax complex, all segments from the third thoracic to the eighth abdominal develop like the second thoracic, the identity specified by *Antp* alone.

In cells that express several *Hox* genes, the more posterior gene usually determines the identity, by repressing the more anterior genes or by overriding their effects on common targets, a rule known as posterior prevalence. *Hox* proteins bind similar short DNA sequences (with the core TAAT) on their own; their specificity in vivo comes from partners, the TALE homeodomain proteins Extradenticle and Homothorax, with which they form heterodimers that read longer sites whose preferred sequences differ between *Hox* proteins (Slattery and colleagues, 2011). Their targets include genes for appendages and organs: Ubx and Abd-A repress *Distal-less* in the abdomen, which is why insects have no abdominal legs.

### 15.5.2. Colinearity

**Definition 15.5.2 (Hox colinearity)** **Hox colinearity** is the correspondence between the order of the Hox genes along the chromosome and the order of their expression domains along the body axis (spatial colinearity): genes nearer one end of a cluster (the 3′ end in vertebrate nomenclature) are expressed more anteriorly. In vertebrates the genes are also activated in the same order in time, 3′ genes first (temporal colinearity, [7.5.17](/7.5.17)).

Spatial colinearity was discovered by Lewis (1978) in the bithorax complex and extended to the whole HOM-C when the genes were cloned (figure). In *Drosophila* the complex is split into two parts about 10 Mb apart, and some genes have lost their role in axial patterning (*bicoid*, *zerknüllt* and *fushi tarazu* lie inside ANT-C and are derived *Hox* genes); colinearity holds nevertheless, which shows that it does not depend on the physical continuity of the cluster in flies. In vertebrates, where the clusters are compact and colinear expression depends on regulatory elements shared across the cluster, it does ([7.5.17](/7.5.17)).

![The homeotic complex of *Drosophila* and spatial colinearity. Top: the eight Hox genes on chromosome 3R in their chromosomal order, the Antennapedia complex (labial, proboscipedia, Deformed, Sex combs reduced, Antennapedia) and the bithorax complex (Ultrabithorax, abdominal-A, Abdominal-B), separated by about 10 Mb. Bottom: the segments of the embryo from the intercalary (Ic), mandibular (Md), maxillary (Mx) and labial (Lb) head segments through the thorax (T1–T3) to the abdomen (A1–A8), with the main domain of each gene (strong colour) and, for Scr, Antp and Ubx, the weaker expression posterior to it (pale). The order of the genes on the chromosome matches the order of their anterior limits along the body (schematic)](./plots/hox-complex.py)

### 15.5.3. The Regulatory Regions of the Bithorax Complex

The bithorax complex spans about 300 kb but encodes only three proteins; most of it is regulatory DNA. Lewis's genetic analysis, before any of it was cloned, divided it into a series of regulatory regions, each required for the identity of one parasegment: *abx*/*bx* for parasegment 5, *bxd*/*pbx* for parasegment 6 (both controlling *Ubx*), and *iab-2* to *iab-8* for parasegments 7–13 (controlling *abd-A* and *Abd-B*). The regions lie on the chromosome in the same order as the parasegments they control.

**Example 15.5.1 (Deletion and rescue in the bithorax complex)** Embryos lacking the entire bithorax complex have parasegments 5–13 transformed into copies of parasegment 4. Adding back a **transgene** containing *Ubx* and its regulatory regions restores parasegments 5 and 6 but leaves 7–13 like 6; adding *Ubx* and *abd-A* restores 5–9; and the full complex restores 5–13 (after Lewis and subsequent molecular dissection). The experiment shows two things. Each gene is responsible for a block of parasegments: *Ubx* for 5–6, *abd-A* for 7–9, *Abd-B* for 10–13. And within each block the regulatory regions add successive levels: a parasegment lacking the more posterior gene takes the identity of the most posterior parasegment the remaining genes can specify, which is posterior prevalence read from a deletion series.

The regulatory regions are domains of chromatin, each with an initiator element that reads the gap and pair-rule proteins in one parasegment and a maintenance element that keeps the state of the domain afterwards, separated from neighbouring domains by boundary (**insulator**) elements such as *Fab-7*. In each parasegment, the regions up to the corresponding one are open and the more posterior ones closed, so that the number of open domains increases from anterior to posterior: a chromatin version of colinearity.

## 15.6. Maintenance: Polycomb and Trithorax

The gap and pair-rule proteins that initiate *Hox* expression disappear within a few hours, yet the *Hox* domains persist through larval life and metamorphosis. Two groups of genes maintain them, found because their mutants transform segments although their products are not localized.

**Definition 15.6.1 (Polycomb and Trithorax group proteins)** The **Polycomb group** (PcG) proteins are chromatin regulators that maintain the repressed state of developmental regulator genes, including the *Hox* genes, in cells where they were initially repressed; they act through the Polycomb repressive complexes, PRC2, which trimethylates histone H3 at lysine 27 (H3K27me3), and PRC1, which binds this mark and compacts chromatin and monoubiquitinates histone H2A. The **Trithorax group** (TrxG) proteins maintain the active state of the same genes in cells where they were initially active, by methylating histone H3 at lysine 4 and lysine 36 and by remodelling chromatin.

Heterozygous *Polycomb* males have extra sex combs on the second and third legs, because *Scr*, normally restricted to the first thoracic segment, is derepressed more posteriorly; in homozygous embryos lacking maternal and zygotic Polycomb, all *Hox* genes are eventually expressed in all segments and all segments develop like the eighth abdominal, the identity specified by the most posterior gene, *Abd-B*. In *trithorax* mutants, by contrast, *Hox* expression is initiated but not maintained, and segments are transformed towards more anterior identities. Neither group sets up the pattern: in PcG mutants the domains are initially normal and are lost only after the gap proteins have decayed. PcG and TrxG proteins are recruited to Polycomb response elements, DNA elements within the *Hox* regulatory regions, and the state of an element (repressed or active) is copied through cell divisions. The biochemistry of the complexes and of read–write feedback is described in [7.2.15](/7.2.15), and the genetics of *Polycomb* and **position effects** in [7.4.18](/7.4.18).

The logic is a hand-over from transcription factors to chromatin: a transient input decides the state of a locus, and an epigenetic feedback keeps it. Dodd, Sneppen, Thon and colleagues showed with a minimal model ([7.2.15](/7.2.15#ex-15.6.1)) that recruitment of modifying enzymes by modified nucleosomes, if it is cooperative and long-range, makes a chromatin region bistable. The figure adds the developmental step to their model: during an initial period a gap repressor (in one cell) or an activator (in another) biases the noisy conversions of the nucleosomes; afterwards the bias is removed and only the feedback remains. With strong feedback, each cell keeps the state it was given for many divisions; with weak feedback, the instruction is lost within a few divisions. This is **cell memory** in its simplest form, the same principle as the Wingless–Hedgehog loop of 15.4.2 but stored inside one cell.

![Initiation by gap repressors, maintenance by Polycomb, in the read–write model of Dodd and colleagues (7.2.15): a region of 60 nucleosomes, each modified for silencing (M), unmodified (U) or modified for activity (A), converted by recruitment (probability F/(1+F), towards the state of a randomly chosen nucleosome) or by noise, with a cell division (half of the nucleosomes reset to U) every 100 sweeps (ticks). During the first 300 sweeps (shaded) a transcription factor biases the noisy conversions towards M (a cell with a gap repressor, purple) or towards A (a cell with an activator, green); afterwards the bias is removed. A: strong feedback (F = 4); both cells keep their instructed state. B: weak feedback (F = 1); both forget it within a few divisions](./plots/polycomb-memory.py)

The two groups are conserved. Mammalian PRC2 (with the methyltransferase EZH2) and PRC1 repress *Hox* and many other developmental genes, and the mammalian Trithorax homologues are the KMT2 (MLL) methyltransferases. Their defects cause disease: rearrangements of *KMT2A* (*MLL*) fusing it to other genes cause leukaemias, in which *HOXA* genes are aberrantly maintained; activating mutations of *EZH2* occur in lymphomas, inactivating ones in Weaver syndrome, an overgrowth disorder; and mutations in *KMT2D* cause Kabuki syndrome, a disorder of development affecting the face, skeleton and heart.

## 15.7. A Cartesian Coordinate System

By the end of germ-band extension, the anterior–posterior position of every cell is specified at two levels, the parasegment (by the *Hox* genes) and the position within it (by the segment-polarity genes), and its dorsal–ventral position by the Dorsal and Dpp systems ([7.5.14](/7.5.14)). Organ primordia arise at intersections of these coordinates. The salivary glands form in parasegment 2, where *Scr* is expressed, on the ventral side, where Dpp is absent; ectopic Scr induces salivary glands in other ventral segments, and dorsal Dpp prevents them. The leg primordia, marked by *Distal-less*, form in each thoracic segment where the Wingless stripe meets the lateral region of low Dpp, and are repressed in the abdomen by Ubx and Abd-A. The tracheal placodes, the precursors of the respiratory system, form in ten lateral positions defined in the same way. This Cartesian logic, independent coordinates read in combination, is the general solution by which a few signals specify many distinct structures; it reappears in the imaginal discs and in vertebrate limbs and **neural tube**.

## Summary

| Topic | Key points |
|---|---|
| Hierarchy (15.1, Definition 15.1.1) | maternal → gap → pair-rule → segment polarity → *Hox*; **parasegments** (en anterior, wg posterior) are offset from segments by half a segment |
| Gap genes (15.2, Formula 15.2.1) | short-lived TFs in broad domains; Bcd → *hb*, Cad → *kni*, *gt*; strong repression between non-neighbours, weak and asymmetric between neighbours; anterior shifts; gene circuits reproduce domains and mutants |
| Switches (Formula 15.2.2, Proposition 15.2.1, Remark 15.2.1) | common-repressor switch: one gene on, every pure state stable, choice by history; gradients must bias the competition while it is unresolved; evolution stacked repressors rather than designing an economical mechanism |
| Pair-rule (15.3, Formula 15.3.1) | 7 stripes from modular enhancers; *eve* stripe 2: Bcd, Hb activate, Gt, Kr repress over short range; thermodynamic AND-NOT model; primary/secondary genes, Odd-paired switch to 14 stripes; clocks in short-germ insects |
| Segment polarity (15.4, Formula 15.4.1) | *en* where Eve/Ftz high, *wg* where Slp but no Eve/Ftz; Wg → En, Hh → Wg across the boundary; bistable two-cell loop stores the pattern; robustness (von Dassow); denticle patterning by Wg and Hh |
| *Hox* genes (15.5, Definitions 15.5.1, 15.5.2, Example 15.5.1) | ANT-C (*lab*, *pb*, *Dfd*, *Scr*, *Antp*), BX-C (*Ubx*, *abd-A*, *Abd-B*); homeotic transformations (haltere → wing, antenna → leg); posterior prevalence; Exd/Hth cofactors; spatial **Hox colinearity**; BX-C regulatory domains PS5–PS13 |
| Memory (15.6, Definition 15.6.1) | Polycomb group (PRC2: H3K27me3; PRC1) keeps repressed, Trithorax group keeps active; initiation by gap/pair-rule, maintenance by chromatin feedback (Dodd model); KMT2A leukaemia, EZH2 |
| Cartesian coordinates (15.7) | organ primordia at intersections of AP and DV coordinates: salivary glands (Scr, no Dpp), leg primordia (Wg × Dpp, repressed by Ubx) |

## Questions

1. Explain why the parasegment rather than the segment is the unit of early gene expression, using the positions of the *engrailed* and *wingless* stripes. Which larval structures keep the parasegmental register?

   **Answer** The pair-rule genes subdivide the embryo into units whose boundaries are where they activate *engrailed* (the anterior row of a unit) and *wingless* (the posterior row of the preceding unit); these units are the parasegments, and the *Hox* genes, read from the same gap and pair-rule inputs, also have their limits at parasegment boundaries. The segment boundary forms later, just posterior to each *engrailed* row, so the segment straddles two parasegments. The ventral nerve cord and the musculature keep the parasegmental register; the epidermis and cuticle follow segments.

2. Predict the expression of *Krüppel* in embryos from *bicoid* mutant mothers, and explain the prediction with the regulation described in 15.2.1.

   **Answer** Without Bicoid, zygotic *hunchback* is not activated anteriorly, and maternal Hunchback is present only at moderate uniform levels in the anterior half (graded by Nanos posteriorly). High Hunchback, which normally represses *Krüppel* anteriorly, is absent, whereas moderate Hunchback, which permits or activates *Krüppel*, is present; the *Krüppel* domain therefore expands anteriorly towards the pole, as observed. The anterior *giant* domain, which requires Bicoid, is also lost, removing another anterior repressor.

3. For the stripe 2 enhancer model (Formula 15.3.1) with five Bicoid sites and no Hunchback site, compute the probability that at least two activator sites are occupied when $\theta_{\mathrm{B}} = 0.5$ and when $\theta_{\mathrm{B}} = 0.2$. How much does occupancy of each of three Krüppel sites with $\theta_{\mathrm{K}} = 0.5$ reduce the activity?

   **Answer** $P(\ge 2) = 1 - (1-\theta)^5 - 5\theta(1-\theta)^4$. For $\theta = 0.5$: $1 - 1/32 - 5/32 = 26/32 = 0.81$. For $\theta = 0.2$: $1 - 0.328 - 5 \times 0.2 \times 0.410 = 1 - 0.328 - 0.410 = 0.26$. A 2.5-fold drop in occupancy lowers activity about 3-fold, steeper than linear because two activators are required. Three Krüppel sites at $\theta_{\mathrm{K}} = 0.5$ multiply activity by $(1 - 0.5)^3 = 0.125$: with several sites, moderate repressor levels already silence the enhancer, which makes the stripe border sharp.

4. Short-range repression is essential for the modular organization of the *eve* locus. What would happen to the seven-stripe pattern if Giant and Krüppel repressed over several kilobases?

   **Answer** A repressor bound in any enhancer would silence all enhancers of the locus. Wherever Krüppel or Giant is present, no stripe could form, even stripes whose own enhancers lack their sites (for example stripes 3 and 4–6, which lie in or near the *Krüppel* and *giant* domains); the pattern would be reduced to the stripes lying outside all repressor domains. Independence of the enhancers, and hence the ability to make seven stripes by adding separate elements, requires that each repressor acts only on the element to which it binds.

5. In the model of Formula 15.4.1 the off state of a parasegment boundary is stable. Which experiment in the embryo demonstrates the same property, and what does it imply for the robustness of the boundary to transient perturbations?

   **Answer** Temperature-shift experiments with **temperature-sensitive alleles** of *wingless* (or *hedgehog*): removing the function for a period after the pair-rule proteins have decayed causes permanent loss of *engrailed* in the affected cells, even when the function is restored, because no input remains to switch the loop back on. A boundary is therefore robust to fluctuations that do not drive it below the threshold of the loop, but a perturbation that does is irreversible. The bistability that gives memory also makes the stored state fragile against large transient disruptions once the initiating inputs are gone.

6. For the multilevel switch of Formula 15.2.2 with $\beta = 2$ and $\gamma = 1$, find the eigenvalues of the $(g_i, r)$ block at the state with gene $i$ on. Is the approach to that state monotonic or oscillatory?

   **Answer** $J = \begin{bmatrix} 1 & -1/c_i \\ 4c_i & -2 \end{bmatrix}$, $\operatorname{tr} J = -1$, $\det J = -2 + 4 = 2$. The eigenvalues solve $\lambda^2 + \lambda + 2 = 0$: $\lambda = (-1 \pm \mathrm{i}\sqrt{7})/2$. They are complex with negative real part $-1/2$, so the state is a stable focus: the gene and the repressor approach their steady levels with damped oscillations of angular frequency $\sqrt 7/2 \approx 1.3$ (in units of $\gamma$), independently of $c_i$.

7. *Polycomb* mutant embryos initially express the *Hox* genes in their normal domains. Design an experiment to determine when PcG function becomes necessary for maintaining *Ubx* repression in the anterior of the embryo.

   **Answer** Use a temperature-sensitive allele of a PcG gene (such as *Polycomb* or *extra sex combs*), or a conditional degradation system, and shift embryos (and larvae) to the restrictive condition at different times, then examine *Ubx* expression (by antibody staining or a reporter) in the anterior segments some hours later. Repression should be independent of PcG while the gap repressors (Hunchback) are present, during cycle 14 and gastrulation, and should require PcG from the stage at which Hunchback has decayed (about stage 10). The earliest shift that still derepresses *Ubx* marks the beginning of the maintenance phase; shifts at later stages, including larval stages, test whether maintenance is needed continuously.

8. Explain the phenotype of a fly lacking the whole bithorax complex in terms of posterior prevalence, and predict the identity of the abdominal segments in a fly lacking only *Abd-B*.

   **Answer** Without the bithorax complex, no gene more posterior than *Antp* is expressed in parasegments 5–13; *Antp*, expressed there, specifies the identity of parasegment 4 (posterior T1, anterior T2), so all these parasegments develop like it. Without *Abd-B* alone, parasegments 10–13 express *Ubx* and *abd-A* but no more posterior gene, so they take the most posterior identity that *abd-A* can specify, that of parasegment 9 (posterior A3, anterior A4): the posterior abdominal segments are transformed towards A4.

9. Why can *bicoid*, *zerknüllt* and *fushi tarazu* lie within the Antennapedia complex without being expressed colinearly, and what does this say about colinearity in *Drosophila*?

   **Answer** These genes descend from *Hox* genes (*Hox3* for *zen* and *bicoid*, a *Hox* gene related to *Antp* for *ftz*) but have acquired new roles and new regulatory elements of their own: *bicoid* is a maternal mRNA, *zen* is expressed dorsally, *ftz* in pair-rule stripes. Their positions are inherited from the ancestral cluster, their expression is not. In *Drosophila* the remaining *Hox* genes are regulated largely by their own, gene-specific regulatory regions, which is also why the cluster could be split by a large inversion without loss of colinearity; colinearity there reflects shared ancestry of the regulatory logic rather than a mechanism requiring the genes to be adjacent.

10. (Open question) The *Drosophila* segmentation cascade specifies all segments simultaneously; short-germ insects add segments from a posterior zone with an oscillating clock. Outline what changes would be needed, in terms of the genes described in this chapter, to convert a clock-based system into the *Drosophila* system, and what evidence would support such a history.

    **Answer** Points to include: the pair-rule genes are the clock components in short-germ insects (oscillating *eve*, *runt*, *odd* in *Tribolium*); in a long-germ insect their stripes must instead be positioned in space by the gap genes, which requires the acquisition of stripe-specific enhancers reading gap repressors (the modular enhancers of 15.3) and the expansion of the gap genes' role from the posterior zone to the whole blastoderm, together with a strong anterior maternal gradient (Bicoid in higher flies, a new gene). Evidence: the phylogenetic distribution of long- and short-germ development (long-germ arose independently several times), comparative expression of pair-rule genes, the conservation of the pair-rule regulatory network between *Tribolium* and *Drosophila* despite different spatial outputs (Clark and Akam), and intermediate modes in other insects. The Odd-paired switch from seven to fourteen stripes in *Drosophila* resembles a frozen step of a dynamic network.
