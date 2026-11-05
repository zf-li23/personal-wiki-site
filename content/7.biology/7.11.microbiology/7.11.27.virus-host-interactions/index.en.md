---
title: Virus–Host Interactions
description: "How viruses infect hosts and how hosts resist: receptors, host range and tropism, spread within the body, cell-autonomous restriction factors and their viral antagonists, pattern recognition and the interferon response, escape from adaptive immunity, patterns of infection and within-host dynamics, mechanisms of viral disease and oncogenesis, and the emergence of new viruses."
---

The molecular virology of the preceding chapters describes what happens in one infected cell. A disease happens in an organism, and an epidemic in a population. This chapter is about the levels in between: how a virus chooses its cells and its hosts, what defences it meets in the first hours, how an infection is sustained or cleared, why some infections cause disease and others none, and how a virus that has circulated in another animal for a long time comes to infect people.

The emphasis is on what constrains viral replication, because that is what belongs in a microbiology course. The cells and organs of the immune system, antigen presentation, the development of lymphocytes and the structure of antibodies are the subject of immunology ([7.15](/7.15)); here we go as far as the defences a virus must antagonize in order to replicate at all — the restriction factors and the interferon system — and treat adaptive immunity only as the selective force that shapes viral antigens. Within-host dynamics are modelled here; transmission between hosts, epidemiological parameters and diagnosis are in [7.11.35](/7.11.35).

## 27.1. Three Levels of Infection

The outcome of an encounter between a virus and a host is set by a three-way interaction: the virus, the cell it enters, and the immune system of the host. The same virus can produce no symptoms in one person and a fatal illness in another, and the same number of particles delivered by two routes can give different diseases.

Three requirements must be met for an infection to start at all: enough infectious particles must arrive; they must reach cells that are both *susceptible* (bearing the receptor) and *permissive* (able to support replication); and the local defences must be absent or slow enough. Most encounters fail at one of these, and most infections that do start are subclinical. It is worth stating plainly, because the diseases are what get studied: severe disease is the exception, not the purpose of the virus — a virus that kills its host quickly loses the transmission opportunities that selection acts on ([7.10.17](/7.10.17#sec-17.2)).

## 27.2. Host Range, Tropism and Spread

**Remark 27.2.1** **Host range** and **tissue tropism** (Definition 22.5.1) are determined in the first instance by the receptor, and after that by every subsequent step. A cell without the receptor is not susceptible; a cell with the receptor but lacking a required transcription factor, protease or nucleotide pool is susceptible but not permissive; a cell that is both may still restrict the virus with the defences of §27.3 and §27.4.

Receptors explain much of what a virus does in the body.

- *Hepatitis B virus* binds the sodium taurocholate cotransporting polypeptide (NTCP), a bile-acid transporter expressed almost only on the basolateral membrane of hepatocytes. The strict hepatotropism and narrow host range of the virus follow directly, and the identification of NTCP in 2012 made it possible to render ordinary cell lines susceptible by expressing a single human gene.
- *SARS-CoV-2* binds angiotensin-converting enzyme 2 (ACE2), which is expressed in nasal and bronchial epithelium, in alveolar type II cells, in the intestine, the kidney and the vascular endothelium — a distribution that matches the respiratory presentation and the systemic complications. Entry also needs a protease to cleave the spike, TMPRSS2 at the plasma membrane or cathepsin L in the endosome, and which one is available further restricts which cells are productively infected.
- *HIV-1* needs CD4 together with a chemokine coreceptor, CCR5 or CXCR4. The requirement for two molecules restricts the virus to CD4⁺ T cells, macrophages and dendritic cells, and people homozygous for the *CCR5*-Δ32 deletion are largely resistant to infection by the common CCR5-using strains.
- *Rabies virus*, at the other extreme, uses conserved neuronal molecules and infects essentially all mammals — a broad host range with a very narrow tropism.

![Host range, tropism and spread within the body. A: the receptor sets which cells are susceptible — NTCP on hepatocytes for hepatitis B virus, ACE2 with the protease TMPRSS2 on respiratory epithelium for SARS-CoV-2, CD4 with CCR5 on T cells and macrophages for HIV-1 — but a cell is productively infected only if it is also permissive and its defences are overcome. B: routes within a host. A virus that enters at a mucosal surface may stay local (influenza virus, rotavirus) or spread, by the blood (primary and secondary viraemia, as in poliovirus and measles virus) or along peripheral nerves by retrograde axonal transport (rabies virus, herpes simplex virus); shedding into respiratory secretions, saliva, faeces, urine, milk, semen or skin lesions determines how the next host is reached](./plots/tropism-and-spread.py)

A virus that replicates only at the site of entry gives a short incubation period and a local disease — influenza in the airway, rotavirus in the gut. A virus that disseminates needs a route. *Haematogenous* spread goes through the blood, usually in two stages: a primary viraemia seeding the liver, spleen or lymph nodes, replication there, and a secondary viraemia of higher titre that reaches the target organ. Poliovirus reaches the central nervous system in a small minority of infections this way; measles virus reaches the skin. *Neural* spread uses the axon: rabies virus binds at the neuromuscular junction and is carried to the spinal cord and brain by retrograde transport along microtubules at a few millimetres to centimetres per day, which is why the incubation period depends on the distance from the bite to the brain, and why the disease is hidden from the immune system for weeks. Herpes simplex virus travels the same road in both directions, to the trigeminal ganglion for latency and back to the lip on reactivation.

## 27.3. Cell-Autonomous Defence: Restriction Factors

Long before any immune cell arrives, the infected cell itself opposes the virus with proteins that are already present.

**Definition 27.3.1 (Restriction Factor)** A **restriction factor** is a host protein that directly blocks a step of viral replication in the cell in which it is expressed. Restriction factors are constitutively present, usually induced further by interferon, act without any prior exposure to the virus, and are typically countered by a dedicated viral antagonist; the genes encoding them are among the fastest-evolving in mammalian genomes, carrying the signature of recurrent positive selection ([7.10.23](/7.10.23)).

| Factor | What it does | Viral antagonist |
|---|---|---|
| APOBEC3G | a cytidine deaminase packaged into virions; deaminates C to U in the minus-strand DNA during reverse transcription, producing lethal G-to-A hypermutation of the provirus | HIV-1 Vif recruits a ubiquitin ligase that degrades it |
| Tetherin (BST-2) | a membrane protein with two anchors that retains budded virions on the cell surface | HIV-1 Vpu, SARS-CoV-2 Orf7a, and unrelated proteins of other viruses |
| TRIM5α | binds the incoming capsid lattice and causes premature uncoating and degradation; its specificity for capsid sequence is a major barrier to retroviruses crossing between primate species | capsid substitutions that are not recognized |
| SAMHD1 | hydrolyses dNTPs and keeps their concentration in resting cells too low for reverse transcription | Vpx of HIV-2 and some SIVs degrades it; HIV-1 has no Vpx |
| MxA, MxB | large GTPases that trap incoming nucleocapsids (influenza virus) or block nuclear import (HIV-1) | nucleoprotein substitutions |
| LY6E | impairs fusion of coronavirus spike with the membrane and limits disease in mice | not established |
| IFITM proteins | alter the properties of the endosomal membrane and prevent fusion | several, virus-dependent |

![Restriction factors act at the steps of the retroviral cycle, and each is countered. APOBEC3G is packaged into the virion and hypermutates the nascent DNA unless Vif degrades it; TRIM5α attacks the incoming capsid; SAMHD1 starves reverse transcription of dNTPs in resting cells, and Vpx of HIV-2 removes it; MxB blocks nuclear import of the pre-integration complex; tetherin retains finished virions at the plasma membrane until Vpu removes it. The same logic — a constitutive host block and a dedicated viral antagonist — recurs for other virus families; SARS-CoV-2 Orf7a antagonizes tetherin and LY6E opposes coronavirus fusion](./plots/restriction-factors.py)

**Remark 27.3.1** The pattern is the molecular form of the arms race of [7.11.23](/7.11.23) and [7.11.26](/7.11.26#sec-26.5). Because a restriction factor and its antagonist each impose selection on the other, the interacting surfaces accumulate non-synonymous substitutions far faster than the rest of the protein, and the history of past conflicts can be read from present-day sequences: the pattern of selection on primate *TRIM5* records which retroviruses infected which lineages, long before any of them were isolated.

## 27.4. Sensing the Virus and the Interferon Response

The second line is also cell-autonomous, but it is inducible and it warns the neighbours.

**Definition 27.4.1 (Pattern Recognition Receptor)** A **pattern recognition receptor** (PRR) is a germline-encoded host sensor that recognizes a **pathogen-associated molecular pattern** (PAMP) — a molecular feature shared by a class of microbes and absent from, or mislocalized relative to, the host's own molecules. For viruses the patterns are almost all nucleic acids in the wrong place or the wrong form.

| Sensor | Location | Ligand |
|---|---|---|
| TLR3 | endosome | double-stranded RNA |
| TLR7, TLR8 | endosome | single-stranded RNA |
| TLR9 | endosome | unmethylated CpG DNA |
| RIG-I | cytoplasm | short double-stranded RNA, and RNA with a 5′-triphosphate |
| MDA5 | cytoplasm | long double-stranded RNA |
| cGAS | cytoplasm | double-stranded DNA of any sequence |

Each is a solution to the problem of telling foreign nucleic acid from the cell's own: by compartment (DNA in the cytosol is not supposed to be there), by chemistry (host mRNA is capped and its 5′-triphosphate is hidden) or by structure (long duplex RNA has no cellular counterpart).

Ligand binding starts a short signalling path. The RNA helicases signal through the mitochondrial adaptor MAVS, which polymerizes into a prion-like filament ([7.11.26](/7.11.26#sec-26.10)) that is the active form; cGAS makes the cyclic dinucleotide 2′3′-cGAMP, which binds the endoplasmic-reticulum adaptor STING; the Toll-like receptors signal through MyD88 or TRIF. All converge on the kinases that activate the transcription factors IRF3 and NF-κB, and these induce the interferons.

**Definition 27.4.2 (Interferon)** The **interferon**s are secreted cytokines induced by virus infection that render cells resistant to infection. Type I (IFN-α, IFN-β) acts on almost all nucleated cells; type III (IFN-λ) acts on epithelial cells of the airway and gut, where it provides a first, more local response; type II (IFN-γ) is a product of lymphocytes and belongs to [7.15](/7.15). Interferon was discovered in 1957 by Isaacs and Lindenmann as the activity, released by influenza-infected cells, that interfered with the growth of a second virus.

**Definition 27.4.3 (Interferon-Stimulated Gene)** An **interferon-stimulated gene** (ISG) is a gene transcribed in response to interferon. Several hundred are induced; their products include the sensors themselves (so the system amplifies), the restriction factors of §27.3, and effectors such as protein kinase R, which phosphorylates eIF2α and shuts down translation, and oligoadenylate synthetase with RNase L, which degrades cellular and viral RNA. The result is an *antiviral state* in the infected cell and in its uninfected neighbours before they are infected.

![Sensing of viral nucleic acid and the interferon response, with the points at which viruses intervene. Endosomal TLR3, TLR7/8 and TLR9 and the cytoplasmic sensors RIG-I, MDA5 and cGAS recognize viral RNA or DNA; signalling through MAVS, STING and the TLR adaptors activates IRF3 and NF-κB, which induce type I and type III interferon. Secreted interferon binds its receptors on the same and neighbouring cells, and JAK–STAT signalling induces several hundred interferon-stimulated genes, whose products establish the antiviral state. Red bars mark documented viral antagonists at each step: among them the Zika virus NS2B3 protease, which cleaves human STING, and influenza virus NS1, which sequesters double-stranded RNA and blocks RIG-I](./plots/interferon-response.py)

Every virus that replicates in a vertebrate antagonizes this system somewhere. Influenza virus NS1 binds double-stranded RNA and interferes with RIG-I activation; the Zika virus NS2B3 protease cleaves human STING; many viruses block the nuclear import of STAT proteins, degrade IRF3, or encode decoy receptors that mop up secreted interferon. Mapping these antagonists is in practice how the pathway was worked out, and the specificity is itself informative: the Zika protease cleaves human but not mouse STING, which is one reason the virus replicates poorly in ordinary mice.

**Remark 27.4.1** This machinery is old. cGAS-like receptors that sense RNA and trigger antiviral signalling have been found in *Drosophila*, and the cyclic-nucleotide signalling used by cGAS–STING is homologous to the bacterial CBASS systems of [7.11.23](/7.11.23#sec-23.8). A second ancient mechanism, RNA interference ([7.2.18](/7.2.18#sec-18.5)), is the principal antiviral defence of plants and invertebrates: viral double-stranded RNA is cut into siRNAs that guide cleavage of the viral genome, and plant and insect viruses encode suppressors of silencing in reply. Vertebrates retain the machinery but use it mainly for gene regulation, the interferon system having taken over the antiviral role.

## 27.5. Adaptive Immunity as a Selective Force

Adaptive immunity clears most acute infections and prevents most second ones. Two of its effectors matter for what follows: neutralizing antibodies, which bind the surface protein and prevent attachment or fusion, and cytotoxic T lymphocytes, which kill cells displaying viral peptides. Their mechanisms belong to [7.15](/7.15). What belongs here is the evolutionary consequence: these effectors are the strongest selection acting on viral surface proteins, and the ways viruses evade them are properties of the virus.

**Definition 27.5.1 (Antigenic Drift)** **Antigenic drift** is the gradual accumulation of amino acid substitutions in the antigenic sites of a viral surface protein, selected by the antibodies of a partly immune population. In influenza A virus it alters the haemagglutinin and neuraminidase continuously and is the reason the vaccine must be reformulated; it is the same process in the escape variants of HIV-1 within a single patient and in the SARS-CoV-2 variants that arose during the pandemic.

**Definition 27.5.2 (Antigenic Shift)** **Antigenic shift** is the abrupt appearance of a surface protein to which the human population has no immunity, produced in a segmented virus by reassortment ([7.11.24](/7.11.24#sec-24.2)) between a human and an animal strain in a coinfected host. Drift causes epidemics; shift causes pandemics.

![Antigenic drift and antigenic shift in influenza A virus. A: drift — point substitutions accumulate in the antigenic sites of the haemagglutinin head under antibody selection, so that the antigenic distance from a given vaccine strain grows year by year and strains that escape existing antibodies sweep through the population; the plot shows a simulated antigenic lineage with the characteristic ladder-like genealogy, successive variants replacing their predecessors. B: shift — a cell coinfected by a human and an avian virus can package any combination of the eight segments, and a reassortant carrying an avian haemagglutinin on an otherwise human-adapted background meets a population with no immunity. The 1957, 1968 and 2009 pandemic viruses arose by reassortment of this kind](./plots/drift-and-shift.py)

The other escape strategies are structural rather than sequence-based: latency, in which almost no viral protein is made and there is nothing for a T cell to see (herpesviruses); replication in sites that lymphocytes patrol poorly (neurons, the eye); glycan shields that cover the conserved parts of a surface protein (HIV-1 Env); direct infection and destruction of immune cells (HIV-1, measles virus); and virus-encoded proteins that interfere with antigen presentation or with the complement cascade.

## 27.6. Patterns of Infection and Within-Host Dynamics

Infections of an individual fall into a small number of patterns, distinguished by the time course of virus production and by whether the genome persists.

| Pattern | Virus production | Examples |
|---|---|---|
| Acute | a burst, cleared in days to weeks | rhinovirus, rotavirus, influenza virus |
| Persistent (chronic) | continuous, often lifelong, at variable titre | hepatitis B and C viruses, HIV-1, LCMV |
| Latent | an initial acute phase, then none, with episodic reactivation | herpes simplex virus, varicella-zoster virus |
| Slow | a long symptom-free interval, then progressive disease | measles virus in SSPE, HIV-1 untreated |
| Abortive | none: the cell is not permissive or the genome is defective | many encounters, by far the commonest outcome |
| Transforming | little or none; the cell is altered instead | HPV, EBV in some cells |

The incubation period — the interval from infection to the first symptoms — follows from the pattern and the route: one to three days for influenza and rhinovirus, which replicate at the point of entry; one to three weeks for infections that must disseminate, such as measles (9–12 days) and smallpox (12–14 days); one to five months for hepatitis B and for rabies, where the journey along the nerve is slow.

These time courses can be modelled, and the model is the basis of modern clinical virology.

**Formula 27.6.1 (The Target-Cell Model)** Let $T$ be the number of uninfected target cells, $I$ the number of productively infected cells and $V$ the concentration of free virus. Target cells are produced at rate $\lambda$ and die at rate $d$; infection occurs by mass action with rate constant $\beta$; infected cells die at rate $\delta$ and release virus at rate $p$ per cell; free virions are cleared at rate $c$:

$$
\begin{aligned}
\frac{\mathrm{d}T}{\mathrm{d}t} &= \lambda - dT - \beta V T, \\
\frac{\mathrm{d}I}{\mathrm{d}t} &= \beta V T - \delta I, \\
\frac{\mathrm{d}V}{\mathrm{d}t} &= pI - cV.
\end{aligned}
$$

With $T_0 = \lambda/d$ uninfected cells at the start, the **basic reproduction number** within the host is

$$
R_0 = \frac{\beta p T_0}{\delta c}, \tag{27.1}
$$

the number of newly infected cells produced by one infected cell in an otherwise uninfected tissue. Infection spreads if $R_0 > 1$; at steady state the fraction of target cells remaining is $1/R_0$.

**Remark 27.6.1** This $R_0$ counts infected *cells* within one host and must not be confused with the epidemiological $R_0$, which counts infected *people* ([7.11.35](/7.11.35), [1.4.7](/1.4.7)). The two are formally identical and numerically unrelated.

![Patterns of infection and the target-cell model. A: the four classical time courses of virus production in a host — acute, latent with reactivation, persistent and slow — with the period of symptoms shaded. B: the model of Formula 27.6.1 simulated with parameters for an acute infection: target cells are depleted, the virus peaks when $T$ falls to $T_0/R_0$, and the infection resolves; raising the clearance rate of infected cells or lowering $\beta$ below the threshold $R_0 = 1$ prevents takeoff. C: the decay of plasma virus when replication is blocked completely by drug at $t = 0$. The first, steep phase has the rate of loss of productively infected cells ($\delta$) and the clearance of free virions ($c$); fitting it to patient data gave the half-life of an HIV-1-infected cell as about one day and of a virion as hours, from which the production of $10^{10}$ virions per day follows — the measurement that changed the understanding of the asymptomatic phase](./plots/within-host-dynamics.py)

**Example 27.6.1** The perturbation experiment in panel C of the figure is the classical one. Before 1995 the long asymptomatic phase of HIV-1 infection was read as a period of viral quiescence. When potent protease inhibitors were given, plasma virus fell by two orders of magnitude with a half-life of about two days, which can only mean that the pre-treatment steady state was a balance between enormous production and equally rapid destruction. The same analysis applied to hepatitis B and C virus gave production rates of $10^{11}$–$10^{12}$ virions per day. A high turnover with an error-prone polymerase is exactly the condition under which resistance to a single drug is certain ([7.11.28](/7.11.28)).

## 27.7. How Viruses Cause Disease

There are three mechanisms, and in most diseases more than one operates.

1. *Killing of infected cells.* Lysis, apoptosis induced by the infection, or the shutoff of host transcription and translation. Poliovirus kills motor neurons; rotavirus destroys the absorptive cells of the small intestine; the symptoms follow from the function of the cells that are lost.
2. *Immunopathology.* The response, not the virus, does the damage. In mice infected intracerebrally with lymphocytic choriomeningitis virus, the virus itself is not cytopathic: animals lacking CD8⁺ T cells survive the infection, and those with an intact response die of the T-cell attack on infected meninges. In humans, much of the lung injury in severe influenza and COVID-19 is inflammatory, and in the most severe cases a dysregulated systemic release of cytokines, with fever, vascular leak and organ failure, produces the picture called a *cytokine storm*. Liver damage in hepatitis B is almost entirely immune-mediated.
3. *Transformation.* The cell is not killed but is changed: it continues to divide (§27.8).

**Definition 27.7.1 (Antibody-Dependent Enhancement)** **Antibody-dependent enhancement** (ADE) is the aggravation of an infection by antibodies that bind the virus without neutralizing it. The complex is taken up through Fc receptors into monocytes and macrophages, cells in which the virus can replicate, so that non-neutralizing or sub-neutralizing antibody raises rather than lowers the number of infected cells. The best-established case is dengue: infection with one of the four serotypes protects against that serotype but leaves cross-reactive, non-neutralizing antibody against the others, and severe dengue is much more likely in a second infection with a different serotype. It is the central difficulty in dengue vaccine development, and the reason every new vaccine against a flavivirus or a coronavirus is examined for it.

Severity also has specific molecular determinants. The Zika virus strains responsible for the Americas outbreak belong to the Asian lineage, and a single substitution in the precursor membrane protein, S139N, which arose in that lineage before the outbreak, increases replication in human neural progenitor cells and neurovirulence in neonatal mice — an example of how a small sequence change can alter the disease a virus causes without changing the way it spreads.

## 27.8. Viruses and Cancer

Roughly one in eight human cancers worldwide is attributable to infection, and most of that burden is viral. Seven human viruses are accepted as oncogenic: human papillomaviruses (cervical and other anogenital cancers, a growing fraction of oropharyngeal cancer), Epstein–Barr virus (Burkitt and other lymphomas, nasopharyngeal carcinoma), hepatitis B and hepatitis C viruses (hepatocellular carcinoma), human T-lymphotropic virus 1 (adult T-cell leukaemia), Kaposi sarcoma herpesvirus and Merkel cell polyomavirus.

Three routes lead from infection to tumour, and the cell-biological and genetic consequences are those of [7.3.26](/7.3.26) and [7.4.21](/7.4.21), which are not repeated here.

- *Direct action of viral oncoproteins.* The small DNA tumour viruses carry proteins whose normal job is to keep a differentiating cell in a replication-competent state: HPV E7 binds Rb and E6 directs the degradation of p53 ([7.11.24](/7.11.24#sec-24.4)). In a cell where the viral genome has integrated and lost the E2 repressor, these proteins are overexpressed and the two main tumour suppressor pathways are disabled at once.
- *Insertional and transcriptional activation.* HTLV-1 Tax activates host transcription broadly; some retroviruses integrate beside a proto-oncogene and activate it from the LTR promoter.
- *Chronic inflammation and regeneration.* Hepatitis B and C cause decades of hepatocyte death and division, with the mutational consequences of sustained proliferation. Hepatitis B also integrates fragments of its genome, and hepatitis C encodes no oncoprotein at all yet causes cancer — evidence that the indirect route is sufficient.

In every case the virus is necessary but not sufficient: the cancers appear in a small minority of those infected, decades after infection, and require additional somatic mutations. The practical consequence is large, because an infection can be prevented: vaccination against HPV and hepatitis B, and cure of hepatitis C, each prevent a cancer ([7.11.28](/7.11.28)).

## 27.9. Emergence

A **zoonosis** is an infection transmissible from animals to humans, and most new human viruses are zoonotic. Emergence is not a single event but a sequence of barriers, each of which must be crossed.

1. *Contact.* The reservoir host and people must meet, often through agriculture, bushmeat hunting, live-animal markets, deforestation or the trade in exotic animals, and sometimes through an intermediate amplifying host.
2. *Infection of a human cell.* The virus must use a receptor present in humans, or acquire the ability to; the receptor is usually the first barrier and often the main one. Beyond entry there are the restriction factors of §27.3, which are frequently species-specific — a major part of what makes a virus "adapted" to one host.
3. *Replication and shedding sufficient for transmission.* Many spillovers are dead ends: the person is infected, may become severely ill, and infects no one else (rabies, most avian influenza infections, Nipah in most settings).
4. *Sustained human-to-human transmission*, which requires an effective reproduction number above one in human populations.

The sources of variation that let a virus cross these barriers are the ordinary ones of [7.11.25](/7.11.25): point mutation at the high rates of RNA viruses, recombination, and reassortment in segmented viruses. Canine parvovirus arose from a feline virus by two substitutions in the capsid that changed the receptor specificity; the pandemic influenza viruses of 1957, 1968 and 2009 were reassortants; HIV-1 group M derives from a simian immunodeficiency virus of chimpanzees in central Africa, which entered humans in the early twentieth century, as the molecular clock applied to archival sequences shows ([7.10.24](/7.10.24)), and spread with twentieth-century urbanization and medical practice; SARS-CoV-2 is a betacoronavirus most closely related to bat viruses, of the lineage that had already produced SARS-CoV in 2002 and, from a different branch, MERS-CoV in camels in 2012.

**Remark 27.9.1** Surveillance now works on genomes. Metagenomic sequencing identifies an unknown agent from a clinical sample without a hypothesis ([7.8.14](/7.8.14#sec-14.6.1)), phylogenetics assigns lineages and reconstructs transmission chains, and the molecular clock dates the common ancestor of an outbreak ([7.10.24](/7.10.24)). SARS-CoV-2 was identified and its genome released within weeks of the first cases, and the design of the first vaccines began from that sequence alone ([7.11.28](/7.11.28)) — which is the clearest illustration of why genomic surveillance is treated as public-health infrastructure. The epidemiological side of this — transmission, incidence, case definitions, outbreak investigation — is [7.11.35](/7.11.35).

## Summary

- The outcome of an infection is set by the virus, the cell and the immune response together. An infection requires enough particles, cells that are both susceptible and permissive, and defences that are absent or slow; most encounters fail and most infections are subclinical.
- **Host range** and **tropism** follow from the receptor and from every later step: NTCP for hepatitis B virus, ACE2 with TMPRSS2 for SARS-CoV-2, CD4 with CCR5 for HIV-1 (Remark 27.2.1). Spread within the host is haematogenous, in two stages of viraemia, or neural by axonal transport.
- **Restriction factors** (Definition 27.3.1) are constitutive host blocks — APOBEC3G, tetherin, TRIM5α, SAMHD1, Mx, IFITM, LY6E — each with a viral antagonist; the pairs evolve under recurrent positive selection (Remark 27.3.1).
- **Pattern recognition receptors** (Definition 27.4.1) detect viral nucleic acid by compartment, chemistry or structure (TLR3/7/8/9, RIG-I, MDA5, cGAS) and induce **interferon** (Definition 27.4.2), whose **interferon-stimulated genes** (Definition 27.4.3) establish the antiviral state. Every vertebrate virus antagonizes some step. The system is ancient, and RNA interference serves the same role in plants and invertebrates (Remark 27.4.1).
- Adaptive immunity acts mainly as selection: **antigenic drift** (Definition 27.5.1) drives the seasonal reformulation of influenza vaccines, **antigenic shift** (Definition 27.5.2) produces pandemics, and latency, immune-privileged sites and glycan shields provide structural escape.
- Infections are acute, persistent, latent, slow, abortive or transforming. The target-cell model (Formula 27.6.1) gives the within-host $R_0 = \beta p T_0/(\delta c)$ and, through perturbation by drug, the measurement of viral turnover (Example 27.6.1).
- Disease arises from cell killing, from immunopathology — including **antibody-dependent enhancement** (Definition 27.7.1) in dengue — or from transformation; about one in eight cancers worldwide is attributable to infection, and seven human viruses are accepted as oncogenic.
- Emergence requires contact, entry into a human cell, replication sufficient for shedding, and sustained human-to-human transmission; mutation, recombination and reassortment supply the variation, and genomic surveillance is how emergence is now detected.

## Questions

1. A virus binds its receptor on a cell line, enters and uncoats, but no progeny are made. What distinguishes the possible explanations, and how would you test them?

   **Answer** The cell is susceptible but not permissive. Either a required host factor is missing — a transcription factor, a protease, a nucleotide pool — or an intrinsic block is acting. Testing: assay the viral replication intermediates to locate the step that fails; complement by expressing candidate host factors; knock out or deplete candidate restriction factors (or pre-treat with and without interferon: if interferon deepens the block and a knockout relieves it, a restriction factor is responsible); transfect the naked genome, which bypasses entry and uncoating and tells you whether the block is before or after them.

2. Why is the cytosol a good place to put a DNA sensor, and the endosome a good place to put an RNA sensor?

   **Answer** Discrimination of self from non-self is by location and context. The cell's own DNA is in the nucleus and the mitochondria, so double-stranded DNA free in the cytosol is a reliable sign of infection (or of damage) regardless of its sequence, which is why cGAS can be sequence-independent. The endosome receives material taken up from outside, including the nucleic acids of ingested or entering microbes, and host RNA is not normally delivered there; placing TLR3, TLR7/8 and TLR9 in that compartment restricts them to foreign material without requiring them to read a sequence. The remaining cytoplasmic RNA sensors must discriminate chemically instead — RIG-I recognizes the 5′-triphosphate that host capping hides, MDA5 the long duplexes that cells do not make.

3. Using Formula 27.6.1, show that at steady state the number of uninfected target cells is $T^* = T_0/R_0$, and interpret the result.

   **Answer** Setting $\mathrm{d}I/\mathrm{d}t = 0$ gives $\beta V T = \delta I$, and $\mathrm{d}V/\mathrm{d}t = 0$ gives $V = pI/c$. Substituting, $\beta (pI/c) T = \delta I$, so for $I \neq 0$, $T^* = \delta c/(\beta p)$. With $R_0 = \beta p T_0/(\delta c)$ this is $T^* = T_0/R_0$. The interpretation is the same as in epidemiology: the infection depletes susceptible cells until each infected cell infects exactly one more, that is, until the effective reproduction number is 1. A therapy that reduces $\beta$ or $p$ by a factor $f$ reduces $R_0$ by the same factor and, if it brings $R_0$ below 1, eliminates the infection rather than merely suppressing it.

4. Antigenic drift and the escape of HIV-1 from neutralizing antibodies within one patient are the same process on different scales. What does each imply for vaccine design?

   **Answer** Both are antibody-driven selection on a surface protein with a high mutation supply. For influenza, drift occurs between hosts and is global and relatively slow, so a vaccine can track it if strains are chosen frequently; the long-term aim is an immunogen directed at the conserved stalk, which drifts less because it is less accessible. For HIV-1, escape occurs within each patient within weeks, so no fixed Env sequence can be protective; useful immunogens must elicit broadly neutralizing antibodies against the conserved, glycan-shielded sites that the virus cannot change without losing function. In both cases the design target is the part of the protein that selection cannot move.

5. A new virus is isolated from a patient infected by an animal. Which properties would you measure to judge whether it can spread between people?

   **Answer** Which human receptor it uses and where that receptor is expressed — a receptor on upper-airway epithelium favours transmission, one reached only through the blood or deep lung does not; whether the virus replicates efficiently at the temperature and pH of the upper airway; whether it is shed in respiratory secretions, faeces or only in blood, and for how long; whether it is restricted by human intrinsic factors and whether it antagonizes human interferon signalling; the serial interval and secondary attack rate among the patient's contacts; and, phylogenetically, whether sequences from separate cases form a transmission chain or independent spillovers. Such assessment is done on isolates and sequences as they occur; experiments designed to make a virus more transmissible are not part of it, and are restricted on biosafety grounds ([7.11.10](/7.11.10)).
