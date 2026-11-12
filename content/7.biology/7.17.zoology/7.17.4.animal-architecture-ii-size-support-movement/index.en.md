---
title: "Animal Architecture II: Size, Support, Movement, and Exchange"
description: Size and scaling, and the limit that diffusion sets on body form; skeletons (hydrostatic, exoskeleton, endoskeleton) with the Clark–Cowey model of worms reinforced by helical fibers and the materials of skeletons; locomotion at low and high Reynolds number; feeding types and the three kinds of digestive system; gas exchange and circulation; protonephridia, metanephridia and Malpighian tubules and the filtration–reabsorption principle; types of nervous system; asexual and sexual reproduction, gonads and sperm transfer; body coverings and chemical coordination. A catalog of design solutions that later chapters take up phylum by phylum.
---

Every animal must solve the same practical problems: it must hold its shape and move, obtain food and digest it, take up oxygen and give off carbon dioxide, distribute substances within the body, get rid of nitrogenous waste while keeping its water and salts in balance, protect itself with a body covering, coordinate its parts by nerves and hormones, and reproduce. The previous chapter ([7.17.3](/7.17.3)) described the overall architecture of the body; this one surveys the solutions animals have evolved for each of these problems, as a catalog to which the chapters on the individual phyla will refer. A single physical constraint runs through the catalog: as an animal grows, its volume increases faster than its surface, and diffusion, which serves small animals well, becomes too slow. The physiology of each system is the subject of animal physiology ([7.14](/7.14)); here we stress the structural types and how they are distributed among the phyla.

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

### 4.1.3. Numbers for Surface, Volume and Diffusion

Two simple calculations show how sharply the constraint bites. For a sphere of radius $r$ the ratio of surface to volume is $3/r$; the time that diffusion takes grows with the square of the distance.

**Formula 4.1.1 (Diffusion Time)** The mean time for a molecule with diffusion coefficient $D$ to diffuse a distance $x$ in one direction is approximately

$$
t \approx \frac{x^2}{2D}.
\tag{4.2}
$$

:::

| Radius or distance | Surface/volume of a sphere | Time for O$_2$ to diffuse that far in water ($D \approx 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$) | Biological scale |
|---|---|---|---|
| 1 µm | $3\times10^{6}\,\mathrm{m^{-1}}$ | 0.25 ms | A bacterium; the alveolar wall is about 0.5 µm thick |
| 10 µm | $3\times10^{5}\,\mathrm{m^{-1}}$ | 25 ms | An animal cell; distance from a capillary to most cells |
| 100 µm | $3\times10^{4}\,\mathrm{m^{-1}}$ | 2.5 s | A rotifer; a flatworm's half-thickness |
| 1 mm | $3\times10^{3}\,\mathrm{m^{-1}}$ | about 4 min | A copepod; the limit for an active sphere |
| 1 cm | $300\,\mathrm{m^{-1}}$ | about 7 h | A small insect; the thickness of an earthworm |
| 1 m | $3\,\mathrm{m^{-1}}$ | about 8 years | A large mammal |

The quadratic dependence is decisive: diffusion is fast enough within a cell and across thin epithelia, but useless over the length of an animal. This is why almost all exchange surfaces are thin and why bulk flow (breathing, pumping blood, ciliary currents) carries substances over every distance larger than a fraction of a millimeter. Animals increase the area of their exchange surfaces enormously: the human lungs have an alveolar surface of about $70\,\mathrm{m^2}$ behind a barrier about $0.5\,\mu\mathrm{m}$ thick, and the human small intestine, with its folds, villi and microvilli, has a mucosal surface of about $30\,\mathrm{m^2}$ (Helander and Fändriks 2014; older estimates of 200–300 m² were too high), compared with about $1.8\,\mathrm{m^2}$ of skin.

### 4.1.4. Scaling of Metabolism, Support and Life History

The surface–volume constraint has consequences beyond gas exchange. Because whole-animal metabolic rate scales approximately as $M^{3/4}$ (**Kleiber's law**, [7.14.30](/7.14.30#sec-30.3)), the metabolic rate per gram scales as $M^{-1/4}$: a 3 g shrew uses oxygen per gram of tissue about $(4\times10^{6}/3)^{1/4} \approx 34$ times as fast as a 4 t elephant. The same quarter-power rule applies to many rates and times: heart rate and breathing rate scale approximately as $M^{-1/4}$ (a shrew's heart beats several hundred to a thousand times a minute, an elephant's about thirty), and life span and generation time approximately as $M^{1/4}$.

Support scales differently from metabolism. If animals were geometrically similar, the stress in their bones under their own weight would rise in proportion to length, and the largest animals would break their legs. Mammals solve this only partly by thicker bones: across mammals skeletal mass scales approximately as $M^{1.09}$ (Prange and colleagues 1979), only slightly faster than body mass. The main solution is posture: large mammals stand with straighter limbs, which aligns the bones with the load and increases the mechanical advantage of the muscles, so that peak bone stresses are similar from mice to horses (Biewener 1989). Aquatic animals escape much of the constraint because water supports them, which is one reason why the largest animals that have ever lived, the blue whales, are marine.

The range of animal size spans about eight orders of magnitude in length. Among the smallest free-living animals are some rotifers, tardigrades and the fairyfly *Megaphragma mymaripenne*, a parasitoid wasp about 0.2 mm long whose nervous system of a few thousand neurons consists mostly of cells that lose their nuclei during development (Polilov 2012). The largest is the blue whale, up to about 30 m and more than 150 t. Arthropods are never as large as the largest vertebrates; the largest insects lived in the late Carboniferous and Permian, when griffinflies (*Meganeuropsis*) reached wingspans of about 70 cm. A popular hypothesis attributes such giants to the high atmospheric oxygen of that time (perhaps 30%), which would have extended the reach of the tracheal system ([7.17.26](/7.17.26#sec-26.4)), but the correlation is debated.

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

The mechanical properties of these materials span a wide range. Their stiffness, measured by **Young's modulus** (stress divided by strain in the elastic range), differs by about ten orders of magnitude, which allows animals to build structures from jelly to tooth with a small set of molecules (orders of magnitude after Wainwright and colleagues 1976 and Vogel 2003):

| Material | Young's modulus (order of magnitude) | Function |
|---|---|---|
| Mesoglea of jellyfish | $10^{2}$–$10^{4}\,\mathrm{Pa}$ | Bulk and shape at almost no metabolic cost |
| Resilin, elastin | About $1\,\mathrm{MPa}$ | Rubber-like springs: insect wing hinges, the jumping mechanism of fleas, arterial walls |
| **Mutable collagenous tissue** (echinoderms) | Changes by an order of magnitude or more under nervous control | Catch connective tissue that locks spines and arms |
| Tendon collagen | About $1\,\mathrm{GPa}$ | Inextensible fibers in tension |
| Sclerotized insect cuticle | $1$–$20\,\mathrm{GPa}$ | Rigid levers and armor |
| Bone (compact) | About $20\,\mathrm{GPa}$ | Stiff, tough, self-repairing levers |
| Nacre of mollusc shells | About $70\,\mathrm{GPa}$ | Hard, fracture-resistant armor |
| Tooth enamel | About $80\,\mathrm{GPa}$ | Hardest vertebrate tissue, for cutting and grinding |

### 4.2.4. Skeletons across the Phyla and Their Mechanics

Each type of skeleton takes several forms, and most phyla combine more than one.

| Skeleton | Form | Examples | Chapter |
|---|---|---|---|
| Hydrostatic | Fluid in the gastrovascular cavity | Sea anemones, *Hydra* (the mouth closes to trap water) | [7.17.9](/7.17.9) |
| | Fluid in a blastocoelom under high pressure | Nematodes | [7.17.17](/7.17.17) |
| | Fluid in a coelom, divided by septa | Earthworms, many polychaetes | [7.17.15](/7.17.15) |
| | Fluid in an undivided coelom or hemocoel | Sipunculans, the foot of bivalves, the proboscis of nemerteans | [7.17.14](/7.17.14), [7.17.16](/7.17.16) |
| | Hydraulic extension of appendages | Spider legs (extended by hemolymph pressure), echinoderm tube feet | [7.17.19](/7.17.19), [7.17.42](/7.17.42) |
| Muscular hydrostat | Muscle tissue itself as the incompressible volume | Cephalopod arms and tentacles, tongues of mammals and lizards, the elephant's trunk | [7.17.14](/7.17.14) |
| Exoskeleton | Molted, jointed cuticle of chitin and protein, often mineralized | Arthropods | [7.17.18](/7.17.18) |
| | Accretionary calcareous shell | Molluscs, brachiopods | [7.17.13](/7.17.13), [7.17.16](/7.17.16) |
| | Secreted cup or tube | Corals, serpulid polychaetes, bryozoans | [7.17.9](/7.17.9) |
| Endoskeleton | Spicules and spongin in the mesohyl | Sponges | [7.17.7](/7.17.7) |
| | Ossicles of calcite in the dermis, each a single crystal with a porous stereom | Echinoderms | [7.17.42](/7.17.42) |
| | Cartilage and bone | Vertebrates; cartilage also around the brain of cephalopods, cartilage-like gill bars in lancelets | [7.17.58](/7.17.58) |

**Definition 4.2.1 (Muscular Hydrostat)** A **muscular hydrostat** is a muscular organ without skeletal support or a fluid-filled cavity, in which the muscle tissue itself forms an incompressible volume; muscles arranged in at least three directions (longitudinal, transverse or circular, and helical or oblique) act as antagonists to one another, so that a decrease in one dimension causes an increase in another.

Muscular hydrostats, analyzed by Kier and Smith (1985), allow bending, elongation, shortening and twisting with great precision. A squid's tentacle, for example, extends by up to about 80% in a few tens of milliseconds during prey capture by the contraction of transverse muscle fibers that are cross-striated for speed.

Rigid skeletons act as levers, and their arrangement determines the trade-off between force and speed.

**Formula 4.2.2 (Lever)** A muscle that exerts a force $F_{\mathrm{in}}$ at a distance $l_{\mathrm{in}}$ from a joint (the in-lever) moves a load at a distance $l_{\mathrm{out}}$ (the out-lever). At equilibrium, and for the velocities at the two points,

$$
F_{\mathrm{out}} = F_{\mathrm{in}}\,\frac{l_{\mathrm{in}}}{l_{\mathrm{out}}}, \qquad v_{\mathrm{out}} = v_{\mathrm{in}}\,\frac{l_{\mathrm{out}}}{l_{\mathrm{in}}};
\tag{4.3}
$$

the ratio $l_{\mathrm{in}}/l_{\mathrm{out}}$ is the mechanical advantage.

:::

Limbs built for speed, such as the legs of running ungulates, have a small mechanical advantage: the muscles insert close to the joint and the foot moves fast. Limbs built for force, such as the forelimbs of digging moles or the chelae of crabs, have a large one. The same rule applies to jaws, where the lower jaw of a fish or mammal is a lever whose design reflects its diet ([7.17.58](/7.17.58)).

The shape of a skeletal element matters as much as its material. A beam resists bending in proportion to the second moment of area of its cross section, which for a tube of outer radius $R$ and inner radius $r$ is $I = \pi(R^4 - r^4)/4$. For a given amount of material (a given cross-sectional area $A$), a tube with $r = kR$ is stiffer than a solid rod by the factor $(1 + k^2)/(1 - k^2)$: about 4.6 for $k = 0.8$. This is why arthropod legs, bird bones and the shafts of mammalian long bones are hollow, and why the exoskeleton, a tube with the muscles inside, is an efficient design for small animals. It becomes less efficient at large size, because a thin-walled tube buckles locally and because the animal must molt: a freshly molted arthropod is supported only by hemolymph pressure until the new cuticle hardens, a phase in which large land arthropods would collapse under their weight.

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

![Reynolds numbers of moving organisms (logarithmic scale; values from Vogel 1994, *Life in Moving Fluids*, 2nd ed., for the speeds stated). The scale spans thirteen orders of magnitude. Below $Re \approx 1$ viscosity dominates and organisms swim with cilia or flagella, whose asymmetric or wave-like beats avoid the reciprocal motion that produces no net displacement; above $Re \approx 1000$ inertia dominates and animals are streamlined and propel themselves with fins, tails, wings or jets. The intermediate range, where both forces matter, is occupied by copepods, the smallest flying insects and many larvae](./plots/reynolds-ladder.py)

### 4.3.3. Locomotion Compared

The main modes of locomotion are compared below. Each is suited to a range of sizes, which is one reason why the mode of locomotion changes during the life of many animals: a ciliated larva becomes a crawling or swimming adult.

| Mode | Mechanism | Size and $Re$ | Examples | Chapter |
|---|---|---|---|---|
| Ciliary swimming | Metachronal waves of cilia on the body surface or in bands | Micrometers to millimeters; $Re < 1$ | Larvae, rotifers, small flatworms; ctenophores with comb plates | [7.17.8](/7.17.8), [7.17.12](/7.17.12) |
| Ciliary gliding | Cilia beat in a layer of mucus on the substrate | Up to several centimeters if flat | Planarians, small nemerteans, many gastropods in part | [7.17.11](/7.17.11) |
| Peristaltic crawling and burrowing | Waves of contraction of circular and longitudinal muscles on a segmented hydrostatic skeleton | Centimeters to meters | Earthworms, many polychaetes | [7.17.15](/7.17.15) |
| Two-anchor burrowing | Alternate anchoring of the front (by swelling) and the rear (by a shell or swollen body), with the hydrostatic body pulling between | Centimeters | Bivalves with the foot, sipunculans, burrowing sea anemones | [7.17.14](/7.17.14) |
| Pedal waves | Waves of muscle contraction along a foot gliding on mucus | Millimeters to decimeters | Snails, slugs, chitons | [7.17.13](/7.17.13) |
| Undulation | Lateral or dorsoventral waves of bending along a body stiffened by a notochord, a vertebral column or a pressurized cuticle | Millimeters to meters | Nematodes (dorsoventral), polychaetes with parapodia, lancelets, eels, snakes | [7.17.17](/7.17.17), [7.17.43](/7.17.43) |
| Jet propulsion | Expulsion of water from a cavity, refilled by elastic recoil or by muscles | Millimeters to meters | Medusae, squid and octopuses, scallops, salps, dragonfly larvae | [7.17.9](/7.17.9), [7.17.14](/7.17.14) |
| Walking with appendages | Jointed legs acting as levers, coordinated in gaits | Millimeters to meters | Arthropods (metachronal waves in myriapods, the alternating tripod of insects), tetrapods | [7.17.20](/7.17.20), [7.17.24](/7.17.24), [7.17.61](/7.17.61) |
| Tube feet | Hydraulic extension and adhesion of many small podia | Centimeters | Sea stars, sea urchins | [7.17.42](/7.17.42) |
| Paddling and rowing | Appendages with a power stroke and a feathered recovery stroke | Millimeters to meters | Copepods, water beetles, turtles | [7.17.21](/7.17.21) |
| Flapping flight | Wings generating lift and thrust | Insects from 0.2 mm, birds, bats, extinct pterosaurs | Four independent origins | [7.17.25](/7.17.25), [7.17.53](/7.17.53) |

Several modes recur in unrelated lineages: jet propulsion in cnidarians, molluscs, tunicates and insects; undulation in nematodes, annelids and vertebrates; flight in four lineages. What they share is a mechanical principle, not an ancestry, and their distribution follows size and medium more closely than phylogeny.

### 4.3.4. The Cost of Locomotion

**Definition 4.3.1 (Cost of Transport)** The **cost of transport** is the metabolic energy an animal spends to move a unit of its body mass over a unit of distance, usually measured in joules per kilogram per meter; the net cost of transport excludes the resting metabolic rate.

Schmidt-Nielsen (1972) compared the minimum cost of transport of runners, fliers and swimmers over a wide range of sizes. For each mode the cost per kilogram decreases with body size, approximately as $M^{-0.3}$, so that large animals move more cheaply. At the same body mass, swimming is the cheapest mode, because the water supports the body and streamlined swimmers suffer little drag; flying is intermediate, because a flier must support its weight but travels fast; and running is the most expensive, because muscles do work against gravity at every step. These differences help explain the long migrations of whales and birds and the short ranges of walking animals of the same size, and why burrowing, which must push soil aside, is many times more costly than walking.

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

### 4.4.3. How Suspension Feeders Capture Particles

**Filter feeding** has evolved in so many lineages that its mechanisms form a catalog of their own. They differ in what generates the current, what retains the particles and how the particles are carried to the mouth.

| Mechanism | Current and capture | Examples | Chapter |
|---|---|---|---|
| Choanocyte pump | Flagella of collar cells drive water through the body; bacteria are trapped on the collar microvilli | Sponges | [7.17.7](/7.17.7#sec-7.3) |
| Downstream ciliary bands | A band of compound cilia (prototroch, metatroch) creates the current and catches particles on the downstream side; a food groove between the bands leads to the mouth | Trochophore larvae of annelids and molluscs, rotifers, entoprocts | [7.17.5](/7.17.5) |
| Upstream ciliary bands | Single cilia create the current; particles are caught on the upstream side by a local reversal of beat | Lophophorates, pterobranchs, echinoderm and enteropneust larvae | [7.17.16](/7.17.16), [7.17.41](/7.17.41) |
| Ciliary–mucus sheets | Cilia of the gills or pharynx create a current; a mucus sheet secreted by an endostyle or gland traps particles and is rolled into a strand | Bivalves, tunicates, lancelets, some gastropods such as *Crepidula* | [7.17.14](/7.17.14), [7.17.43](/7.17.43) |
| Mucus nets | A net of mucus spun outside the body, collected and eaten | Appendicularian houses, the polychaete *Chaetopterus*, vermetid gastropods | [7.17.43](/7.17.43) |
| Setose appendages | Limbs bearing setae sweep or pump water; at low $Re$ they act more as paddles than as sieves | Copepods, barnacles, krill, branchiopods | [7.17.21](/7.17.21) |
| Tentacles | Passive capture by sticky or stinging tentacles held in the current | Hydroids, corals, sea lilies, dendrochirotid sea cucumbers | [7.17.9](/7.17.9), [7.17.42](/7.17.42) |
| Baleen | Gulping a large volume and expelling it through keratin plates | Baleen whales | [7.17.55](/7.17.55) |

The distinction between downstream and upstream collecting systems was emphasized by Nielsen as a character of larval evolution: downstream systems of compound cilia characterize the trochophores of spiralians, upstream systems of single cilia the larvae of lophophorates and deuterostomes ([7.17.5](/7.17.5#sec-5.4)). Particle sizes range from bacteria (0.5–1 µm, sponges and appendicularians) through phytoplankton (2–100 µm, bivalves and copepods) to krill (several centimeters, baleen whales).

### 4.4.4. Structures for Obtaining Food

| Structure | Construction | Examples | Chapter |
|---|---|---|---|
| Cnidae and tentacles | Discharging capsules on tentacles that paralyze and hold prey | Cnidarians; colloblasts (adhesive cells) in ctenophores | [7.17.9](/7.17.9), [7.17.8](/7.17.8) |
| Eversible pharynx | A muscular pharynx protruded through the mouth | Planarians, many polychaetes | [7.17.11](/7.17.11) |
| Cuticular jaws | Jaws and teeth of the pharynx lining | Gnathiferans (rotifer trophi in the mastax), polychaete jaws, cephalopod beaks | [7.17.12](/7.17.12), [7.17.14](/7.17.14) |
| **Radula** | A ribbon of chitinous teeth moved over a cartilaginous support | Molluscs except bivalves | [7.17.13](/7.17.13) |
| Mouthparts | Modified appendages: mandibles, maxillae, chelicerae | Arthropods; insect mouthpart types | [7.17.18](/7.17.18), [7.17.23](/7.17.23) |
| Aristotle's lantern | Five teeth moved by a complex of ossicles and muscles | Sea urchins | [7.17.42](/7.17.42) |
| Proboscis | An eversible tube, sometimes armed with a stylet | Nemerteans, many gastropods (cone snails with harpoon-like radular teeth) | [7.17.16](/7.17.16) |
| Jaws and teeth | Bony or cartilaginous jaws of the first pharyngeal arch, with teeth of dentine and enamel | Gnathostome vertebrates | [7.17.46](/7.17.46), [7.17.63](/7.17.63) |

### 4.4.5. Regions of a Complete Gut

A complete gut develops from three parts: the stomodeum, an ingrowth of ectoderm at the mouth, forms the foregut; the endodermal archenteron forms the midgut; and the proctodeum, an ingrowth of ectoderm at the anus, forms the hindgut. In arthropods the ectodermal foregut and hindgut are lined with cuticle that is shed at each molt, and digestion and absorption take place in the midgut. The regions are differently specialized in different animals:

| Region | Earthworm | Insect | Crayfish | Bird |
|---|---|---|---|---|
| Foregut | Muscular pharynx, esophagus with calciferous glands, crop for storage, gizzard for grinding | Pharynx, esophagus, crop, proventriculus with cuticular teeth | Esophagus, stomach with a gastric mill of calcified ossicles | Esophagus with crop, glandular stomach (proventriculus), gizzard |
| Midgut | Intestine with a dorsal fold (typhlosole) that increases its surface | Midgut with gastric caeca, lined by a peritrophic membrane | Midgut with a large digestive gland (hepatopancreas) | Small intestine with liver and pancreas |
| Hindgut | Short rectum | Ileum, colon and rectum with rectal pads that reabsorb water | Intestine and anus | Large intestine, paired caeca, cloaca |
| Chapter | [7.17.15](/7.17.15) | [7.17.26](/7.17.26#sec-26.2) | [7.17.21](/7.17.21) | [7.17.53](/7.17.53), [7.17.63](/7.17.63) |

The table shows a convergence that reflects the problems all animals face: a storage organ (crop) where food is taken in quickly, a grinding organ (gizzard, proventriculus, gastric mill) for animals that lack chewing teeth, a large absorptive surface in the midgut, and a terminal region that recovers water. How the digestive system was modified along the animal tree is the subject of [7.17.44](/7.17.44).

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

### 4.5.1. Respiratory Organs and Circulatory Systems by Phylum

| Group | Gas exchange | Circulation | Chapter |
|---|---|---|---|
| Sponges, cnidarians, ctenophores, placozoans | Whole surface, water currents through the body or the gastrovascular cavity | None | [7.17.7](/7.17.7)–[7.17.9](/7.17.9) |
| Flatworms, xenacoelomorphs, gastrotrichs, rotifers | Body surface | None | [7.17.10](/7.17.10)–[7.17.12](/7.17.12) |
| Nematodes | Body surface | None; the pressurized body fluid mixes by movement | [7.17.17](/7.17.17) |
| Nemerteans | Body surface | Closed system of vessels without a heart, moved by contraction of the vessels and body wall | [7.17.16](/7.17.16#sec-16.1) |
| Annelids | Body surface, parapodial gills, branchial crowns of tube worms | Closed in most: a contractile dorsal vessel pumping forward and a ventral vessel, linked by segmental vessels (five pairs of "hearts" in the earthworm) | [7.17.15](/7.17.15) |
| Molluscs | Ctenidia in the mantle cavity; a lung in land snails | Open in most, with a heart in a pericardial coelom; closed in cephalopods, which have a systemic heart and two branchial hearts | [7.17.13](/7.17.13), [7.17.14](/7.17.14) |
| Crustaceans | Gills on the limbs or under the carapace | Open, with a dorsal heart in a pericardial sinus | [7.17.21](/7.17.21) |
| Chelicerates | Book gills (horseshoe crabs), book lungs and tracheae (arachnids) | Open, dorsal tubular heart with ostia | [7.17.19](/7.17.19) |
| Insects, myriapods | Tracheae opening by spiracles | Open; the dorsal vessel distributes nutrients and hormones, not oxygen | [7.17.26](/7.17.26#sec-26.5) |
| Echinoderms | Tube feet, papulae (dermal gills), respiratory trees of sea cucumbers | Coelomic fluid; a hemal system of sinuses of uncertain function | [7.17.42](/7.17.42) |
| Hemichordates, tunicates | Pharyngeal slits and body surface | Open; the tunicate heart periodically reverses the direction of flow | [7.17.41](/7.17.41), [7.17.43](/7.17.43) |
| Vertebrates | Gills (fishes, larval amphibians), lungs, skin | Closed, with a ventral chambered heart | [7.17.64](/7.17.64), [7.17.65](/7.17.65) |

The distinction between open and closed systems is less sharp than the terms suggest: the closed systems of annelids include sinuses, and the open systems of decapod crustaceans have well-defined arteries that branch to small vessels before the blood enters the sinuses. Closed systems allow higher pressures and faster, directed delivery, which suits large active animals (squid, vertebrates); open systems operate at low pressure and the hemolymph often has functions besides transport, such as the hydraulic skeleton of spider legs.

### 4.5.2. Respiratory Pigments

| Pigment | Oxygen-binding site | Location | Color (oxygenated / deoxygenated) | Groups |
|---|---|---|---|---|
| Hemoglobin | Iron in a heme group; one O$_2$ per heme | In red blood cells (vertebrates) or dissolved as giant extracellular molecules (many annelids) | Red / dark red | Vertebrates, many annelids, some molluscs (planorbid snails, some bivalves), branchiopod crustaceans (*Daphnia*), chironomid midge larvae |
| Chlorocruorin | Iron in a modified heme | Dissolved | Green in dilute solution, red when concentrated | Some polychaetes (sabellids, serpulids) |
| Hemocyanin | Two copper atoms per O$_2$ | Dissolved | Blue / colorless | Molluscs and arthropods; the two hemocyanins share a type of copper site but have different protein architectures and evolved independently |
| Hemerythrin | Two non-heme iron atoms per O$_2$ | In cells | Violet-pink / colorless | Sipunculans, priapulids, brachiopods, the polychaete *Magelona* |

The scattered distribution of hemoglobins reflects the antiquity of the globin gene family, present in all kingdoms, from which oxygen carriers have been recruited many times; hemocyanins evolved separately from enzymes, the phenoloxidases in arthropods and tyrosinase-like proteins in molluscs.

## 4.6. Excretion and Osmoregulation

Animals excrete the nitrogen of surplus amino acids as ammonia (most aquatic animals), urea (mammals, adult amphibians, cartilaginous fishes) or uric acid (insects, birds, reptiles, land snails), a choice that depends on the availability of water ([7.14.21](/7.14.21)). Most of them must also regulate the water and ions of their body fluids. The organs that do both have, with few exceptions, a common working principle: a primary fluid resembling the body fluid is formed, by filtration or by secretion, and is then modified as it passes along a tube, by reabsorption of useful solutes and water and secretion of wastes, before it leaves the body as urine. Three types of tubular excretory organ are found among invertebrates (see the figure below).

**Definition 4.6.1 (Protonephridium, Flame Cell)** A **protonephridium** is a tubular excretory organ whose inner end is closed by one or more terminal cells; the outer end opens to the exterior through a nephridiopore. In a **flame cell** the terminal cell bears a tuft of cilia whose beating, seen in the light microscope as a flickering flame, drives fluid down the tubule; body fluid is filtered into the lumen through a fine weir of slits or pores in the wall of the terminal cell. Terminal cells with a single flagellum are called solenocytes.

**Definition 4.6.2 (Metanephridium)** A **metanephridium** is a tubular excretory organ whose inner end opens into the coelom through a ciliated funnel, the nephrostome; coelomic fluid enters the funnel, is modified along the tubule and leaves through a nephridiopore. In segmented annelids each segment typically has a pair, whose funnel lies in the segment in front of the one in which the tubule opens.

**Definition 4.6.3 (Malpighian Tubule)** A **Malpighian tubule** is a blind excretory tubule of terrestrial arthropods (insects, myriapods, arachnids) that lies free in the hemocoel and opens into the gut at the junction between midgut and hindgut. Its cells actively secrete potassium and other ions into the lumen, water and wastes follow, and the fluid is modified further in the hindgut and rectum, where most of the water and ions are reabsorbed.

![Three types of invertebrate excretory organ (schematic, not to scale). (A) Protonephridium of a flatworm: branched blind tubules ending in flame cells whose ciliary tufts drive fluid through the tubule to the nephridiopore. (B) Metanephridium of an annelid: a ciliated funnel, the nephrostome, opens into the coelom of one segment; the coiled tubule passes through the septum and opens through a nephridiopore in the next segment, modifying the fluid on the way. (C) Malpighian tubules of an insect: blind tubules bathed in hemolymph secrete ions, and water and nitrogenous waste follow; the fluid enters the gut at the junction of midgut and hindgut, and the rectum reabsorbs water and ions](./plots/excretory-organs.py)

Protonephridia occur in animals without a spacious coelom or without a closed circulation: flatworms, rotifers, gastrotrichs, nemerteans, and the larvae (the trochophores) of annelids and molluscs. Metanephridia occur in coelomate animals with a circulatory system. In these, as Ruppert and Smith (1988) showed, filtration does not take place in the nephridium itself: blood pressure forces fluid out of the blood vessels across a filter formed by specialized coelomic lining cells with slit-like gaps between their processes (podocytes), into the coelom, and the metanephridium collects and modifies the filtrate. The vertebrate kidney follows the same scheme in a compact form: in each **nephron** blood is filtered across the podocyte layer of the glomerulus into Bowman's capsule, a derivative of the coelom, and the tubule reabsorbs most of the filtrate ([7.14.22](/7.14.22)).

Malpighian tubules work without filtration, by secretion. They evolved independently in insects and arachnids, and they suit animals on land that must conserve water: uric acid precipitates in the hindgut and can be excreted almost dry. Crustaceans have instead antennal or maxillary glands (green glands), and arachnids, besides Malpighian tubules, coxal glands; both are sacs derived from the coelom with a filtering wall and a tubule. In freshwater sponges, as in freshwater protists, water entering by osmosis is expelled by contractile vacuoles.

### 4.6.1. Excretory Organs across the Phyla

| Group | Excretory organ | Origin and remarks | Chapter |
|---|---|---|---|
| Sponges, cnidarians, ctenophores, placozoans | None | Diffusion of ammonia across the body surface; contractile vacuoles in cells of freshwater sponges | [7.17.7](/7.17.7)–[7.17.9](/7.17.9) |
| Xenacoelomorphs | None | Their absence of nephridia defines the sister group Nephrozoa | [7.17.10](/7.17.10) |
| Flatworms, gastrotrichs, rotifers, nemerteans | Protonephridia with flame cells | Osmoregulation as much as excretion; in rotifers the tubules open into a bladder | [7.17.11](/7.17.11), [7.17.12](/7.17.12) |
| Annelids | Metanephridia, one pair per segment; protonephridia in larvae and some small adults | Chloragogen tissue on the gut stores and processes nitrogenous waste, like a liver | [7.17.15](/7.17.15) |
| Molluscs | Kidneys (one or two), metanephridia draining the pericardial coelom through renopericardial canals | Ultrafiltration across the heart wall into the pericardium | [7.17.13](/7.17.13) |
| Nematodes | Renette cells or an H-shaped system of canals | No cilia, as in all ecdysozoans | [7.17.17](/7.17.17) |
| Crustaceans | Antennal glands (green glands) or maxillary glands | Coelomic end sac with podocytes, labyrinth and tubule | [7.17.21](/7.17.21) |
| Arachnids | Coxal glands and Malpighian tubules | The tubules grow from the endodermal midgut | [7.17.19](/7.17.19#sec-19.6) |
| Insects, myriapods | Malpighian tubules | The tubules grow from the ectodermal hindgut; cryptonephric systems in some beetles and caterpillars | [7.17.26](/7.17.26#sec-26.3) |
| Echinoderms | None | Diffusion across tube feet and gills; coelomocytes collect waste | [7.17.42](/7.17.42) |
| Lancelets | Protonephridia with solenocyte-like terminal cells (cyrtopodocytes) | A chordate with protonephridia: their terminal cells lie on blood vessels and are thought to filter the blood | [7.17.43](/7.17.43) |
| Tunicates | No tubular organ | Nephrocytes and a renal sac that stores urate concretions | [7.17.43](/7.17.43) |
| Vertebrates | Kidneys of nephrons: pronephros, mesonephros or opisthonephros, metanephros | Derived from intermediate mesoderm; ducts used also by the male reproductive system | [7.17.66](/7.17.66) |

Two general points emerge. The organs are tubes in almost every phylum that has them, and they work by producing a primary fluid and modifying it; and the terminal structure, a cilia-driven weir in protonephridia, a coelomic funnel in metanephridia or a blood-filtering podocyte layer in the coelomic sacs of crustaceans, mollusc hearts and vertebrate glomeruli, depends on whether the animal has a coelom and a pressurized circulation. Whether protonephridia and metanephridia are homologous, and how the nephridia of different phyla are related, is discussed with the evolution of organ systems in [7.17.44](/7.17.44).

## 4.7. Nervous Systems

The nervous system of an animal reflects its symmetry and way of life (the cellular and molecular evolution of nervous systems is treated in [7.16.53](/7.16.53)). Four types of overall arrangement are distinguished:

- A **nerve net** of interconnected neurons spread through the epithelia, without a central ganglion, in cnidarians and ctenophores. Impulses spread in all directions from a stimulus, which suits radial animals; local condensations form nerve rings around the margin of medusae and around the mouth.
- A ladder-like nervous system, with cerebral ganglia and several longitudinal nerve cords joined by transverse commissures, in flatworms and some other small worms.
- A ventral nerve cord of paired ganglia, one pair per segment, in annelids and arthropods, below the gut, with a brain above the pharynx connected to it by a ring around the gut.
- A dorsal hollow nerve cord, the neural tube, above the gut, enlarged anteriorly into a brain, in chordates (**dorsal hollow nerve cord**, [7.17.43](/7.17.43)).

**Definition 4.7.1 (Ladder-Like Nervous System, Ventral Nerve Cord)** A **ladder-like nervous system** (orthogon) consists of an anterior cerebral ganglion and several pairs of longitudinal nerve cords linked at intervals by transverse commissures, like the rungs of a ladder. A **ventral nerve cord** (ganglionated ventral nerve cord) is a pair of nerve cords, often fused, running along the ventral midline below the gut and bearing a pair of ganglia in each segment, connected to the brain by circumpharyngeal (circumesophageal) connectives.

Other phyla have their own arrangements: molluscs have several pairs of ganglia connected by nerve cords, concentrated into a large brain around the esophagus in cephalopods; echinoderms have a nerve ring around the mouth with radial nerves into the arms and no brain. The trend toward centralization, with fewer longitudinal cords, concentration of ganglia and a large anterior brain, accompanies active locomotion and cephalization; sessile animals such as bryozoans, tunicates and bivalves show the opposite trend. As noted in [7.17.3](/7.17.3#sec-3.2.2), the ventral nerve cord of protostomes and the dorsal cord of chordates are specified by the same genes from an inverted dorsoventral axis, which suggests that the bilaterian ancestor already had a centralized nerve cord, although this is debated.

### 4.7.1. Nervous Systems by Phylum

| Group | Arrangement | Remarks | Chapter |
|---|---|---|---|
| Sponges, placozoans | No neurons | Coordination by contractile cells and chemical signals; sponges have many synaptic genes | [7.17.7](/7.17.7), [7.17.8](/7.17.8) |
| Ctenophores | Subepithelial nerve net, a syncytium in *Mnemiopsis*; apical organ with statolith | Neurons may have evolved independently ([7.17.6](/7.17.6#sec-6.5.1)) | [7.17.8](/7.17.8) |
| Cnidarians | **Nerve net** in epidermis and gastrodermis; nerve rings and rhopalia in medusae | Rhopalia of box jellyfish carry lens eyes | [7.17.9](/7.17.9) |
| Xenacoelomorphs | Basiepidermal nerve net with an anterior condensation | | [7.17.10](/7.17.10) |
| Flatworms | Bilobed brain and an orthogon of longitudinal cords (**ladder-like nervous system**) | Planarians regenerate the brain | [7.17.11](/7.17.11) |
| Molluscs | Paired cerebral, pedal, pleural and visceral ganglia; tetraneurous cords in chitons | Cephalopod brain of fused ganglia around the esophagus | [7.17.13](/7.17.13), [7.17.14](/7.17.14) |
| Annelids | Dorsal brain, circumpharyngeal connectives, **ventral nerve cord** with segmental ganglia; giant axons | | [7.17.15](/7.17.15) |
| Nematodes | Nerve ring around the pharynx, dorsal and ventral cords | 302 neurons in the hermaphrodite *C. elegans* | [7.17.17](/7.17.17) |
| Arthropods | Brain of protocerebrum, deutocerebrum and tritocerebrum; ventral cord, often with fused ganglia | | [7.17.18](/7.17.18), [7.17.26](/7.17.26#sec-26.6) |
| Echinoderms | Circumoral nerve ring and radial nerves; no brain | Ectoneural and hyponeural systems | [7.17.42](/7.17.42) |
| Hemichordates | Epidermal nerve net with dorsal and ventral cords; a hollow collar cord | | [7.17.41](/7.17.41) |
| Chordates | **Dorsal hollow nerve cord** with an anterior brain | Cerebral vesicle in lancelets; three-part brain in vertebrates | [7.17.43](/7.17.43), [7.17.67](/7.17.67) |

### 4.7.2. Sense Organs: Basic Types

Sense organs are as varied as nervous systems, but most fall into a few types, each found in many phyla.

| Type | Structure | Examples |
|---|---|---|
| Statocyst | A fluid-filled sac with sensory cilia and a dense statolith; senses gravity | Ctenophore apical organ, medusae, acoels, molluscs, decapod crustaceans; the vertebrate inner ear is a comparable organ |
| Mechanoreceptors on the surface | Ciliary sensory cells, or sensilla in a cuticle | Lateral-line neuromasts of fishes; insect hairs, campaniform and chordotonal sensilla ([7.17.27](/7.17.27)) |
| Chemoreceptors | Sensory cells in pits or on appendages | Nuchal organs of polychaetes, the osphradium of molluscs, aesthetascs of crustacean antennules, insect sensilla, vertebrate olfactory epithelium |
| Eyespot and pigment-cup ocellus | Photoreceptors shaded on one side by pigment, giving the direction of light | Flatworms, larvae of many invertebrates, polychaetes |
| Pinhole eye | A deep cup with a small aperture and no lens | *Nautilus* |
| Lens (camera) eye | A cup with a lens focusing an image on a retina | Vertebrates, cephalopods, box jellyfish, some polychaetes and gastropods, jumping spiders |
| **Compound eye** | Many ommatidia, each with its own lens | Arthropods (apposition and superposition types), sabellid fan worms, ark clams |
| Mirror eye | A concave reflector forms the image | Scallops |

Photoreceptor cells are of two kinds: ciliary photoreceptors, whose membrane is expanded from a cilium (vertebrate rods and cones, many cnidarians), and rhabdomeric ones, whose membrane forms microvilli (arthropods, cephalopods). Both kinds are present in many animals, and their distribution suggests that the bilaterian ancestor had both ([7.16.53](/7.16.53#sec-53.4)). The repeated origin of image-forming eyes from these elements is a classic example of convergence on a common genetic basis (Pax6), discussed in [7.17.44](/7.17.44).

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

### 4.8.1. Gonads, Ducts and the Transfer of Sperm

The reproductive organs of animals are built from a few components: gonads, which are mesodermal in most bilaterians and lie in or next to the coelom, ducts that carry the gametes out, and accessory organs that store or package sperm and provide eggs with yolk and protective coverings. Their arrangement varies with the mode of fertilization.

| Arrangement | Description | Examples | Chapter |
|---|---|---|---|
| No permanent gonads | Gametes differentiate from scattered cells and leave through the body cavity or the mouth | Sponges (from choanocytes and archaeocytes), many cnidarians | [7.17.7](/7.17.7), [7.17.9](/7.17.9) |
| Gonads shedding into the coelom | Gametes mature in the coelom and leave through metanephridia or coelomoducts, or by rupture of the body wall | Many polychaetes, sipunculans | [7.17.15](/7.17.15) |
| Gonads with their own ducts, external fertilization | Spawning of eggs and sperm into the water | Many bivalves, echinoderms, most bony fishes | [7.17.42](/7.17.42) |
| Complex hermaphroditic system | Ovary, testes, yolk glands (vitellaria), seminal receptacles and a copulatory organ in one individual | Flatworms, earthworms, pulmonate snails | [7.17.11](/7.17.11), [7.17.15](/7.17.15) |
| Spermatophores | Sperm packaged in a capsule, transferred directly or deposited for the female to pick up | Cephalopods (by the hectocotylus), many arachnids and myriapods, collembolans, salamanders | [7.17.14](/7.17.14), [7.17.19](/7.17.19) |
| Copulation with sperm storage | Internal fertilization with a sperm-storage organ in the female | Insects (spermatheca), sharks, amniotes | [7.17.28](/7.17.28) |
| Hypodermic insemination | Sperm injected through the body wall | Some flatworms and leeches, bed bugs (traumatic insemination) | [7.17.32](/7.17.32) |

Sperm structure reflects these modes. The sperm of external fertilizers usually has a small head, a midpiece of a few mitochondria and a simple flagellum (the "primitive" aquasperm), whereas internal fertilization is often accompanied by elongated, modified sperm (introsperm), sometimes without a flagellum, as in nematodes, whose sperm crawl by amoeboid movement. Brooding, viviparity and the provision of yolk are treated with life histories in [7.17.5](/7.17.5).

## 4.9. The Body Wall and Its Coverings

The **integument** separates the animal from its environment, protects it, and in many groups also secretes the skeleton, exchanges gases or absorbs food. Its basic component is the epidermis, a single-layered or stratified epithelium of ectodermal origin, with the muscles of the body wall beneath it; Chinese textbooks call the combination of epidermis and muscle layers in worms the "dermomuscular sac".

| Covering | Structure | Examples | Chapter |
|---|---|---|---|
| Ciliated epidermis | Single-layered epithelium with motile cilia and gland cells | Xenacoelomorphs, turbellarian flatworms, nemerteans, many larvae | [7.17.11](/7.17.11) |
| Syncytial tegument | A nonciliated syncytium whose nuclei lie below the muscle layers; absorbs nutrients | Parasitic flatworms (Neodermata), acanthocephalans | [7.17.11](/7.17.11#sec-11.4) |
| Collagenous cuticle, not molted | Secreted by the epidermis and grown continuously | Annelids | [7.17.15](/7.17.15) |
| Molted cuticle | Shed and replaced at each molt under ecdysteroid control: collagenous in nematodes, chitinous in panarthropods and scalidophorans | Ecdysozoa | [7.17.17](/7.17.17), [7.17.23](/7.17.23#sec-23.1) |
| Shell | Calcium carbonate secreted by the mantle | Molluscs, brachiopods | [7.17.13](/7.17.13) |
| Tunic | Cellulose-like tunicin with cells, secreted by the epidermis | Tunicates, the only animals that make cellulose | [7.17.43](/7.17.43) |
| Stratified, keratinized epidermis over a dermis | Multilayered epidermis producing keratin structures (scales, feathers, hair), with dermal bone and scales in many | Vertebrates | [7.17.57](/7.17.57) |

The choice of covering is linked to the other systems of the body plan. A ciliated epidermis is possible only in a moist or aquatic animal and serves for locomotion; a cuticle that is never shed allows growth only if it is thin and flexible; a hard molted cuticle forces growth into steps ([7.17.29](/7.17.29)); a keratinized skin limits water loss on land and makes the skin useless for respiration, except in amphibians, which keep a thin, moist skin and breathe through it.

## 4.10. Chemical Coordination

All animals with nervous systems also use chemical messengers carried by the body fluids, and in most invertebrates the main endocrine cells are neurosecretory cells of the central nervous system (**neurosecretion**), whose products are released from neurohemal organs into the blood or hemolymph. Separate endocrine glands of non-neural origin occur in arthropods and vertebrates.

| Group | Main endocrine structures | Hormones and functions | Chapter |
|---|---|---|---|
| Cnidarians | Neurosecretory cells | Neuropeptides controlling metamorphosis, strobilation and spawning | [7.17.9](/7.17.9) |
| Annelids | Neurosecretory cells of the brain | Regeneration, maturation and the switch to epitoky in polychaetes | [7.17.15](/7.17.15) |
| Molluscs | Neurosecretory cells; optic glands of cephalopods | Egg-laying hormone of *Aplysia*; optic gland secretions control maturation and post-reproductive death in octopuses | [7.17.14](/7.17.14) |
| Crustaceans | X-organ–sinus gland complex in the eyestalk; Y-organs | Molt-inhibiting hormone versus ecdysteroids; pigment-dispersing hormones | [7.17.21](/7.17.21) |
| Insects | Brain neurosecretory cells, corpora cardiaca, corpora allata, prothoracic glands | Prothoracicotropic hormone, ecdysone, juvenile hormone, bursicon, adipokinetic hormone | [7.17.26](/7.17.26#sec-26.7), [7.17.29](/7.17.29#sec-29.4) |
| Echinoderms | Neurosecretory cells of the radial nerves | Relaxin-like gonad-stimulating substance induces spawning in sea stars | [7.17.42](/7.17.42) |
| Vertebrates | Hypothalamus and pituitary, thyroid, adrenals, pancreatic islets, gonads and others | [7.14.32](/7.14.32) and the following chapters | [7.17.67](/7.17.67) |

Many hormone families are older than the phyla that use them. Insulin-like peptides regulate growth and metabolism in insects, nematodes and vertebrates; the vertebrate thyroid hormones control metamorphosis in amphibians, and related iodinated compounds act in the metamorphosis of lancelets and tunicates; and the nuclear hormone receptors that relay the ecdysone signal in the insect molting cycle have orthologues that drive the molting cycle of nematodes, although *Caenorhabditis elegans* does not use ecdysone itself. Such cases show the endocrine system, like the nervous system, as an ancient toolkit deployed differently in different body plans ([7.14.32](/7.14.32)).

## Summary

| Problem | Solutions (where) |
|---|---|
| Size and diffusion | Surface/volume $= 3/r$ for a sphere; diffusion time $t \approx x^2/2D$ (Formula 4.1.1); flat (flatworms), thin (nemerteans), inert core (medusae), water through the body (sponges), exchange organs and circulation (large active animals); metabolic rates per gram scale as $M^{-1/4}$ |
| Support | **Hydrostatic skeleton** (worms, polyps), muscular hydrostats (Definition 4.2.1), exoskeleton (arthropods, molluscs), endoskeleton (echinoderms, vertebrates); helical fiber lattices with the optimum $54^\circ 44'$ (Formula 4.2.1); levers trade force for speed (Formula 4.2.2); tubes are stiffer than rods of the same mass |
| Movement | Amoeboid, ciliary (small animals, low $Re$), hydrostatic (peristalsis, two-anchor burrowing, pedal waves, jets), muscles and levers (walking, paddling, flight), undulation; cost of transport (Definition 4.3.1) lowest for swimming, highest for running |
| Feeding | **Filter feeding** (Definition 4.4.1) by choanocytes, ciliary bands (downstream or upstream), mucus sheets and nets, setose limbs, tentacles or baleen; deposit feeding, grazing, predation, fluid feeding, symbionts, absorption |
| Digestion | Intracellular (sponges); **gastrovascular cavity** (cnidarians, flatworms); **complete digestive tract** (Nephrozoa) (Definition 4.4.2) with ectodermal foregut and hindgut and endodermal midgut |
| Gas exchange | Body surface, gills, lungs, tracheae; open or closed circulation; hemoglobin, chlorocruorin, hemocyanin, hemerythrin |
| Excretion | **Protonephridia** with **flame cells** (Definition 4.6.1), **metanephridia** (Definition 4.6.2), **Malpighian tubules** (Definition 4.6.3), antennal and coxal glands, nephrons; filtration (or secretion) followed by modification |
| Coordination | Nerve net, **ladder-like nervous system**, **ventral nerve cord** (Definition 4.7.1), dorsal hollow nerve cord; statocysts, eyespots, pinhole, lens, compound and mirror eyes; neurosecretory cells and endocrine glands |
| Reproduction | Budding, fission, fragmentation, parthenogenesis; gonochorism and simultaneous or sequential hermaphroditism; spawning, spermatophores, copulation, hypodermic insemination |
| Body covering | Ciliated epidermis, syncytial tegument, collagenous or molted cuticle, shell, tunic, keratinized skin |

## Questions

1. Show from Eq. (4.1) that the maximum volume is reached at $\tan\theta = \sqrt{2}$, and compute the aspect ratio $l/2r$ of the cylinder at that angle.

   **Answer** $\frac{\mathrm{d}}{\mathrm{d}\theta}(\sin^2\theta\cos\theta) = 2\sin\theta\cos^2\theta - \sin^3\theta = \sin\theta\,(2\cos^2\theta - \sin^2\theta)$, which vanishes for $0 < \theta < 90^\circ$ when $\tan^2\theta = 2$, so $\theta = \arctan\sqrt{2} \approx 54.74^\circ = 54^\circ 44'$. The aspect ratio is $\pi\cot\theta = \pi/\sqrt{2} \approx 2.2$: at maximum volume the worm segment is about twice as long as it is wide.

2. A flatworm consumes oxygen at $M = 2.6\times10^{-4}\,\mathrm{mol\,m^{-3}\,s^{-1}}$. Using the values of the diffusion-limit figure, what is the greatest thickness it can have if it is a flat sheet, and what is the greatest radius of a spherical animal with the same metabolic rate?

   **Answer** The half-thickness of a sheet is $\sqrt{2Dc_0/M} = \sqrt{2 \times 2\times10^{-9} \times 0.25 / 2.6\times10^{-4}} \approx \sqrt{3.8\times10^{-6}}\,\mathrm{m} \approx 2.0\,\mathrm{mm}$, so the total thickness can reach about 4 mm (real flatworms are thinner, because their surface concentration and diffusion coefficient are lower and they are often active). A sphere could have a radius of $\sqrt{6Dc_0/M} \approx 3.4\,\mathrm{mm}$; but a flat sheet can have any length and width, whereas the sphere is limited in all directions.

3. Why do metanephridia occur in animals with a circulatory system and a coelom, whereas protonephridia are typical of small animals without them?

   **Answer** A metanephridium does not filter; it collects fluid from the coelom. It works only where a filtrate is produced in the coelom, which requires blood vessels with enough pressure to force fluid across the podocyte filter of the coelomic lining. Without a coelom and a pressurized circulation, the animal must make the filtrate itself, and the protonephridium does so by the negative pressure generated by its ciliary flame, which draws body fluid through the weir of the terminal cell. The correspondence is not perfect: some coelomates have protonephridia, and annelid larvae have protonephridia before the adult metanephridia develop.

4. A ciliated larva 0.2 mm long swims at 1 mm/s in seawater ($\rho \approx 1025\,\mathrm{kg\,m^{-3}}$, $\mu \approx 1.1\times10^{-3}\,\mathrm{Pa\,s}$). Compute its Reynolds number and explain why it cannot swim by flapping a rigid paddle back and forth.

   **Answer** $Re = \rho U L/\mu = 1025 \times 10^{-3} \times 2\times10^{-4} / 1.1\times10^{-3} \approx 0.19$. Viscous forces dominate and inertia is negligible, so the flow depends only on the instantaneous motion of the body, not on its history. A rigid paddle that moves back along exactly the path of its forward stroke reverses all the flow it produced and the larva returns to where it was. Cilia avoid this by changing shape: a stiff power stroke and a flexible recovery stroke close to the body sweep different areas.

5. A muscle inserts 2 cm from the elbow joint of a forelimb and the hand is 30 cm from the joint. If the muscle exerts 600 N and shortens at 5 cm/s, what force can the hand exert and how fast does it move? How would a digging animal change this design?

   **Answer** By Eq. (4.3) the mechanical advantage is $l_{\mathrm{in}}/l_{\mathrm{out}} = 2/30 = 1/15$. The hand exerts $600/15 = 40\,\mathrm{N}$ and moves at $5 \times 15 = 75\,\mathrm{cm/s}$. A digging animal such as a mole has a longer olecranon process (in-lever) and a shorter forearm (out-lever), increasing the mechanical advantage: it gains force at the expense of speed.

6. Using Eq. (4.2), estimate how long oxygen would take to diffuse from the surface to the center of a sphere of radius 5 mm, and explain why an earthworm of that radius needs a circulatory system although a planarian of the same length does not.

   **Answer** With $D = 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$, $t \approx (5\times10^{-3})^2/(2 \times 2\times10^{-9}) \approx 6\times10^{3}\,\mathrm{s}$, about 1.7 hours, far too slow to supply metabolizing tissue. The earthworm's body is a cylinder several millimeters thick, so its inner tissues are too far from the surface; blood pumped through capillaries brings oxygen within a few micrometers of every cell. A planarian is equally long but only a fraction of a millimeter thick, so that every cell lies within a diffusion distance of the surface (Section 4.1.2), and its branched gut distributes food.
