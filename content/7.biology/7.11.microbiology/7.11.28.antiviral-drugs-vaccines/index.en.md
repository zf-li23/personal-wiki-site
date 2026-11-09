---
title: Antiviral Drugs and Vaccines
description: Why antiviral chemotherapy is harder than antibacterial chemotherapy; how antiviral compounds are found; the drug targets along the replication cycle and the chemistry of nucleoside analogues; resistance and combination therapy; the HIV and hepatitis C success stories; vaccine platforms from inactivated virus to mRNA; adjuvants, trials and correlates of protection; herd immunity and eradication; and passive immunization with monoclonal antibodies.
---

Two kinds of intervention follow from the biology of the preceding chapters. A drug attacks a step of the replication cycle in a person already infected; a vaccine prepares the immune system before infection. Both are applications of molecular virology, and both are limited by the same property of viruses that makes them interesting: they use the machinery of the host cell, and they evolve fast.

This chapter treats the virological side. The immunological mechanisms by which a vaccine protects belong to [7.15](/7.15); the statistics of the trials that evaluate them belong to [7.7.18](/7.7.18); antibacterial chemotherapy and bacterial resistance, with which the comparisons here are drawn, are [7.11.14](/7.11.14) and [7.11.15](/7.11.15).

## 28.1. Why Antiviral Chemotherapy Is Difficult

**Definition 28.1.1 (Antiviral Drug)** An **antiviral drug** is a compound that inhibits a step of viral replication at concentrations that the host tolerates. As with antibacterial agents, the requirement is selective toxicity ([7.11.14](/7.11.14)) — a difference between the target in the pathogen and anything comparable in the host — but for viruses that difference is harder to find.

Four difficulties follow from the biology.

- *The target list is short.* A bacterium has a cell wall, its own ribosome, its own folate pathway and its own DNA gyrase. A virus has only the few proteins its genome encodes, and uses the host's ribosomes, membranes and metabolism for everything else. The viral enzymes that exist — polymerases, proteases, integrases, neuraminidases — are therefore almost the whole target list.
- *Replication is finished before the diagnosis.* In an acute respiratory infection the virus peaks within two or three days, often before the patient presents; a drug given after the peak has little left to inhibit. This is why antivirals have succeeded first against chronic infections (HIV, hepatitis B and C, herpesviruses), where there is always replication to block.
- *The spectrum is narrow.* An antibacterial drug may cover dozens of genera; an antiviral drug usually works on one family, because the target enzymes differ. There is no antiviral equivalent of a broad-spectrum antibiotic.
- *Resistance is certain.* The populations are enormous and the polymerases are error-prone ([7.11.25](/7.11.25#sec-25.2)), so every single-nucleotide change pre-exists somewhere in the population before treatment begins (§28.4).

**Remark 28.1.1** Potency therefore matters more than for antibacterial agents. If an inhibitor leaves even a few percent of replication intact, that replication is the source of the resistant mutants that will end the treatment; a drug that suppresses replication completely creates no mutants at all, because mutations arise only when a genome is copied.

## 28.2. Finding an Antiviral Compound

Three approaches are used, usually together.

- *Cell-based screening.* A library of compounds is tested for inhibition of virus growth in culture, which selects for compounds that are active, enter cells and are not grossly toxic, without any hypothesis about the target. The target is then identified by selecting resistant virus and sequencing it: the substitution that confers resistance usually lies in the protein the drug binds.
- *Mechanism-based screening.* A purified viral enzyme is assayed directly, which gives clean structure–activity relationships but no guarantee that the hit works in a cell.
- *Structure-based design.* The structure of the target with a substrate or an inhibitor is used to design a molecule that fits the active site. The HIV protease inhibitors are the standard example: they are *peptidomimetics*, designed from the Phe–Pro cleavage site of the Gag–Pol polyprotein, which no cellular protease cuts.

**Example 28.2.1 (The replicon system)** Hepatitis C virus could not be grown in culture for a decade after its discovery in 1989, which blocked drug development entirely. The way round was the **replicon**: a self-replicating subgenomic RNA, carrying the non-structural proteins and a selectable marker but no structural genes, maintained in a hepatoma cell line. It makes no virions, so it is not infectious, but it reproduces the replication machinery faithfully, and a cell line carrying it reports inhibition of that machinery as loss of the marker. Every class of direct-acting anti-HCV drug was found or optimized in this system.

:::

The subsequent path is the ordinary one of drug development: pharmacokinetics and toxicology in animals, then phase I (safety and dose in a small number of volunteers), phase II (dose-finding and preliminary efficacy), phase III (randomized trials powered for clinical endpoints) and phase IV (surveillance after licensing); the designs and the statistics are in [7.7.18](/7.7.18). Attrition is severe and is dominated by toxicity rather than by lack of potency, and five to ten years typically pass between a promising compound and a licensed drug.

## 28.3. Targets along the Replication Cycle

![Antiviral drug classes placed on the replication cycle. Attachment and entry: the CCR5 antagonist maraviroc (a host-directed drug) and the fusion inhibitor enfuvirtide, a peptide copying the second heptad repeat of HIV-1 gp41. Uncoating: amantadine, which blocks the influenza A M2 proton channel. Genome replication: nucleoside and nucleotide analogues (acyclovir, zidovudine, tenofovir, sofosbuvir, remdesivir) and the non-nucleoside inhibitors of HIV-1 reverse transcriptase, which bind an allosteric pocket; the cap-snatching endonuclease inhibitor baloxavir acts here for influenza. Integration: the strand-transfer inhibitors raltegravir and dolutegravir, which chelate the two active-site magnesium ions. Polyprotein processing: the protease inhibitors of HIV-1, HCV and SARS-CoV-2. Release: the neuraminidase inhibitors oseltamivir and zanamivir. Host-directed options and interferon act across several steps](./plots/antiviral-targets.py)

The largest and oldest class attacks genome replication.

**Definition 28.3.1 (Nucleoside Analogue)** A **nucleoside analogue** is a drug resembling a natural nucleoside that is phosphorylated inside the cell to the triphosphate and then accepted by a viral polymerase. Most lack the 3′-hydroxyl needed for the next phosphodiester bond and therefore terminate the chain; nucleotide analogues (more exactly nucleoside monophosphate prodrugs, such as tenofovir and sofosbuvir) carry a masked phosphate group and so bypass the first, often rate-limiting, phosphorylation.

Selectivity can be obtained at either of two steps: activation or incorporation.

```smiles
NC1=NC(=O)c2ncn(COCCO)c2N1 1
NC1=NC(=O)c2ncn([C@@H]3O[C@H](CO)[C@@H](O)C3)c2N1 2
CC1=CN([C@H]2C[C@H](N=[N+]=[N-])[C@@H](CO)O2)C(=O)NC1=O 3
```

**Example 28.3.1 (Acyclovir)** Acyclovir (1) is 2′-deoxyguanosine (2) with the sugar replaced by an acyclic side chain that lacks the 2′ and 3′ carbons. Cellular kinases phosphorylate it very poorly; the thymidine kinase of herpes simplex virus phosphorylates it efficiently. The monophosphate is then converted to the triphosphate by cellular enzymes, and the viral DNA polymerase incorporates it in preference to dGTP, after which no further nucleotide can be added because there is no 3′-OH. Selectivity therefore comes twice over — activation only in infected cells, incorporation preferentially by the viral enzyme — which is why acyclovir is one of the least toxic antiviral drugs. Resistance arises mostly by loss of the viral thymidine kinase, and such mutants are correspondingly less virulent.

![The selectivity of acyclovir, and the general shape of nucleoside-analogue action. A: the activation pathway. Acyclovir is a poor substrate for cellular kinases, so in an uninfected cell it remains unphosphorylated and inert; the herpesvirus thymidine kinase makes the monophosphate, cellular kinases complete the triphosphate, and the viral DNA polymerase incorporates it and stops. B: the consequence, as a simple competition model — the probability that a growing chain is terminated as a function of the ratio of analogue triphosphate to dGTP, for a viral polymerase that discriminates weakly against the analogue and a cellular polymerase that discriminates strongly. The therapeutic window is the range of concentrations in which viral synthesis is terminated and host synthesis is not. C: the three ways a nucleoside analogue can act — obligate chain termination (acyclovir, zidovudine), non-obligate termination and competitive inhibition (sofosbuvir, remdesivir, which stop synthesis a few nucleotides later), and lethal mutagenesis (ribavirin, molnupiravir), which raises the error rate beyond the error threshold](./plots/nucleoside-analogues.py)

:::

Zidovudine (3, AZT) is the same logic without the first layer: it is activated by cellular kinases in every cell, and selectivity rests only on preferential incorporation by reverse transcriptase, which is why its toxicity is appreciable. The non-nucleoside reverse transcriptase inhibitors (nevirapine, efavirenz, rilpivirine) are chemically unrelated to nucleotides and bind an allosteric pocket present only in HIV-1 reverse transcriptase, so their selectivity is absolute but their barrier to resistance is low: one substitution in the pocket abolishes binding.

The other classes are:

| Class | Target | Examples |
|---|---|---|
| Entry and fusion inhibitors | the viral envelope protein, or its cellular receptor | enfuvirtide (gp41), maraviroc (CCR5) |
| Uncoating inhibitors | the M2 proton channel | amantadine, rimantadine (now of historical interest: resistance is near-universal in circulating influenza A) |
| Polymerase inhibitors | the viral polymerase | acyclovir, tenofovir, sofosbuvir, remdesivir; baloxavir, against the cap-snatching endonuclease |
| Integrase strand-transfer inhibitors | the integrase active site | raltegravir, dolutegravir, bictegravir |
| Protease inhibitors | the viral protease | darunavir (HIV-1), glecaprevir (HCV), nirmatrelvir (SARS-CoV-2 M<sup>pro</sup>, given with ritonavir to inhibit its metabolism) |
| Neuraminidase inhibitors | the viral neuraminidase, by mimicking the transition state of sialic acid cleavage | oseltamivir, zanamivir |
| Host-directed agents and interferon | a cellular factor the virus requires | maraviroc; pegylated interferon-α, now largely superseded |

**Remark 28.3.1** A host-directed drug has a high barrier to resistance, because the virus cannot mutate the host protein, but it necessarily interferes with a cellular function and so is more likely to be toxic. The two strategies trade resistance against toxicity, and which is preferable depends on how long the drug must be given.

## 28.4. Resistance and Combination Therapy

The argument is arithmetical. An untreated HIV-1 infection produces of the order of $10^{10}$ virions a day ([7.11.27](/7.11.27#sec-27.6)) with a mutation rate near $3 \times 10^{-5}$ per base per cycle and a genome of $10^4$ bases. Every possible single substitution is therefore generated up to about $10^{10} \times 3 \times 10^{-5} / 3 = 10^5$ times a day (fewer, but still many thousands, if only a minority of the virions go on to infect cells), and a single-drug regimen selects a pre-existing resistant variant within weeks. Two drugs are better, but the required double mutant also pre-exists if each single mutation is common. With $n$ independent mutations needed, the probability of a genome carrying all of them falls as the product of the individual frequencies, and three drugs put that product below the number of genomes present.

![Why monotherapy fails and combination therapy works. A: the expected number of genomes in an untreated HIV-1 population that already carry all of the substitutions needed for resistance, against the number required, for mutation frequencies of $10^{-4}$ to $10^{-5}$ per site per replication and a population of $10^{10}$ infected cells. One or two mutations pre-exist with near certainty; three or four do not. B: a stochastic simulation of viral load under monotherapy and under a three-drug combination, with resistant subpopulations arising by mutation. Monotherapy suppresses the load for a few weeks and is then overtaken by the resistant variant; the combination holds it below the limit of detection, and failure occurs only if adherence lapses, which allows residual replication and therefore new mutants. C: the same point as a threshold — the residual fraction of replication left by a regimen determines how quickly resistance appears](./plots/resistance-and-combination.py)

Hence the rules of practice: combine drugs with different targets; prefer drugs with a high genetic barrier, meaning those for which resistance requires several substitutions or costs the virus fitness; and insist on adherence, since a partially suppressive drug concentration is worse than none in evolutionary terms. Resistance patterns also interact in ways that can be exploited — some substitutions that confer resistance to one reverse transcriptase inhibitor restore susceptibility to another, so particular combinations constrain the virus more than the sum of their parts.

## 28.5. Two Success Stories

*HIV-1.* Combination antiretroviral therapy, from 1996, typically two nucleos(t)ide analogues with an integrase inhibitor or a non-nucleoside inhibitor, suppresses plasma virus below the limit of detection indefinitely and restores near-normal life expectancy. It does not cure: the provirus persists in long-lived resting memory CD4⁺ T cells, and virus rebounds within weeks if treatment stops. Suppression also prevents transmission, so treatment is prevention, and the same drugs taken before exposure (pre-exposure prophylaxis) prevent infection in people at risk. Strategies aimed at cure — reactivating latent proviruses so that the cells can be cleared, or excising the provirus — remain experimental; the handful of reported cures followed bone-marrow transplantation for a hematological malignancy, in most cases from a *CCR5*-Δ32 donor, which is not a generalizable procedure.

*Hepatitis C virus.* HCV is curable, and the sequence of steps from 1989 to that cure is a compact illustration of the whole chapter: identification of the agent by molecular cloning, development of the replicon system to make the replication machinery assayable (Example 28.2.1), structure-based design of inhibitors of the NS3/4A protease, the NS5B polymerase and the NS5A protein, and combination of two or three direct-acting antivirals to raise the barrier to resistance. Sofosbuvir, a nucleotide prodrug targeting NS5B, was the key component. Modern regimens are taken for 8–12 weeks and cure — sustained virological response, meaning no detectable RNA months after the end of treatment — more than 95 % of patients, across genotypes. Cure is possible for HCV and not for HIV-1 or hepatitis B because HCV leaves no archived genome in the cell: there is no provirus and no covalently closed circular DNA ([7.11.25](/7.11.25#sec-25.7)), so when replication is stopped for long enough the infection is gone.

The remaining obstacles for HCV are not virological. Most infected people do not know they are infected; the launch price of the first regimens put them out of reach of most of the world, and access improved only through generic licensing and competition. Cure also does not confer immunity, so reinfection is possible, and there is still no vaccine (§28.9).

## 28.6. Vaccines: Principle and Platforms

**Definition 28.6.1 (Vaccine)** A **vaccine** is a preparation that induces protective immunity against a pathogen without causing the disease. Immunization is *active* when the host makes its own response, which takes days to weeks but leaves immunological memory, and *passive* when preformed antibody is transferred, which protects at once but temporarily (§28.10).

Vaccination exploits the fact that a second encounter with a pathogen is handled faster than the first. Its goal is to obtain that second-encounter response without paying the cost of the first, and the design problem is to present enough of the right antigen, in the right form and with enough danger signal, that the response generated is protective and durable.

| Platform | What is given | Examples | Properties |
|---|---|---|---|
| Live attenuated | a replicating virus whose virulence has been reduced | measles, mumps, rubella, varicella, yellow fever, oral polio, rotavirus | strong and durable response, humoral and cellular, often after one dose; contraindicated in immunodeficiency and pregnancy; needs a cold chain; can revert (OPV-derived polioviruses) |
| Inactivated | whole virus killed with formalin or β-propiolactone | hepatitis A, rabies, inactivated polio, many influenza vaccines | safe in the immunocompromised; no replication, so more antigen, adjuvant and boosters are needed; mostly antibody, little CD8 response |
| Subunit or recombinant protein | a purified protein | hepatitis B surface antigen, recombinant zoster glycoprotein E | defined composition, very safe; needs an adjuvant |
| Virus-like particle | capsid proteins self-assembled into a particle without a genome | HPV (L1), hepatitis B | particulate, repetitive display of epitopes gives strong B-cell responses; non-infectious |
| Polysaccharide and conjugate | a bacterial capsular polysaccharide, coupled to a carrier protein | pneumococcus, *Haemophilus influenzae* type b, meningococcus | conjugation to protein converts a T-independent antigen into one that gives memory and works in infants |
| Toxoid | an inactivated bacterial toxin | tetanus, diphtheria | immunity to the toxin rather than to the organism |
| Viral vector | a replication-defective or attenuated virus carrying the gene for the antigen | adenovirus-vectored COVID-19 vaccines, VSV-vectored Ebola vaccine | antigen is made inside the cell, so CD8 responses are induced; pre-existing immunity to the vector can blunt the response |
| Nucleic acid | mRNA in a lipid nanoparticle, or plasmid DNA | COVID-19 mRNA vaccines | the sequence is the product, so design and manufacture are fast and platform-generic |

**Definition 28.6.2 (Live Attenuated Vaccine)** A **live attenuated vaccine** contains a virus that replicates in the recipient but has lost the capacity to cause disease. Attenuation was classically obtained by serial passage in a foreign host or at low temperature, which selects variants adapted to the culture conditions and poorly adapted to the original host; it can now be designed, for example by recoding a genome to use rare codon pairs, or by disabling the virus's interferon antagonist so that it replicates only in cells with a defective interferon response.

**Definition 28.6.3 (Inactivated Vaccine)** An **inactivated vaccine** contains virus whose infectivity has been destroyed chemically or physically while its antigenic structure is preserved. The qualification matters: inactivation that denatures the surface protein destroys the epitopes that neutralizing antibodies recognize, and an early formalin-inactivated respiratory syncytial virus vaccine in the 1960s not only failed to protect but worsened subsequent disease, a precedent that shapes the safety assessment of every new vaccine against a respiratory virus.

**Definition 28.6.4 (Virus-Like Particle)** A **virus-like particle** (VLP) is a particle assembled from viral structural proteins that contains no genome and cannot replicate. The HPV vaccines consist of L1 protein expressed in yeast or in insect cells with a baculovirus vector ([7.11.26](/7.11.26#sec-26.8)), which self-assembles into capsids; the dense, ordered display of epitopes is far more immunogenic than the same protein in solution.

**Definition 28.6.5 (mRNA Vaccine)** An **mRNA vaccine** delivers a messenger RNA encoding the antigen, encapsulated in a lipid nanoparticle that protects it and mediates uptake and endosomal escape. The RNA is translated by the recipient's own cells, so the antigen is made in its native conformation and enters both the MHC class I and class II pathways. Two problems had to be solved: unmodified RNA is a potent ligand for the sensors of [7.11.27](/7.11.27#sec-27.4) and is both inflammatory and poorly translated, which was solved by replacing uridine with a modified nucleoside (N1-methylpseudouridine), the discovery for which Karikó and Weissman received the 2023 Nobel Prize in Physiology or Medicine; and the RNA had to be delivered, which the ionizable lipid nanoparticle achieves. The platform is generic: a new vaccine requires only a new sequence.

![Vaccine platforms, drawn against the step of the immune response each exploits. From left: inactivated whole virus and purified subunit protein, which are taken up by antigen-presenting cells and give mainly antibody; virus-like particles, whose repetitive surface cross-links B-cell receptors strongly; live attenuated virus and viral vectors, which replicate or at least express antigen inside cells and therefore also prime CD8 T cells; and mRNA in a lipid nanoparticle, which is translated by the recipient's cells so that the antigen is made in its native conformation. Below each, the properties that follow: the need for adjuvant and boosters, the cold chain, the contraindication in immunodeficiency, and the speed with which a new antigen can be substituted](./plots/vaccine-platforms.py)

## 28.7. Adjuvants, Schedules and Evaluation

*Adjuvants* are substances that increase the response to a co-administered antigen. The classical aluminum salts adsorb the antigen and provide a local inflammatory signal; newer adjuvants are deliberate agonists of the pattern recognition receptors of [7.11.27](/7.11.27#sec-27.4) — the TLR4 agonist monophosphoryl lipid A, the TLR9 agonist CpG 1018, and oil-in-water emulsions such as MF59 and AS01. Their function is to supply the second signal that a purified antigen does not carry, which is why inactivated and subunit vaccines need them and live vaccines do not: a replicating virus provides its own.

Evaluation follows the clinical trial sequence of [7.7.18](/7.7.18), with one definition particular to vaccines. *Vaccine efficacy* is the relative reduction in the incidence of disease in the vaccinated arm,

$$
\mathrm{VE} = 1 - \frac{I_{\mathrm{vaccinated}}}{I_{\mathrm{unvaccinated}}} = 1 - \mathrm{RR}, \tag{28.1}
$$

estimated in a randomized trial; *vaccine effectiveness* is the same quantity measured observationally after licensing, where confounding has to be handled ([7.7.15](/7.7.15)). Efficacy depends on the endpoint — against infection, against symptomatic disease, against severe disease — and these can differ by a great deal for the same vaccine, so the endpoint must always be stated.

A *correlate of protection* is a measurable immune response, usually a neutralizing antibody titer, that predicts protection well enough to license a vaccine without a new efficacy trial. Where one is established — as for hepatitis B, where an anti-HBs concentration above $10\,\mathrm{mIU\,ml^{-1}}$ suffices — it shortens development enormously; where protection depends on T cells or on mucosal immunity, no simple correlate exists and clinical endpoints are unavoidable.

## 28.8. Herd Immunity and Eradication

**Definition 28.8.1 (Herd Immunity)** **Herd immunity** is the protection of susceptible individuals that results from a sufficient fraction of the population being immune, so that an introduced infection does not spread. Let $R_0$ be the basic reproduction number ([1.4.7](/1.4.7)) and $p$ the immune fraction. Each infected person then produces on average $R = R_0(1 - p)$ secondary cases, so transmission dies out when $R < 1$, that is when

$$
p > p_{\mathrm{c}} = 1 - \frac{1}{R_0}. \tag{28.2}
$$

With measles at $R_0 \approx 12$–$18$ this requires 92–95 % immunity; for a virus with $R_0 \approx 3$ about two thirds. The social and evolutionary consequences of the same threshold are discussed in [7.10.34](/7.10.34).

![Herd immunity. A: the critical immune fraction $1 - 1/R_0$ (Eq. (28.2)), with the ranges estimated for measles, pertussis, polio, smallpox, seasonal influenza and the ancestral SARS-CoV-2 lineage marked; a highly transmissible pathogen leaves almost no room for non-immune individuals. B: an SIR simulation at several coverages, showing the epidemic flattening and then failing to start as coverage crosses the threshold, and the residual cases among the unvaccinated that occur below it. C: why coverage above the threshold matters even for the vaccinated — clustering. The same average coverage distributed unevenly leaves pockets in which the local reproduction number exceeds one, which is how measles outbreaks occur in highly vaccinated countries](./plots/herd-immunity.py)

Three conditions make a virus a candidate for *eradication*: humans must be the only reservoir, infection or vaccination must induce lasting immunity, and a practical diagnostic test and vaccine must exist. Smallpox met all three and was declared eradicated in 1980, the only human disease so far; the campaign relied as much on surveillance and ring vaccination as on mass immunization, because the long rash made cases easy to identify. Poliovirus meets the conditions and has been eliminated from most of the world, with wild type 1 remaining in two countries, but the oral vaccine's capacity to revert and circulate complicates the last stage, which is why the inactivated vaccine takes over at the end of a campaign. Measles meets the biological conditions but has the highest threshold of any human infection, so elimination is repeatedly lost when coverage falls.

## 28.9. What Vaccines Have Achieved, and Where They Fail

Vaccination has removed several of the commonest causes of childhood death. Measles deaths worldwide fell by close to 90 % between 2000 and 2024, from some 800 000 a year to under 100 000; hepatitis B vaccination, given at birth, has reduced chronic infection in vaccinated cohorts to below 1 % in countries where carriage was formerly 8–10 %, and with it the incidence of hepatocellular carcinoma — the first vaccine shown to prevent a human cancer. HPV vaccination has reduced infection with the targeted types by about 90 % in vaccinated cohorts and is already reducing the incidence of cervical precancer, with national programs aiming at elimination of cervical cancer as a public-health problem.

Two viruses have resisted vaccination for decades, and the reasons are instructive.

- *HIV-1.* The virus integrates within days, so sterilizing immunity is the only useful kind; the envelope protein is the most variable protein known, is covered in host-derived glycan, and presents its conserved surfaces only transiently during fusion; natural infection induces no protective immunity, so there is no model to imitate; and there is no animal model that reproduces the human disease. Broadly neutralizing antibodies that bind the conserved sites do exist in some patients, and the current approach is to design immunogens that elicit them, through sequences of immunogens that guide the maturation of the right B-cell lineages.
- *Hepatitis C virus.* High genetic variability, efficient evasion of innate and adaptive responses, the lack until recently of experimental systems, and the availability of a cure, which has reduced the incentive while leaving the epidemiological need.

**Example 28.9.1 (SARS-CoV-2)** The genome sequence was released in January 2020 and the first vaccine doses were given in trials within months, with efficacy results and emergency authorizations before the end of the year. Three things made this possible, and none of them was luck: the platform — mRNA and adenovirus vectors need only a sequence; the antigen — work on SARS-CoV and MERS-CoV had already shown that the spike is the target and that stabilizing it in its prefusion conformation with two proline substitutions greatly improves the response; and the conduct of trials in parallel with manufacture, at financial rather than scientific risk. The experience also showed the limits of the approach: immunity against infection wanes and the virus drifts (§[7.11.27](/7.11.27#sec-27.5)), so the vaccines are reformulated like those against influenza, while protection against severe disease has proved far more durable.

## 28.10. Passive Immunization and Monoclonal Antibodies

Transferring antibody protects immediately and without any contribution from the recipient's immune system, which makes it the only option after exposure to an agent with a short incubation period or in a patient who cannot respond. Classical preparations are pooled human immunoglobulin, and specific immune globulins against hepatitis B, varicella-zoster, rabies and tetanus; rabies post-exposure prophylaxis combines immune globulin infiltrated around the wound with a course of vaccine, and works because the virus takes weeks to reach the nervous system.

Monoclonal antibodies have replaced these where the target is known. Palivizumab and the longer-acting nirsevimab prevent severe respiratory syncytial virus disease in infants; monoclonal antibodies against the SARS-CoV-2 spike were used during the pandemic and lost activity one after another as the virus drifted — a direct demonstration, in the clinic, of the escape described in [7.11.27](/7.11.27#sec-27.5). Protection is transient, since the antibody is cleared in weeks, and it leaves no memory; passive immunization is therefore a treatment, not an immunization in the proper sense.

## Summary

- Antiviral chemotherapy is harder than antibacterial chemotherapy because viruses use host machinery, which leaves few selective targets; because acute infections peak before diagnosis; because the spectrum of each drug is narrow; and because resistance is certain in populations of $10^{10}$ with error-prone polymerases (Definition 28.1.1, Remark 28.1.1).
- Compounds are found by cell-based screening, mechanism-based assays and structure-based design, and the HCV **replicon** made the non-growable virus assayable (Example 28.2.1).
- Every step of the cycle has inhibitors: entry (enfuvirtide, maraviroc), uncoating (amantadine), genome replication (**nucleoside analogues**, Definition 28.3.1, and non-nucleoside inhibitors), integration (raltegravir, dolutegravir), polyprotein processing (darunavir, glecaprevir, nirmatrelvir) and release (oseltamivir). Acyclovir is selective twice over, at activation and at incorporation (Example 28.3.1).
- Monotherapy fails because single mutants pre-exist; combination therapy works because the probability of a genome carrying three or four specific substitutions is below the population size. High genetic barrier and adherence are the practical consequences.
- Antiretroviral therapy suppresses HIV-1 indefinitely but does not cure, because of the latent provirus; direct-acting antivirals cure more than 95 % of HCV infections, because that virus archives no genome in the cell.
- **Vaccines** (Definition 28.6.1) are given on eight platforms, from inactivated (Definition 28.6.3) and live attenuated (Definition 28.6.2) virus to **virus-like particles** (Definition 28.6.4), vectors and **mRNA** in lipid nanoparticles (Definition 28.6.5); adjuvants supply the innate signal that purified antigens lack.
- Efficacy is $\mathrm{VE} = 1 - \mathrm{RR}$ (Eq. (28.1)) for a stated endpoint; a correlate of protection, where one exists, replaces new efficacy trials.
- **Herd immunity** (Definition 28.8.1) requires an immune fraction above $1 - 1/R_0$ (Eq. (28.2)) — 92–95 % for measles. Eradication needs a single reservoir, lasting immunity and a practical vaccine and test; smallpox is the one success.
- Vaccines have prevented a cancer (hepatitis B, HPV) and eliminated several childhood diseases, while HIV-1 and HCV have resisted vaccination for reasons that follow from their biology (Example 28.9.1 contrasts the SARS-CoV-2 case).
- Passive immunization with immune globulin or monoclonal antibodies protects immediately but transiently, and monoclonals are themselves subject to viral escape.

## Questions

1. Why was it possible to make a safe and highly selective drug against herpes simplex virus (acyclovir) decades before equally selective drugs against most RNA viruses?

   **Answer** Acyclovir exploits a viral enzyme that has no close cellular equivalent in its substrate preference — the herpesvirus thymidine kinase, which phosphorylates the analogue efficiently while cellular kinases do not — so the drug is activated almost only in infected cells, and it is then incorporated preferentially by the viral DNA polymerase. Two independent layers of selectivity give a very wide therapeutic window. Most RNA viruses encode no such activating enzyme, so a nucleoside analogue against them is activated in every cell and selectivity rests on the polymerase alone.

2. A patient on a single antiviral drug has a viral load that falls by 99 % and then returns to its original level within eight weeks. Explain, and state what should have been done differently.

   **Answer** The drug suppressed replication but not completely. The residual replication both generated and selected a resistant variant, which was already present at low frequency before treatment because the population turns over $10^{10}$ genomes a day with a mutation rate of about $10^{-5}$ per base; once selected, it grows back to the original set point. The remedy is combination therapy with drugs of different targets, so that resistance requires several simultaneous substitutions, together with full adherence, which keeps the concentration above the level at which any replication is possible.

3. A vaccine shows 95 % efficacy against symptomatic disease and 60 % against infection. Can it still produce herd immunity against a pathogen with $R_0 = 5$?

   **Answer** Herd immunity depends on transmission, so the relevant figure is the effect on infection and onward transmission, not on symptoms. The threshold is $p_{\mathrm{c}} = 1 - 1/5 = 0.8$. If the vaccine prevents 60 % of infections, then even with 100 % coverage the effective immune fraction is 0.6, below 0.8, and transmission continues; the vaccine protects the individual against disease but does not stop circulation. Reaching the threshold would require either a higher efficacy against infection, an additional reduction in infectiousness in breakthrough infections (which should be measured separately), or measures beyond vaccination.

4. Both a nucleoside analogue that terminates chains and a mutagenic nucleoside act on the viral polymerase. Why do they fail in different ways, and what does each imply about dosing?

   **Answer** A chain terminator is a competitive, all-or-nothing block: resistance requires a polymerase that discriminates against it, which is a single step, and partial inhibition leaves a replicating population from which such mutants come. A mutagen works by pushing the population over the error threshold ([7.11.25](/7.11.25#sec-25.2)); partial dosing raises the mutation rate without extinguishing the population, which increases variation and may accelerate the appearance of resistance to other drugs, and raises the concern that variants emerging from treated patients may spread. A terminator should be dosed to suppress replication completely and combined with other drugs; a mutagen must be dosed high enough and long enough to cross the threshold, not merely to approach it.

5. Smallpox was eradicated; measles, with a vaccine that is at least as good, has not been. Why?

   **Answer** Both have a single human reservoir and both vaccines give lasting immunity, so the difference is quantitative. Measles has the higher $R_0$ (12–18 against about 5–7 for smallpox), so the required coverage is 92–95 % rather than roughly 80 %, and it must be sustained everywhere, in every birth cohort. Measles is also infectious before the rash appears and is transmitted by aerosol that persists in a room, so cases cannot be identified and contained the way smallpox cases could by their characteristic rash; ring vaccination, which was decisive against smallpox, is far less effective. Finally, the measles vaccine is given in two doses with the first after maternal antibody has waned, which leaves a susceptible window in infancy that smallpox vaccination did not have.
