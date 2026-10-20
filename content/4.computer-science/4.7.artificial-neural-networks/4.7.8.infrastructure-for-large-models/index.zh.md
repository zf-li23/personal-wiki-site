---
title: 大模型的训练基础设施
description: 训练时 GPU 内存去了哪里（每个参数 16 字节的模型状态、激活值、重计算）；从 FP32 到 BF16、FP8 与 NVFP4 的浮点格式，混合精度训练与损失缩放；集合通信与环形全规约；数据并行、ZeRO 与 FSDP，张量、流水线、上下文与专家并行及其组合；GPU 内存层次、Roofline 模型与 FlashAttention；用 6ND 与 MFU 估算训练算力；以预填充与解码、连续批处理、PagedAttention 和投机解码部署语言模型。
source_hash: 3df4ed701136
---

上一章把预训练模型当作数学对象来处理：一个网络、一个损失和一个优化器。本章讲的是真正训练和部署它需要什么。数字是出发点。Llama 3 405B 有 4050 亿个参数；仅权重在 16 位精度下就占 810 GB，是一块 H100 GPU 内存的十倍；它的训练消耗了 $3.8 \times 10^{25}$ 次**浮点运算**，相当于一块 H100 运行约 3000 年，或 16384 块 H100 运行两个多月。内存迫使我们切分模型，算力迫使我们并行使用数千个加速器。本章依次回答由此产生的问题：训练时的内存去了哪里（§8.1）；低精度数值格式怎样在不破坏优化的前提下节省内存和时间（§8.2）；GPU 之间怎样交换数据（§8.3），以及训练怎样通过数据并行、张量并行和流水线并行在它们之间分工（§8.4–§8.6）；为什么注意力的瓶颈是内存访问而不是算术运算，FlashAttention 怎样解决它（§8.7）；怎样估算一次训练的算力和时长（§8.8）；以及怎样高效地部署训练好的模型（§8.9）。**浮点数**的数值背景见 [3.5.1](/3.5.1)，**BLAS** 等矩阵乘法库见 [4.4.3](/4.4.3)，**Transformer** 及其 **KV 缓存**见 [4.7.6](/4.7.6)。算力应当在参数与数据之间如何分配，即规模定律，见 [4.7.9](/4.7.9)。

## 8.1. GPU 内存去了哪里

### 8.1.1. 模型状态与激活值

一个训练步的内存分为两类（Rajbhandari 等，2020）。

**定义 8.1.1（模型状态）** 训练的**模型状态**是大小与参数个数成正比的那些量：参数本身、它们的梯度，以及优化器状态（对 Adam 而言，是每个参数的一阶矩与二阶矩估计）。**激活值**是前向传播中为反向传播保存的中间结果，其大小与一次同时处理的词元数成正比。

除此之外还有临时缓冲区（通信缓冲区、矩阵乘法核的工作空间）和碎片：空闲内存散落在对大张量而言太小的空隙中，因此即使名义上还有五分之一以上的内存空闲，运行也可能因"内存不足"而失败。

### 8.1.2. 模型状态：每个参数 16 字节

在混合精度训练与 **Adam**（§8.2.2）下，每个参数的开销为

| 量 | 格式 | 字节数 |
|---|---|---|
| 前向与反向使用的权重 | BF16 | 2 |
| 梯度 | BF16 | 2 |
| 权重的 FP32 主副本 | FP32 | 4 |
| Adam 一阶矩 $\boldsymbol{m}$ | FP32 | 4 |
| Adam 二阶矩 $\boldsymbol{v}$ | FP32 | 4 |
| 合计 | | 16 |

优化器状态（后三行）占总量的四分之三，总量是推理所需每参数 2 字节的八倍。有些配置把梯度保存为 FP32（18 字节；这是 Megatron-LM BF16 训练的默认设置）。混合精度并不减少模型状态（用 Adam 的纯 FP32 训练同样需要 $4 + 4 + 4 + 4 = 16$ 字节）；它节省的是激活值内存，更重要的是时间。对 Llama-3-70B，模型状态为 $70.55 \times 10^9 \times 16$ 字节 $\approx 1{,}129$ GB。

### 8.1.3. 激活值

对于隐层宽度为 $h$、有 $a$ 个注意力头、序列长度为 $s$ 个**词元**的 **Transformer** 层，Korthikanti 等（2023）精确统计了 16 位精度下保存的激活值：矩阵乘法的输入、归一化和**激活函数**每层每个序列占 $34\,sh$ 字节；标准注意力还要加上 $a$ 个大小为 $s \times s$ 的分数矩阵，带**随机失活**时为 $5as^2$ 字节（分数、**softmax 函数** 输出和 dropout 掩码），不带时为 $2as^2$ 字节。第二项随序列长度二次增长：对 Llama-3-8B（32 个头），32K 词元时一层的分数就需要 $2 \times 32 \times 32768^2$ 字节 $\approx 69$ GB。FlashAttention（§8.7）从不保存分数矩阵，只剩线性项。对 Llama-3-8B（$h = 4096$，32 层）和一个 8192 词元的序列，每层为 $34 \times 8192 \times 4096$ 字节 $= 1.14$ GB，共 36.5 GB，是 16 GB 权重的两倍多。用于计算损失的 logits 在 FP32 下还要加 $4 \times s \times V$ 字节，对词表大小 $V = 128{,}256$ 为 4.2 GB。

激活值随每个*微批次*（一块 GPU 在一次前向–反向传播中处理的序列）的词元数线性增长：用四个序列代替一个，激活值变为四倍，而模型状态不变。

### 8.1.4. 激活重计算

**定义 8.1.2（激活重计算）** **激活重计算**（也称*梯度检查点*）在前向传播中只保存一部分激活值（通常是每个 Transformer 层的输入），其余的在反向传播时、需要梯度之前，通过重新运行对应层的前向计算来重新得到。

重计算是用算力换内存。*完全*重计算只保存各层输入（每层 $2sh$ 字节）和当前正在处理的那一层的激活值：对 8K 词元的 Llama-3-8B，峰值从 36.5 GB 降到 $2.15 + 1.14 \approx 3.3$ GB。代价是多一次前向传播：反向传播的代价约为前向的两倍，所以一个训练步从 3 个前向传播当量增加到 4 个，多 33% 的计算。*选择性*重计算只重新计算那些体积大但重算便宜的部分，主要是注意力分数：对 GPT-3，它把激活值内存减少了 70%，代价是约 1% 的额外计算。FlashAttention 本来就要重算分数，所以配合它使用时选择性重计算是免费的。Chen 等（2016）观察到，在 $L$ 层网络中每隔 $\sqrt{L}$ 层保存一次输入，可以把激活值内存从 $O(L)$ 降到 $O(\sqrt{L})$，代价是多一次前向传播。

### 8.1.5. 例：Llama 3 需要多少块 GPU？

这套核算可以写成一个小函数。它假设混合精度 Adam、FlashAttention、每块 GPU 一个 8192 词元的序列，并假设模型状态由 ZeRO-3（§8.5.1）在各 GPU 间均匀切分，ZeRO-3 不切分激活值；不含缓冲区。

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

H100 的 80 GB 在扣除运行时开销后可用约 76 GB，ZeRO-3 的缓冲区还要占几 GB，因此 8B 模型可以放进 8 块 GPU，使用重计算时放进 4 块。对 70B 模型，单个序列的 182.5 GB 激活值无法放进任何一块 GPU，无论有多少块 GPU 分担模型状态；重计算把它降到 13 GB，24 块 GPU（三台服务器）就够了。要切分激活值本身，需要张量并行或上下文并行（§8.6）。

![Llama-3-8B、70B 与 405B 在单个设备上的训练内存：BF16 权重与梯度、FP32 主权重与 Adam 矩（占总量的四分之三）、使用 FlashAttention 时一个 8192 词元序列的激活值，以及 FP32 logits；虚线是一块 H100 的 80 GB](./plots/memory-breakdown.py)

## 8.2. 数值格式与混合精度

### 8.2.1. 浮点格式

二进制**浮点数**形如 $\pm 1.f \times 2^{e}$，指数字段有 $E$ 位，小数（尾数）字段有 $M$ 位（[3.5.1](/3.5.1#sec-1.2.3)）。指数位决定范围，即可表示的最大和最小量级；尾数位决定精度，即**机器精度** $2^{-M}$，也就是 $1$ 与下一个更大的数之间的间隔。除 **IEEE 754 标准**的 FP32（**单精度**）外，**深度学习**还使用几种其他格式，记为 ExMy，表示 $x$ 位指数、$y$ 位尾数。

| 格式 | 位数（E，M） | 最大值 | 最小规格化数 | 机器精度 | 主要用途 |
|---|---|---|---|---|---|
| FP32 | 32（8，23） | $3.4 \times 10^{38}$ | $1.2 \times 10^{-38}$ | $2^{-23} \approx 1.2 \times 10^{-7}$ | 主权重、优化器状态、累加 |
| BF16 | 16（8，7） | $3.4 \times 10^{38}$ | $1.2 \times 10^{-38}$ | $2^{-7} \approx 0.0078$ | 训练大模型的默认格式 |
| FP16 | 16（5，10） | 65,504 | $6.1 \times 10^{-5}$ | $2^{-10} \approx 0.00098$ | 较老的 GPU（V100）；需要损失缩放 |
| FP8 E5M2 | 8（5，2） | 57,344 | $6.1 \times 10^{-5}$ | $2^{-2}$ | 梯度（范围重要） |
| FP8 E4M3 | 8（4，3） | 448 | $2^{-6} \approx 0.016$ | $2^{-3}$ | FP8 训练中的权重与激活值 |
| FP4 E2M1 | 4（2，1） | 6 | 1 | $2^{-1}$ | 分块缩放的权重与激活值（NVFP4、MXFP4） |

低于最小规格化数时，**非规格化数**保留较少的有效数字；FP16 在值**下溢**为零之前可以到达 $2^{-24} \approx 6 \times 10^{-8}$。E4M3 放弃了无穷（只保留一种位模式表示 NaN），腾出一个额外的指数值，把最大值从 240 提高到 448。FP4 E2M1 只有 $0, 0.5, 1, 1.5, 2, 3, 4, 6$ 这些量级。

**定义 8.2.1（BF16）** **BF16**（bfloat16，"brain floating point"，由 Google 为 TPU 提出）是 16 位浮点格式，含 1 位符号、8 位指数和 7 位尾数。它由 FP32 数的高 16 位构成，因此范围与 FP32 相同，约有 2–3 位十进制有效数字。

![浮点格式的范围与精度：可表示的正量级区间（对数 $\log_2$ 刻度，非规格化部分颜色较浅）以及机器精度；BF16 有 FP32 的范围，精度只有几位，而 FP16 与 FP8 用范围换精度](./plots/number-formats.py)

更小的格式在两方面有收益。每个数的内存和内存访问量减半或变为四分之一，而且 GPU 的*张量核心*（用硬件计算小矩阵乘积的单元）做 16 位矩阵乘法比通用 FP32 运算快 15–30 倍，FP8 比 BF16 快一倍，FP4 又快一倍。

### 8.2.2. 混合精度方案

**定义 8.2.2（混合精度训练）** **混合精度训练**（Micikevicius 等，ICLR 2018）用 16 位格式（BF16 或 FP16）进行前向与反向传播，并保存激活值与梯度，矩阵乘积在 FP32 中累加，同时保留权重的 FP32 *主副本*：优化器在 FP32 中更新主权重，再把它们舍入后复制成 16 位，用于下一步。

之所以需要主副本，是因为更新 $w \leftarrow w + \Delta w$ 中的**舍入误差**。当 $\lvert\Delta w\rvert$ 小于 $w$ 与其在 16 位格式中相邻数之间间隔的一半时，和会舍入回 $w$，更新就完全丢失了。在 BF16 中，$w$ 处的间隔约为 $2^{-7}\lvert w\rvert$，所以只要 $\lvert w\rvert$ 超过约 $256\,\lvert\Delta w\rvert$ 就会发生这种情况（FP16 约为 $2{,}048\,\lvert\Delta w\rvert$）。这个比值很容易达到：**Adam** 的步长与学习率大小相当，所以一个大小为 $0.02$ 的权重，在学习率衰减到 $3 \times 10^{-5}$ 时，比值约为 670，用纯 BF16 它就不再移动了。NumPy 没有 BF16 类型，但把 FP32 舍入到它的高 16 位就能精确模拟：

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

前三行显示了两种 16 位格式的取舍：FP16 保留三位十进制数字，却在 70,000 处**溢出**、在 $10^{-8}$ 处下溢；BF16 两者都能表示，但 $1 + 0.003$ 会舍入为 $1$。最后一行说明了为什么要保留主权重：在纯 BF16 中，一千次大小为 $3 \times 10^{-5}$ 的更新完全没有效果，而在 FP32 中累加则能让权重正确移动。出于同样的原因，矩阵乘法单元以 FP32 累加乘积之和。

### 8.2.3. FP16 的损失缩放

FP16 有相反的问题：小的梯度会下溢。Micikevicius 等发现，在一个 SSD 目标检测器中，大部分激活值梯度低于 $2^{-24}$，在 FP16 中变为零，网络因此无法训练，而 FP16 范围的上半部分却没有用到。

**定义 8.2.3（损失缩放）** **损失缩放**在反向传播前把损失乘以常数 $S$，这样由链式法则，每个梯度都乘上 $S$，被移入可表示的范围；在优化器更新前再（在 FP32 中）把梯度除以 $S$。在*动态*损失缩放中，只要梯度里出现无穷或 NaN，就把 $S$ 减半并跳过该步；每经过固定步数（PyTorch 的 `GradScaler` 为 2000 步）没有溢出，就把 $S$ 加倍。

对 SSD，因子 8 就足够了（mAP 为 77.1%，FP32 为 76.9%）。由于缩放在更新前被撤销，学习率和其他**超参数**不需要改变。

### 8.2.4. BF16 为什么胜出

BF16 在张量核心上有 FP16 的速度和 FP32 的范围：$10^{-38}$ 到 $10^{38}$ 的值都能放下，所以梯度既不会下溢也不会上溢，不需要损失缩放。它的低精度由方案中的两个 FP32 环节弥补：矩阵乘法中的累加和主权重。自 A100（2020）以及更早的 TPU 起，带 FP32 主权重的 BF16 是训练大模型的默认方案；带损失缩放的 FP16 主要保留在较老的硬件上。

### 8.2.5. FP8 训练

在 H100 及之后的 GPU 上，FP8 把 BF16 的矩阵乘法峰值吞吐量提高一倍，但 E4M3 只覆盖约 $0.016$（规格化）到 $448$ 的量级。因此 FP8 训练在转换前把每组数乘以一个缩放因子，因子的选取使这组数的最大绝对值映射到格式的最大值，再用这些因子除矩阵乘积的结果；这就是应用到每个张量上的损失缩放。

- *按张量*缩放（NVIDIA Transformer Engine 在 Hopper 上的默认方式）每个张量使用一个缩放因子，通常取自最近若干步的最大值（"延迟缩放"）。含有极大值的离群通道会迫使缩放因子变小，于是张量中大量小值下溢。
- *细粒度*缩放由 DeepSeek-V3（2024 年 12 月）大规模引入，对激活值每 $1 \times 128$ 个元素（一个**词元**的 128 个通道）一个分块、对权重每 $128 \times 128$ 一个分块使用一个缩放因子，这样离群值只破坏它自己所在的分块。DeepSeek-V3 的所有 FP8 矩阵乘积输入都使用 E4M3，并且每隔较短间隔把部分和提升到 FP32，因为 H800 的 FP8 张量核心累加精度有限；主权重、权重梯度和优化器状态则保持较高精度。它的**预训练**损失与 BF16 基线相差不超过 0.25%。
- Blackwell GPU（2025）在硬件上支持开放计算项目（Open Compute Project）的*微缩放*格式所描述的这种分块缩放：MXFP8 使用 32 个值一块，共享一个以 8 位（E8M0）存储的 2 的幂缩放因子。

### 8.2.6. 四位格式

四位对于单一的浮点格式来说太少，无法单独使用；它们只有配合细粒度缩放因子才行。*MXFP4* 把 E2M1 值按 32 个一块存储，并配一个 E8M0 缩放因子。*NVFP4* 是 NVIDIA 为 Blackwell 设计的格式，把 E2M1 值按 16 个一块存储，每块配一个 FP8 E4M3 缩放因子（它与 2 的幂不同，可以紧密贴合该块），每个张量再配一个 FP32 缩放因子，合计每个值约 4.5 位。四位权重早已用于推理（量化方法如 GPTQ 与 AWQ，以及 [4.7.7](/4.7.7#sec-7.6.5) 中 QLoRA 的 NF4 格式）；自 2025 年起它们也用于训练。NVIDIA 用 NVFP4 原生预训练了 Nemotron 3 Super（2026 年 3 月）和 Nemotron 3 Ultra（2026 年 6 月，5500 亿参数），DeepSeek 发布的 DeepSeek-V4（2026 年 4 月）的专家权重为 FP4，其他权重为 FP8。在每种情形下，敏感部分（第一层和最后一层、优化器状态、累加）仍保持较高精度。

## 8.3. 集合通信

### 8.3.1. 集合操作

并行训练需要 GPU 之间合并数据：对梯度求和、共享参数、把**词元**发送给专家。这些操作称为*集合通信*，即组内所有 GPU 共同参与的调用，在 NVIDIA GPU 上由 NCCL 库实现。设 $p$ 块 GPU 各持有 $n$ 个元素的缓冲区。

**定义 8.3.1（全规约）** **全规约**使每块 GPU 上都得到 $p$ 个缓冲区的逐元素和（或其他满足结合律的规约）。**规约散射**只在第 $i$ 块 GPU 上留下和的 $p$ 等分切片中的第 $i$ 片，**全收集**则把来自每块 GPU 的一个切片拼接起来，并把完整结果留在每块 GPU 上。全规约等于规约散射后再做全收集。

| 集合操作 | 每块 GPU 最终得到 | 每块 GPU 发送的数据量（带宽最优） | 主要用途 |
|---|---|---|---|
| 广播 | 某块 GPU 缓冲区的副本 | $n$ | 初始权重 |
| 规约散射 | 和的一个切片 | $\frac{p-1}{p}n$ | ZeRO / FSDP 梯度 |
| 全收集 | 全部切片 | $\frac{p-1}{p}n$ | ZeRO / FSDP 权重 |
| 全规约 | 完整的和 | $2\frac{p-1}{p}n$ | 数据并行梯度、张量并行激活值 |
| 全交换（all-to-all） | 发给它的数据块，每块 GPU 一块 | $\frac{p-1}{p}n$ | 把词元路由给专家 |

### 8.3.2. 环形全规约

GPU 排成一个环，每个缓冲区切成 $p$ 块。在规约散射阶段，共 $p - 1$ 步，每一步每块 GPU 把一块发送给它的后继，后继把它加到自己那一块的副本上；$p - 1$ 步之后，每块 GPU 持有完整和的一块。在全收集阶段，完成的数据块再用 $p - 1$ 步沿环传递。每一步每块 GPU 发送一块，即 $n/p$ 个元素，所以每块 GPU 共发送 $2(p-1)n/p < 2n$ 个元素，与 $p$ 无关；Patarasuk 和 Yuan（2009）证明，使用点对点消息且不做压缩的任何算法都不能做得更好。代价是*延迟*：设每条消息有固定的启动开销 $\alpha$，带宽为 $\beta$ 字节每秒，则时间约为

$$
T_{\text{ring}} \approx 2(p - 1)\,\alpha + 2\,\frac{p-1}{p}\,\frac{n_{\text{bytes}}}{\beta},
$$

其中第一项随 $p$ 增长；对于小消息或非常多的 GPU，NCCL 会切换到只需 $O(\log p)$ 步的树形算法。下面用数组做模拟，同时检验结果和通信量：

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

### 8.3.3. 带宽层次

集合通信在哪里运行，与发送多少同样重要。在层次结构的每一级，带宽大约下降一个数量级：

| 层级 | H100（每块 GPU，每个方向） | B200 |
|---|---|---|
| HBM，GPU 自己的内存 | 3.35 TB/s | 8 TB/s |
| NVLink，一台服务器内的 8 块 GPU 之间 | 450 GB/s | 900 GB/s |
| 服务器之间的网络（InfiniBand 或以太网） | 50 GB/s（一张 400 Gb/s 网卡） | 50–100 GB/s |

厂商给出的数字需要仔细看待：H100 NVLink 的"900 GB/s"是双向之和，网卡则以比特为单位标称（400 Gb/s 即 50 GB/s）。由 NVLink 相连的一组 GPU 称为 *NVLink 域*，是一台 8 块 GPU 的服务器，或 GB200 NVL72 机架中的 72 块。由此得到的规则组织了本章其余部分：每一层都要等待的通信应放在 NVLink 域内；每步只发生一次、或可以与计算重叠的通信，则可以跨越网络。

## 8.4. 数据并行

**定义 8.4.1（数据并行）** 在**数据并行**（DP）中，$p$ 块 GPU 各持有模型的完整副本，并各处理每个小批量的不同切片；反向传播之后，用一次全规约在各 GPU 间对梯度取平均，每块 GPU 施加相同的更新。

**命题 8.4.1** 如果一个小批量的损失是各样本损失的平均，并且大小为 $B$ 的小批量 $\mathcal{B}$ 被分成 $p$ 个大小为 $B/p$ 的切片 $\mathcal{B}_1, \dots, \mathcal{B}_p$，则 $p$ 个切片梯度的平均等于整个小批量的梯度。因此数据并行训练在数学上与批量大小为 $B$ 的**小批量梯度下降**完全相同。

**证明** 由梯度的线性性，

$$
\frac{1}{p}\sum_{k=1}^{p}\nabla_{\boldsymbol{\theta}}\Bigl(\frac{p}{B}\sum_{i \in \mathcal{B}_k}\ell_i(\boldsymbol{\theta})\Bigr) = \frac{1}{B}\sum_{k=1}^{p}\sum_{i \in \mathcal{B}_k}\nabla_{\boldsymbol{\theta}}\ell_i(\boldsymbol{\theta}) = \nabla_{\boldsymbol{\theta}}\Bigl(\frac{1}{B}\sum_{i \in \mathcal{B}}\ell_i(\boldsymbol{\theta})\Bigr). \qquad \square
$$

（切片内耦合各样本的运算，如**批归一化**，会破坏这一等式，除非它们的统计量也被同步。）所以增加 GPU 意味着更大的批量，学习率必须相应调整（[4.7.4](/4.7.4)）。通信是每步对全部梯度做一次全规约，对 BF16 下 $N$ 个参数，每块 GPU 约 $2 \times 2N$ 字节，并且可以被隐藏：PyTorch 的 `DistributedDataParallel` 按反向传播产生梯度的顺序，把梯度归入约 25 MB 的桶，在反向传播继续处理更早的层时就开始每个桶的全规约。对 70 亿参数的模型，14 GB 的梯度在连接良好的集群上约需 50–75 ms，比反向传播还短。朴素数据并行的问题是内存：每块 GPU 都存储每参数的全部 16 字节，70 亿参数需要 112 GB，增加 GPU 并不能减少它。

## 8.5. 切分模型状态：ZeRO 与 FSDP

### 8.5.1. ZeRO

**定义 8.5.1（ZeRO）** **零冗余优化器**（ZeRO；Rajbhandari 等，SC 2020）是这样一种数据并行：模型状态在 $p$ 块数据并行的 GPU 上被划分（*分片*）而不是复制，每块 GPU 只存储并更新自己那 $1/p$ 份。阶段 1 对优化器状态（包括 FP32 主权重）分片，阶段 2 再对梯度分片，阶段 3 再对 16 位参数分片。

ZeRO 并不是一种新的优化器：每一步的结果与普通 **Adam** 相同。它的诀窍在于，全规约就是规约散射后再做全收集，而更新可以在两者之间完成。规约散射之后，每块 GPU 得到自己那部分参数切片的梯度之和，用自己的优化器状态更新该切片，然后全收集把更新后的 16 位参数分发出去。因此阶段 1 和 2 的通信量与朴素数据并行完全相同。阶段 3 在前向传播中每层用完后就释放该层的参数，反向传播时必须再次全收集，共三次模型大小的传输而不是两次，通信量是数据并行的 1.5 倍。

| 策略 | 每块 GPU 上每参数的字节数 | Llama-3-70B，64 块 GPU | 512 块 GPU | 相对 DP 的通信量 |
|---|---|---|---|---|
| DP | $16$ | 1,129 GB | 1,129 GB | 1 |
| ZeRO-1 | $4 + 12/p$ | 295 GB | 284 GB | 1 |
| ZeRO-2 | $2 + 14/p$ | 157 GB | 143 GB | 1 |
| ZeRO-3 | $16/p$ | 17.6 GB | 2.2 GB | 1.5 |

只有阶段 3 能无下限地减少内存：无论有多少块 GPU，ZeRO-1 和 ZeRO-2 在每块 GPU 上仍保留每参数 4 字节和 2 字节，最多只节省 4 倍和 8 倍。所有阶段都不切分激活值，因为每块 GPU 仍然在自己的数据上运行所有层。

### 8.5.2. 全分片数据并行

**定义 8.5.2（全分片数据并行）** **全分片数据并行**（FSDP）是 PyTorch 对 ZeRO 阶段 3 的实现。模型被划分为若干单元，通常每个 Transformer 块一个单元；前向传播中，每个单元的参数在使用前被全收集，使用后释放；反向传播中再次全收集，并对梯度做规约散射，使每块 GPU 保留自己那一片的梯度。

通信在单独的流上进行并被*预取*：第 $k + 1$ 个单元的全收集在第 $k$ 个单元计算时就发出，因此只有传输比计算慢时 GPU 才需要等待（对 GPT-175B，反向预取使训练快了约 18%）。FSDP2（2024）按行对每个张量分片，而不是把一个单元的所有参数展平到一个缓冲区，这使它能与张量并行和 FP8 缩放因子干净地组合。*混合分片*（HSDP）在一台服务器内分片，使全收集留在 NVLink 上，而在服务器之间像朴素数据并行那样复制；代价是无论使用多少台服务器，每块 GPU 都保留 $1/8$ 的模型状态，对 Llama-3-70B 为 141 GB，单靠它太多了。

## 8.6. 模型并行

### 8.6.1. 张量并行

**定义 8.6.1（张量并行）** **张量并行**（TP）把每一层的权重矩阵切分到一组 GPU（组的大小称为 *TP 度*）上，使每块 GPU 只存储并相乘每个矩阵的一个切片，并在层内用集合操作合并部分结果。

Megatron-LM（Shoeybi 等，2019）切分 **Transformer** 的前馈块 $Y = \operatorname{GeLU}(XW_1)W_2$，使它只需要一次全规约。$W_1 = [W_1^{(1)}, \dots, W_1^{(p)}]$ 按列切分；由于 GeLU 是逐元素作用的，第 $i$ 块 GPU 无需通信就能算出 $\operatorname{GeLU}(XW_1^{(i)})$。$W_2$ 按对应的行切分，于是

$$
Y = \operatorname{GeLU}(XW_1)\,W_2 = \sum_{i=1}^{p}\operatorname{GeLU}\bigl(XW_1^{(i)}\bigr)\,W_2^{(i)},
$$

这是各 GPU 部分结果之和，一次全规约就能把它们加起来。（若改为按行切分 $W_1$，则在非线性之前就需要通信。）反向传播中，关于 $X$ 的梯度也是部分结果之和，因此在块的输入处还需要再做一次全规约。

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

注意力以同样的方式按头切分：查询、键、值投影按列切分，使每块 GPU 算出完整的头；输出投影按行切分，之后做一次全规约。因此一个 Transformer 层在前向传播中需要两次全规约，反向传播中也需要两次，每次的大小等于该层激活值的大小。*序列并行*进一步把 TP 单独使用时会被复制的归一化与 **随机失活**区域沿**词元**维度切分，把每次全规约换成一次规约散射加一次全收集，总通信量相同；每块 GPU 的激活值内存因此缩小为原来的 $1/\text{TP 度}$。

代价是这种通信位于关键路径上。对 TP 度为 8、微批次为 4096 个词元的 Llama-3-70B，每块 GPU 每层发送约 $4 \times 2 \cdot \tfrac78 \times 4096 \times 8192 \times 2$ 字节 $\approx 470$ MB，而由于通信量和计算量都随词元数增长，更大的批量并不能稀释它。在 NVLink（450 GB/s）上这只占计算时间的一小部分；在 50 GB/s 的网络链路上，它会与计算一样长甚至更长。因此张量并行用在一台服务器之内，度至多为 8，Megatron 的测量（64 块 A100 上的 1620 亿参数 GPT）恰好在 TP 度为 8 时最快。

### 8.6.2. 流水线并行

**定义 8.6.2（流水线并行）** **流水线并行**（PP）把网络的各层划分为放在不同 GPU 上的 $p$ 个连续*阶段*；激活值从一个阶段送到下一个阶段，其梯度反向传递；小批量被划分为 $m$ 个微批次，依次流过各阶段，使不同阶段同时处理不同的微批次。

只有一个微批次时，同一时刻只有一块 GPU 在工作。GPipe（Huang 等，2019）把 $m$ 个微批次背靠背地送过所有阶段，再运行所有反向传播，累积梯度，每步只更新一次（一次*冲刷*），这使更新与不使用流水线的训练保持一致。每步开始和结束时的空闲时间称为*流水线气泡*。设每个微批次在每个阶段的前向和反向时间分别为 $t_F$ 与 $t_B$，则每块 GPU 在长度为 $(m + p - 1)(t_F + t_B)$ 的一步中空闲 $(p - 1)(t_F + t_B)$，所以空闲占比为

$$
\frac{p - 1}{m + p - 1}.
$$

对 4 个阶段和 8 个微批次，这是 $3/11 \approx 27\%$；有 32 个微批次时是 $3/35 \approx 8.6\%$。（有些论文改以忙碌时间为分母，报告 $(p-1)/m$。）更多微批次可以稀释气泡但不能消除它，而它们受全局批量大小以及小微批次上矩阵乘法效率的限制。

![4 块 GPU、8 个微批次、反向传播时间为前向两倍时的流水线调度：GPipe 先运行所有前向传播再运行所有反向传播；1F1B 在预热之后交替进行。两者的空闲时间都占 27%，但在 1F1B 下，第一块 GPU 最多持有 4 个微批次的激活值，而不是 8 个](./plots/pipeline-schedule.py)

GPipe 必须保存全部 $m$ 个微批次的激活值。*1F1B* 调度（一次前向、一次反向；PipeDream，Narayanan 等，2019）让每个微批次的反向传播尽早开始，使得预热之后每次前向传播之后都接一次反向传播；气泡相同，但每个阶段至多持有 $p$ 个微批次的激活值。*交错式* 1F1B 在每块 GPU 上放置 $v$ 个不相邻的层块，把气泡除以 $v$，代价是 GPU 之间的传输次数变为 $v$ 倍。*零气泡*调度（Qi 等，ICLR 2024）把反向传播拆成关于输入的梯度（前一阶段在等待它）和关于权重的梯度（可以推迟到气泡中完成）。DeepSeek-V3 的调度 DualPipe（[4.7.9](/4.7.9)）从流水线两端同时送入微批次，并使一个微批次的计算与另一个微批次的通信重叠。流水线并行的通信量很小，每个阶段边界上每个微批次只有一个激活值张量（Llama-3-70B 的 4096 词元约为 67 MB），因此可以跨服务器运行。

### 8.6.3. 上下文并行与专家并行

还有两个维度，切分其他维度切分不了的东西。*上下文并行*在每一层把一个长序列切分到多块 GPU 上；注意力需要序列的全部键和值，通过全收集或沿环传递数据块（环形注意力，ring attention）来交换它们。Llama 3 在它 128K 词元的训练阶段用了它。*专家并行*把混合专家层（[4.7.9](/4.7.9)）的各个专家放在不同的 GPU 上，每层用两次全交换把每个词元送到其专家所在的 GPU 再送回来。

### 8.6.4. 各个维度的组合

各维度相乘：TP 度为 $t$、有 $s$ 个流水线阶段和 $d$ 个数据并行副本时，GPU 总数为 $t \cdot s \cdot d$。三者全部组合称为 *3D 并行*。放置方式遵循 §8.3.3 的带宽层次。

| | 切分什么 | 每块 GPU 的模型状态 | 每块 GPU 的激活值 | 通信 | 典型位置与规模 |
|---|---|---|---|---|---|
| DP（ZeRO-1） | 批量 | 每参数 $4 + 12/d$ 字节 | 与单块 GPU 相同 | 每步一次梯度，与反向传播重叠 | 跨服务器，64–128 |
| ZeRO-3 / FSDP | 批量与模型状态 | 每参数 $16/d$ 字节 | 与单块 GPU 相同 | DP 的 1.5 倍，带预取 | 跨服务器 |
| TP（+ SP） | 权重矩阵 | 除以 $t$ | 除以 $t$（配合 SP） | 每层 4 次阻塞的全规约 | 服务器内，$t \le 8$ |
| PP | 层 | 除以 $s$ | 第一阶段约为一个微批次穿过所有层（1F1B） | 阶段边界上的激活值，加上气泡 | 跨服务器，16–64 |

Narayanan 等（SC 2021）的做法是：在服务器内使用张量并行，增加流水线阶段直到模型放得下，其余的 GPU 用于数据并行；对很长的序列加上上下文并行，对混合专家加上专家并行。两个已发表的训练运行说明了这一点。

| 运行 | GPU | TP | CP | PP | EP | DP |
|---|---|---|---|---|---|---|
| Llama-3-405B，8K 上下文 | 16,384 块 H100 | 8 | 1 | 16 | – | 128 |
| Llama-3-405B，128K 上下文 | 16,384 块 H100 | 8 | 16 | 16 | – | 8 |
| DeepSeek-V3（混合专家） | 2,048 块 H800 | – | – | 16 | 64 | 128（ZeRO-1） |

Llama 3 把各维度从内到外排列为 TP、CP、PP、DP，并用 FSDP 对数据并行维度分片；它达到了 BF16 峰值的 38–43%。DeepSeek-V3 通过精细的内存节省完全避开了张量并行，部分原因是受出口限制的 H800 的 NVLink 带宽被削减，并把专家分散到 8 台服务器的 64 块 GPU 上。

## 8.7. GPU 上的注意力：FlashAttention

### 8.7.1. 内存层次与 Roofline 模型

GPU 由许多流式多处理器（SM）组成，每个 SM 有一小块快速的片上 SRAM（每个 SM 约 100–250 KB，总计约 20–50 MB），此外还有一大块片外 HBM（80–288 GB）。在 A100 上，SRAM 比 HBM 快约 13 倍、小约 2000 倍。计算用到的每个数都必须先从 HBM 搬进 SM。

**定义 8.7.1（算术强度）** 一次计算的**算术强度**是它每字节内存访问所执行的浮点运算次数。在 **Roofline 模型**（Williams 等，2009）中，强度为 $I$ 的计算在峰值算力为 $\pi$（FLOP/s）、内存带宽为 $\beta$（字节/秒）的处理器上，最快只能以 $\min(\pi, I\beta)$ 运行；若 $I < \pi/\beta$ 则称为*访存受限*，否则称为*计算受限*。

对 A100，$\pi/\beta = 312\ \mathrm{TFLOP/s} \div 1.555\ \mathrm{TB/s} \approx 200$ 次**浮点运算**每字节；对 H100 约为 295。大型**矩阵乘法**的强度与矩阵维数成正比，是计算受限的。逐元素运算、归一化和 **softmax 函数** 的强度只有每字节几次浮点运算，是访存受限的。

### 8.7.2. 为什么标准注意力是访存受限的

单个头的标准注意力以独立的核计算 $S = QK^{\mathsf T}/\sqrt{d}$、$P = \operatorname{softmax}(S)$ 和 $O = PV$，其中 $Q, K, V \in \mathbb{R}^{N \times d}$。每个核把结果写入 HBM，下一个核再读回，所以两个 $N \times N$ 矩阵 $S$ 和 $P$ 要在 HBM 上往返一次，反向传播还要再读一次 $P$。每个分数约需 $4d$ 次浮点运算（两次矩阵乘积），对应 8 字节的 BF16 访存，强度为 $d/2$，头维数 64–128 时为 32–64，远低于 200。对 8K **词元**的 Llama-3-8B，仅 $P$ 每层就有 $32 \times 8192^2 \times 2$ 字节 $\approx 4.3$ GB，为 32 层的反向传播保存它需要 137 GB。

### 8.7.3. 分块与在线 softmax

**定义 8.7.2（FlashAttention）** **FlashAttention**（Dao 等，NeurIPS 2022）是一种精确的注意力算法，它通过*分块*在一个核中算出输出：加载能放进 SRAM 的 $Q$、$K$、$V$ 的块，在 SRAM 中算出对应的分数块及其对输出的贡献，从不把分数矩阵或概率矩阵写入 HBM。softmax 由在线 softmax 递增地计算，反向传播则由 $Q$、$K$ 和保存的行统计量重新计算分数。

困难在于 softmax：对一行归一化需要它的最大值和对全部 $N$ 个键的求和，但键是一块一块到来的。*在线 softmax*（Milakov 和 Gimelshein，2018）对每个查询行保留一个滚动的最大值 $m$、$\mathrm{e}^{s - m}$ 的滚动和 $\ell$ 以及一个未归一化的输出 $\boldsymbol{o}$。当一块新的分数 $\boldsymbol{s}$ 及其值向量 $V_j$ 到来时，

$$
m' = \max\bigl(m, \max_k s_k\bigr), \qquad \ell' = \mathrm{e}^{m - m'}\ell + \sum_k \mathrm{e}^{s_k - m'}, \qquad \boldsymbol{o}' = \mathrm{e}^{m - m'}\boldsymbol{o} + \sum_k \mathrm{e}^{s_k - m'}\boldsymbol{v}_k,
$$

也就是说，只要最大值上升，旧的和与旧的输出就要乘上 $\mathrm{e}^{m - m'}$ 重新缩放。最后 $\boldsymbol{o}/\ell$ 恰好是 softmax 加权平均：结果不是近似。减去滚动最大值使指数不会上溢，这与 [4.7.1](/4.7.1#sec-1.5.2) 的稳定 softmax 相同。反向传播只需保存输出和每行一个数，即对数和指数 $m + \log\ell$。

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

### 8.7.4. 重计算、结果与后续版本

FlashAttention 比标准注意力做更多的算术运算，因为反向传播要重新计算分数，但内存访问量少得多。对 A100 上 GPT-2 medium 的注意力（前向加反向），原论文报告：75.2 对 66.6 GFLOPs（多 13%），HBM 访存 4.4 对 40.3 GB（少 9 倍），耗时 7.3 对 41.7 ms（快 5.7 倍）。它的额外内存随序列长度线性而不是二次增长，这使长上下文训练变得可行：在 8K 词元时，13 亿参数的 GPT 以约 56% 的 A100 峰值训练，比 Megatron-LM 在 2K 时使用标准注意力还要快。这是该领域的典型模式：浮点运算昂贵但节省内存访问的重计算，会让访存受限的代码更快。

每一代 GPU 都需要一个新版本。FlashAttention-2（2023）减少了非矩阵乘法运算（它们的速度只有张量核心的一小部分），并沿序列长度并行，在 A100 上速度翻倍。FlashAttention-3（2024）利用 H100 的异步数据搬运单元使加载与计算重叠，并加入了 FP8，达到 BF16 峰值的约 85%。FlashAttention-4（2026）面向 Blackwell：那里矩阵单元每个 SM 的速度翻了一倍，而计算指数的单元没有，于是用普通乘加单元上的多项式近似计算一部分指数。

## 8.8. 估算训练算力

### 8.8.1. 计算浮点运算次数：$C \approx 6ND$

对于有 $N$ 个参数、在 $D$ 个**词元**上训练的稠密 **Transformer**，训练算力约为

$$
C \approx 6ND \ \text{FLOPs}.
$$

前向传播中，每个权重对每个词元参与一次乘法和一次加法，共 2 次**浮点运算**。线性层 $\boldsymbol{y} = W\boldsymbol{x}$ 的反向传播要计算两个同样大小的乘积：用于向前传递的输入梯度 $W^{\mathsf T}\nabla_{\boldsymbol{y}}$ 和权重梯度 $\nabla_{\boldsymbol{y}}\boldsymbol{x}^{\mathsf T}$，每个权重每个词元 4 次浮点运算。推理只需前向传播，每个词元约 $2N$ 次浮点运算。对 GPT-3，$6 \times 175 \times 10^9 \times 300 \times 10^9 = 3.15 \times 10^{23}$ 次浮点运算，与报告的 $3.14 \times 10^{23}$ 接近。这条规则有三点修正：

- 注意力的乘积 $QK^{\mathsf T}$ 与 $PV$ 没有权重，没有被计入；对序列长度 $s$、隐层宽度 $h$ 并带有**因果掩码**的情形，它们相对 $6ND$ 的占比约为 $s/(12h)$，Llama-3-405B 在 8K 词元时为 4%，在 128K 时为 67%；
- 对混合专家，$N$ 是每个词元*激活*的参数个数（DeepSeek-V3 为 370 亿，而不是 6710 亿）；
- 重计算使硬件实际执行约 $8ND$ 次浮点运算，但有效工作仍然是 $6ND$。

### 8.8.2. 从浮点运算到 GPU 小时

**定义 8.8.1（模型浮点运算利用率）** 一次训练的**模型浮点运算利用率**（MFU）是有效浮点运算速率（每个词元的模型浮点运算 $6N$ 加上注意力，乘以每秒处理的词元数）与硬件峰值浮点运算速率之比。*硬件浮点运算利用率*（HFU）还计入重计算的浮点运算，所以 $\mathrm{HFU} \ge \mathrm{MFU}$。

于是训练时间为 $C / (\text{GPU 数} \times \text{峰值} \times \mathrm{MFU})$。峰值必须取稠密峰值：NVIDIA 对 H100 BF16 吞吐量宣传的 1,979 TFLOP/s 数字假定了 2:4 结构化稀疏（一半权重为零），稠密峰值是它的一半。

| GPU | 稠密 BF16 TFLOP/s | 稠密 FP8 TFLOP/s | HBM TB/s |
|---|---|---|---|
| A100 80 GB | 312 | – | 2.0 |
| H100 SXM | 989 | 1,979 | 3.35 |
| H200 SXM | 989 | 1,979 | 4.8 |
| B200 | 2,250 | 4,500 | 8 |

调优良好的大规模训练能达到约 40% 的 MFU；其余消耗在没有被隐藏的通信、流水线气泡和访存受限的核上。MFU 随规模和上下文长度下降（Llama-3-405B：8K 块 GPU 时 43%，16K 块时 41%，128K 上下文时 38%），把故障和重启在内的全部计费时间都算上则更低（PaLM：稳态 46.2%，总体约 31%）。一个方便的单位：一个 H100 小时在 40% MFU 下是 $989 \times 10^{12} \times 0.4 \times 3600 \approx 1.4 \times 10^{18}$ 次浮点运算，所以 $10^{24}$ 次浮点运算约为 70 万个 H100 小时。

**例 8.8.1** 一个 700 亿参数的稠密模型，在 15 万亿个词元（Llama-3-70B 的规模）上、用 1024 块 H100 以 40% MFU 训练：

| 步骤 | 计算 | 结果 |
|---|---|---|
| 算力 | $6 \times 70 \times 10^9 \times 15 \times 10^{12}$ | $6.3 \times 10^{24}$ 次浮点运算 |
| 速度 | $1024 \times 989 \times 10^{12} \times 0.40$ | $4.05 \times 10^{17}$ FLOP/s |
| 时间 | $6.3 \times 10^{24} \div 4.05 \times 10^{17}$ | $1.56 \times 10^{7}$ s $\approx 180$ 天 |
| GPU 小时 | $1024 \times 4320$ | 440 万 |
| 按假设的每 GPU 小时 \$2 计的费用 | | 约 \$880 万 |

结果对假设很敏感：误用稀疏峰值会使估算时间减半，而如果那 40% 是带完全重计算的 HFU，训练时间会长三分之一。Meta 报告 Llama-3-70B 的**预训练**用了 640 万个 H100 小时。

### 8.8.3. 核对已发表的训练运行

用同样的算术可以核对已发表的报告，即用 $6ND$ 除以报告的 GPU 小时数：

| | Llama-3-405B | DeepSeek-V3 |
|---|---|---|
| 参数 $\times$ 词元 | 405B $\times$ 15.6T | 37B 激活 $\times$ 14.8T |
| $6ND$ | $3.8 \times 10^{25}$ | $3.3 \times 10^{24}$ |
| GPU | 最多 16,384 块 H100 | 2,048 块 H800 |
| 报告的 GPU 小时 | 3084 万（总计） | 266.4 万（预训练），278.8 万（总计） |
| 每块 GPU 平均有效 FLOP/s | 342 TFLOP/s，峰值的 35% | 343 TFLOP/s，峰值的 35% |

两个运行对 GPU 的利用程度大致相同；DeepSeek-V3 便宜约 11 倍，因为每个词元激活的参数少 11 倍。它广为引用的 \$560 万成本，是最终运行的 GPU 小时按每小时 \$2 计的租用价值，而不是研究、数据和早期实验的成本。

## 8.9. 部署大模型

### 8.9.1. 预填充与解码

生成回复分为两个代价截然不同的阶段。在**预填充**阶段，整个**提示**在一次前向传播中处理：从 HBM 读取的每个权重被用于所有提示**词元**，所以**预填充**是计算受限的。在*解码*阶段，每个序列每步产生一个词元，每一步都要从 HBM 读取全部权重和该序列的 **KV 缓存**（[4.7.6](/4.7.6)）。BF16 权重（2 字节）对批中每个序列用于 2 次**浮点运算**，因此解码的算术强度约等于批量大小，远低于 H100 的 $\pi/\beta \approx 295$：解码是访存受限的。于是单个序列速度的一个上界是

$$
\text{每个序列每秒词元数} \le \frac{\text{HBM 带宽}}{\text{每个解码步读取的字节数}}.
$$

对 8 块 H100 上用张量并行的 BF16 Llama-3-70B（总带宽 26.8 TB/s），每步读取 141 GB 权重，单个序列最多约每秒 189 个词元；FP8 权重与 KV 缓存使它翻倍。256 个序列的批共享权重读取，但每个序列读取自己的 KV 缓存，这个模型为每词元 320 KiB，4K 词元上下文时总计 344 GB：该批每秒总共产生约 14,000 个词元，但每个用户只得到约 55 个。批处理提高吞吐量，而不是每个序列的速度。实测系统通常只能达到这些上界的一部分。

因此 KV 缓存是部署的核心资源，许多架构改动都以缩小它为目标：**分组查询注意力**（[4.7.6](/4.7.6)）、**多头潜在注意力**与线性注意力混合架构（[4.7.9](/4.7.9)），以及把缓存量化为 8 位或 4 位。大型服务还把这两个阶段分离到不同的 GPU 上（*解耦的*预填充与解码），因为它们需要不同的硬件配比。

### 8.9.2. 连续批处理

请求在随机的时间到达，产生的输出长度差别很大。如果先组成一个批并一直运行到其中所有序列结束，短请求就要等待最长的那个，GPU 也会在已完成的位置上空转。

**定义 8.9.1（连续批处理）** **连续批处理**（迭代级调度；Orca，Yu 等，OSDI 2022）以单个解码步为粒度调度部署批：每一步之后，已完成的序列离开批，等待的请求（在预填充之后）加入，使批始终保持满的状态。

### 8.9.3. PagedAttention

连续批处理使 KV 缓存的内存管理变得困难：每个序列的缓存每步增长一项，最终长度未知。早期系统为每个请求按最大长度预留一段连续区域，按 Kwon 等的测量，预留的 KV 内存中只有 20–40% 真正用于缓存条目。

**定义 8.9.2（PagedAttention）** **PagedAttention**（Kwon 等，SOSP 2023）把 KV 缓存存放在固定大小的块（例如 16 个词元）中，块按需从共享池分配，每个序列有一张块表，把逻辑词元位置映射到物理块，类似于操作系统虚拟内存中的页和页表；注意力核通过块表收集键和值。

碎片降到缓存的 4% 以下，因此内存中能放下更多序列，批可以更大；基于它构建的 vLLM 系统在相同延迟下取得了早期部署系统 2–4 倍的吞吐量。块也可以共享：具有共同前缀的序列（系统提示、长文档、同一提示的多个样本）指向相同的物理块，只在它们分叉时才复制。跨请求复用共同前缀的缓存，是**提示缓存**（[4.2.14](/4.2.14)）背后的机制。

### 8.9.4. 投机解码

由于一个解码步受限于读取权重，在一次前向传播中检查多个词元的代价与生成一个几乎相同。投机解码利用了这一点。

**定义 8.9.3（投机解码）** **投机解码**（Leviathan 等，ICML 2023；Chen 等，2023）用廉价的*草稿模型* $q$ 生成 $\gamma$ 个草稿词元，用目标模型 $p$ 在一次前向传播中对它们全部求值，并按顺序以概率 $\min\bigl(1, p(x)/q(x)\bigr)$ 接受每个草稿词元 $x$；在第一次拒绝时，从归一化的残差分布 $\bigl(p - q\bigr)_+ / \sum\bigl(p - q\bigr)_+$ 中采样一个替代词元并丢弃其余草稿，如果所有草稿都被接受，则再从 $p$ 中采样一个词元。

**定理 8.9.1** 投机解码输出的每个词元（给定其前面的词元）都恰好按目标模型 $p$ 分布。

**证明** 考虑一个位置，设草稿分布为 $q$、目标分布为 $p$，都是词表上的分布。词元 $x$ 被输出，要么是因为它被草拟并被接受，概率为 $q(x)\min\bigl(1, p(x)/q(x)\bigr) = \min\bigl(p(x), q(x)\bigr)$，要么是因为草稿被拒绝而 $x$ 是重新采样得到的。总拒绝概率为 $1 - \sum_y \min(p(y), q(y)) = \sum_y \bigl(p(y) - q(y)\bigr)_+$，这里用到 $p(y) = \min(p(y), q(y)) + (p(y) - q(y))_+$。因此

$$
\mathbb{P}(\text{emit } x) = \min\bigl(p(x), q(x)\bigr) + \sum_y \bigl(p(y) - q(y)\bigr)_+ \cdot \frac{\bigl(p(x) - q(x)\bigr)_+}{\sum_y \bigl(p(y) - q(y)\bigr)_+} = \min\bigl(p(x), q(x)\bigr) + \bigl(p(x) - q(x)\bigr)_+ = p(x). \qquad \square
$$

因此投机解码在不改变输出分布的前提下加快了生成。设接受率 $a = \sum_x \min(p(x), q(x))$，并假设各位置相互独立，则一次目标模型的前向传播平均产出 $(1 - a^{\gamma + 1})/(1 - a)$ 个词元。下面的模拟验证了定理和接受率：

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

草稿模型可以是同一系列的小模型，也可以是目标模型自身上的轻量额外头，由它的最后隐状态预测若干个未来词元（Medusa、EAGLE）。DeepSeek-V3 训练了一个多词元预测模块并把它复用为草稿器：其第二个词元的预测有 85–90% 被接受，使解码速度约为原来的 1.8 倍。实践中通常有 2–3 倍的加速，在批量较小时最大，因为那时解码的访存受限最严重。

## 小结

- 用混合精度 **Adam** 训练时，模型状态每个参数占 16 字节（BF16 权重与梯度、FP32 主权重与两个矩）；使用 FlashAttention 时，激活值每层每个序列约占 $34\,sh$ 字节，可以通过重计算用算力换内存（完全重计算多 33% 的**浮点运算**）。
- BF16 有 FP32 的范围和 7 位尾数；混合精度在 16 位下计算，但在 FP32 下累加和更新，因为小的更新在 16 位下会被舍入掉。FP16 需要损失缩放来防止下溢。FP8 与 4 位格式（MXFP4、NVFP4）依靠细粒度的分块缩放因子工作；前沿模型现在用 FP8 和 NVFP4 做预训练。
- 全规约等于规约散射加全收集；环形算法让每块 GPU 发送 $2(p-1)/p$ 倍的数据，这是最优的。从 HBM 到 NVLink 再到网络，带宽每级约降低十倍。
- 数据并行等价于大批量 **随机梯度下降**，每步通信一次；ZeRO 对优化器状态、梯度和参数分片（阶段 3 即 FSDP，通信量为 1.5 倍）；张量并行切分矩阵，必须留在服务器内；流水线并行切分层，要付出 $(p-1)/(m+p-1)$ 的气泡。实践：服务器内用 TP，用 PP 直到模型放得下，其余用 DP，再加上上下文并行与专家并行。
- 注意力是访存受限的；FlashAttention 用精确的在线 **softmax 函数** 在 SRAM 中分块计算，并在反向传播中重算分数，用线性而不是二次的内存，运行速度快数倍。
- 训练算力为 $C \approx 6ND$（混合专家用激活参数）；时间是 $C$ 除以 GPU 数、稠密峰值与 MFU（良好运行约 40%）。
- 解码是访存受限的：每个序列每秒的**词元**数受带宽除以每步读取字节数的限制。连续批处理、PagedAttention（分页的 **KV 缓存**，浪费不到 4%）和投机解码（精确，快 2–3 倍）是标准的部署技术。
