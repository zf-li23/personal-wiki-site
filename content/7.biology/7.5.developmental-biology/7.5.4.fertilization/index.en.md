---
title: Fertilization
description: "How sperm and egg meet, recognize each other, fuse and start development: the structure of sperm and egg and their envelopes; external fertilization in sea urchins (chemotaxis by resact and speract, the acrosome reaction, bindin and its receptor, membrane fusion, the fast electrical and slow cortical-granule blocks to polyspermy, the calcium wave and the early and late responses of egg activation, pronuclear fusion); a Poisson model of polyspermy and the trade-off between sperm limitation and polyspermy; the calcium wave as a bistable reaction–diffusion front with speed √(Dk/2)(1−2a); internal fertilization in mammals (transport, the isthmic reservoir, capacitation, hyperactivation, rheotaxis, thermotaxis and chemotaxis, the acrosome reaction and ZP2, IZUMO1–JUNO fusion, zona and membrane blocks, physiological polyspermy, PLCζ and calcium oscillations, exit from meiosis II, the pronuclei and the first spindle); and a timeline of human fertilization."
---

Fertilization has two functions. It combines the genes of two parents (sex), and it starts the development of a new organism (reproduction). These are separable: in parthenogenetic species development starts without sperm, and in some all-female salamanders the sperm of another species activates the egg without contributing genes. The process unfolds in four steps that recur in every animal: contact and recognition between sperm and egg, regulation of sperm entry so that only one sperm enters, fusion of the genetic material, and activation of the egg's metabolism. Neither partner is passive: the egg activates the sperm, and the sperm activates the egg, and both activations use calcium ions and membrane fusion. We describe the two best-studied systems, the external fertilization of sea urchins and the internal fertilization of mammals. The gametes themselves are made by meiosis and gametogenesis ([7.3.21](/7.3.21#sec-21.7.4), 7.5.27); the next chapter follows the zygote into cleavage.

## 4.1. The Gametes

**Definition 4.1.1 (Fertilization)** **Fertilization** is the fusion of a sperm and an egg, which combines a haploid set of chromosomes from each parent in one cell, the zygote, and activates the egg to begin development.

### 4.1.1. The Sperm

A sperm is a haploid nucleus with a propulsion system and a sac of enzymes; almost all its cytoplasm is discarded during its maturation. The head contains the nucleus, whose DNA is packed very tightly (in mammals by protamines instead of histones), and in front of it the acrosome, a secretory vesicle derived from the Golgi apparatus that contains enzymes able to digest proteins and complex sugars. In many species globular actin lies between the nucleus and the acrosome and polymerizes into an acrosomal process during fertilization. The flagellum is driven by the **dynein** arms of its **axoneme** (nine outer doublet microtubules around a central pair), which grows from a **centriole** at the base of the nucleus, and the ATP comes from mitochondria in the midpiece. In mammals dense outer fibres stiffen the tail. Defects of dynein cause primary ciliary dyskinesia (the Kartagener triad): affected men are sterile, patients of both sexes suffer bronchial infections, and half of them have a mirror-image arrangement of the internal organs (situs inversus), because the cilia that break left–right symmetry in the embryo are immotile too (7.5.17).

### 4.1.2. The Egg

Whereas the sperm sheds its cytoplasm, the egg accumulates it. A sea urchin egg has a volume of about 200 pl, more than ten thousand times that of the sperm; a human egg is about $120\,\mu\mathrm{m}$ across, a *Xenopus* egg $1.2\,\mathrm{mm}$, and a bird's egg yolk is a single enormous cell. The egg stores what the early embryo needs before its own genes are active:

- nutritive proteins, in many species yolk proteins made in the liver or fat body and taken up from the blood;
- ribosomes and tRNAs (amphibian oocytes make about $10^{12}$ ribosomes during meiotic prophase);
- thousands of different mRNAs, kept in a repressed state until fertilization;
- morphogenetic factors, transcription factors and paracrine factors, often localized in particular regions of the egg;
- protective substances: ultraviolet filters, DNA repair enzymes, distasteful molecules, and in bird eggs antibodies.

In most animals the egg is fertilized before meiosis is finished, so that the egg is strictly an oocyte when the sperm enters. Sea urchin eggs have completed meiosis and contain a haploid female pronucleus; most mammals are fertilized in metaphase of meiosis II, with the first **polar body** already extruded ([7.3.21](/7.3.21#sec-21.7.4)); the roundworm *Ascaris* and dogs and foxes are fertilized as primary oocytes, with the large diploid nucleus (germinal vesicle) still intact; many molluscs, annelids and insects in metaphase I.

The egg membrane is surrounded by extracellular coats.

**Definition 4.1.2 (Vitelline Envelope and Zona Pellucida)** The **vitelline envelope** is the thin glycoprotein coat attached to the egg membrane of invertebrate eggs such as those of sea urchins; it carries the receptors for species-specific sperm binding. The **zona pellucida** is the much thicker glycoprotein coat of mammalian eggs, made of three proteins in the mouse (ZP1, ZP2, ZP3) and four in humans (ZP1–ZP4), separated from the egg membrane by the perivitelline space.

Outside the vitelline envelope many eggs have a jelly coat that attracts or activates sperm; the mammalian egg is ovulated within a cloud of cumulus cells, the follicle cells that nourished it, embedded in a matrix of hyaluronan, the innermost layer of which is the corona radiata. Under the egg membrane lies the cortex, a gel rich in actin, which polymerizes at fertilization to form microvilli. In the cortex lie the cortical granules, secretory vesicles homologous to the acrosome: a sea urchin egg has about 15 000, each about $1\,\mu\mathrm{m}$ across, containing proteases, mucopolysaccharides, adhesive glycoproteins and hyalin.

![The gametes. A: a mammalian sperm (acrosome over the front of the head, condensed haploid nucleus, midpiece with a helix of mitochondria, flagellum) and a sea urchin sperm (small conical head, small acrosomal vesicle, one mitochondrion). B: a sea urchin egg with jelly coat, vitelline envelope, cortical granules under the membrane and the haploid female pronucleus. C: a mammalian egg arrested in metaphase II (spindle under the first polar body), with zona pellucida, perivitelline space, cortical granules (absent over the spindle) and cumulus cells. Not to scale](./plots/gametes.py)

## 4.2. Five Steps of Recognition

In most animals sperm and egg interact in five steps: (1) the sperm is attracted to the egg by soluble molecules the egg releases; (2) the acrosome undergoes exocytosis and releases its enzymes; (3) the sperm binds to the extracellular coat of the egg (vitelline envelope or zona pellucida); (4) it passes through this coat; (5) the sperm and egg membranes fuse. Then the nuclei can meet and the egg is activated.

## 4.3. External Fertilization in Sea Urchins

Sea urchins shed their gametes into seawater, where sperm and eggs are diluted and where several species may spawn at the same time. Two problems follow: how gametes find each other, and how fertilization by sperm of other species is prevented. Species-specific attraction and activation of sperm solve both.

### 4.3.1. Sperm Attraction and Activation

Sea urchin sperm are immotile in the testis, where a high CO₂ concentration keeps their internal pH at about 7.2; in seawater it rises to about 7.6, which activates the dynein ATPase, and the sperm begin to swim. Direction comes from sperm-activating peptides released by the egg jelly: resact (14 amino acids) from the eggs of *Arbacia punctulata*, speract (10 amino acids) from *Strongylocentrotus purpuratus*. Sperm swimming in circles of about $50\,\mu\mathrm{m}$ diameter in a drop of seawater converge within seconds on a nanolitre of 10 nM resact, and resact attracts only sperm of its own species. The peptide binds a receptor guanylyl cyclase in the sperm membrane; cyclic GMP opens potassium channels, the membrane hyperpolarizes, and the subsequent depolarization opens CatSper calcium channels, the same channels that control the swimming of mammalian sperm. Each pulse of Ca²⁺ makes the flagellar beat more asymmetric and turns the sperm; because the stimulus changes as the sperm circles in the gradient, the circles drift up the gradient (**chemotaxis**, [7.3.15](/7.3.15)). The binding of a single peptide molecule can produce a response. The peptides also raise sperm respiration and motility, so they both attract and activate.

### 4.3.2. The Acrosome Reaction

**Definition 4.3.1 (Acrosome Reaction)** The **acrosome reaction** is the exocytosis of the acrosome, in which the outer acrosomal membrane fuses with the sperm plasma membrane and releases the acrosomal enzymes, exposing the inner acrosomal membrane; in many invertebrates it is accompanied by the extension of an acrosomal process by actin polymerization.

In sea urchins the reaction is triggered by contact with the egg jelly, whose sulfated polysaccharides (in *S. purpuratus* a repeating polymer of fucose sulfate) bind receptors above the acrosome. These polysaccharides differ between species, so that in three species living together near Rio de Janeiro each species' jelly induces the reaction mainly in its own sperm: a barrier against hybrid fertilization. The receptor activates a calcium channel, a Na⁺/H⁺ exchanger (which alkalinizes the sperm) and a phospholipase that makes IP₃; the rise of Ca²⁺ in a basic cytoplasm causes the acrosomal vesicle to fuse with the plasma membrane. Proteolytic enzymes and proteasomes released from it digest a path through the jelly. Then actin, held in a non-polymerized state by profilin behind the acrosome, polymerizes into a bundle that extends the acrosomal process within seconds ([7.3.13](/7.3.13)).

### 4.3.3. Species-Specific Binding

The acrosomal process is coated with bindin, an insoluble protein of 30.5 kDa. Particles of bindin from *S. purpuratus* agglutinate dejellied eggs of their own species but not those of *S. franciscanus*, and the bindin receptor of the vitelline envelope, a large glycoprotein (EBR1, about 350 kDa), binds sperm of its own species only. Bindins and their receptors are among the most rapidly evolving proteins known: closely related species with nearly identical other proteins differ substantially in them, which suggests that the recognition of gametes is driven by selection, perhaps by conflict between sperm and egg over the risk of polyspermy, and can contribute to speciation.

### 4.3.4. Fusion

The sperm and egg membranes fuse at the tip of the acrosomal process, which can itself promote membrane fusion in vitro. The egg responds with a fertilization cone, a mound of polymerized actin that draws the sperm in through a widening cytoplasmic bridge. The sperm nucleus, centriole and a little cytoplasm enter; the mitochondria and the flagellum disintegrate, so that the mitochondria of the embryo are inherited from the mother, while in almost all animals except rodents the centrosome of the zygote derives from the sperm centriole.

### 4.3.5. Blocks to Polyspermy

**Definition 4.3.2 (Polyspermy)** **Polyspermy** is the entry of more than one sperm into an egg.

In most animals polyspermy is lethal. Theodor Boveri (1902) showed why in sea urchin eggs fertilized by two sperm: the nucleus becomes triploid, and because each sperm centriole divides, four spindle poles form instead of two, so that at the first division the 54 chromosomes (three sets of 18) are distributed randomly among up to four cells, and the blastomeres receive unbalanced sets of chromosomes and die or develop abnormally. Sea urchin eggs therefore have two successive blocks.

**Definition 4.3.3 (Fast and Slow Blocks to Polyspermy)** The **fast block to polyspermy** is an electrical block: within seconds of the fusion of the first sperm the egg membrane depolarizes, and sperm cannot fuse with a depolarized membrane. The slow block to polyspermy, the **cortical granule reaction**, is the exocytosis of the cortical granules, whose contents modify the egg coat so that it no longer binds sperm and, in sea urchins, lift and harden it into the **fertilization envelope**, an impenetrable barrier around the egg.

The resting potential of the unfertilized sea urchin egg is about $-70\,\mathrm{mV}$ (**membrane potential**, [7.3.5](/7.3.5)). Within 1–3 s of the binding of the first sperm, a small influx of Na⁺ through newly opened channels shifts it to about $+20\,\mathrm{mV}$, where it stays for about a minute. Laurinda Jaffe showed that the depolarization is the block: an egg held at a negative potential by an applied current becomes polyspermic, an egg held at a positive potential cannot be fertilized at all, and eggs fertilized in seawater with less Na⁺ (120 mM instead of about 490 mM, the rest replaced by choline) become polyspermic in almost all cases (97 % instead of about 22 % at the high sperm densities used). Frog eggs also have an electrical fast block, but because pond water contains little Na⁺ they depolarize by an efflux of Cl⁻ through a calcium-activated chloride channel (TMEM16A). Most mammals have no electrical block.

The fast block is transient and does not remove sperm already bound to the vitelline envelope. About a minute after fusion, the cortical granules fuse with the egg membrane in a wave that starts at the point of sperm entry. Their serine protease cuts the posts that attach the vitelline envelope to the membrane and clips off the bindin receptors together with the sperm bound to them; mucopolysaccharides draw in water and lift the envelope; ovoperoxidase and transglutaminase cross-link its proteins (ovoperoxidase uses hydrogen peroxide made by the egg to form dityrosine links), turning it into the hard fertilization envelope that also protects the embryo against the shear of waves; and hyalin forms the hyaline layer, which supports the blastomeres during cleavage. The envelope begins to form about 20 s after sperm attachment and is complete by the end of the first minute.

![Fertilization in the sea urchin. Top: the five steps at the egg surface: (1) attraction and activation by peptides from the jelly; (2) the acrosome reaction, with extension of the acrosomal process; (3) digestion of a path through the jelly; (4) binding of bindin to its receptor on the vitelline envelope; (5) membrane fusion and the fertilization cone. Bottom: the cortex before fertilization (cortical granules under the membrane, vitelline envelope attached by posts), during cortical granule exocytosis (15–60 s; granule contents released, posts cut, envelope lifting) and after (fertilization envelope raised and hardened, hyaline layer on the egg surface)](./plots/urchin-fertilization.py)

### 4.3.6. A Poisson Model of Polyspermy

Why are two blocks needed? Suppose fusion-competent sperm reach the egg membrane at random, independent times, at an average rate $\lambda$ that depends on the sperm density: a Poisson process, so that the waiting times between arrivals follow the **exponential distribution** ([3.1.4](/3.1.4)) and the process has no memory (**memorylessness**).

**Formula 4.3.1 (Probability of Polyspermy)** Let sperm arrive as a Poisson process of rate $\lambda$. If after the first fusion further fusions remain possible at the full rate for a time $\delta$ and at a reduced rate $\varepsilon\lambda$ until a permanent block is complete at time $T$, the probability that a fertilized egg becomes polyspermic is

$$
P_{\mathrm{poly}} = 1 - \exp\bigl[-\lambda\delta - \varepsilon\lambda(T-\delta)\bigr].
\tag{4.1}
$$
With only the slow block ($\varepsilon = 1$), $P_{\mathrm{poly}} = 1-\mathrm{e}^{-\lambda T}$. If the egg is exposed to sperm for a time $W$, the probability that it is fertilized by exactly one sperm is $P_{\mathrm{mono}} = (1-\mathrm{e}^{-\lambda W})(1-P_{\mathrm{poly}})$.

**Proof** By the memorylessness of the Poisson process, the arrivals after the first fusion are again a Poisson process, independent of the past. Further fusions in $(0,\delta)$ and in $(\delta, T)$ after the first are Poisson with means $\lambda\delta$ and $\varepsilon\lambda(T-\delta)$, so the probability of none is the exponential of minus their sum. The egg is fertilized during the exposure $W$ if at least one sperm arrives, with probability $1-\mathrm{e}^{-\lambda W}$, independently of what happens afterwards. $\square$

The arrival rate can be estimated from the encounter rate of swimming sperm with a sphere. A sperm swimming at speed $u$ in a suspension of density $n$ sweeps a volume $\pi R^2 u$ per unit time relative to an egg of radius $R$, so $\lambda \approx \pi R^2 u n$ times the fraction of encounters that lead to fusion.

**Example 4.3.1** For a sea urchin egg ($R = 40\,\mu\mathrm{m}$), sperm swimming at $u = 200\,\mu\mathrm{m\,s^{-1}}$ at a density of $10^5$ per millilitre ($10^{-7}\,\mu\mathrm{m^{-3}}$), $\lambda \approx \pi\cdot1600\cdot200\cdot10^{-7}\,\mathrm{s^{-1}} \approx 0.1\,\mathrm{s^{-1}}$ if every encounter fused. With only a slow block at $T = 60\,\mathrm{s}$, $P_{\mathrm{poly}} = 1-\mathrm{e}^{-6} \approx 0.998$: nearly every egg would be polyspermic. A fast block after $\delta = 1\,\mathrm{s}$ that reduces fusion a hundredfold ($\varepsilon = 0.01$) gives $P_{\mathrm{poly}} = 1-\mathrm{e}^{-0.1-0.059} \approx 0.15$. At a hundred times lower density ($\lambda = 0.001\,\mathrm{s^{-1}}$) polyspermy is rare even without a fast block ($6\,\%$), but then an egg exposed for 5 min is fertilized with probability only $1-\mathrm{e}^{-0.3} \approx 0.26$.

![A Poisson model of polyspermy (Formula 4.3.1). A: probability that a fertilized egg becomes polyspermic against the rate λ at which fusion-competent sperm arrive, with a slow block only (effective after 60 s) or with a fast block after 1 s that reduces fusion a hundredfold until the slow block is complete. B: for eggs exposed to sperm for 5 min, the probability of fertilization (dashed) and of fertilization by exactly one sperm (solid): normal fertilization is possible only in a window of sperm densities, which the fast block widens by about two orders of magnitude](./plots/polyspermy.py)

The model makes the evolutionary problem explicit. Externally fertilizing animals face both sperm limitation, when gametes are too dilute, and polyspermy, when they are too dense, and the probability of normal fertilization is maximal at intermediate densities. A fast block shifts the polyspermy limit to densities about $1/\varepsilon$ times higher; mammals, in which the female tract lets only a few sperm reach the egg (Section 4.4.1), can rely on slower blocks. In real eggs not every encounter leads to fusion, and the egg coat and the jelly regulate access, so the measured arrival rates are lower than the estimate.

### 4.3.7. Calcium and the Activation of the Egg

**Definition 4.3.4 (Egg Activation)** **Egg activation** is the set of changes in the egg triggered by the sperm (or, artificially, by other stimuli) that start development: the release of intracellular calcium, the cortical granule reaction, the completion of meiosis where it is arrested, the resumption of the cell cycle, and the initiation of protein and DNA synthesis.

In every animal studied, a rise of free Ca²⁺ in the egg cytoplasm triggers activation. In the sea urchin egg free Ca²⁺ rises from about $0.05$ to $1$–$5\,\mu\mathrm{M}$ in a wave that starts at the point of sperm entry and crosses the egg, visualized with calcium-sensitive dyes (aequorin, fura-2); the wave travels at about $5$–$10\,\mu\mathrm{m\,s^{-1}}$ and the whole release is over within about 30 s, after which Ca²⁺ is pumped back into the stores. Three experiments show that the calcium comes from inside the egg and is sufficient and necessary: the calcium ionophore A23187 activates eggs and causes the cortical granule reaction even in seawater without calcium; injection of Ca²⁺ or of IP₃ activates unfertilized eggs; injection of the calcium chelator EGTA prevents activation by sperm.

The calcium is released from the endoplasmic reticulum, which in sea urchin and frog eggs forms a dense network in the cortex around the cortical granules. **Phospholipase C** splits the membrane lipid PIP₂ into IP₃ and diacylglycerol (**second messenger**, [7.1.14](/7.1.14)); IP₃ opens IP₃ receptor channels in the endoplasmic reticulum, and the released Ca²⁺ opens further channels (calcium-induced calcium release), so that the release propagates itself. In sea urchins the enzyme is a PLCγ of the egg, activated through a Src kinase after sperm binding; in mammals it is brought in by the sperm (Section 4.4.6). Diacylglycerol activates protein kinase C, which activates the Na⁺/H⁺ exchanger, so that the egg pH rises by a few tenths of a unit.

A self-propagating release of this kind is a bistable medium: each region of cytoplasm has a stable low-calcium state and a stable high-calcium state, and a sufficiently large local increase switches it, and its neighbours, to the high state.

**Formula 4.3.2 (Speed of a Bistable Calcium Front)** Let $c(x,t)$ be the free calcium concentration scaled between the resting level ($0$) and the fully released level ($1$), with effective (buffered) diffusion coefficient $D$, and let calcium-induced release act as the cubic source $f(c) = kc(c-a)(1-c)$ with threshold $0<a<1/2$:

$$
\frac{\partial c}{\partial t} = D\frac{\partial^2 c}{\partial x^2} + kc(c-a)(1-c)
\tag{4.2}
$$
(a **reaction-diffusion equation**, [2.5.7](/2.5.7#sec-7.5.2)). It has a **traveling wave solution** in which the released state invades the resting state,

$$
c(x,t) = \frac{1}{1+\exp\bigl[(x-vt)/w\bigr]}, \qquad w = \sqrt{\frac{2D}{k}}, \qquad v = \sqrt{\frac{Dk}{2}}\,(1-2a).
\tag{4.3}
$$

**Proof** Put $c = U(\xi)$, $\xi = x - vt$, so that $DU'' + vU' + f(U) = 0$. Try $U = 1/(1+\mathrm{e}^{\xi/w})$, for which $U' = -U(1-U)/w$ and $U'' = U(1-U)(1-2U)/w^2$. Then

$$
DU''+vU'+f(U) = U(1-U)\Bigl[\frac{D(1-2U)}{w^2} - \frac{v}{w} + k(U-a)\Bigr].
$$
The bracket is linear in $U$; it vanishes for all $U$ if the coefficient of $U$, $-2D/w^2 + k$, and the constant term, $D/w^2 - v/w - ka$, both vanish. The first gives $w^2 = 2D/k$, the second $v = w(D/w^2 - ka) = w k(1/2 - a) = \sqrt{Dk/2}\,(1-2a)$. $\square$

The front moves into the resting region ($v>0$) only if the threshold $a$ is below one half, that is if the released state is "stronger" than the resting state; its speed grows as the square root of both diffusion and release rate, as for the Fisher–KPP equation of invasion ([2.5.7](/2.5.7#sec-7.5.2)), but unlike that front it has a threshold: a stimulus that raises calcium in too small a region decays instead of starting a wave.

**Example 4.3.2** With an effective diffusion coefficient of calcium in buffered cytoplasm $D = 20\,\mu\mathrm{m^2\,s^{-1}}$, $k = 10\,\mathrm{s^{-1}}$ and $a = 0.25$, the front width is $w = \sqrt{2\cdot20/10}\,\mu\mathrm{m} = 2\,\mu\mathrm{m}$ and the speed $v = \sqrt{100}\cdot0.5\,\mu\mathrm{m\,s^{-1}} = 5\,\mu\mathrm{m\,s^{-1}}$: the wave crosses an egg of $80\,\mu\mathrm{m}$ in about 16 s, in agreement with the measured speed of fertilization waves, which is close to $10\,\mu\mathrm{m\,s^{-1}}$ in eggs of very different sizes (Jaffe's observation of a nearly universal speed). Larger eggs therefore take longer to be activated: about 4 min for the 1.2-mm *Xenopus* egg at $5\,\mu\mathrm{m\,s^{-1}}$, 2 min at the measured $10\,\mu\mathrm{m\,s^{-1}}$.

![Calcium at fertilization. A: kymograph of a bistable calcium front (Eq. 4.2; D = 20 µm²/s, k = 10 s⁻¹, a = 0.25) started by a local release at the sperm entry point and crossing an 80-µm egg; the dashed line has the predicted slope v = 5 µm/s (Formula 4.3.2). B: calcium profiles every 3 s: a front of constant shape and speed. C: a minimal model of calcium oscillations (Goldbeter, Dupont and Berridge 1990) with a sustained level of IP₃ receptor activation β: repetitive spikes instead of one wave, at higher frequency for stronger stimulation (β = 0.3, blue; β = 0.5, orange). The model's time scale is seconds; mammalian eggs spike every 10–20 min, but the frequency coding is the same](./plots/calcium-wave.py)

The calcium release starts a programmed series of responses, early (within about a minute) and late (minutes to an hour); approximate times for sea urchins, after Whitaker and Steinhardt (1985) and Mohri and colleagues (1995):

| Response | Time after insemination |
|---|---|
| sperm–egg binding | 0 s |
| fertilization potential (fast block), membrane fusion | within 1 s |
| calcium rise first detected | 10 s |
| cortical granule exocytosis (slow block) | 15–60 s |
| activation of NAD⁺ kinase, more NADP⁺ and NADPH, rise in O₂ consumption | from 1 min |
| sperm entry | 1–2 min |
| acid efflux and rise of pH | 1–5 min |
| decondensation of sperm chromatin, migration of the sperm nucleus to the egg centre | 2–12 min |
| migration of the egg nucleus to the sperm nucleus | 5–10 min |
| activation of protein synthesis and amino acid transport | from 5–10 min |
| initiation of DNA synthesis | 20–40 min |
| mitosis | 60–80 min |
| first cleavage | 85–95 min |

NAD⁺ kinase converts NAD⁺ to NADP⁺, the coenzyme of lipid synthesis, needed for the new membranes of cleavage, and NADPH supports the cross-linking of the fertilization envelope and the regeneration of antioxidants. The late responses need both the calcium rise and the rise of pH: an artificial rise of pH alone, with ammonia, starts DNA synthesis and the burst of protein synthesis. Protein synthesis increases without new mRNA, from stored maternal messages: an inhibitor that binds the translation initiation factor eIF4E is phosphorylated and degraded, and among the mRNAs released from repression is that of cyclin B, which with Cdk1 forms the mitosis-promoting factor (**maturation-promoting factor**, [7.3.20](/7.3.20)). Calcium also inactivates MAP kinase, removing an inhibition of DNA synthesis.

![The time course of sea urchin fertilization. A: the egg membrane potential jumps from about −70 mV to about +20 mV within a second of sperm binding (the fast block) and stays positive for about a minute while the cortical granules undergo exocytosis (shaded). B: events after insemination on a logarithmic time scale, from the fertilization potential (below 1 s) to the first cleavage (about 85–95 min)](./plots/urchin-timeline.py)

### 4.3.8. Fusion of the Genetic Material

**Definition 4.3.5 (Pronucleus)** A **pronucleus** is the haploid nucleus of a sperm (male pronucleus) or of an egg (female pronucleus) in the zygote, before the two genomes come together.

In the egg cytoplasm the sperm nuclear envelope breaks down, egg kinases phosphorylate the sperm-specific histones, which are replaced by cleavage-stage histones from the egg, and the chromatin decondenses into the male pronucleus. The sperm nucleus rotates by $180^\circ$ so that the centriole lies between it and the egg pronucleus; the centriole nucleates microtubules that join egg microtubules in a sperm aster, Hertwig's "sun in the egg", which reaches the female pronucleus, and the two pronuclei move towards each other along the microtubules and fuse into the diploid zygote nucleus.

## 4.4. Internal Fertilization in Mammals

Mammalian fertilization occurs inside the oviduct, among a heterogeneous population of sperm, of which very few reach the egg; it is harder to study, and several of its steps were revised in the 2010s.

### 4.4.1. Getting the Gametes Together

The female tract is not a passive conduit: it regulates the transport and maturation of both gametes. The fimbriae of the oviduct pick up the ovulated egg with its cumulus (the complex is not taken up if the cumulus matrix is removed), and cilia and muscle contractions move it to the ampulla, where fertilization takes place. Of about $2$–$3\times10^8$ human sperm ejaculated, only about one in a million enters the oviducts, and a few hundred reach the vicinity of the egg. The sperm are moved by several processes at different times:

- their own motility, needed to pass the cervical mucus (in species whose females mate with several males, sperm of one male can form "trains" that swim faster);
- contractions of the uterus, which bring sperm into the oviducts of mice, hamsters, cows and humans within 30 min, faster than they could swim;
- rheotaxis: sperm swim against the flow of fluid from the oviduct, sensing it through CatSper calcium channels.

Before entering the ampulla, uncapacitated sperm bind to the epithelium of the narrow isthmus of the oviduct and are released when they become capacitated. This sperm reservoir prolongs their life (human sperm can fertilize for typically up to 3 days, at most about 5, after intercourse, and nearly all conceptions follow intercourse in the 6 days ending on the day of ovulation) and limits the number of sperm that reach the egg at the same time; when the isthmus is removed in cows, polyspermy increases.

### 4.4.2. Capacitation and Hyperactivation

**Definition 4.4.1 (Capacitation)** **Capacitation** is the set of physiological changes that mammalian sperm undergo during their residence in the female reproductive tract and that make them able to undergo the acrosome reaction, to respond to guidance cues and to fertilize the egg.

Freshly ejaculated mammalian sperm cannot fertilize an egg (Chang and Austin, 1951); this discovery made in vitro fertilization possible, since sperm must be capacitated in a suitable medium. Capacitation involves the removal of cholesterol from the sperm membrane by albumin, which increases its fluidity; the loss of glycoproteins that had been adsorbed in the male tract; hyperpolarization of the membrane by K⁺ efflux; influx of bicarbonate and Ca²⁺, which activate the soluble adenylyl cyclase of the sperm (ADCY10, also called sAC) and raise cAMP; activation of protein kinase A and then of tyrosine phosphorylation of many proteins; alkalinization; and the relocation of proteins such as IZUMO1 to the surface of the head. Capacitation may be transient: sperm may have only a limited window of competence once capacitated.

**Definition 4.4.2 (Hyperactivation)** **Hyperactivation** is the change of the beat of capacitated mammalian sperm from a symmetric, low-amplitude beat to an asymmetric, high-amplitude whip-like beat that generates more force; it depends on Ca²⁺ entry through the sperm-specific CatSper channels of the flagellum.

Hyperactivation releases sperm from the oviduct epithelium and, with the hyaluronidase PH-20 on the sperm surface, lets them push through the cumulus. Three calcium-mediated guidance mechanisms bring them to the egg: rheotaxis over long distances, thermotaxis over the intermediate range (capacitated sperm can detect temperature differences of about $0.014\,^\circ\mathrm{C}$ over a millimetre and swim towards the ampulla, which is about $2\,^\circ\mathrm{C}$ warmer than the isthmus), and chemotaxis within a millimetre or so of the egg. Human sperm respond to progesterone from the cumulus cells, which opens CatSper indirectly: it activates the lipid hydrolase ABHD2, which removes an endocannabinoid that inhibits the channel. Only capacitated sperm respond to these cues, and the egg seems to release its attractants only when it can be fertilized.

### 4.4.3. The Acrosome Reaction and the Zona Pellucida

The classical model of mammalian fertilization, based on the mouse, held that acrosome-intact sperm bind to the carbohydrates of ZP3 (by a sperm galactosyltransferase or other lectins), that ZP3 then triggers the acrosome reaction on the zona, and that the reacted sperm bind ZP2 before penetrating. Two lines of evidence changed this picture:

- Timing. Mouse sperm whose acrosomes were labelled with green fluorescent protein showed that the sperm that fertilized eggs had already undergone the acrosome reaction before they reached the zona, in the cumulus or even in the upper isthmus; sperm that reacted on the zona almost always failed (Jin and colleagues, 2011; La Spina and colleagues, 2016).
- The ligand. Human sperm do not bind mouse eggs, but they bind mouse eggs whose zona contains human ZP2, and not those with human ZP1, ZP3 or ZP4 (Baibakov and colleagues, 2012); a region near the N terminus of ZP2 (amino acids 51–149 in the mouse) is required for binding (Avella and colleagues, 2014).

The present view is therefore that most fertilizing sperm undergo the acrosome reaction before reaching the zona and bind to the N-terminal domain of ZP2, whose cleavage after fertilization prevents further binding (Section 4.4.5); acrosome-intact binding to ZP3 may occur but is not required. The physical force of hyperactivated motility, more than the digestion of the zona by acrosomal enzymes, carries the sperm through: mice lacking acrosin, the main acrosomal protease, are fertile.

### 4.4.4. Gamete Fusion

Mammalian sperm do not meet the egg membrane with their tip, as sea urchin sperm do, but lie alongside it, and fusion begins at the equatorial segment, where the inner acrosomal membrane exposed by the acrosome reaction meets the plasma membrane. The egg membrane over the meiotic spindle lacks microvilli and is not used.

On the sperm, the immunoglobulin-superfamily protein IZUMO1, which moves after the acrosome reaction from the acrosomal membrane to the equatorial segment, is essential: *Izumo1*-null sperm penetrate the zona but cannot fuse (Inoue and colleagues, 2005). Its receptor on the egg is JUNO, a GPI-anchored protein of the folate-receptor family (Bianchi and colleagues, 2014); eggs without JUNO cannot fuse with sperm, and the interaction is conserved in humans. The tetraspanin CD9 on the egg microvilli is also required. IZUMO1–JUNO binding, with a dissociation constant in the micromolar range, mediates adhesion; fusion itself needs further sperm proteins identified by knockout mice since 2020 (SPACA6, TMEM95, SOF1, FIMP, DCST1 and DCST2), some of which form a complex with IZUMO1, and the fish egg protein Bouncer, which confers species specificity in zebrafish and medaka, plays a role analogous to JUNO. The protein that actually merges the two membranes in vertebrates is not known (plants and many protists use a fusogen, HAP2, that vertebrates lack).

### 4.4.5. Blocks to Polyspermy in Mammals

Polyspermy occurs in about 1–2 % of human eggs fertilized in vivo and more often in vitro, and is lethal (it is one source of triploid conceptions). Mammals rely on the small number of sperm that reach the egg and on slow blocks that develop over tens of minutes:

- Zona block: cortical granule exocytosis releases the metalloprotease ovastacin, which cleaves ZP2 near its N terminus, so that the zona no longer binds sperm (Burkart and colleagues, 2012). Mice whose ZP2 cannot be cleaved bind sperm to the zona of 2-cell embryos and show more polyspermy, but are only partly infertile, so other modifications of the zona also contribute, among them the binding of zinc released from the egg at activation (the "zinc spark") to the zona.
- Membrane block: JUNO is shed from the egg membrane, in vesicles, within about 40 min of fertilization; soluble JUNO in the perivitelline space may also bind and neutralize other sperm. Zona-free eggs fertilized in vitro resist a second dose of sperm, which shows that the membrane block exists independently of the zona.

**Definition 4.4.3 (Physiological Polyspermy)** **Physiological polyspermy** is the normal entry of several sperm into an egg, as in birds, many insects, urodele amphibians, reptiles and elasmobranch fishes, in which only one male pronucleus fuses with the female pronucleus while the others degenerate.

A bird egg can contain dozens of male pronuclei. In the newt *Cynops pyrrhogaster*, the female pronucleus is surrounded by factors needed to organize microtubules (Aurora A and Cdk1); these are recruited to the centrosome of the male pronucleus nearest to it, whose aster grows towards and engulfs the female pronucleus; the other male pronuclei, deprived of these limited resources, form small asters, cannot approach the female pronucleus and degenerate. In birds, sperm DNA outside the region of the female pronucleus may be destroyed by DNases of the egg cytoplasm.

![Fertilization in mammals. A: the route of sperm through the female tract (schematic), with approximate numbers, the isthmic reservoir where sperm capacitate, and the ranges of the three guidance mechanisms: uterine contractions and rheotaxis, thermotaxis towards the warmer ampulla, chemotaxis near the egg. B: at the egg: hyperactivated sperm pass the cumulus, acrosome-reacted sperm bind ZP2 and cross the zona pellucida, and fusion begins at the equatorial segment through IZUMO1 and JUNO. C: blocks to polyspermy: cortical granule exocytosis releases ovastacin, which cleaves ZP2; JUNO is shed from the egg membrane; the zinc spark and calcium oscillations accompany activation](./plots/mammal-fertilization.py)

### 4.4.6. Activation of the Mammalian Egg

In mammals the sperm sets off not a single wave but a series of Ca²⁺ spikes, every 10–20 min in the mouse, which continue for several hours until the pronuclei form. The trigger is a sperm protein, phospholipase C zeta (PLCζ). The first evidence came from intracytoplasmic sperm injection (ICSI), the clinical technique in which a sperm is injected directly into the egg, bypassing all membrane interactions: to the surprise of those who had thought binding to an egg receptor essential, the injected eggs were activated and developed. Extracts of sperm, and the mRNA or protein of PLCζ, cause calcium oscillations when injected into eggs; removing PLCζ from sperm abolishes their calcium-releasing activity; and men whose sperm lack functional PLCζ, because of mutations in *PLCZ1*, are infertile with eggs that fail to activate after ICSI. PLCζ is unusually sensitive to Ca²⁺ and acts on PIP₂ in internal membranes of the egg, so that it produces IP₃ throughout the egg once it is delivered. Sperm from mice lacking *Plcz1* do not trigger oscillations, yet some of the eggs they fertilize are activated and develop, at a reduced rate and with frequent polyspermy, which shows that other sperm factors can partly substitute.

The oscillations, not a single rise, are how the egg decodes the signal: the number, amplitude and duration of the spikes regulate the events of activation, so that cortical granule exocytosis needs fewer spikes than the exit from meiosis and the recruitment of maternal mRNAs. A sustained production of IP₃ is converted into repetitive spikes by the feedback of calcium on its own release and re-uptake, as minimal models show (panel C of the calcium figure in Section 4.3.7). Influx of extracellular Ca²⁺ during the oscillations refills the stores and is needed to complete meiosis: if it is blocked, the second polar body does not form and the egg has two female pronuclei.

The mammalian egg is held in metaphase II by cytostatic factor, whose key component Emi2 inhibits the anaphase-promoting complex (APC/C), so that cyclin B and securin are stable and MPF stays active ([7.3.21](/7.3.21#sec-21.7.4)). Calcium activates calmodulin-dependent protein kinase II, which marks Emi2 for destruction; the APC/C then degrades cyclin B and securin, MPF falls, the sister chromatids separate, and the second polar body is extruded. The Mos–MEK–MAP kinase pathway is inactivated more slowly, which is needed for the pronuclei to form. Zinc is part of the same switch: the egg accumulates zinc during maturation and loses about a fifth of it in the zinc spark, and the fall in zinc is needed to escape metaphase II. In amphibians MPF and CSF are regulated in the same way: MPF activity is high in the egg arrested in metaphase II, falls abruptly at fertilization, and then oscillates with the cleavage cycles.

### 4.4.7. The Pronuclei and the First Spindle

The protamines of the sperm chromatin are reduced by glutathione in the egg cytoplasm, which breaks their disulfide bonds, and are replaced by maternal histones (largely the variant H3.3, deposited by the chaperone HIRA). The paternal genome is then actively demethylated, by oxidation of 5-methylcytosine by the dioxygenase TET3, while the maternal genome loses its methylation more slowly, by dilution during replication (**DNA methylation**; the protection of imprinted genes from this reprogramming is described in [7.4.18](/7.4.18)). DNA is replicated separately in the two pronuclei. Pronuclear migration takes about 12 hours, compared with less than an hour in the sea urchin. The pronuclei do not fuse: when they meet, their envelopes break down and the chromosomes assemble on the first mitotic spindle, so that a single diploid nucleus first appears at the 2-cell stage; in the mouse, each set of parental chromosomes even assembles its own half-spindle before the two merge (Reichmann and colleagues, 2018). In humans the sperm centriole organizes the zygote's centrosome, as in most animals; mouse sperm lose their centrioles, and the mouse zygote builds its first spindles from maternal microtubule-organizing centres. Paternal mitochondria are marked and degraded, so mitochondrial DNA is inherited maternally ([7.4.11](/7.4.11)).

### 4.4.8. A Timeline of Human Fertilization

| Time | Event |
|---|---|
| ovulation | egg in metaphase II with the first polar body, released with its cumulus; fertilizable for about 12–24 h |
| hours after insemination | capacitation in the female tract; release from the isthmic reservoir |
| 0 | sperm fuses with the egg in the ampulla; Ca²⁺ oscillations begin |
| minutes | cortical granule exocytosis; zona and membrane blocks over the following tens of minutes |
| about 2–3 h | completion of meiosis II; second polar body |
| about 4–7 h | male and female pronuclei visible |
| about 15–24 h | pronuclei meet at the centre; envelopes break down (syngamy) |
| about 24–30 h | first cleavage |

In clinical in vitro fertilization the presence of two pronuclei and two polar bodies at 16–18 h is checked as evidence of normal fertilization; three pronuclei indicate polyspermy or failure to extrude the second polar body. ICSI is used when sperm are few or cannot penetrate the zona; eggs that fail to activate after ICSI can sometimes be activated artificially with a calcium ionophore (assisted reproduction, 7.5.5).

## Summary

- Fertilization combines two haploid genomes and activates the egg (Definition 4.1.1); it proceeds by recognition, regulated entry, fusion of the genetic material and egg activation, and each gamete activates the other.
- The sperm is a condensed haploid nucleus with an acrosome, a midpiece with mitochondria and a dynein-driven flagellum; the egg stores nutrients, ribosomes, mRNAs, determinants and protective molecules, is usually fertilized before meiosis is complete, and is surrounded by a vitelline envelope or zona pellucida (Definition 4.1.2) and, in mammals, cumulus.

| Step | Sea urchin | Mammal |
|---|---|---|
| attraction | resact, speract → guanylyl cyclase, CatSper | rheotaxis, thermotaxis, chemotaxis (progesterone) |
| maturation of sperm | activation in seawater | capacitation, hyperactivation (Definitions 4.4.1, 4.4.2) |
| acrosome reaction (Definition 4.3.1) | on contact with jelly (fucose sulfate) | mostly before reaching the zona |
| binding | bindin ↔ EBR1 on vitelline envelope | N-terminal ZP2 of the zona |
| fusion | tip of acrosomal process; fertilization cone | equatorial segment; IZUMO1–JUNO, CD9 |
| fast block | depolarization to +20 mV in 1–3 s (Na⁺) | absent |
| slow block | cortical granules → fertilization envelope | ovastacin cleaves ZP2; JUNO shed; zinc |
| Ca²⁺ trigger | one wave; PLCγ of the egg | oscillations for hours; PLCζ from the sperm |
| pronuclei | fuse into a zygote nucleus | meet on the first spindle |

- Polyspermy (Definition 4.3.2) is lethal because of extra centrosomes and unbalanced chromosomes; fast and slow blocks (Definition 4.3.3) act in sequence. With Poisson arrival of sperm, $P_{\mathrm{poly}} = 1-\exp[-\lambda\delta-\varepsilon\lambda(T-\delta)]$ (Formula 4.3.1, Example 4.3.1): normal fertilization lies in a window of sperm densities that the fast block widens.
- Egg activation (Definition 4.3.4) is triggered by IP₃-induced Ca²⁺ release that propagates as a bistable front, $v = \sqrt{Dk/2}\,(1-2a)$, about $5$–$10\,\mu\mathrm{m\,s^{-1}}$ (Formula 4.3.2, Example 4.3.2), followed by early (blocks, NADP⁺, pH) and late (protein and DNA synthesis, cleavage) responses.
- In mammals, Ca²⁺ oscillations destroy Emi2, activate APC/C and complete meiosis II; the pronuclei (Definition 4.3.5) replicate separately and meet on the first spindle. Physiological polyspermy (Definition 4.4.3) is resolved by selection of one male pronucleus.

## Questions

1. Why is the sea urchin egg's fast block electrical rather than chemical, and how did Jaffe show that depolarization is sufficient and necessary to prevent sperm fusion?

   **Answer** An electrical change of the whole membrane can spread over the entire egg surface within a second, much faster than exocytosis or the diffusion of molecules; it is reversible and transient, which suffices until the slow block is complete. Jaffe clamped the membrane potential of eggs with an applied current: eggs held at positive potentials could not be fertilized (depolarization is sufficient to block fusion), and eggs held at negative potentials after the first fusion became polyspermic (depolarization is necessary). Lowering Na⁺ in the seawater, which reduces the depolarization, also caused polyspermy.

2. Using Formula 4.3.1, how strong must the fast block be ($\varepsilon$) to keep polyspermy below 5 % at $\lambda = 0.1\,\mathrm{s^{-1}}$, with $\delta = 1\,\mathrm{s}$ and $T = 60\,\mathrm{s}$? Is a delay of $\delta = 1\,\mathrm{s}$ short enough?

   **Answer** We need $\lambda\delta + \varepsilon\lambda(T-\delta) \le -\ln 0.95 = 0.0513$. But $\lambda\delta = 0.1$ alone exceeds this, so no value of $\varepsilon$ suffices: with a 1-s delay, about $1-\mathrm{e}^{-0.1} = 9.5\,\%$ of eggs would be polyspermic even with a perfect fast block. The delay must be shorter: with $\delta = 0.3\,\mathrm{s}$, $\lambda\delta = 0.03$, leaving $0.021$ for $\varepsilon\cdot0.1\cdot59.7$, so $\varepsilon \le 0.0035$. The measured depolarization within 1–3 s is therefore barely fast enough at such densities, and real fusion rates must be lower (most encounters do not lead to fusion), or eggs at such sperm densities do become polyspermic, as in the laboratory at high sperm concentrations.

3. For the Poisson model, at what arrival rate is the probability of monospermic fertilization maximal for an egg exposed for a time $W$ with only a slow block at $T$? Evaluate for $W = 300\,\mathrm{s}$, $T = 60\,\mathrm{s}$.

   **Answer** $P_{\mathrm{mono}} = (1-\mathrm{e}^{-\lambda W})\mathrm{e}^{-\lambda T}$. Setting the derivative to zero: $W\mathrm{e}^{-\lambda W}\mathrm{e}^{-\lambda T} - T(1-\mathrm{e}^{-\lambda W})\mathrm{e}^{-\lambda T} = 0$, so $\mathrm{e}^{-\lambda W} = T/(W+T)$ and $\lambda^* = \ln(1+W/T)/W$. With $W = 300\,\mathrm{s}$, $T = 60\,\mathrm{s}$: $\lambda^* = \ln 6/300 \approx 0.006\,\mathrm{s^{-1}}$, and $P_{\mathrm{mono}} = (5/6)\cdot6^{-1/5} \approx 0.58$, the maximum of the yellow curve in panel B.

4. Show that a stimulus confined to a very small region does not start a calcium wave in the bistable model, while in the Fisher–KPP model any positive stimulus eventually spreads. Why is a threshold useful for an egg?

   **Answer** In the bistable model (Eq. 4.2) the resting state $c = 0$ is stable to small perturbations ($f'(0) = -ka < 0$): a small region raised above $a$ loses calcium by diffusion to its surroundings faster than release can make more, if the region is smaller than a critical size of the order of the front width $w$, so the perturbation decays. In the Fisher–KPP equation $f'(0) > 0$, so any small positive perturbation grows and spreads. A threshold protects the egg from accidental activation by small local fluctuations of calcium (mechanical stress, spontaneous channel openings), while a sperm, which delivers a large local stimulus, reliably triggers the wave.

5. Estimate the time a fertilization wave at $10\,\mu\mathrm{m\,s^{-1}}$ needs to cross a mouse egg ($80\,\mu\mathrm{m}$), a *Xenopus* egg ($1.2\,\mathrm{mm}$) and a hen's egg yolk ($\approx 30\,\mathrm{mm}$). What does this suggest about activation in very large eggs?

   **Answer** About 8 s, 2 min and 50 min. For the yolk the time would be impractically long and inhomogeneous; very large meroblastic eggs (birds) are activated by several sperm (physiological polyspermy), each starting a wave locally, and only the small disc of cytoplasm at the animal pole needs to be activated.

6. Design experiments to show that mammalian sperm-induced calcium oscillations are triggered by a soluble sperm factor rather than by sperm binding to an egg receptor.

   **Answer** Inject a sperm (ICSI) or a sperm extract into the egg cytoplasm, bypassing the membrane: oscillations still occur, so membrane binding is not required. Fractionate the extract, show that the active component is a protein that can be depleted with antibodies to PLCζ, and that injection of PLCζ mRNA or recombinant protein causes oscillations, while catalytically inactive PLCζ does not. Show that sperm from *Plcz1* mutant males, or human sperm with *PLCZ1* mutations, fail to cause oscillations after injection. Conversely, binding of sperm to the egg membrane without fusion (for example sperm lacking IZUMO1 cannot fuse) causes no oscillations.

7. In repeated ICSI cycles of a couple, the injected sperm heads are found inside the eggs, but the eggs never extrude a second polar body or form pronuclei. The woman's eggs are activated normally by sperm of a donor. Which molecule would you suspect, and what treatment might help?

   **Answer** The eggs can be activated, so the defect lies in the sperm's activating factor: one suspects absent or nonfunctional PLCζ (mutations in *PLCZ1*), which is needed to trigger the calcium oscillations that destroy Emi2 and complete meiosis II. Injecting the sperm into mouse eggs and measuring calcium (a heterologous activation test), or measuring PLCζ protein in the sperm, would confirm it; artificial oocyte activation with a calcium ionophore immediately after ICSI can rescue fertilization in such cases.

8. Why are bindin and its receptor, and mammalian ZP2 and IZUMO1, among the fastest-evolving proteins, and what is the consequence for speciation?

   **Answer** Gamete recognition proteins are under continuing selection: in dense spawning populations, eggs gain from receptors that reduce polyspermy, and sperm from variants that bind faster, an evolutionary conflict that drives repeated changes in both partners; recognition also mediates choice against heterospecific sperm where related species spawn together (reinforcement). Rapid divergence in these proteins makes the gametes of recently separated populations incompatible, which can create reproductive isolation quickly and contribute to speciation.

9. Why must the sea urchin egg cut the bindin receptors and lift the vitelline envelope, when the fast block already prevents fusion?

   **Answer** The fast block lasts only about a minute, while many sperm remain bound to the envelope; once the membrane repolarizes they could fuse. Cutting the receptors releases the bound sperm and prevents new binding; lifting and hardening the envelope makes a permanent physical barrier that also protects the embryo mechanically. The two blocks thus combine speed (electrical) and permanence (structural).

10. (Experimental logic.) A mouse mutant has eggs with normal zonae and normal IZUMO1–JUNO binding, but its eggs become polyspermic. Suggest three possible defects and how to distinguish them.

    **Answer** (i) No cortical granule exocytosis (or no ovastacin): test whether ZP2 is cleaved after fertilization (a shift in its size on immunoblots) and whether sperm bind the zona of 2-cell embryos. (ii) No membrane block: JUNO remains on the egg membrane after fertilization; test by reinseminating zona-free fertilized eggs and by staining for JUNO. (iii) Defective egg activation (weak calcium oscillations, which are needed for cortical granule exocytosis): measure calcium signals after fertilization and test whether artificial activation (ionophore, strontium) restores the blocks. A combination may also apply; the mutant gene's expression and function would point to which.
