---
title: Infrastructure for Large Models
description: Where GPU memory goes in training (model states at 16 bytes per parameter, activations, recomputation); floating-point formats from FP32 to BF16, FP8 and NVFP4, mixed-precision training and loss scaling; collective communication and ring all-reduce; data parallelism, ZeRO and FSDP, tensor, pipeline, context and expert parallelism and how to combine them; the GPU memory hierarchy, the roofline model and FlashAttention; estimating training compute with 6ND and MFU; serving language models with prefill and decode, continuous batching, PagedAttention and speculative decoding.
---

The previous chapter treated a pre-trained model as a mathematical object: a network, a loss and an optimizer. This chapter is about what it takes to actually train and serve one. The numbers are the starting point. Llama 3 405B has 405 billion parameters; its weights alone take 810 GB in 16-bit precision, ten times the memory of one H100 GPU, and its training took $3.8 \times 10^{25}$ **floating-point operations**, about 3,000 years of one H100 or more than two months of 16,384 of them. Memory forces us to split the model, and compute forces us to use thousands of accelerators in parallel. The chapter answers the questions this raises in order: where the memory of a training run goes (§8.1); how lower-precision number formats save memory and time without spoiling the optimization (§8.2); how GPUs exchange data (§8.3) and how training is divided among them by data, tensor and pipeline parallelism (§8.4–§8.6); why attention is limited by memory traffic rather than arithmetic and how FlashAttention fixes it (§8.7); how to estimate the compute and duration of a training run (§8.8); and how a trained model is served efficiently (§8.9). The numerical background on **floating-point numbers** is in [3.5.1](/3.5.1), matrix multiplication libraries such as **BLAS** are introduced in [4.4.3](/4.4.3), and the **Transformer** and its **KV cache** in [4.7.6](/4.7.6). How much compute should be spent on parameters versus data, the scaling laws, is the subject of [4.7.9](/4.7.9).

## 8.1. Where GPU Memory Goes

### 8.1.1. Model States and Activations

The memory of a training step falls into two classes (Rajbhandari et al. 2020).

**Definition 8.1.1 (Model States)** The **model states** of a training run are the quantities whose size is proportional to the number of parameters: the parameters themselves, their gradients, and the optimizer states (for Adam, the first and second moment estimates of every parameter). The **activations** are the intermediate results of the forward pass that are stored for the backward pass; their size is proportional to the number of tokens processed at once.

Besides these there are temporary buffers (communication buffers, workspace of matrix multiplication kernels) and fragmentation: free memory scattered in gaps too small for a large tensor, so that a run can fail with "out of memory" while a fifth or more of the memory is nominally free.

### 8.1.2. Model States: 16 Bytes per Parameter

With mixed-precision training and **Adam** (§8.2.2) every parameter costs

| Quantity | Format | Bytes |
|---|---|---|
| weights used in forward and backward | BF16 | 2 |
| gradients | BF16 | 2 |
| FP32 master copy of the weights | FP32 | 4 |
| Adam first moment $\boldsymbol{m}$ | FP32 | 4 |
| Adam second moment $\boldsymbol{v}$ | FP32 | 4 |
| total | | 16 |

The optimizer states (the last three rows) are three quarters of the total, and the total is eight times the 2 bytes per parameter that inference needs. Some setups keep the gradients in FP32 (18 bytes; the default of Megatron-LM's BF16 training). Mixed precision does not reduce the model states (pure FP32 training with Adam also needs $4 + 4 + 4 + 4 = 16$ bytes); what it saves is activation memory and, above all, time. For Llama-3-70B the model states are $70.55 \times 10^9 \times 16$ bytes $\approx 1{,}129$ GB.

### 8.1.3. Activations

For a **Transformer** layer with hidden size $h$, $a$ attention heads and a sequence of $s$ **tokens**, Korthikanti et al. (2023) counted the stored activations in 16-bit precision exactly: the inputs of the matrix multiplications, the normalizations and the **activation functions** take $34\,sh$ bytes per layer and sequence, and standard attention adds the $a$ score matrices of size $s \times s$, $5as^2$ bytes with **dropout** (the scores, the **softmax** output and the dropout mask) or $2as^2$ without. The second term grows quadratically in the sequence length: for Llama-3-8B (32 heads) one layer at 32K tokens would need $2 \times 32 \times 32768^2$ bytes $\approx 69$ GB of scores. FlashAttention (§8.7) never stores the score matrices, leaving the linear term. For Llama-3-8B ($h = 4096$, 32 layers) and one sequence of 8,192 tokens, this is $34 \times 8192 \times 4096$ bytes $= 1.14$ GB per layer, 36.5 GB in total, more than twice the 16 GB of the weights. The logits for the loss add $4 \times s \times V$ bytes in FP32, 4.2 GB for the vocabulary of $V = 128{,}256$ tokens.

Activations grow linearly with the number of tokens per *micro-batch* (the sequences a GPU processes in one forward–backward pass): four sequences instead of one quadruple them, while the model states stay the same.

### 8.1.4. Activation Recomputation

**Definition 8.1.2 (Activation Recomputation)** **Activation recomputation** (also *gradient checkpointing*) stores only some of the activations in the forward pass, typically the input of each Transformer layer, and recomputes the others during the backward pass by running the forward computation of the corresponding layer again just before its gradients are needed.

Recomputation trades compute for memory. *Full* recomputation keeps only the layer inputs ($2sh$ bytes per layer) plus the activations of the one layer currently being processed: for Llama-3-8B at 8K tokens the peak drops from 36.5 GB to $2.15 + 1.14 \approx 3.3$ GB. The cost is one extra forward pass: a backward pass costs about twice a forward pass, so a training step goes from 3 to 4 forward-pass equivalents, 33% more computation. *Selective* recomputation recomputes only the parts that are large but cheap to recompute, above all the attention scores: for GPT-3 it reduced activation memory by 70% at a cost of about 1% more computation. FlashAttention recomputes the scores anyway, so with it selective recomputation comes for free. Chen et al. (2016) observed that storing the inputs of every $\sqrt{L}$-th layer of an $L$-layer network reduces activation memory from $O(L)$ to $O(\sqrt{L})$ at the cost of one extra forward pass.

### 8.1.5. Example: How Many GPUs Does Llama 3 Need?

The accounting can be written as a small function. It assumes mixed-precision Adam, FlashAttention, one 8,192-token sequence per GPU, and that the model states are split evenly across GPUs by ZeRO-3 (§8.5.1), which does not split activations; buffers are not included.

```python
GB = 1e9

def training_memory(params, layers, hidden, vocab, tokens, gpus=1, zero3=False,
                    recompute=False):
    """Per-GPU memory (GB) for mixed-precision Adam training of a dense Transformer,
    one sequence of `tokens` tokens per GPU, FlashAttention (no stored scores)."""
    states = 16 * params / (gpus if zero3 else 1)        # 2+2 (BF16 w, g) + 12 (FP32 m, v, master)
    per_layer = 34 * tokens * hidden                     # Korthikanti et al., 16-bit activations
    if recompute:                                        # keep layer inputs + one layer's activations
        acts = 2 * tokens * hidden * layers + per_layer
    else:
        acts = per_layer * layers
    logits = 4 * tokens * vocab                          # FP32 logits for the loss
    return states / GB, acts / GB, logits / GB

llama = {"8B": (8.03e9, 32, 4096, 128256), "70B": (70.55e9, 80, 8192, 128256)}
print(f"{'model':5} {'setup':28} {'states':>7} {'acts':>7} {'logits':>7} {'total':>7}")
for name, setup, kw in [("8B", "1 GPU", {}),
                        ("8B", "ZeRO-3, 8 GPUs", dict(gpus=8, zero3=True)),
                        ("8B", "ZeRO-3 + recompute, 4 GPUs", dict(gpus=4, zero3=True, recompute=True)),
                        ("70B", "ZeRO-3, 24 GPUs", dict(gpus=24, zero3=True)),
                        ("70B", "ZeRO-3 + recompute, 24 GPUs", dict(gpus=24, zero3=True, recompute=True))]:
    s, a, l = training_memory(*llama[name], tokens=8192, **kw)
    print(f"{name:5} {setup:28} {s:7.1f} {a:7.1f} {l:7.1f} {s + a + l:7.1f}")
```

```text
model setup                         states    acts  logits   total
8B    1 GPU                          128.5    36.5     4.2   169.2
8B    ZeRO-3, 8 GPUs                  16.1    36.5     4.2    56.8
8B    ZeRO-3 + recompute, 4 GPUs      32.1     3.3     4.2    39.6
70B   ZeRO-3, 24 GPUs                 47.0   182.5     4.2   233.8
70B   ZeRO-3 + recompute, 24 GPUs     47.0    13.0     4.2    64.3
```

With roughly 76 of the 80 GB of an H100 usable after runtime overhead, and several more gigabytes for the buffers of ZeRO-3, the 8B model fits on 8 GPUs, or on 4 with recomputation. For the 70B model the 182.5 GB of activations of a single sequence cannot fit on any one GPU, however many GPUs share the model states; recomputation brings it to 13 GB, and 24 GPUs (three servers) suffice. Splitting the activations themselves requires tensor or context parallelism (§8.6).

![Training memory of Llama-3-8B, 70B and 405B on a single device: BF16 weights and gradients, FP32 master weights and Adam moments (three quarters of the total), activations of one 8,192-token sequence with FlashAttention, and FP32 logits; the dashed line is the 80 GB of one H100](./plots/memory-breakdown.py)

## 8.2. Number Formats and Mixed Precision

### 8.2.1. Floating-Point Formats

A binary **floating-point number** is $\pm 1.f \times 2^{e}$ with an exponent field of $E$ bits and a fraction (mantissa) field of $M$ bits ([3.5.1](/3.5.1#sec-1.2.3)). The exponent bits set the range, the largest and smallest representable magnitudes; the mantissa bits set the precision, the **machine epsilon** $2^{-M}$, which is the gap between $1$ and the next larger number. **Deep learning** uses several formats besides the FP32 of the **IEEE 754 standard** (**single precision**), written ExMy for $x$ exponent and $y$ mantissa bits.

| Format | Bits (E, M) | Largest | Smallest normal | Machine epsilon | Main use |
|---|---|---|---|---|---|
| FP32 | 32 (8, 23) | $3.4 \times 10^{38}$ | $1.2 \times 10^{-38}$ | $2^{-23} \approx 1.2 \times 10^{-7}$ | master weights, optimizer states, accumulation |
| BF16 | 16 (8, 7) | $3.4 \times 10^{38}$ | $1.2 \times 10^{-38}$ | $2^{-7} \approx 0.0078$ | default for training large models |
| FP16 | 16 (5, 10) | 65,504 | $6.1 \times 10^{-5}$ | $2^{-10} \approx 0.00098$ | older GPUs (V100); needs loss scaling |
| FP8 E5M2 | 8 (5, 2) | 57,344 | $6.1 \times 10^{-5}$ | $2^{-2}$ | gradients, where range matters |
| FP8 E4M3 | 8 (4, 3) | 448 | $2^{-6} \approx 0.016$ | $2^{-3}$ | weights and activations in FP8 training |
| FP4 E2M1 | 4 (2, 1) | 6 | 1 | $2^{-1}$ | block-scaled weights and activations (NVFP4, MXFP4) |

Below the smallest normal number, **subnormal numbers** keep fewer significant digits; FP16 reaches $2^{-24} \approx 6 \times 10^{-8}$ before values **underflow** to zero. E4M3 gives up infinities (only one bit pattern is reserved for NaN), which frees an extra exponent value and raises its maximum from 240 to 448. FP4 E2M1 has only the magnitudes $0, 0.5, 1, 1.5, 2, 3, 4, 6$.

**Definition 8.2.1 (BF16)** **BF16** (bfloat16, "brain floating point", introduced by Google for TPUs) is the 16-bit floating-point format with 1 sign bit, 8 exponent bits and 7 mantissa bits. It consists of the upper 16 bits of an FP32 number, so it has the same range as FP32 and about 2–3 significant decimal digits.

![Range and precision of floating-point formats: the interval of representable positive magnitudes on a log2 scale, with the subnormal part lighter, and the machine epsilon; BF16 has the range of FP32 with the precision of a few bits, while FP16 and FP8 trade range for precision](./plots/number-formats.py)

Smaller formats pay off on two counts. They halve or quarter the memory and the memory traffic per number, and the *tensor cores* of GPUs (the units that compute small matrix products in hardware) run 16-bit matrix multiplication 15–30 times faster than general FP32 arithmetic, FP8 twice as fast as BF16 and FP4 twice as fast again.

### 8.2.2. The Mixed-Precision Recipe

**Definition 8.2.2 (Mixed-Precision Training)** **Mixed-precision training** (Micikevicius et al., ICLR 2018) performs the forward and backward passes, and stores the activations and gradients, in a 16-bit format (BF16 or FP16), with matrix products accumulated in FP32, while keeping an FP32 *master copy* of the weights: the optimizer updates the master weights in FP32 and then copies them, rounded, to 16 bits for the next step.

The master copy is needed because of **rounding error** in the update $w \leftarrow w + \Delta w$. When $\lvert\Delta w\rvert$ is less than half the gap between $w$ and its neighbors in the 16-bit format, the sum rounds back to $w$ and the update is lost entirely. In BF16 the gap at $w$ is about $2^{-7}\lvert w\rvert$, so this happens as soon as $\lvert w\rvert$ exceeds about $256\,\lvert\Delta w\rvert$ (in FP16 about $2{,}048\,\lvert\Delta w\rvert$). The ratio is easily reached: **Adam**'s steps are about the size of the learning rate, so a weight of $0.02$ with a learning rate decayed to $3 \times 10^{-5}$ has a ratio of about 670, and in pure BF16 it would stop moving. NumPy has no BF16 type, but rounding FP32 to its upper 16 bits emulates it exactly:

```python
import numpy as np

def to_bf16(x):
    """Round float32 values to the nearest bfloat16 (ties to even), returned as float32.
    BF16 is the upper 16 bits of FP32: sign, 8 exponent bits, 7 mantissa bits."""
    b = np.asarray(x, dtype=np.float32).view(np.uint32)
    b = b + 0x7FFF + ((b >> 16) & 1)          # round to nearest even at bit 16
    return (b & 0xFFFF0000).view(np.float32)

np.seterr(over="ignore")                  # FP16 overflow to inf is the point
for name, f in [("FP32", np.float32), ("FP16", np.float16), ("BF16", to_bf16)]:
    print(f"{name}: 1 + 0.003 = {float(f(np.float32(1) + np.float32(0.003))):.6f}, "
          f"70000 -> {float(f(np.float32(70000))):.0f}, 1e-8 -> {float(f(np.float32(1e-8))):.2e}")

# 1,000 steps of a small update to a weight of size 0.02
w0, update, steps = 0.02, 3e-5, 1000
w_bf16 = to_bf16(w0)
w_master = np.float32(w0)
for _ in range(steps):
    w_bf16 = to_bf16(w_bf16 + np.float32(update))       # pure BF16 weights
    w_master = w_master + np.float32(update)            # FP32 master weights
print(f"start {float(to_bf16(w0)):.5f}  exact {w0 + steps * update:.5f}  BF16 weights {float(w_bf16):.5f}  "
      f"FP32 master copied to BF16 {float(to_bf16(w_master)):.5f}")
```

```text
FP32: 1 + 0.003 = 1.003000, 70000 -> 70000, 1e-8 -> 1.00e-08
FP16: 1 + 0.003 = 1.002930, 70000 -> inf, 1e-8 -> 0.00e+00
BF16: 1 + 0.003 = 1.000000, 70000 -> 70144, 1e-8 -> 1.00e-08
start 0.02002  exact 0.05000  BF16 weights 0.02002  FP32 master copied to BF16 0.05005
```

The first three lines show the trade-off of the two 16-bit formats: FP16 keeps three decimal digits but **overflows** at 70,000 and underflows at $10^{-8}$; BF16 represents both, but $1 + 0.003$ rounds to $1$. The last line shows why the master weights are kept: in pure BF16 a thousand updates of $3 \times 10^{-5}$ have no effect at all, while accumulated in FP32 they move the weight correctly. For the same reason matrix multiplication units accumulate their sums of products in FP32.

### 8.2.3. Loss Scaling for FP16

FP16 has the opposite problem: small gradients underflow. Micikevicius et al. found that in an SSD object detector most activation gradients were below $2^{-24}$ and became zero in FP16, so that the network did not train, while the upper part of the FP16 range was unused.

**Definition 8.2.3 (Loss Scaling)** **Loss scaling** multiplies the loss by a constant $S$ before the backward pass, so that by the **chain rule** every gradient is multiplied by $S$ and shifted into the representable range, and divides the gradients by $S$ (in FP32) before the optimizer step. In *dynamic* loss scaling, $S$ is halved and the step is skipped whenever an infinity or NaN appears in the gradients, and doubled after a fixed number of steps (2,000 in PyTorch's `GradScaler`) without overflow.

For SSD a factor of 8 sufficed (77.1% mAP against 76.9% in FP32). Since the scaling is undone before the update, the learning rate and other **hyperparameters** do not change.

### 8.2.4. Why BF16 Won

BF16 has the speed of FP16 on tensor cores and the range of FP32: values from $10^{-38}$ to $10^{38}$ fit, so gradients neither underflow nor overflow and no loss scaling is needed. Its low precision is compensated by the two FP32 elements of the recipe, accumulation in matrix multiplications and master weights. Since the A100 (2020) and TPUs before it, BF16 with FP32 master weights is the default for training large models; FP16 with loss scaling survives mainly on older hardware.

### 8.2.5. FP8 Training

FP8 doubles the peak matrix-multiplication throughput of BF16 on H100 and later GPUs, but E4M3 covers only magnitudes from about $0.016$ (normal) to $448$. FP8 training therefore multiplies each group of numbers by a scale factor before the conversion, chosen so that the group's largest absolute value maps to the format's maximum, and divides the result of the matrix product by the scales; this is loss scaling applied to every tensor.

- *Per-tensor* scaling (the default of NVIDIA's Transformer Engine on Hopper) uses one scale per tensor, often taken from the maximum of recent steps ("delayed scaling"). An outlier channel with very large values forces a small scale, and the many small values of the tensor then underflow.
- *Fine-grained* scaling, introduced at scale by DeepSeek-V3 (December 2024), uses one scale per tile of $1 \times 128$ elements for activations (one **token**, 128 channels) and per block of $128 \times 128$ for weights, so that an outlier spoils only its own tile. DeepSeek-V3 used E4M3 for all inputs of its FP8 matrix products, promoted partial sums to FP32 at short intervals because the FP8 tensor cores of the H800 accumulate with limited precision, and kept master weights, weight gradients and optimizer states in higher precision. Its **pre-training** loss stayed within 0.25% of a BF16 baseline.
- Blackwell GPUs (2025) support such block scaling in hardware with the *microscaling* formats of the Open Compute Project: MXFP8 uses blocks of 32 values with a shared power-of-two scale stored in 8 bits (E8M0).

### 8.2.6. Four-Bit Formats

Four bits are too few for a single floating-point format to be usable on its own; they work only with fine-grained scales. *MXFP4* stores E2M1 values in blocks of 32 with an E8M0 scale. *NVFP4*, NVIDIA's format for Blackwell, stores E2M1 values in blocks of 16 with an FP8 E4M3 scale per block (which, unlike a power of two, can be fitted closely to the block) and an FP32 scale per tensor, about 4.5 bits per value in total. Four-bit weights have long been used for inference (quantization methods such as GPTQ and AWQ, and the NF4 format of QLoRA in [4.7.7](/4.7.7#sec-7.6.5)); since 2025 they are also used in training. NVIDIA pre-trained Nemotron 3 Super (March 2026) and Nemotron 3 Ultra (June 2026, 550 billion parameters) natively in NVFP4, and DeepSeek released the expert weights of DeepSeek-V4 (April 2026) in FP4 with the other weights in FP8. In each case sensitive parts (the first and last layers, optimizer states, accumulation) remain in higher precision.

## 8.3. Collective Communication

### 8.3.1. Collective Operations

Parallel training needs GPUs to combine data: to sum gradients, to share parameters, to send **tokens** to experts. These operations are *collectives*, calls that all GPUs in a group join, implemented on NVIDIA GPUs by the NCCL library. Let each of $p$ GPUs hold a buffer of $n$ elements.

**Definition 8.3.1 (All-Reduce)** An **all-reduce** leaves on every GPU the elementwise sum (or another associative reduction) of the $p$ buffers. A **reduce-scatter** leaves on GPU $i$ only the $i$-th of $p$ equal slices of the sum, and an **all-gather** concatenates one slice from every GPU and leaves the whole result on every GPU. An all-reduce equals a reduce-scatter followed by an all-gather.

| Collective | Each GPU ends with | Data sent per GPU (bandwidth-optimal) | Main use |
|---|---|---|---|
| broadcast | a copy of one GPU's buffer | $n$ | initial weights |
| reduce-scatter | one slice of the sum | $\frac{p-1}{p}n$ | ZeRO / FSDP gradients |
| all-gather | all slices | $\frac{p-1}{p}n$ | ZeRO / FSDP weights |
| all-reduce | the full sum | $2\frac{p-1}{p}n$ | data-parallel gradients, tensor-parallel activations |
| all-to-all | the blocks addressed to it, one from each GPU | $\frac{p-1}{p}n$ | routing tokens to experts |

### 8.3.2. Ring All-Reduce

The GPUs are arranged in a ring and each buffer is cut into $p$ chunks. In the reduce-scatter phase, in each of $p - 1$ steps every GPU sends one chunk to its successor, which adds it to its own copy of that chunk; after $p - 1$ steps each GPU holds one chunk of the complete sum. In the all-gather phase the finished chunks travel around the ring in another $p - 1$ steps. Each step sends one chunk, $n/p$ elements, per GPU, so each GPU sends $2(p-1)n/p < 2n$ elements in total, independent of $p$, and Patarasuk and Yuan (2009) proved that no algorithm using point-to-point messages without compression can do better. The price is *latency*: with a fixed start-up cost $\alpha$ per message and bandwidth $\beta$ bytes per second, the time is about

$$
T_{\text{ring}} \approx 2(p - 1)\,\alpha + 2\,\frac{p-1}{p}\,\frac{n_{\text{bytes}}}{\beta},
$$

whose first term grows with $p$; for small messages or very many GPUs, NCCL switches to tree algorithms with $O(\log p)$ steps. A simulation on arrays checks both the result and the communication volume:

```python
import numpy as np

def ring_all_reduce(buffers):
    """Simulate ring all-reduce on p equal-length arrays (one per GPU).
    Returns the reduced arrays and the number of elements each GPU sent."""
    p = len(buffers)
    chunks = [np.array_split(b.astype(float), p) for b in buffers]   # chunks[gpu][c]
    sent = [0] * p
    # reduce-scatter: in step s, GPU i sends chunk (i - s) mod p to GPU i + 1
    for s in range(p - 1):
        msgs = [(i, (i - s) % p, chunks[i][(i - s) % p].copy()) for i in range(p)]
        for i, c, data in msgs:                     # all sends of a step happen at once
            chunks[(i + 1) % p][c] += data
            sent[i] += data.size
    # now GPU i holds the full sum of chunk (i + 1) mod p
    # all-gather: pass the finished chunks around the ring
    for s in range(p - 1):
        msgs = [(i, (i + 1 - s) % p, chunks[i][(i + 1 - s) % p].copy()) for i in range(p)]
        for i, c, data in msgs:
            chunks[(i + 1) % p][c] = data
            sent[i] += data.size
    return [np.concatenate(ch) for ch in chunks], sent

rng = np.random.default_rng(0)
p, n = 4, 1_000_000
grads = [rng.standard_normal(n) for _ in range(p)]
out, sent = ring_all_reduce(grads)
print("all GPUs hold the sum:", all(np.allclose(o, sum(grads)) for o in out))
print(f"elements sent per GPU: {sent[0]:,} = {sent[0] / n:.2f} x n "
      f"(formula 2(p-1)/p = {2 * (p - 1) / p:.2f})")
```

```text
all GPUs hold the sum: True
elements sent per GPU: 1,500,000 = 1.50 x n (formula 2(p-1)/p = 1.50)
```

### 8.3.3. The Bandwidth Hierarchy

Where a collective runs matters as much as how much it sends. Bandwidth drops by roughly an order of magnitude at each level of the hierarchy:

| Level | H100 (per GPU, each direction) | B200 |
|---|---|---|
| HBM, the GPU's own memory | 3.35 TB/s | 8 TB/s |
| NVLink, between the 8 GPUs of a server | 450 GB/s | 900 GB/s |
| network (InfiniBand or Ethernet) between servers | 50 GB/s (one 400 Gb/s card) | 50–100 GB/s |

Vendor figures need care: the "900 GB/s" of H100 NVLink counts both directions, and network cards are rated in bits (400 Gb/s is 50 GB/s). The group of GPUs connected by NVLink, the *NVLink domain*, is a server of 8 GPUs, or 72 in a GB200 NVL72 rack. The rule that follows organizes the rest of the chapter: communication that every layer must wait for belongs inside the NVLink domain; communication that happens once per step, or can be overlapped with computation, can cross the network.

## 8.4. Data Parallelism

**Definition 8.4.1 (Data Parallelism)** In **data parallelism** (DP) each of $p$ GPUs holds a complete copy of the model and processes a different slice of each mini-batch; after the backward pass the gradients are averaged across GPUs by an all-reduce, and every GPU applies the same update.

**Proposition 8.4.1** If the loss of a mini-batch is the average of per-example losses and the mini-batch $\mathcal{B}$ of size $B$ is divided into $p$ slices $\mathcal{B}_1, \dots, \mathcal{B}_p$ of size $B/p$, then the average of the $p$ slice gradients equals the gradient of the whole mini-batch. Hence data-parallel training is mathematically identical to **mini-batch gradient descent** with batch size $B$.

**Proof** By linearity of the gradient,

$$
\frac{1}{p}\sum_{k=1}^{p}\nabla_{\boldsymbol{\theta}}\Bigl(\frac{p}{B}\sum_{i \in \mathcal{B}_k}\ell_i(\boldsymbol{\theta})\Bigr) = \frac{1}{B}\sum_{k=1}^{p}\sum_{i \in \mathcal{B}_k}\nabla_{\boldsymbol{\theta}}\ell_i(\boldsymbol{\theta}) = \nabla_{\boldsymbol{\theta}}\Bigl(\frac{1}{B}\sum_{i \in \mathcal{B}}\ell_i(\boldsymbol{\theta})\Bigr). \qquad \square
$$

(Operations that couple examples within a slice, such as **batch normalization**, break the identity unless their statistics are synchronized too.) Adding GPUs therefore means a larger batch, and the learning rate must be adjusted to it ([4.7.4](/4.7.4)). The communication is one all-reduce of all gradients per step, about $2 \times 2N$ bytes per GPU for $N$ parameters in BF16, and it can be hidden: PyTorch's `DistributedDataParallel` groups gradients into buckets of about 25 MB in the order the backward pass produces them and starts the all-reduce of each bucket while the backward pass continues on earlier layers. For a 7-billion-parameter model the 14 GB of gradients take about 50–75 ms on a well-connected cluster, less than the backward pass. The problem of plain data parallelism is memory: every GPU stores all 16 bytes per parameter, 112 GB for 7 billion parameters, and adding GPUs does not reduce it.

## 8.5. Sharding the Model States: ZeRO and FSDP

### 8.5.1. ZeRO

**Definition 8.5.1 (ZeRO)** The **Zero Redundancy Optimizer** (ZeRO; Rajbhandari et al., SC 2020) is data parallelism in which the model states are partitioned (*sharded*) across the $p$ data-parallel GPUs instead of replicated: each GPU stores, and updates, only its $1/p$ share. Stage 1 shards the optimizer states (including the FP32 master weights), stage 2 also the gradients, and stage 3 also the 16-bit parameters.

ZeRO is not a new optimizer: the result of every step is the same as with plain **Adam**. Its trick is that an all-reduce is a reduce-scatter followed by an all-gather, and the update can be done between the two. After the reduce-scatter each GPU has the summed gradients of its own slice of the parameters, updates that slice with its optimizer states, and the all-gather then distributes the updated 16-bit parameters. Stages 1 and 2 therefore send exactly as much as plain data parallelism. Stage 3 frees each layer's parameters after use in the forward pass and must all-gather them again for the backward pass, three transfers of the model size instead of two, 1.5 times the traffic of data parallelism.

| Strategy | Bytes per parameter on each GPU | Llama-3-70B, 64 GPUs | 512 GPUs | Communication relative to DP |
|---|---|---|---|---|
| DP | $16$ | 1,129 GB | 1,129 GB | 1 |
| ZeRO-1 | $4 + 12/p$ | 295 GB | 284 GB | 1 |
| ZeRO-2 | $2 + 14/p$ | 157 GB | 143 GB | 1 |
| ZeRO-3 | $16/p$ | 17.6 GB | 2.2 GB | 1.5 |

Only stage 3 reduces the memory without a floor: ZeRO-1 and ZeRO-2 keep 4 and 2 bytes per parameter on every GPU however many GPUs there are, so they save at most a factor of 4 and 8. None of the stages splits the activations, since every GPU still runs all layers on its own data.

### 8.5.2. Fully Sharded Data Parallelism

**Definition 8.5.2 (Fully Sharded Data Parallelism)** **Fully sharded data parallelism** (FSDP) is PyTorch's implementation of ZeRO stage 3. The model is divided into units, typically one Transformer block each; in the forward pass each unit's parameters are all-gathered just before use and freed afterwards; in the backward pass they are all-gathered again, and the gradients are reduce-scattered so that each GPU keeps the gradients of its own shard.

Communication runs on a separate stream and is *prefetched*: the all-gather of unit $k + 1$ is issued while unit $k$ computes, so the GPU waits only when the transfer is slower than the computation (for GPT-175B, backward prefetching made training about 18% faster). FSDP2 (2024) shards every tensor by rows instead of flattening all parameters of a unit into one buffer, which composes cleanly with tensor parallelism and with FP8 scales. *Hybrid sharding* (HSDP) shards within a server, so that the all-gathers stay on NVLink, and replicates across servers like plain data parallelism; the price is that each GPU keeps $1/8$ of the model states however many servers are used, 141 GB for Llama-3-70B, too much on its own.

## 8.6. Model Parallelism

### 8.6.1. Tensor Parallelism

**Definition 8.6.1 (Tensor Parallelism)** **Tensor parallelism** (TP) splits the weight matrices of each layer across a group of GPUs (of size the *TP degree*), so that each GPU stores and multiplies only a slice of every matrix, and combines the partial results with collective operations inside the layer.

Megatron-LM (Shoeybi et al. 2019) splits a **Transformer**'s feed-forward block $Y = \operatorname{GeLU}(XW_1)W_2$ so that it needs only one all-reduce. $W_1 = [W_1^{(1)}, \dots, W_1^{(p)}]$ is split by columns; since GeLU acts elementwise, GPU $i$ computes $\operatorname{GeLU}(XW_1^{(i)})$ without communication. $W_2$ is split by the matching rows, and

$$
Y = \operatorname{GeLU}(XW_1)\,W_2 = \sum_{i=1}^{p}\operatorname{GeLU}\bigl(XW_1^{(i)}\bigr)\,W_2^{(i)},
$$

a sum of partial results, one per GPU, which a single all-reduce adds up. (Splitting $W_1$ by rows instead would require communication before the nonlinearity.) In the backward pass the gradient with respect to $X$ is a sum of partial results as well, so one more all-reduce is needed at the block's input.

```python
import numpy as np

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

rng = np.random.default_rng(0)
tokens, h, p = 8, 64, 4                          # 4-way tensor parallelism
X = rng.standard_normal((tokens, h))
W1 = rng.standard_normal((h, 4 * h)) / np.sqrt(h)        # Y = GeLU(X W1) W2
W2 = rng.standard_normal((4 * h, h)) / np.sqrt(4 * h)
reference = gelu(X @ W1) @ W2

W1_parts = np.split(W1, p, axis=1)               # column blocks of W1
W2_parts = np.split(W2, p, axis=0)               # matching row blocks of W2
partial = [gelu(X @ A) @ B for A, B in zip(W1_parts, W2_parts)]   # GPU i, no communication
print("sum of partial outputs (one all-reduce) is exact:",
      np.allclose(sum(partial), reference))
```

```text
sum of partial outputs (one all-reduce) is exact: True
```

Attention is split by heads in the same way: the query, key and value projections by columns, so that each GPU computes complete heads, and the output projection by rows, followed by one all-reduce. A Transformer layer thus needs two all-reduces in the forward pass and two in the backward pass, each of the size of the layer's activations. *Sequence parallelism* additionally splits the normalization and **dropout** regions, which TP alone replicates, along the **token** dimension, replacing each all-reduce by a reduce-scatter and an all-gather with the same total traffic; activation memory per GPU then shrinks by the TP degree.

The cost is that this communication lies on the critical path. For Llama-3-70B with TP degree 8 and a micro-batch of 4,096 tokens each GPU sends about $4 \times 2 \cdot \tfrac78 \times 4096 \times 8192 \times 2$ bytes $\approx 470$ MB per layer, and since both the traffic and the computation grow with the number of tokens, a larger batch does not dilute it. Over NVLink (450 GB/s) this is a fraction of the compute time; over a 50 GB/s network link it would be as long as the computation or longer. Tensor parallelism is therefore used within one server, with a degree of at most 8, and Megatron's measurements (a 162-billion-parameter GPT on 64 A100s) are fastest exactly at TP degree 8.

### 8.6.2. Pipeline Parallelism

**Definition 8.6.2 (Pipeline Parallelism)** **Pipeline parallelism** (PP) divides the layers of a network into $p$ consecutive *stages* placed on different GPUs; activations are sent forward from stage to stage and their gradients backward, and the mini-batch is divided into $m$ micro-batches that flow through the stages one after another, so that different stages work on different micro-batches at the same time.

With a single micro-batch only one GPU works at a time. GPipe (Huang et al. 2019) feeds the $m$ micro-batches back to back through all stages, then runs all backward passes, accumulates the gradients and updates once per step (a *flush*), which keeps the update identical to unpipelined training. The idle time at the start and end of each step is the *pipeline bubble*. With forward and backward times $t_F$ and $t_B$ per micro-batch and stage, each GPU is idle for $(p - 1)(t_F + t_B)$ of a step of length $(m + p - 1)(t_F + t_B)$, so the idle share is

$$
\frac{p - 1}{m + p - 1}.
$$

For 4 stages and 8 micro-batches this is $3/11 \approx 27\%$; with 32 micro-batches it is $3/35 \approx 8.6\%$. (Some papers divide by the busy time instead and report $(p-1)/m$.) More micro-batches dilute the bubble but cannot remove it, and they are limited by the global batch size and by the efficiency of matrix multiplications on small micro-batches.

![Pipeline schedules on 4 GPUs with 8 micro-batches, backward passes twice as long as forward passes: GPipe runs all forward passes and then all backward passes; 1F1B alternates after a warm-up. Both are idle 27% of the time, but under 1F1B the first GPU holds the activations of at most 4 micro-batches instead of 8](./plots/pipeline-schedule.py)

GPipe must store the activations of all $m$ micro-batches. The *1F1B* schedule (one forward, one backward; PipeDream, Narayanan et al. 2019) starts each micro-batch's backward pass as early as possible, so that after a warm-up every forward pass is followed by a backward pass; the bubble is the same, but each stage holds the activations of at most $p$ micro-batches. *Interleaved* 1F1B places $v$ non-adjacent chunks of layers on each GPU, which divides the bubble by $v$ at the cost of $v$ times as many transfers between GPUs. *Zero-bubble* schedules (Qi et al., ICLR 2024) split the backward pass into the gradient with respect to the inputs, which the previous stage waits for, and the gradient with respect to the weights, which can be postponed into the bubble. DualPipe, the schedule of DeepSeek-V3 ([4.7.9](/4.7.9)), feeds micro-batches from both ends of the pipeline and overlaps the computation of one micro-batch with the communication of another. Pipeline parallelism communicates little, one activation tensor per micro-batch at each stage boundary (about 67 MB for 4,096 tokens of Llama-3-70B), and therefore runs across servers.

### 8.6.3. Context and Expert Parallelism

Two more dimensions split what the others cannot. *Context parallelism* splits a long sequence across GPUs in every layer; attention, which needs all keys and values of the sequence, exchanges them by an all-gather or by passing blocks around a ring (ring attention). Llama 3 used it for its 128K-token training stage. *Expert parallelism* places the experts of a mixture-of-experts layer ([4.7.9](/4.7.9)) on different GPUs and sends each token to the GPUs of its experts and back with two all-to-all operations per layer.

### 8.6.4. Combining the Dimensions

The dimensions multiply: with TP degree $t$, $s$ pipeline stages and $d$ data-parallel replicas, the number of GPUs is $t \cdot s \cdot d$. Combining all three is called *3D parallelism*. The placement follows the bandwidth hierarchy of §8.3.3.

| | Splits | Model states per GPU | Activations per GPU | Communication | Typical place and size |
|---|---|---|---|---|---|
| DP (ZeRO-1) | the batch | $4 + 12/d$ bytes per parameter | as on one GPU | gradients once per step, overlapped with backward | across servers, 64–128 |
| ZeRO-3 / FSDP | the batch and the model states | $16/d$ bytes per parameter | as on one GPU | 1.5 times DP, prefetched | across servers |
| TP (+ SP) | weight matrices | divided by $t$ | divided by $t$ (with SP) | 4 blocking all-reduces per layer | inside a server, $t \le 8$ |
| PP | layers | divided by $s$ | first stage about one micro-batch through all layers (1F1B) | activations at stage boundaries, plus the bubble | across servers, 16–64 |

The recipe of Narayanan et al. (SC 2021) is: use tensor parallelism inside a server, add pipeline stages until the model fits, and use the remaining GPUs for data parallelism; add context parallelism for very long sequences and expert parallelism for mixtures of experts. Two published runs illustrate it.

| Run | GPUs | TP | CP | PP | EP | DP |
|---|---|---|---|---|---|---|
| Llama-3-405B, 8K context | 16,384 H100 | 8 | 1 | 16 | – | 128 |
| Llama-3-405B, 128K context | 16,384 H100 | 8 | 16 | 16 | – | 8 |
| DeepSeek-V3 (mixture of experts) | 2,048 H800 | – | – | 16 | 64 | 128 (ZeRO-1) |

Llama 3 orders the dimensions from inside out as TP, CP, PP, DP and shards the data-parallel dimension with FSDP; it reached 38–43% of the BF16 peak. DeepSeek-V3 avoided tensor parallelism altogether through careful memory savings, partly because the export-restricted H800 has reduced NVLink bandwidth, and spread its experts over 64 GPUs in 8 servers.

## 8.7. Attention on the GPU: FlashAttention

### 8.7.1. The Memory Hierarchy and the Roofline Model

A GPU consists of many streaming multiprocessors (SMs), each with a small, fast on-chip SRAM (about 100–250 KB per SM, some 20–50 MB in total), and a large off-chip HBM (80–288 GB). On an A100 the SRAM is about 13 times faster than HBM and some 2,000 times smaller. Every number a computation uses must be brought from HBM into an SM first.

**Definition 8.7.1 (Arithmetic Intensity)** The **arithmetic intensity** of a computation is the number of floating-point operations it performs per byte of memory traffic. In the **roofline model** (Williams et al. 2009), a computation of intensity $I$ on a processor with peak compute $\pi$ (FLOP/s) and memory bandwidth $\beta$ (bytes/s) runs at most at $\min(\pi, I\beta)$; it is *memory-bound* if $I < \pi/\beta$ and *compute-bound* otherwise.

For an A100, $\pi/\beta = 312\ \mathrm{TFLOP/s} \div 1.555\ \mathrm{TB/s} \approx 200$ **FLOPs** per byte; for an H100 about 295. Large **matrix multiplication** has intensity proportional to the matrix dimensions and is compute-bound. Elementwise operations, normalization and **softmax** have an intensity of a few FLOPs per byte and are memory-bound.

### 8.7.2. Why Standard Attention Is Memory-Bound

Standard attention for one head computes $S = QK^{\mathsf T}/\sqrt{d}$, $P = \operatorname{softmax}(S)$ and $O = PV$ with $Q, K, V \in \mathbb{R}^{N \times d}$ as separate kernels. Each kernel writes its result to HBM and the next reads it back, so the two $N \times N$ matrices $S$ and $P$ make a round trip through HBM, and the backward pass reads $P$ again. Per score this is about $4d$ FLOPs (the two matrix products) for 8 bytes of BF16 traffic, an intensity of $d/2 = 32$–$64$ for head dimensions 64–128, far below 200. For Llama-3-8B with 8K **tokens**, $P$ alone is $32 \times 8192^2 \times 2$ bytes $\approx 4.3$ GB per layer, and keeping it for the backward pass of 32 layers would take 137 GB.

### 8.7.3. Tiling and the Online Softmax

**Definition 8.7.2 (FlashAttention)** **FlashAttention** (Dao et al., NeurIPS 2022) is an exact attention algorithm that computes the output in one kernel by *tiling*: it loads blocks of $Q$, $K$ and $V$ that fit into SRAM, computes the corresponding block of scores and their contribution to the output in SRAM, and never writes the score or probability matrices to HBM. The softmax is computed incrementally by the online softmax, and the backward pass recomputes the scores from $Q$, $K$ and the stored row statistics.

The difficulty is the softmax: normalizing a row needs its maximum and its sum over all $N$ keys, but the keys arrive block by block. The *online softmax* (Milakov and Gimelshein 2018) keeps for each query row a running maximum $m$, a running sum $\ell$ of $\mathrm{e}^{s - m}$, and an unnormalized output $\boldsymbol{o}$. When a new block of scores $\boldsymbol{s}$ arrives with values $V_j$,

$$
m' = \max\bigl(m, \max_k s_k\bigr), \qquad \ell' = \mathrm{e}^{m - m'}\ell + \sum_k \mathrm{e}^{s_k - m'}, \qquad \boldsymbol{o}' = \mathrm{e}^{m - m'}\boldsymbol{o} + \sum_k \mathrm{e}^{s_k - m'}\boldsymbol{v}_k,
$$

that is, the old sum and output are rescaled by $\mathrm{e}^{m - m'}$ whenever the maximum rises. At the end $\boldsymbol{o}/\ell$ is exactly the softmax-weighted average: the result is not an approximation. Subtracting the running maximum keeps the exponentials from overflowing, as in the stable softmax of [4.7.1](/4.7.1#sec-1.5.2). For the backward pass only the output and one number per row, the log-sum-exp $m + \log\ell$, are stored.

```python
import numpy as np

def attention(Q, K, V):
    S = Q @ K.T / np.sqrt(Q.shape[1])
    P = np.exp(S - S.max(axis=1, keepdims=True))
    return (P / P.sum(axis=1, keepdims=True)) @ V

def flash_attention(Q, K, V, block=64):
    """Tiled attention with online softmax: the N x N score matrix is never formed."""
    N, d = Q.shape
    O = np.zeros_like(Q)
    m = np.full(N, -np.inf)                      # running row maximum
    l = np.zeros(N)                              # running row sum of exp(score - m)
    for j in range(0, N, block):                 # outer loop over blocks of K and V
        Kj, Vj = K[j:j + block], V[j:j + block]
        for i in range(0, N, block):             # inner loop over blocks of Q
            S = Q[i:i + block] @ Kj.T / np.sqrt(d)            # block x block, "in SRAM"
            m_new = np.maximum(m[i:i + block], S.max(axis=1))
            P = np.exp(S - m_new[:, None])
            c = np.exp(m[i:i + block] - m_new)                # rescale the old statistics
            l[i:i + block] = c * l[i:i + block] + P.sum(axis=1)
            O[i:i + block] = c[:, None] * O[i:i + block] + P @ Vj
            m[i:i + block] = m_new
    return O / l[:, None], m + np.log(l)         # output and log-sum-exp for backward

rng = np.random.default_rng(0)
N, d = 1024, 64
Q, K, V = (rng.standard_normal((N, d)) for _ in range(3))
O, lse = flash_attention(Q, K, V)
print("max difference from standard attention:", np.abs(O - attention(Q, K, V)).max())
print(f"stored for backward: {O.size + lse.size:,} numbers instead of {N * N:,} probabilities")
```

```text
max difference from standard attention: 2.7755575615628914e-16
stored for backward: 66,560 numbers instead of 1,048,576 probabilities
```

### 8.7.4. Recomputation, Results and Later Versions

FlashAttention does more arithmetic than standard attention, because the backward pass recomputes the scores, but far less memory traffic. For the attention of GPT-2 medium on an A100 (forward and backward), the original paper reports 75.2 instead of 66.6 GFLOPs (13% more), 4.4 instead of 40.3 GB of HBM traffic (9 times less), and 7.3 instead of 41.7 ms (5.7 times faster). Its extra memory grows linearly instead of quadratically with the sequence length, which made long-context training practical: at 8K tokens a 1.3-billion-parameter GPT trained at about 56% of the A100's peak, faster than Megatron-LM's standard attention at 2K. This is the typical pattern of the field: recomputation that is expensive in FLOPs but saves memory traffic makes memory-bound code faster.

Each GPU generation has required a new version. FlashAttention-2 (2023) reduced the non-matrix-multiplication operations, which run at a small fraction of tensor-core speed, and parallelized over the sequence length, doubling the speed on A100. FlashAttention-3 (2024) used the asynchronous data movement units of the H100 to overlap loading with computation and added FP8, reaching about 85% of the BF16 peak. FlashAttention-4 (2026) targets Blackwell, where matrix units doubled their speed per SM but the units computing exponentials did not, and evaluates part of the exponentials with polynomial approximations on the ordinary multiply-add units.

## 8.8. Estimating Training Compute

### 8.8.1. Counting FLOPs: $C \approx 6ND$

For a dense **Transformer** with $N$ parameters trained on $D$ **tokens**, the training compute is approximately

$$
C \approx 6ND \ \text{FLOPs}.
$$

In the forward pass every weight takes part in one multiplication and one addition per token, 2 **FLOPs**. The backward pass of a linear layer $\boldsymbol{y} = W\boldsymbol{x}$ computes two products of the same size, $W^{\mathsf T}\nabla_{\boldsymbol{y}}$ for the input gradient that is passed back and $\nabla_{\boldsymbol{y}}\boldsymbol{x}^{\mathsf T}$ for the weight gradient, 4 FLOPs per weight and token. Inference needs only the forward pass, about $2N$ FLOPs per token. For GPT-3, $6 \times 175 \times 10^9 \times 300 \times 10^9 = 3.15 \times 10^{23}$ FLOPs, close to the $3.14 \times 10^{23}$ reported. The rule has three refinements:

- the attention products $QK^{\mathsf T}$ and $PV$ have no weights and are not counted; their share relative to $6ND$ is about $s/(12h)$ for sequence length $s$ and hidden size $h$ with a **causal mask**, 4% for Llama-3-405B at 8K tokens but 67% at 128K;
- for a mixture of experts, $N$ is the number of *activated* parameters per token (37 billion for DeepSeek-V3, not 671 billion);
- recomputation makes the hardware execute about $8ND$ FLOPs, but the useful work remains $6ND$.

### 8.8.2. From FLOPs to GPU-Hours

**Definition 8.8.1 (Model FLOPs Utilization)** The **model FLOPs utilization** (MFU) of a training run is the ratio of the useful FLOP rate (the model FLOPs $6N$ plus attention, per token, times the tokens processed per second) to the peak FLOP rate of the hardware. The *hardware FLOPs utilization* (HFU) also counts recomputed FLOPs, so $\mathrm{HFU} \ge \mathrm{MFU}$.

The training time is then $C / (\text{number of GPUs} \times \text{peak} \times \mathrm{MFU})$. The peak must be the dense one: NVIDIA's headline figure for the H100's BF16 throughput, 1,979 TFLOP/s, assumes 2:4 structured sparsity (half of the weights zero), and the dense peak is half of it.

| GPU | dense BF16 TFLOP/s | dense FP8 TFLOP/s | HBM TB/s |
|---|---|---|---|
| A100 80 GB | 312 | – | 2.0 |
| H100 SXM | 989 | 1,979 | 3.35 |
| H200 SXM | 989 | 1,979 | 4.8 |
| B200 | 2,250 | 4,500 | 8 |

Well-tuned large runs reach about 40% MFU; the rest goes to communication that is not hidden, pipeline bubbles and memory-bound kernels. MFU falls with scale and context length (Llama-3-405B: 43% on 8K GPUs, 41% on 16K, 38% at 128K context), and over all billed hours, including failures and restarts, it is lower still (PaLM: 46.2% in steady state, about 31% overall). A convenient unit: one H100-hour at 40% MFU is $989 \times 10^{12} \times 0.4 \times 3600 \approx 1.4 \times 10^{18}$ FLOPs, so $10^{24}$ FLOPs is about 0.7 million H100-hours.

**Example 8.8.1** A dense 70-billion-parameter model trained on 15 trillion tokens (the scale of Llama-3-70B) on 1,024 H100s at 40% MFU:

| Step | Calculation | Result |
|---|---|---|
| compute | $6 \times 70 \times 10^9 \times 15 \times 10^{12}$ | $6.3 \times 10^{24}$ FLOPs |
| speed | $1024 \times 989 \times 10^{12} \times 0.40$ | $4.05 \times 10^{17}$ FLOP/s |
| time | $6.3 \times 10^{24} \div 4.05 \times 10^{17}$ | $1.56 \times 10^{7}$ s $\approx 180$ days |
| GPU-hours | $1024 \times 4320$ | 4.4 million |
| cost at an assumed \$2 per GPU-hour | | about \$8.8 million |

The result is sensitive to the assumptions: using the sparse peak by mistake halves the estimated time, and if the 40% were HFU with full recomputation, the run would take a third longer. Meta reported 6.4 million H100-hours for the **pre-training** of Llama-3-70B.

### 8.8.3. Checking Published Runs

The same arithmetic checks published reports, by dividing $6ND$ by the reported GPU-hours:

| | Llama-3-405B | DeepSeek-V3 |
|---|---|---|
| parameters $\times$ tokens | 405B $\times$ 15.6T | 37B activated $\times$ 14.8T |
| $6ND$ | $3.8 \times 10^{25}$ | $3.3 \times 10^{24}$ |
| GPUs | up to 16,384 H100 | 2,048 H800 |
| reported GPU-hours | 30.84 million (total) | 2.664 million (pre-training), 2.788 million (total) |
| average useful FLOP/s per GPU | 342 TFLOP/s, 35% of peak | 343 TFLOP/s, 35% of peak |

Both runs used their GPUs about equally well; DeepSeek-V3 was about 11 times cheaper because a token activates 11 times fewer parameters. Its widely quoted cost of \$5.6 million is the rental value of the final run's GPU-hours at \$2, not the cost of research, data and earlier experiments.

## 8.9. Serving Large Models

### 8.9.1. Prefill and Decode

Generating a response has two phases with very different costs. In the **prefill** phase the whole **prompt** is processed in one forward pass: each weight read from HBM is used for all prompt **tokens**, so **prefill** is compute-bound. In the *decode* phase each sequence produces one token per step, and every step reads all weights and the sequence's **KV cache** from HBM ([4.7.6](/4.7.6)). With BF16 weights (2 bytes) used for 2 **FLOPs** per sequence in the batch, the arithmetic intensity of decoding is about the batch size, far below the H100's $\pi/\beta \approx 295$: decoding is memory-bound. An upper bound on the speed of one sequence is therefore

$$
\text{tokens per second per sequence} \le \frac{\text{HBM bandwidth}}{\text{bytes read per decode step}}.
$$

For Llama-3-70B in BF16 on 8 H100s with tensor parallelism (aggregate bandwidth 26.8 TB/s), 141 GB of weights per step give at most about 189 tokens per second for a single sequence; FP8 weights and KV cache double this. A batch of 256 sequences shares the weight reads, but each sequence reads its own KV cache, 320 KiB per token for this model, 344 GB in total at 4K tokens of context: the batch produces about 14,000 tokens per second in total, but each user gets only about 55. Batching raises throughput, not the speed of each sequence. Measured systems typically reach a fraction of these bounds.

The KV cache is therefore the central resource of serving, and many architectural changes aim at shrinking it: **grouped-query attention** ([4.7.6](/4.7.6)), **multi-head latent attention** and linear-attention hybrids ([4.7.9](/4.7.9)), and quantizing the cache to 8 or 4 bits. Large services also separate the two phases onto different GPUs (*disaggregated* prefill and decode), since they need different hardware balances.

### 8.9.2. Continuous Batching

Requests arrive at random times and produce outputs of very different lengths. If a batch is formed and run until all its sequences finish, short requests wait for the longest one and GPUs idle on finished slots.

**Definition 8.9.1 (Continuous Batching)** **Continuous batching** (iteration-level scheduling; Orca, Yu et al., OSDI 2022) schedules a serving batch at the granularity of single decode steps: after every step, finished sequences leave the batch and waiting requests join it (after their prefill), so the batch is kept full.

### 8.9.3. PagedAttention

Continuous batching makes memory management of the KV cache hard: each sequence's cache grows by one entry per step to an unknown final length. Early systems reserved a contiguous region for the maximum length of every request and, by the measurements of Kwon et al., used only 20–40% of the reserved KV memory for actual cache entries.

**Definition 8.9.2 (PagedAttention)** **PagedAttention** (Kwon et al., SOSP 2023) stores the KV cache in fixed-size blocks (for example 16 tokens) allocated on demand from a shared pool, with a per-sequence block table mapping logical token positions to physical blocks, analogous to pages and page tables in the virtual memory of an operating system; the attention kernel gathers the keys and values through the block table.

Fragmentation drops to under 4% of the cache, so more sequences fit into memory and the batch can be larger; the vLLM system built on it achieved 2–4 times the throughput of earlier serving systems at the same latency. Blocks can also be shared: sequences with a common prefix (a system prompt, a long document, several samples of one prompt) point to the same physical blocks, copied only when they diverge. Reusing the cache of a common prefix across requests is the mechanism behind **prompt caching** ([4.2.14](/4.2.14)).

### 8.9.4. Speculative Decoding

Since a decode step is bound by reading the weights, checking several tokens in one forward pass costs almost the same as generating one. Speculative decoding exploits this.

**Definition 8.9.3 (Speculative Decoding)** **Speculative decoding** (Leviathan et al., ICML 2023; Chen et al. 2023) generates $\gamma$ draft tokens with a cheap *draft model* $q$, evaluates all of them with the target model $p$ in one forward pass, and accepts each draft token $x$ in order with probability $\min\bigl(1, p(x)/q(x)\bigr)$; at the first rejection it samples a replacement from the normalized residual distribution $\bigl(p - q\bigr)_+ / \sum\bigl(p - q\bigr)_+$ and discards the rest, and if all drafts are accepted it samples one more token from $p$.

**Theorem 8.9.1** Every token emitted by speculative decoding is distributed exactly according to the target model $p$ (given the preceding tokens).

**Proof** Consider one position, with draft distribution $q$ and target distribution $p$ over the vocabulary. A token $x$ is emitted either because it was drafted and accepted, with probability $q(x)\min\bigl(1, p(x)/q(x)\bigr) = \min\bigl(p(x), q(x)\bigr)$, or because the draft was rejected and $x$ was resampled. The total rejection probability is $1 - \sum_y \min(p(y), q(y)) = \sum_y \bigl(p(y) - q(y)\bigr)_+$, using $p(y) = \min(p(y), q(y)) + (p(y) - q(y))_+$. Hence

$$
\mathbb{P}(\text{emit } x) = \min\bigl(p(x), q(x)\bigr) + \sum_y \bigl(p(y) - q(y)\bigr)_+ \cdot \frac{\bigl(p(x) - q(x)\bigr)_+}{\sum_y \bigl(p(y) - q(y)\bigr)_+} = \min\bigl(p(x), q(x)\bigr) + \bigl(p(x) - q(x)\bigr)_+ = p(x). \qquad \square
$$

Speculative decoding thus speeds up generation without changing its output distribution. With acceptance rate $a = \sum_x \min(p(x), q(x))$, assumed independent across positions, one target pass yields on average $(1 - a^{\gamma + 1})/(1 - a)$ tokens. A simulation confirms the theorem and the acceptance rate:

```python
import numpy as np

rng = np.random.default_rng(0)
p = np.array([0.50, 0.25, 0.15, 0.10])          # target model's next-token distribution
q = np.array([0.30, 0.40, 0.20, 0.10])          # draft model's distribution

def speculative_token(rng):
    x = rng.choice(4, p=q)                       # draft proposes x ~ q
    if rng.random() < min(1.0, p[x] / q[x]):     # target accepts with prob min(1, p/q)
        return x, True
    residual = np.maximum(p - q, 0)              # otherwise resample from (p - q)+
    return rng.choice(4, p=residual / residual.sum()), False

draws = [speculative_token(rng) for _ in range(200_000)]
tokens = np.array([t for t, _ in draws])
print("empirical:", np.round(np.bincount(tokens, minlength=4) / len(tokens), 3), " target:", p)
print(f"acceptance rate {np.mean([a for _, a in draws]):.3f}  "
      f"(theory: sum of min(p, q) = {np.minimum(p, q).sum():.3f})")
```

```text
empirical: [0.5   0.25  0.151 0.099]  target: [0.5  0.25 0.15 0.1 ]
acceptance rate 0.800  (theory: sum of min(p, q) = 0.800)
```

The draft model can be a small model of the same family, or lightweight extra heads on the target model itself that predict several future tokens from its last hidden states (Medusa, EAGLE). DeepSeek-V3 trained a multi-token prediction module that is reused as a drafter: its second-token predictions were accepted 85–90% of the time, giving about 1.8 times the decoding speed. Speedups of 2–3 times are typical in practice, largest at small batch sizes where decoding is most memory-bound.

## Summary

- Training with mixed-precision **Adam** stores 16 bytes per parameter of model states (BF16 weights and gradients, FP32 master weights and two moments); activations take about $34\,sh$ bytes per layer and sequence with FlashAttention and can be traded for computation by recomputation (+33% **FLOPs** for full recomputation).
- BF16 has the range of FP32 and 7 mantissa bits; mixed precision computes in 16 bits but accumulates and updates in FP32, because small updates are rounded away in 16 bits. FP16 needs loss scaling against underflow. FP8 and 4-bit formats (MXFP4, NVFP4) work with fine-grained block scales; frontier models are now pre-trained in FP8 and NVFP4.
- An all-reduce is a reduce-scatter plus an all-gather; the ring algorithm sends $2(p-1)/p$ times the data per GPU, the optimum. Bandwidth falls by about ten times from HBM to NVLink to the network.
- Data parallelism equals large-batch **SGD** and communicates once per step; ZeRO shards optimizer states, gradients and parameters (stage 3 = FSDP, 1.5 times the traffic); tensor parallelism splits matrices and must stay inside a server; pipeline parallelism splits layers and pays a bubble of $(p-1)/(m+p-1)$. Practice: TP inside the server, PP until the model fits, DP for the rest, plus context and expert parallelism.
- Attention is memory-bound; FlashAttention tiles it in SRAM with an exact online **softmax** and recomputes scores in the backward pass, using linear instead of quadratic memory and running several times faster.
- Training compute is $C \approx 6ND$ (activated parameters for MoE); time is $C$ divided by GPUs, dense peak and MFU (about 40% in good runs).
- Decoding is memory-bound: **tokens** per second per sequence are bounded by bandwidth divided by the bytes read per step. Continuous batching, PagedAttention (paged **KV cache**, under 4% waste) and speculative decoding (exact, 2–3 times faster) are the standard serving techniques.
