---
title: 服务器与集群计算
description: 为计算生物学使用共享 Linux 服务器和高性能计算集群：集群及其文件系统的构成，用模块、conda 和容器管理软件环境，用 Slurm 提交批处理作业（资源请求、作业数组、依赖、优先级与回填），多线程、多进程、MPI 和 GPU 作业，用 rsync 和校验和移动并验证数据，以及把这一切串起来的工作流管理器（Snakemake、Nextflow）。
source_hash: ffb1927cb8b9
---

笔记本电脑足以开发一项分析，却很少足以运行它：比对几十个 RNA-seq 样本的读段、对全基因组做变异检测、组装基因组或训练模型，需要比个人电脑多得多的核数、内存和存储，并持续数小时乃至数天。这类工作在共享的 Linux 机器上运行，即课题组服务器或大学的高性能计算（HPC）集群，用 [4.11.10](/4.11.10) 的工具远程访问。本章是本课程在实践上的终点。它运用**进程**与调度（[4.11.2](/4.11.2)、[4.11.3](/4.11.3)）、**线程**（[4.11.6](/4.11.6)）、**文件系统**与存储（[4.11.7](/4.11.7)、[4.11.8](/4.11.8)）以及**容器**（[4.11.9](/4.11.9)），说明集群如何组织、软件如何在其上提供、如何用 Slurm 描述和调度批处理作业、如何并行化工作、如何移动数据，以及工作流管理器如何把多步分析自动化。分区名称、限额和存储路径等细节因站点而异；每个集群都有自己的文档，应以该文档为准，而非这里的通用示例。

## 11.1. 集群的构成

### 11.1.1. 节点与网络

**定义 11.1.1（计算集群）** **计算集群**是由快速网络连接、作为一个系统管理的一组计算机，即其*节点*：用户登录*登录节点*，它由所有人共享，用于编辑、编译、提交和监控工作；计算在*计算节点*上运行，计算节点由*工作负载管理器*分配给作业；所有节点挂载相同的共享文件系统。

典型的集群有少数几个登录节点，数百到数千个计算节点（每个有两颗多核 CPU，共 64–256 个核，以及 256 GiB 到数 TiB 内存），数量较少的带 GPU 或超大内存的节点，以及存储服务器。节点之间由用于管理的以太网和供并行程序与存储使用的低延迟互连（InfiniBand，或支持 RDMA 的高速以太网）相连。登录节点是每个人都会用到的唯一共享资源：在其上运行重计算会拖慢整个用户群体，通常会被自动杀死。除轻量工作外，一切都应放进作业（§11.3）；需要交互时，请求一个计算节点上的交互式会话。

### 11.1.2. 存储

集群提供若干用途不同的**文件系统**，为每类数据选对位置是用好集群的一部分：

| 区域 | 典型文件系统 | 容量与策略 | 用于 |
|---|---|---|---|
| 家目录（`$HOME`） | NFS，有备份 | 配额小（几十 GB） | 脚本、配置、小型源代码 |
| 项目或课题组 | NFS 或并行文件系统，有时有备份 | 配额大（TB），由一个组共享 | 原始数据、最终结果、共享参考数据 |
| 暂存（scratch） | 并行文件系统（Lustre、IBM Storage Scale、BeeGFS） | 容量很大、速度快、无备份；若干周未使用的文件会被清除 | 正在运行的分析的中间文件 |
| 节点本地 | 计算节点上的 SSD（常为 `$TMPDIR`） | 数百 GB，作业结束时删除 | 有大量小块或随机访问的临时文件 |
| 归档 | 磁盘缓存后面的磁带 | 容量很大，取回很慢 | 原始数据的长期保存 |

并行文件系统把每个大文件条带化到许多存储服务器上，因此数百个节点读取同一份参考数据或写入不同的 BAM 文件时，可获得每秒数 GB 的聚合带宽。它针对大块顺序 I/O 优化，而不是元数据：每次 `open`、`stat` 和 `ls` 都要去访问少数几台元数据服务器（[4.11.7](/4.11.7#sec-7.2.4)）。创建数百万个小文件的流程，或每次启动 Python 都要读取数十万个文件的 conda 环境，会使元数据服务器过载，用户自己也会觉得慢。因此集群既限制文件的大小，也限制文件的数量（**索引节点**配额，用 `quota`、`lfs quota` 或站点提供的命令查看），并建议把小文件打包成归档，把软件环境放在容器中（一个 SIF 文件，[4.11.9](/4.11.9#sec-9.6)），把临时文件放在节点本地磁盘上。

## 11.2. 软件环境

用户无法在集群上做系统级的软件安装（没有 `sudo`，[4.11.10](/4.11.10#sec-10.4)），而不同项目需要同一工具的不同版本。有四种机制并存。

**定义 11.2.1（环境模块）** **环境模块**是由 Lmod 或 Environment Modules 等工具解释的脚本，它修改 Shell 的环境变量（`PATH`、`LD_LIBRARY_PATH`、`MANPATH` 等），使集中安装的某个软件包的特定版本可用；加载和卸载模块可以在不同版本之间无冲突地切换。

```bash
module avail                 # list modules that can be loaded now
module spider samtools       # search all modules, including those behind a compiler or MPI module
module load samtools/1.21    # make a version available
module list                  # show what is loaded
module purge                 # unload everything (start job scripts from a clean state)
```

HPC 中心用专为此设计的**包管理器** Spack 和 EasyBuild 构建模块树，它们针对选定的编译器和 MPI 库编译每个软件包。另外三种机制由用户自己掌控：

| 机制 | 优点 | 在集群上的缺点 |
|---|---|---|
| 模块 | 针对硬件构建（优化过的编译器、MPI、GPU 库），由管理员维护 | 只有管理员装了的软件；各集群的版本不同 |
| conda / mamba / pixi 环境（[4.4.1](/4.4.1#sec-1.4)） | Bioconda 几乎涵盖所有生物信息学工具；用户可自行安装；用**锁文件**可复现 | 数十万个小文件（放在项目空间而不是暂存空间，并留意索引节点配额） |
| 用 Apptainer 的容器（[4.11.9](/4.11.9#sec-9.6)） | 每个环境一个文件，在笔记本电脑和集群上完全一致，整个用户空间被固定 | MPI 和 GPU 需要小心地与宿主机匹配 |
| 在 `$HOME/.local` 中自行构建 | 完全可控 | 维护负担 |

常见的安排是：编译器、MPI 和 CUDA 用模块，生物信息学工具用 conda 环境或容器，再由工作流管理器为每一步自动创建环境或拉取镜像（§11.6）。

## 11.3. 用 Slurm 提交批处理作业

### 11.3.1. 作业与工作负载管理器

**定义 11.3.1（批处理作业）** **批处理作业**是提交给工作负载管理器的一个工作单元：一个脚本，加上资源请求（节点数、任务数、CPU 核数、内存、GPU、最长运行时间）。工作负载管理器把作业排队，在所请求的资源空闲且优先级允许时在计算节点上启动它，把它限制在这些资源内，并记录其计费数据。一个作业可以包含若干*作业步*，每个作业步是一组并行的*任务*（进程）。

**定义 11.3.2（工作负载管理器）** **工作负载管理器**（批处理系统、作业调度器）是把集群的计算节点分配给批处理作业的软件：它维护等待中的作业队列，按调度策略决定哪些作业何时何地启动，启动并监控它们，并强制执行其资源限制。

Slurm 是世界上大多数最大的超级计算机以及许多大学集群所用的工作负载管理器；其他的有 PBS Pro/OpenPBS、IBM Spectrum LSF 和 HTCondor（专门处理大量相互独立的作业）。在 Slurm 中，节点被分成分区（带各自限制的队列，如最长运行时间或 GPU 节点），*QOS*（服务质量）设置和*账户*决定限额与优先级。Slurm 作业由**控制组**限制（[4.11.9](/4.11.9#sec-9.4.3)）：它只能看到分配给它的核，超出所请求的内存就会被杀死。

### 11.3.2. 作业脚本

作业脚本是一个 **Shell** 脚本，其开头以 `#SBATCH` 开始的注释是 `sbatch` 的选项：

```bash
#!/bin/bash
#SBATCH --job-name=align_ctrl1
#SBATCH --partition=standard          # site-specific
#SBATCH --nodes=1
#SBATCH --ntasks=1                    # one process ...
#SBATCH --cpus-per-task=8             # ... with 8 cores for its threads
#SBATCH --mem=16G                     # memory per node
#SBATCH --time=02:00:00               # wall-time limit, HH:MM:SS
#SBATCH --output=logs/%x_%j.out       # %x = job name, %j = job ID
#SBATCH --error=logs/%x_%j.err

set -euo pipefail
module purge
module load minimap2/2.28 samtools/1.21

cd "$SLURM_SUBMIT_DIR"
echo "job $SLURM_JOB_ID on $(hostname) with $SLURM_CPUS_PER_TASK cores"

minimap2 -t "$SLURM_CPUS_PER_TASK" -a ref/genome.fa fastq/ctrl_1.fq.gz \
    | samtools sort -@ 2 -m 1G -o results/ctrl_1.sorted.bam
samtools index results/ctrl_1.sorted.bam
```

`logs` 目录必须在提交前已存在，因为 Slurm 不会创建它。基本命令如下：

| 命令 | 用途 |
|---|---|
| `sbatch job.sh` | 提交批处理脚本；打印作业 ID |
| `squeue --me` | 自己的等待中（`PD`）和运行中（`R`）的作业，以及作业等待的原因（`Priority`、`Resources`、某项限制） |
| `scancel 12345`、`scancel --me` | 取消作业 |
| `sinfo` | 分区及其节点的状态 |
| `srun --pty --cpus-per-task=4 --mem=8G --time=1:00:00 bash` | 计算节点上的交互式 Shell（`salloc` 先分配资源，再在其中运行命令） |
| `sacct -j 12345 --format=JobID,State,Elapsed,TotalCPU,MaxRSS,ReqMem` | 已结束作业的计费信息：状态、时间、峰值内存 |
| `seff 12345` | 效率摘要：已用与所请求的 CPU 时间和内存之比（许多集群安装的第三方贡献工具） |
| `scontrol show job 12345` | 作业的全部细节 |

### 11.3.3. 请求资源

所请求的资源既是限制也是成本：作业不能超出它，而且作业运行期间，所请求的资源无论是否用到都为它保留，并计入账户的公平共享。请求应当测量而不是猜测：运行一个样本，查看 `sacct` 或 `seff`，然后请求观测到的峰值内存加 20–50 % 的余量，以及观测到的时间再加余量。

| 请求 | 过小时的症状 | 过大时的代价 |
|---|---|---|
| `--time` | 作业被杀死，状态为 `TIMEOUT` | 调度器无法回填它（§11.3.5）；等待更久 |
| `--mem`、`--mem-per-cpu` | 作业被杀死，状态为 `OUT_OF_MEMORY`（控制组的 OOM killer，退出状态 137） | 等待有这么多空闲内存的节点；内存对别人闲置 |
| `--cpus-per-task` | 程序的线程共用更少的核，运行更慢 | 核闲置，`seff` 中效率低 |
| `--gres=gpu:1` 或 `--gpus=1` | 程序看不到 GPU | GPU 是最稀缺的资源；等待很久 |

程序只会用到被告知的核数：请求 8 个核而让 `minimap2` 用它默认的 3 个**线程**，就浪费了 5 个。要把 `$SLURM_CPUS_PER_TASK` 传给程序的线程选项，对使用 OpenMP 线程的程序，还要把 `OMP_NUM_THREADS`（以及 **BLAS** 库对应的变量）设为同一个数。

### 11.3.4. 作业数组与依赖

大多数生物信息学工作是把同样的步骤施加到许多样本上。

**定义 11.3.3（作业数组）** **作业数组**是从一个脚本一起提交的一组批处理作业，除了*数组下标*之外各作业完全相同；脚本从环境变量 `SLURM_ARRAY_TASK_ID` 读取下标来选择自己的输入。`--array=1-96%20` 创建 96 个数组任务，其中至多 20 个同时运行。

```bash
#!/bin/bash
#SBATCH --job-name=align
#SBATCH --array=1-96%20
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x_%A_%a.out    # %A = array job ID, %a = array index

set -euo pipefail
# line N of samples.txt holds the name of sample N
sample=$(sed -n "${SLURM_ARRAY_TASK_ID}p" samples.txt)
minimap2 -t "$SLURM_CPUS_PER_TASK" -a ref/genome.fa "fastq/${sample}.fq.gz" \
    | samtools sort -@ 2 -o "results/${sample}.sorted.bam"
```

相互依赖的步骤用依赖串联起来：`sbatch --dependency=afterok:12345 merge.sh` 仅在作业 12345（数组的所有任务）成功完成之后才启动 `merge.sh`；`afterany` 等待任何结果，`--parsable` 使 `sbatch` 只打印作业 ID，便于在脚本中使用（`jid=$(sbatch --parsable align.sh)`）。用这种方式串联多于几步，很快就难以管理，这正是工作流管理器要解决的问题（§11.6）。

### 11.3.5. Slurm 如何决定运行什么

调度器按优先级对等待中的作业排序，并在资源空闲时启动优先级最高的作业。Slurm 的*多因子*优先级是若干因子的加权和：作业在队列中的年龄、规模、分区和 QOS，以及最重要的*公平共享*。

**定义 11.3.4（公平共享调度）** **公平共享调度**为作业分配优先级，使每个账户（用户、组、项目）在长期上获得与其配额成比例的集群份额：账户的作业优先级随其近期用量相对于其份额而降低，其中过去的用量按指数衰减加权，半衰期通常为一到两周。

这是 CPU 调度（[4.11.3](/4.11.3)）中比例份额思想在周的时间尺度上对整台机器的应用：近期用了很多集群资源的组等待更久，一直闲置的组很快就能开始。严格按优先级顺序会在大的高优先级作业等待足够多的节点空闲时浪费资源，所以 Slurm 还会回填。

**定义 11.3.5（回填调度）** **回填调度**允许优先级较低的作业越过优先级顺序提前启动，条件是它能放进当前空闲的资源，并且按运行中和等待中作业的时间限制，它会在它所用资源为更高优先级作业预留的时刻之前结束；因此它从不推迟任何更高优先级作业的预期开始时间。

**例 11.3.1** 一个分区有 8 个核。作业 A 在 6 个核上运行到第 4 小时。按优先级顺序等待的是 B（8 个核，2 小时）、C（2 个核，3 小时）和 D（2 个核，6 小时）。B 在 A 结束的第 4 小时之前无法开始，所以它得到第 4–6 小时的预留。在此之前有两个核空闲。C 能放进去，并且按其时间限制会在第 3 小时结束，早于 B 的预留，所以回填调度器立即启动它；D 会在 B 于第 4 小时需要的核上运行到第 6 小时，因此必须等待。完成时间由 B 为 6、C 为 9、D 为 12 变为 C 为 3、B 为 6、D 为 12：C 提前六小时完成，没有任何作业被推迟。

![例 11.3.1 在 8 个核上的甘特图。上：作业严格按优先级顺序启动，前四小时有两个核闲置。下：使用回填时，作业 C 立即在空闲的核中启动，并在作业 B 于第 4 小时的预留（虚线）之前结束。](./plots/backfill-schedule.py)

回填取决于时间限制：调度器只知道所请求的 `--time`，而不知道真实的运行时间。因此准确的时间限制能让作业更早开始，而默认请求分区上限（几天）的作业几乎永远得不到回填。

## 11.4. 并行作业

作业可以用几种方式利用并行性，它们对应不同的资源请求：

| 种类 | 机制 | Slurm 请求 | 例子 |
|---|---|---|---|
| 多线程，单节点 | 共享内存的线程：pthreads、OpenMP、工具的 `-t`/`--threads` 选项 | `--ntasks=1 --cpus-per-task=N` | 比对器（BWA、minimap2、STAR）、`samtools sort -@` |
| 独立任务 | 互不通信的独立进程 | 作业数组，或一个作业运行若干进程 | 逐样本的步骤、参数扫描、bootstrap 重复 |
| 多进程，多节点 | 用 MPI 传递消息：不同节点上的进程通过互连通信 | `--ntasks=N`（以及 `--nodes`），用 `srun` 启动 | 分子动力学（GROMACS）、大型系统发育分析（RAxML-NG、IQ-TREE 的 MPI 版本）、气候模型 |
| GPU | 一个或多个 GPU 上的数千个 GPU 线程 | `--gpus=N` 或 `--gres=gpu:N`，加上喂数据所需的 CPU 核 | 深度学习、纳米孔数据的碱基识别、GPU 分子动力学、AlphaFold 类的结构预测 |

**定义 11.4.1（MPI）** **消息传递接口**（MPI）是为由许多进程组成的并行程序制定的标准化库接口，这些进程有各自独立的地址空间，通过发送和接收消息协作（点对点操作如发送和接收，集合操作如广播和归约）。实现有 Open MPI 和 MPICH；MPI 程序一次性启动为多个进程，在集群上用 `srun` 启动。

大多数生物信息学工具是单节点的多线程程序，大多数分析由许多独立任务组成；MPI 主要对模拟程序重要。前面几章引出两条经验法则。多线程工具不会无限扩展：按 **Amdahl 定律**（[4.4.7](/4.4.7#sec-7.4.4)），串行部分占 10 % 的工具无论用多少个核，加速都不会超过 10 倍，而且 I/O 或内存带宽常常使它更早受限，所以在请求 64 个核之前，先测量 4、8 和 16 个核时的加速比是值得的。此外，许多独立任务最好表示为作业数组，或交给工作流管理器，作为**易并行**问题（[4.4.7](/4.4.7)）处理：96 个各用 8 个核的作业通常比一个 768 个核的作业更早完成，因为它们可以填进调度的空隙，而且一次失败只影响一个样本。

## 11.5. 数据的移动与保护

测序数据以 TB 计，移动它们本身就是一项任务。在 1 Gbit/s 连接的满速下，1 TB 需要 $8 \times 10^{12}\,\mathrm{bit} / 10^{9}\,\mathrm{bit/s} = 8000\,\mathrm{s} \approx 2.2$ 小时；在互联网上实际能达到的 100 Mbit/s 下，约需一天。从小规模到大规模传输的工具如下：

| 工具 | 用途 |
|---|---|
| `scp file cluster:dir/` | 通过 SSH 复制少量文件 |
| `rsync -avP src/ cluster:dst/` | 通过 SSH 同步目录：只传输有差异的文件，可以续传被中断的传输 |
| `wget`、`curl -O`、`aria2c` | 从 Web 或 FTP 服务器下载（公共数据、参考基因组） |
| SRA Toolkit（`prefetch`、`fasterq-dump`）、ENA 下载 | 按登录号获取公共测序数据 |
| Globus | 机构数据传输节点之间受管理的、并行的、可重启的传输；TB 规模数据移动的标准做法 |

`rsync` 值得好好学习。`-a`（归档）保留**目录树**、时间和权限；`-v` 列出被传输的内容；`-P` 保留部分传输的文件并显示进度；`-n`（`--dry-run`）显示将要发生什么；`--delete` 删除目标中源里已不存在的文件（危险：务必先试运行）。源路径末尾的斜杠很重要：`rsync -a data/ dst/` 把 `data` 的内容复制到 `dst` 中，而 `rsync -a data dst/` 则创建 `dst/data`。rsync 默认用大小和修改时间判断文件是否有差异；`--checksum` 则比较内容。大规模传输应通过集群的数据传输节点而不是登录节点进行，并在 `tmux` 中运行，使连接断开时传输不被中断（[4.11.10](/4.11.10#sec-10.7.2)）。

传输只有经过验证才算完成。测序机构和公共档案库会公布其文件的校验和（MD5 或 SHA-256）：

```bash
md5sum *.fq.gz > checksums.md5        # on the source: record checksums
md5sum -c checksums.md5               # on the destination: verify, printing OK or FAILED per file
```

无法重新生成的原始数据最需要小心：保持只读（`chmod -R a-w raw/`），绝不就地修改（每项分析都读取它们并把结果写到别处），至少在集群暂存文件系统（会被清除且无备份）之外保留一份副本，并在项目结束时连同校验和与元数据归档到磁带或公共仓库。对文本格式要压缩（gzip，或更利于随机访问的 BGZF），并优先选用本领域的压缩二进制格式（用 BAM 或 CRAM 而不是 SAM）。

## 11.6. 工作流管理器

### 11.6.1. 为什么需要

测序实验的分析是一系列步骤（质量控制、修剪、比对、排序、计数、统计），每一步施加到每个样本上，步骤之间有依赖关系。Shell 脚本和 `sbatch --dependency` 链很难很好地表达这一点：失败之后要重新运行一切，参数改变后不知道哪些输出已经过期，还把集群的细节写死在里面。

**定义 11.6.1（工作流管理系统）** **工作流管理系统**执行一个描述为一组步骤的分析，这些步骤声明了各自的输入和输出。系统由这些声明导出任务的**有向无环图**，在输入就绪时运行每个任务，在图允许的地方并行，可以在本地机器、集群或云上运行；只重新运行输出缺失或已过期的任务；为每个任务提供其软件环境；并记录运行了什么。

这一思想就是 `make` 及其他**构建系统**（[4.2.2](/4.2.2#sec-2.6)）在数据分析上的应用，再加上集群执行、软件环境和溯源。生物信息学中有两个系统占主导：Snakemake，基于 Python 的语言，规则由文件名模式定义，图像 `make` 那样从所请求的输出向后推导；以及 Nextflow，数据流语言，进程由通道连接，数据沿其向前流动。其他的还有通用工作流语言（CWL）和 WDL，它们是大型联盟和云平台使用的标准描述。

### 11.6.2. Snakemake

Snakemake 工作流是由规则组成的 `Snakefile`：

```python
SAMPLES = ["ctrl_1", "ctrl_2", "treat_1", "treat_2"]


rule all:
    input:
        expand("results/{sample}.sorted.bam.bai", sample=SAMPLES),


rule align:
    input:
        ref="ref/genome.fa",
        reads="fastq/{sample}.fq.gz",
    output:
        "results/{sample}.sorted.bam",
    threads: 8
    resources:
        mem_mb=16000,
        runtime=120,                    # minutes
    conda:
        "envs/align.yaml"
    log:
        "logs/align/{sample}.log",
    shell:
        "(minimap2 -t {threads} -a {input.ref} {input.reads}"
        " | samtools sort -@ 2 -o {output}) 2> {log}"


rule index:
    input:
        "results/{sample}.sorted.bam",
    output:
        "results/{sample}.sorted.bam.bai",
    shell:
        "samtools index {input}"
```

Snakemake 从目标出发，即第一条规则 `all` 的输入：四个 `.bai` 文件。每个文件名与各规则的输出模式匹配；通配符 `{sample}` 取使模式匹配的值（`ctrl_1`、……），由此确定该规则的输入，再向后继续，直到遇到已存在的文件。得到的图有八个作业。若作业的输出缺失或比其输入更旧，它就会运行（默认情况下，规则的代码、参数或软件环境改变时也会运行）。典型的调用如下：

```bash
snakemake -n                                   # dry run: list the jobs that would run
snakemake --cores 8 --sdm conda                # run locally on 8 cores, creating conda envs per rule
snakemake --executor slurm --jobs 50 --sdm apptainer \
    --default-resources slurm_partition=standard    # submit each job to Slurm, at most 50 at a time
snakemake --dag | dot -Tsvg > dag.svg          # draw the graph
```

使用 Slurm 执行器插件（Snakemake 8 及以后），每个作业成为一个 Slurm 作业，其资源请求来自规则的 `threads` 和 `resources`；Snakemake 进程本身很轻，在登录节点的 `tmux` 中运行，或作为一个长时间运行的小作业运行。与站点相关的选项集中在一个*配置文件*（profile，一个 YAML 文件）中，使工作流本身保持可移植。

### 11.6.3. Nextflow

用 Nextflow 写同样的比对，采用自 Nextflow 26.04 起默认的严格语法：

```text
params.reads = "fastq/*.fq.gz"
params.ref   = "ref/genome.fa"

process ALIGN {
    tag "${sample}"
    cpus 8
    memory '16 GB'
    time '2h'
    conda 'bioconda::minimap2=2.28 bioconda::samtools=1.21'

    input:
    tuple val(sample), path(reads)
    path ref

    output:
    tuple val(sample), path("${sample}.sorted.bam")

    script:
    """
    minimap2 -t ${task.cpus} -a ${ref} ${reads} | samtools sort -o ${sample}.sorted.bam
    """
}

workflow {
    reads = channel.fromPath(params.reads).map { f -> tuple(f.simpleName, f) }
    ALIGN(reads, file(params.ref))
}
```

process 声明输入和输出；workflow 块用*通道*把各 process 连接起来，通道是值的队列（这里是样本名与文件的二元组），值沿通道向前流动。每个任务在自己的工作目录中运行，`-resume` 复用输入和脚本都未改变的任务的结果（以哈希为键的缓存）。执行平台在 `nextflow.config` 中选择，通常通过 profile：

```text
profiles {
    slurm {
        process.executor = 'slurm'
        process.queue    = 'standard'
    }
    apptainer {
        apptainer.enabled = true
    }
}
```

`nextflow run main.nf -profile slurm,apptainer -resume` 随后把每个任务作为容器内的 Slurm 作业提交。nf-core 社区维护着经过同行评审的、面向标准分析的 Nextflow 流程，例如 `nextflow run nf-core/rnaseq -profile apptainer --input samplesheet.csv --outdir results --genome GRCh38`，并为许多机构的集群提供配置 profile；对于标准分析，使用这样的流程通常比自己编写一个更好。

| | Snakemake | Nextflow |
|---|---|---|
| 语言 | 带规则语法的 Python | 基于 Groovy 的 DSL（自 26.04 起为严格语法） |
| 模型 | 规则按文件名模式匹配；图从目标向后推导 | process 由通道连接；数据向前流动 |
| 重新运行的判据 | 输出缺失或过期（修改时间、代码、参数、环境） | 输入和脚本的任务哈希（`-resume`） |
| 生态 | Snakemake workflow catalog、wrapper | nf-core 流程与模块 |
| 适合 | 以文件和 Python 思考的人；探索性的、定制的分析 | 标准化的大规模生产流程和云 |

## 11.7. 良好实践

- 先小后大，晚些扩展：在数据的一个子集（几千条读段、一条染色体）上，交互式地或用一个短作业测试每一步，然后用测得的资源请求扩大规模。
- 把代码、环境和数据分开：代码放在受版本控制的仓库（`git`）中，环境放在锁文件或镜像中，原始数据在项目空间中只读，中间文件在暂存空间，结果与产生它们的代码放在一起。
- 使每个结果都可以从头复现：工作流、固定的环境（conda 锁文件或容器摘要）、参考数据的版本和参数一起决定输出；把它们和工作流管理器的日志一并与结果一起记录。
- 尊重共享资源：不在登录节点上计算，不提交数千个微小的作业（用数组或带分组的工作流管理器），不在并行文件系统上创建数百万个小文件，资源请求要准确，并清理暂存空间。
- 预期故障：节点会故障，作业会达到时间限制，传输会被中断。先以临时名称写出输出、最后重命名的步骤（[4.11.7](/4.11.7#sec-7.4.5)）、只重新运行缺失部分的工作流管理器、校验和与备份，会把故障变成延迟而不是损失。

## 小结

- 集群由共享的登录节点、由工作负载管理器分配的计算节点、快速互连和若干文件系统组成：有备份的家目录和项目空间、快速但会被清除的并行暂存空间、节点本地磁盘和归档。并行文件系统擅长大块顺序 I/O，在大量小文件下表现很差。
- 软件来自环境模块（Lmod，由 Spack 或 EasyBuild 构建）、conda/pixi 环境和 Apptainer 容器。
- 批处理作业是带资源请求（`--cpus-per-task`、`--mem`、`--time`、`--gpus`）的脚本，用 `sbatch` 提交，用 `squeue` 和 `sacct` 监控，由控制组限制。作业数组处理许多样本；依赖把步骤串联起来。
- Slurm 按以公平共享为主的多因子优先级为作业排序，并在时间限制保证不推迟任何更高优先级作业时，把较低优先级的作业回填到空闲资源中；准确的时间限制能缩短等待。
- 节点内的线程、独立任务、跨节点的 MPI 和 GPU 需要不同的请求；Amdahl 定律限制多线程的加速，独立任务最适合用数组扩展。
- 用 `rsync` 和 Globus 移动数据，用校验和验证它们，把原始数据保持只读，并在暂存空间之外备份。
- 工作流管理器（Snakemake、Nextflow）由声明的输入和输出构建任务的有向无环图，在集群上并行运行它们，每步有各自的软件环境，并只重新运行有变化的部分；nf-core 提供标准流程。
