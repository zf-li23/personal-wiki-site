---
title: 数据通路与单周期处理器
description: 指令的五个执行阶段与三种实现方式；数据通路的组合部件与状态部件（PC、寄存器堆、存储器）和时钟方法；为 add、sub、addi、lw、sw、分支、jal、jalr、lui、auipc 逐步构建 RV32I 的数据通路；立即数生成器；控制信号及其真值表、控制器的 SystemVerilog 实现；关键路径、时钟周期与单周期处理器的性能。
---

前几章分别给出了 **RISC-V** 的**指令格式**和运算器。本章把它们组合成一个能执行指令的处理器：先确定执行一条指令需要哪些部件、数据在部件之间怎样流动（数据通路），再设计根据指令产生各部件控制信号的控制器。最简单的组织方式是让每条指令在一个**时钟周期**内完成，称为单周期处理器。它的结构和时序都很简单，是理解后续章节中多周期处理器与流水线的基础；它的缺点（时钟周期由最慢的指令决定）也正是那些改进的出发点。本章以 RV32I 中覆盖全部六种指令格式的一组指令为例：`add`、`sub`、`addi`、`lw`、`sw`、`beq`（及其他分支）、`jal`、`jalr`、`lui`、`auipc`，其他指令的实现原理与之相同。

## 6.1. 指令的执行过程

存储程序计算机在运行前把程序和数据存入存储器。执行程序时，处理器从程序的首地址开始，逐条取出指令、分析指令、按指令的要求完成操作，同时形成下一条指令的地址，并自动地连续执行下去，直到程序结束；整个过程由硬件自己完成。这是**冯·诺依曼结构**的核心。

一条指令的执行通常分为五个阶段，划分方式由指令的功能和硬件结构共同决定：

| 阶段 | 名称 | 工作 |
|---|---|---|
| IF | 取指令（instruction fetch） | 以 **PC** 为地址从存储器读出指令，并计算 PC $+ 4$ |
| ID | 译码（instruction decode） | 分析指令，读**寄存器堆**得到源操作数，生成立即数 |
| EX | 执行（execute） | **ALU** 完成运算，或计算访存地址、分支目标 |
| MEM | 访存（memory access） | 读或写数据存储器 |
| WB | 写回（write back） | 把 ALU 的结果或从存储器读出的数据写入目的**寄存器** |

并非每条指令都需要全部五个阶段：`add` 不访存，`sw` 和分支指令不写回。一条指令从取出到执行完毕的时间称为**指令周期**，处理器的时钟周期称为 CPU 周期。按怎样安排这几个阶段，处理器有三种基本的实现方式：

- 单周期：每条指令都用一个时钟周期完成全部阶段，前一条指令结束后才开始下一条；
- 多周期：每个阶段占一个时钟周期，不同指令使用不等的周期数，控制信号随执行步骤变化；
- 流水线：每个阶段占一个时钟周期，但相邻指令的执行在时间上重叠，每结束一个阶段就启动下一条指令的这个阶段，理想情况下每个时钟周期完成一条指令。当前的处理器普遍使用流水线。

后两种在后续章节中讨论。

## 6.2. 数据通路的组成

**定义 6.2.1（数据通路与控制单元）** 处理器中存储、传送和加工数据的部件及其连接（寄存器、存储器、ALU、加法器、多路选择器以及它们之间的连线）称为**数据通路**（datapath）；根据当前指令产生数据通路中各部件所需控制信号的部件称为**控制单元**（control unit），也称控制器。

这对应于**冯·诺依曼结构**中运算器与控制器的分工：数据通路负责数据的移动和运算，控制器指挥数据怎样移动和运算。数据通路的部件分为两类。

组合部件的输出只取决于当前的输入：

- 加法器：计算 PC $+ 4$；
- **多路选择器**：在几个数据来源中选择一个，选择信号来自控制器；
- ALU：上一章的 32 位 ALU，运算由 ALUSel 选择；
- 立即数生成器（§6.3.8）与分支比较器（§6.3.5）。

状态部件（时序部件）保存数据，在时钟边沿更新：

- **程序计数器** PC：一个 32 位寄存器，由 32 个 **D 触发器**组成，每个时钟上升沿写入下一条指令的地址；
- 寄存器堆：32 个 32 位寄存器，有两个读端口和一个写端口。读端口是组合的：给出地址 AddrA、AddrB，经过一段延迟后在 DataA、DataB 上得到寄存器的值；写端口在时钟上升沿、且写使能 RegWEn 为 $1$ 时把 DataD 写入 AddrD 指定的寄存器。`x0` 恒为 $0$，对它的写入被忽略。一个时钟周期内可以完成两次读和一次写；
- 指令存储器 IMEM 与数据存储器 DMEM：在单周期的理想化模型中，读是组合的（给出地址即得到数据），写在时钟边沿、且写使能为 $1$ 时发生。

一条指令在一个周期内既要取指令又可能要读写数据，而每个部件在一个周期内只能使用一次，因此单周期处理器必须把指令存储器和数据存储器分开，同理也需要单独的加法器计算 PC $+ 4$，不能与 ALU 共用。

时钟方法采用**边沿触发**：所有状态部件在同一个时钟上升沿更新；两个边沿之间，状态部件的输出经组合逻辑传播，在下一个边沿到来前稳定在状态部件的输入端。于是一个状态部件可以在同一个周期内先被读、后被写（例如 `addi x5, x5, 1` 读出旧的 `x5`，在周期末写入新值），不会产生**竞争**。

用 **SystemVerilog** 描述的寄存器堆如下，读是组合逻辑，写在时钟上升沿：

```systemverilog
module regfile (
  input  logic        clk, we,
  input  logic [4:0]  addr_a, addr_b, addr_d,
  input  logic [31:0] data_d,
  output logic [31:0] data_a, data_b
);
  logic [31:0] regs [31:1];          // x0 is not stored: it always reads as zero

  always_ff @(posedge clk)
    if (we && addr_d != 5'd0) regs[addr_d] <= data_d;

  assign data_a = (addr_a == 5'd0) ? 32'd0 : regs[addr_a];
  assign data_b = (addr_b == 5'd0) ? 32'd0 : regs[addr_b];
endmodule
```

## 6.3. 逐条指令构建数据通路

构建数据通路的方法是：从一个最简单的指令出发，每次加入一类新指令，检查现有的通路能否完成它的功能，不能就增加部件或多路选择器。

### 6.3.1. R 型指令

`add rd, rs1, rs2` 完成 $R[\mathrm{rd}] \gets R[\mathrm{rs1}] + R[\mathrm{rs2}]$，`sub` 完成减法；执行后 PC $\gets$ PC $+ 4$。需要的通路是：

1. 取指令：PC 送 IMEM 的地址，读出 32 位指令 inst；PC 同时送加法器得到 PC $+ 4$，在周期末写回 PC；
2. 读寄存器：inst[19:15]（rs1）、inst[24:20]（rs2）分别送寄存器堆的 AddrA、AddrB；
3. 运算：DataA、DataB 送 ALU，控制器按 funct7 与 funct3 给出 ALUSel（`add` 为 ADD，`sub` 为 SUB）；
4. 写回：ALU 的结果送 DataD，inst[11:7]（rd）送 AddrD，RegWEn $= 1$。

RISC-V 的各种格式中 rs1、rs2、rd 总在相同的位置，因此寄存器堆的地址可以直接从指令的固定位段连线，在控制器译码完成之前就开始读寄存器。读出的值如果用不到（例如 I 型指令的 rs2 位置其实是立即数），丢弃即可。这是 RISC-V 指令格式设计中为缩短关键路径所做的考虑。

### 6.3.2. I 型算术指令

`addi rd, rs1, imm` 完成 $R[\mathrm{rd}] \gets R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{imm})$。ALU 的第二个操作数要能来自立即数，于是增加：

- 立即数生成器 ImmGen：从 inst[31:20] 取出 12 位立即数并**符号扩展**到 32 位；
- ALU 的 B 输入前加一个多路选择器，BSel $= 0$ 选 rs2，BSel $= 1$ 选立即数。

### 6.3.3. 取数指令

`lw rd, imm(rs1)` 完成 $\mathrm{Addr} = R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{imm})$、$R[\mathrm{rd}] \gets \mathrm{MEM}[\mathrm{Addr}]$。地址计算与 `addi` 完全相同（立即数也是 I 型），新增的是：

- 数据存储器 DMEM：ALU 的结果送其地址端 Addr，读出的数据为 DataR；
- 写回前加一个多路选择器 WBSel，选择写入寄存器的是 ALU 的结果还是 DataR。

`lb`、`lh`、`lbu`、`lhu` 还需要在 DataR 之后按地址的低两位选出相应的字节或半字，并按 funct3 做符号扩展或零扩展。

### 6.3.4. 存数指令

`sw rs2, imm(rs1)` 完成 $\mathrm{MEM}[R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{imm})] \gets R[\mathrm{rs2}]$。新增的是：

- DMEM 的写数据端 DataW 接寄存器堆的 DataB（rs2 的值），写使能由 MemRW 控制；
- S 型指令的立即数分成 inst[31:25] 与 inst[11:7] 两段，立即数生成器要能按格式拼接，因此它的输入扩大为 inst[31:7]，并增加格式选择信号 ImmSel；
- 存数指令不写寄存器，RegWEn $= 0$。

`sb`、`sh` 需要存储器支持按字节写使能，只改写一个字中的部分字节。

### 6.3.5. 分支指令

`beq rs1, rs2, offset` 完成：若 $R[\mathrm{rs1}] = R[\mathrm{rs2}]$，则 PC $\gets$ PC $+ \mathrm{SignExt}(\mathrm{offset})$，否则 PC $\gets$ PC $+ 4$。它同时需要比较两个寄存器和计算分支目标，而 ALU 只有一个，所以增加：

- 分支比较器 Branch Comp：输入 DataA、DataB，输出 BrEq（相等）与 BrLt（小于），由控制信号 BrUn 选择按无符号（`bltu`、`bgeu`）还是有符号（`blt`、`bge`）比较；
- ALU 的 A 输入前加一个多路选择器 ASel，ASel $= 1$ 时选 PC，于是 ALU 计算 PC $+$ 立即数作为分支目标；
- PC 的输入前加一个多路选择器 PCSel，在 PC $+ 4$ 与 ALU 的结果之间选择。控制器根据 BrEq、BrLt 和 funct3 决定 PCSel。

B 型立即数编码的是以 $2$ 字节为单位的偏移，立即数生成器在最低位补 $0$，因此分支范围是 $\pm 4\ \mathrm{KiB}$。

### 6.3.6. 跳转指令

`jal rd, offset` 完成 $R[\mathrm{rd}] \gets$ PC $+ 4$、PC $\gets$ PC $+ \mathrm{SignExt}(\mathrm{offset})$。跳转目标由 ALU 计算（ASel 选 PC，BSel 选 J 型立即数），PCSel 选 ALU；而写回寄存器的是 PC $+ 4$，现有通路中没有这条路径。可以改造 ALU，但更简单的办法是把 PC $+ 4$ 引到写回多路选择器，WBSel 扩展为三选一：$0$ 选 DMEM、$1$ 选 ALU、$2$ 选 PC $+ 4$。

`jalr rd, offset(rs1)` 是 I 型指令，完成 $R[\mathrm{rd}] \gets$ PC $+ 4$、PC $\gets (R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{offset}))\ \&\ {\sim}1$。它与 `jal` 的区别只是 ALU 的 A 输入取 rs1（ASel $= 0$）、立即数取 I 型，现有通路已经足够；规范要求把目标地址的最低位清零，只需在 PC 的输入端把 ALU 结果的第 0 位接 $0$（分支与 `jal` 的目标本来就是偶数，不受影响）。

### 6.3.7. U 型指令

`lui rd, imm` 把 20 位立即数放在 rd 的高 20 位、低 12 位清零；`auipc rd, imm` 把同样的立即数加到 PC 上写入 rd。立即数生成器增加 U 型格式（inst[31:12] 后接 12 个 $0$）之后，`auipc` 用 ASel 选 PC、BSel 选立即数、ALU 做加法；`lui` 让 ALU 直接输出 B 输入（上一章 ALU 的 PASS B 运算）。两条指令都不需要新的数据通路。

### 6.3.8. 立即数生成器

**定义 6.3.1（立即数生成器）** 数据通路中按指令格式从指令字中取出立即数的各个位段、按规定的顺序拼接并扩展为 32 位操作数的组合电路称为**立即数生成器**（immediate generator）。

RV32I 五种带立即数的格式所生成的 32 位立即数如下，其中 $\{n\{b\}\}$ 表示把位 $b$ 重复 $n$ 次：

| ImmSel | 指令 | 生成的立即数 imm[31:0] |
|---|---|---|
| I | `addi`、`lw`、`jalr` 等 | $\{21\{\mathrm{inst}[31]\}\}$, inst[30:20] |
| S | `sw` 等 | $\{21\{\mathrm{inst}[31]\}\}$, inst[30:25], inst[11:7] |
| B | 分支 | $\{20\{\mathrm{inst}[31]\}\}$, inst[7], inst[30:25], inst[11:8], $0$ |
| U | `lui`、`auipc` | inst[31:12], $\{12\{0\}\}$ |
| J | `jal` | $\{12\{\mathrm{inst}[31]\}\}$, inst[19:12], inst[20], inst[30:21], $0$ |

RISC-V 的立即数位段排列看似零乱，实则是为这个电路设计的：符号位总是 inst[31]，符号扩展可以在知道格式之前就开始；同一个立即数位在不同格式中尽量来自指令的同一位置（如 imm[10:5] 总是 inst[30:25]），每个输出位只需一个很小的多路选择器。

```systemverilog
package cpu_pkg;
  typedef enum logic [2:0] {IMM_I, IMM_S, IMM_B, IMM_U, IMM_J} imm_sel_t;
endpackage

module imm_gen
  import cpu_pkg::*;
(
  input  logic [31:7] inst,
  input  imm_sel_t    sel,
  output logic [31:0] imm
);
  always_comb begin
    unique case (sel)
      IMM_I:   imm = {{21{inst[31]}}, inst[30:20]};
      IMM_S:   imm = {{21{inst[31]}}, inst[30:25], inst[11:7]};
      IMM_B:   imm = {{20{inst[31]}}, inst[7], inst[30:25], inst[11:8], 1'b0};
      IMM_U:   imm = {inst[31:12], 12'b0};
      IMM_J:   imm = {{12{inst[31]}}, inst[19:12], inst[20], inst[30:21], 1'b0};
      default: imm = '0;
    endcase
  end
endmodule
```

### 6.3.9. 完整的数据通路

把以上各步合在一起，就得到支持这组指令的单周期数据通路：

![RV32I 单周期数据通路：PC、指令存储器 IMEM、寄存器堆 RegFile、立即数生成器 ImmGen、分支比较器、ALU、数据存储器 DMEM，以及 PCSel、ASel、BSel、WBSel 四个多路选择器；虚线是控制单元发出的控制信号，BrEq、BrLt 是比较器送给控制单元的状态](./plots/single-cycle-datapath.py)

## 6.4. 控制器

### 6.4.1. 控制信号

| 信号 | 取值 | 作用 |
|---|---|---|
| PCSel | $0$：PC $+ 4$；$1$：ALU 结果 | 选择下一条指令的地址 |
| ImmSel | I / S / B / U / J | 选择立即数格式 |
| RegWEn | $0$ / $1$ | 寄存器堆写使能 |
| BrUn | $0$：有符号；$1$：无符号 | 分支比较方式 |
| BrEq、BrLt | 比较器的输出 | 送给控制器，不是控制信号 |
| ASel | $0$：rs1；$1$：PC | ALU 的 A 输入 |
| BSel | $0$：rs2；$1$：立即数 | ALU 的 B 输入 |
| ALUSel | ADD、SUB、…、PASS B | ALU 的运算 |
| MemRW | Read / Write | 数据存储器读写 |
| WBSel | $0$：DMEM；$1$：ALU；$2$：PC $+ 4$ | 写回寄存器的数据 |

### 6.4.2. 控制信号真值表

把每条指令所需的信号整理成表（`*` 表示**无关项**，可取任意值）：

| 指令 | PCSel | ImmSel | BrUn | ASel | BSel | ALUSel | MemRW | RegWEn | WBSel |
|---|---|---|---|---|---|---|---|---|---|
| `add` | $+4$ | * | * | rs1 | rs2 | ADD | Read | 1 | ALU |
| `sub` | $+4$ | * | * | rs1 | rs2 | SUB | Read | 1 | ALU |
| 其他 R 型 | $+4$ | * | * | rs1 | rs2 | 由 funct 决定 | Read | 1 | ALU |
| `addi` 等 | $+4$ | I | * | rs1 | Imm | 由 funct3 决定 | Read | 1 | ALU |
| `lw` | $+4$ | I | * | rs1 | Imm | ADD | Read | 1 | Mem |
| `sw` | $+4$ | S | * | rs1 | Imm | ADD | Write | 0 | * |
| `beq` | BrEq ? ALU : $+4$ | B | * | PC | Imm | ADD | Read | 0 | * |
| `bne` | BrEq ? $+4$ : ALU | B | * | PC | Imm | ADD | Read | 0 | * |
| `blt` / `bge` | BrLt ? ALU : $+4$ / 反之 | B | 0 | PC | Imm | ADD | Read | 0 | * |
| `bltu` / `bgeu` | BrLt ? ALU : $+4$ / 反之 | B | 1 | PC | Imm | ADD | Read | 0 | * |
| `jal` | ALU | J | * | PC | Imm | ADD | Read | 1 | PC $+ 4$ |
| `jalr` | ALU | I | * | rs1 | Imm | ADD | Read | 1 | PC $+ 4$ |
| `lui` | $+4$ | U | * | * | Imm | PASS B | Read | 1 | ALU |
| `auipc` | $+4$ | U | * | PC | Imm | ADD | Read | 1 | ALU |

单周期处理器的控制器不需要保存任何状态：它是一个组合电路，输入是指令（实际只用到 opcode、funct3 和 inst[30]）以及比较器的 BrEq、BrLt，输出是全部控制信号。表中值得注意的两点：

- 写存储器和写寄存器的使能信号绝不能是无关项，否则会破坏状态；其余信号的无关项可以按化简的方便取值。
- ALU 的运算编码取 $\{\mathrm{inst}[30], \mathrm{funct3}\}$（上一章 §5.2.5）。对 R 型指令，inst[30] 是 funct7 的第 5 位，区分 `add`/`sub` 与 `srl`/`sra`；对 I 型算术指令，inst[30] 是立即数的一位，只有移位指令 `srai` 用它区分算术右移，其他指令必须把它当作 $0$，否则 `addi` 遇到第 10 位为 $1$ 的立即数会被误译为减法。

### 6.4.3. 控制器的实现

控制器可以用 **ROM** 或 **PLA** 实现**真值表**，也可以直接写成组合逻辑。下面的 SystemVerilog 代码按 opcode 给出每类指令的信号，分支是否发生由 funct3 与比较器的输出决定；ALU 的运算编码沿用上一章的 `alu_pkg`：

```systemverilog
module control
  import alu_pkg::*, cpu_pkg::*;
(
  input  logic [31:0] inst,
  input  logic        br_eq, br_lt,
  output logic        pc_sel,      // 0: PC + 4, 1: ALU result
  output imm_sel_t    imm_sel,
  output logic        br_un,       // 1: unsigned comparison
  output logic        a_sel,       // 0: rs1, 1: PC
  output logic        b_sel,       // 0: rs2, 1: immediate
  output alu_op_t     alu_sel,
  output logic        mem_rw,      // 1: write data memory
  output logic        reg_wen,
  output logic [1:0]  wb_sel       // 0: DMEM, 1: ALU, 2: PC + 4
);
  logic [6:0] opcode;
  logic [2:0] funct3;
  logic       taken;

  assign opcode = inst[6:0];
  assign funct3 = inst[14:12];

  always_comb begin                // branch condition
    unique case (funct3)
      3'b000:         taken = br_eq;     // beq
      3'b001:         taken = !br_eq;    // bne
      3'b100, 3'b110: taken = br_lt;     // blt, bltu
      3'b101, 3'b111: taken = !br_lt;    // bge, bgeu
      default:        taken = 1'b0;
    endcase
  end

  always_comb begin
    // defaults: no state is written, PC advances by 4
    pc_sel = 1'b0; imm_sel = IMM_I; br_un = funct3[1];
    a_sel = 1'b0; b_sel = 1'b0; alu_sel = ALU_ADD;
    mem_rw = 1'b0; reg_wen = 1'b0; wb_sel = 2'd1;
    unique case (opcode)
      7'b0110011: begin            // R-type
        alu_sel = alu_op_t'({inst[30], funct3});
        reg_wen = 1'b1;
      end
      7'b0010011: begin            // I-type arithmetic: inst[30] only matters for srai
        b_sel = 1'b1; reg_wen = 1'b1;
        alu_sel = alu_op_t'({(funct3 == 3'b101) & inst[30], funct3});
      end
      7'b0000011: begin            // loads
        b_sel = 1'b1; reg_wen = 1'b1; wb_sel = 2'd0;
      end
      7'b0100011: begin            // stores
        imm_sel = IMM_S; b_sel = 1'b1; mem_rw = 1'b1;
      end
      7'b1100011: begin            // branches
        imm_sel = IMM_B; a_sel = 1'b1; b_sel = 1'b1; pc_sel = taken;
      end
      7'b1101111: begin            // jal
        imm_sel = IMM_J; a_sel = 1'b1; b_sel = 1'b1; pc_sel = 1'b1;
        reg_wen = 1'b1; wb_sel = 2'd2;
      end
      7'b1100111: begin            // jalr
        b_sel = 1'b1; pc_sel = 1'b1; reg_wen = 1'b1; wb_sel = 2'd2;
      end
      7'b0110111: begin            // lui
        imm_sel = IMM_U; b_sel = 1'b1; alu_sel = ALU_B; reg_wen = 1'b1;
      end
      7'b0010111: begin            // auipc
        imm_sel = IMM_U; a_sel = 1'b1; b_sel = 1'b1; reg_wen = 1'b1;
      end
      default: ;                   // unsupported opcode: change no state
    endcase
  end
endmodule
```

把各部件连起来就是完整的单周期处理器。为了简洁，这里的存储器只支持按字访问，并且是组合读出的；**FPGA** 上的块存储器（BRAM）是同步读出的，实际实现时要相应调整时序，或使用外部的 SRAM：

```systemverilog
module single_cycle_cpu
  import alu_pkg::*, cpu_pkg::*;
(
  input logic clk, rst
);
  logic [31:0] pc, pc_plus4, inst, rs1, rs2, imm, a, b, alu_y, dmem_r, wb;
  logic        pc_sel, br_un, br_eq, br_lt, a_sel, b_sel, mem_rw, reg_wen;
  logic [1:0]  wb_sel;
  imm_sel_t    imm_sel;
  alu_op_t     alu_sel;

  logic [31:0] imem [0:1023];      // 4 KiB instruction memory
  logic [31:0] dmem [0:1023];      // 4 KiB data memory, word accesses only

  // instruction fetch and next PC (bit 0 cleared for jalr)
  assign pc_plus4 = pc + 32'd4;
  always_ff @(posedge clk)
    if (rst) pc <= 32'h0;
    else     pc <= pc_sel ? {alu_y[31:1], 1'b0} : pc_plus4;
  assign inst = imem[pc[11:2]];

  // decode, register read, immediate, branch comparison
  regfile u_rf (.clk, .we(reg_wen), .addr_a(inst[19:15]), .addr_b(inst[24:20]),
                .addr_d(inst[11:7]), .data_d(wb), .data_a(rs1), .data_b(rs2));
  imm_gen u_imm (.inst(inst[31:7]), .sel(imm_sel), .imm);
  assign br_eq = (rs1 == rs2);
  assign br_lt = br_un ? (rs1 < rs2) : ($signed(rs1) < $signed(rs2));

  // execute
  assign a = a_sel ? pc : rs1;
  assign b = b_sel ? imm : rs2;
  alu u_alu (.a, .b, .op(alu_sel), .y(alu_y));

  // memory access
  assign dmem_r = dmem[alu_y[11:2]];
  always_ff @(posedge clk)
    if (mem_rw) dmem[alu_y[11:2]] <= rs2;

  // write back
  always_comb
    unique case (wb_sel)
      2'd0:    wb = dmem_r;
      2'd1:    wb = alu_y;
      default: wb = pc_plus4;
    endcase

  control u_ctl (.inst, .br_eq, .br_lt, .pc_sel, .imm_sel, .br_un, .a_sel, .b_sel,
                 .alu_sel, .mem_rw, .reg_wen, .wb_sel);
endmodule
```

## 6.5. 时序与性能

### 6.5.1. 关键路径与时钟周期

单周期处理器在一个时钟周期内完成一条指令：周期开始时（上一个上升沿之后）PC 的新值出现，取指令、译码、运算、访存相继完成，所有结果在下一个上升沿同时写入 PC、寄存器堆和数据存储器。整个**指令周期**中控制信号保持不变。因此时钟周期必须容纳最慢的那条指令所经过的最长组合路径。

**定义 6.5.1（关键路径）** 同步时序电路中，从一个状态部件的时钟边沿出发、经过组合逻辑到达另一个（或同一个）状态部件输入端的所有路径中，延迟最长的一条称为**关键路径**（critical path）。

时钟周期 $T_{\mathrm{c}}$ 必须满足

$$
T_{\mathrm{c}} \ge t_{\mathrm{pcq}} + t_{\mathrm{logic}} + t_{\mathrm{su}} ,
$$
其中 $t_{\mathrm{pcq}}$ 是**触发器**的**时钟到输出延迟**，$t_{\mathrm{logic}}$ 是关键路径上组合逻辑的延迟，$t_{\mathrm{su}}$ 是目的触发器的**建立时间**（[锁存器与触发器](/4.9.6)）。

**例 6.5.1** 设各部件的延迟为：$t_{\mathrm{pcq}} = 30\ \mathrm{ps}$，IMEM 读 $200\ \mathrm{ps}$，寄存器堆读 $100\ \mathrm{ps}$，立即数生成 $50\ \mathrm{ps}$，多路选择器 $20\ \mathrm{ps}$，ALU $150\ \mathrm{ps}$，分支比较器 $80\ \mathrm{ps}$，DMEM 读 $200\ \mathrm{ps}$，写入状态部件的建立时间 $t_{\mathrm{su}} = 20\ \mathrm{ps}$；控制器的译码（$50\ \mathrm{ps}$）与寄存器堆的读取并行，不在关键路径上。各类指令的最长路径为：

| 指令类型 | 最长路径 | 延迟 |
|---|---|---|
| R 型、I 型算术、`lui`、`auipc` | PC → IMEM → 寄存器堆 → BSel → ALU → WBSel → 寄存器堆 | $30 + 200 + 100 + 20 + 150 + 20 + 20 = 540\ \mathrm{ps}$ |
| `lw` | PC → IMEM → 寄存器堆 → BSel → ALU → DMEM → WBSel → 寄存器堆 | $30 + 200 + 100 + 20 + 150 + 200 + 20 + 20 = 740\ \mathrm{ps}$ |
| `sw` | PC → IMEM → 寄存器堆 → BSel → ALU → DMEM 地址 | $30 + 200 + 100 + 20 + 150 + 20 = 520\ \mathrm{ps}$ |
| 分支、`jal` | PC → IMEM → ImmGen → BSel → ALU → PCSel → PC | $30 + 200 + 50 + 20 + 150 + 20 + 20 = 490\ \mathrm{ps}$ |

分支的另一条路径（寄存器堆 → 比较器 → 控制器 → PCSel）为 $30 + 200 + 100 + 80 + 30 + 20 + 20 = 480\ \mathrm{ps}$（设控制器由比较结果产生 PCSel 需 $30\ \mathrm{ps}$），略短于目标地址的计算。`jalr` 的路径与 R 型相近：ALU 的结果写 PC，PC $+ 4$ 早已稳定。关键路径是 `lw` 的取指—读寄存器—算地址—读存储器—写回，时钟周期至少为 $740\ \mathrm{ps}$，频率约 $1.35\ \mathrm{GHz}$。

此外还有**保持时间**约束：最短路径的延迟必须不小于目的触发器的保持时间，否则新数据会在边沿之后过早地改变触发器的输入。单周期处理器中最短的路径也要经过存储器或寄存器堆，一般不成问题。

### 6.5.2. 单周期处理器的性能

处理器的**执行时间**是 CPU 时间 $=$ 指令数 $\times$ **CPI** $\times$ 时钟周期。单周期处理器的 CPI 恰好为 $1$，但时钟周期由最慢的指令决定：

**例 6.5.2** 设某程序的指令组成为：`lw` 占 $25\%$，`sw` 占 $10\%$，R 型与 I 型算术指令占 $45\%$，分支占 $15\%$，跳转占 $5\%$。若时钟周期能随指令变化（只是假想），平均每条指令的时间为

$$
0.25 \times 740 + 0.10 \times 520 + 0.45 \times 540 + 0.15 \times 490 + 0.05 \times 490 = 578\ \mathrm{ps},
$$
而单周期处理器的每条指令都要 $740\ \mathrm{ps}$，慢了 $740 / 578 \approx 1.28$ 倍。执行 $10^9$ 条指令，单周期处理器需要 $0.74\ \mathrm{s}$。

**定义 6.5.2（单周期处理器）** 每条指令都在一个时钟周期内完成全部执行步骤、时钟周期由最长的指令路径决定的处理器称为**单周期处理器**。

单周期处理器的特点可以概括为：

- 优点：每条指令一个周期，CPI $= 1$；控制器是纯组合逻辑，不需要状态信息；逻辑设计和时序分析都简单。
- 缺点：时钟周期必须满足执行时间最长的指令，大多数指令在周期的后半段闲置；每个部件在一个周期内只能使用一次，必须重复设置（两个存储器、单独的加法器）；控制信号在整个周期内保持，部件的利用率低。如果再加入乘除法或**浮点运算**，时钟周期会长得无法接受。

因此单周期处理器主要用于教学，实际的处理器不采用这种方式：早期的计算机多采用多周期、微程序控制的方式，现代处理器则使用流水线。改进的方向有两条，都在后续章节中讨论：一是把指令的执行拆成多个较短的周期，让简单的指令少用几个周期（多周期处理器）；二是让多条指令的不同阶段重叠执行（流水线），在保持 CPI 接近 $1$ 的同时把时钟周期缩短到大约一个阶段的长度。

## 小结

| 主题 | 要点 |
|---|---|
| 执行阶段 | IF、ID、EX、MEM、WB；单周期、多周期、流水线三种组织方式 |
| 数据通路 | 组合部件（加法器、多路选择器、ALU、立即数生成器、比较器）+ 状态部件（PC、寄存器堆、IMEM、DMEM）；边沿触发，读组合、写在时钟边沿 |
| 逐条构建 | R 型：寄存器堆 + ALU；I 型：ImmGen + BSel；`lw`：DMEM + WBSel；`sw`：DataW、ImmSel；分支：比较器 + ASel + PCSel；`jal`/`jalr`：WBSel 选 PC $+ 4$；U 型：ALU 的 PASS B |
| 立即数生成器 | 五种格式拼接与**符号扩展**；符号位总在 inst[31] |
| 控制器 | 组合逻辑；输入 opcode、funct3、inst[30]、BrEq、BrLt；输出 PCSel、ImmSel、BrUn、ASel、BSel、ALUSel、MemRW、RegWEn、WBSel；写使能不能是无关项 |
| 时序 | $T_{\mathrm{c}} \ge t_{\mathrm{pcq}} + t_{\mathrm{logic}} + t_{\mathrm{su}}$；关键路径是 `lw` |
| 性能 | CPI $= 1$，时钟周期由最慢的指令决定；利用率低，引出多周期与流水线 |
