---
title: Membrane Transport and the Movement of Water
description: Why membrane transport is needed; simple diffusion and the permeability coefficient P = KD/Δx; protein pores, ion channels and carriers, selectivity and the two-state Boltzmann form of gating; saturation kinetics of facilitated diffusion J = k₃R₀A/(A + K_d); electrochemical potential and net driving force; primary active transport (Na⁺/K⁺-ATPase, Ca²⁺ pump, H⁺ pump) and secondary active transport (1:1 and 2:1 concentrating power of SGLT, the Ca²⁺ gradient NCX can maintain); comparison of the classes of transport proteins; water transport, aquaporins, osmolarity and osmotic pressure (1 mOsm/L ≈ 19.3 mmHg), isosmotic versus isotonic solutions, cell volume; coupled ion and water absorption across epithelia; Na⁺-driven and H⁺/K⁺-driven secondary transport and the evolution of aquaporins across groups.
source_hash: 9ed9a1b0b673
---

The cell is an open functional unit: it must take up glucose, amino acids and $\ce{O2}$ from the extracellular fluid, expel $\ce{CO2}$, $\ce{H+}$ and metabolic waste, maintain an ionic composition quite different from that of the extracellular fluid (Chapter 1), and change the permeability to certain substances as function demands. The **lipid bilayer** by itself lets almost no ions or polar molecules through, so the two basic features of membrane transport are necessity and controllability: almost every substance needs membrane proteins to cross the membrane at a physiologically useful rate, and the type, number, distribution and activity of these proteins are all regulated. This chapter classifies membrane transport by driving force and carrier (Sections 3.1–3.4), compares the classes of transport proteins (Section 3.5), then treats the movement of water and cell volume (Section 3.6) and how epithelia combine the transport of single cells into transepithelial absorption and secretion (Section 3.7). The next chapter derives the membrane potential from the same ion gradients.

The structure and classification of membranes and transport proteins are given in biochemistry ([7.1.13](/7.1.13)); the **pump–leak model** of the Na⁺/K⁺-ATPase, cell volume and transepithelial transport are treated in cell biology ([7.3.5](/7.3.5)), and the statistical physics of channel gating in [7.6.4](/7.6.4). This chapter stresses quantitative physiological reasoning: by what factor a transporter can concentrate its substrate, and whether a solution will make a cell swell or shrink.

## 3.1. Modes of Membrane Transport

By whether metabolic energy is consumed, membrane transport is divided into **passive transport** (down the electrochemical gradient, without direct consumption of ATP) and **active transport** (against the electrochemical gradient, requiring energy). By carrier, it is divided into simple diffusion through the lipid bilayer, diffusion through protein pores or channels, carrier-mediated diffusion, active transport by pumps and coupled transporters, and **endocytosis** and **exocytosis** by membrane vesicles (for macromolecules such as antibodies and substances that cannot be transported by carriers).

| Mode | Carrier | Energy | Direction | Examples |
|---|---|---|---|---|
| Simple diffusion | Lipid bilayer | None | Down the concentration gradient | $\ce{O2}$, $\ce{CO2}$, $\ce{NH3}$, ethanol, **steroid hormones** |
| Through pores and channels | Porins, ion channels | None | Down the electrochemical gradient | Water, $\ce{Na+}$, $\ce{K+}$, $\ce{Ca^2+}$, $\ce{Cl-}$ |
| Carrier-mediated diffusion | **Uniporters** | None | Down the electrochemical gradient | Glucose (GLUT), urea |
| Primary active transport | ATPases (pumps) | ATP | Against the gradient | $\ce{Na+}$/$\ce{K+}$, $\ce{Ca^2+}$, $\ce{H+}$ |
| Secondary active transport | Symporters, antiporters | Gradient of another ion | One down, one up | Glucose (SGLT), $\ce{Ca^2+}$ (NCX), $\ce{H+}$ (NHE) |
| Vesicular transport | Endocytosis, exocytosis | ATP, GTP | — | Proteins, **neurotransmitters**, hormones |

## 3.2. Simple Diffusion

Small lipid-soluble molecules dissolve directly in the lipid bilayer and cross it.

**Definition 3.2.1 (Simple Diffusion and Permeability Coefficient)** The transport of a substance directly across the lipid bilayer down its concentration gradient, without the aid of membrane proteins, is called **simple diffusion**. Its rate is proportional to the concentration difference across the membrane,
$$
\frac{\mathrm{d}n}{\mathrm{d}t} = PA\,\Delta C, \tag{3.1}
$$
where $n$ is the number of molecules (or amount of substance), $A$ the membrane area and $\Delta C$ the concentration difference; the constant of proportionality $P$ (in $\mathrm{cm\,s^{-1}}$) is called the **permeability coefficient** of the substance.

Eq. (3.1) follows from **Fick's law** within the membrane: if the **partition coefficient** of the substance between the aqueous phase and the membrane is $K$ (the ratio of concentration in the membrane to that in water), its diffusion coefficient in the membrane is $D$ and the membrane thickness is $\Delta x$, then the concentration difference within the membrane is $K\Delta C$ and the flux is $DK\Delta C/\Delta x$, so that
$$
P = \frac{KD}{\Delta x}. \tag{3.2}
$$
The permeability coefficient is determined mainly by the partition coefficient: nonpolar $\ce{O2}$, $\ce{CO2}$ and fatty acids enter the hydrocarbon core of the membrane easily and have large $P$; polar molecules and ions are surrounded by hydration shells and entering the hydrocarbon core costs a great deal of free energy, so $P$ is smaller by several to more than ten orders of magnitude ($P$ for $\ce{K+}$ across a pure lipid bilayer is about $10^{-12}\,\mathrm{cm\,s^{-1}}$, for water about $10^{-3}$, for $\ce{O2}$ about $10$).

By Eqs. (3.1)–(3.2), the means by which a cell can regulate the simple diffusion of a substance are limited: changing the membrane area (microvilli, membrane folding), changing the composition and thickness of the membrane (**cholesterol** and **sphingolipids** make the membrane denser and less permeable), or changing the concentration gradient (rapid consumption of the incoming $\ce{O2}$, or conversion of $\ce{CO2}$ to $\ce{HCO3-}$). For $\ce{O2}$ the most important variables are diffusion distance and area, which is why the walls of alveoli and capillaries are extremely thin and their area extremely large (Chapters 18 and 19).

## 3.3. Pores, Channels and Carriers

### 3.3.1. Biological Membranes Are Far More Permeable than Artificial Ones

Biological membranes are permeable to water and ions by several orders of magnitude more than pure lipid bilayers, are selective (passing only one ion or one class of ions), and are regulated (the number, type, distribution and open or closed state of channels can be changed). These properties show that specialized protein pathways exist in the membrane: pores, channels and carriers.

Protein pores are continuously open, with a fast rate of passage, and can be approximated as straight tubes whose selectivity depends mainly on pore size. Examples are the **porins** of the outer mitochondrial membrane (passing ATP and small molecules), perforin secreted by cytotoxic T cells (making holes in the membrane of target cells), the **nuclear pore complex**, and the **aquaporins** that pass only water (Section 3.6).

**Ion channels** have selectivity and gating. Selectivity depends on two factors: the size and shape of the narrowest part of the pore (the **selectivity filter**) and the distribution of charge around the pore. The filter of a $\ce{Na+}$ channel is about $0.3 \times 0.5\,\mathrm{nm}$, negatively charged amino acid residues attract cations, and the pore just accommodates partly dehydrated $\ce{Na+}$. A $\ce{K+}$ channel is about 1000 times more permeable to $\ce{K+}$ than to $\ce{Na+}$: a ring of carbonyl oxygen atoms in the filter just replaces the hydration shell of $\ce{K+}$, compensating the energy lost in dehydrating $\ce{K+}$; the smaller $\ce{Na+}$ is too far from these oxygen atoms and, once dehydrated, obtains no such compensation, so it passes with difficulty (structure and energetics in [7.6.30](/7.6.30)).

### 3.3.2. Gating

A channel switches at random between open and closed conformations, and single-channel recordings show the current jumping between zero and a fixed value. If the free-energy difference between the open and closed states is $\Delta G = G_{\text{open}} - G_{\text{closed}}$, then by the **Boltzmann distribution** the open probability is
$$
P_{\mathrm{o}} = \frac{1}{1 + \mathrm{e}^{\Delta G/k_{\mathrm{B}}T}}, \tag{3.3}
$$
the two-state model of [7.6.4](/7.6.4). A gating stimulus changes $\Delta G$: for a **voltage-gated channel**, $\Delta G = \Delta G_0 - zeV$ ($ze$ is the **gating charge**), and $P_{\mathrm{o}}$ varies sigmoidally with membrane potential $V$, the curve being steeper the larger $z$; for a **ligand-gated channel**, the ligand binds the open state more tightly and lowers $\Delta G$; for a **mechanosensitive channel**, work done by **membrane tension** lowers $\Delta G$; temperature-sensitive TRP channels have a large gating enthalpy change.

At the macroscopic level the conductance of the membrane for an ion is $N \times P_{\mathrm{o}} \times \gamma$ (number of channels, open probability, single-channel conductance), and the cell can regulate ion permeability by expression (changing $N$), gating (changing $P_{\mathrm{o}}$), and modification and subunit composition (changing $\gamma$ and gating properties); this underlies the electrical signals of nerve and muscle (Chapter 4).

### 3.3.3. Carrier-Mediated Diffusion

Polar molecules such as glucose and amino acids are too large to pass through channels; they are transported by carriers (**transporters**). Carriers work by the **alternating-access mechanism**: the substrate binding site faces alternately the two sides of the membrane, and each cycle moves only one or a few molecules. Carrier transport that consumes no energy and runs down the concentration gradient is called **facilitated diffusion**, for example the glucose transporter GLUT of red cells and most tissues.

The hallmark of carrier transport is saturation. Let the total number of carriers be $R_0$, let substrate $A$ bind the carrier rapidly with **dissociation constant** $K_{\mathrm{d}}$, and let the bound complex complete transport with rate constant $k_3$; then
$$
J = k_3R_0\frac{A}{A + K_{\mathrm{d}}}. \tag{3.4}
$$
This has the same form as the **Michaelis–Menten equation** of enzyme kinetics. For $A \ll K_{\mathrm{d}}$, $J \approx (k_3R_0/K_{\mathrm{d}})A$, linear as in simple diffusion; for $A \gg K_{\mathrm{d}}$, $J \to k_3R_0$, the maximal transport rate. In addition, carriers are stereospecific (GLUT transports D-glucose and hardly transports L-glucose) and are subject to **competitive inhibition** by structural analogues.

Eq. (3.4) points to three ways of regulation: changing the carrier number $R_0$, the affinity $K_{\mathrm{d}}$ or the turnover rate $k_3$. The first is the commonest in physiology: **insulin** moves GLUT4, stored in intracellular vesicles, to the membrane of muscle and fat cells and raises glucose uptake several-fold within minutes (Chapter 35). Different tissues use isoforms with different $K_{\mathrm{d}}$ to suit their needs: GLUT1 (red cells, **blood–brain barrier**) and GLUT3 (neurons) have $K_{\mathrm{d}}$ of about $1$–$2\,\mathrm{mmol\,L^{-1}}$ and are nearly saturated at normal blood glucose (about $5\,\mathrm{mmol\,L^{-1}}$), ensuring a steady energy supply to these tissues; GLUT2 of the liver and pancreatic β cells has a $K_{\mathrm{d}}$ of about $17\,\mathrm{mmol\,L^{-1}}$, and its transport rate varies almost linearly with blood glucose, so that these cells can "sense" whether blood glucose is high or low.

![Simple diffusion and carrier-mediated diffusion. A: influx as a function of extracellular concentration A (intracellular concentration kept near zero). Simple diffusion is linear; the carrier saturates as J = k₃R₀A/(A + Kd) and tends to k₃R₀ for A ≫ Kd. At the same maximal rate, a GLUT1-like carrier with Kd = 1.5 mM is already nearly saturated over the blood glucose range (gray band, 4–8 mM), whereas a GLUT2-like carrier with Kd = 17 mM varies almost linearly with blood glucose. B: three ways of regulating carrier flux at A = 5 mM: doubling the number of carriers (as when insulin brings GLUT4 to the membrane), doubling the affinity (Kd halved) or doubling the turnover rate](./plots/carrier-kinetics.py)

## 3.4. Electrochemical Driving Force and Active Transport

### 3.4.1. Electrochemical Potential

A concentration difference is not the only factor driving substances across the membrane. For charged ions the electrical potential difference across the membrane is equally important; for the exchange of water and solutes across the vessel wall, hydrostatic pressure also acts. When an ion $\mathrm{X}$ (valence $z_{\mathrm{X}}$) moves from outside to inside, the change in **electrochemical potential** per mole is
$$
\Delta\tilde\mu_{\mathrm{X}} = RT\ln\frac{[\mathrm{X}]_{\mathrm{i}}}{[\mathrm{X}]_{\mathrm{o}}} + z_{\mathrm{X}}F(\psi_{\mathrm{i}} - \psi_{\mathrm{o}}) = RT\ln\frac{[\mathrm{X}]_{\mathrm{i}}}{[\mathrm{X}]_{\mathrm{o}}} + z_{\mathrm{X}}FV_{\mathrm{m}}, \tag{3.5}
$$
where the first term is the chemical potential difference, the second the electrical potential energy difference, and $V_{\mathrm{m}} = \psi_{\mathrm{i}} - \psi_{\mathrm{o}}$ is the membrane potential (by convention inside relative to outside). When $\Delta\tilde\mu_{\mathrm{X}} < 0$ the ion flows spontaneously inward, when $> 0$ spontaneously outward, and when $= 0$ it is at equilibrium.

**Example 3.4.1 (Driving Force for $\ce{Na+}$ Influx)** At $37\,{}^\circ\mathrm{C}$ ($RT = 2.58\,\mathrm{kJ\,mol^{-1}}$), take $[\ce{Na+}]_{\mathrm{o}} = 145$, $[\ce{Na+}]_{\mathrm{i}} = 12\,\mathrm{mmol\,L^{-1}}$ and $V_{\mathrm{m}} = -70\,\mathrm{mV}$: the chemical term is $2.58\ln(12/145) = -6.4\,\mathrm{kJ\,mol^{-1}}$, the electrical term $96.5 \times (-0.070) = -6.8\,\mathrm{kJ\,mol^{-1}}$, and the total $-13.2\,\mathrm{kJ\,mol^{-1}}$. Both terms drive $\ce{Na+}$ inward and are of similar size: the electrochemical gradient of $\ce{Na+}$ is a considerable store of free energy in the cell, about one quarter of the free energy of ATP hydrolysis (about $-50$ to $-60\,\mathrm{kJ\,mol^{-1}}$ in the cell). Most secondary active transport in animal cells is driven by this energy.

Setting Eq. (3.5) to zero gives the membrane potential at which an ion is at equilibrium; the difference between this potential and the actual membrane potential is the net electrochemical driving force on that ion. These are the subject of the next chapter.

### 3.4.2. Primary Active Transport

**Definition 3.4.1 (Primary Active Transport)** Transport in which the transport protein is itself an ATPase and uses the energy of ATP hydrolysis directly to move substances against the electrochemical gradient is called **primary active transport**; such transport proteins are called pumps.

The most important is the **Na⁺/K⁺-ATPase** (the sodium–potassium pump, a **P-type ATPase**): for each ATP hydrolyzed it pumps 3 $\ce{Na+}$ out of the cell and 2 $\ce{K+}$ into it, and each pump cycles about 100 times per second. It maintains the state of low intracellular $\ce{Na+}$ and high $\ce{K+}$ and is the ultimate source of all $\ce{Na+}$ gradients in epithelial cells, neurons and muscle cells; at rest about $20\%$–$30\%$ of a person's energy (about half in the brain) is spent on this pump. Because each cycle removes one net positive charge, it is **electrogenic** and directly makes the membrane potential a few millivolts more negative (Chapter 4). Cardiac glycosides (ouabain, digoxin) inhibit it specifically.

Other important pumps:

- $\ce{Ca^2+}$ pumps: PMCA of the plasma membrane (1 $\ce{Ca^2+}$ pumped out per ATP) and SERCA of the **endoplasmic reticulum** and **sarcoplasmic reticulum** (2 $\ce{Ca^2+}$ pumped in per ATP), which keep the cytosolic $[\ce{Ca^2+}]$ at about $100\,\mathrm{nmol\,L^{-1}}$, about ten thousand times lower than outside.
- $\ce{H+}$ pumps: the $\ce{H+}$/$\ce{K+}$-ATPase of gastric parietal cells (P-type) acidifies gastric juice to pH about 1 ([7.3.5](/7.3.5), Chapter 27); V-type $\ce{H+}$-ATPases acidify **lysosomes** and secretory vesicles and secrete $\ce{H+}$ out of the cell in **intercalated cells** of the renal collecting duct and in **osteoclasts**.
- **ABC transporters**: pump drugs, bile acids and lipids out of cells (as in bile secretion by hepatocytes, Chapter 29).

### 3.4.3. Secondary Active Transport

**Secondary active transport** uses an ion gradient established by primary active transport (usually the $\ce{Na+}$ gradient) to transport another substance against its gradient. By analogy, primary active transport is like a water pump that uses electricity to lift water to a height, and secondary active transport like a hydroelectric station in which water flowing down from the height drives a turbine. A transporter that moves two substances in the same direction is called a **symporter** (such as the $\ce{Na+}$–glucose cotransporter SGLT and the $\ce{Na+}$–$\ce{K+}$–$2\ce{Cl-}$ cotransporter NKCC), and one that moves them in opposite directions an **antiporter** (such as the $\ce{Na+}$/$\ce{Ca^2+}$ exchanger NCX and the $\ce{Na+}$/$\ce{H+}$ exchanger NHE).

By what factor can coupled transport concentrate a substrate? At the equilibrium point of the transporter, the free energy released by the influx of $n$ $\ce{Na+}$ is exactly equal to the free energy needed for the influx of one glucose against its gradient:
$$
RT\ln\frac{[\mathrm{G}]_{\mathrm{i}}}{[\mathrm{G}]_{\mathrm{o}}} + n\left(RT\ln\frac{[\ce{Na+}]_{\mathrm{i}}}{[\ce{Na+}]_{\mathrm{o}}} + FV_{\mathrm{m}}\right) = 0,
$$
that is,
$$
\frac{[\mathrm{G}]_{\mathrm{i}}}{[\mathrm{G}]_{\mathrm{o}}} = \left(\frac{[\ce{Na+}]_{\mathrm{o}}}{[\ce{Na+}]_{\mathrm{i}}}\right)^n\mathrm{e}^{-nFV_{\mathrm{m}}/RT} = \left(\frac{[\ce{Na+}]_{\mathrm{o}}}{[\ce{Na+}]_{\mathrm{i}}}\cdot 10^{-V_{\mathrm{m}}/60\,\mathrm{mV}}\right)^n, \tag{3.6}
$$
where in the last step $RT\ln 10/F \approx 60\,\mathrm{mV}$ (at about $30\,{}^\circ\mathrm{C}$; $61.5\,\mathrm{mV}$ at $37\,{}^\circ\mathrm{C}$).

**Example 3.4.2 (SGLT2 and SGLT1)** SGLT2 (and SGLT3) transport 1 $\ce{Na+}$ : 1 glucose. Taking extracellular $[\ce{Na+}]$ as about 10 times intracellular and $V_{\mathrm{m}} = -60\,\mathrm{mV}$, Eq. (3.6) gives $[\mathrm{G}]_{\mathrm{i}}/[\mathrm{G}]_{\mathrm{o}} = 10 \times 10 = 100$: the chemical gradient and the electrical gradient each contribute a factor of 10. SGLT1 transports 2 $\ce{Na+}$ : 1 glucose and under the same conditions gives $100^2 = 10^4$; calculated at $37\,{}^\circ\mathrm{C}$ with $[\ce{Na+}]_{\mathrm{o}}/[\ce{Na+}]_{\mathrm{i}} = 145/12$ the values are about $1.1\times10^2$ and $1.3\times10^4$, respectively. The cost is that each glucose consumes twice as much $\ce{Na+}$, that is, twice the work by the Na⁺/K⁺-ATPase (one ATP per 3 $\ce{Na+}$).

The two stoichiometries match their distributions. In the initial segments of the renal proximal tubule (S1 and S2) the glucose concentration in the filtrate is high, and SGLT2, with high capacity and low affinity, reabsorbs about $90\%$ of the filtered glucose; the 1:1 stoichiometry is more "economical"; the late proximal tubule (S3) and the small-intestinal brush border face a low glucose concentration and must recover nearly all of it from very low concentrations, and the 2:1 stoichiometry of SGLT1 provides sufficient concentrating power (Chapters 23 and 28). SGLT2 inhibitors (the gliflozins) cause large amounts of glucose to be excreted in the urine; they are used to treat **type 2 diabetes** and also reduce the risk of heart failure and chronic kidney disease.

**Example 3.4.3 (How Low Can NCX Keep Cytosolic $\ce{Ca^2+}$?)** Each cycle of NCX brings in 3 $\ce{Na+}$ and takes out 1 $\ce{Ca^2+}$, with net movement of one positive charge inward. At equilibrium
$$
RT\ln\frac{[\ce{Ca^2+}]_{\mathrm{o}}}{[\ce{Ca^2+}]_{\mathrm{i}}} - 2FV_{\mathrm{m}} = 3\left(RT\ln\frac{[\ce{Na+}]_{\mathrm{o}}}{[\ce{Na+}]_{\mathrm{i}}} - FV_{\mathrm{m}}\right),
$$
that is,
$$
\frac{[\ce{Ca^2+}]_{\mathrm{o}}}{[\ce{Ca^2+}]_{\mathrm{i}}} = \left(\frac{[\ce{Na+}]_{\mathrm{o}}}{[\ce{Na+}]_{\mathrm{i}}}\right)^3\mathrm{e}^{-FV_{\mathrm{m}}/RT}.
$$
Taking $[\ce{Na+}]_{\mathrm{o}}/[\ce{Na+}]_{\mathrm{i}} = 10$ and $V_{\mathrm{m}} = -60\,\mathrm{mV}$: $10^3 \times 10 = 10^4$. The extracellular $[\ce{Ca^2+}]$ is about $1$–$1.2\,\mathrm{mmol\,L^{-1}}$, so NCX can lower the cytosolic $[\ce{Ca^2+}]$ at most to about $100\,\mathrm{nmol\,L^{-1}}$, exactly the measured resting value. Calculated with $145/12$ and $37\,{}^\circ\mathrm{C}$, the lower limit is about $70\,\mathrm{nmol\,L^{-1}}$ at $-60\,\mathrm{mV}$ and about $30\,\mathrm{nmol\,L^{-1}}$ at $-85\,\mathrm{mV}$. NCX is thus near equilibrium at rest, and its direction is sensitive to both membrane potential and $[\ce{Na+}]_{\mathrm{i}}$: during the plateau of the cardiac **action potential** the membrane potential is positive and NCX temporarily reverses, letting $\ce{Ca^2+}$ in; cardiac glycosides inhibit the Na⁺/K⁺-ATPase and slightly raise $[\ce{Na+}]_{\mathrm{i}}$, so NCX extrudes less $\ce{Ca^2+}$, the $\ce{Ca^2+}$ stored in the sarcoplasmic reticulum increases and the force of cardiac contraction increases, which is the mechanism by which digitalis drugs treat heart failure (Chapter 13).

![Limits of Na⁺-coupled transport (37 °C, [Na⁺]ₒ/[Na⁺]ᵢ = 145/12). A: the maximal intracellular-to-extracellular glucose ratio that Na⁺–glucose cotransport can reach as a function of membrane potential (Eq. 3.6), for 1:1 (SGLT2) and 2:1 (SGLT1); about 10² and 10⁴ at −60 mV. B: cytosolic [Ca²⁺] at equilibrium of the 3 Na⁺ : 1 Ca²⁺ Na⁺/Ca²⁺ exchanger ([Ca²⁺]ₒ = 1.2 mM). When cytosolic [Ca²⁺] is above this line the exchanger extrudes Ca²⁺ (forward mode), below it transport reverses; at the resting potential the equilibrium value is close to 100 nM, and when the membrane potential rises above about −50 mV, a cytosolic Ca²⁺ of 100 nM makes the exchanger reverse](./plots/sglt-ratio.py)

## 3.5. Comparison of Transport Proteins

| Property | Pores | Channels | Carriers | Pumps |
|---|---|---|---|---|
| Open to both sides at once | Always | When open | Never (alternating access) | Never |
| Gating | None | Voltage, ligand, mechanical, temperature | Conformational cycle | ATP-driven conformational cycle |
| Rate per protein ($\mathrm{s^{-1}}$) | Water channel about $10^9$ | $10^6$–$10^8$ ions | $10^2$–$10^4$ | $10^1$–$10^3$ |
| Saturation | Very weak | Very weak | Yes, on the scale of $K_{\mathrm{d}}$ | Yes |
| Energy | Down the gradient | Down the gradient | Down the gradient (uniport) or coupled | ATP |
| Examples | Aquaporins, porins | $\mathrm{Na_V}$, $\mathrm{K_V}$, nAChR | GLUT, SGLT, NCX | Na⁺/K⁺-ATPase, SERCA, $\ce{H+}$/$\ce{K+}$-ATPase |

Channels and carriers differ in rate by about ten thousand times, which determines their division of labor: channels are suited to changing the membrane potential rapidly and briefly (tens of millions of ions per second), carriers and pumps to continuous movement of substrates and maintenance of gradients. The same substance can have several pathways, and by combining the types, numbers, polarized distribution, modification and regulation of transport proteins the cell obtains great plasticity in the transport of substances.

## 3.6. Movement of Water and Cell Volume

### 3.6.1. Water Transport Is Passive

A small amount of water can cross the lipid bilayer directly (the water molecule is electrically neutral and small, with a partition coefficient much larger than that of ions), at a rate related to the fluidity of the membrane lipids; but in most cell membranes water moves mainly through **aquaporins**. Some water channels are permanently in the plasma membrane (AQP1 of red cells and the proximal tubule), others are inserted into it in a regulated way: **antidiuretic hormone** moves AQP2 from vesicles to the apical membrane of collecting duct **principal cells** and concentrates the urine (Chapter 24). The discovery of aquaporins (Agre, 1992) explained the very high water permeability of red cells and renal tubules.

### 3.6.2. Osmolarity and Osmotic Pressure

The movement of water across a **semipermeable membrane** driven by a difference in water concentration between the two sides is called **osmosis**; the pressure needed to prevent net movement of water is called **osmotic pressure**. Osmotic pressure depends only on the number of solute particles in the solution, not on their kind or size.

The number of solute particles is measured in osmoles (Osm): $1\,\mathrm{Osm}$ is $1\,\mathrm{mol}$ of solute particles. $180\,\mathrm{g}$ of glucose dissolved is $1\,\mathrm{Osm}$; $58.5\,\mathrm{g}$ of NaCl dissociates into $\ce{Na+}$ and $\ce{Cl-}$ and ideally is $2\,\mathrm{Osm}$. In real solutions, ion interactions reduce the effective number of particles, corrected by the **osmotic coefficient** $\phi$: for NaCl at physiological concentration $\phi \approx 0.93$, giving $2 \times 0.93 = 1.86\,\mathrm{Osm}$ (often neglected in everyday calculation). The number of osmoles per unit volume of solution is the **osmolarity** ($\mathrm{Osm\,L^{-1}}$; per kilogram of water it is called osmolality, $\mathrm{Osm\,kg^{-1}}$, and in dilute solutions the two are almost equal).

By the van 't Hoff equation, the osmotic pressure is $\pi = \phi RTc$. At $37\,{}^\circ\mathrm{C}$, $RT = 2.58\times10^6\,\mathrm{Pa\,L\,Osm^{-1}}$, so
$$
1\,\mathrm{Osm\,L^{-1}} \approx 2.58\,\mathrm{MPa} \approx 19\,300\,\mathrm{mmHg}, \qquad 1\,\mathrm{mOsm\,L^{-1}} \approx 19.3\,\mathrm{mmHg}\ (2.58\,\mathrm{kPa}). \tag{3.7}
$$

**Example 3.6.1** $5.85\,\mathrm{g}$ of NaCl made up to $1\,\mathrm{L}$: $0.1\,\mathrm{mol}$ NaCl, $0.2\,\mathrm{Osm}$, osmotic pressure about $0.2 \times 19\,300 = 3860\,\mathrm{mmHg}$ (about $515\,\mathrm{kPa}$; $3590\,\mathrm{mmHg}$ with $\phi = 0.93$). The osmolarity of plasma is about $290\,\mathrm{mOsm\,L^{-1}}$ and its osmotic pressure about $5600\,\mathrm{mmHg}$ (about $0.75\,\mathrm{MPa}$, more than 7 atmospheres).

Plasma, interstitial fluid and intracellular fluid have the same osmolarity (about $290\,\mathrm{mOsm\,kg^{-1}}$), but from different sources: that of the extracellular fluid comes mainly from $\ce{Na+}$, $\ce{Cl-}$ and $\ce{HCO3-}$, that of the intracellular fluid mainly from $\ce{K+}$ and organic phosphates, proteins and their counterions.

**Definition 3.6.1 (Crystalloid Osmotic Pressure)** The osmotic pressure formed by crystalloid substances (electrolytes and small molecules such as glucose and urea) is called **crystalloid osmotic pressure** and makes up the great majority of plasma osmotic pressure.

Small solutes pass freely through the capillary wall and there is no concentration difference between plasma and interstitial fluid, so crystalloid osmotic pressure determines the distribution of water between the inside and outside of cells, not between the inside and outside of vessels. The **colloid osmotic pressure** formed by plasma proteins (mainly albumin) is only about $25\,\mathrm{mmHg}$ ($3.3\,\mathrm{kPa}$), less than $0.5\%$ of the total osmotic pressure, but proteins do not readily cross the capillary wall, so it determines the distribution of water between the inside and outside of vessels (Chapters 11 and 15).

### 3.6.3. Driving Force for Water

The movement of water is driven by the difference in the **chemical potential** of water. The change in chemical potential per mole of water moved from inside to outside the cell is approximately
$$
\Delta\mu_{\ce{H2O}} \approx -\bar V_{\mathrm{w}}\left[RT(\mathrm{Osm_o} - \mathrm{Osm_i}) + (P_{\mathrm{i}} - P_{\mathrm{o}})\right], \tag{3.8}
$$
where $\bar V_{\mathrm{w}}$ is the **partial molar volume** of water (about $18\,\mathrm{cm^3\,mol^{-1}}$) and the bracket is the force driving water outward, in units of pressure: the osmotic pressure difference plus the hydrostatic pressure difference (when the bracket is positive, $\Delta\mu_{\ce{H2O}} < 0$ and water flows out spontaneously). "Concentration of water" is not an intuitive quantity, whereas osmotic pressure is more intuitive and easy to measure, so physiology customarily describes the driving force on water by osmotic pressure. The membrane of an animal cell is soft and deformable and cannot bear a significant hydrostatic pressure difference, $P_{\mathrm{i}} - P_{\mathrm{o}} \approx 0$, so the movement of water is driven only by the osmotic pressure difference: water always flows from the side of lower osmolarity (higher water concentration) to the side of higher osmolarity; when extracellular osmolarity is high water leaves the cell and the cell shrinks, when intracellular osmolarity is high water enters and the cell swells, until the osmolarities on the two sides are equal. Plant cells have a **cell wall** that bears **turgor pressure**, and the second term of Eq. (3.8) cannot be neglected ([7.13.2](/7.13.2)). Across the capillary wall, the hydrostatic pressure difference and the colloid osmotic pressure difference together determine filtration (**Starling forces**, Chapter 15).

### 3.6.4. Isosmotic and Isotonic

**Definition 3.6.2 (Isosmotic and Isotonic Solutions)** A solution with the same osmolarity as plasma is called an **isosmotic solution**; a solution that causes red cells (or other cells) neither to swell nor to shrink, so that they keep their normal volume, is called an **isotonic solution**.

The two are not necessarily the same, the difference being whether the solute can enter the cell. In $0.9\%$ NaCl (physiological saline, $154\,\mathrm{mmol\,L^{-1}}$, about $286\,\mathrm{mOsm\,L^{-1}}$), $\ce{Na+}$ is continually pumped out by the Na⁺/K⁺-ATPase and $\ce{Cl-}$ distributes accordingly, so NaCl effectively cannot enter the cell and the solution is both isosmotic and isotonic. A $1.9\%$ urea solution (about $300\,\mathrm{mmol\,L^{-1}}$) is isosmotic, but urea crosses the cell membrane quickly and, after entering, raises the intracellular osmolarity, water follows, and red cells swell and even lyse, so it is hypotonic. $5\%$ glucose (about $278\,\mathrm{mmol\,L^{-1}}$) is isosmotic when infused, but after the cells take up and metabolize the glucose what remains is water, so physiologically it is equivalent to infusing a hypotonic solution. How "effective" a solute is can be described by the **reflection coefficient** $\sigma$ ($\sigma = 1$ means completely impermeant, $0$ means as free as water); the effective osmotic pressure is $\sigma RT\Delta c$, and tonicity is determined by the effective osmotic pressure.

### 3.6.5. Ions and Water Together Regulate Cell Volume

Cell volume is the joint result of ion transport and the movement of water. The cell contains a large number of negatively charged macromolecules that cannot cross the membrane (proteins, nucleic acids, organic phosphates), which attract diffusible cations; according to the **Donnan equilibrium**, the total numbers of diffusible ions on the two sides of the membrane are unequal at equilibrium, the intracellular osmolarity is higher, water would enter continually, and the cell would swell without limit. Animal cells have no cell wall and counteract this tendency with the Na⁺/K⁺-ATPase: by pumping $\ce{Na+}$ out, the pump makes $\ce{Na+}$ in effect an extracellular solute that "cannot enter", osmotically balancing the intracellular macromolecules (the **pump–leak model**, [7.3.5](/7.3.5)).

Therefore, when the Na⁺/K⁺-ATPase is inhibited (ouabain, hypoxia, cold), $\ce{Na+}$ leaks in down its gradient and $\ce{Cl-}$ follows to maintain electroneutrality ($\ce{K+}$ efflux is slower); for every pair of $\ce{Na+}$ and $\ce{Cl-}$ that enters, the intracellular osmolarity rises, water flows in and the cell swells. This is one cause of cell edema in ischemia (such as brain edema). Cells also have dedicated volume-regulatory mechanisms: on swelling they open $\ce{K+}$ and $\ce{Cl-}$ channels and expel ions and organic osmolytes (**regulatory volume decrease**), on shrinking they activate NKCC and NHE to take up ions (**regulatory volume increase**).

## 3.7. Ions and Water Together Accomplish Transepithelial Absorption

Epithelial cells use **tight junctions** to divide the cell membrane into two domains, the apical membrane (facing the intestinal or tubular lumen) and the basolateral membrane (facing interstitial fluid and blood), with different transport proteins on the two sides, so that the transport of single cells is combined into directional **transepithelial transport**.

Take the absorption of $\ce{Na+}$, glucose and water by the small intestine and proximal tubule as an example:

1. The Na⁺/K⁺-ATPase of the basolateral membrane pumps $\ce{Na+}$ out of the cell, keeping intracellular $[\ce{Na+}]$ low and the membrane potential negative and establishing an electrochemical gradient for $\ce{Na+}$ from lumen to cell; this is the only step in the whole process that consumes ATP directly, and absorption is an energy-consuming process.
2. SGLT1 in the apical membrane uses this gradient to transport $\ce{Na+}$ and glucose into the cell together, and glucose accumulates inside the cell to a concentration above that in plasma.
3. Glucose leaves the cell down its concentration gradient into the interstitial fluid through GLUT2 of the basolateral membrane; $\ce{Cl-}$ follows $\ce{Na+}$ by the **paracellular pathway** or the **transcellular pathway** to maintain electroneutrality.
4. Solute accumulates in the intercellular spaces and on the basal side, making the local osmolarity slightly higher, and water follows passively through aquaporins and tight junctions (osmosis), so that in the end the fluid is absorbed isosmotically.

This mechanism has direct clinical significance: cholera toxin makes the intestinal epithelium secrete large amounts of $\ce{Cl-}$ and water but does not damage SGLT1; oral rehydration salts combine glucose and NaCl in a definite proportion and use the coupled absorption by SGLT1 to "pull" $\ce{Na+}$ and water back into the body, one of the medical advances that saved the most lives in the twentieth century. The various epithelial transports in the chapters on the urinary and digestive systems (Chapters 23 and 28) are all different combinations of the same set of components (pumps, channels, coupled transporters, tight junctions).

## 3.8. Evolution and Comparison

### 3.8.1. $\ce{Na+}$-Driven and $\ce{H+}$-Driven Secondary Transport

Animal cells use the $\ce{Na+}$ gradient as the main "currency" of secondary transport, and the Na⁺/K⁺-ATPase is a major feature of animals (and their unicellular relatives), found only sporadically in other eukaryotes. Bacteria, fungi and plants use mainly the $\ce{H+}$ gradient (the **proton-motive force**), established by the plasma-membrane $\ce{H+}$-ATPase or the **respiratory chain**; the uptake of sugars, nitrate and ions in plants is mostly $\ce{H+}$-coupled ([7.13](/7.13)). Some marine bacteria in $\ce{Na+}$-rich environments also use $\ce{Na+}$-driven respiratory chains and flagellar motors.

There are exceptions among animals, the most typical being the midgut of lepidopteran larvae. The V-type $\ce{H+}$-ATPase in the apical membrane of its goblet cells pumps $\ce{H+}$ into the lumen, and an electrogenic $\ce{K+}$/$2\ce{H+}$ antiporter then exchanges $\ce{K+}$ into the lumen, with the result that the lumen is high in $\ce{K+}$ and strongly alkaline (pH up to 10–12), with a transepithelial potential of more than $100\,\mathrm{mV}$; the absorption of amino acids is carried out by $\ce{K+}$-coupled symporters. This system is adapted to plant-feeding larvae: plant tissue is rich in $\ce{K+}$ and poor in $\ce{Na+}$, and using $\ce{K+}$ instead of $\ce{Na+}$ as the driving ion saves scarce $\ce{Na+}$. The Malpighian tubules of insects and many epithelia also use the V-type $\ce{H+}$-ATPase as the primary driving pump.

The problem of freshwater animals is to take up $\ce{Na+}$ from a very dilute environment ($[\ce{Na+}]$ often below $1\,\mathrm{mmol\,L^{-1}}$), where the chemical gradient of $\ce{Na+}$ points outward. In frog skin and in some cells of the freshwater fish gill, the apical V-type $\ce{H+}$-ATPase pumps out $\ce{H+}$ and makes the potential just inside the apical membrane very negative, so that $\ce{Na+}$ is "sucked" into the cell through $\ce{Na+}$ channels against its concentration gradient and then sent into the blood by the basolateral Na⁺/K⁺-ATPase. This is an example of the potential produced by one pump driving the absorption of another ion; the whole of osmoregulation is treated in Chapter 21.

### 3.8.2. The Aquaporin Family

Aquaporins belong to the ancient MIP family and are found in bacteria, archaea, plants and animals. They fall into two main branches: the classical aquaporins that pass only water, and the aquaglyceroporins that also pass small molecules such as glycerol and urea. Mammals have 13 (AQP0–AQP12), with different distributions and functions: AQP1 is in red cells, the proximal tubule and capillary endothelium, AQP2 is regulated by antidiuretic hormone, AQP3 and AQP7 transport glycerol, AQP4 is in the end-feet of brain astrocytes (related to brain edema), and AQP5 is in salivary glands, lacrimal glands and alveolar epithelium. Plants have several dozen aquaporins ([7.13.2](/7.13.2)), suited to a way of life in which water is the main transport medium; insects also have dedicated water channels (such as Drip in the Malpighian tubule), which let them excrete the large amounts of water in a blood meal quickly. **Euryhaline** fishes adjust the expression of aquaporins in the gill and intestine when moving from seawater to fresh water, showing that regulation of water channels is a component of **osmoregulation**.

## Summary

| Topic | Relations and values |
|---|---|
| Simple diffusion (Definition 3.2.1) | $\mathrm{d}n/\mathrm{d}t = PA\Delta C$ (Eq. 3.1), $P = KD/\Delta x$ (Eq. 3.2); lipid solubility determines the rate |
| Pores and channels | Pores are continuously open, selectivity by pore size; channels have selectivity (pore size and charge, $\ce{K+}$:$\ce{Na+}$ about 1000:1) and gating; $P_{\mathrm{o}} = 1/(1 + \mathrm{e}^{\Delta G/k_{\mathrm{B}}T})$ (Eq. 3.3); conductance $= NP_{\mathrm{o}}\gamma$ |
| Carriers | $J = k_3R_0A/(A + K_{\mathrm{d}})$ (Eq. 3.4): saturation, specificity, competition; regulate $R_0$ (GLUT4), $K_{\mathrm{d}}$ (GLUT1 and GLUT2) |
| Electrochemical potential | $\Delta\tilde\mu = RT\ln([\mathrm{X}]_{\mathrm{i}}/[\mathrm{X}]_{\mathrm{o}}) + zFV_{\mathrm{m}}$ (Eq. 3.5); $\ce{Na+}$ influx about $-13\,\mathrm{kJ\,mol^{-1}}$ (Example 3.4.1) |
| Primary active transport (Definition 3.4.1) | Na⁺/K⁺-ATPase 3 $\ce{Na+}$ out, 2 $\ce{K+}$ in, electrogenic, $20\%$–$30\%$ of resting energy use; PMCA, SERCA; $\ce{H+}$/$\ce{K+}$-ATPase, V-type $\ce{H+}$-ATPase |
| Secondary active transport | Concentration ratio $([\ce{Na+}]_{\mathrm{o}}/[\ce{Na+}]_{\mathrm{i}}\cdot10^{-V_{\mathrm{m}}/60\,\mathrm{mV}})^n$ (Eq. 3.6): SGLT2 about $10^2$, SGLT1 about $10^4$ (Example 3.4.2); NCX sets a lower limit of cytosolic $\ce{Ca^2+}$ of about $100\,\mathrm{nmol\,L^{-1}}$ and can reverse (Example 3.4.3) |
| Rates | Water channel $10^9$, ion channel $10^6$–$10^8$, carrier $10^2$–$10^4$, pump $10^1$–$10^3\,\mathrm{s^{-1}}$ |
| Osmosis | $1\,\mathrm{mOsm\,L^{-1}} \approx 19.3\,\mathrm{mmHg}$ (Eq. 3.7); plasma about $290\,\mathrm{mOsm\,L^{-1}}$, $5600\,\mathrm{mmHg}$; crystalloid osmotic pressure (Definition 3.6.1) sets the distribution inside versus outside cells, colloid osmotic pressure (about $25\,\mathrm{mmHg}$) inside versus outside vessels |
| Driving force for water | $\bar V_{\mathrm{w}}[RT\Delta\mathrm{Osm} + \Delta P]$ (Eq. 3.8); animal cells $\Delta P \approx 0$, water flows toward higher osmolarity |
| Isosmotic and isotonic (Definition 3.6.2) | Physiological saline is isosmotic and isotonic; urea solution is isosmotic and hypotonic; effective osmotic pressure $\sigma RT\Delta c$ |
| Cell volume and epithelia | Pump inhibited → $\ce{Na+}$, $\ce{Cl-}$ enter → swelling; transepithelial absorption: basolateral pump + apical coupled transport + passive following of water |
| Evolution | Animals use $\ce{Na+}$, bacteria, fungi and plants use $\ce{H+}$; the V-ATPase–$\ce{K+}$ system of the lepidopteran midgut; $\ce{H+}$ pump driving $\ce{Na+}$ uptake in freshwater epithelia; aquaporins and aquaglyceroporins |

## Questions

1. Why do $\ce{O2}$ and $\ce{CO2}$ not need transport proteins, whereas water and $\ce{K+}$ do? If an anesthetic makes the membrane lipids more "fluid", which class of substances has its transmembrane rate affected most?

   **Answer** By Eq. (3.2) the permeability coefficient is dominated by the partition coefficient. $\ce{O2}$ and $\ce{CO2}$ are nonpolar and dissolve readily in the hydrocarbon core of the membrane, so $P$ is large; ions are charged and surrounded by hydration shells, entering the low-dielectric hydrocarbon core costs a great deal of free energy, and $P$ is smaller by more than ten orders of magnitude; water, although small and neutral, is strongly polar, and its rate across the lipid bilayer is still insufficient for the needs of red cells, renal tubules and so on. Membrane fluidity mainly affects simple diffusion across the lipid bilayer (especially of water and small polar molecules) and affects channel- and carrier-mediated transport less (though it can change the conformation and gating of membrane proteins indirectly).

2. Calculate the maximal intracellular-to-extracellular glucose ratio that SGLT1 can maintain at $37\,{}^\circ\mathrm{C}$, $[\ce{Na+}]_{\mathrm{o}} = 145$, $[\ce{Na+}]_{\mathrm{i}} = 15\,\mathrm{mmol\,L^{-1}}$ and $V_{\mathrm{m}} = -50\,\mathrm{mV}$. If small-intestinal epithelial cells are partly depolarized to $-30\,\mathrm{mV}$ by hypoxia, what does the ratio fall to?

   **Answer** The factor for each $\ce{Na+}$ is $(145/15)\times10^{50/61.5} = 9.67 \times 6.5 = 62.8$, and its square is about $3.9\times10^3$. At $-30\,\mathrm{mV}$ it is $9.67\times10^{30/61.5} = 9.67\times3.07 = 29.7$, whose square is about $880$. If hypoxia also raises $[\ce{Na+}]_{\mathrm{i}}$, the ratio falls further; this shows that secondary active transport depends on the electrochemical gradient established by primary active transport.

3. A transporter has $K_{\mathrm{d}} = 2\,\mathrm{mmol\,L^{-1}}$. By what factor does the transport rate increase when the substrate concentration rises from $1$ to $10\,\mathrm{mmol\,L^{-1}}$? What if the transport were simple diffusion?

   **Answer** Carrier: $J(1) \propto 1/3 = 0.333$ and $J(10) \propto 10/12 = 0.833$, an increase of only 2.5-fold. Simple diffusion is proportional to concentration and increases 10-fold. Saturation makes carrier transport insensitive to concentration at high concentrations.

4. Is each of the following solutions hypotonic, isotonic or hypertonic to human red cells? (a) $0.9\%$ NaCl; (b) $0.45\%$ NaCl; (c) $300\,\mathrm{mmol\,L^{-1}}$ urea; (d) $150\,\mathrm{mmol\,L^{-1}}$ NaCl plus $100\,\mathrm{mmol\,L^{-1}}$ urea.

   **Answer** (a) Isosmotic and isotonic. (b) About $143\,\mathrm{mOsm\,L^{-1}}$, hyposmotic and hypotonic; red cells swell. (c) Isosmotic but hypotonic: urea enters the cells until its concentrations inside and outside are equal, equivalent to the cells being in water with no effective solute, and they swell and lyse. (d) The total osmolarity is about $380\,\mathrm{mOsm\,L^{-1}}$, hyperosmotic; but urea is permeant and the only effective solute is NaCl (about $280$), so the solution is in the end nearly isotonic: the cells first shrink slightly and recover their original volume as urea enters.

5. Why do cells swell after the Na⁺/K⁺-ATPase is inhibited with ouabain? Why do the swelling (and the loss of the ion gradients) take tens of minutes or more, much longer than the change in membrane potential?

   **Answer** After the pump stops, $\ce{Na+}$ leaks in down its electrochemical gradient and $\ce{Cl-}$ follows to maintain electroneutrality (because of the **depolarization** of the membrane, the driving force on $\ce{Cl-}$ also becomes favorable for influx), the number of intracellular solute particles increases and water enters; the impermeant intracellular macromolecules continually attract ions and water according to the Donnan equilibrium. The leak flux is small (the permeability to $\ce{Na+}$ at rest is low) while the ion pools inside and outside the cell are large (tens to over a hundred millimoles per liter), so changes in ion concentrations and the resulting change in volume take tens of minutes to hours; the membrane potential, in contrast, can be changed by the movement of very few ions (Chapter 4), so the electrical changes precede the volume change.

6. (Open question) In the formula of oral rehydration salts, why is the ratio of glucose to $\ce{Na+}$ roughly 1:1, and why is the total osmolarity slightly below that of plasma?

   **Answer** Key points: SGLT1 couples 2 $\ce{Na+}$ : 1 glucose, and there are other pathways of $\ce{Na+}$ absorption in the intestinal lumen; an equimolar ratio of glucose and $\ce{Na+}$ lets both be fully used, and too much glucose would remain in the lumen and cause osmotic diarrhea; a solution slightly below plasma osmolarity (the current WHO reduced-osmolarity formula is about $245\,\mathrm{mOsm\,L^{-1}}$) makes it easier for water to follow the solutes into the body rather than being drawn osmotically into the lumen. This is a direct application of the principle of "ions and water absorbed together" (Section 3.7).
