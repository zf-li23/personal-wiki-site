---
title: "Animal Architecture II: Size, Support, Movement, and Exchange"
description: Size and scaling, and the limit that diffusion sets on body form; skeletons (hydrostatic, exoskeleton, endoskeleton) with the Clark–Cowey model of worms reinforced by helical fibers and the materials of skeletons; locomotion at low and high Reynolds number; feeding types and the three kinds of digestive system; gas exchange and circulation; protonephridia, metanephridia and Malpighian tubules and the filtration–reabsorption principle; types of nervous system; asexual and sexual reproduction. A catalog of design solutions that later chapters take up phylum by phylum.
---

Every animal must solve the same practical problems: it must hold its shape and move, obtain food and digest it, take up oxygen and give off carbon dioxide, distribute substances within the body, get rid of nitrogenous waste while keeping its water and salts in balance, coordinate its parts and reproduce. The previous chapter ([7.17.3](/7.17.3)) described the overall architecture of the body; this one surveys the solutions animals have evolved for each of these problems, as a catalog to which the chapters on the individual phyla will refer. A single physical constraint runs through the catalog: as an animal grows, its volume increases faster than its surface, and diffusion, which serves small animals well, becomes too slow. The physiology of each system is the subject of animal physiology ([7.14](/7.14)); here we stress the structural types and how they are distributed among the phyla.

## 4.1. Size and Its Consequences

### 4.1.1. Surface and Volume

If an animal changes size while keeping its shape (geometric similarity), all its lengths scale with a characteristic length $L$, its surface areas with $L^2$ and its volume and mass with $L^3$. The surface available per unit volume therefore falls as $1/L$. A tenfold increase in length gives a thousandfold increase in mass, which must be supported and supplied with oxygen, but only a hundredfold increase in the area across which oxygen and food enter and wastes leave, and in the cross-sectional area of the legs that carry it. Galileo already noted that large animals cannot simply be scaled-up small ones: their bones must be disproportionately thick.

Living animals deviate from geometric similarity in systematic ways (**allometry**, [7.5.34](/7.5.34)), and their metabolic rate does not rise in proportion to mass but approximately as its three-quarter power (**Kleiber's law**, [7.14.30](/7.14.30)). Both are partly responses to the surface–volume constraint, which has shaped animal body plans at every level.

### 4.1.2. The Limit of Diffusion

How large can an animal be if oxygen reaches its tissues only by diffusion from the surface? For a body that consumes oxygen at a rate $M$ per unit volume, with a diffusion coefficient $D$ in the tissue and a concentration $c_0$ at the surface, the steady-state diffusion equation gives a maximum radius $R_{\max} = \sqrt{6Dc_0/M}$ for a sphere, $\sqrt{4Dc_0/M}$ for a long cylinder and a maximum half-thickness $\sqrt{2Dc_0/M}$ for a flat sheet (derived in [7.14.17](/7.14.17#sec-17.2.4)). With realistic values, an actively metabolizing spherical animal cannot be much larger than about 1 mm in radius (see the figure below).

![The maximum size of an animal supplied with oxygen by diffusion alone, as a function of its oxygen consumption per unit volume, for three body shapes (logarithmic axes; $D = 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$, $c_0 = 0.25\,\mathrm{mol\,m^{-3}}$ as in 7.14.17). The vertical lines mark the average consumption of human tissue and one ten times lower, typical of flatworms and the living tissue of jellyfish. Because the limit scales only as the inverse square root of the metabolic rate, a tenfold reduction of metabolism raises the limit only about threefold, whereas a change of shape (sheet or thin cylinder) removes the limit in one or two dimensions](./plots/diffusion-limit.py)

The figure explains several body plans as solutions to the same problem:

- Flattening: flatworms can be centimeters long and wide but are rarely more than a few tenths of a millimeter thick, because every cell lies close to the surface ([7.17.11](/7.17.11)).
- Elongation: thin, long bodies, such as those of nemerteans and nematodes, keep the radius small.
- A metabolically inert core: in medusae and ctenophores most of the volume is mesoglea, which consumes almost no oxygen, so the living tissue forms thin layers on its surfaces ([7.17.2](/7.17.2#def-2.4.2)).
- Bringing the environment inside: sponges pump water through canals lined by choanocytes, and cnidarians circulate water through a branched **gastrovascular cavity**.
- Internal transport: larger, active animals have specialized exchange surfaces of large area (gills, lungs, **tracheal systems**) and a circulatory system that carries oxygen by bulk flow, faster than diffusion over any distance beyond about a millimeter.

## 4.2. Support: Skeletons

### 4.2.1. Three Types of Skeleton

A skeleton transmits the force of muscles, which can only pull by shortening, so that one muscle can be stretched again by another (its antagonist), and it maintains the shape of the body against gravity and the forces of the environment. Three types are recognized:

| Type | Principle | Examples |
|---|---|---|
| **Hydrostatic skeleton** | An enclosed volume of incompressible fluid transmits muscle force; contraction of circular muscles lengthens the body, of longitudinal muscles shortens it | Cnidarian polyps, nemerteans, nematodes, annelids, the feet and siphons of molluscs, tube feet of echinoderms |
| **Exoskeleton** | A rigid covering secreted by the epidermis; muscles attach to its inner surface and move its articulated parts | Arthropod cuticle, mollusc shells, brachiopod valves, coral skeletons |
| Endoskeleton | Rigid elements inside the body, usually of mesodermal origin, covered by soft tissue; muscles attach outside them | Sponge spicules, echinoderm ossicles, vertebrate cartilage and bone, cephalopod cartilage |

The three are not exclusive. Every animal with soft tissues uses hydrostatic principles somewhere: the tongue and trunk of mammals are muscular hydrostats, in which the muscle tissue itself is the incompressible volume, and so are the arms of octopuses. Arthropods extend the legs of spiders by hemolymph pressure, and many larvae are hydrostatic animals inside a thin cuticle.

### 4.2.2. Worms Reinforced by Helical Fibers: the Clark–Cowey Model

A cylindrical worm with a hydrostatic skeleton faces a geometric problem: if it shortens, it must become thicker, because its volume is constant, and its body wall must allow this without kinking. Many worms solve it with a lattice of inextensible fibers, collagen in the body wall of nemerteans and flatworms or in the cuticle of nematodes, wound around the body in two opposite helices. R. B. Clark and J. B. Cowey (1958) analyzed what such a lattice permits.

**Formula 4.2.1 (Volume Enclosed by a Helical Fiber Lattice)** Let a fiber of fixed length $D$ make one complete turn around a cylinder at the angle $\theta$ to its long axis. The turn spans a length $l = D\cos\theta$ of the body and a circumference $2\pi r = D\sin\theta$, so the volume enclosed by one turn is

$$
V(\theta) = \pi r^2 l = \frac{D^3}{4\pi}\,\sin^2\theta\,\cos\theta .
\tag{4.1}
$$

The volume is greatest where $\mathrm{d}V/\mathrm{d}\theta = 0$, that is at $\tan\theta = \sqrt{2}$, $\theta = 54^\circ 44'$; the aspect ratio of the cylinder is $l/2r = \pi\cot\theta$.

:::

A real worm has a fixed volume smaller than this maximum (see the figure below). At its fixed volume the worm can keep a circular cross section only between the two fiber angles where $V(\theta)$ equals its volume: it cannot elongate beyond the smaller angle, because the fibers are then nearly straight along the body, and if it contracts beyond the larger angle the lattice encloses more volume than the worm contains and the body must flatten, its cross section becoming elliptical.

![The Clark–Cowey model. Left: the volume enclosed by a cylinder wound with inextensible helical fibers, relative to its maximum, as a function of the fiber angle $\theta$ to the long axis (Eq. (4.1)); it peaks at $54^\circ 44'$. For a worm of fixed volume (horizontal line, here an illustrative 0.4 of the maximum) a circular cross section is possible only between the two angles where the curve meets the line; elongation stops at the smaller angle, and below the larger one the body must flatten. Right: cylinders drawn to the aspect ratios that correspond to three fiber angles, with the crossing fibers](./plots/clark-cowey.py)

The model explains differences among worms that measurements confirm. Nemerteans, which can stretch to many times their contracted length, have a volume close to the maximum curve over a wide range of fiber angles and remain nearly round in section; turbellarian flatworms have a volume far below the curve and are flat at every length, so their fiber lattice limits extension but not flattening. Nematodes, at the other extreme, have a high internal pressure and a cuticle whose fibers make an angle of about $75^\circ$ with the axis; their length changes little, and they move by dorsoventral bending rather than by changing length ([7.17.17](/7.17.17)). The same geometry governs the arrangement of collagen in shark skin and in the walls of arteries and the notochord ([7.17.43](/7.17.43)).

### 4.2.3. Skeletal Materials

| Material | Composition | Where |
|---|---|---|
| Collagen | Fibrous protein, often cross-linked | Body walls of worms, cuticle of annelids and nematodes; organic matrix of bone; spongin of sponges |
| **Chitin** | Polysaccharide of N-acetylglucosamine, combined with proteins | Arthropod cuticle; chaetae of annelids; radula and beaks of molluscs; perisarc of hydroids |
| Calcium carbonate | Calcite or aragonite in an organic matrix | Mollusc shells, coral skeletons, echinoderm ossicles, calcareous sponges, crustacean cuticle (with chitin), brachiopods |
| Silica | Hydrated amorphous silica | Spicules of glass sponges and demosponges only |
| Calcium phosphate | Hydroxyapatite in a collagen matrix | Vertebrate bone, dentine and enamel; shells of lingulid brachiopods |

Mineralized skeletons appeared in many lineages independently near the beginning of the Cambrian, about 550–520 million years ago (the "small shelly fauna" and the **Cambrian explosion**, [7.10.29](/7.10.29#sec-29.4)). A hard skeleton gives protection, attachment for muscles, and greater size on land, at the price of the need to grow by molting (arthropods), by adding to the margin (molluscs, brachiopods) or by internal remodeling (vertebrates).

## 4.3. Movement

### 4.3.1. Mechanisms of Locomotion

Animals move by four basic mechanisms:

- Amoeboid movement: extension of pseudopodia by actin polymerization ([7.14.2](/7.14.2)). It moves single cells within animals (white blood cells, the archaeocytes of sponges, migrating embryonic cells) and perhaps the whole body of placozoans.
- Ciliary and flagellar movement: beating of cilia moves small animals (larvae, ctenophores, small flatworms and gastrotrichs) and drives water or mucus over surfaces. Ciliary swimming is limited to animals of a few millimeters at most; ctenophores, up to about a meter, are the largest animals that swim by cilia, which are fused into comb plates.
- Hydrostatic locomotion: muscles acting on a hydrostatic skeleton. Burrowing earthworms alternate contraction of circular muscles (segments become long and thin and extend forward) with contraction of longitudinal muscles (segments become short and thick and anchor against the burrow with their chaetae), in waves that pass backward along the body (**peristalsis**, made possible by the septa that divide the coelom). Jellyfish, squid and scallops swim by jet propulsion.
- Muscles and articulated skeletons: limbs acting as levers, as in arthropods (muscles inside the tubular segments, attached to the cuticle through internal ingrowths called apodemes) and vertebrates (muscles outside the bones). Undulation of the whole body, by alternating contraction of muscles on the two sides acting on the notochord or vertebral column, propels fishes, snakes and nematodes.

### 4.3.2. Reynolds Number

The physics of moving through water depends on size and speed. The **Reynolds number** $Re = \rho U L/\mu$ ($\rho$ density and $\mu$ dynamic viscosity of the fluid, $U$ speed, $L$ length of the body) measures the ratio of inertial to viscous forces. A whale swimming at several meters per second has $Re \approx 10^8$, a fish $10^4$–$10^6$, a copepod $1$–$100$, a ciliated larva about $1$ or less, a sperm cell about $10^{-2}$.

At high Reynolds number inertia dominates: a swimmer that stops coasting forward, streamlined bodies reduce drag, and fins and tails generate thrust by accelerating water backward. At low Reynolds number viscosity dominates: motion stops almost instantly when propulsion stops, water is effectively syrup, and a reciprocal motion, a stroke reversed exactly in the return stroke, gives no net movement at all. Cilia escape this by beating asymmetrically, with a stiff power stroke and a bent recovery stroke; flagella by propagating helical or planar waves. Low Reynolds number also governs suspension feeding: the bristles of copepod limbs and the tentacles of bryozoans work less as sieves than as paddles that move a parcel of viscous water containing particles.

## 4.4. Feeding and Digestion

### 4.4.1. Feeding Types

| Type | Food and method | Examples |
|---|---|---|
| Suspension feeding | Particles suspended in water, captured by sieves, mucus nets or ciliary currents | Sponges, bivalves, brachiopods, bryozoans, tunicates, lancelets, barnacles, baleen whales |
| Deposit feeding | Organic matter in sediment, swallowed with it or collected by tentacles | Earthworms, many polychaetes, sea cucumbers |
| Herbivory and grazing | Plants, algae, microbial films; scraped, chewed or cut | Snails with the radula, sea urchins, many insects, ungulates |
| Predation | Animal prey, captured and swallowed or torn | Cnidarians, flatworms, cephalopods, spiders, most vertebrates |
| Fluid feeding | Plant sap, nectar, blood, body fluids, by piercing and sucking | Aphids, mosquitoes, leeches, ticks, vampire bats |
| Symbiotic nutrition | Products of photosynthetic or chemosynthetic symbionts | Reef corals with zooxanthellae, giant clams, siboglinid tube worms |
| Absorption | Dissolved nutrients across the body surface | Tapeworms, acanthocephalans |

**Definition 4.4.1 (Filter Feeding)** **Filter feeding** (suspension feeding) is feeding on particles suspended in water, which the animal separates from a current of water that it generates or that the environment provides, using a filter of cilia, bristles, tentacles or mucus.

Filter feeding is one of the most widespread modes of life in the sea and has evolved independently many times. It allows sessile animals to live on food brought by currents, but it requires the processing of large volumes of water: a sponge can pump its own volume every few seconds, an oyster about 10 L per hour.

### 4.4.2. Three Kinds of Digestive System

Food is digested intracellularly, in food vacuoles after phagocytosis, or extracellularly, by enzymes secreted into a cavity, and the two are often combined (see the figure below).

**Definition 4.4.2 (Gastrovascular Cavity, Complete Digestive Tract)** A **gastrovascular cavity** is a digestive cavity with a single opening that serves as both mouth and anus; it digests food extracellularly and, by its branching or the circulation of its fluid, also distributes the products through the body. A **complete digestive tract** (through gut) is a tube with two openings, a mouth and an anus, through which food passes in one direction.

![Three ways animals digest food (schematic). (A) Intracellular digestion: a choanocyte of a sponge engulfs a particle and digests it in a food vacuole. (B) A gastrovascular cavity with a single opening that serves as mouth and anus, as in a cnidarian polyp; digestion begins extracellularly in the cavity and is completed inside the cells of the gastrodermis. (C) A complete digestive tract with a mouth and an anus, in which food passes one way through a sequence of specialized regions](./plots/gut-types.py)

Sponges and placozoans digest food only intracellularly. Cnidarians, ctenophores (whose anal pores are an exception), xenacoelomorphs and flatworms have a gastrovascular cavity, branched in large flatworms and in medusae into canals that reach every part of the body. A complete gut is the rule in the Nephrozoa (bilaterians other than xenacoelomorphs). Its advantage is the division of labor along the tube: food can be taken in while earlier meals are still being digested, and successive regions can specialize in storage (crop, stomach), grinding (gizzard), enzymatic digestion, absorption (intestine, often with a large surface increased by folds and villi) and the recovery of water and ions (rectum). The digestive systems of vertebrates are compared in [7.17.63](/7.17.63) and their physiology treated in [7.14.26](/7.14.26)–[7.14.28](/7.14.28).

## 4.5. Gas Exchange and Circulation

Oxygen enters animals by diffusion across a moist surface, and the rate of entry is proportional to the area of that surface and to the difference in partial pressure across it, and inversely proportional to its thickness (Fick's law, [7.14.17](/7.14.17)). Small or flat animals use the whole body surface; larger animals use one of four kinds of respiratory organ:

| Organ | Structure | Examples |
|---|---|---|
| Body surface | Thin, moist, often richly supplied with blood | Flatworms, nemerteans, earthworms, many small arthropods, lungless salamanders |
| Gills | Thin evaginations of the body surface, ventilated by water | Polychaetes, molluscs (ctenidia), crustaceans, aquatic insect larvae, fishes, amphibian larvae |
| Lungs | Invaginations holding air | Book lungs of spiders and scorpions, the mantle cavity of land snails, the lungs of vertebrates |
| Tracheae | Branching air-filled tubes that carry oxygen directly to the cells | Insects, myriapods, many arachnids, onychophorans |

Water contains about 30 times less oxygen than air and is about 800 times denser and 50 times more viscous, so ventilating a gill costs much more than ventilating a lung; gill breathers compensate by **countercurrent exchange** ([7.14.17](/7.14.17)). The **tracheal system** is a radical alternative: it makes a circulatory system unnecessary for gas transport and limits insect size, because diffusion along the tracheae becomes slow over large distances ([7.17.26](/7.17.26)).

Where oxygen must be carried more than a millimeter or so, a circulatory system moves body fluid by bulk flow. In an **open circulatory system** the heart pumps hemolymph through vessels that open into the hemocoel, where it bathes the tissues (arthropods, most molluscs); in a **closed circulatory system** blood remains within vessels, and exchange takes place across the walls of capillaries (annelids, cephalopods, vertebrates). Respiratory pigments increase the oxygen capacity of the blood: hemoglobin (vertebrates, many annelids, some insects and crustaceans), hemocyanin, a copper protein dissolved in the plasma (molluscs and arthropods, independently evolved in the two), hemerythrin (sipunculans, brachiopods) and chlorocruorin (some polychaetes). The physiology of circulation and gas transport is treated in [7.14.12](/7.14.12) and [7.14.19](/7.14.19).

## 4.6. Excretion and Osmoregulation

Animals excrete the nitrogen of surplus amino acids as ammonia (most aquatic animals), urea (mammals, adult amphibians, cartilaginous fishes) or uric acid (insects, birds, reptiles, land snails), a choice that depends on the availability of water ([7.14.21](/7.14.21)). Most of them must also regulate the water and ions of their body fluids. The organs that do both have, with few exceptions, a common working principle: a primary fluid resembling the body fluid is formed, by filtration or by secretion, and is then modified as it passes along a tube, by reabsorption of useful solutes and water and secretion of wastes, before it leaves the body as urine. Three types of tubular excretory organ are found among invertebrates (see the figure below).

**Definition 4.6.1 (Protonephridium, Flame Cell)** A **protonephridium** is a tubular excretory organ whose inner end is closed by one or more terminal cells; the outer end opens to the exterior through a nephridiopore. In a **flame cell** the terminal cell bears a tuft of cilia whose beating, seen in the light microscope as a flickering flame, drives fluid down the tubule; body fluid is filtered into the lumen through a fine weir of slits or pores in the wall of the terminal cell. Terminal cells with a single flagellum are called solenocytes.

**Definition 4.6.2 (Metanephridium)** A **metanephridium** is a tubular excretory organ whose inner end opens into the coelom through a ciliated funnel, the nephrostome; coelomic fluid enters the funnel, is modified along the tubule and leaves through a nephridiopore. In segmented annelids each segment typically has a pair, whose funnel lies in the segment in front of the one in which the tubule opens.

**Definition 4.6.3 (Malpighian Tubule)** A **Malpighian tubule** is a blind excretory tubule of terrestrial arthropods (insects, myriapods, arachnids) that lies free in the hemocoel and opens into the gut at the junction between midgut and hindgut. Its cells actively secrete potassium and other ions into the lumen, water and wastes follow, and the fluid is modified further in the hindgut and rectum, where most of the water and ions are reabsorbed.

![Three types of invertebrate excretory organ (schematic, not to scale). (A) Protonephridium of a flatworm: branched blind tubules ending in flame cells whose ciliary tufts drive fluid through the tubule to the nephridiopore. (B) Metanephridium of an annelid: a ciliated funnel, the nephrostome, opens into the coelom of one segment; the coiled tubule passes through the septum and opens through a nephridiopore in the next segment, modifying the fluid on the way. (C) Malpighian tubules of an insect: blind tubules bathed in hemolymph secrete ions, and water and nitrogenous waste follow; the fluid enters the gut at the junction of midgut and hindgut, and the rectum reabsorbs water and ions](./plots/excretory-organs.py)

Protonephridia occur in animals without a spacious coelom or without a closed circulation: flatworms, rotifers, gastrotrichs, nemerteans, and the larvae (the trochophores) of annelids and molluscs. Metanephridia occur in coelomate animals with a circulatory system. In these, as Ruppert and Smith (1988) showed, filtration does not take place in the nephridium itself: blood pressure forces fluid out of the blood vessels across a filter formed by specialized coelomic lining cells with slit-like gaps between their processes (podocytes), into the coelom, and the metanephridium collects and modifies the filtrate. The vertebrate kidney follows the same scheme in a compact form: in each **nephron** blood is filtered across the podocyte layer of the glomerulus into Bowman's capsule, a derivative of the coelom, and the tubule reabsorbs most of the filtrate ([7.14.22](/7.14.22)).

Malpighian tubules work without filtration, by secretion. They evolved independently in insects and arachnids, and they suit animals on land that must conserve water: uric acid precipitates in the hindgut and can be excreted almost dry. Crustaceans have instead antennal or maxillary glands (green glands), and arachnids, besides Malpighian tubules, coxal glands; both are sacs derived from the coelom with a filtering wall and a tubule. In freshwater sponges, as in freshwater protists, water entering by osmosis is expelled by contractile vacuoles.

## 4.7. Nervous Systems

The nervous system of an animal reflects its symmetry and way of life (the cellular and molecular evolution of nervous systems is treated in [7.16.53](/7.16.53)). Four types of overall arrangement are distinguished:

- A **nerve net** of interconnected neurons spread through the epithelia, without a central ganglion, in cnidarians and ctenophores. Impulses spread in all directions from a stimulus, which suits radial animals; local condensations form nerve rings around the margin of medusae and around the mouth.
- A ladder-like nervous system, with cerebral ganglia and several longitudinal nerve cords joined by transverse commissures, in flatworms and some other small worms.
- A ventral nerve cord of paired ganglia, one pair per segment, in annelids and arthropods, below the gut, with a brain above the pharynx connected to it by a ring around the gut.
- A dorsal hollow nerve cord, the neural tube, above the gut, enlarged anteriorly into a brain, in chordates (**dorsal hollow nerve cord**, [7.17.43](/7.17.43)).

**Definition 4.7.1 (Ladder-Like Nervous System, Ventral Nerve Cord)** A **ladder-like nervous system** (orthogon) consists of an anterior cerebral ganglion and several pairs of longitudinal nerve cords linked at intervals by transverse commissures, like the rungs of a ladder. A **ventral nerve cord** (ganglionated ventral nerve cord) is a pair of nerve cords, often fused, running along the ventral midline below the gut and bearing a pair of ganglia in each segment, connected to the brain by circumpharyngeal (circumesophageal) connectives.

Other phyla have their own arrangements: molluscs have several pairs of ganglia connected by nerve cords, concentrated into a large brain around the esophagus in cephalopods; echinoderms have a nerve ring around the mouth with radial nerves into the arms and no brain. The trend toward centralization, with fewer longitudinal cords, concentration of ganglia and a large anterior brain, accompanies active locomotion and cephalization; sessile animals such as bryozoans, tunicates and bivalves show the opposite trend. As noted in [7.17.3](/7.17.3#sec-3.2.2), the ventral nerve cord of protostomes and the dorsal cord of chordates are specified by the same genes from an inverted dorsoventral axis, which suggests that the bilaterian ancestor already had a centralized nerve cord, although this is debated.

## 4.8. Reproduction

Animals reproduce sexually, and many also asexually. Asexual reproduction produces genetically identical offspring and allows rapid multiplication of a successful genotype; sexual reproduction produces variable offspring at the cost of meiosis and mating ([7.10.14](/7.10.14)).

| Mode | Process | Examples |
|---|---|---|
| Budding | A new individual grows from the body of the parent and either separates or remains attached, forming a **colony** | *Hydra*, corals, bryozoans, tunicates |
| Fission | The body divides into two or more parts, each regenerating the missing structures | Sea anemones (longitudinal), planarians and some annelids (transverse) |
| Fragmentation | The body breaks into pieces that regenerate | Sponges, nemerteans, sea stars |
| Gemmules, statoblasts | Resistant asexual bodies that survive unfavorable seasons | Freshwater sponges, freshwater bryozoans |
| **Parthenogenesis** | Development of an egg without fertilization | Rotifers (bdelloids exclusively), aphids, water fleas, honey bee drones, some lizards |
| Polyembryony | One zygote splits into several embryos | Parasitoid wasps, armadillos |

In sexual reproduction most animals are gonochoristic, with separate sexes, but hermaphroditism is common in sessile, slow or parasitic animals, for which finding a mate is difficult. Simultaneous hermaphrodites have both kinds of gonad at once and usually cross-fertilize (earthworms and land snails exchange sperm), whereas some tapeworms self-fertilize. Sequential hermaphrodites change sex during life: the slipper limpet *Crepidula* and anemonefish are first male and later female (protandry), and many wrasses first female and later male (protogyny). Fertilization is external in many aquatic animals, which shed gametes into the water, and internal in most land animals, often by means of packets of sperm (spermatophores) or a copulatory organ. The modes of development that follow fertilization are the subject of [7.17.5](/7.17.5).

## Summary

| Problem | Solutions (where) |
|---|---|
| Size and diffusion | Flat (flatworms), thin (nemerteans), inert core (medusae), water through the body (sponges), exchange organs and circulation (large active animals) |
| Support | **Hydrostatic skeleton** (worms, polyps), exoskeleton (arthropods, molluscs), endoskeleton (echinoderms, vertebrates); helical fiber lattices with the optimum $54^\circ 44'$ (Formula 4.2.1) |
| Movement | Amoeboid, ciliary (small animals, low $Re$), hydrostatic (peristalsis, jets), muscles and levers, undulation |
| Feeding | **Filter feeding** (Definition 4.4.1), deposit feeding, grazing, predation, fluid feeding, symbionts, absorption |
| Digestion | Intracellular (sponges); **gastrovascular cavity** (cnidarians, flatworms); **complete digestive tract** (Nephrozoa) (Definition 4.4.2) |
| Gas exchange | Body surface, gills, lungs, tracheae; open or closed circulation |
| Excretion | **Protonephridia** with **flame cells** (Definition 4.6.1), **metanephridia** (Definition 4.6.2), **Malpighian tubules** (Definition 4.6.3), antennal and coxal glands, nephrons; filtration (or secretion) followed by modification |
| Coordination | Nerve net, **ladder-like nervous system**, **ventral nerve cord** (Definition 4.7.1), dorsal hollow nerve cord |
| Reproduction | Budding, fission, fragmentation, parthenogenesis; gonochorism and simultaneous or sequential hermaphroditism |

## Questions

1. Show from Eq. (4.1) that the maximum volume is reached at $\tan\theta = \sqrt{2}$, and compute the aspect ratio $l/2r$ of the cylinder at that angle.

   **Answer** $\frac{\mathrm{d}}{\mathrm{d}\theta}(\sin^2\theta\cos\theta) = 2\sin\theta\cos^2\theta - \sin^3\theta = \sin\theta\,(2\cos^2\theta - \sin^2\theta)$, which vanishes for $0 < \theta < 90^\circ$ when $\tan^2\theta = 2$, so $\theta = \arctan\sqrt{2} \approx 54.74^\circ = 54^\circ 44'$. The aspect ratio is $\pi\cot\theta = \pi/\sqrt{2} \approx 2.2$: at maximum volume the worm segment is about twice as long as it is wide.

2. A flatworm consumes oxygen at $M = 2.6\times10^{-4}\,\mathrm{mol\,m^{-3}\,s^{-1}}$. Using the values of the diffusion-limit figure, what is the greatest thickness it can have if it is a flat sheet, and what is the greatest radius of a spherical animal with the same metabolic rate?

   **Answer** The half-thickness of a sheet is $\sqrt{2Dc_0/M} = \sqrt{2 \times 2\times10^{-9} \times 0.25 / 2.6\times10^{-4}} \approx \sqrt{3.8\times10^{-6}}\,\mathrm{m} \approx 2.0\,\mathrm{mm}$, so the total thickness can reach about 4 mm (real flatworms are thinner, because their surface concentration and diffusion coefficient are lower and they are often active). A sphere could have a radius of $\sqrt{6Dc_0/M} \approx 3.4\,\mathrm{mm}$; but a flat sheet can have any length and width, whereas the sphere is limited in all directions.

3. Why do metanephridia occur in animals with a circulatory system and a coelom, whereas protonephridia are typical of small animals without them?

   **Answer** A metanephridium does not filter; it collects fluid from the coelom. It works only where a filtrate is produced in the coelom, which requires blood vessels with enough pressure to force fluid across the podocyte filter of the coelomic lining. Without a coelom and a pressurized circulation, the animal must make the filtrate itself, and the protonephridium does so by the negative pressure generated by its ciliary flame, which draws body fluid through the weir of the terminal cell. The correspondence is not perfect: some coelomates have protonephridia, and annelid larvae have protonephridia before the adult metanephridia develop.

4. A ciliated larva 0.2 mm long swims at 1 mm/s in seawater ($\rho \approx 1025\,\mathrm{kg\,m^{-3}}$, $\mu \approx 1.1\times10^{-3}\,\mathrm{Pa\,s}$). Compute its Reynolds number and explain why it cannot swim by flapping a rigid paddle back and forth.

   **Answer** $Re = \rho U L/\mu = 1025 \times 10^{-3} \times 2\times10^{-4} / 1.1\times10^{-3} \approx 0.19$. Viscous forces dominate and inertia is negligible, so the flow depends only on the instantaneous motion of the body, not on its history. A rigid paddle that moves back along exactly the path of its forward stroke reverses all the flow it produced and the larva returns to where it was. Cilia avoid this by changing shape: a stiff power stroke and a flexible recovery stroke close to the body sweep different areas.
