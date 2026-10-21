---
title: Linux 命令行
description: 在 Unix Shell 中工作：命令、参数与 PATH；文件系统导航、通配符与引号；标准流、重定向与由经典文本工具（grep、sed、awk、sort、cut、xargs、find）组成的管道线；用户、组与权限位；进程、信号与作业控制；环境变量与配置文件；用 ssh 和 tmux 远程工作；编写健壮的 Bash 脚本。
source_hash: 9843cbbcd20d
---

大多数生物信息学软件在 Linux 上开发，并通过命令行使用：比对器、变异检测工具和组装器都是命令行程序，运行它们的服务器和集群没有图形界面，工具之间的粘合剂则是一条命令管道线或一个 Shell 脚本。命令行也是前几章的操作系统概念直接可见的地方：每条命令都是由 `fork` 和 `exec` 创建的**进程**（[4.11.2](/4.11.2)），每次重定向都在重排**文件描述符**（[4.11.8](/4.11.8#sec-8.5.3)），权限则是**索引节点**的字段（[4.11.7](/4.11.7#sec-7.1.3)）。本章讲授 Bash，它是 **Linux 发行版**和集群上的默认 Shell；工具采用 Ubuntu 上的 GNU 版本（在 WSL 2 或服务器上）。macOS 自带 zsh 和 BSD 版本的工具，部分选项有所不同。示例在 Ubuntu 24.04 的 Bash 5.2 下运行；行首的 `$` 是提示符，不必输入。

## 10.1. Shell 与命令

### 10.1.1. 终端、Shell 与命令

“使用命令行”时有三个程序协同工作。**终端模拟器**（Windows Terminal、GNOME Terminal、VS Code 的终端面板）负责显示字符并发送按键；它通过伪终端设备与 Shell 相连。

**定义 10.1.1（Shell）** **Shell** 是读取命令（从终端交互输入或从脚本读取）并执行的程序：它展开命令行（变量、通配符、引号），设置重定向和管道，把程序作为子进程启动并等待其结束，并提供带变量、控制流和函数的编程语言。常见的 Shell 有 Bash（GNU 的 Bourne-again shell）、zsh、fish，以及最精简的 POSIX `sh`（在 Ubuntu 上是 `dash`）。

命令行由空格分隔的词组成：第一个词是命令，其余是它的参数。按惯例，选项以 `-`（短选项，可合并：`ls -l -a` 即 `ls -la`）或 `--`（长选项：`ls --all`）开头，单独的 `--` 表示选项结束，因此 `rm -- -file` 删除名为 `-file` 的文件。命令属于下列之一：

| 种类 | 例子 | 查找方式 |
|---|---|---|
| 别名（alias） | 把 `ll` 定义为 `ls -alF` | Shell 的别名表 |
| 函数 | 在脚本或 `~/.bashrc` 中定义 | Shell |
| 内建命令（builtin） | `cd`、`echo`、`export`、`source`、`type` | 内置于 Shell（`cd` 必须如此：子进程无法改变其父进程的目录） |
| 外部程序 | `/usr/bin/grep` | 在 `PATH` 的各目录中依次搜索 |

`type grep` 说明一个名字属于哪一种，`which -a python3` 列出 `PATH` 上所有匹配的程序，第一个匹配者优先；激活 conda 环境或加载模块（[4.11.11](/4.11.11#sec-11.2)）之所以会改变运行的 `python3`，原因正在于此。

### 10.1.2. 获取帮助

`man ls` 显示手册页（`/` 搜索，`n` 跳到下一个匹配，`q` 退出）；`man 2 open` 显示第 2 节中的**系统调用**而不是命令的手册页；`ls --help` 给出摘要；`help cd` 是内建命令的文档；`tldr ls`（若已安装）给出实用示例。Bash 的行编辑功能可以省去大量输入：Tab 补全命令和文件名，上箭头和 Ctrl-R 搜索历史，Ctrl-A 和 Ctrl-E 移到行首和行尾，Ctrl-C 中断正在运行的程序，Ctrl-D 结束输入（并退出 Shell）。

## 10.2. 文件与目录

### 10.2.1. 导航与操作

| 命令 | 作用 |
|---|---|
| `pwd` | 打印工作目录 |
| `cd dir`、`cd ..`、`cd ~` 或 `cd`、`cd -` | 切换目录：到 `dir`、上级目录、家目录、上一个目录 |
| `ls -lah` | 以长格式列出（`-l`），包括名称以 `.` 开头的隐藏文件（`-a`），并以易读的单位显示大小（`-h`） |
| `mkdir -p a/b/c` | 创建目录，同时创建缺失的上级目录 |
| `cp -r src dst`、`mv old new`、`rm file`、`rm -r dir` | 复制、移动或重命名、删除（永久删除：没有回收站） |
| `ln -s target name` | 创建**符号链接**（[4.11.7](/4.11.7#sec-7.1.4)） |
| `touch f` | 创建空文件或更新其修改时间 |
| `cat`、`less`、`head -n 20`、`tail -n 20`、`tail -f log` | 打印、分页浏览、显示开头或末尾、跟踪不断增长的文件 |
| `du -sh dir`、`df -h` | 目录的磁盘用量、**文件系统**的剩余空间 |
| `find dir -name '*.fq.gz' -size +1G` | 按名称、大小、时间、类型搜索目录树 |
| `tar -czf out.tar.gz dir`、`tar -xzf out.tar.gz` | 创建和解开压缩归档 |

### 10.2.2. 展开与引号

运行命令之前，Shell 按固定的顺序展开命令行：花括号（`{a,b}`、`{1..3}`）、波浪号（`~`）、参数与变量（`$HOME`）、命令替换（`$(date)`）、算术（`$((7 * 6))`）、分词，最后是路径名展开。

**定义 10.2.1（通配符）** **通配符**（模式）是包含 `*`（任意字符串，包括空串）、`?`（任意单个字符）或方括号表达式 `[...]`（集合中的一个字符，如 `[0-9]`）的词；Shell 把它替换为匹配的文件名按字典序排成的列表。通配符不是**正则表达式**：单独的 `*` 表示“任意内容”，在 Bash 的默认设置下，没有匹配项的通配符会原样传给命令。

引号用来控制展开。单引号保留每个字符的字面含义；双引号允许 `$` 展开和命令替换，但抑制分词和通配符展开；反斜杠为一个字符加引号。

```text
$ echo data/*.fa            # glob expanded by the shell
data/sample B.fa data/sampleA.fa
$ echo 'data/*.fa'          # single quotes: literal
data/*.fa
$ echo "$HOME" '$HOME'      # double quotes expand variables, single quotes do not
/home/zf-li23 $HOME
$ f="my file.txt"; touch "$f"
$ ls $f                     # unquoted: split into two words, "my" and "file.txt"
ls: cannot access 'my': No such file or directory
ls: cannot access 'file.txt': No such file or directory
$ ls "$f"
my file.txt
```

由最后一个例子得出的规则是：除非需要分词，否则变量一律写在双引号里（`"$f"`、`"$@"`）。带空格的文件名来自 Windows 和测序机构，会使忽略这条规则的脚本出错。

## 10.3. 流、重定向与管道线

### 10.3.1. 标准流与重定向

**定义 10.3.1（标准流）** 每个进程启动时都有三个已打开的文件描述符，即**标准流**：标准输入（描述符 0，`stdin`），程序从中读取输入；标准输出（描述符 1，`stdout`），程序向其写出结果；标准错误（描述符 2，`stderr`），程序向其写出诊断信息。在交互式 Shell 中，三者都指向终端。

读标准输入、写标准输出的程序可以任意组合，因为 Shell 能在启动它们之前把这些流接到文件或其他程序上。

**定义 10.3.2（重定向）** **重定向**是 Shell 把命令的标准流（或其他描述符）替换为文件的操作，在程序启动之前于子进程中完成。形式如下：

| 语法 | 含义 |
|---|---|
| `cmd > file` | 标准输出写入 `file`（先截断） |
| `cmd >> file` | 标准输出追加到 `file` |
| `cmd 2> err.log` | 标准错误写入 `err.log` |
| `cmd > out.log 2>&1` | 标准输出写入 `out.log`，然后让描述符 2 复制描述符 1：两者都进入 `out.log`（Bash 也接受 `&> out.log`） |
| `cmd < file` | 标准输入取自 `file` |
| `cmd << EOF` … `EOF` | *here document*：其后直到 `EOF` 的各行作为标准输入 |
| `cmd <<< "$var"` | *here string* |
| `cmd 2> /dev/null` | 丢弃错误信息（[4.11.8](/4.11.8#sec-8.1.4)） |

重定向按从左到右的顺序处理，每一个都是一次 `dup2`（[4.11.8](/4.11.8#sec-8.5.3)）。因此 `cmd > out.log 2>&1` 把两个流都送入文件，而 `cmd 2>&1 > out.log` 先让标准错误成为旧标准输出（终端）的副本，然后才把标准输出重定向到文件。结果留在标准输出、诊断信息留在标准错误，正是 `tool > result.txt` 既能得到干净的结果文件、错误又仍显示在屏幕上的原因。

### 10.3.2. 管道与管道线

**定义 10.3.3（管道与管道线）** **管道**是内核中带写端和读端的缓冲区，两端各是一个文件描述符；写入写端的字节按顺序从读端读出，缓冲区空时读者阻塞，缓冲区满时写者阻塞（Linux 上默认 64 KiB）。**管道线** `cmd1 | cmd2 | ... | cmdn` 通过管道把每条命令的标准输出连到下一条命令的标准输入；所有命令作为独立的进程并发运行，管道线的**退出状态**是最后一条命令的退出状态。

管道线是无需编程的并发：`cmd1` 还在产生后面的行时，`cmd2` 已在处理最前面的行；数据在内存中流动，不需要临时文件；在多核机器上各级并行运行。一条对 50 GB 的 FASTQ 文件解压、过滤并计数的管道线只需几千字节内存。读者提前退出（`head`）时，写者的下一次写入会因 `SIGPIPE` 失败并终止，所以 `zcat huge.fq.gz | head` 会立即返回。

### 10.3.3. 文本处理工具

Unix 工具把文本看作一系列行，行内常以制表符分成字段，这恰是大多数生物信息学格式（BED、GTF、VCF、SAM、计数表）的形态。核心工具如下：

| 工具 | 用途 | 例子 |
|---|---|---|
| `cat`、`zcat` | 连接文件；把 gzip 解压到标准输出 | `zcat reads.fq.gz \| head -4` |
| `head`、`tail` | 开头或末尾的若干行；`tail -n +2` 从第 2 行起（跳过表头） | `tail -n +2 table.tsv` |
| `wc` | 统计行、词、字节（`-l`、`-w`、`-c`） | `wc -l reads.fq` |
| `cut` | 选取字段（`-f`，默认以制表符分隔；`-d,` 以逗号分隔） | `cut -f1,3 genes.tsv` |
| `sort` | 对行排序；`-k2,2` 按第 2 个字段，`-n` 按数值，`-r` 逆序，`-u` 去重，`-t` 指定分隔符 | `sort -k1,1 -k2,2n regions.bed` |
| `uniq` | 合并相邻的相同行；`-c` 计数（先排序） | `sort \| uniq -c` |
| `tr` | 转换或删除字符 | `tr -d '\n'`、`tr a-z A-Z` |
| `paste`、`join` | 把文件并排合并，或按公共键合并 | `paste ids.txt values.txt` |
| `grep` | 打印匹配**正则表达式**的行；`-v` 反选，`-c` 计数，`-i` 忽略大小写，`-E` 扩展语法，`-F` 固定字符串，`-w` 整词，`-o` 只输出匹配部分 | `grep -c '^>' seqs.fa` |
| `sed` | 流编辑器；主要用于替换 `s/regex/replacement/flags` | `sed -E 's/^chr//'` |
| `awk` | 按字段处理的小型语言：对每一行执行 `pattern { action }`，字段为 `$1, $2, ...`，`NR` 为行号，`NF` 为字段数，支持关联数组 | 见下 |
| `find`、`xargs` | 查找文件；由标准输入构造命令行 | `find . -name '*.bam' -print0 \| xargs -0 -n1 samtools index` |

用一张小的基因表来说明这些工具：

```text
$ head -3 genes.tsv
gene_id	chrom	start	end	strand	biotype
ENSG01	chr1	11869	14409	+	lncRNA
ENSG02	chr1	14404	29570	-	pseudogene
```

按生物型统计基因数：跳过表头，取第 6 个字段，排序，对相邻重复计数，再按计数排序：

```text
$ tail -n +2 genes.tsv | cut -f6 | sort | uniq -c | sort -rn
      4 protein_coding
      3 lncRNA
      1 pseudogene
```

`awk` 一步完成过滤与计算。下面先给出蛋白质编码基因的长度（坐标从 1 起且包含两端，故有 $+1$），再用关联数组统计每条染色体上的基因数和总长度：

```text
$ awk -F'\t' 'NR > 1 && $6 == "protein_coding" { print $1, $2, $4 - $3 + 1 }' genes.tsv
ENSG03 chr1 6167
ENSG04 chr2 8057
ENSG06 chr3 10536
ENSG07 chrX 38854
$ awk -F'\t' 'NR > 1 { n[$2]++; bp[$2] += $4 - $3 + 1 }
>             END { for (c in n) print c, n[c], bp[c] }' genes.tsv | sort
chr1 3 23875
chr2 2 8990
chr3 1 10536
chrX 2 65889
```

对 FASTA 文件：统计记录数和碱基总数，找出含模糊碱基 `N` 的记录（`-B1` 在每个匹配前多打印一行上下文），并用捕获组改写标题行：

```text
$ grep -c '>' seqs.fa
3
$ grep -v '>' seqs.fa | tr -d '\n' | wc -c
34
$ grep -B1 N seqs.fa
>read3 sample=A
ACGTNNACGT
$ sed -E 's/^>(\S+) sample=(\S+)/>\2_\1/' seqs.fa | head -2
>A_read1
ACGTACGTTTGA
```

有两个陷阱值得了解。`sort` 默认遵循区域设置的排序规则，与字节序不同；要求输入已排序的工具（`join`、`comm`、许多基因组学工具）期望的是 `LC_ALL=C sort`，它也快得多。此外，这些工具不理解 CSV 文件中的引号（带引号字段内的逗号）；处理真正的 CSV 应使用能识别 CSV 的工具（`csvkit`、`mlr`、`xsv`/`qsv`）或 pandas（[4.4.5](/4.4.5)）。`samtools`、`bcftools`、`bedtools` 和 `seqkit` 等专用工具能正确而快速地处理基因组学格式；通用工具用于快速查看、简单的表格和粘合。

## 10.4. 用户、组与权限

Linux 是多用户系统。每个用户有一个数字用户 ID（UID），属于一个主组，还可能属于其他组（用 `id` 查看）；每个文件有所有者、组和模式。

**定义 10.4.1（权限位）** 文件的**权限位**是其索引节点中的九个二进制位，对*用户*（所有者）、组和*其他人*三类各占三位：读（`r`）、写（`w`）和执行（`x`）。对普通文件，它们分别允许读取其内容、修改它、以及把它作为程序运行。对目录，`r` 允许列出其中的名称，`w` 允许在其中创建、删除和重命名条目，`x`（*搜索*）允许按名称访问其中的条目，访问目录内的任何东西都需要它。内核检查适用于调用进程的第一类（是所有者就按所有者，否则是同组就按组，否则按其他人）。

`ls -l` 以十个字符显示类型和模式，其后是链接数、所有者、组、大小和修改时间：

```text
$ ls -l fasta_stats.sh
-rwxr-xr-x 1 zf-li23 zf-li23 840 Oct 21 15:47 fasta_stats.sh
$ ls -ld data
drwxr-xr-x 2 zf-li23 zf-li23 4096 Oct 21 15:47 data
```

第一个字符是类型（`-` 普通文件，`d` 目录，`l` 符号链接，`b`/`c` 设备）；`rwxr-xr-x` 表示所有者可读、写、执行，组和其他人可读和执行。八进制下每一类是一位数字，$r = 4$、$w = 2$、$x = 1$，所以 `rwxr-xr-x` 是 755，`rw-r-----` 是 640。

| 命令 | 作用 |
|---|---|
| `chmod 640 results.tsv` | 以八进制设置模式 |
| `chmod u+x script.sh`、`chmod -R g+rX project/` | 以符号方式增减权限位（`X`：仅对目录和已可执行的文件加执行位） |
| `chgrp lab project/`、`chown` | 更改组；更改所有者需要 root |
| `umask` | 新建文件的模式中要去掉的位；通常的 `0022` 下，新文件为 `644`，新目录为 `755`；`umask 007` 使新文件仅组内可见 |

三个特殊位补全了模式。可执行文件上的 *setuid* 使它以文件所有者的 UID 运行（属于 root 的 `passwd` 正是这样才能更新口令数据库）；目录上的 *setgid* 使新文件继承该目录的组，使共享的课题组目录能被全组使用；目录上的*粘滞位*（`/tmp` 的模式是 `1777`，显示为 `drwxrwxrwt`）使用户只能删除其中自己的文件。超级用户 `root`（UID 0）不受这些检查约束；普通用户用 `sudo` 以 root 身份运行单条命令，而服务器和集群一般不授予这一权限，所以那里的软件装在家目录、conda 环境或容器中（[4.11.9](/4.11.9)、[4.11.11](/4.11.11#sec-11.2)）。

在共享服务器上，默认设置很重要：模式为 755 的家目录会让所有用户读取其中的一切。用 `chmod 700 ~`，或至少用 `chmod 700 ~/.ssh` 保护私人数据和凭据，并通过组而不是模式 777 共享项目。

## 10.5. 进程与作业控制

Shell 是**进程**管理器。每条命令作为子进程运行，有自己的 **PID**，观察和控制进程的工具有：

| 命令 | 作用 |
|---|---|
| `ps aux`、`ps -ef` | 列出所有进程；`ps -u $USER` 只列出自己的 |
| `pgrep -a name`、`pidof` | 按名称查找进程 |
| `top`、`htop`、`btop` | 交互式显示每个进程的 CPU 和内存使用 |
| `kill PID`、`kill -9 PID`、`pkill name` | 发送 `SIGTERM`（请求进程终止）、`SIGKILL`（强制，无法捕获），或按名称发送某个**信号** |
| `time cmd`、`/usr/bin/time -v cmd` | 经过时间、用户时间和系统时间；加 `-v` 还显示最大常驻内存 |
| `nice -n 10 cmd`、`renice` | 以较低的调度优先级运行 |

每条命令返回一个**退出状态**（0 表示成功，1–255 表示失败，被信号 n 杀死时为 128 + n，故 `SIGKILL` 对应 137），Shell 把它存入 `$?` 并用于控制流：`cmd1 && cmd2` 仅当 `cmd1` 成功时才运行 `cmd2`，`cmd1 || cmd2` 仅当 `cmd1` 失败时才运行，`cmd1; cmd2` 则两者都运行。

**定义 10.5.1（作业控制）** **作业控制**是 Shell 在一个终端上运行多条管道线（即*作业*），并在*前台*（与终端的输入相连，至多一个）和*后台*之间移动它们的能力。`cmd &` 在后台启动作业；Ctrl-Z 停止前台作业（发送 `SIGTSTP`）；`jobs` 列出作业；`fg %n` 和 `bg %n` 在前台或后台恢复作业 `n`；Ctrl-C 向前台作业发送 `SIGINT`。

后台作业属于终端会话。终端关闭时（SSH 连接断开、笔记本电脑休眠），Shell 向其作业发送 `SIGHUP`，作业通常随之终止。因此长时间的计算必须脱离终端：用 `nohup cmd > log 2>&1 &` 运行（忽略 `SIGHUP`）、在 `tmux` 中运行（§10.7.2），或在集群上作为批处理作业运行（[4.11.11](/4.11.11#sec-11.3)）。

## 10.6. 环境与配置

**定义 10.6.1（环境变量）** **环境变量**是进程*环境*中的一个名称–值对（均为字符串）；环境是进程在 `exec` 时从父进程继承、并传给自己子进程的一个列表。Shell 区分普通 Shell 变量（`x=1`）与导出的变量（`export X=1`）；只有导出的变量才会传到子进程。

重要的变量有：

| 变量 | 含义 |
|---|---|
| `PATH` | 以冒号分隔的目录列表，按顺序在其中搜索命令 |
| `HOME`、`USER`、`PWD`、`SHELL` | 家目录、用户名、工作目录、登录 Shell |
| `LANG`、`LC_ALL` | 区域设置：语言、字符编码、排序规则 |
| `TMPDIR` | 程序创建临时文件的位置（在集群上设为本地暂存盘） |
| `OMP_NUM_THREADS` | OpenMP 程序和许多数值库使用的线程数（[4.11.11](/4.11.11#sec-11.4)） |
| `LD_LIBRARY_PATH` | 运行时搜索共享库的额外目录（[4.2.2](/4.2.2#sec-2.4.4)） |

`env` 打印环境，`echo "$PATH"` 打印一个变量，`VAR=value cmd` 只为一条命令设置变量（`LC_ALL=C sort`）。要加入自己的程序目录，写 `export PATH="$HOME/.local/bin:$PATH"`（放在前面使其优先）。Bash 启动时读取配置文件：*登录* Shell（SSH 会话）读取 `~/.bash_profile` 或 `~/.profile`，交互式非登录 Shell（新开的终端标签页）读取 `~/.bashrc`；通常的安排是把一切放在 `~/.bashrc` 中，并让 `~/.profile` 去 source 它。编辑之后，`source ~/.bashrc` 使改动在当前 Shell 中生效。`conda init` 等工具加到这些文件里的行，常是 `PATH` 上出现“错误的” `python3` 的原因。

## 10.7. 远程工作

### 10.7.1. SSH

**定义 10.7.1（SSH）** **SSH**（Secure Shell）是一种加密的网络协议，用于登录远程机器并在其上运行命令，也用于在加密且经过认证的通道上建立隧道、转发其他连接和复制文件。客户端是 `ssh`；服务端是 `sshd`，默认监听 TCP 端口 22。

`ssh alice@login.cluster.example.org` 在远程机器上打开一个 Shell；`ssh host cmd` 在那里运行单条命令。不用口令而用密钥对：私钥留在笔记本电脑上，公钥放在服务器的 `~/.ssh/authorized_keys` 中，服务器验证客户端持有私钥，而私钥本身从不被发送。

```bash
ssh-keygen -t ed25519 -C "alice@laptop"      # create ~/.ssh/id_ed25519 and id_ed25519.pub
ssh-copy-id alice@login.cluster.example.org  # append the public key to the server's authorized_keys
```

用口令短语保护私钥，并让 `ssh-agent` 在会话期间记住它。文件 `~/.ssh/config` 可以省去输入，也能处理只能经网关访问的集群：

```text
Host gateway
    HostName gateway.example.org
    User alice

Host cluster
    HostName login.cluster.example.org
    User alice
    ProxyJump gateway          # connect through the gateway
    ServerAliveInterval 60     # keep idle connections open
```

有了它，`ssh cluster`、`scp results.tsv cluster:project/` 和 `rsync -av data/ cluster:project/data/` 都可以按名称使用（[4.11.11](/4.11.11#sec-11.5)）。端口转发可以访问只在远程机器上监听的服务：`ssh -L 8888:localhost:8888 cluster` 使运行在集群 8888 端口的 Jupyter 服务器能在笔记本电脑的浏览器中通过 `localhost:8888` 访问。VS Code 的 Remote-SSH 扩展使用同样的配置在服务器上编辑和运行代码。

### 10.7.2. tmux

**定义 10.7.2（终端复用器）** **终端复用器**是在虚拟终端中运行 Shell 的程序，这些虚拟终端由一个独立于任何真实终端的服务进程管理；客户端可以连接（attach）这些会话，把它们分成窗口和窗格，也可以分离（detach）而不终止它们。常见的有 `tmux` 和 GNU `screen`。

典型用法是在远程服务器上运行长时间的作业：用 SSH 连接，启动 `tmux new -s assembly`，运行作业，按 Ctrl-B 再按 D 分离，然后退出登录。作业继续运行，因为它的终端属于 tmux 服务进程而不是 SSH 连接；之后 `ssh server` 再 `tmux attach -t assembly`（或用 `tmux ls` 列出会话）即可回到它。在 tmux 内，前缀键 Ctrl-B 后接 `c` 创建窗口，`n` 和 `p` 切换窗口，`%` 和 `"` 把窗口分成窗格，`[` 进入滚动模式。在集群上，tmux 只用在登录节点上做编辑和监控；计算要通过调度器提交到计算节点（[4.11.11](/4.11.11#sec-11.1)）。

## 10.8. Bash 脚本

### 10.8.1. 一个完整的脚本

脚本是由 Shell 命令组成的文件。下面这个脚本汇总 FASTA 文件，并展示了健壮脚本的各个要素：

```bash
#!/usr/bin/env bash
# Summarize FASTA files: number of sequences and total length per file.
set -euo pipefail

usage() {
    echo "usage: $(basename "$0") [-o OUT] FILE..." >&2
    exit 2
}

out=/dev/stdout
while getopts "o:h" opt; do
    case "$opt" in
        o) out=$OPTARG ;;
        *) usage ;;
    esac
done
shift $((OPTIND - 1))
[[ $# -ge 1 ]] || usage

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT          # clean up even if the script fails

printf 'file\tsequences\tbases\n' > "$tmp"
for f in "$@"; do
    if [[ ! -r $f ]]; then
        echo "warning: cannot read '$f', skipped" >&2
        continue
    fi
    n=$(grep -c '^>' "$f" || true)            # grep exits 1 when nothing matches
    bases=$(grep -v '^>' "$f" | tr -d '\n' | wc -c)
    printf '%s\t%d\t%d\n' "$(basename "$f")" "$n" "$bases" >> "$tmp"
done
cat "$tmp" > "$out"
```

```text
$ chmod +x fasta_stats.sh
$ ./fasta_stats.sh data/*.fa missing.fa
warning: cannot read 'missing.fa', skipped
file	sequences	bases
sample B.fa	1	2
sampleA.fa	2	9
$ ./fasta_stats.sh; echo "exit status: $?"
usage: fasta_stats.sh [-o OUT] FILE...
exit status: 2
```

逐行说明：

- 第一行的 *shebang* `#!` 告诉**内核**在 `exec` 时用哪个解释器运行该文件；`/usr/bin/env bash` 在 `PATH` 上查找 `bash`。设置了执行位（`chmod +x`）后，脚本可以作为 `./fasta_stats.sh` 运行；否则用 `bash fasta_stats.sh`。
- `set -euo pipefail` 是“严格模式”：`-e` 在第一条失败的命令（条件判断之外）处退出，`-u` 把未定义的变量当作错误（可以发现 `OUTDIR` 未设置时 `rm -rf "$OUTDIR/"` 这类笔误），`-o pipefail` 使管道线在任何一级失败时就算失败，而不只看最后一级。没有 `pipefail` 时，`false | true` 是成功的。允许失败的命令要明确标出，如上面的 `grep -c ... || true`。
- 函数（`usage`）像命令一样调用，其参数是 `$1`、`$2`、…。
- `getopts` 解析短选项；`"$@"` 展开为所有剩余参数，每个参数是独立的一个词，即使其中含有空格（文件 `sample B.fa` 就被正确处理）；`$#` 是参数个数。
- `[[ ... ]]` 是 Bash 的测试命令：`-r` 可读，`-f` 普通文件，`-d` 目录，`-z` 空字符串，`==` 模式匹配，`=~` 正则表达式匹配，`-lt`/`-gt` 数值比较。
- `$(...)` 是**命令替换**（command substitution）：它运行一条命令，并代入其标准输出。
- `mktemp` 创建唯一的临时文件，`trap ... EXIT` 无论脚本如何结束都会删除它；输出只在最后才写到最终位置，所以被中断的运行不会在最终文件名下留下写了一半的结果。
- 消息送往标准错误（`>&2`），数据送往标准输出，出错时返回非零退出状态，这样脚本可以与管道线和工作流管理器组合使用。

### 10.8.2. 变量、循环与数组

```bash
samples=(ctrl_1 ctrl_2 treat_1 treat_2)       # an indexed array
echo "${#samples[@]} samples, first: ${samples[0]}"

for s in "${samples[@]}"; do                   # quote to keep elements intact
    echo "aligning $s"
    # minimap2 -t 8 -a ref.fa "fastq/${s}.fq.gz" > "bam/${s}.sam"
done

for i in {1..22} X Y; do echo "chr$i"; done   # brace expansion

while IFS=$'\t' read -r id chrom start end _; do   # read a TSV line by line
    echo "$id is on $chrom"
done < <(tail -n +2 genes.tsv)

f=sample.sorted.bam
echo "${f%.bam}.bai"      # remove a suffix: sample.sorted.bai
echo "${f##*.}"           # extension: bam
echo "${OUTDIR:-results}" # default value if OUTDIR is unset or empty
```

Shell 算术只有整数（`$(( (a + b) / 2 ))`）；浮点运算要调用 `awk` 或 Python。Shell 是编排程序和文件的合适语言；一旦脚本需要数据结构、浮点运算或超过一页的逻辑，Python 是更好的选择；一旦需要对许多样本运行许多步骤、并且只重新执行有变化的部分，就该用工作流管理器了（[4.11.11](/4.11.11#sec-11.6)）。ShellCheck（`shellcheck script.sh`）能发现 Shell 脚本中大多数引号错误和其他常见缺陷，值得对每个脚本都运行一遍。

### 10.8.3. 并行运行多条命令

多核机器可以直接在 Shell 中并行处理相互独立的文件：

```bash
# Compress every FASTQ file, 8 at a time
find fastq -name '*.fq' -print0 | xargs -0 -P 8 -n 1 gzip

# The same with GNU parallel, which also collects output in order and logs jobs
parallel -j 8 --joblog jobs.log 'samtools sort -o {.}.sorted.bam {}' ::: bam/*.bam
```

`-print0` 和 `-0` 用空字节分隔名称，对含空格的名称是安全的。这是**易并行**计算的 Shell 形式（[4.4.7](/4.4.7)）；在集群上，同样的模式变成作业数组（[4.11.11](/4.11.11#sec-11.4)）。

## 小结

- Shell 读取命令行，展开它们（变量、命令替换、通配符），并把通过 `PATH` 找到的程序作为子进程运行。变量要加引号（`"$f"`、`"$@"`）；通配符不是正则表达式。
- 每个进程都有标准输入、标准输出和标准错误。重定向（`>`、`>>`、`2>`、`2>&1`、`<`）是子进程中的 `dup2` 调用，按从左到右的顺序处理；管道线并发运行其中的命令，命令之间由管道连接。
- 文本工具 `grep`、`sed`、`awk`、`cut`、`sort`、`uniq`、`tr`、`find` 和 `xargs` 处理按行和字段组织的数据；用 `LC_ALL=C sort` 得到字节序，对 SAM、VCF 和真正的 CSV 使用针对格式的工具。
- 权限位（用户、组、其他人的 `rwx`；八进制 755、640）控制访问，对目录有特殊含义；`umask` 设定默认值，setgid 目录和组支持共享。
- 退出状态驱动 `&&` 和 `||`；作业控制在前台和后台之间移动作业；作业会随终端一起终止，除非用 `nohup` 或 `tmux` 使之脱离。
- 环境变量被子进程继承；`PATH` 决定运行哪个程序；`~/.bashrc` 配置交互式 Shell。
- 使用 ed25519 密钥和 `~/.ssh/config`（含 `ProxyJump` 和端口转发）的 SSH 是进入服务器的途径；`tmux` 使会话在断线后依然保持。
- 健壮的 Bash 脚本使用 shebang、`set -euo pipefail`、引号、`trap` 清理、送往标准错误的消息和有意义的退出状态；ShellCheck 能发现常见错误。
