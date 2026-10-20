---
title: Introduction to Neural Networks
description: Understanding the neuron through template matching for digit recognition; activation functions (sign, sigmoid, tanh, ReLU, softmax), fully connected networks, and the universal approximation theorem; loss functions (squared error and cross-entropy), the three forms of gradient descent, and the derivation of the backpropagation algorithm; training a network on the XOR problem with backpropagation.
source_hash: aadb2b6ce4d0
---

The search methods of the previous two chapters require people to write down the rules and the evaluation of a problem; AlphaGo in the previous chapter, by contrast, used neural networks to learn evaluations and moves from data. This chapter introduces the basic concepts of neural networks starting from a concrete problem: how to make a computer recognize handwritten digits. We will see that a single neuron is one act of "template matching," that connecting many neurons in layers can combine them into complex patterns, and that the patterns (the weights of the network) are not designed by people but learned automatically from labeled examples by gradient descent and backpropagation. This chapter covers only the most basic fully connected networks and training algorithm; deeper material such as convolutional networks, training techniques, recurrent networks, and Transformers is in [4.7 Artificial Neural Networks](/4.7), and the theory of optimization methods is in [3.5.5](/3.5.5).

## 4.1. Starting from Digit Recognition

### 4.1.1. Template Matching

Suppose a digit image is a $15 \times 15$ black-and-white dot matrix, flattened row by row into a vector $\boldsymbol{x} = (x_1, \dots, x_n)$ with $n = 225$, where a black dot is $1$ and a white dot is $0$. How do we decide whether it is the digit 3? A naive idea is to design a template $\boldsymbol{w} = (w_1, \dots, w_n)$ for the digit 3: positions through which the strokes of a 3 pass get $1$; positions through which the strokes of a 3 never pass but those of other digits often do (for example the left side of a 3, where an 8 has strokes) get $-1$; the rest get $0$. The degree of match between the image and the template is measured by the inner product:

$$
\mathrm{net} = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n = \boldsymbol{w} \cdot \boldsymbol{x}.
$$
The more strokes coincide with the positions of $1$ in the template, the larger $\mathrm{net}$ is; strokes falling on positions of $-1$ are penalized. So an image of a 3 scores high, while an image of an 8, although it covers all the strokes of a 3, has strokes on its left side that fall on positions of $-1$ and so scores lower.

Comparing $\mathrm{net}$ directly has a problem: its size depends on the number of strokes. The digit 1 has few strokes, so even a perfect match scores lower than a digit with many strokes; different templates have no common scale, and there is no way to judge "how large counts as a match." The remedy is to add a bias $b$ and then use a monotone function to squeeze the score into $(0, 1)$:

$$
y = \sigma(\boldsymbol{w} \cdot \boldsymbol{x} + b), \qquad \sigma(z) = \frac{1}{1 + \mathrm{e}^{-z}}.
$$
$-b$ acts as the "passing line": for example, if an image of a 3 scores 143 and an image of an 8 scores 115, taking $b = -129$ gives $\sigma(14) \approx 0.999999$ and $\sigma(-14) \approx 0.000001$, and the output can be interpreted as "the degree to which this is a 3."

### 4.1.2. From Neurons to Networks

The computing unit above is a neuron. Setting up one template for each digit gives 10 neurons in parallel with outputs $y_0, \dots, y_9$, and the image is classified as digit $k$ when the $k$-th output is largest. This extends the network in "width": increasing the number of patterns. The same digit can be written in different ways, so several templates may also be set up for it.

The drawback of whole-digit templates is inflexibility: if the digit is written slightly off-center or slanted, the match fails. Noticing that 3 and 8 have the same right half and different left halves, we can first use one layer of neurons to detect "local patterns," such as "the upper right arc," "the lower left arc," and "the middle horizontal bar," and then use the next layer of neurons to combine the local patterns into a whole digit: 3 = upper right arc + lower right arc + middle bar, 8 = 3 + upper left arc + lower left arc. This extends the network in "depth": the more layers, the more abstract the combinations of patterns. The result is a multilayer neural network: the input layer receives pixels, several hidden layers extract increasingly abstract patterns layer by layer, and the output layer gives the classification.

The most crucial point is that patterns are represented by the connection weights of the neurons, and these weights are not designed by hand but learned automatically from training examples. The learned patterns are an implicit representation and are generally not as clearly readable as the "arcs" and "bars" in the example above.

## 4.2. Neurons and Neural Networks

### 4.2.1. The Neuron

**Definition 4.2.1 (Neuron)** A **neuron** receives inputs $\boldsymbol{x} = (x_1, \dots, x_n)$, computes the weighted sum

$$
\mathrm{net} = \sum_{i=1}^{n} w_i x_i + b,
$$
and outputs $o = g(\mathrm{net})$. Here $w_i$ are the connection weights, $b$ is the bias, and $g$ is the activation function.

Setting $x_0 = 1$ and $w_0 = b$, the bias can be absorbed into the weights: $\mathrm{net} = \sum_{i=0}^{n} w_i x_i = \boldsymbol{w} \cdot \boldsymbol{x}$. This model comes from McCulloch and Pitts's (1943) abstraction of the biological neuron: dendrites receive signals, the cell body integrates them, and the axon fires when a threshold is exceeded. Taking $g$ to be the sign function gives Rosenblatt's (1958) perceptron; its learning algorithm and limitations are in [4.7.2](/4.7.2).

### 4.2.2. Activation Functions

**Definition 4.2.2 (Activation Function)** The function $g$ in a neuron that maps the weighted sum $\mathrm{net}$ to the output is called the **activation function**. Commonly used ones are:

- the sign function $\operatorname{sgn}(z) = 1$ ($z \ge 0$), $-1$ ($z < 0$);
- the sigmoid function $\sigma(z) = \dfrac{1}{1 + \mathrm{e}^{-z}}$, with values in $(0, 1)$ and $\sigma'(z) = \sigma(z)\bigl(1 - \sigma(z)\bigr)$;
- the hyperbolic tangent $\tanh z = \dfrac{\mathrm{e}^{z} - \mathrm{e}^{-z}}{\mathrm{e}^{z} + \mathrm{e}^{-z}} = 2\sigma(2z) - 1$, with values in $(-1, 1)$ and $\tanh' z = 1 - \tanh^2 z$;
- the rectified linear function $\operatorname{ReLU}(z) = \max(0, z)$, whose derivative is 1 for $z > 0$ and 0 for $z < 0$.

![The four activation functions (solid lines) and their derivatives (dashed lines): the derivative of the sign function is 0 almost everywhere, so it cannot be used with gradient descent; sigmoid and tanh have derivatives tending to 0 for large |z| (saturation); ReLU has derivative exactly 1 on the positive half-line](./plots/activations.py)

The activation function must be nonlinear: if $g$ were linear, the composition of a multilayer network would still be a linear map, and deepening the network would add no expressive power. The sign function is discontinuous and has zero derivative almost everywhere, so it cannot be trained by gradients; sigmoid and tanh are smooth, but their derivatives tend to zero when $\lvert z\rvert$ is large, so the error signal grows weaker and weaker after passing through many layers (vanishing gradients, see [4.7.4](/4.7.4)). ReLU is cheap to compute and does not saturate on the positive half-line; it has been the default choice for hidden layers since the 2010s, and today's large models mostly use its smooth variants (GELU, SwiGLU, and so on).

For classification, the output layer often uses softmax to turn the weighted sums $\mathrm{net}_1, \dots, \mathrm{net}_K$ of the $K$ output neurons into a probability distribution.

**Definition 4.2.3 (Softmax Function)** The **softmax function** maps a vector $(z_1, \dots, z_K)$ to

$$
o_k = \frac{\mathrm{e}^{z_k}}{\sum_{j=1}^{K} \mathrm{e}^{z_j}}, \qquad k = 1, \dots, K.
$$
It satisfies $0 < o_k < 1$ and $\sum_k o_k = 1$, and preserves the order of the components.

Softmax is a smooth version of the "maximum": if all the $z_k$ are multiplied by a large positive number, its output tends to the one-hot vector that is 1 at the largest component. In computation, first subtract $\max_k z_k$ and then exponentiate, which leaves the result unchanged while avoiding overflow. For $K = 2$, $o_1 = \sigma(z_1 - z_2)$, which is the sigmoid.

### 4.2.3. Fully Connected Networks

**Definition 4.2.4 (Fully Connected Network)** The neurons are arranged in layers: an input layer, one or more hidden layers, and an output layer. Every neuron in each layer is connected to all neurons in the next layer, there are no connections within a layer or across non-adjacent layers, and signals propagate in one direction only, from input to output. Such a network is called a **fully connected network**, also called a feedforward network or multilayer perceptron (MLP); each of its layers is called a fully connected layer or dense layer.

In matrix form, let the weight matrix of layer $l$ be $W^{(l)}$ (row $j$ holds the weights of the $j$-th neuron of layer $l$) and the bias vector be $\boldsymbol{b}^{(l)}$. Then

$$
\boldsymbol{z}^{(l)} = W^{(l)}\boldsymbol{o}^{(l-1)} + \boldsymbol{b}^{(l)}, \qquad \boldsymbol{o}^{(l)} = g\bigl(\boldsymbol{z}^{(l)}\bigr), \qquad l = 1, \dots, L,
$$
where $\boldsymbol{o}^{(0)} = \boldsymbol{x}$ is the input, $g$ acts componentwise, and $\boldsymbol{o}^{(L)}$ is the output of the network. One layer is a matrix multiplication followed by a componentwise nonlinear transformation, which is also why neural networks are well suited to computation on GPUs.

A single hidden layer is enough to approximate any continuous function:

**Theorem 4.2.1 (Universal Approximation Theorem)** Let $g$ be a continuous function that is not a polynomial, and let $K \subset \mathbb{R}^n$ be compact. Then for any continuous function $f\colon K \to \mathbb{R}$ and any $\varepsilon > 0$, there exist $N$ and $a_j, b_j \in \mathbb{R}$, $\boldsymbol{w}_j \in \mathbb{R}^n$ such that

$$
\Bigl\lvert f(\boldsymbol{x}) - \sum_{j=1}^{N} a_j\, g(\boldsymbol{w}_j \cdot \boldsymbol{x} + b_j)\Bigr\rvert < \varepsilon \quad \text{for all } \boldsymbol{x} \in K.
$$

The case of the sigmoid activation was proved by Cybenko (1989), and general non-polynomial activations by Leshno et al. (1993). The theorem guarantees only existence: it does not say how many neurons are needed (possibly exponentially many in the dimension), nor whether these parameters can be found by training. In practice, deep and narrow networks often achieve the same effect with fewer parameters than shallow and wide ones, because a deep network can reuse the patterns of intermediate layers, which is exactly the intuition of "combining patterns" in §4.1.2.

## 4.3. Training Neural Networks

### 4.3.1. Datasets

Just as a child learning about animals must first see many animals and be told their names, training a network first requires data: collect a large number of examples (photographs in different poses, angles, and sizes; digits written by different people) and label each example with the correct answer. Training a model with labeled examples is **supervised learning**. The data are generally split into a training set and a test set: the weights are adjusted on the training set, and the model is evaluated on the test set that it has not seen during training; when tuning hyperparameters such as the network structure, a validation set is split off as well, or **cross-validation** ([3.4.10](/3.4.10)) is used. Performing well only on the training set and poorly on new data is **overfitting**. Experimental methods and evaluation metrics are in [4.6.2](/4.6.2).

### 4.3.2. Loss Functions

The goal of training is to make the network's output $o_k$ close to the desired output $t_k$ (the label). The gap between the two is measured by a **loss function**, and training means finding the weights $\boldsymbol{w}$ that minimize the loss. The most direct choice is the sum of squared errors: for example $d$,

$$
E_d(\boldsymbol{w}) = \frac12 \sum_{k=1}^{M} (t_{kd} - o_{kd})^2, \qquad E(\boldsymbol{w}) = \sum_{d=1}^{D} E_d(\boldsymbol{w}),
$$
where $M$ is the number of output neurons, $D$ is the number of examples, and $t_{kd}$, $o_{kd}$ are the desired and actual values of the $k$-th output for example $d$. The factor $\frac12$ is only there to cancel the 2 after differentiation.

For classification problems cross-entropy is more commonly used.

**Definition 4.3.1 (Cross-Entropy Loss)** Suppose the network output $\boldsymbol{o}_d$ is a probability distribution (such as the output of softmax), and the desired output $\boldsymbol{t}_d$ is also a probability distribution. The **cross-entropy loss** of example $d$ is

$$
H_d(\boldsymbol{w}) = -\sum_{k=1}^{M} t_{kd} \log o_{kd},
$$
and the total loss is $H(\boldsymbol{w}) = \sum_{d=1}^{D} H_d(\boldsymbol{w})$.

In classification, the desired output of example $d$ is 1 only at the correct class $c_d$ and 0 elsewhere (a one-hot vector), and the cross-entropy reduces to $H_d = -\log o_{c_d d}$: the closer the predicted probability of the correct class is to 1, the closer the loss is to 0; as the predicted probability approaches 0 the loss tends to infinity. Minimizing the cross-entropy is equivalent to maximizing the log-likelihood of the training data, that is, **maximum likelihood estimation** ([3.2.3](/3.2.3)).

The division of labor between the two losses: the sum of squared errors is used for regression problems whose outputs are concrete numerical values, and cross-entropy is used for classification problems. Pairing softmax with cross-entropy also has a computational benefit: the partial derivative of $H_d$ with respect to the softmax input $z_k$ is exactly

$$
\frac{\partial H_d}{\partial z_k} = o_{kd} - t_{kd},
$$
which is simple and does not shrink because of sigmoid saturation (proof: $\partial o_j / \partial z_k = o_j(\delta_{jk} - o_k)$; substitute and use $\sum_j t_{jd} = 1$).

### 4.3.3. Gradient Descent

Minimizing a loss function generally has no closed-form solution and must be solved iteratively: starting from an initial value, each step modifies the weights in a direction that decreases the loss. The negative gradient direction is the direction of locally steepest descent, which gives **gradient descent** ([3.5.5](/3.5.5)):

$$
\boldsymbol{w} \leftarrow \boldsymbol{w} - \eta\, \nabla_{\boldsymbol{w}} E(\boldsymbol{w}), \qquad \nabla_{\boldsymbol{w}} E = \Bigl(\frac{\partial E}{\partial w_1}, \dots, \frac{\partial E}{\partial w_n}\Bigr),
$$
where $\eta > 0$ is the learning rate (step size). The direction of the modification is determined by the gradient, and its size is controlled by $\eta$: if $\eta$ is too large the iterates oscillate back and forth across the valley or even diverge, and if it is too small convergence is very slow.

According to the number of examples used in each update, there are three forms:

| Name | Examples used per update | Characteristics |
|---|---|---|
| Batch gradient descent | All $D$ examples, $E = \sum_d E_d$ | Accurate direction, but the cost of each step grows with the amount of data |
| **Stochastic gradient descent** | 1 example, $E_d$ | Cheap steps, noisy direction; the noise sometimes helps escape poor local minima |
| **Mini-batch gradient descent** | $B$ examples (for example 32–4096) | A compromise between the two, easy to parallelize on GPUs, and the standard practice in deep learning |

In practice the term "stochastic gradient descent" (SGD) often also refers to the mini-batch version. Improved optimizers such as momentum and Adam and learning-rate schedules are in [4.7.4](/4.7.4).

### 4.3.4. Backpropagation

Gradient descent needs the partial derivative of the loss with respect to every weight. A network has thousands, or even trillions, of weights, and approximating each partial derivative by finite differences would require recomputing the whole network for each one, at an unacceptable cost. Backpropagation uses the **chain rule** to obtain all the partial derivatives with just one forward computation and one backward computation.

We derive it first for sigmoid activation, the sum-of-squared-errors loss, and stochastic gradient descent on a single example $d$ (dropping the subscript $d$). Let $x_{ji}$ be the $i$-th input of neuron $j$, $w_{ji}$ the corresponding weight, $\mathrm{net}_j = \sum_i w_{ji} x_{ji}$, and $o_j = \sigma(\mathrm{net}_j)$. The weight $w_{ji}$ affects the loss only through $\mathrm{net}_j$, so

$$
\frac{\partial E}{\partial w_{ji}} = \frac{\partial E}{\partial \mathrm{net}_j} \cdot \frac{\partial \mathrm{net}_j}{\partial w_{ji}} = \frac{\partial E}{\partial \mathrm{net}_j}\, x_{ji}.
$$
Let $\delta_j = -\dfrac{\partial E}{\partial \mathrm{net}_j}$ (called the error term of neuron $j$). Then the weight update is

$$
\Delta w_{ji} = -\eta \frac{\partial E}{\partial w_{ji}} = \eta\, \delta_j\, x_{ji}.
$$
It remains to compute $\delta_j$, in two cases.

For an output-layer neuron $k$: only one term of $E = \frac12\sum_k (t_k - o_k)^2$ contains $o_k$, so

$$
\delta_k = -\frac{\partial E}{\partial o_k} \cdot \frac{\partial o_k}{\partial \mathrm{net}_k} = (t_k - o_k)\, o_k (1 - o_k).
$$

For a hidden-layer neuron $h$: it affects the loss through all its successor neurons (the neurons in the next layer connected to it); denote the set of successors by $\operatorname{Ds}(h)$. Since $\mathrm{net}_k = \sum_j w_{kj} o_j$, we have $\partial \mathrm{net}_k / \partial o_h = w_{kh}$, so

$$
\delta_h = -\sum_{k \in \operatorname{Ds}(h)} \frac{\partial E}{\partial \mathrm{net}_k} \cdot \frac{\partial \mathrm{net}_k}{\partial o_h} \cdot \frac{\partial o_h}{\partial \mathrm{net}_h} = o_h (1 - o_h) \sum_{k \in \operatorname{Ds}(h)} \delta_k\, w_{kh}.
$$
The error term of a hidden layer is obtained as a weighted sum of the error terms of the next layer: the error is "propagated backward" layer by layer from the output layer toward the input layer.

**Algorithm 4.3.1 (Backpropagation, Stochastic Gradient Descent Version)** Initialize all weights to small random numbers (for example uniformly distributed in $[-0.05, 0.05]$). Until a termination condition is met, for each training example:

1. Forward pass: feed the example into the network and compute the output $o_u$ of every neuron $u$ layer by layer;
2. For each output neuron $k$, compute $\delta_k = (t_k - o_k)\, o_k(1 - o_k)$;
3. Going from back to front, for each hidden-layer neuron $h$, compute $\delta_h = o_h(1 - o_h)\sum_{k \in \operatorname{Ds}(h)} \delta_k w_{kh}$;
4. Update each weight: $w_{ji} \leftarrow w_{ji} + \eta\, \delta_j\, x_{ji}$.

This method of efficiently computing all partial derivatives from back to front with the chain rule is called *backpropagation*, abbreviated BP, and also known as error backpropagation. It was proposed independently by several people and became widely known through the work of Rumelhart, Hinton, and Williams (1986).

The derivation above depends on specific conditions: a fully connected network, stochastic gradient descent, sigmoid activation, and the sum of squared errors. With another activation function, one only needs to replace $o(1 - o)$ by $g'(\mathrm{net})$; with cross-entropy and softmax, the error term of the output layer becomes $t_k - o_k$ (§4.3.2). In matrix form, the general version is

$$
\boldsymbol{\delta}^{(L)} = -\nabla_{\boldsymbol{z}^{(L)}} E, \qquad \boldsymbol{\delta}^{(l)} = \bigl(W^{(l+1)\mathsf T}\boldsymbol{\delta}^{(l+1)}\bigr) \odot g'\bigl(\boldsymbol{z}^{(l)}\bigr), \qquad \frac{\partial E}{\partial W^{(l)}} = -\boldsymbol{\delta}^{(l)}\boldsymbol{o}^{(l-1)\mathsf T},
$$
where $\odot$ is the componentwise product. The cost of the backward computation is of the same order as that of the forward computation, that is, proportional to the number of weights. Modern deep learning frameworks (PyTorch, JAX, and others) represent any computation composed of basic operations as a computational graph and carry out this process automatically, which is called automatic differentiation (reverse mode); the user only needs to write the forward computation. The complete derivation, computational graphs, and the various losses and activation functions are in [4.7.2](/4.7.2).

### 4.3.5. Example: The XOR Problem

The four examples of exclusive or, $a \oplus b = (\lnot a \land b) \lor (a \land \lnot b)$, namely $(0,0) \mapsto 0$, $(0,1) \mapsto 1$, $(1,0) \mapsto 1$, $(1,1) \mapsto 0$, cannot be separated by a straight line, so a single neuron cannot represent it ([4.7.2](/4.7.2)); at least one hidden layer is needed. Below we implement a 2–3–1 sigmoid network in numpy and train it with Algorithm 4.3.1; first we check the gradients obtained by backpropagation against central differences.

```python
import numpy as np

rng = np.random.default_rng(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float).T   # one sample per column
T = np.array([[0, 1, 1, 0]], dtype=float)                       # XOR targets

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# A 2-3-1 fully connected network; W has shape (outputs, inputs).
W1, b1 = rng.uniform(-1, 1, (3, 2)), np.zeros((3, 1))
W2, b2 = rng.uniform(-1, 1, (1, 3)), np.zeros((1, 1))

def forward(x):
    h = sigmoid(W1 @ x + b1)
    o = sigmoid(W2 @ h + b2)
    return h, o

def loss(x, t):
    return 0.5 * np.sum((t - forward(x)[1]) ** 2)

def backprop(x, t):
    """Gradients of E = sum (t - o)^2 / 2 by the delta rule."""
    h, o = forward(x)
    delta_o = (t - o) * o * (1 - o)                   # output layer
    delta_h = h * (1 - h) * (W2.T @ delta_o)          # hidden layer
    return -delta_h @ x.T, -delta_h, -delta_o @ h.T, -delta_o   # dE/dW1, dE/db1, dE/dW2, dE/db2

# Gradient check against central finite differences.
x0, t0 = X[:, [1]], T[:, [1]]
analytic = backprop(x0, t0)[0]
numeric = np.zeros_like(W1)
eps = 1e-6
for idx in np.ndindex(W1.shape):
    old = W1[idx]
    W1[idx] = old + eps
    e_plus = loss(x0, t0)
    W1[idx] = old - eps
    e_minus = loss(x0, t0)
    W1[idx] = old
    numeric[idx] = (e_plus - e_minus) / (2 * eps)
print(f"max gradient error: {np.abs(analytic - numeric).max():.1e}")

# Stochastic gradient descent, one sample at a time.
eta = 0.5
for epoch in range(10001):
    for i in rng.permutation(4):
        gW1, gb1, gW2, gb2 = backprop(X[:, [i]], T[:, [i]])
        W1 -= eta * gW1
        b1 -= eta * gb1
        W2 -= eta * gW2
        b2 -= eta * gb2
    if epoch % 2500 == 0:
        print(f"epoch {epoch:5d}: E = {loss(X, T):.5f}")
print("outputs:", np.round(forward(X)[1], 3))
```

```text
max gradient error: 2.3e-11
epoch     0: E = 0.51101
epoch  2500: E = 0.00331
epoch  5000: E = 0.00112
epoch  7500: E = 0.00065
epoch 10000: E = 0.00046
outputs: [[0.015 0.985 0.985 0.015]]
```

![Training result of the 2–3–1 network on the XOR problem: the left panel shows the network output over the plane, with the black line the decision boundary o = 0.5, and the region between the two roughly parallel boundaries classified as 1; the right panel shows the training loss against epochs (logarithmic axis), with a plateau at the beginning followed by a rapid decrease](./plots/xor-network.py)

At the start of training the loss barely changes and then suddenly drops: initially the outputs of the hidden neurons are similar, and it takes a while for them to "divide the labor" into two different linear boundaries. Each hidden neuron corresponds to a straight-line boundary in the plane, and the output neuron combines them, finally dividing the plane into three bands, with the middle band classified as 1. This process is sensitive to the initial values and the learning rate: with a different random seed the length of the plateau differs, and occasionally training stops at a local minimum; this is rarer when there are more hidden neurons.

## 4.4. What Has Been Learned

If we plot the weights of each neuron in the first layer of a trained digit-recognition network as a $15 \times 15$ image, we see stroke-like and blob-like patterns, some resembling parts of a digit and some hard to interpret; the later the layer, the more abstract the patterns. This is exactly the intuition of §4.1: the network automatically learns "templates" and their combinations, without anyone having to design features.

The network in this chapter is still elementary, and many problems arise when it is applied to images, speech, and text; these are the subject of [4.7](/4.7):

- The parameters of a fully connected layer grow rapidly with input size and do not exploit the locality and translation invariance of images, hence convolutional neural networks ([4.7.3](/4.7.3));
- When a network is deepened, gradients vanish, training becomes unstable, and overfitting appears, which calls for techniques such as ReLU, normalization, residual connections, dropout, and better optimizers ([4.7.4](/4.7.4));
- Text and speech are variable-length sequences, which require word vectors and recurrent networks ([4.7.5](/4.7.5)), and today's mainstream, the Transformer ([4.7.6](/4.7.6)).

## Summary

- A neuron computes a weighted sum and passes it through an activation function, which can be understood as one act of template matching with a threshold; several neurons in parallel increase the number of patterns, and connecting them in layers combines them into more abstract patterns.
- The activation function must be nonlinear. Sigmoid and tanh are smooth but saturate, ReLU is the default choice for hidden layers, and softmax turns the output into a probability distribution.
- Each layer of a fully connected network is a matrix multiplication plus a componentwise nonlinearity; a single hidden layer can approximate any continuous function (Theorem 4.2.1), but deep networks are usually more efficient.
- Training = choosing a loss function (squared error for regression, cross-entropy for classification) + gradient descent (batch, stochastic, mini-batch).
- Backpropagation uses the chain rule to compute the error terms $\delta$ layer by layer from the output layer toward the input layer, at a cost of the same order as the forward computation; the weight update is $\Delta w_{ji} = \eta\,\delta_j x_{ji}$.
