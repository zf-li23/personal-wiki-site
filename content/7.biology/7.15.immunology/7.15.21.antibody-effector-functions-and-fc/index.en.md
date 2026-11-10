---
title: Antibody Effector Functions and Fc Receptors
description: "How antibodies clear antigen: neutralization that depends only on the Fab, and opsonization, complement activation, ADCC and mast cell activation that depend on the Fc; the activating and inhibitory members of the Fc receptor family; how pH-dependent recycling by the neonatal Fc receptor determines the half-life of IgG and the transfer of maternal antibody, and how the polymeric immunoglobulin receptor delivers IgA to mucosal surfaces."
source_hash: e5cba76020d6
---

This chapter answers the question "by which effectors is antigen cleared?" on the humoral side. The previous chapter ([7.15.20](/7.15.20)) described how B cells produce high-affinity, class-switched **antibody**; the structure of antibodies (the **Fab fragment** and **Fc fragment**, the five classes) is described in [7.15.9](/7.15.9). Antibody itself kills almost nothing: its Fab end provides specificity, and its Fc end "hands" this specificity over to other systems, namely **complement** ([7.15.10](/7.15.10)), innate immune cells carrying Fc receptors, and the transport receptors that carry antibody to the fetus and to mucosal surfaces. Almost all antibody effects can therefore be read in one sentence: the isotype determines the Fc, and the Fc determines who carries out the effect. The IgE receptor of mast cells is developed in [7.15.26](/7.15.26), and IgA in mucosa in [7.15.23](/7.15.23).

## 21.1. Fab and Fc: Two Kinds of Effects

![Five effector mechanisms of antibody. A: Neutralization: the Fab of the antibody binds the site on a virus or toxin that binds the host receptor, so that it cannot attach to or enter cells; this action does not require the Fc. B: Opsonization: IgG coating the surface of a pathogen binds, through its Fc, activating FcγRs (FcγRI, FcγRIIA) on macrophages and triggers phagocytosis and killing. C: Complement activation: several adjacent Fc regions on the target surface (an IgG hexamer, or a pentameric IgM that has bound antigen) bind C1q and start the classical pathway; C3b deposited on the surface acts as an opsonin and C5b–9 forms the membrane attack complex. D: ADCC: IgG bound to the surface of an infected cell or tumor cell is recognized by FcγRIIIA (CD16) on an NK cell, which releases perforin and granzymes and causes the target cell to undergo apoptosis. E: FcεRI on the surface of a mast cell has been preloaded with IgE; after multivalent antigen cross-links adjacent IgE molecules, the mast cell degranulates and releases mediators such as histamine](./plots/effector-functions.py)

| Effect | Part used | Main isotypes | Executor |
|---|---|---|---|
| Neutralization | Fab | High-affinity IgG, IgA (mucosal), IgM | The antibody itself |
| Agglutination | Fab, multivalent | IgM, dimeric IgA | The antibody itself (cleared afterward) |
| Opsonization and phagocytosis | Fc → FcγR, FcαR | IgG1, IgG3, IgA | Macrophages, neutrophils, monocytes, DCs |
| Complement activation | Fc → C1q | IgM, IgG3 > IgG1 > IgG2 | The complement system |
| ADCC | Fc → FcγRIIIA and others | IgG1, IgG3 (IgE and IgA also mediate killing by eosinophils and neutrophils) | Mainly NK cells |
| Activation of mast cells and basophils | Fc → FcεRI | IgE | Mast cells, basophils, (eosinophils) |
| Transplacental transport, extended half-life | Fc → FcRn | IgG | Syncytiotrophoblast, endothelial cells |
| Transepithelial transport | Fc and J chain → pIgR | Dimeric IgA, pentameric IgM | Mucosal and glandular epithelium |

The cross-linking principle. Almost all Fc-mediated effects require several antibodies to be aggregated on the same target. The serum IgG concentration is about $10\,\mathrm{g\,L^{-1}}$ (about $6 \times 10^{-5}\,\mathrm{M}$), far above the dissociation constant of the high-affinity receptor FcγRI, so FcγRI on monocytes is always occupied by free IgG; if a single antibody could trigger signaling, these cells would be activated continuously. In fact, Fc receptors or C1q are aggregated, and the signal is triggered, only when antibody binds at a certain density on the surface of a particle or cell and forms an **immune complex**. The antibody first "recognizes" the target, and the multivalent Fc array then "summons" the effectors; this guarantees the specificity of humoral immunity.

## 21.2. Neutralization

**Definition 21.2.1 (Neutralization)** The action by which an antibody binds a functional molecule on a virus, bacterium or toxin and blocks its binding to host cell receptors, membrane fusion or the steps that follow entry into the cell, so that the agent loses its infectivity or toxicity, is called **neutralization**. Antibodies that have this action are called neutralizing antibodies.

Neutralization requires only the Fab and is physiologically the most effective mechanism for preventing infection, because it acts before the pathogen enters the cell, causes no inflammation and needs no participation of other cells; for many vaccines, protection correlates best with the titer of neutralizing antibody ([7.15.33](/7.15.33)). The neutralized pathogen or toxin is then mostly cleared by phagocytes in the form of immune complexes.

The efficiency of neutralization is determined by two factors:

- Whether the antibody binds a functional epitope: only antibodies that bind the receptor-binding site, the fusion machinery or sites that lock its conformation can neutralize; antibodies that bind other epitopes may bind well yet not neutralize at all (although they can still mediate opsonization or ADCC through the Fc).
- The occupancy of binding: neutralization usually requires that a considerable fraction of the functional molecules on the surface of a particle be occupied by antibody. At an antibody concentration $[\mathrm{Ab}]$, the occupancy for monovalent binding is

  $$
  \theta = \frac{K_{\mathrm{A}}[\mathrm{Ab}]}{1 + K_{\mathrm{A}}[\mathrm{Ab}]},
  $$
  so the antibody concentration required to reach the same occupancy is inversely proportional to the **affinity** $K_{\mathrm{A}}$, which is the direct payoff of affinity maturation ([7.15.20](/7.15.20)); multivalent binding by IgG and IgM makes the effective binding constant (the **avidity**) several orders of magnitude higher than the monovalent affinity, which matters especially when the monovalent affinity is low.

The ways in which pathogens have evolved to escape neutralization (epitope variation, glycan shielding, conformational masking) are the theme of the arms race between humoral immunity and pathogens, discussed in [7.15.32](/7.15.32).

## 21.3. Opsonization and Complement Activation

**Opsonization** ([7.15.7](/7.15.7)) is the "labeling" of particles that makes them easier for phagocytes to engulf. Antibody and complement provide two sets of opsonic labels that reinforce each other:

- After IgG (especially human IgG1 and IgG3) coats a particle, its Fc is bound by activating FcγRs on macrophages and neutrophils, which triggers phagocytosis (also called antibody-dependent cellular phagocytosis, ADCP), the **respiratory burst** and secretion of inflammatory cytokines;
- Ingested antigen–antibody complexes are processed and presented in DCs, so antibody can also enhance T-cell responses.

Complement activation. Antibody is the initiator of the classical pathway: C1q in the C1 complex has six globular heads, the affinity of a single head for Fc is very low, and only simultaneous binding to two or more adjacent Fc regions allows stable binding and activation of C1r and C1s. Several rules follow:

- After a pentameric IgM binds to the surface of a particle, it changes from a planar conformation to a "staple" conformation and exposes several C1q-binding sites, so a single molecule can activate complement; free IgM cannot.
- IgG must bind at sufficient density on the antigen surface; adjacent IgG molecules arrange themselves into a hexameric ring through Fc–Fc interactions, matching the six heads of C1q, so complement activation by IgG depends on epitope density.
- The ability of the human IgG subclasses to activate complement is IgG3 > IgG1 > IgG2, and IgG4 essentially cannot; IgA, IgE and IgD do not activate complement through the classical pathway.

Earlier textbooks explained this by saying that "after the Fab binds antigen, the antibody changes conformation and exposes the complement-binding site on the Fc"; current structural evidence shows that the determining factor is aggregation of Fc regions and not a conformational change in a single molecule (the conformational transition of IgM is an exception, but it too serves to make several binding sites available at once). After complement is activated, the C3b and iC3b deposited on the surface are more effective opsonins than antibody, C5b–9 forms the membrane attack complex, and C3a and C5a recruit inflammatory cells ([7.15.10](/7.15.10)).

## 21.4. ADCC and Activation of Granulocytes

**Definition 21.4.1 (Antibody-Dependent Cell-Mediated Cytotoxicity)** The process in which the Fab of an antibody such as IgG binds an antigen on the surface of a target cell (an infected cell or tumor cell) and the Fc binds an activating Fc receptor on an effector cell, thereby triggering the effector cell to kill the target cell, is called **antibody-dependent cell-mediated cytotoxicity** (ADCC).

The main executors of ADCC are **natural killer cells**: the only Fc receptor expressed by NK cells is FcγRIIIA (CD16), which, when cross-linked with Fc, signals through an ITAM (supplied by the FcεRIγ chain or CD3ζ chain), and the NK cell releases **perforin** and **granzymes** in a directed way so that the target cell undergoes apoptosis (the killing mechanism of NK cells is described in [7.15.5](/7.15.5)). Macrophages and neutrophils through FcγR or FcαRI, and eosinophils through the receptors for IgE or IgA, can also kill antibody-coated targets that are too large to be phagocytosed (for example parasites). ADCC is one of the main mechanisms of action of many therapeutic monoclonal antibodies (such as anti-CD20 and anti-HER2 antibodies); removing the fucose from the N297 glycan on the IgG1 Fc raises its affinity for FcγRIIIA about 50-fold and markedly enhances ADCC, a common method of Fc engineering for antibody drugs.

**Definition 21.4.2 (FcεRI)** The receptor on the surface of mast cells and basophils (in humans also activated eosinophils and some DCs and monocytes) that binds the Fc of IgE with very high affinity is called **FcεRI**, also known as the high-affinity IgE receptor. On mast cells it is an $\alpha\beta\gamma_2$ tetramer composed of one α chain that binds IgE, one β chain with four transmembrane segments and two γ chains carrying ITAMs.

The dissociation constant of FcεRI for IgE is about $10^{-10}\,\mathrm{M}$, so the very small amount of IgE in serum (about $0.0003\,\mathrm{g\,L^{-1}}$ in adults, about one thirty-thousandth of IgG) can be bound on the surface of mast cells for a long time: free IgE has a serum half-life of only about 2 days, whereas IgE bound to mast cells can persist for weeks. The mast cell thus resembles a detector that has been "armed", carrying IgE of many specificities on its surface; after multivalent antigen cross-links adjacent IgE–FcεRI complexes, the cell degranulates within seconds to minutes, releasing histamine and proteases, and then synthesizes leukotrienes, prostaglandins and cytokines. Against parasites this is an effector of **type 2 immunity**; against harmless environmental antigens it is type I **hypersensitivity** ([7.15.26](/7.15.26)). The low-affinity IgE receptor FcεRII (CD23) is a C-type lectin, not a member of the immunoglobulin superfamily, and takes part in regulating IgE production.

## 21.5. The Fc Receptor Family

**Definition 21.5.1 (Fc Receptor)** A receptor that is expressed on the cell surface (or inside the cell) and binds specifically the Fc portion of one or several classes of immunoglobulin, thereby linking the specificity of antibody to the effector, regulatory or transport functions of the cell, is called an **Fc receptor** (FcR). Receptors are named according to the isotype they bind: FcγR binds IgG, FcεR binds IgE, FcαR binds IgA and FcμR binds IgM.

| Receptor | CD | Binds (human) | Affinity | Signaling | Main cells | Function |
|---|---|---|---|---|---|---|
| FcγRI | CD64 | IgG1, IgG3 | High (monomeric IgG can bind) | γ-chain ITAM | Monocytes, macrophages, DCs; activated neutrophils | Phagocytosis, respiratory burst, ADCC |
| FcγRIIA | CD32A | IgG (complexes) | Low | Own ITAM | Myeloid cells, platelets | Phagocytosis, degranulation |
| FcγRIIB | CD32B | IgG (complexes) | Low | ITIM (recruits SHIP) | B cells, myeloid cells, FDCs, liver sinusoidal endothelium | Inhibits activation of B cells and myeloid cells; FDCs retain immune complexes |
| FcγRIIIA | CD16a | IgG1, IgG3 | Low to intermediate | γ-chain or ζ-chain ITAM | NK cells, macrophages, monocyte subsets | ADCC, cytokine secretion |
| FcγRIIIB | CD16b | IgG1, IgG3 | Low | GPI-anchored, no ITAM | Neutrophils | Cooperates with FcγRIIA to capture immune complexes |
| FcεRI | — | IgE | Very high | β-chain, γ-chain ITAMs | Mast cells, basophils | Degranulation |
| FcεRII | CD23 | IgE | Low | C-type lectin | B cells, FDCs | Regulates IgE production, transports IgE complexes |
| FcαRI | CD89 | IgA | Intermediate | γ-chain ITAM | Neutrophils, monocytes, macrophages | Phagocytosis, ADCC; transmits an inhibitory signal when monomeric IgA binds |
| Fcα/μR | CD351 | IgM, IgA | High (IgM) | — | B cells, macrophages, FDCs | Endocytosis of IgM complexes |
| FcμR | — | IgM | High | — | B, T, NK cells | Regulates lymphocyte activation |
| pIgR | — | Dimeric IgA, pentameric IgM (requires J chain) | — | Transport | Mucosal and glandular epithelium | Transepithelial transport (§21.7) |
| FcRn | — | IgG, albumin | pH-dependent | Transport | Endothelium, syncytiotrophoblast, epithelium, myeloid cells | Recycling, transplacental transport (§21.6) |
| TRIM21 | — | IgG, IgM, IgA | Very high | Intracellular ubiquitin ligase | Cytosol of almost all cells | Sends antibody complexes that entered the cell with a virus for degradation |

The FcγRs of the mouse differ (for example there is an FcγRIV and no FcγRIIA), so the correspondence between subclasses and receptors needs attention when antibody effects are studied in the mouse.

The balance between activation and inhibition. Most FcγRs are activating and signal through ITAMs; FcγRIIB is the only inhibitory FcγR and recruits the phosphatase SHIP through an ITIM. A single cell often expresses both kinds of receptor and is engaged by immune complexes on both at once; the response of the cell depends on the ratio of the two. Different IgG subclasses bind activating and inhibitory receptors in different ratios, so the subclass itself encodes the "strength of effect"; inflammatory cytokines such as IFN-γ upregulate activating receptors, and IL-4 and TGF-β upregulate FcγRIIB. On B cells, when FcγRIIB and the BCR are co-engaged by the same antigen–IgG complex, B-cell activation is inhibited, a negative feedback of antibody on its own production ([7.15.19](/7.15.19)); mice deficient in FcγRIIB develop autoimmunity resembling systemic lupus erythematosus, which shows that this brake is necessary to maintain tolerance ([7.15.25](/7.15.25)).

The functions of the four human IgG subclasses can therefore be listed in a table (the more "+", the stronger):

| | IgG1 | IgG2 | IgG3 | IgG4 |
|---|---|---|---|---|
| Fraction of serum IgG | About 60% | About 25% | About 8% | About 4% |
| Half-life | About 21 days | About 21 days | About 7 days | About 21 days |
| Complement activation | ++ | + | +++ | − |
| Binding to activating FcγRs | +++ | + (mainly the H131 form of FcγRIIA) | +++ | + |
| Typical antigens | Proteins | Bacterial capsular polysaccharides | Proteins (viruses, early response) | Long-term, repeated antigen contact ("Fab-arm exchange" makes it a functionally monovalent antibody) |

## 21.6. The Neonatal Fc Receptor: IgG Half-Life and Maternal Antibody

**Definition 21.6.1 (Neonatal Fc Receptor)** The receptor that is structurally similar to MHC class I molecules, associates with β2-microglobulin, binds the Fc of IgG and albumin at acidic pH (about 6.0) but hardly at neutral pH (7.4), and thereby rescues IgG from the lysosomal degradation pathway and carries it across cell layers is called the **neonatal Fc receptor** (FcRn).

FcRn was first found in the intestinal epithelium of newborn rats, where it is responsible for absorbing IgG from milk, hence its name; in adults it is continuously expressed on vascular endothelium, hematopoietic cells and many epithelia and has three functions:

1. Recycling: endothelial cells continuously take up plasma by pinocytosis; after the endocytic vesicles acidify, the IgG in them binds FcRn and is returned to the cell surface, where it is released into the blood at neutral pH; unbound protein goes to lysosomes for degradation. This is why the serum half-life of IgG (and albumin) is as long as about three weeks, whereas IgA and IgM, which do not depend on FcRn, have half-lives of only about 5–6 days and IgE about 2 days. Human IgG3 has arginine instead of histidine at position 435 of the Fc, binds FcRn more weakly at pH 6 and consequently has a half-life of only about 7 days.
2. Transplacental transport: syncytiotrophoblast cells transport maternal IgG into the fetal blood in the same way. IgG is the only antibody that crosses the human placenta; transport begins in mid-pregnancy and is most active in the last three months, and the IgG concentration of a full-term newborn can be slightly higher than that of the mother, whereas that of a premature infant is markedly lower.
3. Mucosal transport and antigen presentation: carrying IgG into or out of mucosal epithelium, carrying IgG-bound antigen back to the lamina propria; and in DCs sending IgG immune complexes into the compartments of antigen processing.

The structural basis of the pH switch is several histidines at the CH2–CH3 junction of the Fc: the side chain of histidine has a $\mathrm{p}K_{\mathrm{a}}$ of about 6 and is positively charged in the acidic environment of the endosome, forming salt bridges with acidic residues on FcRn; at pH 7.4 it loses the proton and binding is released.

**Example 21.6.1 (A Saturation Model of FcRn Recycling)** Suppose a cell takes up plasma IgG with rate constant $k_{\mathrm{u}}$, a fraction $f$ of the IgG taken up is rescued by FcRn and the rest is degraded. If the amount of FcRn is limited, the fraction rescued falls as the IgG concentration $C$ rises,

$$
f(C) = \frac{f_{\max}}{1 + C/K}, \qquad k(C) = k_{\mathrm{u}}\bigl(1 - f(C)\bigr), \qquad t_{1/2} = \frac{\ln 2}{k(C)},
$$
and serum IgG obeys $\frac{\mathrm{d}C}{\mathrm{d}t} = P - k(C)\,C$, where $P$ is the secretion rate of plasma cells (first-order kinetics and half-life are discussed in [2.4](/2.4)). Take $t_{1/2} = 2.5\,\mathrm{d}$ without recycling and $f_{\max} = 0.95$, and fix $K$ by requiring a half-life of 21 days for a normal adult ($C = 10\,\mathrm{g\,L^{-1}}$) (all these are illustrative values); the model gives:

- The half-life varies with the IgG concentration: about 35 days in hypogammaglobulinemia, 21 days when normal, and about 10 days after a large intravenous infusion of IgG. It is indeed observed clinically that the higher the IgG concentration, the faster IgG catabolism; this is also one mechanism by which high-dose IgG treats autoimmune diseases: it occupies FcRn and accelerates the degradation of pathogenic autoantibodies.
- Blocking FcRn ($f_{\max}$ reduced from 0.95 to 0.6) without changing antibody production lowers serum IgG by about 70% within several weeks, and it recovers after the drug is stopped. This is exactly the principle by which FcRn-antagonist drugs lower pathogenic IgG ([7.15.28](/7.15.28)); conversely, introducing mutations in the Fc that enhance binding at pH 6 can extend the half-life of a therapeutic antibody two- to fourfold.

Maternal antibody provides a natural experiment of "production stopped, only degradation left": after birth the IgG that came from the mother decays with a half-life of about 3–4 weeks while the infant's own IgG synthesis gradually increases, and the sum of the two reaches its minimum at about 3–6 months of age (physiological hypogammaglobulinemia), a period in which infants are prone to repeated infections. Maternal antibody is natural **passive immunity**; it also neutralizes some live attenuated vaccines and suppresses the infant's response to them, which is why some vaccines are postponed until maternal antibody has fallen ([7.15.33](/7.15.33)).

![A saturation model of FcRn recycling (Example 21.6.1, illustrative parameters). A: the IgG half-life as a function of the serum IgG concentration: the higher the concentration, the more saturated FcRn is and the lower the fraction rescued, so the shorter the half-life; the red dashed line is the half-life without any FcRn recycling (2.5 days). B: FcRn is blocked on days 14–56 (maximum fraction rescued reduced from 0.95 to 0.6) with antibody production unchanged; serum IgG falls by about 70% and recovers after the drug is stopped. C: serum IgG of an infant: maternal IgG acquired across the placenta (orange dashed line) decays after birth with a half-life of about 4 weeks, the infant's own synthesis (green dashed line) gradually increases, and the total (blue line) reaches its trough at about 3 months of age](./plots/fcrn-recycling.py)

:::

## 21.7. The Polymeric Immunoglobulin Receptor: IgA Enters the Mucosa

**Definition 21.7.1 (Polymeric Immunoglobulin Receptor)** The receptor that is expressed on the basolateral surface of epithelial cells of mucosae and exocrine glands, binds dimeric IgA and pentameric IgM that contain the J chain, carries them to the apical surface of the epithelium by transcytosis, and is cleaved there so that its extracellular portion (the secretory component) is released together with the antibody is called the **polymeric immunoglobulin receptor** (pIgR).

Plasma cells in the lamina propria secrete dimeric IgA carrying the **J chain**; IgA binds pIgR on the basal surface of the epithelium, is endocytosed, crosses the epithelial cell, and at the apical surface pIgR is cleaved by a protease; the extracellular portion left on the IgA is called the secretory component, and the two together are called **secretory IgA**. The secretory component protects IgA from degradation by proteases in the gut lumen and, through its glycans, anchors IgA in mucus. Humans secrete about 3–5 g of IgA into the gut lumen each day, more than the IgG produced by the whole body each day, so IgA is the antibody produced in the largest quantity in the human body. The large amount of secretory IgA in milk is not absorbed by the infant but acts in the infant's gut as protection, another form of maternal passive immunity.

Secretory IgA does not activate complement and its inflammatory effects through Fc receptors are weak, which suits it to work continuously on surfaces that are exposed every day to large numbers of commensal bacteria and food antigens: it binds microbes and antigens outside the epithelium, traps them in mucus and has them expelled by peristalsis ("immune exclusion"), without causing inflammation. Other aspects of mucosal immunity are covered in [7.15.23](/7.15.23).

## 21.8. Isotype and Effect: A Summary

| Isotype | Serum concentration (adult, $\mathrm{g\,L^{-1}}$) | Half-life | Main effects | Main sites |
|---|---|---|---|---|
| IgG | 7–16 | About 21 days (IgG3 about 7 days) | Neutralization, opsonization, complement (IgG1, IgG3), ADCC, transplacental | Blood and interstitial fluid; fetus |
| IgM | 0.4–2.3 | About 5 days | Strongest complement activation, agglutination, early response; BCR of B cells | Blood; natural antibody of B-1 cells |
| IgA | 0.7–4 | About 6 days | Neutralization, immune exclusion; phagocytosis through FcαRI | Mucosal secretions, milk (secretory form) |
| IgE | About 0.0003 | About 2 days (weeks when bound to mast cells) | Activation of mast cells and basophils through FcεRI | Mast cells in tissues |
| IgD | About 0.03 | About 3 days | BCR of naive B cells; secreted IgD can bind basophils | B-cell surface; upper respiratory tract |

While protecting the body, these effects are also the mechanisms of antibody-mediated tissue damage: IgE and mast cells correspond to type I hypersensitivity, IgG/IgM against cell-surface antigens causes type II hypersensitivity through complement, opsonization and ADCC, and deposited immune complexes cause type III hypersensitivity through complement and FcγR ([7.15.26](/7.15.26), [7.15.27](/7.15.27)).

## Summary

- The Fab determines "what is bound" and the Fc determines "what happens afterward". What depends on the Fab alone is **neutralization** (Definition 21.2.1) and agglutination; what depends on the Fc is opsonization, complement activation, **antibody-dependent cell-mediated cytotoxicity** (Definition 21.4.1), mast cell activation and transport.
- The cross-linking principle: Fc-mediated effects require several antibodies to aggregate on the same target (IgG hexamers and C1q, aggregation of FcRs); free antibody does not trigger effects.
- **Fc receptors** (Definition 21.5.1): activating receptors signal through ITAMs and the inhibitory FcγRIIB through an ITIM; the response of a cell depends on the ratio of the two. NK cells express only FcγRIIIA (CD16) and are the mainstay of ADCC; **FcεRI** (Definition 21.4.2), with a dissociation constant of the order of $10^{-10}\,\mathrm{M}$, keeps mast cells "armed" with IgE for a long time.
- **FcRn** (Definition 21.6.1): binds at pH 6 and releases at pH 7.4, recycling IgG and albumin (half-life about 21 days) and carrying maternal IgG across the placenta; the saturation model explains the shorter half-life at high IgG concentrations, the lowering of IgG by FcRn blockade, and the IgG trough at 3–6 months of age in infants (Example 21.6.1).
- **pIgR** (Definition 21.7.1): carries dimeric IgA and pentameric IgM to the mucosal surface, producing secretory IgA, which achieves immune exclusion without causing inflammation.

## Questions

1. A monoclonal antibody binds a virus efficiently in vitro but does not neutralize it; in mice it is still protective, and the protection disappears when its Fc is mutated so that it can no longer bind FcγR. Explain these results.

   **Answer** The epitope bound by the antibody is not on the receptor-binding site or the fusion machinery (or binding does not interfere with their function), so there is no neutralization. Its protection comes from the Fc: antibody bound to the surface of virus particles or infected cells mediates phagocytosis (opsonization) and ADCC through FcγR and clears virus and infected cells; after the Fc mutation these effects are lost and the protection disappears. This shows that the protective activity of an antibody cannot be judged from in vitro neutralization assays alone.

2. Why can a single IgG bound to antigen not activate complement, whereas a single IgM bound to antigen can? What does this require of the density of antigen epitopes?

   **Answer** Binding of a single globular head of C1q to Fc is very weak, and stable binding requires several Fc regions at once. IgM is a pentamer; after binding to a surface it changes into the staple conformation, and a single molecule supplies several C1q-binding sites at once; IgG is a monomer, and several IgG molecules must bind adjacent to one another on the surface and arrange themselves as a hexamer to bind C1q. Complement activation by IgG therefore requires a sufficient density of epitopes on the antigen surface (for example repeated antigens on the surface of a bacterium), and on sparse epitopes IgG can hardly activate complement.

3. Use the model of Example 21.6.1 to explain why giving a high dose of normal human IgG can accelerate the clearance of pathogenic autoantibodies in a patient. Give a qualitative argument.

   **Answer** The pathogenic autoantibodies share the same FcRn with the infused IgG. A high dose of IgG raises the total IgG concentration $C$, so $f(C) = f_{\max}/(1 + C/K)$ falls, and the elimination rate $k(C) = k_{\mathrm{u}}(1 - f(C))$ of all IgG (including the autoantibodies) rises and the half-life shortens, so the autoantibodies are degraded faster. This is only one mechanism of action of high-dose IgG, which also acts through FcγR (including upregulation of FcγRIIB) and other routes.

4. During pregnancy a mother produces IgG against an antigen of fetal red blood cells. Why can this antibody harm the fetus, whereas IgM of the same specificity cannot? Why does the damage subside by itself after birth?

   **Answer** IgG is actively transported into the fetal blood by FcRn in the syncytiotrophoblast, binds fetal red blood cells and destroys them through opsonization and phagocytosis mediated by complement and FcγR; IgM is a pentamer, does not bind FcRn and cannot cross the placenta. After birth no new maternal IgG enters, and the maternal IgG that has already entered decays with a half-life of about 3–4 weeks, so the damage subsides (the mechanism of this class of disease is described in [7.15.27](/7.15.27)).

5. Why is IgA, and not IgG, predominant on mucosal surfaces? Answer in terms of site of production, transport and effect.

   **Answer** Site of production: plasma cells in the mucosal lamina propria secrete mainly IgA, and TGF-β, retinoic acid, BAFF and APRIL in the mucosal environment drive B cells to switch to IgA. Transport: dimeric IgA carries the J chain and can be actively carried to the epithelial surface by pIgR, and the secretory component also protects it from degradation by gut luminal proteases; monomeric IgG does not bind pIgR and can reach the surface only through limited transport by FcRn or by exudation. Effect: IgA does not activate complement and its inflammatory Fc effects are weak, which suits it to bind and exclude antigen continuously on surfaces where large numbers of commensal bacteria and food antigens are present without causing inflammation; if IgG were predominant, continuous complement activation and FcγR activation would cause chronic inflammation.
