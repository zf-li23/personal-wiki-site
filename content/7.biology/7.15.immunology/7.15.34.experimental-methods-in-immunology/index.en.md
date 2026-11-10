---
title: Experimental Methods in Immunology
description: The common logic of immunological techniques (specific recognition, signal amplification, readout); production and characterization of antibodies; precipitation and agglutination (a network model of the precipitin curve); ELISA and the four-parameter logistic standard curve; affinity measurement (SPR, isothermal titration calorimetry); immunohistochemistry and imaging; spectral spillover and compensation in flow cytometry; mass cytometry; assays of proliferation, killing, apoptosis and pMHC tetramers; single-cell omics and genetic engineering; interpreting test results and predictive values.
source_hash: d7ed86d119bf
---

Almost every experimental method in immunology rests on one fact: an antibody (or receptor) can bind one molecule with very high specificity. Turn this binding event into a readable signal (a clump of precipitate, a color, a spot of light, a fluorescence intensity, an ion count) and you have a technique. This chapter is the "methodology" outside the knowledge pathway: the knowledge of the earlier chapters (cell types, receptors, kinetic data) all came from these experiments, and in reading papers and interpreting test results one must know how a number was measured and what artifacts may be present. The chapter therefore presents only principles, readouts and their interpretation, not protocols or reagent recipes. The order runs from the simplest in vitro reactions (precipitation, agglutination), through solid-phase assays, affinity measurement, imaging and flow cytometry, to assays of cell function, and finally single-cell omics and genetic engineering; for each class of technique we choose the mathematical model that best illustrates the readout logic and write it as a script: the network model of the precipitin curve, the four-parameter curve of ELISA, the kinetics of SPR, and fluorescence compensation in flow cytometry. How markers and "immunophenotypes" are read is in the next chapter, [7.15.35](/7.15.35); spatial omics and single-cell methodology were covered in [7.9.5](/7.9.5) and [7.9.6](/7.9.6), and here we discuss only their use in immunology.

## 34.1. The Common Logic of Techniques and an Overview

An immunological assay consists of three parts: recognition (specific binding of an antibody, receptor or ligand to the target molecule), amplification (turning one binding event into a detectable signal: enzymatic catalytic turnover, fluorophores, metal isotopes, agglutination into a visible clump) and readout (converting the signal into a concentration, frequency, position or function). Sensitivity is determined by amplification and specificity by recognition, while the reliability of results depends on controls: without negative controls (omission of the primary antibody, isotype control, knockout samples) and a standard curve, a signal is almost impossible to interpret.

| Question to answer | Technique | Readout | Key points of interpretation |
|---|---|---|---|
| How much of an antigen or antibody is in the sample | **ELISA**, agglutination, immunoprecipitation | Absorbance or titer, converted through a standard curve | Working range, hook effect, cross-reactivity |
| Size and relative amount of a protein | **Western blot** | Position and intensity of bands | Band position validates antibody specificity |
| Where an antigen is in a tissue or cell | Immunohistochemistry, immunofluorescence | Image | Localization must agree with the known distribution; controls |
| Which cells and how many | Flow cytometry, mass cytometry | Multiparameter intensity per cell | Compensation, gating, controls |
| What cells are doing | Assays of proliferation, killing, apoptosis and cytokine secretion | Dilution peaks, specific lysis, quadrants, spot counts | Definition and threshold of positivity |
| Who binds whom and how tightly | SPR, isothermal titration calorimetry, coimmunoprecipitation | $k_{\mathrm{on}}$, $k_{\mathrm{off}}$, $K_{\mathrm{D}}$ | The mode of immobilization affects the reading |
| What a gene does | Gene knockout, **CRISPR screen**, transgenesis | Phenotype | Differences between mouse and human |

In terms of detection limit these methods differ by more than six orders of magnitude: precipitation in solution requires $20$–$200\,\mu\mathrm{g/ml}$ of antibody, direct agglutination about $0.006$–$0.06\,\mu\mathrm{g/ml}$, radioimmunoassay and ELISA can reach $10^{-4}$–$10^{-2}\,\mu\mathrm{g/ml}$, and chemiluminescent ELISA is lower still. This is why precipitation is used today mainly for qualitative work and teaching, whereas clinical quantification mainly uses solid-phase immunoassays.

## 34.2. Production and Characterization of Antibodies

**Polyclonal antibodies** come from the serum of immunized animals and are a mixture of the products of many B cell clones against several epitopes of the antigen: broad coverage, insensitivity to denaturation or slight changes of the antigen, but batch-to-batch inconsistency and irrelevant antibodies. **Monoclonal antibodies** are produced by a single B cell clone and recognize a single epitope, with defined specificity and unlimited supply; the earliest approach fused B cells of an immunized animal with myeloma cells to make **hybridomas**: the myeloma cell supplies immortality and the B cell a single antibody specificity, and the genetic defect of myeloma cells in an enzyme of the salvage synthesis pathway is exploited so that only fused cells survive in selective culture (Köhler and Milstein, 1975). Recombinant antibodies are now used more: variable region genes are cloned from single B cells or phage display libraries and expressed as the required antibody type; therapeutic antibodies are further chimerized, humanized or made fully human ([7.15.9](/7.15.9), [7.15.33](/7.15.33)).

Characterizing an antibody means answering four questions: what it recognizes (epitope mapping, and whether it recognizes a linear epitope surviving denaturation or a conformational epitope); how specific it is (cross-reaction with related antigens, and whether signal persists in cells or tissue in which the target gene has been knocked out); how tightly it binds (affinity, §34.5); and what isotype it is (which determines the secondary antibody that can be used, and also Fc function). Variable antibody quality is an important source of irreproducible results, so current practice is to validate the antibody in each application ("antibody validation", see [7.15.35](/7.15.35)).

## 34.3. Precipitation and Agglutination

### 34.3.1. The Precipitation Reaction and the Precipitin Curve

**Definition 34.3.1 (Immunoprecipitation)** The reaction in which bivalent or multivalent antibody binds multivalent soluble antigen to form a cross-linked network too large to remain dissolved and comes out of solution, together with the method of precipitating and isolating a particular antigen using this principle (or with antibody immobilized on a solid support), is called **immunoprecipitation**.

Precipitation requires both antibody and antigen to be multivalent: a monovalent Fab can only bind antigen and cannot cross-link, and an antigen with only one epitope cannot be bridged by antibody. The quantitative precipitin curve of Heidelberger and Kendall is the classic result: with the amount of antibody fixed and antigen added stepwise, the precipitate first increases with antigen, reaches a peak and then falls, because in antigen excess all sites of each antigen molecule are occupied by different antibodies and can no longer bridge, and the network dissolves. The curve is thus divided into three zones: antibody excess (antigen sites fully occupied, much free antibody), equivalence (maximum precipitate) and antigen excess (less precipitate, free antigen in the supernatant). This also explains the hook effect and the prozone phenomenon: at high concentrations of antigen or antibody, precipitation and agglutination reactions weaken or even become negative, and the sample must be diluted and retested.

This curve can be written quantitatively with a network model. Take a bivalent antibody (2 sites) and an antigen of valence $v$, with site-binding equilibrium constant $K$, let $a$ and $g$ be the concentrations of free antibody and antigen sites, and $B$ the concentration of bound sites:

$$
B = K a g,\qquad a = 2[\mathrm{Ab}] - B,\quad g = v[\mathrm{Ag}] - B .
$$

The fractions of antibody sites and antigen sites occupied are $p_a = B/(2[\mathrm{Ab}])$ and $p_g = B/(v[\mathrm{Ag}])$. Starting from a bound site and moving along the bond: on reaching an antibody, its other site is bound with probability $p_a$, leading to another antigen, and each of the other $v-1$ sites of that antigen is bound with probability $p_g$, so the expected number of new branches per "generation" is $p_a p_g (v-1)$. When this number exceeds 1, the network can extend indefinitely, that is, a gel (precipitate) forms; this is the Flory–Stockmayer gelation condition:

$$
p_a\,p_g\,(v-1) > 1 .
$$

It has three clear consequences: for $v = 2$ the left-hand side does not exceed 1, so a bivalent antigen can form only chains and cannot precipitate; in antibody excess $p_g$ is close to 1 but $p_a$ is small, and in antigen excess the reverse, so in both cases the product is below the threshold; only when the occupied fractions of both kinds of site are high enough (the equivalence zone) does the network form.

**Example 34.3.1** Take an antibody concentration of $1\,\mu\mathrm{M}$ ($150\,\mathrm{kDa}$), an antigen of molecular weight $60\,\mathrm{kDa}$ and a site affinity $K = 10^8\,\mathrm{M^{-1}}$, and solve for the gelled fraction and the precipitated mass (figure). An antigen with $v = 6$ precipitates over a range of antigen-to-antibody molar ratio of about $0.07$–$1.7$, with a maximum precipitate of about $195\,\mu\mathrm{g/ml}$ at a ratio of about $0.9$; the window for $v=4$ is much narrower (about $0.17$–$1.5$); for $v=2$ there is no precipitate, consistent with the condition $p_a p_g(v-1)>1$. The shape of the curve is determined only by valence, site affinity and concentration. A real antibody–antigen system must also take into account non-independence of sites, steric hindrance of the antigen and flexibility of the antibody; the model gives qualitative behavior and orders of magnitude.

:::

![Network model of the precipitin curve (see Example 34.3.1). With $1\,\mu\mathrm{M}$ antibody fixed and antigen added: the precipitate first increases and then decreases, and neither the antibody-excess zone nor the antigen-excess zone can form a network; an antigen of valence $v=2$ does not precipitate, and the larger $v$ is, the wider the precipitation window](./plots/precipitin-curve.py)

Precipitation is also carried out in agar gel: in Ouchterlony double immunodiffusion, antigen and antibody are placed in adjacent wells and diffuse toward each other, forming a precipitation line where their concentrations are comparable; fusion of the lines of two antigen wells against the same antiserum indicates identical antigens, crossing with a "spur" indicates partial identity, and crossing without fusion indicates different antigens, so the method can judge identity and cross-reaction of antigens. Single radial immunodiffusion makes the area of the precipitation ring proportional to the amount of antigen and permits quantification. Another use of precipitation is isolation by **immunoprecipitation**: antibody (often attached to solid-phase beads, or captured with Fc-binding protein A or G) pulls the target protein and its binding partners out of a cell lysate together, which is then read out by Western blot; **co-immunoprecipitation** is used in this way to analyze protein complexes, for example this method was used in the earliest demonstrations that the TCR and BCR coreceptor complexes consist of several molecules.

### 34.3.2. Agglutination

**Definition 34.3.2 (Agglutination)** The reaction in which antibody binds several antigens on the surface of a particulate antigen (red blood cells, bacteria or antigen-coated particles) and cross-links the particles into visible clumps is called **agglutination**.

Agglutination is the same in principle as precipitation, except that the antigen is on a particle surface, so it is easier to observe and about three orders of magnitude more sensitive than precipitation (see §34.1). The quantitative approach is the titer: serum is serially diluted by doubling, and the reciprocal of the highest dilution still giving positive agglutination is the titer. Doubling dilutions make the reading an integer on a logarithmic scale, and a difference of 1 in $\log_2$ titer corresponds to a 2-fold difference in concentration, so a difference within one dilution is usually considered experimental error, and in diagnosis a titer in convalescent serum at least 4 times that of acute serum (a difference of two dilutions) is emphasized as indicating recent infection.

The main uses of agglutination are:

- Blood typing: mixing red cells with anti-A, anti-B (and anti-D) antibodies, agglutination indicates expression of the corresponding antigen; reverse typing uses known red cells to detect natural antibodies in the subject's serum (for **blood groups** and transfusion reactions see [7.15.27](/7.15.27)).
- Hemagglutination inhibition: the hemagglutinin (HA) of viruses such as influenza agglutinates red cells; if the patient's serum contains antibody against the HA of that virus, it prevents agglutination, so the highest dilution that inhibits reflects the antibody level, and this is the classic method for assessing the response to influenza vaccine and the correlate of protection ([7.15.33](/7.15.33)).
- Antiglobulin (Coombs) test: some antibodies (especially incomplete antibodies such as anti-Rh IgG) can bind red cells without causing agglutination, because IgG is too small to span the charge repulsion between red cells; after an anti-human immunoglobulin secondary antibody is added, it bridges the bound IgG and agglutinates the red cells. The direct test detects antibody already bound to red cells and is used to diagnose autoimmune hemolysis and hemolytic disease of the newborn; the indirect test detects whether the serum contains antibody that can bind red cells and is used for crossmatching before transfusion.
- Bacterial agglutination: detecting antibacterial antibody (as in the diagnosis of typhoid) and identifying bacteria.

## 34.4. Solid-Phase Immunoassays

Immobilizing antibody or antigen on a solid phase (microplate, beads, membrane) so that bound and unbound material are easily separated is the basis of modern immunoassay. In ELISA, enzyme-labeled antibody is used for detection on the solid phase, and one enzyme molecule can catalyze many substrate molecules to give a colored or luminescent product; this is the amplification. The four common formats depend on the relation between analyte and antibody:

| Format | Logic of the method | Requirements | Relation of signal to analyte |
|---|---|---|---|
| Direct | Antigen immobilized, detected directly by enzyme-labeled primary antibody | Less used; the primary antibody must be labeled for each antigen | Positive |
| Indirect | Antigen immobilized; after primary antibody binds, detected by enzyme-labeled secondary antibody (against the Fc of the primary) | The secondary antibody can be universal; more amplification | Positive; used to measure antibody |
| Sandwich | Immobilized capture antibody binds antigen, which is then detected by an enzyme-labeled detection antibody recognizing another epitope | The antigen needs at least two nonoverlapping epitopes; both antibodies must be specific | Positive; highest specificity, the first choice for measuring cytokines and proteins |
| Competitive | Antigen in the sample competes with labeled antigen for limited antibody sites | For small molecules with only one epitope | Negative: the more analyte, the lower the signal |

That the sandwich assay needs two epitopes is the same matter as the valence condition of precipitation: the analyte must have at least two sites that two antibodies can bind at the same time. The sandwich assay has one more feature, the high-dose hook effect: when antigen is extremely abundant, free antigen separately saturates the capture antibody and the detection antibody and no longer forms a "sandwich", so the signal falls and the reading is too low. Samples that may be very high must therefore be diluted and dilution linearity checked.

The standard curve is usually sigmoidal and is fitted with the four-parameter logistic (4PL) function:

$$
y = d + \frac{a - d}{1 + (x/c)^b},
$$

where $a$ is the signal at zero concentration, $d$ the saturating signal, $c$ the **half-maximal effective concentration**, often written EC50, and $b$ the slope (Hill coefficient). The inverse function $x = c\,\bigl[(a - d)/(y - d) - 1\bigr]^{1/b}$ converts the absorbance of a sample into a concentration. In interpretation, note that only concentration readings from the middle of the curve (roughly EC10 to EC90) have small error, since the two ends are flat and a small change in signal corresponds to a large change in concentration; the detection limit is often taken as the concentration corresponding to the blank mean plus 3 standard deviations; and the sample matrix must be validated by dilution linearity and spike recovery, otherwise the difference between the standard curve (in buffer) and the sample brings systematic error.

**Example 34.4.1** Simulate a set of 2-fold dilution standards ($1000$–$7.8\,\mathrm{pg/ml}$, each concentration in duplicate, true values $a = 0.05$, $d = 2.5$, $c = 80\,\mathrm{pg/ml}$, $b = 1.2$, with 5% multiplicative noise), and fit the 4PL by least squares on log concentration, giving $\hat a = 0.08$, $\hat b = 1.33$, $\hat c = 79\,\mathrm{pg/ml}$, $\hat d = 2.47$ (in agreement with the true values). An unknown sample with absorbance 1.0 reads out about $56\,\mathrm{pg/ml}$ from the inverse function; the working range corresponding to EC10–EC90 is about $15$–$410\,\mathrm{pg/ml}$, roughly 27-fold, which shows that the reliable range of a single standard curve is quite limited, and a sample concentration falling outside the two ends must be diluted again.

:::

![Principle of the sandwich ELISA and the four-parameter logistic standard curve (simulated data, see Example 34.4.1). A: the capture antibody is immobilized on the solid phase, binds antigen, and is sandwiched by an enzyme-labeled detection antibody against another epitope; the enzyme catalyzes color development from the substrate. B: 4PL fit (line) on a logarithmic axis with duplicate standards (points); the dashed lines show the concentration of an unknown sample read back from absorbance 1.0](./plots/elisa-4pl.py)

The **Western blot** first separates a protein mixture by molecular weight on a gel, transfers it to a membrane, and then detects with antibody: its advantage is that the position of the band at the same time validates the specificity of the antibody (it should appear at the expected molecular weight of the target protein); its drawback is that the protein has been denatured, so only linear epitopes can be recognized, and it is useless for antibodies that recognize only conformational epitopes.

**Definition 34.4.1 (ELISpot)** The method in which cells are cultured on a solid phase coated with capture antibody, the cytokine or antibody they secrete is captured around them and developed by an enzyme-labeled detection antibody as a spot, and single cells secreting that product are counted by the number of spots, is called **ELISpot** (enzyme-linked immunospot).

One spot corresponds to one secreting cell, so the result is "the number of IFN-γ-secreting cells per million cells" and not a concentration in the supernatant; the sensitivity can reach a cell frequency of $10^{-5}$, suitable for detecting the frequency of antigen-specific T cells and plasma cells ([7.15.18](/7.15.18), [7.15.20](/7.15.20)). Methods such as multiplex beads and proximity extension can measure dozens of cytokines at once in a very small sample.

## 34.5. Measuring Affinity

The strength of binding is expressed by the dissociation constant $K_{\mathrm{D}}$ (for the definition of affinity see [7.15.9](/7.15.9)). For $\mathrm{Ab} + \mathrm{Ag} \rightleftharpoons \mathrm{AbAg}$,

$$
K_{\mathrm{D}} = \frac{[\mathrm{Ab}][\mathrm{Ag}]}{[\mathrm{AbAg}]} = \frac{k_{\mathrm{off}}}{k_{\mathrm{on}}},
$$

and $K_{\mathrm{D}}$ is the free ligand concentration at which half the sites are occupied. Three commonly used methods correspond to three kinds of readout:

- Equilibrium dialysis and the Scatchard plot: antibody and a small-molecule ligand are separated by a semipermeable membrane, and at equilibrium the difference in ligand concentration across the membrane is the amount bound; plotting bound/free against bound gives a straight line whose slope is $-1/K_{\mathrm{D}}$ and whose abscissa intercept is the number of binding sites. It gives equilibrium information but not kinetics, requires much sample, and has been largely replaced by SPR.
- **Surface plasmon resonance** (SPR): one molecule is immobilized on a gold film surface and the other flows past in solution; binding changes the refractive index at the gold surface, and the change in the resonance angle of the reflected light (response units, RU) is proportional to the bound mass. The sensorgram has an association phase and a dissociation phase: in the association phase, $R(t) = R_{\mathrm{eq}}\bigl(1 - \mathrm{e}^{-k_{\mathrm{obs}} t}\bigr)$, where $k_{\mathrm{obs}} = k_{\mathrm{on}} C + k_{\mathrm{off}}$ and $R_{\mathrm{eq}} = R_{\max} C/(C + K_{\mathrm{D}})$; in the dissociation phase there is only $R(t) = R_0\,\mathrm{e}^{-k_{\mathrm{off}} (t - t_0)}$. For a series of concentrations, $k_{\mathrm{obs}}$ plotted against $C$ gives a straight line whose slope is $k_{\mathrm{on}}$ and whose intercept is $k_{\mathrm{off}}$. It measures $k_{\mathrm{on}}$, $k_{\mathrm{off}}$ and $K_{\mathrm{D}}$ together.
- Isothermal titration calorimetry (ITC): one molecule is added stepwise to a solution of the other and the heat released or absorbed at each binding is measured; one experiment gives $K_{\mathrm{D}}$, the binding enthalpy $\Delta H$ and the stoichiometry $n$; then from $\Delta G^\circ = RT\ln K_{\mathrm{D}}$ (with $1\,\mathrm{M}$ as the standard state) and $\Delta G^\circ = \Delta H - T\Delta S$ the entropy change is obtained, showing whether binding is enthalpy-driven or entropy-driven.

**Example 34.5.1** The relation between $K_{\mathrm{D}}$ and free energy is logarithmic: at $298\,\mathrm{K}$, $RT\ln 10 = 5.7\,\mathrm{kJ\,mol^{-1}}$, so $K_{\mathrm{D}} = 1\,\mathrm{nM}$ corresponds to $\Delta G^\circ \approx -51\,\mathrm{kJ\,mol^{-1}}$, and each 10-fold decrease in $K_{\mathrm{D}}$ adds only $5.7\,\mathrm{kJ\,mol^{-1}}$ of binding free energy, about one hydrogen bond. The same $K_{\mathrm{D}}$ can have entirely different kinetics: antibody 1 has $k_{\mathrm{on}} = 10^6\,\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} = 10^{-3}\,\mathrm{s^{-1}}$, antibody 2 has $k_{\mathrm{on}} = 10^5$ and $k_{\mathrm{off}} = 10^{-4}$, and both have $K_{\mathrm{D}} = 1\,\mathrm{nM}$. With $10\,\mathrm{nM}$ antigen flowing for 300 s, antibody 1 is already close to equilibrium ($R\approx 88\,\mathrm{RU}$, $R_{\max}=100$) while antibody 2 reaches only $26\,\mathrm{RU}$; after 900 s of dissociation, the signal of antibody 1 has fallen to $36\,\mathrm{RU}$ (half-life $\ln 2/k_{\mathrm{off}} \approx 690\,\mathrm{s}$) whereas that of antibody 2 is almost unchanged (half-life about $6900\,\mathrm{s}$). Giving $K_{\mathrm{D}}$ alone is therefore not enough: the efficacy of a neutralizing antibody and the duration of antigen recognition depend more on $k_{\mathrm{off}}$, and selection for affinity maturation in the germinal center also acts mainly on $k_{\mathrm{off}}$ ([7.15.20](/7.15.20)).

:::

![Simulated SPR sensorgrams (see Example 34.5.1). A: association phase (within 300 s) and dissociation phase of one antibody at four antigen concentrations. B: two antibodies with the same $K_{\mathrm{D}}$ (1 nM) but different kinetics: antibody 1 binds fast and dissociates fast, antibody 2 binds slowly and dissociates slowly](./plots/spr-sensorgram.py)

The mode of immobilization must be treated with care when interpreting SPR: if antigen is immobilized on the chip and bivalent IgG flows past, the two arms of one IgG can bind adjacent antigens at the same time, giving an apparent avidity far higher than the affinity of monovalent binding; to obtain the intrinsic affinity, immobilize the antibody and let the antigen flow past, or use a Fab fragment.

## 34.6. Microscopy and Imaging

There are two main ways of labeling when antibody is used to show where an antigen is in a tissue or cell.

**Definition 34.6.1 (Immunohistochemistry)** The method in which enzyme-labeled antibody detects antigen in a tissue section, the enzyme catalyzing the substrate to an insoluble colored precipitate so that the position of the antigen becomes visible under an ordinary light microscope, is called **immunohistochemistry** (IHC).

IHC commonly uses horseradish peroxidase to catalyze diaminobenzidine to a brown precipitate and counterstains nuclei with hematoxylin; fixed pathology sections can be stored and read for a long time, and this is the basis of pathological diagnosis. Its drawbacks are that the chromogenic precipitate is hard to quantify and usually only one or two markers can be detected per section. **Immunofluorescence** replaces the enzyme with a fluorophore, so one section can show several molecules simultaneously in several fluorescence channels; confocal microscopy can give optical sections, multiphoton microscopy (infrared pulsed excitation, deep penetration, little photodamage) can image living tissue, and intravital imaging can, for example, observe how T cells randomly scan dendritic cells in a lymph node ([7.15.3](/7.15.3), [7.15.22](/7.15.22)). **Multiplexed immunofluorescence** and imaging mass cytometry extend the number of species detected to dozens ([7.9.6](/7.9.6)). Immunoelectron microscopy labels antibody with gold particles of different sizes and can localize molecules at the subcellular level.

There are three principles for reading imaging results. First, negative controls: secondary antibody only, isotype control and target-gene knockout samples, to exclude nonspecific binding and autofluorescence. Second, localization must agree with what is known: CD3 is on the cell membrane and FOXP3 in the nucleus, and if the signal is in the wrong place, the antibody or the fixation conditions should be suspected. Third, fixation and antigen retrieval change antigenicity, and the optimal conditions differ between antibodies (see [7.15.35](/7.15.35)).

## 34.7. Flow Cytometry and Mass Cytometry

### 34.7.1. Principle and Spectral Spillover

**Flow cytometry** passes suspended cells one by one through a laser beam, and each cell simultaneously generates a set of signals: forward scatter (FSC, roughly reflecting cell size), side scatter (SSC, reflecting internal granularity and complexity) and the fluorescence detectors (corresponding to antibodies or dyes labeled with different fluorophores). Its characteristics are therefore single-cell, multiparameter and high-throughput (thousands of cells per second); it gives the proportion of each subset in a population of cells and defines cell types with dozens of parameters from the same sample; unlike imaging, it has no spatial information, but it yields quantitative cell counts.

The emission spectrum of a fluorophore is broad, and the light of one fluorophore falls into the detector of another; this is **spectral spillover**, and the correction it requires is called compensation.

**Definition 34.7.1 (Spectral Spillover)** The phenomenon in which the emitted light of one fluorophore is received by the detector of another fluorophore, so that the reading of that detector contains signal that does not belong to it, is called **spectral spillover**.

Suppose there are $m$ fluorophores, the true intensity vector is $\boldsymbol{x}\ge\boldsymbol{0}$, the readings of the detectors are $\boldsymbol{y}$, and the spillover matrix $S$ has elements $S_{ij}$ giving the signal entering detector $i$ from a unit of fluorophore $j$; then

$$
\boldsymbol{y} = S\boldsymbol{x} + \boldsymbol{\varepsilon},\qquad \hat{\boldsymbol{x}} = S^{-1}\boldsymbol{y},
$$

and compensation is the solution of this linear equation: the matrix $S$ is measured with single-stain controls (each tube containing only one fluorophore), and each column is the proportion of that fluorophore's reading in the various detectors. This has the same form as the image spillover compensation formula in [7.9.6](/7.9.6); when there are more detectors than fluorophores (spectral flow cytometry, in which the full emission spectrum of each cell is recorded), unmixing is done by least squares (with a nonnegativity constraint), and autofluorescence can also be subtracted as an extra "fluorophore" (for linear algebra see [2.1](/2.1)).

Compensation subtracts the mean of the spillover signal but cannot subtract its noise. The variance of photon shot noise is proportional to the size of the signal, and the spilled-in photons carry their own fluctuation; after compensation the mean is zero but the variance remains and is amplified by the matrix $S^{-1}$. This is spreading error: in a channel receiving spillover from a bright signal, the negative population widens after compensation, making dim positives hard to resolve.

**Example 34.7.1** Take two fluorophores, FITC and PE, with $S = \begin{bmatrix}1 & 0.05\\ 0.20 & 1\end{bmatrix}$ (20% of FITC enters the PE detector and 5% of PE enters the FITC detector), $S^{-1} \approx \begin{bmatrix}1.010 & -0.051\\ -0.202 & 1.010\end{bmatrix}$. A single-positive FITC cell with true intensity $\boldsymbol{x} = (8000, 0)$ is read as $\boldsymbol{y} = (8000, 1600)$ and rises along the diagonal in the two-channel scatter plot; after compensation $\hat{\boldsymbol{x}} = (8000, 0)$, back on the FITC axis. A simulation of 600 cells (including shot noise) finds that after compensation the mean PE reading of FITC single-positive cells is about 0 ($35$), but the standard deviation is about $370$, compared with about $60$ for unstained cells, roughly 6 times wider; the more spillover (the larger $S_{21}$), the more severe the spreading. This gives one rule for designing flow panels: do not put dim markers in channels that receive heavy spillover from bright fluorophores; for lowly expressed antigens choose bright fluorophores with little spillover, and for strongly expressed antigens choose dim fluorophores (see the panel design in [7.15.35](/7.15.35)).

:::

![Spectral spillover and compensation in two-color flow cytometry (simulated data, see Example 34.7.1; axes are symmetric logarithmic). A: before compensation, FITC single-positive cells (green) deviate from the FITC axis because of spillover into the PE detector. B: after compensation each population is back on the axis, but the FITC-positive population widens on the PE axis. C: comparison of the PE reading of compensated FITC single-positive cells (spreading error) with that of unstained cells](./plots/flow-compensation.py)

### 34.7.2. Controls, Sorting and Mass Cytometry

The reliability of flow cytometry depends on controls: single-stain controls are used to compute the compensation matrix; the "fluorescence minus one" (FMO) control omits one fluorophore from the full set and gives the boundary between positive and negative in that channel, because spreading error means the negative boundary cannot be drawn arbitrarily; viability dyes exclude dead cells, which bind antibody nonspecifically; Fc receptors are blocked to prevent antibody binding through the Fc; and for display a biexponential (logicle) scale is used, which can show both negative values and signals spanning a wide range. The process of delimiting cell populations from these data is called gating (see [7.15.35](/7.15.35)).

The **fluorescence-activated cell sorter** (FACS) adds sorting to flow cytometry: droplets containing cells are charged according to the result of preset gates and deflected in an electric field into collection tubes, giving purified subsets for functional experiments or sequencing. Purity and recovery of sorting are in conflict, and the rarer the subset, the harder it is to have both; magnetic bead sorting is gentler but of lower resolving power.

**Definition 34.7.2 (Mass Cytometry)** The single-cell technique in which antibodies are labeled with rare metal isotopes, cells are atomized and ionized in an inductively coupled plasma, and the ion counts of each isotope are read out cell by cell by time-of-flight mass spectrometry, is called **mass cytometry** (CyTOF).

The masses of metal isotopes are well separated from each other, so there is no spectral overlap as with fluorescence, more than 40 parameters can be measured at once, and panel design is flexible; a small amount of spillover remains (isotope impurities, oxides), but of a much smaller order. The cost is that cells are destroyed in the measurement (they cannot be sorted), throughput is lower (hundreds of cells per second), and some cells are lost. Combining laser ablation with mass cytometry gives imaging mass cytometry ([7.9.6](/7.9.6)).

| Technique | Label | Number of parameters | Spatial information | Features |
|---|---|---|---|---|
| Conventional flow cytometry | Fluorophores | About 10–20 | None | High throughput, can sort; needs compensation |
| Spectral flow cytometry | Fluorophores, whole spectrum recorded | 30–40 or more | None | Unmixing subtracts autofluorescence |
| Mass cytometry | Metal isotopes | 40 or more | None | Minimal spillover; cells destroyed, lower throughput |
| Multiplexed imaging | Fluorescence or metal | Dozens | Yes | Position retained; problems of segmentation and spillover ([7.9.6](/7.9.6)) |

## 34.8. Assays of Cell Function

Proliferation: early assays used incorporation of tritiated thymidine; now incorporation of the thymidine analogs BrdU or EdU into S-phase cells, or detection of Ki-67 (expressed by cycling cells), is more common. The most direct is dye dilution: carboxyfluorescein succinimidyl ester (CFSE) and its analogs covalently label intracellular proteins, which are divided equally between the two daughter cells at each division, so fluorescence halves, and after $n$ divisions the intensity is $F_0/2^n$; on a logarithmic scale each division differs by $\log_{10}2 \approx 0.30$, so equally spaced peaks appear on the flow histogram and the number of cells in each generation can be counted. From the distribution over generations one can also estimate the number of progeny produced by a precursor (the division index), corresponding to clonal expansion in [7.15.18](/7.15.18).

Cytotoxicity: the classic assay is the chromium release assay, in which target cells take up $^{51}\mathrm{Cr}$ beforehand and release it into the supernatant when killed, quantified by specific lysis:

$$
\text{specific lysis}\,(\%) = \frac{\text{experimental release} - \text{spontaneous release}}{\text{maximum release} - \text{spontaneous release}} \times 100,
$$

spontaneous release (target cells only) corrects for leakage from the target cells themselves, and maximum release (with detergent) represents the total releasable amount; specific lysis rises with the ratio of effector cells to target cells (E:T). Because radioactive handling is inconvenient, lactate dehydrogenase release, calcein release, flow-based methods (target cells labeled with a dye and read out with a death dye), and impedance and imaging methods are now used more; CD107a (a surrogate marker of degranulation) and granzyme B reflect killing function from the effector cell side ([7.15.5](/7.15.5), [7.15.17](/7.15.17)).

Apoptosis: phosphatidylserine is exposed on the outer membrane of early apoptotic cells, and fluorescently labeled Annexin V protein (requiring $\mathrm{Ca^{2+}}$) can bind it; propidium iodide and 7-AAD enter only cells that have lost membrane integrity. Used together, they give four quadrants in a two-dimensional scatter plot: Annexin V⁻/PI⁻ live cells, Annexin V⁺/PI⁻ early apoptosis, Annexin V⁺/PI⁺ late apoptosis or necrosis, and Annexin V⁻/PI⁺ necrosis or debris; TUNEL labels the 3′ ends of DNA fragments, and caspase activity can be read out with substrates or cleavage-specific antibodies, but TUNEL has lower specificity, and late necrotic cells are also positive ([7.3.25](/7.3.25)).

**Cytokines**: ELISA or multiplex beads measure the total amount in the supernatant; ELISpot measures the frequency of secreting cells (§34.4); in intracellular cytokine staining a protein transport inhibitor is added during stimulation so that the cytokine accumulates inside the cell, and after fixation and permeabilization it is stained with antibody and read out by flow cytometry, with the advantage of obtaining at once the phenotype (surface markers) and the function (which cytokine is produced) of the cell. The three answer different questions: concentration, frequency, and "which class of cell produces it".

Detection of antigen-specific T cells: the affinity of a single pMHC for a TCR is low ($K_{\mathrm{D}}$ in the micromolar range, with very fast dissociation), and a monomer cannot stain cells stably.

**Definition 34.8.1 (pMHC Tetramer)** The reagent in which four biotinylated peptide–MHC complexes are joined through streptavidin into one tetravalent, fluorescent molecule, used to stain and detect antigen-specific T cells, is called a **pMHC tetramer**.

Four pMHC bind several TCRs on the same cell at once, greatly lowering the apparent dissociation rate (the avidity effect), so stable staining is possible. The readout is "the percentage of CD8⁺ cells expressing a given TCR specificity", which can be sorted or phenotyped further; with magnetic bead enrichment, rare clones at a frequency of $10^{-5}$–$10^{-6}$ among naive T cells can even be detected ([7.15.18](/7.15.18)). Four points matter in interpretation: tetramers show only binding, and binding does not mean function, so they should be combined with ELISpot or intracellular staining; the MHC allele must match the subject, and each peptide–MHC combination must be prepared separately; clones of low affinity are missed; and for CD4⁺ T cells, staining is more difficult because the binding of MHC II to the TCR is weaker.

## 34.9. Single-Cell Omics and Genetic Engineering

Single-cell RNA sequencing and receptor sequencing link the transcriptome of each cell (cell type and state) with its TCR or BCR sequence: cells with the same CDR3 nucleotide sequence belong to one clone, clone size reflects the degree of expansion, and the phenotype of the clone reflects its differentiation fate ([7.15.12](/7.15.12), [7.15.18](/7.15.18)). The diversity of a repertoire can be described by information entropy: with clone frequencies $p_i$,

$$
H = -\sum_i p_i \ln p_i,\qquad \text{clonality} = 1 - \frac{H}{\ln N},
$$

where $N$ is the number of clones. A uniform repertoire has $H = \ln N$ and clonality 0; a repertoire dominated by a few clones (such as tumor-infiltrating T cells, chronic infection or immunosenescence) has small $H$ and high clonality. Methods such as CITE-seq use antibodies carrying nucleic acid barcodes to measure surface proteins and the transcriptome simultaneously, so that antibody-based immunophenotyping ([7.15.35](/7.15.35)) can be related to the whole transcriptome; positional information of cells in tissue is supplied by spatial omics ([7.9.5](/7.9.5), [7.9.6](/7.9.6)).

Animal models and genetic engineering are the basis for establishing function, and the most commonly used designs in immunology and their logic are:

- Inbred strains and congenic markers: mouse strains (C57BL/6, BALB/c) have an identical genetic background, so cell transfer does not cause rejection; congenic markers such as CD45.1 and CD45.2 distinguish donor from recipient cells for adoptive transfer, to track the fate of a particular cell population.
- TCR transgenics (such as OT-I, which recognizes an ovalbumin peptide presented by H-2K$^{\mathrm b}$, and OT-II, which recognizes an ovalbumin peptide presented by I-A$^{\mathrm b}$): almost all T cells carry the same TCR, making tracking and expansion of antigen-specific responses possible; this is the basis of the selection experiments in [7.15.15](/7.15.15).
- Gene knockout and conditional knockout: **knockout mice** such as *Rag1*⁻/⁻ (no T or B cells) and *Il2rg*⁻/⁻ combined with *Prkdc* deficiency (severely immunodeficient strains such as NSG, which can accommodate human cells to establish humanized mice, [7.15.31](/7.15.31)); **conditional knockout** (Cre–loxP) uses a cell-type-specific Cre (for example CD4-Cre deletes the gene only in T cells) to delete a gene in a particular lineage or at a particular time, avoiding the embryonic lethality or compensation of whole-body knockout;
- Bone marrow chimeras: bone marrow of different genotypes is transplanted into irradiated recipients, to distinguish whether the gene of the hematopoietic cell or of the stromal cell acts, for example the classic experiments showing that the MHC of epithelial cells is decisive in thymic positive selection.
- CRISPR and functional genomic screens: editing genes in primary T cells, or carrying out genome-wide **CRISPR screens**, to find genes that control T cell exhaustion, activation or killing ([7.2.24](/7.2.24)).

In using these models one must remember the differences between mouse and human: for example, IL-7 signaling is required by mouse B cells but not by human B cells ([7.15.31](/7.15.31)), and mice raised in a specific-pathogen-free environment have less mature immune memory than humans.

## 34.10. Interpreting Readouts: Sensitivity, Specificity and Predictive Value

The result of a test must be interpreted probabilistically. With sensitivity (the proportion of truly diseased individuals testing positive), specificity (the proportion of non-diseased individuals testing negative) and prevalence, the positive predictive value (the probability that a person testing positive is truly diseased) follows from Bayes' formula:

$$
\mathrm{PPV} = \frac{\mathrm{Se}\cdot \pi}{\mathrm{Se}\cdot\pi + (1-\mathrm{Sp})(1-\pi)},
$$

where $\pi$ is the prevalence (for measures of diagnostic tests and the ROC curve see [7.7.3](/7.7.3), for Bayes' theorem [3.1](/3.1)).

**Example 34.10.1** An antibody screening test has a sensitivity of $99.5\%$ and a specificity of $99.8\%$. When the population prevalence is $\pi=0.1\%$, $\mathrm{PPV} = 0.995\times0.001/(0.995\times0.001 + 0.002\times0.999) \approx 33.2\%$: two thirds of positive results are false positives; if the prevalence is $1\%$, $\mathrm{PPV}\approx 83.4\%$. A positive result in a low-prevalence population therefore needs confirmation: retesting with another test based on an independent principle (such as a confirmatory test with a sensitivity of $99\%$ and a specificity of $99.9\%$) raises the positive predictive value to $0.99\times0.332/(0.99\times0.332 + 0.001\times0.668) \approx 99.8\%$. This is why tests such as those for HIV use the two-step strategy of "high-sensitivity screening plus high-specificity confirmation": screening should miss as few cases as possible, and confirmation should make as few errors as possible; two tests of the same principle have correlated errors and are less effective than two tests of different principles.

:::

## Summary

- The common logic of immunological techniques is recognition, amplification and readout; sensitivity comes from amplification, specificity from recognition and reliability from controls; the detection limits of the methods differ by more than six orders of magnitude.
- Monoclonal antibodies are produced by a single B cell clone and polyclonal antibodies are a mixture; an antibody must be characterized in four respects: epitope, specificity, affinity and isotype.
- Precipitation (Definition 34.3.1) and agglutination (Definition 34.3.2) both depend on cross-linking of multivalent antibody and multivalent antigen; the network model gives the gelation condition $p_a p_g(v-1)>1$ and the antibody-excess, equivalence and antigen-excess zones of precipitation, explaining the hook effect (Example 34.3.1); the Coombs test detects incomplete antibodies that cannot agglutinate.
- The sandwich ELISA requires an antigen with at least two epitopes, and in the competitive format the signal is negatively related to concentration; the standard curve is fitted with a 4PL and is reliable only between EC10 and EC90 (Example 34.4.1); ELISpot (Definition 34.4.1) counts single secreting cells by spots.
- $K_{\mathrm{D}}=k_{\mathrm{off}}/k_{\mathrm{on}}$; SPR measures both $k_{\mathrm{on}}$ and $k_{\mathrm{off}}$, and ITC measures $\Delta H$ and $n$; the same $K_{\mathrm{D}}$ can have different kinetics (Example 34.5.1); the mode of immobilization can make SPR measure avidity.
- Immunohistochemistry (Definition 34.6.1) and immunofluorescence show position; reading images requires negative controls and checking of localization.
- Spectral spillover in flow cytometry (Definition 34.7.1) is corrected by compensation $\hat{\boldsymbol{x}}=S^{-1}\boldsymbol{y}$, but compensation amplifies noise, causing spreading error (Example 34.7.1); mass cytometry (Definition 34.7.2) has almost no spillover, but cells are destroyed.
- Functional assays: dye dilution halves fluorescence at each generation, chromium release uses specific lysis, Annexin V/PI gives four quadrants, and the pMHC tetramer (Definition 34.8.1) detects antigen-specific T cells through multivalent binding.
- Single-cell omics links phenotype to clone; animal models and conditional genetic engineering establish function.
- Test results must be interpreted with sensitivity, specificity and prevalence: at low prevalence the positive predictive value is low, and a confirmatory test of a different principle is needed (Example 34.10.1).

## Questions

1. Why can a reagent containing only monovalent Fab not produce precipitation, and why can a bivalent antigen not either? Explain with the gelation condition.

   **Answer** Precipitation requires the formation of an indefinitely extending cross-linked network, with the condition $p_a p_g (v-1) > 1$. Fab is monovalent, one Fab can link only one antigen and cannot bridge, so the network cannot extend. For a bivalent antigen ($v = 2$) the left-hand side is $p_a p_g \le 1$, equal to 1 only when all sites are occupied ($p_a = p_g = 1$), so only linear chains or closed rings can form and no network; at practical concentrations the result is small soluble complexes. Precipitation therefore requires an antigen with at least 3 sites that antibody can bind (or an antibody with more than two sites binding a multivalent antigen).

2. In a sandwich ELISA, the reading for a patient serum diluted 10-fold is higher than for the undiluted serum. What might be the cause? How should it be verified?

   **Answer** Most likely the high-dose hook effect: when the antigen concentration is too high, free antigen separately saturates the immobilized capture antibody and the detection antibody in solution and cannot form a "sandwich" with both at once, so the signal falls and the undiluted reading is too low. To verify, perform serial dilutions and see whether the concentration readings agree across dilutions (dilution linearity): for a sample without a hook effect, each dilution should convert to the same original concentration; when a hook effect occurs, the reading first increases on dilution and only later falls with further dilution. It could also be an interfering substance in the sample matrix whose interference weakens on dilution, which must be distinguished by spike recovery.

3. For therapeutic antibody A, $K_{\mathrm{D}}=1\,\mathrm{nM}$ and $k_{\mathrm{off}}=10^{-3}\,\mathrm{s^{-1}}$; for another antibody B, $K_{\mathrm{D}}$ is also $1\,\mathrm{nM}$ but $k_{\mathrm{off}}=10^{-5}\,\mathrm{s^{-1}}$. Calculate $k_{\mathrm{on}}$ and the dissociation half-life for each, and state which is more suitable as a long-acting neutralizing drug.

   **Answer** $k_{\mathrm{on}} = k_{\mathrm{off}}/K_{\mathrm{D}}$: for A it is $10^6\,\mathrm{M^{-1}s^{-1}}$ and for B $10^4\,\mathrm{M^{-1}s^{-1}}$. The dissociation half-life $\ln2/k_{\mathrm{off}}$ is about $690\,\mathrm{s}$ (about 12 minutes) for A and about $6.9\times10^4\,\mathrm{s}$ (about 19 hours) for B. For a treatment that needs long occupancy of a target whose concentration is continually renewed, the slow dissociation of B is more favorable, since once bound it does not come off quickly; but B takes a long time to reach binding equilibrium ($k_{\mathrm{obs}}=k_{\mathrm{on}}C+k_{\mathrm{off}}$ is small), so if rapid onset is wanted and the target concentration is high, A is more suitable. The choice depends on the turnover rate of the target and the mechanism of action.

4. In flow cytometry, why after compensation is the mean PE reading of FITC single-positive cells 0, yet much wider than that of unstained cells? What does this imply for panel design?

   **Answer** Compensation subtracts the mean contribution of FITC spillover into the PE detector (20% of the FITC signal), so the mean returns to 0; but the number of spilled photons itself has shot fluctuation (variance proportional to the signal), and compensation subtracts only the mean, the noise remains and is amplified by the compensation matrix, so the distribution of PE readings widens (spreading error). This makes dim positive populations in the PE channel hard to distinguish from the "negative" edge of FITC-positive cells. In designing a panel one should: assign strongly expressed antigens dim fluorophores, and weakly expressed antigens bright fluorophores in channels that do not receive spillover from bright fluorophores; use FMO controls to set boundaries; and where necessary switch to spectral flow cytometry or mass cytometry.

5. (Open question) An infection with a population prevalence of 0.5% is to be screened for, and two tests are available: test X with sensitivity 99% and specificity 95%; test Y with sensitivity 90% and specificity 99.9%. Design a screening and confirmation strategy, and calculate the positive predictive value obtained with your strategy.

   **Answer** Outline: first use X, with high sensitivity, as the screen (no missed diagnoses), then use Y, with high specificity, to confirm. For X, $\mathrm{PPV}=0.99\times0.005/(0.99\times0.005 + 0.05\times0.995) = 0.00495/(0.00495+0.04975)\approx 9.0\%$; Y is then applied to those positive on X, $\mathrm{PPV}_2 = 0.9\times0.0905/(0.9\times0.0905 + 0.001\times0.9095)\approx 98.9\%$. The overall sensitivity of the strategy is about $0.99\times0.90 = 89\%$, so about 11% of patients will be missed; if the cost of a missed diagnosis is high, people positive on X but negative on Y can be rechecked or tested with a third test instead of being excluded directly. If the errors of the two tests are correlated (for example antibody tests against the same antigen), the effect of confirmation will be smaller than calculated.
