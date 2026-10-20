---
title: "Introduction: The Development of Artificial Intelligence"
description: What artificial intelligence is; the Turing test and the Chinese room; AI as definition plus algorithm; the methods and bottlenecks of five eras (symbolic, knowledge, feature, data, large models); three case studies (Deep Blue, AlphaGo, ChatGPT); the state of large models in 2026 and the limits of deep learning; the contents of this course.
source_hash: c1592bb0cc92
---

Artificial intelligence studies how to make machines perform tasks that require intelligence: playing board games, proving theorems, understanding images, understanding language, and planning actions. Over seven decades the field has gone through several cycles of boom and bust. Each era has had a dominant method, and each method has hit a bottleneck it could not get past: logical reasoning requires people to write down rules, expert systems require people to organize knowledge, statistical learning requires people to design features, deep learning requires large amounts of labeled data, and large models require vast amounts of data and compute. This chapter first discusses what "intelligence" means and how to test for it, then traces the development of AI through five eras, uses three case studies (Deep Blue, AlphaGo, and ChatGPT) to show how methods have evolved, and finally describes how the rest of the course is organized. The technical details of deep learning and large models are developed in [4.7 Artificial Neural Networks](/4.7), and the methodology of machine learning in [4.6 Introduction to Machine Learning](/4.6).

## 1.1. What Is Artificial Intelligence

### 1.1.1. The Birth of Artificial Intelligence

Building thinking machines is an ancient dream. Turning it into a science had to wait for two developments: a precise characterization of "computation" itself, and the appearance of the electronic computer. In 1936, Turing introduced the **Turing machine** in his paper "On Computable Numbers, with an Application to the Entscheidungsproblem," giving a precise definition of "mechanical computation"; general-purpose electronic computers appeared in the 1940s. In 1950, Turing published "Computing Machinery and Intelligence," which opens with the question: "Can machines think?"

In the summer of 1956, John McCarthy, Marvin Minsky, Nathaniel Rochester, and Claude Shannon organized a two-month workshop at Dartmouth College in the United States. In their 1955 proposal they wrote that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it. The term "artificial intelligence" comes from this proposal, and the workshop is usually regarded as the birth of AI as a field.

**Definition 1.1.1 (Artificial Intelligence)** The science that studies how to build artificial intelligent machines or systems that simulate, extend, and expand human intelligent activities (perception, reasoning, learning, decision making, communication, and so on) is called **artificial intelligence**.

This definition can be read in two ways. One focuses on being "humanlike": making a machine behave or think the way humans do. The other focuses on "doing well": making a machine perform tasks rationally and as well as possible, whether or not it resembles a human. Modern AI textbooks (such as Russell and Norvig's *Artificial Intelligence: A Modern Approach*) mainly adopt the latter view and regard AI as the study of rational agents: an agent perceives its environment and takes actions so as to maximize some performance measure.

### 1.1.2. The Turing Test and the Chinese Room

"Intelligence" is hard to define, so Turing replaced the question with an operational one.

**Definition 1.1.2 (Turing Test)** An interrogator converses through a text terminal with a human and a machine at the same time, without seeing either. The interrogator may ask any question and, after a fixed time, must decide which one is the machine. If the interrogator cannot reliably tell them apart, the machine is considered to have passed the test and to be intelligent. This test is called the **Turing test** (Turing himself called it the "imitation game").

The significance of the Turing test is that it turns the philosophical question "Can machines think?" into a behavioral test: we judge whether other people are intelligent only by what they say and do. The test also has clear limitations. It examines only linguistic behavior, and it measures being "humanlike" rather than being "capable." A system can pass by exploiting human psychological weaknesses (making deliberate typos, dodging questions). Since the 2020s, large language models have become hard to distinguish from people in short text conversations, so the Turing test has lost much of its significance as a research goal, and people have turned to benchmarks of specific tasks to measure capability.

In 1980, the philosopher John Searle proposed the *Chinese room* thought experiment to challenge the claim that passing the Turing test amounts to intelligence.

**Example 1.1.1 (The Chinese Room)** A person who does not understand Chinese is locked in a room with a rule book written in English. The book specifies which string of Chinese symbols to write in response to each string of Chinese symbols received. People outside slip questions written in Chinese through a slot in the door; the person inside looks up the rules in the book and slips the answers back out. To those outside, the person inside appears to understand Chinese, yet the person inside knows nothing about the meaning of these symbols.

Searle's conclusion is that manipulating symbols according to rules (syntax) is not sufficient to produce understanding (semantics), so a computer running a program cannot be said to "understand" anything even if it passes the Turing test. The background of the argument was the story-understanding programs of the time, such as Schank's. Tell such a program, "A man went into a restaurant and ordered a hamburger; when the hamburger arrived it was burned to a crisp, and he stormed out without paying or leaving a tip," then ask, "Did he eat the hamburger?" and it can answer "No." Has it really understood the story? The classic replies to the Chinese room include the "systems reply" (the person in the room does not understand Chinese, but the whole of person, rule book, and room does) and the "robot reply" (if the symbols are connected to perception and action, they acquire meaning). The debate remains unresolved, and large language models have made it newly practical: a model learns statistical relationships among symbols from vast amounts of text, but does it "understand" those symbols?

### 1.1.3. Artificial Intelligence = Definition + Algorithm

The AI methods of different eras share one feature: they first "define" an intelligence problem in a form a computer can handle, and then design an algorithm to solve it. That is,

$$
\text{artificial intelligence} = \text{definition} + \text{algorithm}.
$$
The definition describes the problem: what the states and goals are, and what counts as a good answer; the algorithm turns the intelligence problem into a computational problem. Playing a board game can be defined as search on a game tree ([4.5.3](/4.5.3)), navigation as a shortest-path problem on a graph ([4.5.2](/4.5.2)), and image recognition as a classification problem with labeled data ([4.5.4](/4.5.4)).

The definition is often the hardest step. Take "What is a cat?" as an example. An encyclopedia defines it this way: "Round head and short face; five toes on the forelimbs and four on the hindlimbs, with sharp, curved, retractable claws at the tips of the toes. Nocturnal. Hunts other animals by ambush, and most can climb trees." This definition is useful to a person but nearly useless to a computer: how do you tell from a photograph whether "the claws are retractable"? The methods of the different eras are, to a large extent, answers to the question "who gives the definition, and how": people write rules, people organize knowledge, people design features, or the machine learns from data by itself. This thread runs through the five eras in the next section.

The capability of an AI system also depends on several elements: algorithms, computing power (computational resources), data, and the application scenario together with the people who develop and use the system. The three technical elements trade off differently in different eras: the symbolic era relied almost entirely on algorithms, whereas in the eras of deep learning and large models, data and compute became as important as algorithms.

## 1.2. The Five Eras of AI

The following table summarizes the five eras of AI. The division is rough: the methods of different eras overlap in time, and earlier methods did not disappear. Search, for example, is still an important component of AlphaGo and of reasoning models.

| Era | Approximate years | Core methods | Where knowledge comes from | Bottleneck | Representative figures |
|---|---|---|---|---|---|
| Symbolic (logic) | 1956 to early 1970s | Logical reasoning, search, symbolic calculus | People define symbols and inference rules | Combinatorial explosion; common sense and uncertainty | Newell, Simon, McCarthy |
| Knowledge | 1970s to late 1980s | Expert systems, knowledge engineering | People organize domain knowledge | Knowledge acquisition | Feigenbaum |
| Feature | 1990s to around 2010 | Statistical learning, probabilistic models, optimization | People design features; models learn parameters from data | Feature design | Valiant, Pearl, Vapnik |
| Data | 2012 to around 2020 | Deep learning, representation learning | Models learn features automatically from large amounts of labeled data | Labeled data, interpretability | Hinton, LeCun, Bengio |
| Large models | Around 2020 to the present | Large-scale pre-training, alignment, reasoning, and agents | Models learn by self-supervision from vast amounts of unlabeled data | Compute and data, reliability, cost | |

### 1.2.1. The Symbolic Era

Early AI researchers believed that the essence of intelligence is the manipulation of symbols. Newell and Simon put forward the physical symbol system hypothesis: a physical symbol system has the necessary and sufficient means for general intelligent action. Representative work of this era includes:

- Theorem proving: the Logic Theorist of Newell, Simon, and Shaw (1956) proved 38 of the first 52 theorems in Chapter 2 of *Principia Mathematica*; in 1959, Hao Wang's program proved all the theorems of the **propositional logic** part of *Principia Mathematica* in a few minutes.
- General problem solving: Newell and Simon's General Problem Solver (GPS, 1957) solved formalized problems by means-ends analysis, treating problem solving as search in a state space ([4.1.14](/4.1.14), [4.5.2](/4.5.2)).
- Games: Samuel's checkers program (1950s) improved its evaluation function through self-play and in 1962 defeated a state-level player; it is also an early use of the term "machine learning."
- Machine translation: a 1954 experiment by Georgetown University and IBM translated more than 60 Russian sentences into English using 250 words and 6 grammar rules, which aroused optimistic expectations.
- Programming languages: McCarthy designed LISP (1958), which was the main language of AI research for the next several decades.

The successes of this era were concentrated on "toy problems" with clearly defined rules. Difficulties soon appeared. The first was combinatorial explosion: once a problem grows even a little, the search space grows exponentially. The second was common sense and uncertainty: most real-world knowledge is vague and incomplete, and hard to write as logical rules. Machine translation is the typical case. A widely told joke says that "The spirit is willing but the flesh is weak" was translated into Russian and back into English as "The vodka is good but the meat is rotten." The story is probably apocryphal, but it illustrates the problem with word-by-word translation plus grammar rules: meaning depends on context and common sense. The 1966 ALPAC report in the United States judged the prospects of machine translation to be poor, and related funding was cut sharply; the 1973 Lighthill report in the United Kingdom also criticized AI for failing to deliver on its promises. AI entered its first winter.

### 1.2.2. The Knowledge Era

If general-purpose reasoning methods are not enough, hand the knowledge of domain experts to the computer. Feigenbaum proposed that "knowledge is power": the capability of an intelligent system comes mainly from the specialized knowledge it has, not from the reasoning method itself.

**Definition 1.2.1 (Expert System)** A computer program that stores the knowledge of experts in a domain and uses that knowledge to simulate the experts' reasoning in order to solve problems in that domain is called an **expert system**. It usually consists of a knowledge base (which stores domain knowledge in forms such as rules), an inference engine (which derives conclusions from the knowledge base and known facts), and modules for explanation, knowledge acquisition, and human–computer interaction.

The first expert system was DENDRAL by Feigenbaum and colleagues (from 1965), which inferred the structure of organic molecules from mass spectrometry data. MYCIN (1970s) diagnosed blood infections and recommended antibiotics, handling uncertain reasoning with "certainty factors," and performed on par with specialist physicians in tests. XCON at DEC (1980) configured computer systems for customers and reportedly saved the company tens of millions of dollars a year. Expert systems were the first large-scale commercial application of AI, and Feigenbaum received the 1994 Turing Award for this work.

The central research question of this era was how to represent and use knowledge.

**Definition 1.2.2 (Knowledge Representation)** Describing knowledge in a formal way that a computer can store and process is called **knowledge representation**. Common methods include production rules ("if ... then ..."), first-order predicate logic, semantic networks, and frames.

The engineering method of organizing expert knowledge into a knowledge base and building expert systems is called knowledge engineering, and the corresponding engineers are called knowledge engineers. Reasoning under uncertainty (certainty factors, subjective Bayesian methods, evidence theory, and later Bayesian networks) was used to handle incomplete and imprecise knowledge.

The bottleneck of expert systems was knowledge acquisition. Much of an expert's knowledge is "hard to put into words." How do you ride a bicycle? An experienced rider can hardly write the method of keeping balance as rules, and even if they did, others could not learn to ride by following the rules. The larger a knowledge base, the greater the conflicts among rules and the cost of maintenance; a system works only in a narrow domain and fails completely when it meets a situation outside its knowledge base ("brittleness"). Japan's Fifth Generation Computer project, launched in 1982 with logical reasoning at its core, failed to reach its goals after ten years; around 1987 the market for special-purpose LISP machines collapsed, and AI entered its second winter. Lenat's Cyc project, begun in 1984, tried to enter all of human common sense by hand and is still far from complete decades later, which also illustrates the difficulty of this approach.

### 1.2.3. The Feature Era

In the 1990s the mainstream of AI shifted from "people write knowledge" to "learning from data." The statistical learning approach is as follows: people represent the problem as feature vectors and choose a class of models, and the machine estimates the model parameters from labeled data ([4.5.5](/4.5.5) §5.1.1). Representative advances include:

- Learning theory: Valiant's PAC learning theory (1984) gave a precise definition of "learnable" (2010 Turing Award); Vapnik's statistical learning theory and the **support vector machine** (Cortes and Vapnik, 1995) combined margin maximization with kernel methods ([4.5.5](/4.5.5)).
- Probabilistic models: Pearl's Bayesian networks (1988) combined probabilistic inference with graph structure and provided a solid foundation for reasoning under uncertainty (2011 Turing Award); hidden Markov models ([4.6.8](/4.6.8)) became the standard method for speech recognition.
- Decision trees and ensemble methods: ID3, C4.5, CART ([4.5.6](/4.5.6)), random forests, and boosting ([4.6.6](/4.6.6)).
- Optimization: convex optimization and stochastic gradient methods became the core of learning algorithms ([3.5](/3.5)).

The bottleneck of statistical learning lies in features. The performance of a model depends heavily on its input features, and the features are designed by people: MFCC in speech recognition, SIFT and HOG in image recognition, and tf-idf in text classification are all the distilled experience of domain experts over many years. Take speech recognition as an example: how do we extract from a sound wave features that distinguish different phonemes yet are insensitive to the speaker and to noise? This problem resembles "how to ride a bicycle": people can recognize speech but cannot say which features they use. Most models of this era were "shallow": a single (kernel) feature map followed by a linear model.

### 1.2.4. The Data Era

The idea of deep learning is that features are no longer designed by people. Instead, a multilayer neural network automatically learns features at different levels of abstraction from raw data (pixels, sound waves, characters): edges and strokes at the low levels, parts and objects at the high levels ([4.5.4](/4.5.4) §4.1.2). This kind of "deep feature mapping" is also called representation learning.

The ideas behind neural networks are old: the McCulloch–Pitts neuron (1943), Rosenblatt's perceptron (1958), backpropagation (1986), and LeCun's convolutional networks (used from 1989 for handwritten ZIP code recognition). They regained attention around 2006 (Hinton and colleagues' deep belief networks) and achieved a breakthrough in 2012: AlexNet, a convolutional network trained on GPUs by Krizhevsky and others, students of Hinton, cut the top-5 error rate in the ImageNet classification competition from about 26% to about 15%, far ahead of all methods based on hand-designed features. In the same period, deep networks greatly reduced the error rate of speech recognition. Three conditions matured at once: large-scale labeled data brought by the Internet (ImageNet has over a million labeled images), computing power provided by GPUs, and training techniques such as ReLU and dropout. Over the following years deep learning replaced the older methods across vision, speech, and machine translation; the error rate of ResNet (2015) on ImageNet was already below that of human annotators; and AlphaGo (2016) and AlphaFold (which in 2020 approached experimental accuracy in protein structure prediction) extended it to games and scientific problems. Hinton, LeCun, and Bengio received the 2018 Turing Award; in 2024, Hopfield and Hinton received the Nobel Prize in Physics for foundational work on neural networks, and Hassabis and Jumper shared the Nobel Prize in Chemistry with Baker for AlphaFold.

The problems of deep learning are also clear. Compared with humans:

| Deep learning | Humans |
|---|---|
| Needs large amounts of labeled data | Learn from a few examples |
| Black box, hard to interpret | Can explain their reasons |
| Trained once; learning new knowledge easily overwrites old knowledge | Learn continually and incrementally |
| Stubborn: confident even in wrong outputs, hard to correct | Correct their mistakes |
| Relies on statistical correlation and errs on out-of-distribution data | Reason from understanding and causality |

For example, adding a tiny perturbation that the human eye cannot perceive to an image can make a classification network give a wrong answer with very high confidence (adversarial examples). The most direct bottleneck among these is labeled data: collecting and labeling large amounts of data for every task is expensive.

### 1.2.5. The Large-Model Era

The way to break through the labeling bottleneck is self-supervised learning: constructing supervision signals from the data itself. For text, the most natural task is "predicting the next word." A language model gives

$$
\mathbb{P}(w_t \mid w_1 w_2 \cdots w_{t-1}),
$$
that is, it predicts the $t$-th **token** from the preceding $t - 1$ tokens. Any piece of text automatically supplies training examples, with no manual labeling. A traditional $n$-gram language model looks only at the previous $n - 1$ words and estimates probabilities from counts (the bigram model in [4.5.2](/4.5.2) §2.4.2); a neural language model represents this conditional distribution with a neural network and can use a much longer context.

Several key developments:

- In 2017, the Transformer architecture ([4.7.6](/4.7.6)) replaced recurrent networks with the attention mechanism, making large-scale parallel training on GPUs convenient.
- In 2018–2020, pre-trained models such as BERT, GPT-2, and GPT-3 ([4.7.7](/4.7.7)) showed that a model pre-trained on vast amounts of text can perform a wide range of language tasks with a little fine-tuning, or even none. GPT-3 (2020) has 175 billion parameters. Scaling laws show that a model's loss decreases smoothly as a power law in the number of parameters, the amount of data, and the amount of compute, so "making it bigger" became a route with predictable returns.
- In November 2022, OpenAI released ChatGPT. Built on models of the GPT-3.5 series, with instruction tuning and reinforcement learning from human feedback (RLHF: first train a reward model that predicts human preferences, then use reinforcement learning to make the model's answers better match them), it became a general-purpose assistant capable of multi-turn dialogue and instruction following. It reportedly exceeded 100 million users within two months, making large models a technology of wide public attention.
- From 2023, models such as GPT-4 can process multiple modalities, including images; open-weight models such as Meta's LLaMA allow researchers to study and improve large models locally.
- In 2024–2025, **reasoning models** ([4.2.14](/4.2.14)) generate a long chain of thought before answering and are trained for reasoning with **reinforcement learning with verifiable rewards**, making great progress in mathematics and programming. In July 2025, Google DeepMind's Gemini Deep Think and an experimental OpenAI model both reached the gold-medal threshold at the International Mathematical Olympiad (the former graded by the competition's officials). DeepSeek-V3 (December 2024) is a mixture-of-experts model with 671 billion total parameters, 37 billion of them activated per token, trained on 14.8 trillion tokens; the official training run used only 2048 H800 GPUs and about 2.79 million GPU hours (about 5.6 million US dollars at rental prices, excluding earlier research and experiments). The open-source DeepSeek-R1 (January 2025) that followed published a method for training reasoning ability with reinforcement learning and significantly lowered the cost barrier to the frontier.
- In 2025–2026, models increasingly work as agents: calling tools, browsing the web, operating computers, and autonomously completing multi-step tasks in code repositories (**coding agents**, [4.2.14](/4.2.14)). According to Stanford University's *AI Index Report 2026*, the task success rate of agents on the OSWorld benchmark, which uses real computers, rose from about 12% to about 66%, still below humans and with roughly one failure in three on structured tasks; the performance gap between the top American and Chinese models has become very small.

The abilities of large models show a "jagged frontier": the same model that can win a gold medal at the Mathematical Olympiad reads an analog clock correctly only about half the time. Their main problems are: confidently producing wrong content (hallucination); knowledge that is frozen once training is finished, making continual learning difficult; the enormous compute and energy required for training and inference; and alignment and safety, that is, how to ensure that increasingly capable systems act in accordance with human intentions. These problems, and the architectures, training, and alignment methods of large models, are discussed in [4.7.9](/4.7.9).

## 1.3. Three Case Studies

### 1.3.1. Deep Blue

In May 1997, IBM's Deep Blue defeated the world chess champion Kasparov 3.5 to 2.5 (in their first match in February 1996, Deep Blue had lost 2 to 4). Deep Blue's algorithmic framework was game-tree search with alpha–beta pruning ([4.5.3](/4.5.3) §3.3): its special-purpose chips searched about 200 million positions per second, and its evaluation function was designed and tuned with the participation of chess grandmasters. Its victory can be summarized as

$$
\text{expert knowledge} + \text{search (}\alpha\text{-}\beta\text{ pruning)}.
$$
Deep Blue's success depended on the participation of chess grandmasters, and also on the nature of chess itself: the values of the pieces are well defined, so positions are easy to evaluate with hand-designed features. In 2006, to mark the 50th anniversary of the birth of AI, the Chinese Association for Artificial Intelligence organized a human–computer match in Chinese chess (xiangqi), in which 5 xiangqi programs played 5 grandmasters, including Liu Dahua; the machines won 11 to 9 overall.

### 1.3.2. AlphaGo

The state space of Go is far larger than that of chess, and, more importantly, it is very hard to write a good evaluation function. In March 2016, DeepMind's AlphaGo defeated Lee Sedol 4 to 1, and in May 2017 it defeated Ke Jie 3 to 0. AlphaGo's framework is Monte Carlo tree search, using a policy network to narrow the breadth of the search and a value network to evaluate positions; the networks first learned from 160,000 human games and were then strengthened through self-play ([4.5.3](/4.5.3) §3.7):

$$
\text{human data} + \text{Monte Carlo tree search} + \text{deep learning}.
$$
Unlike Deep Blue, it did not need Go masters to take part directly in designing the evaluation. AlphaGo Zero (2017) went further: using no human game records or hand-designed features, it learned entirely from scratch by self-play, defeating the version that had beaten Lee Sedol 100 to 0 after only 3 days of training, and surpassing the version that had beaten Ke Jie after 40 days.

Does "learning from scratch" mean that it dispensed with data? Not at all. Board games are special: the rules are completely known and the winner can be determined automatically, so unlimited training data can be generated by the system itself. It still fundamentally relies on data, only the data is produced by self-play. Most real-world problems do not have such clear rules and automatic judging, so this method does not extend to them directly.

### 1.3.3. ChatGPT

GPT stands for generative pre-trained Transformer. "Generative" means that it generates tokens one at a time, like a word-chain game: given "The capital of France is," it generates "Paris" and then continues token by token. "Pre-trained" means that it is first trained on vast amounts of text by self-supervised next-token prediction (§1.2.5), learning the regularities of language and a great deal of knowledge. The Transformer is its network architecture ([4.7.6](/4.7.6)). On top of this, ChatGPT is fine-tuned with instruction data and aligned with reinforcement learning from human feedback, turning a model that "continues text" into an assistant that "answers questions." Its language understanding, generation, and multi-turn dialogue management far exceed those of earlier dialogue systems; its problems are correctness (hallucination) and continual learning.

The three case studies show how the way of "defining" has changed: for Deep Blue, people defined the evaluation; for AlphaGo, the evaluation was defined by human game records and self-play data; ChatGPT's abilities come almost entirely from statistical learning on text written by humans, and the role of people has shifted to the selection of data and the preferences used for alignment.

## 1.4. Contents of This Course

This course focuses on algorithms; programming practice is mainly in Python, with some C++. The chapters are:

| Chapter | Contents | What you can answer after studying it |
|---|---|---|
| [4.5.2](/4.5.2) Search | Uninformed search, the A\* algorithm and heuristic functions, dynamic programming and Viterbi decoding | How does a navigation system find a route? How is pinyin converted into Chinese characters? |
| [4.5.3](/4.5.3) Adversarial Search | Minimax, alpha–beta pruning, Monte Carlo tree search, AlphaGo | How does a computer play board games? |
| [4.5.4](/4.5.4) Introduction to Neural Networks | Neurons, fully connected networks, backpropagation | What is deep learning? How do we recognize digits? |
| [4.5.5](/4.5.5) Support Vector Machines | Margin maximization, duality and KKT conditions, kernel methods, SMO | How do we implement a classification system? |
| [4.5.6](/4.5.6) Decision Trees | Information gain, ID3, C4.5, CART, pruning | How do we learn interpretable rules from data? |

The deeper material on neural networks (convolutional networks, recurrent networks, Transformers, pre-training, and large models) belongs to [4.7 Artificial Neural Networks](/4.7); experimental methodology for machine learning, Bayesian learning, clustering, ensemble learning, hidden Markov models, and so on belong to [4.6 Introduction to Machine Learning](/4.6). The mathematical prerequisites for this course are calculus, linear algebra, and probability and statistics ([2](/2), [3](/3)); for programming background see [4.1](/4.1) and [4.3](/4.3).

## Summary

- AI studies how to make machines perform tasks that require intelligence; the Turing test examines intelligence through behavior, while the Chinese room questions whether symbol manipulation can produce understanding.
- Artificial intelligence = definition + algorithm: define the intelligence problem as a computational problem, then solve it with an algorithm. The eras differ mainly in who gives the "definition" and how.
- Five eras: the symbolic era relied on people writing rules, with the bottleneck of combinatorial explosion and common sense; the knowledge era relied on expert systems, with the bottleneck of knowledge acquisition; the feature era relied on statistical learning, with the bottleneck of feature design; the data era relied on deep learning to learn features automatically, with the bottleneck of labeled data and interpretability; the large-model era relies on self-supervised pre-training on vast data plus reinforcement learning, with problems of reliability, continual learning, and cost.
- Deep Blue = expert knowledge + alpha–beta pruning; AlphaGo = human data + Monte Carlo tree search + deep learning; ChatGPT = generative pre-trained Transformer + reinforcement learning from human feedback.
