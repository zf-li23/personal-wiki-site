---
title: "Immunity to Infection: Matching Effector Mechanisms to Pathogens"
description: The location of a pathogen (body surface, extracellular space, intracellular vesicle, cytosol) determines which class of effector mechanism works; type 1, 2 and 3 immunity unify the responses to viruses, bacteria, fungi and parasites; a classification of pathogen immune evasion strategies; immunopathology; immunological problems of emerging and reemerging infections; a competition model of interferon and CTLs in the control of acute viral infection.
source_hash: 6b34f64d8a71
---

The preceding chapters took the immune system apart piece by piece: recognition (receptors and presentation), decision (T cell activation and differentiation), effectors (antibodies, complement, phagocytosis and killing) and memory. This chapter puts the pieces back together and answers an integrative question on the knowledge pathway: faced with a particular pathogen, how does the immune system choose a suitable effector mechanism? The key variable is not the taxonomic name of the pathogen but its location in the body: among bacteria, those multiplying in tissue fluid and those hidden in macrophage phagosomes require entirely different responses; among "viruses", extracellular particles are neutralized by antibody, whereas intracellular ones can be killed only by T cells and NK cells. Matching location to type 1, 2 and 3 immunity ([7.15.1](/7.15.1)) gives a map from which the type of response can be predicted. We first present this map, then discuss viruses, intracellular and extracellular bacteria and fungi, and helminths and protozoa; then the strategies pathogens use to avoid these mechanisms, and immunopathology, in which the damage is caused by the immune response itself; and finally emerging and reemerging infections, closing with a competition model of interferon and CTLs that writes the sequence "the innate response buys time, the adaptive response completes clearance" as equations. Pathogen structure, pathogenic mechanisms and epidemiology are not repeated here, see [7.11.22](/7.11.22)–[7.11.35](/7.11.35); how defects expose each pathway is covered in [7.15.31](/7.15.31); vaccines in [7.15.33](/7.15.33).

## 32.1. Location Determines the Effector Mechanism

Infection can occur in four distinct spaces, which differ in the immune molecules and cells that can reach them:

1. Body surfaces and mucosal lumens (outside the epithelium): the lumina of the gut, airways and genitourinary tract, where antibodies and cells make contact mainly through products secreted by the epithelial barrier and transepithelially transported secretory IgA ([7.15.23](/7.15.23));
2. The extracellular space (tissue fluid, blood and lymph): complement, antibody and phagocytes can contact pathogens directly;
3. Intracellular vesicles (phagosomes and endosomes): the pathogen is enclosed by a cell and is out of reach of antibody, but the infected cell itself can be activated;
4. Cytoplasm and nucleus: all viruses and some bacteria and protozoa, which can be detected only through MHC class I presentation at the cell surface and intracellular sensors.

**Property 32.1.1 (Location–Effector Matching)** The immune mechanism that is effective against a pathogen is determined by where it is located: for extracellular pathogens, antibody, complement and phagocytes; for intravesicular pathogens, macrophages activated by CD4⁺ T cells (Th1); for cytosolic pathogens, CTLs, NK cells and interferon; for pathogens at body surfaces and mucosae, secretory IgA and the "expulsion" mechanisms of type 2 responses.

| Location | Example pathogens | Dominant immune type | Core effector mechanisms | Role of antibody |
|---|---|---|---|---|
| Body surfaces and mucosal lumens | Helminths; bacteria and fungi adhering to epithelium | Type 2 (partly type 3) | Secretory IgA; IgE, eosinophils, mast cells; goblet cell mucus and smooth muscle contraction; antimicrobial peptides | Blocking adhesion and neutralization, "quiet expulsion" without inflammation |
| Extracellular | Pyogenic bacteria; fungi; viruses and protozoa in transit | Type 3, plus antibody responses | Complement, opsonization and phagocytosis; neutrophil recruitment (Th17); toxin neutralization | Principal effector: opsonization, complement activation, neutralization |
| Intravesicular | Mycobacteria, *Salmonella*, *Leishmania* | Type 1 | IFN-γ activates macrophages and raises killing; granuloma containment | Limited; only prevents cell-to-cell spread |
| Cytosol and nucleus | Viruses; *Listeria*; some protozoa | Type 1 | Type I interferon; NK cells; CTLs; cytotoxic CD4⁺ T cells | Neutralizes extracellular virions; ADCC removes infected cells |

This table corresponds to earlier chapters: the center of type 1 immunity is the IL-12–IFN-γ axis with Th1 cells and CTLs ([7.15.17](/7.15.17)), type 3 immunity consists of IL-17, IL-22 and neutrophils, and type 2 immunity of IL-4, IL-5, IL-13, IgE and eosinophils. Innate lymphoid cells come first and T cells later, using the same cytokine language ([7.15.5](/7.15.5)). It should be stressed that the table gives only the dominant mechanisms: a real infection is always an ensemble of several mechanisms, and a pathogen may occupy different locations at different stages of its life cycle (a virus first spreads extracellularly and is subject to CTLs only after it enters cells).

## 32.2. Immunity to Viral Infection

Viruses are obligate intracellular parasites, and defense proceeds in three steps: cell-autonomous defenses block the virus in the first hours of entry and replication; within days NK cells and interferon limit spread; and after about a week the adaptive response clears the virus completely and leaves memory.

### 32.2.1. The Innate Response and Interferon

Viral nucleic acids are recognized by endosomal TLRs (TLR3, TLR7, TLR9), cytosolic RIG-I-like receptors and the cGAS–STING pathway ([7.15.6](/7.15.6)), and through IRFs induce type I **interferon**. Interferon has two actions: on neighboring cells, through the JAK–STAT pathway it induces hundreds of **interferon-stimulated genes** that put them into an antiviral state (PKR inhibiting translation, OAS–RNase L degrading RNA, Mx proteins and IFITM blocking viral entry and release, and so on); on immune cells, it activates NK cells and dendritic cells and promotes cross-presentation ([7.11.27](/7.11.27)). When a virus downregulates MHC I to escape CTLs, it falls precisely into the "missing self" recognition of NK cells ([7.15.5](/7.15.5)). NK cells peak on days 1–3 after infection and provide the earliest cellular killing, and IL-12 and IL-15 enhance their activity.

### 32.2.2. Division of Labor in the Adaptive Response

| Phase | Time after infection (mouse, order of magnitude for acute viral infection) | Main effectors | Function |
|---|---|---|---|
| Innate | Hours to 3 days | Type I interferon, NK cells | Limit replication and spread; tell the adaptive immune system the direction of the response |
| T cells | CTLs appear on days 3–4 and peak on days 7–10 | Perforin and granzymes, FasL of CD8⁺ CTLs; IFN-γ and TNF-α | Kill infected cells, removing the virus "factories"; noncytolytic cytokine effects also directly suppress replication |
| Antibody | From several days, lasting weeks | Neutralizing antibody (IgG, secretory IgA), complement, opsonization, ADCC | Block binding of extracellular virus to its receptor or membrane fusion, clear free virus, prevent reinfection |
| Memory | Months to lifelong | Memory CD8⁺ T cells, memory B cells and long-lived plasma cells | Faster and stronger response on reinfection ([7.15.18](/7.15.18)) |

The division of labor between antibody and T cells is understood from the location of the virus: **neutralization** occurs only while the virus is still outside cells, so the role of antibody is to prevent reinfection and limit spread (preventing binding to the receptor and membrane fusion, and causing particles to be opsonized or lysed by complement); once the virus has entered cells, and especially once it is integrated into the genome or latent, only CTLs can complete clearance. Priming of CTLs in turn requires help from CD4⁺ T cells, because the latter, through CD40L, endow dendritic cells with the ability to cross-present and supply IL-2 ([7.15.16](/7.15.16)). For mucosal viruses (influenza, poliovirus), preexisting secretory IgA is better at blocking viral entry, so the protective mechanism of mucosal vaccination differs from that of injection ([7.15.33](/7.15.33)). **Antibody-dependent enhancement** shows that antibody is not always protective: when antibody concentration is low or the epitope is non-neutralizing, antibody–virus complexes enter monocytes through Fc receptors and worsen infection with dengue virus and others ([7.11.27](/7.11.27)).

### 32.2.3. Persistent Infection and Exhaustion

Herpesviruses (CMV, EBV) persist for life by latency and are controlled by continuous T cell surveillance; a considerable fraction of clones in the T cell repertoire is occupied by them, which is the main source of memory pool inflation in immunosenescence ([7.15.18](/7.15.18)). In chronic infections in which the virus cannot be cleared and antigen persists (HIV, HBV, HCV, clone 13 of LCMV), T cells progress to exhaustion: proliferation, IL-2, TNF-α and IFN-γ are lost in turn, inhibitory receptors such as PD-1 remain highly expressed, and checkpoint blockade can partly restore function ([7.15.25](/7.15.25)).

## 32.3. Bacteria and Fungi: Extracellular and Intracellular

### 32.3.1. Extracellular Bacteria: Antibody, Complement and Neutrophils

Pyogenic bacteria multiply in tissue fluid, and immunity to them is predominantly humoral. Antibody, complement and phagocytes each play a part: IgG and IgM against capsular polysaccharide or bacterial surface proteins opsonize the bacteria, complement C3b is deposited and promotes phagocytosis through CR3 and CR1, and the membrane attack complex of the alternative and classical pathways can lyse Gram-negative bacteria ([7.15.10](/7.15.10)); neutrophils are recruited and activated through IL-17 and IL-22 from Th17 cells, and the latter also induces epithelial antimicrobial peptides ([7.15.17](/7.15.17)). Antibody against an exotoxin directly neutralizes the toxin so that it cannot bind receptors on target cells; immunity to diphtheria and tetanus therefore depends on antitoxin levels, and **toxoid** vaccines ([7.15.33](/7.15.33)) are designed on this basis.

The immunological peculiarity of capsular polysaccharides: polysaccharides are thymus-independent antigens that mainly elicit IgM responses with limited class switching and memory, and the response of infants and young children is especially poor ([7.15.8](/7.15.8)); these bacteria (*Streptococcus pneumoniae*, *Neisseria meningitidis*, *Haemophilus influenzae* type b) are therefore important pathogens in childhood, and are the problem that **conjugate vaccines** ([7.15.33](/7.15.33)) must solve. In individuals without a spleen or with antibody deficiency, encapsulated bacteria cause fulminant sepsis because of the lack of opsonization and blood clearance ([7.15.31](/7.15.31)).

Bacterial products are themselves strong immune stimuli. Lipopolysaccharide through TLR4 causes massive release of TNF-α, IL-1β and IL-6, which is beneficial inflammation locally but causes septic shock systemically (§32.6); **superantigens** ([7.11.33](/7.11.33)) do not depend on specific peptide–MHC recognition but bridge MHC II and the Vβ of the TCR simultaneously, and can activate a considerable fraction (up to 5%–20%) of T cells at once, causing a cytokine storm.

### 32.3.2. Intracellular Bacteria: Th1 and Macrophage Activation

*Mycobacterium tuberculosis*, *Salmonella*, *Listeria* and others live inside macrophages. Bacteria in the phagosome are not reached by antibody, and killing them requires activation of the macrophage itself: Th1 cells and NK cells secrete IFN-γ, which through JAK–STAT1 enhances phagosome–lysosome fusion, the respiratory burst and nitric oxide production and limits bacterial multiplication ([7.15.5](/7.15.5), [7.15.17](/7.15.17)). This circuit was already revealed through its defects in [7.15.31](/7.15.31): individuals with defects of IL-12, the IL-12 receptor, the IFN-γ receptor or STAT1 are extremely susceptible to mycobacteria. Tumor necrosis factor is also indispensable, so anti-TNF therapy can reactivate latent tuberculosis.

The immunology of tuberculosis is the typical example of type 1 immunity that "controls but does not clear": infected macrophages, T cells and fibroblasts aggregate into **granulomas** that surround the bacteria and keep them dormant; about a quarter of infected people remain asymptomatic for life, the immune system maintaining a balance, and when immunity declines (HIV, anti-TNF therapy, malnutrition) the bacteria become active again. Caseous necrosis at the center of the granuloma is a typical example of immunopathology (§32.6): tissue destruction comes mainly from the reaction of activated macrophages and T cells.

### 32.3.3. Fungi

Most fungal infections are controlled by innate immunity and cause disease only in individuals with defects, so fungal disease acts like a "probe" for immunodeficiency. Phagocytes recognize fungal cell walls through C-type lectins (Dectin-1 recognizes β-glucan) and TLRs, which trigger IL-1β, IL-6 and IL-23 through Syk–CARD9; neutrophils are the main force against *Candida* and *Aspergillus* (patients with chronic granulomatous disease and neutropenia are prone to invasive aspergillosis); Th17 cells and IL-17 protect mucosal surfaces against *Candida* (individuals with CARD9 deficiency, STAT3 deficiency and anti-IL-17 autoantibodies are prone to chronic mucocutaneous candidiasis, [7.15.31](/7.15.31)); fungi inside cells (*Histoplasma capsulatum*, some stages of *Cryptococcus*) require Th1 cells and IFN-γ, so AIDS patients with reduced CD4⁺ T cells are prone to cryptococcal and histoplasma infections.

## 32.4. Parasites

The types and life cycles of parasites are far more complex than those of bacteria; immunologically they are divided by size and location into two major groups.

### 32.4.1. Helminths: Type 2 Immunity

Helminths are large and cannot be phagocytosed; they can be cleared only by "expulsion". Epithelial cells, damaged or stimulated by parasite products, release IL-25, IL-33 and TSLP (intestinal tuft cells are an important source of IL-25), which activate ILC2s and Th2 cells to produce IL-4, IL-5, IL-9 and IL-13 ([7.15.17](/7.15.17)). Their effects divide the labor: IL-4 and IL-13 promote B cell switching to IgE and cause goblet cell hyperplasia and increased mucus secretion, faster epithelial turnover and stronger smooth muscle contraction, "flushing" and "sweeping" the worm out; IL-5 recruits eosinophils, and eosinophils and mast cells, activated through IgE and FcεRI, degranulate and attack worms coated with IgE ([7.15.26](/7.15.26)). The same mechanism out of control is allergy, so type 2 immunity was evolutionarily designed for helminths and causes allergy in the modern environment free of helminth infection. Helminths often persist for a long time, because they induce Tregs and IL-10 to suppress the host response and at the same time divert immunity toward tissue repair (alternatively activated macrophages); the granuloma induced by schistosome eggs is damage caused to tissue by a type 2 response, and is also an example of immunopathology.

### 32.4.2. Protozoa

Protozoa are unicellular eukaryotes living inside cells or in the blood; different species correspond to different locations and therefore require different responses:

- *Leishmania* lives inside macrophage vesicles, and the type of response determines the outcome: a Th1 response (IL-12, IFN-γ) activates macrophages and clears the parasite, as in resistant mouse strains; a Th2 response (IL-4) leaves macrophages unable to kill the parasite and the infection spreads. It is the classic in vivo demonstration of Th1/Th2 polarization ([7.15.17](/7.15.17)), and leprosy has a similar spectrum: the tuberculoid form is Th1-dominated and localized, whereas the lepromatous form is Th2- and antibody-dominated and disseminated.
- *Plasmodium* passes through a hepatocyte stage (controlled by CD8⁺ T cells and IFN-γ; antibody against sporozoite surface proteins can prevent entry into the liver) and an erythrocyte stage (antibody, macrophages and splenic clearance, with Th1 activation of macrophages). Its immunological difficulties are twofold: PfEMP1 on the erythrocyte surface is expressed from one of about 60 *var* genes and is switched continually, producing antigenic variation; and protective immunity is acquired only gradually after repeated exposure over many years, usually as incomplete "disease resistance" rather than sterilizing immunity. Inflammatory factors (TNF-α and others) produced in the erythrocyte stage also cause fever and severe disease.
- Trypanosomes (*Trypanosoma brucei*) live in the blood, and their surface cycles through thousands of variant surface glycoproteins (VSG), so that antibody is always one step behind (§32.5).

## 32.5. Pathogen Immune Evasion

A pathogen that exists today must have found ways to avoid immunity. Classifying these ways by the link of the immune pathway they interfere with is more useful than memorizing them one by one.

**Definition 32.5.1 (Pathogen Immune Evasion)** The phenomenon in which a pathogen, by avoiding recognition, interfering with effector mechanisms or modulating the host immune response, still survives, replicates or is transmitted in the presence of an immune response is called **pathogen immune evasion**.

| Link interfered with | Strategy | Examples |
|---|---|---|
| Avoiding recognition | Antigenic variation (mutation, recombination and switching of expression) | Antigenic drift and shift of influenza HA; trypanosome VSG switching; *Plasmodium* PfEMP1; high mutation rate and glycan shield of HIV Env |
| | Capsule and surface disguise | Multiple capsular serotypes of *Streptococcus pneumoniae*; sialic acid capsule of *Neisseria meningitidis* resembling host molecules; schistosomes coating their surface with host proteins |
| | Latency and hiding | Herpesvirus latency; HIV provirus; escape of *Listeria* and *Shigella* into the cytosol |
| Interfering with effectors | Degrading or binding antibody | IgA protease (*Neisseria*, *Haemophilus influenzae*, *Streptococcus pneumoniae*); *Staphylococcus aureus* protein A binding the Fc of IgG |
| | Inhibiting complement | Binding factor H to limit C3b deposition; poxviruses encoding complement regulatory proteins |
| | Anti-phagocytosis and anti-killing | Capsule and M protein; leukocidins; *Mycobacterium tuberculosis* and *Legionella* blocking phagosome maturation |
| | Interfering with antigen presentation and NK recognition | HSV ICP47 inhibiting TAP; CMV US2 and US11 degrading MHC I; adenovirus retaining MHC I; HIV Nef downregulating MHC I; CMV expressing MHC I homologs to deceive NK cells |
| | Blocking interferon | Influenza NS1; hepatitis C virus protease cleaving MAVS; paramyxoviruses blocking STAT |
| Modulating the host response | Inducing immunosuppression | EBV encoding an IL-10 homolog; helminths inducing Tregs and IL-10; measles and HIV damaging lymphocytes |
| | Steering the response toward an ineffective type | Th1/Th2 deviation in leprosy; *Leishmania* inducing Th2 |

What most needs to be understood in this table is the causal relation between immune selection pressure and escape: antibody and CTLs exert selection on viral epitopes so that escape variants prevail (within an individual HIV can accumulate escape mutations in under a year; annual antigenic drift of influenza means vaccine strains must be updated); antigenic shift, on the other hand, introduces new subtypes against which the population has no preexisting immunity, causing pandemics ([7.11.27](/7.11.27), [7.11.35](/7.11.35)). Another phenomenon is original antigenic sin: memory established by a previous infection with one virus is preferentially reactivated on encountering a variant, with the result that epitopes specific to the new variant elicit only a weaker primary response, so the type of influenza strain a person is first infected with determines his or her lifelong immune preference for later variants ("immune imprinting"). This is the cost of memory, and also the motivation for seeking conserved epitopes in designing universal vaccines ([7.15.33](/7.15.33)).

Details of pathogen evasion and secretion systems are in [7.11.34](/7.11.34).

## 32.6. Immunopathology: Damage Caused by the Response

The immune response has a cost: the most effective means of clearance (killing infected cells, inflammation, cytokines) also destroy tissue, so many symptoms of infection are caused by the host response, and the virulence of the pathogen itself is only the trigger.

- LCMV and CTLs: lymphocytic choriomeningitis virus is not itself cytotoxic to mice; immunocompetent mice infected intracranially die of meningitis, whereas mice lacking T cells survive carrying the virus. This experiment (Doherty and Zinkernagel, the discovery of MHC restriction) shows that the lesion is caused by CTL killing of infected cells. Hepatocyte injury in hepatitis B is also mainly CTL-mediated.
- Septic shock: LPS of Gram-negative bacteria through TLR4 causes massive systemic release of TNF-α, IL-1β and IL-6, causing vasodilation, leakage and intravascular coagulation, and patients die of excessive inflammation rather than of the number of bacteria ([7.15.7](/7.15.7)).
- Granuloma and caseous necrosis (tuberculosis), schistosome egg granuloma: chronic type 1 and type 2 responses cause fibrosis when they persist for a long time ([7.15.27](/7.15.27)).
- Antibody and immune complexes: poststreptococcal glomerulonephritis (immune complexes), rheumatic fever (antibody against M protein cross-reacts with cardiac antigens, molecular mimicry, [7.15.28](/7.15.28)); a second dengue infection is worsened through antibody-dependent enhancement.
- Immune reconstitution inflammatory syndrome: T cells restored after HIV treatment react violently to previously latent pathogens ([7.15.31](/7.15.31)).
- **Cytokine storm**: uncontrolled systemic cytokine release in severe influenza, emerging coronavirus infection or CAR-T therapy ([7.15.30](/7.15.30)).

This has direct implications for treatment: in some infections (tuberculous meningitis, severe pneumonia) inflammation must be suppressed together with antimicrobial therapy; it also explains why regulatory mechanisms (Tregs, IL-10, inhibitory receptors, [7.15.25](/7.15.25)) are crucial for the outcome of infection: too weak and the pathogen cannot be cleared, too strong and the host is damaged.

## 32.7. Immunological Problems of Emerging and Reemerging Infections

Emerging infections mostly come from animal hosts, and the population has no preexisting immunity to them, so their immunological features are: slow primary responses, a susceptible population, no herd immunity, and unrestricted transmission until enough acquired immunity (from infection or vaccine) has arisen. New subtypes arising by antigenic shift and cross-species transmission of animal coronaviruses and avian influenza viruses belong to this class. The work of immunology is to estimate existing antibody levels in the population by serological surveys, to identify protective antigens and correlates of protection ([7.15.33](/7.15.33)), and to assess how much preexisting cross-reactive memory (for example T cell memory to other coronaviruses) can contribute. Reemerging infections have other causes: the resurgence of tuberculosis in the HIV epidemic; the return of measles when population vaccine coverage falls (the collapse of herd immunity, [7.11.35](/7.11.35)); the waning over time of immunity induced by some vaccines (the shorter duration of protection of acellular pertussis vaccine); and pathogens evading existing immunity through antigenic variation.

## 32.8. Model: The Race Between Interferon and CTLs

We use a minimal mathematical model to write the sequence of this chapter as equations. Suppose a tissue contains $T_0 = 10^6$ target cells. Virus $V$ infects target cells $T$ to make infected cells $I$, and $I$ releases virus; infected cells also secrete type I interferon $F$, which reduces the infection rate of neighboring target cells to $\beta/(1 + fF)$; CTLs $E$ start from only $E_0 = 1$ (corresponding to a very small number of specific precursors) and proliferate driven by antigen, so that several days are needed to reach an effective number:

$$
\begin{aligned}
\frac{\mathrm{d}T}{\mathrm{d}t} &= -\frac{\beta TV}{1 + fF},\\
\frac{\mathrm{d}I}{\mathrm{d}t} &= \frac{\beta TV}{1 + fF} - \delta I - kEI,\\
\frac{\mathrm{d}V}{\mathrm{d}t} &= pI - cV,\\
\frac{\mathrm{d}F}{\mathrm{d}t} &= sI - aF,\\
\frac{\mathrm{d}E}{\mathrm{d}t} &= \rho E\,\frac{I}{I + h} - \mu E.
\end{aligned}
$$

Here $\delta$ is the death rate of infected cells caused by the virus, $k$ is the killing rate constant of CTLs, $p$ and $c$ are the production and clearance rates of virus, $s$ and $a$ are the production and decay rates of interferon, $\rho$ is the expansion rate of CTLs when antigen is plentiful, $h$ is the half-saturation number of infected cells, and $\mu$ is the death rate of CTLs. Without an immune response, the growth factor of the virus is determined by the basic reproduction number $R_0 = \beta pT_0/(\delta c)$ (the same as in the HIV model of [7.15.31](/7.15.31); for differential equations see [2.4](/2.4)), in which interferon lowers the effective $\beta$ and CTLs increase the effective $\delta$.

**Example 32.8.1** Take illustrative parameters: $\delta = 0.5\,\mathrm{d^{-1}}$, $c = 5\,\mathrm{d^{-1}}$, $p = 40\,\mathrm{d^{-1}}$, $R_0 = 8$, $f = 0.1$, $k = 2\times10^{-6}$, $\rho = 1.6\,\mathrm{d^{-1}}$, $h = 10^3$, $\mu = 0.05\,\mathrm{d^{-1}}$, $s = 10^{-3}$, $a = 1.5\,\mathrm{d^{-1}}$, and initial virus $V_0 = 10^3$. The numerical solutions for four scenarios are (damage measured by the fraction of target cells infected and depleted):

| Scenario | Viral peak | Time of peak | Target cell loss | Outcome |
|---|---|---|---|---|
| No response | $4.4\times10^6$ | Day 5 | About 100% | Target cells are exhausted and the virus declines for lack of targets |
| Interferon only | $6.5\times10^5$ | Day 7 | About 71% | Peak reduced about 7-fold, but on day 30 the virus is still $1.9\times10^5$: it becomes a persistent infection |
| CTLs only | $4.4\times10^6$ | Day 5 | About 100% | CTLs peak on day 12 and clear the virus by about day 13, but the tissue has already been exhausted |
| Interferon + CTLs | $6.5\times10^5$ | Day 7 | About 35% | Cleared by about day 15, damage reduced to about one third |

The model gives a plain conclusion: interferon "buys time"; it does not clear the virus but suppresses its early growth, giving CTLs time to expand (in the figure the CTLs cross $10^4$ cells, the point at which killing becomes meaningful, at about day 7); CTLs "complete the clearance", but arriving too late they cannot by themselves prevent tissue loss; neither can be dispensed with, which also explains why individuals with interferon pathway defects ([7.15.31](/7.15.31)) develop severe viral disease, whereas those with T cell defects cannot clear the virus. The limitations of the model are that target cells are not regenerated, the antigen dependence of CTLs is simplified, and antibody and NK cells are absent; the parameters only indicate orders of magnitude and are not a fit to any one virus; in practice, antibody neutralizes from weeks 1–2 and would further lower the late viral load.

:::

![Combined control of acute viral infection by interferon and CTLs (illustrative parameters, see Example 32.8.1). A: time course of free virus in the four scenarios (logarithmic scale; the legend gives the fraction of target cells lost): interferon lowers the viral peak, CTLs clear the virus, and damage is smallest when both act together. B: interferon (relative to its peak, left axis) and CTLs (logarithmic scale, right axis) in the combined scenario: interferon rises immediately with the number of infected cells, whereas CTLs expand from a single cell to an effective level only after several days](./plots/ifn-ctl-race.py)

## Summary

- The location of the pathogen determines the effective effector mechanism (Property 32.1.1): at body surfaces and mucosae, secretory IgA and type 2 "expulsion"; in the extracellular space, antibody, complement, phagocytosis and type 3 immunity; in vesicles, Th1 cells and activated macrophages; in the cytosol, interferon, NK cells and CTLs.
- The sequence of viral infection is: interferon and NK cells (hours to 3 days), CTLs (peak on days 7–10), neutralizing antibody and memory; antibody neutralizes only extracellular virus, intracellular virus must be cleared by CTLs; chronic infection exhausts T cells.
- Extracellular bacteria are handled by antibody, complement, neutrophils and Th17 cells; capsular polysaccharides are thymus-independent antigens with poor responses in infants, and the solution is the conjugate vaccine; intracellular bacteria are handled by IFN-γ activation of macrophages, and the tuberculosis granuloma "controls but does not clear".
- Fungi are mostly controlled by innate immunity (C-type lectins, neutrophils) and Th17 cells, so fungal disease is a probe for immunodeficiency.
- Helminths are expelled by type 2 immunity (IL-4, IL-5, IL-13, IgE, eosinophils, mast cells, mucus and smooth muscle), and the same mechanism out of control is allergy; protozoa use different mechanisms according to location, *Leishmania* being the classic demonstration of Th1/Th2 polarization, while *Plasmodium* and trypanosomes escape by antigenic variation.
- Pathogen immune evasion (Definition 32.5.1) can be classified by the link interfered with: avoiding recognition, interfering with effectors, modulating the host response; immune selection pressure and escape are mutual cause and effect, and original antigenic sin is the cost of memory.
- Many symptoms are immunopathology: the damage is caused by the response, and regulatory mechanisms are crucial for the outcome.
- Emerging infection is a problem of a population without preexisting immunity, whereas reemerging infection stems from declining immunity, falling vaccine coverage or antigenic variation.
- The interferon–CTL race model (Example 32.8.1): interferon buys time, CTLs complete clearance, and target cell damage is smallest when both act together.

## Questions

1. A patient is infected with a bacterium that multiplies only inside macrophage phagosomes. His serum has a high antibody titer against the bacterium, yet he cannot clear the infection. Explain. What would happen if he lacked the IFN-γ receptor?

   **Answer** Antibody can reach only extracellular bacteria and cannot reach bacteria inside phagosomes, so a high antibody titer does not protect against intracellular bacteria. Clearing such bacteria requires IFN-γ secreted by Th1 cells and NK cells to activate macrophages (enhanced phagosome–lysosome fusion, respiratory burst and nitric oxide). Without the IFN-γ receptor, macrophages cannot be activated and the bacteria multiply unrestrained; the patient is highly susceptible to mycobacteria and *Salmonella* (Mendelian susceptibility to mycobacterial disease), while immunity to most viruses and extracellular bacteria is largely preserved.

2. Why do preexisting mucosal IgA and serum IgG differ in their protective significance against a respiratory virus? Why can antibody not clear a virus already integrated in the host genome?

   **Answer** Secretory IgA on the airway mucosal surface can neutralize the virus before it binds epithelial cells, without causing inflammation, acting as the "first line of defense"; serum IgG enters the lower airways and tissues by exudation, protects deeper sites, and clears virus through opsonization, complement and ADCC. Antibody acts only on antigen outside cells or at the cell surface; when viral genes are integrated in the genome and no protein is expressed, there is no target on the cell surface; even if protein is expressed, the cell can be cleared only when CTLs and NK cells recognize MHC class I-presented peptides or stress ligands and kill it, so integrated (latent) virus escapes the action of antibody.

3. Using Example 32.8.1, explain why both the "interferon only" and "CTLs only" scenarios are unsatisfactory, whereas target cell loss is smallest when the two are combined.

   **Answer** Interferon is produced immediately after infection begins and lowers the effective infection rate, reducing the viral peak about 7-fold and delaying it by about 2 days; but it does not kill infected cells, and on day 30 the virus is still $1.9\times10^5$, so the infection becomes persistent. CTLs start from very few precursors and cross the effective number only at about day 7, by which time the virus has reached the peak it would reach with no response and the target cells are exhausted; CTLs clear the virus but cannot undo the tissue loss. When combined, the days gained by interferon allow CTLs to arrive before the target cells are exhausted, so the loss is only about 35% and the virus is also cleared. This shows that the innate and adaptive responses are a relay in time, not substitutes for each other.

4. Influenza vaccines are updated every year, whereas measles vaccine has remained unchanged for decades. Explain from the standpoint of antigenic variation, and state the implication of original antigenic sin for influenza vaccines.

   **Answer** Influenza virus is a segmented single-stranded RNA virus whose RNA polymerase has no proofreading; HA and NA undergo point mutations every year (antigenic drift) and accumulate escape mutations under selection pressure, and new subtypes can also arise by segment reassortment (antigenic shift). The antigenicity of measles virus is very stable, there is only one serotype, and neutralizing antibody induced by the vaccine is effective against all strains. Original antigenic sin means that memory B and T cells are preferentially reactivated by previously encountered similar epitopes; on vaccination against a new variant, the response is biased toward the old epitopes and the response to the new epitopes is weaker, so preexisting population immunity provides some protection but also limits the response to new variants, which must be considered in selecting vaccine strains and in designing universal vaccines (directed at conserved epitopes).

5. (Open question) In a patient with severe disease caused by an emerging virus, clinical deterioration in the late phase coincides with a fall in viral load. How would you explain this using the concept of immunopathology? What are the implications for investigations and treatment?

   **Answer** Outline: late worsening may be caused by an excessive immune response rather than by the virus itself (cytokine storm; damage to alveolar epithelium and vascular endothelium by CTLs and inflammation, similar to the CTL-mediated damage of LCMV and to septic shock). Investigations should measure inflammatory markers (IL-6, CRP and others) and lymphocyte subsets, to distinguish the "virus-driven" from the "immune-driven" phase. For treatment, early on antivirals and neutralizing antibody reduce the virus (when viral load is high), and later inflammation can be suppressed (glucocorticoids, IL-6 pathway inhibitors); but inappropriate immunosuppression would weaken viral clearance, so they must be applied according to the stage of the disease; other possibilities such as antibody-dependent enhancement and T cell exhaustion should also be considered.
