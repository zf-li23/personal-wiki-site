---
title: 虚拟化与容器
description: 在一个操作系统中运行另一个操作系统，以及在同一个内核中隔离应用程序：虚拟机与虚拟机监控器、Popek–Goldberg 条件、陷入并模拟、二进制翻译、半虚拟化与硬件支持、内存与 I/O 虚拟化、以 WSL 2 为例；由命名空间、控制组和分层文件系统构成的 Linux 容器；Docker、OCI 镜像与 Podman；面向集群的 Apptainer；以及如何为可复现的科学软件选择隔离机制。
source_hash: 72fca0dc05a0
---

前面几章介绍了**操作系统**如何为进程虚拟化 CPU 和内存，使每个进程都以为自己独占整台机器。本章把同一思想推到更高一层。*虚拟机*让整个操作系统以为自己独占硬件，因此 Linux 可以运行在 Windows 笔记本上，几十台服务器也可以运行在一台物理主机上；*容器*让一组进程以为自己独占操作系统，拥有自己的文件、进程树和网络，却共享同一个内核。两者都是计算生物学的日常工具：WSL 2 是一台虚拟机，生物信息学工具常以 Docker 镜像的形式发布，在集群上同一个镜像通过 Apptainer 运行。本章建立在**受限直接执行**和特权级别（[4.11.1](/4.11.1)、[4.11.2](/4.11.2)）、**地址转换**（[4.11.4](/4.11.4)）以及 [4.11.7](/4.11.7) 的**文件系统**之上；容器在服务器上的实际使用在 [4.11.11](/4.11.11) 继续。

## 9.1. 虚拟机

### 9.1.1. 定义

**定义 9.1.1（虚拟机与虚拟机监控器）** **虚拟机**（VM）是真实机器的一个高效、隔离的副本，未经修改的操作系统，即*客户机*（guest），可以在其上运行。它由**虚拟机监控器**（又称虚拟机管理程序，VMM）提供：这是一层控制真实硬件、并在各虚拟机之间复用硬件的软件。*类型 1*（裸机）虚拟机监控器直接运行在硬件上；*类型 2*（宿主）虚拟机监控器作为应用程序运行在*宿主*（host）操作系统上。

这个定义出自 Popek 和 Goldberg（1974），包含三项要求：*等价性*（程序在虚拟机上的行为与在真实机器上相同，时序和资源可用量除外）、*资源控制*（虚拟机监控器完全控制硬件；客户机不能访问未分配给它的资源）和*高效性*（绝大多数指令直接在 CPU 上运行，无需虚拟机监控器介入）。最后一项把虚拟化与模拟区分开：QEMU 可以通过解释每条指令在 x86 机器上模拟 ARM 处理器，但这要慢几十倍。

| | 类型 1 | 类型 2 |
|---|---|---|
| 运行在 | 硬件上 | 宿主操作系统上 |
| 例子 | Xen、VMware ESXi、Microsoft Hyper-V；KVM（把 Linux 本身变成虚拟机监控器的 Linux 内核模块） | VirtualBox、VMware Workstation、Parallels、不带 KVM 的 QEMU |
| 典型用途 | 服务器、云 | 桌面 |

实际中两者的界线是模糊的。启用 Hyper-V 后，Windows 自己作为特权客户机（"根分区"）运行在虚拟机监控器之上，WSL 2 则是它旁边的另一台客户机（§9.3）；使用 KVM 时，Linux 宿主既是普通的操作系统，又是类型 1 的虚拟机监控器。其动机与 1960 年代 IBM 为大型机发明虚拟机时相同：*整合*（许多轻负载服务器合并到一台机器上）、*隔离*（一台虚拟机的崩溃或被攻破不影响其他虚拟机）、封装（虚拟机是一组文件，可以复制、做快照，甚至在运行中迁移），以及运行需要另一种操作系统的软件。

### 9.1.2. CPU 何时可以被虚拟化？

高效运行客户机内核的自然办法还是受限直接执行：让客户机内核运行在**用户态**，普通指令直接执行，每条**特权指令**都陷入虚拟机监控器，由它模拟该指令对虚拟机状态的影响。这称为*陷入并模拟*（trap-and-emulate）。只有当每一条可能暴露或改变真实机器状态的指令都会陷入时，这种办法才行得通。

**定义 9.1.2（敏感指令与特权指令）** **特权指令**是在用户态执行时陷入、在内核态执行时正常运行的指令。**敏感指令**是读取或改变机器资源配置的指令（控制敏感，例如改变页表基址寄存器或中断允许标志），或者其行为取决于该配置的指令（行为敏感，例如读取当前特权级别）。

**定理 9.1.1（Popek–Goldberg 定理）** 对于具有用户态与内核态以及可重定位内存的常规计算机，如果敏感指令的集合是特权指令集合的子集，就可以构造出满足等价性、资源控制和高效性的虚拟机监控器。

经典的 x86 架构违反了这一条件：约有 17 条指令是敏感的却不是特权的。最著名的是 `popf`，它装载标志寄存器；在用户态下它不陷入，而是悄悄忽略中断允许位，因此客户机内核用 `popf` 关中断时，虚拟机监控器根本察觉不到。`sgdt` 及类似指令让用户代码能读出真实描述符表的位置。所以 x86 无法用陷入并模拟的办法虚拟化，围绕这一点发展出三种技术。

### 9.1.3. 二进制翻译、半虚拟化与硬件支持

二进制翻译（binary translation）（VMware，1999 年）：虚拟机监控器在客户机内核的代码运行之前逐块扫描它，把敏感指令替换成对虚拟机监控器的调用，并缓存翻译后的代码。客户机的用户级代码不含敏感指令，原样运行。这使 x86 虚拟化变得实用并走向商业化。

半虚拟化（paravirtualization）（Xen，2003 年）：修改客户机内核，使它知道自己运行在虚拟机监控器上。它不再执行敏感指令，而是通过*超调用*（hypercall，虚拟机监控器中类似**系统调用**的机制）直接调用虚拟机监控器，并在内存管理和 I/O 上与之协作。这避免了翻译的开销，但需要经过修改的客户机。半虚拟化如今主要保留在**设备驱动程序**（§9.2.4）中，以及客户机与 Hyper-V 或 KVM 在定时器和中断上协作的"增强"（enlightenment）中。

硬件辅助虚拟化（hardware-assisted virtualization）（Intel VT-x，2005 年；AMD-V，2006 年；ARM 和 RISC-V 上有类似扩展）：CPU 新增一种模式。在 x86 上，虚拟机监控器运行在 *VMX 根*模式，客户机运行在*非根*模式，二者各有自己的 0–3 环，因此客户机内核运行在非根模式的 0 环，正如它所期望的那样。内存中的一个控制结构（VMCS）规定哪些事件引起 *VM 退出*（VM exit），即把控制权转交给虚拟机监控器（特权指令、访问某些寄存器、外部中断、I/O）；处理完毕后，虚拟机监控器通过 *VM 进入*（VM entry）恢复客户机。这使架构在精神上满足了 Popek–Goldberg 条件，也是当前所有虚拟机监控器所依赖的。一次 VM 退出的开销约为一微秒，所以虚拟机监控器设计剩下的工作就是避免退出。

## 9.2. 内存与 I/O 的虚拟化

### 9.2.1. 两级地址转换

客户机内核管理**页表**，把客户机**虚拟地址**映射到它自以为的**物理地址**，即*客户机物理地址*。虚拟机监控器必须再加上从客户机物理地址到*宿主物理地址*（真实的内存位置）的第二层映射，因为是它在各虚拟机之间分配真实内存。

### 9.2.2. 影子页表

没有硬件支持时，虚拟机监控器为每个客户机页表维护一个影子页表（shadow page table），直接把客户机虚拟地址映射到宿主物理地址，并让真实的 **MMU** 指向影子页表。它对客户机的页表设置写保护，使客户机每次修改页表都会陷入，虚拟机监控器便可据此更新影子页表。这样地址转换以全速运行，但客户机中的每次页表更新、**上下文切换**和缺页都要付出退出的代价，使进程密集的工作负载（编译、大量短命进程）变慢。

### 9.2.3. 嵌套分页

嵌套分页（nested paging）（Intel 的扩展页表 EPT；AMD 的嵌套页表 NPT）让硬件执行两层转换。客户机可以自由控制自己的页表而无需退出；虚拟机监控器维护第二套从客户机物理地址到宿主物理地址的表；**快表**缺失时，页表遍历硬件会遍历两套表。

**例 9.2.1（二维页表遍历的开销）** 客户机和宿主都使用四级页表时，客户机的四个页表项中的每一个都由客户机物理地址定位，而该地址在被读取之前本身必须经过一次四级宿主遍历来转换。数据的最终客户机物理地址还需要再做一次宿主遍历。最坏情况下的内存访问次数是

$$
\underbrace{4 \cdot 4}_{\text{host walks for guest entries}} + \underbrace{4}_{\text{guest entries}} + \underbrace{4}_{\text{final host walk}} = 24 = (4+1)(4+1) - 1,
$$

而不虚拟化时只需 4 次。

快表缓存的是合成后的转换结果，所以这一开销只在快表缺失时才付出，宿主中的大页（2 MiB 或 1 GiB）还能缩短遍历。实践中，对大多数工作负载，嵌套分页比影子页表快得多，各处都把它作为默认方式。虚拟机监控器还可以*超额分配*（overcommit）内存，即承诺给客户机的内存多于实际拥有的：办法有通过客户机中的*气球驱动程序*（它在客户机内部分配内存，再把这些页交还给虚拟机监控器）回收页面、在虚拟机之间共享相同的页（Linux 中的 KSM），以及换出。

### 9.2.4. I/O 虚拟化

客户机的 I/O 可以用三种方式提供，性能依次提高：

| 方法 | 工作方式 | 性能 |
|---|---|---|
| 完全模拟 | 虚拟机监控器模拟一个真实的、广为人知的设备（IDE 磁盘、Intel e1000 网卡）；对其寄存器的每次访问都引起一次退出 | 慢，但任何客户机都有对应的驱动程序 |
| 半虚拟化设备 | 客户机使用面向理想化虚拟设备的驱动程序：KVM 和 QEMU 上的 *virtio*，Hyper-V 上的 VMBus 设备；请求通过共享内存队列（*virtqueue*）传递，退出很少 | 大多数用途下接近原生 |
| 设备直通 | 把物理设备，或支持 SR-IOV 的设备的一个虚拟功能，直接分配给客户机，由 IOMMU（[4.11.8](/4.11.8#sec-8.1.3)）把它的 **DMA** 限制在客户机内存之内 | 原生性能，但设备不易共享或迁移 |

[4.11.8](/4.11.8#sec-8.1.2) 中的 `/proc/interrupts` 输出从客户机内部显示了这一点：WSL 2 虚拟机的磁盘就是一个 virtio 设备。

## 9.3. 示例：WSL 2

Windows Subsystem for Linux 有两个截然不同的版本，分别说明了在另一种操作系统上运行 Linux 软件的两种途径。

| | WSL 1（2016） | WSL 2（2019） |
|---|---|---|
| 途径 | 翻译层：Linux **系统调用**由 Windows 内核驱动程序实现 | 运行真实 Linux 内核的轻量级虚拟机 |
| Linux 内核 | 无 | 微软基于上游长期支持分支构建的内核 |
| 系统调用兼容性 | 部分（没有 FUSE，`ptrace` 受限，没有内核模块，不支持 Docker） | 完整 |
| Linux 文件系统 | 以 NTFS 文件存储 | 虚拟磁盘文件（`ext4.vhdx`）中的 ext4 |
| 访问 Windows 文件 | 快 | 经 9P 文件服务器，大量小文件时很慢 |
| 内存 | 与 Windows 共享 | 虚拟机的内存，动态增长与回收 |

WSL 2 运行在 Hyper-V 虚拟机监控器之上的一个*工具虚拟机*（utility VM）里，它约一秒即可启动，由 Windows 透明地管理；所有已安装的发行版共享这台虚拟机及其内核，各自处在自己的一组命名空间中（§9.4），所以 `uname` 在所有发行版里报告同一个内核：

```text
$ uname -r
6.6.114.1-microsoft-standard-WSL2
```

这一设计带来若干后果。Linux 一侧有真实的内核，所以容器、systemd 服务、FUSE 和 GPU 计算（通过一个转发到 Windows 驱动程序的半虚拟化 GPU 设备 `/dev/dxg`）都能工作。Windows 一侧的文件通过 9P 协议访问，文件密集的工作应当留在 Linux 文件系统中（[4.11.7](/4.11.7#sec-7.5)）。虚拟机默认最多获得宿主一半的内存；大型的组装或比对任务可能需要更多，这在 `%UserProfile%\.wslconfig` 中设置（`[wsl2]`、`memory=`、`processors=`、`swap=`）。网络默认位于 NAT 之后，因此在 WSL 内运行的服务器可通过 `localhost` 转发从 Windows 访问；*镜像*（mirrored）网络模式则让 Linux 直接使用宿主的网络接口。

## 9.4. 容器

### 9.4.1. 基本思想

虚拟机是一种笨重的隔离单元：每台虚拟机启动自己的内核，预留内存，并运行自己的后台服务。通常需要的东西要轻得多：让一个程序带着自己的一套库和工具运行，与其他程序隔离，但不需要自己的内核。

**定义 9.4.1（容器）** **容器**是一组运行在宿主内核上的进程，由内核本身把它们与系统其余部分隔离开：它们有自己对文件系统、进程树、网络及其他资源的视图，以及对所能消耗资源的限制。在 Linux 上，容器由命名空间（负责视图）、控制组（负责限制）和通常由镜像的各层拼装而成的根文件系统构成。这种技术也称为*操作系统级虚拟化*（OS-level virtualization）。

容器中的进程就是普通的 Linux 进程；在宿主上用 `ps` 就能看到它。没有虚拟机监控器，也没有第二个内核，所以容器几毫秒就能启动，以原生速度运行，只消耗其进程用到的内存。代价是隔离较弱：所有容器共享一个内核，因此内核漏洞可能让进程逃逸，而且容器只能运行面向宿主内核的程序（Windows 或 macOS 上的 Linux 容器运行在一台 Linux 虚拟机里，Docker Desktop 借助 WSL 2 就是这样做的）。

### 9.4.2. 命名空间

**定义 9.4.2（Linux 命名空间）** **Linux 命名空间**包装一种全局系统资源，使命名空间内的进程看到它自己的、隔离的实例；对该资源的改动对命名空间的成员可见，对其他进程不可见。每个进程在每种类型中都属于一个命名空间，新的命名空间由系统调用 `clone`、`unshare` 和 `setns` 创建。

| 命名空间 | 隔离的对象 | 内部效果 |
|---|---|---|
| mount | 挂载点列表 | 独立的文件系统树；容器根文件系统的基础 |
| PID | 进程 ID | 第一个进程的 PID 为 1，只看得到本命名空间的进程 |
| network | 网络接口、路由表、端口、防火墙规则 | 独立的网络协议栈，通常通过一对虚拟以太网接口与宿主相连 |
| UTS | 主机名和域名 | 独立的主机名 |
| IPC | System V IPC 对象、POSIX 消息队列 | 独立的共享内存段和信号量 |
| user | 用户 ID 和组 ID、能力 | 进程在内部可以是 root（UID 0），而在外部只是普通用户 |
| cgroup | 对 cgroup 层次结构的视图 | 把自己的 cgroup 看作根 |
| time | 启动时间和单调时钟 | 独立的时钟偏移（对迁移容器有用） |

user 命名空间使*无根*（rootless）容器成为可能：非特权用户创建一个 user 命名空间，其中他的 UID 被映射为 0，在其中他就可以创建其他命名空间。`unshare` 命令可以在 shell 中完成这件事。下面由一个普通用户在新的 user、PID、UTS、network 和 mount 命名空间中启动一个 shell（带有全新的 `/proc`，使 `ps` 只看到新的 PID 命名空间）：

```bash
echo "host: $(hostname), pid $$, user $(id -un)"
unshare --user --map-root-user --pid --fork --mount-proc --uts --net sh -c '
  hostname sandbox
  echo "inside: $(hostname), pid $$, user $(id -un)"
  ps -o pid,user,cmd
  ip -brief link'
```

```text
host: LAPTOP-J59DFHQK, pid 27080, user zf-li23
inside: sandbox, pid 1, user root
    PID USER     CMD
      1 root     sh -c hostname sandbox; echo "inside: $(hostname), pid $$, user $(id -un)"; ps -o pid,user,cmd; ip -brief link
      5 root     ps -o pid,user,cmd
lo               DOWN           00:00:00:00:00:00 <LOOPBACK>
```

在内部，这个 shell 是 PID 1 和"root"，有自己的主机名，只看得到自己的进程，网络命名空间里只有一个未连接的回环接口。在外部，什么都没变：主机名不变，内部的"root"对宿主文件的权限恰好就是用户 `zf-li23` 的权限。容器运行时做的是同样的事，外加一个新的根文件系统和资源限制。进程所属的命名空间在 `/proc/<pid>/ns/` 中以链接的形式可见。

### 9.4.3. 控制组

**定义 9.4.3（控制组）** **控制组**（cgroup）是按层次结构组织的一组进程，内核通过*控制器*对其施加资源限制并进行统计：CPU 时间（`cpu`）、内存（`memory`）、块 I/O（`io`）、进程数（`pids`）、CPU 与内存节点的放置（`cpuset`）等。在 cgroup 第 2 版（统一层次结构，所有当前发行版的默认版本）中，每个进程恰好属于一个 cgroup，层次结构以文件系统的形式暴露在 `/sys/fs/cgroup`，限制通过写入 `memory.max`、`cpu.max` 之类的文件来设置。

下面是本机上可用的控制器，以及两个通过 `systemd-run` 做的实验；`systemd-run` 在一个新的 cgroup 中按给定的限制启动命令：

```text
$ cat /sys/fs/cgroup/cgroup.controllers
cpuset cpu io memory hugetlb pids rdma
```

```bash
# a Python process that allocates 10 MiB at a time, with a 100 MiB memory limit
systemd-run --user --scope -p MemoryMax=100M -p MemorySwapMax=0 python3 -c "
a = []
for i in range(1, 40):
    a.append(bytearray(10 * 1024 * 1024)); print(i * 10, 'MiB', flush=True)
" | tail -2
echo "exit status: ${PIPESTATUS[0]}"

# a busy loop for 3 s of wall time, limited to half a CPU
systemd-run --user --scope -p CPUQuota=50% sh -c '
  d=/sys/fs/cgroup$(cut -d: -f3 /proc/self/cgroup)
  cat $d/cpu.max
  timeout 3 sh -c "while :; do :; done"
  grep -E "usage_usec|throttled_usec" $d/cpu.stat'
```

```text
80 MiB
90 MiB
exit status: 137
50000 100000
usage_usec 1513501
throttled_usec 1715944
```

当该组的内存将超过 100 MiB 时，内核的 **OOM 杀手**用 `SIGKILL` 杀死该进程（退出状态 $128 + 9 = 137$），而不影响组外的任何东西。CPU 限制 `50000 100000` 表示每 100 ms 的周期内有 50 ms 的 CPU 时间；这个忙循环在 3 秒内得到 1.5 秒的 CPU，其余时间被限流。退出状态 137 和 "Killed" 正是超出内存申请量的集群作业所遇到的情形（[4.11.11](/4.11.11#sec-11.3)）：Slurm、systemd、Docker 和 Kubernetes 都用 cgroup 来强制执行各自的限制。

### 9.4.4. 镜像与分层文件系统

容器需要一个包含程序及其所有库的根文件系统。它来自镜像。

**定义 9.4.4（容器镜像）** **容器镜像**是根文件系统的只读、可移植的打包，组织为有序的*层*栈（每一层是一个 tar 归档，记录相对于其下各层新增、修改或删除的文件），并附带元数据：默认命令、环境变量、工作目录和目标体系结构。镜像由内容哈希（*摘要*，digest）标识，通过*镜像仓库*（registry）分发。

运行时，各层由联合文件系统合并，通常是 OverlayFS，它呈现由一叠只读的*下层*（lower）目录和一个可写的*上层*（upper）目录合并而成的视图。读取时找到文件最上面的版本；对来自下层的文件的第一次写入会把它复制到上层（**写时复制**）；删除则记录为特殊的"whiteout"文件。非特权用户可以在 user 和 mount 命名空间中试一试：

```bash
mkdir lower upper work merged
echo base > lower/a.txt
unshare --user --map-root-user --mount sh -c '
  mount -t overlay overlay -o lowerdir=lower,upperdir=upper,workdir=work merged
  echo changed > merged/a.txt
  echo new > merged/b.txt
  cat merged/a.txt; ls merged'
echo "lower:"; cat lower/a.txt
echo "upper:"; ls upper
```

```text
changed
a.txt
b.txt
lower:
base
upper:
a.txt
b.txt
```

下层目录原封未动；所有改动都进入了上层目录。由于各层是共享的，从同一镜像启动的一百个容器在磁盘和**页缓存**中只用它的文件的一份拷贝，与另一个镜像只有最上层不同的镜像，下载时也只需下载那一层。

还有两种机制使容器的隔离更完整。*能力*（capabilities）把 root 的权力拆分成约 40 项独立的特权（绑定低端口、更改文件属主、加载内核模块等等），容器的"root"大多没有这些特权。*seccomp* 过滤器限制进程究竟可以发起哪些系统调用，从而缩小暴露给攻击的内核攻击面。

## 9.5. Docker、OCI 与 Podman

Docker（2013 年）并没有发明上述任何内核特性（cgroup 和大部分命名空间在 2008 年已在 Linux 中，user 命名空间在 2013 年完成，更早的系统如 FreeBSD jail 和 Solaris zone 已有同样的思想）；它让这些特性变得好用：提供了构建镜像的简单文件格式、分享镜像的仓库以及运行镜像的命令行工具。它的格式成为开放容器倡议（OCI）的开放标准：*镜像规范*、*运行时规范*（如何从解包后的镜像运行容器；参考实现为 `runc`，`crun` 是更快的替代品）和*分发规范*（仓库协议）。任何 OCI 镜像都能在任何 OCI 工具下运行。

镜像由 `Dockerfile` 构建，其中每条指令产生一层：

```text
# Pin the base image; tags can be moved, so production builds pin the digest too
FROM mambaorg/micromamba:2.0.5

# Install tools from conda-forge and bioconda into the base environment
RUN micromamba install -y -n base -c conda-forge -c bioconda \
        samtools=1.21 minimap2=2.28 python=3.12 \
    && micromamba clean --all --yes

WORKDIR /data
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]
CMD ["samtools", "--version"]
```

```bash
docker build -t aligner:1.0 .          # build an image from the Dockerfile in .
docker run --rm aligner:1.0            # run its default command, remove the container afterwards
docker run --rm -v "$PWD":/data aligner:1.0 \
    minimap2 -a ref.fa reads.fq -o out.sam   # bind-mount the current directory at /data
docker images; docker ps -a            # list images and containers
```

通常根本不需要 Dockerfile：BioContainers 项目为每个 Bioconda 软件包自动构建镜像，并发布在 `quay.io/biocontainers/<tool>:<version>--<build>`。

Docker 的架构对共享机器有一个弱点。`docker` 命令与以 root 身份运行的守护进程 `dockerd` 通信，任何被允许使用它的用户都可以把宿主的根目录**挂载**进容器并修改它：属于 `docker` 组等同于拥有 root 权限。*Podman*（Red Hat）提供相同的命令行界面，但没有守护进程，并且默认以*无根*方式运行，利用 user 命名空间，使容器的权利不超过启动它的用户。Docker 也可以无根运行；而跨多台机器编排容器的 Kubernetes，通过 containerd 或 CRI-O 使用 OCI 运行时。

## 9.6. 集群上的 Apptainer

高性能计算集群不允许使用 Docker：用户不得获得 root 权限，作业由批处理调度器而不是守护进程启动，集群的文件系统和高速网络在容器内也必须保持可访问。*Apptainer*（原名 Singularity；2021 年该项目加入 Linux 基金会时更名，Sylabs 的分支继续以 SingularityCE 的名字发展）正是为这一场景设计的：

- 容器以启动它的用户的身份和权限运行，没有守护进程；
- 默认与宿主集成而不是与之隔离：主目录、当前目录和 `/tmp` 被绑定挂载，使用宿主的网络，其他路径用 `--bind` 添加；需要时 `--containall` 提供更强的隔离；
- 镜像是*Singularity 镜像格式*（SIF）的单个文件，即压缩的只读 SquashFS 文件系统，便于复制、随项目归档并放到并行文件系统上，许多节点上的许多进程可以同时读取它；
- 它直接运行 OCI 镜像（将其转换为 SIF），GPU 支持只需一个选项（NVIDIA 用 `--nv`，AMD 用 `--rocm`）。

```bash
apptainer pull samtools.sif docker://quay.io/biocontainers/samtools:<version>--<build>
apptainer exec samtools.sif samtools view -c sample.bam     # run one command in the image
apptainer shell samtools.sif                                # interactive shell inside
apptainer exec --nv pytorch.sif python train.py             # with the host's NVIDIA GPUs
apptainer exec --bind /scratch/$USER:/work tools.sif ls /work
```

镜像也可以由定义文件构建，它的作用相当于 Dockerfile：

```text
Bootstrap: docker
From: mambaorg/micromamba:2.0.5

%post
    micromamba install -y -n base -c conda-forge -c bioconda samtools=1.21
    micromamba clean --all --yes

%environment
    export PATH=/opt/conda/bin:$PATH

%runscript
    exec samtools "$@"
```

`apptainer build tools.sif tools.def` 构建该镜像；在配置为允许非特权 user 命名空间的系统上无需 root（`--fakeroot`）。Snakemake 和 Nextflow 之类的工作流管理器可以为流水线的每一步自动拉取并使用这样的镜像（[4.11.11](/4.11.11#sec-11.6)）。

## 9.7. 选择隔离机制

| | 虚拟机 | 容器（Docker、Podman） | Apptainer | Conda/pixi 环境（[4.4.1](/4.4.1)） |
|---|---|---|---|---|
| 隔离的对象 | 整个操作系统，包括内核 | 文件系统、进程、网络、资源 | 文件系统（主要） | 只隔离库和工具，靠 `PATH` 和前缀 |
| 内核 | 自有 | 宿主的 | 宿主的 | 宿主的 |
| 启动时间 | 秒 | 毫秒 | 毫秒 | 即时 |
| 开销 | 客户机操作系统占用的内存；CPU 开销小 | 几乎没有 | 几乎没有 | 没有 |
| 运行是否需要 root | 虚拟机监控器需要 | 守护进程或 user 命名空间 | 不需要 | 不需要 |
| 可复现性 | 整个系统可以归档 | 镜像摘要固定每个文件 | SIF 文件固定每个文件 | 锁文件固定软件包版本，但操作系统和系统库会变 |
| 典型用途 | 另一种操作系统（WSL 2）、强多租户隔离、云 | 服务、开发、分发工具 | 集群 | 日常开发 |

对于计算工作，各个层次可以组合。带有**锁文件**的 conda 或 pixi 环境是固定项目中工具版本的最轻量的办法；镜像固定整个用户空间软件栈，包括 C 库和系统软件包，并且是流水线或论文补充材料可以按摘要引用的单位。两者都不固定内核或硬件，依赖 CPU 浮点行为或 GPU 库的结果在不同机器上仍可能不同（[3.5](/3.5)）；连这一点也要紧时，就需要使用虚拟机或同一个集群。

## 小结

- 虚拟机监控器在满足等价性、资源控制和高效性的虚拟机上运行客户机操作系统。当每条敏感指令都是特权指令时，陷入并模拟就行得通（Popek–Goldberg）；在 VT-x 和 AMD-V 为客户机增加带 VM 退出的独立模式之前，x86 需要二进制翻译或半虚拟化。
- 内存虚拟化增加了从客户机物理地址到宿主物理地址的第二层转换：软件的影子页表或硬件的嵌套分页（EPT/NPT），四级页表下后者最坏情况的遍历需要 24 次内存访问。I/O 可以是模拟的、半虚拟化的（virtio），或通过 IOMMU 直通。
- WSL 2 是运行真实 Linux 内核的轻量级 Hyper-V 虚拟机，ext4 位于虚拟磁盘中，Windows 文件通过 9P 访问。
- 容器是一组由命名空间（mount、PID、network、UTS、IPC、user、cgroup、time）隔离、由 cgroup 限制（`/sys/fs/cgroup` 处的 cgroup v2）的普通进程，运行在由 OverlayFS 根据镜像各层拼装而成的根文件系统上；能力和 seccomp 进一步缩小它能做的事。
- Docker 使容器变得实用；OCI 把镜像、运行时和仓库标准化；Podman 无需守护进程、以无根方式运行容器。在集群上，Apptainer 以用户自己的身份把 OCI 镜像作为单个 SIF 文件运行。
- 环境固定软件包版本，镜像固定整个用户空间，虚拟机固定操作系统；可复现的分析按摘要固定镜像。
