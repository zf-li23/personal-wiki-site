---
title: Deep Learning for Biological Sequences
description: "Neural networks that read DNA, RNA and protein sequences: one-hot encoding and convolution as a learned weight matrix, a small network trained in numpy that rediscovers the CTCF motif; sequence-to-function models of regulatory DNA (DeepSEA, Basset, Basenji, BPNet, Enformer, Borzoi, SpliceAI), receptive fields and dilated convolutions; interpretation by in silico saturation mutagenesis, gradients and TF-MoDISco; protein and genomic language models (ESM-2, Nucleotide Transformer, HyenaDNA, Evo); zero-shot variant effect prediction and deep mutational scanning; homology leakage, class imbalance and baselines; guide activity and repair outcomes of Cas9."
---

The models of the preceding chapters describe sequences with a few explicit assumptions: a position weight matrix treats the positions of a site as independent ([7.8.8](/7.8.8)), a hidden Markov model lets the next state depend only on the current one ([7.8.7](/7.8.7)), a profile scores each column of a family on its own ([7.8.5](/7.8.5)). Since about 2015 models with far fewer assumptions have been fitted to the large data sets that sequencing produces: millions of chromatin profiles, binding measurements, splice junctions and protein sequences. These models are deep neural networks, and in several areas they now set the standard, among them the effect of a mutation on splicing, the chromatin and expression signals of a stretch of DNA, and the structure of a protein. This chapter treats how such networks read sequences, what they learn and how that can be seen, the pretrained language models of proteins and genomes, the prediction of variant effects, the methodological traps that make published accuracies unreliable, and one application promised in [7.2.24](/7.2.24) and [7.8.10](/7.8.10#sec-10.6): the design of CRISPR guides. The general theory is not repeated here: multilayer networks and **backpropagation** are in [4.7.2](/4.7.2), convolutional networks in [4.7.3](/4.7.3), attention and the Transformer in [4.7.6](/4.7.6), pretraining in [4.7.7](/4.7.7), evaluation in [4.6.2](/4.6.2). RNA structure is predicted by the dynamic programs of [7.8.16](/7.8.16) and protein structure, where learning had its largest success, in [7.8.17](/7.8.17) and [7.6.15](/7.6.15#sec-15.5.5). The running example is the binding motif of CTCF from [7.8.8](/7.8.8): a small network is made to discover it, and then asked where it looked.

## 15.1. Sequences as Input

### 15.1.1. Encoding and Tasks

A network computes with vectors, so a sequence must be encoded. The standard encoding of DNA is the **one-hot vector** ([7.8.7](/7.8.7#sec-7.6)): base $b$ at position $i$ becomes row $i$ of an $L \times 4$ binary matrix $X$ with a single $1$ in column $b$; proteins use $L \times 20$, or $21$ with an unknown symbol. The encoding loses nothing and imposes no similarity between letters, leaving the network to learn which letters behave alike. Language models instead split a sequence into tokens, single residues, overlapping or nonoverlapping $k$-mers, or variable-length units found by **byte-pair encoding** ([4.7.5](/4.7.5#sec-5.7.2)), and map every token to a learned vector.

**Definition 15.1.1 (Sequence-to-Function Model)** A **sequence-to-function model** is a parametric function $f_{\boldsymbol{\theta}}$ that maps a sequence $x$, or its encoding $X$, to measurable properties of the molecule or locus: a scalar (bound or not, splice site or not), a vector over assays and cell types, a profile along the sequence (a coverage track at some resolution), or another sequence. Its parameters are estimated by minimizing a loss over training pairs $(x_n, \boldsymbol{y}_n)$, usually by stochastic gradient descent.

The output decides the loss: the **cross-entropy loss** for classes, a Poisson or multinomial log-likelihood for read counts, squared error for transformed signals. Training is supervised when the targets are measurements and self-supervised when they are parts of the input itself, as in the language models of 15.4.

### 15.1.2. Convolution as a Learned Weight Matrix

The first layer of most sequence networks is a one-dimensional convolution ([4.7.3](/4.7.3#sec-3.2.2)): a filter $F \in \mathbb{R}^{w \times 4}$ with bias $c$ slides along the sequence and produces at position $p$

$$
a_p = c + \sum_{j=1}^{w}\sum_{b}F_{jb}X_{p+j-1,b} = c + \sum_{j=1}^{w}F_{j,x_{p+j-1}}. \tag{15.1}
$$

**Theorem 15.1.1 (Convolution and Weight Matrices)** On one-hot encoded DNA a convolutional filter of width $w$ computes, at every position, the score of a weight matrix of length $w$ plus a constant. Conversely every **position weight matrix** $W_{jb} = \log(p_{jb}/q_b)$ is such a filter, with $F = W$ and $c = 0$. A filter followed by global **max pooling** returns the score of the best site in the sequence; followed by $\log\sum_p\exp(a_p)$ it returns, up to an additive constant, the log-likelihood ratio of a motif model with one site at a uniformly distributed position.

**Proof** Since $X_{ib} = \boldsymbol{1}[x_i = b]$, the inner sum of Eq. (15.1) selects one entry $F_{j,x_{p+j-1}}$ per row, which is the weight-matrix score of the window starting at $p$ ([7.8.8](/7.8.8#sec-8.2.1)); the bias adds a constant. Max pooling takes the largest of these scores. If $F = W$ in natural-log units, $\exp(a_p)$ is the likelihood ratio of a site at $p$ against the background, so the mean over the $M$ windows is the likelihood ratio of the one-occurrence-per-sequence model of [7.8.8](/7.8.8#sec-8.4.3), whose logarithm differs from $\log\sum_p\exp(a_p)$ by $\log M$. $\square$

What differs from a weight matrix is how the entries are obtained. A matrix is counted from aligned sites; a filter is learned from labeled sequences by backpropagation, without being told where the sites are or what they look like, and many filters are learned together with the layers above them, which combine them into rules no single matrix expresses: pairs of sites at preferred spacings and orientations, the absence of a repressor site, the surrounding base composition. With rectified linear units, pooling and further layers the network is a learned, hierarchical, nonlinear scanner for motifs and their arrangements.

## 15.2. Convolutional Networks for Regulatory Sequence

### 15.2.1. A Minimal Network

**Algorithm 15.2.1 (Training a Convolutional Motif Classifier)** Input: one-hot sequences $X_n$ of length $L$ with labels $y_n \in \{0, 1\}$.

1. Model: $K$ filters $F_k$ of width $w$ with biases $c_k$, activations $a_{kp}$ by Eq. (15.1), pooled features $h_k = \max_p\max(a_{kp}, 0)$, logit $z = v_0 + \sum_kv_kh_k$ and probability $\sigma(z)$.
2. Loss: $\ell = -\frac{1}{N}\sum_n[y_n\log\sigma(z_n) + (1 - y_n)\log(1 - \sigma(z_n))] + \frac{\lambda}{2}(\|F\|^2 + \|\boldsymbol{v}\|^2)$.
3. Gradients by backpropagation: $\partial\ell/\partial z_n = (\sigma(z_n) - y_n)/N$ and $\partial z/\partial h_k = v_k$; the gradient of $h_k$ reaches only the window $p^*_k$ at which the maximum is attained, and only if $a_{kp^*_k} > 0$, where $\partial a_{kp}/\partial F_{k,jb} = X_{p+j-1,b}$.
4. Update all parameters by minibatch stochastic gradient descent or Adam ([4.7.4](/4.7.4#sec-4.3.3)) for a few epochs, keeping the parameters with the smallest validation loss.

One epoch costs $O(NLKw)$ operations, the cost of scanning the training set with $K$ matrices.

**Example 15.2.1 (Rediscovering the CTCF Motif)** We simulated $7000$ random sequences of $120$ bp with human base frequencies and planted in half of them one site drawn from the CTCF matrix of [7.8.8](/7.8.8), at a random position and on a random strand. A network with $8$ filters of width $24$ ($785$ parameters), written in numpy as in Algorithm 15.2.1, was trained on $4000$ of them for $15$ epochs. The validation AUROC rose from $0.977$ after one epoch to $0.988$; the training loss kept falling, from $0.38$ to $0.075$, while the validation loss stopped improving after about ten epochs (around $0.14$), the onset of **overfitting**. On $2000$ test sequences the AUROC was $0.988$ and the accuracy $94.1\,\%$. The best possible classifier here is the true matrix scanned over both strands, which reaches $0.998$: the remaining errors are sequences whose planted site happens to be weak. The two filters with the largest output weights, converted into frequency matrices from the validation windows that activate them above half their maximum, are the CTCF motif and its reverse complement, with correlations $0.96$ and $0.97$ to the planted frequencies — learned without ever being shown a site.

![A small convolutional network learns a binding motif from labeled sequences (simulated data). Sequences of 120 bp with human base frequencies, half carrying one site drawn from the CTCF matrix on a random strand, are classified by one convolutional layer of 8 filters of width 24, ReLU, global max pooling and a logistic output, trained with Adam on 4000 sequences (Algorithm 15.2.1). A: training and validation loss and validation AUROC by epoch; the validation loss stops improving after about ten epochs. B: the planted matrix as a logo. C, D: the two filters with the largest output weights as frequency matrices of the validation windows that activate them above half their maximum, aligned to the planted motif (C is its reverse complement, whose first positions fall outside the filter); the correlations with the planted frequencies are 0.97 and 0.96](./plots/cnn-motif.py)

Such models are normally written in a framework with automatic differentiation. The network of Example 15.2.1 in PyTorch is

```python
import torch
import torch.nn as nn


class MotifCNN(nn.Module):
    def __init__(self, n_filters=8, width=24):
        super().__init__()
        self.conv = nn.Conv1d(4, n_filters, kernel_size=width)   # input: batch x 4 x L, one-hot
        self.out = nn.Linear(n_filters, 1)

    def forward(self, x):
        h = torch.relu(self.conv(x)).amax(dim=2)                 # global max pooling over positions
        return self.out(h).squeeze(1)                            # logit


model = MotifCNN()
opt = torch.optim.AdamW(model.parameters(), lr=1e-2, weight_decay=1e-3)
loss_fn = nn.BCEWithLogitsLoss()
for epoch in range(15):
    for x, y in train_loader:                                    # x: float tensor, y: 0/1 labels
        opt.zero_grad()
        loss_fn(model(x), y.float()).backward()
        opt.step()
```

### 15.2.2. From Labels to Profiles

The first deep models of regulatory DNA classified short sequences. DeepBind (Alipanahi and colleagues, 2015) trained one small network per protein on binding data from protein-binding microarrays, HT-SELEX and ChIP-seq. DeepSEA (Zhou and Troyanskaya, 2015) read $1000$ bp and predicted, for the central $200$ bp, $919$ binary chromatin features at once (transcription factor ChIP-seq, DNase I and histone marks from ENCODE and Roadmap); Basset (Kelley and colleagues, 2016) predicted the accessibility of $600$-bp sequences in $164$ cell types. Predicting many outputs jointly lets all tasks share the motif detectors of the first layer, and the difference of the predicted features between two alleles became one of the first genome-wide scores for regulatory variants.

Classifiers discard the shape of a signal. Later models predict profiles. Basenji (Kelley and colleagues, 2018) read $131\,072$ bp and predicted coverage of thousands of assays in bins of $128$ bp; BPNet (Avsec and colleagues, 2021) predicted base-resolution ChIP-nexus profiles of the pluripotency factors Oct4, Sox2, Nanog and Klf4 from $1$ kb, from which rules of motif spacing were read off; Enformer (Avsec and colleagues, 2021) added **self-attention** layers ([4.7.6](/4.7.6)) to read $196\,608$ bp and predict $5313$ human tracks in $896$ bins, so that enhancers up to about $100$ kb away can influence the predicted expression of a gene; Borzoi (Linder and colleagues, 2025) reads $524$ kb and predicts RNA-seq coverage at $32$-bp resolution, which makes splicing and polyadenylation visible. For splicing, SpliceAI (Jaganathan and colleagues, 2019) predicts for every position whether it is a donor, an acceptor or neither from $10$ kb of context, and the change of these probabilities between alleles is used to interpret variants that create or destroy splice sites ([7.8.12](/7.8.12#sec-12.8.2)).

![Input length and output resolution of published sequence-to-function models of regulatory DNA (values from the original publications). The input is the sequence a model reads for one prediction; the output resolution is the length of sequence summarized by one predicted value. Points on the dashed diagonal make one prediction per input; points far below it predict a profile along the input. Since 2015 inputs have grown, to capture distal regulation, and outputs have become finer, to capture the shape of binding, splicing and transcription signals](./plots/model-scales.py)

A long input helps only if the network can relate distant positions. In a stack of convolutions the output depends on a window that grows with depth, the **receptive field** ([4.7.3](/4.7.3#sec-3.4.2)).

**Formula 15.2.1 (Receptive Field of Dilated Convolutions)** A stack of convolutions of kernel width $k$ with dilations $d_1, \dots, d_m$ (taps $d_\ell$ positions apart) has a receptive field of

$$
R = 1 + (k - 1)\sum_{\ell=1}^{m}d_\ell
$$
input positions; with $d_\ell = 2^{\ell-1}$ it is $R = 1 + (k - 1)(2^m - 1)$, growing exponentially in the depth at a cost linear in the number of parameters.

**Example 15.2.2** Undilated convolutions of width $3$ give $R = 2m + 1$, so $2047$ layers would be needed for $4095$ positions. With dilations $1, 2, \dots, 2^{10}$, eleven layers reach $R = 1 + 2(2^{11} - 1) = 4095$ positions; applied to sequence already pooled into bins of $128$ bp, this covers $524\,160$ bp, which is how Basenji sees its input. Attention connects every position to every other in one layer at a cost quadratic in their number, which Enformer keeps affordable by attending among $1536$ bins of $128$ bp rather than among bases ($1536 \times 128 = 196\,608$).

Deep learning entered the other parts of this course in the same form. DeepVariant classifies images of read pileups into genotypes ([7.8.12](/7.8.12#sec-12.2.3)); gene finders such as Helixer and Tiberius label every base as coding, intron or intergenic, sometimes with a hidden Markov model on top to enforce a valid gene structure ([7.8.7](/7.8.7)); basecallers translate nanopore current into bases ([7.8.9](/7.8.9)). Each replaces a hand-built probabilistic model by a learned one, and each inherits the requirement that its training data cover the cases it will meet.

## 15.3. Seeing What a Model Has Learned

A network that predicts well is useful; one whose reasons can be read is also an instrument of discovery. Attribution methods assign to each input position a number measuring its contribution to an output.

**Definition 15.3.1 (In Silico Saturation Mutagenesis)** *In silico saturation mutagenesis* of a sequence $x$ under a model $f$ computes, for every position $i$ and every alternative residue $b \ne x_i$, the predicted effect $\Delta_{ib} = f(x^{(i \to b)}) - f(x)$ of that single substitution. The matrix $(\Delta_{ib})$ is the computational analogue of a saturation mutagenesis experiment, and the mean over $b$ is the importance of position $i$.

The method costs $3L$ evaluations of the model for DNA of length $L$: cheap for small models, expensive for Enformer-sized ones. Gradient methods need one backward pass. The gradient $\partial f/\partial X_{ib}$ is a saliency map; *gradient × input* keeps the entry of the observed base, $X_{ix_i}\,\partial f/\partial X_{ix_i}$. Because a linearization is only local, two refinements are usual: DeepLIFT (Shrikumar and colleagues, 2017) propagates differences from a reference input with modified rules, and integrated gradients (Sundararajan and colleagues, 2017) average the gradient along a path from a reference $X'$ (a shuffled or background sequence) to $X$,

$$
\operatorname{IG}_{ib} = (X_{ib} - X'_{ib})\int_0^1\frac{\partial f}{\partial X_{ib}}\bigl(X' + \alpha(X - X')\bigr)\,\mathrm{d}\alpha, \qquad \sum_{i,b}\operatorname{IG}_{ib} = f(X) - f(X'),
$$
the second identity following from the fundamental theorem of calculus along the path.

**Example 15.3.1** For a test sequence of Example 15.2.1 whose planted site gives a predicted probability of $0.996$, saturation mutagenesis shows that the network relies on the site: $73\,\%$ of the total absolute importance lies in its $19$ bp, and the five most important positions are motif positions $4$, $5$, $10$, $13$ and $14$, the most informative columns of the CTCF logo. The largest single effect, a substitution at motif position $13$, lowers the logit by $5.1$; a few substitutions raise it, by up to $2.4$, by moving the site toward the consensus. Gradient × input reproduces the profile (correlation $0.96$) with one backward pass instead of $360$ forward evaluations. Outside the site the attributions are small and confined to the windows selected by the filters with negative output weights.

![In silico saturation mutagenesis and gradient-times-input attribution for the network of Example 15.2.1 on one test sequence with a planted CTCF site. A: the change in the output logit for each of the three substitutions at every position (blue: loss, red: gain); dots mark the bases of the planted site, whose own cells are zero by definition. B: the importance of each position as the mean loss of logit on mutation (bars) and as gradient × input (line); the shaded band is the planted site. Because of global max pooling only positions inside the maximally activated window of some filter can have nonzero attribution](./plots/ism.py)

Attribution maps of many sequences contain recurring short patterns. TF-MoDISco (Shrikumar and colleagues, 2018) cuts out the high-attribution segments of all sequences, clusters them and aggregates each cluster into a motif with a logo, which closes the circle with [7.8.8](/7.8.8): the motifs come from function rather than from counting aligned sites, and their preferred combinations and spacings can be measured by planting pairs of motifs in synthetic sequences and predicting the output. Three cautions apply. Attributions explain the model, not the cell: a model that has learned a correlate of binding, such as GC content or a cofactor's motif, will display it. Different methods disagree where interactions are strong, since one number per position cannot describe an interaction. And a network trained on genomic sequence predicts within the distribution of the genome and can be confidently wrong for designed or heavily mutated sequences.

## 15.4. Language Models of Sequences

### 15.4.1. Protein Language Models

Labeled data are scarce: a few thousand structures of a fold, a few hundred measured mutants of a protein. Unlabeled sequences are abundant: UniProt holds hundreds of millions of them ([7.8.2](/7.8.2)). A **language model** ([4.7.5](/4.7.5#sec-5.4.1)) learns the distribution of sequences themselves, and so captures the constraints that evolution has imposed on them.

**Definition 15.4.1 (Protein Language Model)** A *protein language model* is a neural network, usually a Transformer, trained by **self-supervised learning** on large collections of natural protein sequences to predict residues from their context: masked residues from the rest of the sequence (**masked language modeling**) or the next residue from the preceding ones. Its representations of residues and sequences, and its predicted residue probabilities, are then used for other tasks.

For masked modeling a random subset $M$ of positions, about $15\,\%$, is hidden and the parameters minimize

$$
\mathcal{L}(\boldsymbol{\theta}) = -\mathbb{E}_{x}\,\mathbb{E}_{M}\sum_{i \in M}\log p_{\boldsymbol{\theta}}(x_i \mid x_{\setminus M}). \tag{15.2}
$$

The ESM models (Rives and colleagues, 2021; ESM-2, Lin and colleagues, 2023) are encoder Transformers trained in this way on clustered UniRef sequences, with $8$ million to $15$ billion parameters; ProtT5 (Elnaggar and colleagues, 2022) is an encoder–decoder alternative. To fill in a masked residue well a model must learn which residues each position of each family tolerates and which positions vary together, and therefore something about structure. The attention maps of such models indeed predict residue contacts without supervision (Rao and colleagues, 2021): a logistic regression on the attention weights recovers contacts about as well as a **Potts model** fitted to a **multiple sequence alignment** ([7.6.15](/7.6.15#sec-15.5.4)), the statistical expression of **coevolution**, although the language model sees one sequence at a time. ESMFold predicts structures from ESM-2 representations without an alignment ([7.8.17](/7.8.17)). Embeddings averaged over residues serve as features for predicting localization, function or solubility with a small supervised head, a form of **transfer learning**; fine-tuning the whole model on the labeled task is the alternative ([4.7.7](/4.7.7#sec-7.5.1)).

### 15.4.2. Genomic Language Models

**Definition 15.4.2 (Genomic Language Model)** A *genomic language model* is a language model trained on DNA, typically whole genomes of one or many species, to predict masked or following nucleotides, and used as a source of representations or likelihoods for genomic tasks.

DNABERT (Ji and colleagues, 2021) used overlapping $k$-mers as tokens; the Nucleotide Transformer (Dalla-Torre and colleagues, 2024) used nonoverlapping $6$-mers and genomes of hundreds of species; HyenaDNA (Nguyen and colleagues, 2023) replaced attention by long convolutions to reach contexts of a million single nucleotides; Evo (Nguyen and colleagues, 2024), with $7$ billion parameters and a context of $131$ kb trained on bacterial, archaeal and phage genomes, generates plausible operons and CRISPR loci, and Evo 2 (2025) extends training to all domains of life. DNA is harder to model than protein. Most of a mammalian genome is not under selection, so the model spends its capacity on repeats and neutral sequence; functional elements are short and sparse; and what a regulatory sequence does depends on the cell, which the sequence alone does not specify. Independent evaluations on regulatory tasks have found that representations from pretrained DNA models often do no better than supervised models trained directly on the task, or than one-hot baselines (Tang and Koo, 2024); they help most where evolutionary constraint is itself the signal, as in coding sequence, splice sites and compact microbial genomes.

## 15.5. Predicting the Effects of Variants

**Definition 15.5.1 (Variant Effect Prediction)** *Variant effect prediction* is the computational estimation, from sequence and possibly structure and conservation, of the consequence of a genetic variant for a molecular phenotype (protein stability or activity, binding, splicing, expression) or for fitness and disease. Supervised predictors are trained on labeled variants; zero-shot predictors score a variant with a model of natural sequences, without labels.

Supervised predictors learn from variants classified in ClinVar ([7.8.12](/7.8.12#sec-12.8.2)) and inherit its biases: well-studied genes are overrepresented, some labels reflect earlier predictions, and test variants are often close relatives of training variants. Zero-shot predictors avoid labels altogether. Their premise is that evolution has run a mutagenesis experiment for hundreds of millions of years, and that the substitutions it tolerated are those seen in present-day sequences.

**Formula 15.5.1 (Masked-Marginal Score)** For the substitution of the wild-type residue at position $i$ by $b$, a masked language model gives

$$
s(i, b) = \log p_{\boldsymbol{\theta}}(x_i = b \mid x_{\setminus i}) - \log p_{\boldsymbol{\theta}}(x_i = \mathrm{wt} \mid x_{\setminus i}), \tag{15.3}
$$
the log odds of the mutant against the wild type with position $i$ masked; negative scores predict damaging substitutions. Several substitutions are scored by summing, which assumes their effects are additive.

**Example 15.5.1** Suppose that at a buried position a model gives probability $0.62$ to the wild-type leucine, $0.20$ to isoleucine and $0.004$ to aspartate. The scores are $\ln(0.20/0.62) = -1.13$ for L→I and $\ln(0.004/0.62) = -5.04$ for L→D: a conservative substitution is mildly disfavored and a charged residue in the core strongly, the mutant being $\mathrm{e}^{5.04} \approx 155$ times less probable than the wild type in this context.

This is the method of ESM-1v (Meier and colleagues, 2021). EVE (Frazer and colleagues, 2021) fits a variational autoencoder to the alignment of each protein family and scores a variant by the change in the approximate log-likelihood, a family-specific model in the tradition of the profiles of [7.8.5](/7.8.5). AlphaMissense (Cheng and colleagues, 2023) adapts the AlphaFold architecture with a language-modeling objective and calibrates its output against population frequencies, treating variants common in humans and other primates as benign; it classified $89\,\%$ of the $71$ million possible human missense substitutions as likely pathogenic ($32\,\%$) or likely benign ($57\,\%$). In the ACMG/AMP framework such scores are supporting computational evidence, not a diagnosis ([7.8.12](/7.8.12#sec-12.8.3)).

The yardstick is experiment. In *deep mutational scanning* a library of all or most single mutants of a protein is expressed, selected for a function (growth, binding, fluorescence) and sequenced before and after selection, and the change in each variant's frequency estimates its effect. ProteinGym (Notin and colleagues, 2023) collects many such assays and ranks predictors by the Spearman correlation between predicted and measured effects; the best zero-shot models average around $0.4$ to $0.5$ and vary greatly between proteins, because an assay measures one function under one selection while evolution integrates all of them.

For noncoding variants, sequence-to-function models are applied to both alleles and the predictions subtracted: the change in predicted accessibility, in a factor's binding profile, in splice-site probabilities or in a gene's expression. Such predictions prioritize variants in fine-mapped association intervals ([7.4.25](/7.4.25)), and a predicted enhancer can then be deleted by editing. But models such as Enformer, trained on the reference genome across cell types, explain little of the variation in expression between individuals measured as **expression quantitative trait locus** effects, and often predict the wrong direction (Sasse and colleagues, 2023; Huang and colleagues, 2023): learning from one genome what each sequence does in each cell type is not the same as learning how small differences between genomes change it. For the lactase-persistence variant of [7.8.8](/7.8.8#sec-8.3.2), a model of accessibility in intestinal cells, not a matrix scan, would be the tool to try.

## 15.6. Pitfalls of Evaluation

### 15.6.1. Homology Leakage

The usual assumption that training and test examples are independent draws from one distribution ([4.7.1](/4.7.1#sec-1.4.2)) fails for biological sequences, which are related by descent. A random split puts close homologs of almost every test sequence into the training set, so a model can score well by recognizing relatives instead of learning the rule that relates sequence to function: a form of **data leakage** ([4.6.2](/4.6.2#sec-2.5)).

**Example 15.6.1 (Leakage by Homology)** We simulated $1200$ sequences of $150$ bp arranged in $40$ superfamilies of $5$ families of $6$ members: a family ancestor differs from its superfamily ancestor at $25\,\%$ of sites and a member from its family ancestor at $5\,\%$, so that pairs within a family share on average $90\,\%$ of positions, pairs within a superfamily $54\,\%$ and unrelated pairs $25\,\%$. The label is a coin toss made once per superfamily, so no rule connects sequence to label and the true accuracy on a new superfamily is $50\,\%$. A nearest-neighbor classifier, standing for any model able to memorize, reaches $100\,\%$ on a random split. Splitting instead by single-linkage clusters at a threshold gives $100\,\%$ down to a threshold of $65\,\%$ identity, $83\,\%$ at $60\,\%$ and $50\,\%$ at $55\,\%$ identity, where the clusters finally coincide with the superfamilies ($44$ clusters for $40$ superfamilies). The estimated accuracy is therefore a property of the split, and only a split that separates evolutionary units measures generalization.

![Homology leakage (simulated). 1200 sequences in 40 superfamilies of 5 families of 6 members; the label is a random property of the superfamily, so the true accuracy on a new superfamily is 50 %. A: distribution of pairwise identity within families, within superfamilies and between superfamilies. B: test accuracy of a nearest-neighbor classifier (mean and standard deviation over 20 splits with 20 % held out) for a random split and for splits by single-linkage identity clusters; the numbers below the points are the clusters obtained at each threshold. The estimate stays at 100 % until the clusters reach the superfamilies](./plots/leakage.py)

This is why benchmarks in bioinformatics are built on clustered splits: training and test sequences are clustered at a chosen identity (CD-HIT or MMseqs2 linclust, [7.8.4](/7.8.4#sec-4.6)) and whole clusters are assigned to one side, or splits are made by family, by fold (as in CASP and CAFA, [7.8.17](/7.8.17)), by chromosome for genomic models, or by held-out species. Thresholds of $25$ to $30\,\%$ identity are used for proteins, because that is where sequence similarity ceases to be detectable ([7.8.3](/7.8.3)). Leakage has other forms: overlapping genomic windows placed on both sides of a split, paralogs of a gene, data from the same individual or experiment in both sets, or filtering and normalization performed before splitting.

### 15.6.2. Imbalance, Metrics and Baselines

Functional sites are rare. Training sets are often balanced by subsampling the negatives, which makes the reported accuracy useless for the genome, where the ratio is thousands to one. The AUROC is nearly unaffected by the class ratio, which is why it is reported; the **precision–recall curve** and its area ([4.6.2](/4.6.2#sec-2.3.4)) are not, and are the honest summary.

**Example 15.6.2** The network of Example 15.2.1 was applied to a test set with the same sequences but a prevalence of $1\,\%$ ($200$ positives among $20\,000$). The AUROC is unchanged at $0.988$, but the average precision falls from $0.988$ on balanced data to $0.78$, and at the default threshold $91\,\%$ of the sites are found at a precision of only $26\,\%$: $508$ false positives for $182$ true ones. At a genome-wide prevalence of one in $10^5$ the same classifier would return mostly false positives, which is the quantitative form of the argument made for matrix scans in [7.8.8](/7.8.8#sec-8.3.1).

A deep model should also be compared with the simplest model that could do the job: a matrix scan, a $k$-mer logistic regression, a gradient-boosted tree on a few hand-made features, or nearest neighbors by sequence identity. In Example 15.2.1 the true matrix beats the network, as it must, since the data were generated from it; on real data the gap is the other way, but it is often small, and the part of a published improvement that comes from a larger training set, a better split or more tuning rather than from the architecture is visible only if a baseline is tuned as carefully as the model. Reporting variability over several random initializations and splits is part of the same discipline.

## 15.7. Sequence Models for Genome Editing

Designing an experiment with **CRISPR–Cas9** requires three predictions from sequence: where else in the genome the guide could cut, how efficiently it will cut its target, and what the repair will leave behind. The first is a search problem, solved by the indexing methods of [7.8.10](/7.8.10#sec-10.6); the other two are learning problems.

*Activity.* Guides targeting the same gene differ in editing efficiency by an order of magnitude, for reasons that lie partly in the spacer sequence: its GC content, the nucleotides next to the PAM, secondary structure in the single guide RNA that competes with the scaffold, and runs of thymidines that terminate transcription from a U6 promoter. Rule Set 2 (Doench and colleagues, 2016) is a gradient-boosted regression on such features, fitted to thousands of guides measured in pooled assays; DeepSpCas9 (Kim and colleagues, 2019) and later convolutional models learn the features themselves from the $30$-nt target context. These models rank guides at one locus reliably enough to be useful, while absolute efficiencies transfer poorly between cell types and delivery methods, because chromatin and expression contribute as much as the sequence ([7.2.24](/7.2.24#sec-24.4)).

*Repair outcomes.* A blunt double-strand break is repaired by **nonhomologous end joining**, often precisely, or by microhomology-mediated end joining, which anneals short identical stretches on the two sides and deletes the sequence between them ([7.2.8](/7.2.8)). The second pathway makes the outcome predictable from sequence alone, since the microhomologies available at a site are a property of the site.

**Algorithm 15.7.1 (Microhomology Deletion Patterns)** For a cut between the flanks $\mathrm{L}$ and $\mathrm{R}$: for every length $k \ge 2$ and every pair of identical $k$-mers, one ending in $\mathrm{L}$ and one beginning in $\mathrm{R}$, record the deletion that keeps a single copy of the microhomology, of length $D$ equal to the distance between the two copies; give it the pattern score

$$
100\,\mathrm{e}^{-D/20}\,(2n_{\mathrm{GC}} + n_{\mathrm{AT}})
$$
with $n_{\mathrm{GC}}$ and $n_{\mathrm{AT}}$ the composition of the microhomology (Bae and colleagues, 2014), keeping for each product only its longest microhomology. The predicted frequency of a product is its share of the total score, and the out-of-frame score is the share of products whose length is not a multiple of three.

**Example 15.7.1** For an invented target whose protospacer AGTTCGGCATCCAGTGGCAG is followed by the PAM TGG, with Cas9 cutting three base pairs upstream of the PAM, the two flanks contain $35$ microhomology pairs. The best is the six-base CAGTGG, present on both sides at a distance of six, giving a $6$-bp deletion with $17.3\,\%$ of the total score; next are a $9$-bp deletion on GTG ($7.5\,\%$) and a $16$-bp deletion on CCA ($5.3\,\%$). The out-of-frame score is $61\,\%$, so a knockout attempt at this site produces a frameshift in roughly three alleles out of five, and the most likely single outcome keeps the reading frame. For a knockout one would pick a guide with a high out-of-frame score; for a precise deletion, a site with one dominant microhomology.

![Predicting the deletions produced by microhomology-mediated end joining at a Cas9 cut (invented target sequence, Algorithm 15.7.1). A: the target with protospacer, PAM and cut site, and the four highest-scoring deletion products; the microhomology that is kept is boxed and the dashed line spans the deleted sequence. B: the share of the total pattern score of the twelve highest-scoring products, labeled by deletion length and microhomology and colored by whether the product keeps the reading frame; the out-of-frame score of this site is 61 %](./plots/repair-outcomes.py)

Learned models go beyond the score. inDelphi (Shen and colleagues, 2018) combines a model of microhomology-mediated deletions with a learned model of insertions of one base, which are templated by the base before the cut, and predicts the full distribution of outcomes; FORECasT (Allen and colleagues, 2019) learns the same distribution from measurements at thousands of synthetic target sites. Both find that outcomes are reproducible between experiments at the same site, which is what makes prediction possible at all, and both are used in reverse: to choose, among the guides that cut a site, one whose dominant product is the desired allele. Prime editing has brought a further round of prediction, of the efficiency of a pegRNA from its spacer, primer binding site and reverse-transcription template ([7.2.24](/7.2.24#sec-24.5)). The statistics of pooled screens, where counts of guides are compared between conditions, belong to [7.9](/7.9), and the negative binomial models they use to [7.7](/7.7).

## Summary

| Topic | Key points |
|---|---|
| Encoding | one-hot DNA ($L\times4$) and protein ($L\times20$); tokens and embeddings for language models; outputs: scalar, multi-task vector, profile (Definition 15.1.1) |
| Convolution | a filter is a weight matrix plus a constant; max pooling = best site, log-sum-exp = one-site model (Theorem 15.1.1); learned jointly with the layers that combine motifs |
| A small model | $8$ filters, $785$ parameters, recover the CTCF motif and its reverse complement ($r = 0.96$, $0.97$) with test AUROC $0.988$ against $0.998$ for the true matrix (Algorithm 15.2.1, Example 15.2.1) |
| Models of regulatory DNA | DeepBind, DeepSEA ($919$ features), Basset; profiles: BPNet (base resolution), Basenji, Enformer ($197$ kb, $128$-bp bins), Borzoi ($524$ kb, $32$ bp), SpliceAI ($10$ kb) |
| Long range | receptive field $1 + (k-1)\sum_\ell d_\ell$; dilations grow it exponentially (Formula 15.2.1, Example 15.2.2); attention is quadratic in the number of bins |
| Interpretation | saturation mutagenesis ($3L$ evaluations, Definition 15.3.1), gradient × input, integrated gradients with completeness; TF-MoDISco turns attributions back into motifs; $73\,\%$ of importance inside the planted site (Example 15.3.1) |
| Language models | masked objective Eq. (15.2); ESM-2, ProtT5; attention maps give contacts without supervision; DNABERT, Nucleotide Transformer, HyenaDNA, Evo; weaker gains on regulatory DNA (Definitions 15.4.1, 15.4.2) |
| Variant effects | masked-marginal log odds Eq. (15.3); EVE, AlphaMissense ($89\,\%$ of human missense variants classified); evaluation by deep mutational scanning (ProteinGym); noncoding predictions are poor for between-individual expression |
| Evaluation | homology leakage: $100\,\%$ accuracy on a random split for a label that cannot be predicted (Example 15.6.1); clustered splits at $25$–$30\,\%$ identity; AUROC hides imbalance, average precision $0.988 \to 0.78$ at $1\,\%$ prevalence (Example 15.6.2); compare with matrix and $k$-mer baselines |
| Editing | guide activity from the $30$-nt context (Rule Set 2, DeepSpCas9); microhomology pattern scores (Algorithm 15.7.1) give the deletion spectrum and the out-of-frame score ($61\,\%$, Example 15.7.1); inDelphi and FORECasT predict full outcome distributions |

## Questions

1. A convolutional filter of width $6$ has weights $F_{j,b}$ equal to $2$ for the base of TATAAT at each position and $-1$ for the three others, with bias $c = 0$. What does this filter compute, and what does the network see after global max pooling?

   **Answer** By Theorem 15.1.1 the filter is a weight matrix: a window matching TATAAT exactly scores $6 \times 2 = 12$, a window with $m$ mismatches scores $12 - 3m$. After a rectified linear unit and global max pooling the feature is $\max(0, 12 - 3m_{\min})$ with $m_{\min}$ the smallest number of mismatches in the sequence, so the network sees only how well the best match fits and nothing about where it is or how many matches there are. Weighting all mismatches equally makes this filter a consensus matcher; a trained filter has position- and base-dependent weights like a real weight matrix, and extra filters or a pooling over several windows are needed to count sites or use their positions.

2. Compute the receptive field of five dilated convolutions of width $5$ with dilations $1, 2, 4, 8, 16$. How many layers of width $3$ with doubling dilations are needed to see $100$ kb of sequence binned at $128$ bp?

   **Answer** $R = 1 + (5 - 1)(1 + 2 + 4 + 8 + 16) = 1 + 4 \times 31 = 253$ positions. For width $3$, $R = 1 + 2(2^m - 1)$ bins, and $100\,000/128 = 782$ bins require $2^m \ge 391.5$, so $m = 9$ layers ($R = 1023$ bins $= 131$ kb). This is why models that reach $100$ kb use strided convolutions to bin the sequence first and then a dozen dilated layers or attention, rather than hundreds of ordinary convolutions.

3. Why does saturation mutagenesis of a sequence under the network of Example 15.2.1 give exactly zero for every position outside the windows that the filters select?

   **Answer** The output is a weighted sum of the pooled features $h_k = \max_p\max(a_{kp}, 0)$. Changing a base outside the maximizing window of filter $k$ changes activations at other positions, and the maximum does not change unless the modified window overtakes the previous maximum; for a small single-base change this rarely happens. So the logit is unchanged and the ISM value is zero, and the gradient is zero for the same reason: the subgradient of a maximum flows only to the argmax. A model whose output pools over positions more smoothly (log-sum-exp, average pooling, a profile head) spreads attribution over the whole sequence, which is one reason profile models are easier to interpret.

4. A masked protein language model gives, at a position whose wild-type residue is glycine, probabilities $0.45$ for G, $0.25$ for A, $0.02$ for S and $0.001$ for W. Score the substitutions G→A, G→S and G→W by Eq. (15.3), and explain what the pattern suggests about the position.

   **Answer** $\ln(0.25/0.45) = -0.59$, $\ln(0.02/0.45) = -3.11$, $\ln(0.001/0.45) = -6.11$. Alanine is almost as acceptable as glycine, serine much less and tryptophan very unlikely, a gradient by size: the model has learned that this position tolerates only small residues, as in a tight turn or a packed interface. The scores are relative likelihoods under the model of natural sequences, not free energies, although they correlate with measured effects; they also assume that the rest of the sequence is wild type, which is why multiple mutants are scored only approximately by summing.

5. A classifier of binding sites has sensitivity $0.9$ and is applied to a genome in which one window in $1000$ is a true site. What precision does it reach at a false positive rate of $10^{-2}$, $10^{-3}$ and $10^{-4}$? What does this imply for the metric to report?

   **Answer** With $\mathbb{P}(\text{site}) = 10^{-3}$, precision $= 0.9 \times 10^{-3}/(0.9\times10^{-3} + \mathrm{FPR} \times 0.999)$: $8.3\,\%$, $47.4\,\%$ and $90.0\,\%$. One point of the ROC curve therefore means completely different things depending on prevalence, while the ROC curve itself is unchanged by it. For rare events the precision–recall curve and its area, computed at the prevalence of the application, are the informative summary, and a model trained on balanced data must be recalibrated or re-thresholded before genome-wide use.

6. In Example 15.6.1 the accuracy with a random split is $100\,\%$ although the label cannot be predicted from sequence. Where exactly does the information come from, and why do clustered splits at $65\,\%$ identity not remove it?

   **Answer** The label is constant within a superfamily, and a random split leaves, for almost every test sequence, several members of its own family (about $90\,\%$ identity) in the training set; the nearest neighbor is then a relative with the same label, so the classifier is really recognizing the superfamily, and the test set measures memorization of relatives rather than generalization. Clustering at $65\,\%$ identity separates families but not superfamilies, since members of different families of one superfamily share only about $54\,\%$ of positions and are not linked into one cluster; the training set still contains the same superfamily with the same label. Only a threshold that merges the superfamily into one cluster, here around $55\,\%$, or an explicit split by superfamily, gives the true $50\,\%$.

7. Two models of enhancer activity are compared: a deep network with AUROC $0.93$ on a random split, and a logistic regression on $6$-mer counts with AUROC $0.90$ on the same split. What should be done before concluding that the network is better?

   **Answer** Repeat both on a split that separates homologous and overlapping regions (by chromosome or by clusters of sequence identity), since the deep model has more capacity to memorize and loses more under a strict split; make sure the negatives are matched in GC content and length, otherwise both models may be classifying composition; report average precision at the prevalence of the intended application as well as AUROC; tune the baseline as carefully as the network ($k$-mer length, regularization) and train both on the same data; repeat over several initializations and splits and report the spread, which for data sets of a few thousand sequences is often of the order of the difference claimed. If the difference survives, ask what the network uses that the baseline cannot represent (spacing, orientation, long-range context) and test it by attribution and by designed sequences.

8. At a Cas9 cut the flanks are GGCCTTGAAGCCTGAAGG and CCTGAAGGTACCTTGCAT. Find the dominant microhomology deletion by Algorithm 15.7.1 and decide whether this site is suitable for making a knockout.

   **Answer** The longest microhomology is CCTGAAGG, present at the end of the left flank and at the start of the right flank; keeping one copy deletes $8$ bp, and with $n_{\mathrm{GC}} = 5$, $n_{\mathrm{AT}} = 3$ the score is $100\,\mathrm{e}^{-8/20}(10 + 3) = 871$, which is $38\,\%$ of the total of all nine products; the next are a $15$-bp deletion on TGAAG ($14\,\%$) and a $16$-bp deletion on CCT ($10\,\%$). The out-of-frame score is $72\,\%$, higher than the $61\,\%$ of Example 15.7.1, because the dominant $8$-bp deletion is itself a frameshift: the site is well suited to a knockout, and a large fraction of edited alleles will carry the same, easily genotyped $8$-bp deletion. For a precise in-frame edit the same property would be a drawback.

9. (Design) A laboratory has ChIP-seq peaks for a transcription factor in one cell type ($15\,000$ peaks) and wants a model that predicts binding from sequence and identifies the motif and its cofactors. Describe the data, the model, the evaluation and the interpretation.

   **Answer** Take the $200$–$1000$ bp around peak summits as positives and, as negatives, genomic regions matched in GC content, length, repeat content and distance from transcription start sites, or dinucleotide-shuffled versions of the positives, which prevents the model from learning composition ([7.8.8](/7.8.8#sec-8.4.5)); mask repeats or keep them deliberately and check their contribution later. Split by chromosome and remove regions that overlap between folds, so that no peak appears in two sets. Begin with baselines: a scan with the known matrix if there is one, and a $k$-mer logistic regression. Then train a convolutional network with a few tens of filters of width $15$–$25$, pooling and one or two further layers, with early stopping on the validation chromosomes, and report AUROC and average precision at a realistic prevalence. Interpret with saturation mutagenesis on strongly predicted peaks and TF-MoDISco on the attributions: the primary motif should emerge, and additional recurring patterns are candidate cofactor motifs. Test their relevance by planting the primary and candidate motifs together in random sequence at varying spacings and predicting the output, and validate against independent evidence: enrichment of the candidate motif in the peaks (AME), centrality at summits, expression of the candidate factor in the cell type, and ChIP-seq of that factor.

10. (Open) Models such as Enformer predict chromatin and expression across cell types well from the reference genome but poorly explain differences in expression between individuals. Give possible reasons and an experiment or analysis that would distinguish them.

    **Answer** Several reasons are plausible. (a) The signal that drives the training loss is the difference between loci, which is dominated by promoter composition, CpG islands and gene structure; the variation between individuals at one locus is much smaller and contributes almost nothing to the loss. (b) Causal variants are often far from the gene, in enhancers whose contribution the model may attribute to the wrong element, and many eQTL associations point to a tagging variant rather than the causal one ([7.4.25](/7.4.25)). (c) The measured variation includes effects the model cannot see: *trans* effects, environment, cell composition of the sample and technical covariates. (d) Training on one reference genome gives no examples of how a single substitution changes the output, so the model is never penalized for a wrong derivative. To distinguish them, evaluate on data where the causal variant is known and the effect is measured directly: massively parallel reporter assays of allele pairs, allele-specific expression and accessibility in heterozygotes (which removes *trans* and environmental effects), and sequences edited at single sites. Compare the model's predicted difference with the measured difference, separately for variants inside and outside the main predicted element, and compare with a model fine-tuned on personal genomes and individual expression; if fine-tuning on variation repairs the predictions, the objective rather than the architecture was the limitation.
