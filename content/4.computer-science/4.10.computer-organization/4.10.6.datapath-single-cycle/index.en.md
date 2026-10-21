---
title: Datapath and the Single-Cycle Processor
description: The five stages of instruction execution and three ways to implement them; the combinational and state elements of a datapath (PC, register file, memories) and the clocking methodology; step-by-step construction of the RV32I datapath for add, sub, addi, lw, sw, branches, jal, jalr, lui, and auipc; the immediate generator; control signals and their truth table, a SystemVerilog implementation of the controller; critical path, clock cycle time, and the performance of the single-cycle processor.
source_hash: 3b19c2cb5cd1
---

The previous chapters gave the **instruction formats** of **RISC-V** and the arithmetic unit. This chapter combines them into a processor that can execute instructions: we first determine which components are needed to execute an instruction and how data flows between them (the datapath), and then design the controller that generates the control signals of each component from the instruction. The simplest organization lets every instruction complete in one **clock cycle**; this is called the single-cycle processor. Its structure and timing are simple, and it is the basis for understanding the multicycle processors and pipelines of later chapters; its drawback (the clock cycle is set by the slowest instruction) is exactly the starting point of those improvements. This chapter takes a set of RV32I instructions covering all six instruction formats as its example: `add`, `sub`, `addi`, `lw`, `sw`, `beq` (and the other branches), `jal`, `jalr`, `lui`, and `auipc`; the other instructions are implemented on the same principles.

## 6.1. How an Instruction Is Executed

A stored-program computer loads the program and data into memory before running. To execute a program, the processor starts from the first address of the program, fetches instructions one by one, analyzes them, performs the operations they require, and forms the address of the next instruction at the same time, continuing automatically until the program ends; the whole process is carried out by the hardware itself. This is the core of the **von Neumann architecture**.

The execution of an instruction is usually divided into five stages, and the division is determined jointly by the function of the instruction and the hardware structure:

| Stage | Name | Work |
|---|---|---|
| IF | instruction fetch | read the instruction from memory using the **PC** as the address, and compute PC $+ 4$ |
| ID | instruction decode | analyze the instruction, read the **register file** to obtain the source operands, and generate the immediate |
| EX | execute | the **ALU** performs the operation, or computes the memory address or branch target |
| MEM | memory access | read or write the data memory |
| WB | write back | write the ALU result or the data read from memory into the destination **register** |

Not every instruction needs all five stages: `add` does not access memory, and `sw` and branch instructions do not write back. The time from fetching an instruction to finishing its execution is called the **instruction cycle**, and the clock cycle of the processor is called the CPU cycle. There are three basic ways to arrange these stages:

- single-cycle: every instruction completes all stages in one clock cycle, and the next instruction starts only after the previous one has finished;
- multicycle: each stage takes one clock cycle, different instructions use different numbers of cycles, and the control signals change with the execution step;
- pipelined: each stage takes one clock cycle, but the execution of adjacent instructions overlaps in time, so that each time a stage finishes, that stage of the next instruction starts, and ideally one instruction completes per clock cycle. Current processors generally use pipelines.

The latter two are discussed in later chapters.

## 6.2. Components of the Datapath

**Definition 6.2.1 (Datapath and Control Unit)** The components of a processor that store, transmit, and process data, together with their connections (registers, memories, the ALU, adders, multiplexers, and the wires between them), are called the **datapath**; the component that generates, from the current instruction, the control signals needed by the components of the datapath is called the **control unit**, also called the controller.

This corresponds to the division of labor between the arithmetic unit and the controller in the **von Neumann architecture**: the datapath moves and operates on data, and the controller directs how the data moves and is operated on. The components of a datapath fall into two kinds.

Combinational components have outputs that depend only on the current inputs:

- adder: computes PC $+ 4$;
- **multiplexer**: selects one of several data sources, with the select signal coming from the controller;
- ALU: the $32$-bit ALU of the previous chapter, with the operation selected by ALUSel;
- the immediate generator (§6.3.8) and the branch comparator (§6.3.5).

State components (sequential components) hold data and are updated at clock edges:

- **program counter** PC: a $32$-bit register made of $32$ **D flip-flops**, written with the address of the next instruction at every rising clock edge;
- register file: $32$ registers of $32$ bits, with two read ports and one write port. The read ports are combinational: given the addresses AddrA and AddrB, after a delay the register values appear on DataA and DataB; the write port writes DataD to the register designated by AddrD at the rising clock edge when the write enable RegWEn is $1$. `x0` is always $0$, and writes to it are ignored. Two reads and one write can be completed in one clock cycle;
- instruction memory IMEM and data memory DMEM: in the idealized model of the single-cycle processor, reads are combinational (the data is obtained as soon as the address is given), and writes occur at a clock edge when the write enable is $1$.

In one cycle an instruction must fetch the instruction and may also read or write data, while each component can be used only once per cycle; therefore the single-cycle processor must separate the instruction memory from the data memory, and likewise needs a separate adder for PC $+ 4$ that cannot be shared with the ALU.

The clocking methodology is **edge-triggered**: all state components are updated at the same rising clock edge; between two edges, the outputs of the state components propagate through combinational logic and settle at the inputs of the state components before the next edge arrives. A state component can therefore be read first and written later in the same cycle (for example `addi x5, x5, 1` reads the old `x5` and writes the new value at the end of the cycle) without causing a **race**.

A register file described in **SystemVerilog** follows; reads are combinational logic and writes occur at the rising clock edge:

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

## 6.3. Building the Datapath Instruction by Instruction

The method of building a datapath is to start from the simplest instruction, add one class of instructions at a time, check whether the existing path can perform its function, and if not, add components or multiplexers.

### 6.3.1. R-Type Instructions

`add rd, rs1, rs2` performs $R[\mathrm{rd}] \gets R[\mathrm{rs1}] + R[\mathrm{rs2}]$, and `sub` performs subtraction; afterwards PC $\gets$ PC $+ 4$. The required paths are:

1. instruction fetch: PC goes to the address input of IMEM, which reads the $32$-bit instruction inst; PC also goes to the adder to give PC $+ 4$, which is written back to PC at the end of the cycle;
2. register read: inst[19:15] (rs1) and inst[24:20] (rs2) go to AddrA and AddrB of the register file;
3. operation: DataA and DataB go to the ALU, and the controller gives ALUSel according to funct7 and funct3 (ADD for `add`, SUB for `sub`);
4. write back: the ALU result goes to DataD, inst[11:7] (rd) goes to AddrD, and RegWEn $= 1$.

In all RISC-V formats rs1, rs2, and rd are always in the same positions, so the register file addresses can be wired directly from fixed fields of the instruction, and the register read can start before the controller has finished decoding. If a value that is read is not needed (for example, the rs2 position of an I-type instruction is actually part of the immediate), it is simply discarded. This is one of the considerations in the design of the RISC-V instruction formats that shortens the critical path.

### 6.3.2. I-Type Arithmetic Instructions

`addi rd, rs1, imm` performs $R[\mathrm{rd}] \gets R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{imm})$. The second operand of the ALU must be able to come from the immediate, so we add:

- the immediate generator ImmGen: extracts the $12$-bit immediate from inst[31:20] and extends it to $32$ bits by **sign extension**;
- a multiplexer in front of the B input of the ALU: BSel $= 0$ selects rs2 and BSel $= 1$ selects the immediate.

### 6.3.3. Load Instructions

`lw rd, imm(rs1)` performs $\mathrm{Addr} = R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{imm})$ and $R[\mathrm{rd}] \gets \mathrm{MEM}[\mathrm{Addr}]$. The address computation is exactly the same as for `addi` (the immediate is also I-type); what is new is:

- the data memory DMEM: the ALU result goes to its address input Addr, and the data read out is DataR;
- a multiplexer WBSel before the write back, selecting whether the value written to the register is the ALU result or DataR.

`lb`, `lh`, `lbu`, and `lhu` additionally need to select the corresponding byte or halfword from DataR according to the low two bits of the address, and to sign-extend or zero-extend it according to funct3.

### 6.3.4. Store Instructions

`sw rs2, imm(rs1)` performs $\mathrm{MEM}[R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{imm})] \gets R[\mathrm{rs2}]$. What is new is:

- the write data input DataW of DMEM is connected to DataB of the register file (the value of rs2), and the write enable is controlled by MemRW;
- the immediate of an S-type instruction is split into two fields, inst[31:25] and inst[11:7], so the immediate generator must assemble it according to the format; its input is therefore widened to inst[31:7], and a format select signal ImmSel is added;
- a store instruction does not write a register, so RegWEn $= 0$.

`sb` and `sh` require the memory to support byte write enables, so that only some of the bytes in a word are rewritten.

### 6.3.5. Branch Instructions

`beq rs1, rs2, offset` performs: if $R[\mathrm{rs1}] = R[\mathrm{rs2}]$, then PC $\gets$ PC $+ \mathrm{SignExt}(\mathrm{offset})$, otherwise PC $\gets$ PC $+ 4$. It must both compare two registers and compute the branch target, but there is only one ALU, so we add:

- a branch comparator Branch Comp: its inputs are DataA and DataB, and its outputs are BrEq (equal) and BrLt (less than); the control signal BrUn selects an unsigned (`bltu`, `bgeu`) or signed (`blt`, `bge`) comparison;
- a multiplexer ASel in front of the A input of the ALU: when ASel $= 1$ it selects PC, so the ALU computes PC $+$ immediate as the branch target;
- a multiplexer PCSel in front of the input of PC, selecting between PC $+ 4$ and the ALU result. The controller decides PCSel from BrEq, BrLt, and funct3.

The B-type immediate encodes an offset in units of $2$ bytes, and the immediate generator appends a $0$ at the lowest bit, so the branch range is $\pm 4\ \mathrm{KiB}$.

### 6.3.6. Jump Instructions

`jal rd, offset` performs $R[\mathrm{rd}] \gets$ PC $+ 4$ and PC $\gets$ PC $+ \mathrm{SignExt}(\mathrm{offset})$. The jump target is computed by the ALU (ASel selects PC, BSel selects the J-type immediate) and PCSel selects the ALU; but what is written back to the register is PC $+ 4$, and the existing datapath has no path for it. The ALU could be modified, but the simpler way is to bring PC $+ 4$ to the write-back multiplexer and extend WBSel to three choices: $0$ selects DMEM, $1$ selects the ALU, and $2$ selects PC $+ 4$.

`jalr rd, offset(rs1)` is an I-type instruction and performs $R[\mathrm{rd}] \gets$ PC $+ 4$ and PC $\gets (R[\mathrm{rs1}] + \mathrm{SignExt}(\mathrm{offset}))\ \&\ {\sim}1$. Its only difference from `jal` is that the A input of the ALU takes rs1 (ASel $= 0$) and the immediate is I-type, so the existing datapath is already sufficient; the specification requires clearing the lowest bit of the target address, which only requires wiring bit $0$ of the ALU result to $0$ at the input of PC (the targets of branches and `jal` are even anyway and are not affected).

### 6.3.7. U-Type Instructions

`lui rd, imm` places the $20$-bit immediate in the upper $20$ bits of rd and clears the lower $12$ bits; `auipc rd, imm` adds the same immediate to PC and writes the result to rd. Once the immediate generator has the U-type format (inst[31:12] followed by $12$ zeros), `auipc` uses ASel to select PC, BSel to select the immediate, and the ALU to add; `lui` makes the ALU output its B input directly (the PASS B operation of the ALU in the previous chapter). Neither instruction needs a new path in the datapath.

### 6.3.8. The Immediate Generator

**Definition 6.3.1 (Immediate Generator)** The combinational circuit in the datapath that extracts the fields of the immediate from the instruction word according to the instruction format, concatenates them in the prescribed order, and extends the result to a $32$-bit operand is called the **immediate generator**.

The $32$-bit immediates generated for the five RV32I formats that carry immediates are as follows, where $\{n\{b\}\}$ denotes the bit $b$ repeated $n$ times:

| ImmSel | Instructions | Generated immediate imm[31:0] |
|---|---|---|
| I | `addi`, `lw`, `jalr`, etc. | $\{21\{\mathrm{inst}[31]\}\}$, inst[30:20] |
| S | `sw`, etc. | $\{21\{\mathrm{inst}[31]\}\}$, inst[30:25], inst[11:7] |
| B | branches | $\{20\{\mathrm{inst}[31]\}\}$, inst[7], inst[30:25], inst[11:8], $0$ |
| U | `lui`, `auipc` | inst[31:12], $\{12\{0\}\}$ |
| J | `jal` | $\{12\{\mathrm{inst}[31]\}\}$, inst[19:12], inst[20], inst[30:21], $0$ |

The arrangement of the immediate fields in RISC-V looks haphazard but was designed for this circuit: the sign bit is always inst[31], so sign extension can begin before the format is known, and the same immediate bit comes from the same position in the instruction in as many formats as possible (for example imm[10:5] is always inst[30:25]), so each output bit needs only a very small multiplexer.

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

### 6.3.9. The Complete Datapath

Putting all the steps above together gives the single-cycle datapath supporting this set of instructions:

![The RV32I single-cycle datapath: PC, instruction memory IMEM, register file RegFile, immediate generator ImmGen, branch comparator, ALU, data memory DMEM, and the four multiplexers PCSel, ASel, BSel, and WBSel; the dashed lines are control signals issued by the control unit, and BrEq and BrLt are status signals sent by the comparator to the control unit](./plots/single-cycle-datapath.py)

## 6.4. The Controller

### 6.4.1. Control Signals

| Signal | Values | Function |
|---|---|---|
| PCSel | $0$: PC $+ 4$; $1$: ALU result | selects the address of the next instruction |
| ImmSel | I / S / B / U / J | selects the immediate format |
| RegWEn | $0$ / $1$ | register file write enable |
| BrUn | $0$: signed; $1$: unsigned | branch comparison mode |
| BrEq, BrLt | outputs of the comparator | sent to the controller; not control signals |
| ASel | $0$: rs1; $1$: PC | A input of the ALU |
| BSel | $0$: rs2; $1$: immediate | B input of the ALU |
| ALUSel | ADD, SUB, …, PASS B | operation of the ALU |
| MemRW | Read / Write | data memory read or write |
| WBSel | $0$: DMEM; $1$: ALU; $2$: PC $+ 4$ | data written back to the register |

### 6.4.2. The Control Signal Truth Table

The signals needed by each instruction are collected in a table (`*` denotes a **don't-care term**, which may take any value):

| Instruction | PCSel | ImmSel | BrUn | ASel | BSel | ALUSel | MemRW | RegWEn | WBSel |
|---|---|---|---|---|---|---|---|---|---|
| `add` | $+4$ | * | * | rs1 | rs2 | ADD | Read | 1 | ALU |
| `sub` | $+4$ | * | * | rs1 | rs2 | SUB | Read | 1 | ALU |
| other R-type | $+4$ | * | * | rs1 | rs2 | determined by funct | Read | 1 | ALU |
| `addi`, etc. | $+4$ | I | * | rs1 | Imm | determined by funct3 | Read | 1 | ALU |
| `lw` | $+4$ | I | * | rs1 | Imm | ADD | Read | 1 | Mem |
| `sw` | $+4$ | S | * | rs1 | Imm | ADD | Write | 0 | * |
| `beq` | BrEq ? ALU : $+4$ | B | * | PC | Imm | ADD | Read | 0 | * |
| `bne` | BrEq ? $+4$ : ALU | B | * | PC | Imm | ADD | Read | 0 | * |
| `blt` / `bge` | BrLt ? ALU : $+4$ / reversed | B | 0 | PC | Imm | ADD | Read | 0 | * |
| `bltu` / `bgeu` | BrLt ? ALU : $+4$ / reversed | B | 1 | PC | Imm | ADD | Read | 0 | * |
| `jal` | ALU | J | * | PC | Imm | ADD | Read | 1 | PC $+ 4$ |
| `jalr` | ALU | I | * | rs1 | Imm | ADD | Read | 1 | PC $+ 4$ |
| `lui` | $+4$ | U | * | * | Imm | PASS B | Read | 1 | ALU |
| `auipc` | $+4$ | U | * | PC | Imm | ADD | Read | 1 | ALU |

The controller of a single-cycle processor needs to store no state: it is a combinational circuit whose inputs are the instruction (only opcode, funct3, and inst[30] are actually used) and the comparator outputs BrEq and BrLt, and whose outputs are all the control signals. Two points in the table deserve attention:

- The enable signals for writing memory and writing registers must never be don't-cares, or state would be corrupted; the don't-cares of the other signals can take whichever values are convenient for simplification.
- The operation code of the ALU is $\{\mathrm{inst}[30], \mathrm{funct3}\}$ (§5.2.5 of the previous chapter). For R-type instructions, inst[30] is bit $5$ of funct7 and distinguishes `add`/`sub` and `srl`/`sra`; for I-type arithmetic instructions, inst[30] is a bit of the immediate, and only the shift instruction `srai` uses it to distinguish an arithmetic right shift; all other instructions must treat it as $0$, or an `addi` whose immediate has bit $10$ set would be misdecoded as a subtraction.

### 6.4.3. Implementing the Controller

The controller can implement the **truth table** with a **ROM** or a **PLA**, or can be written directly as combinational logic. The SystemVerilog code below gives the signals of each class of instruction by opcode, and whether a branch is taken is decided by funct3 and the comparator outputs; the ALU operation codes continue to use the `alu_pkg` of the previous chapter:

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

Connecting all the components gives the complete single-cycle processor. For brevity, the memories here support only word accesses and are read combinationally; the block RAM (BRAM) on an **FPGA** reads synchronously, so in a real implementation the timing must be adjusted accordingly, or an external SRAM used:

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

## 6.5. Timing and Performance

### 6.5.1. The Critical Path and the Clock Cycle

A single-cycle processor completes one instruction in one clock cycle: at the beginning of the cycle (after the previous rising edge) the new value of PC appears; instruction fetch, decode, operation, and memory access complete in turn; and all results are written into PC, the register file, and the data memory simultaneously at the next rising edge. Throughout the **instruction cycle** the control signals stay unchanged. Therefore the clock cycle must accommodate the longest combinational path traversed by the slowest instruction.

**Definition 6.5.1 (Critical Path)** In a synchronous sequential circuit, among all paths that start from the clock edge of one state component and pass through combinational logic to the input of another (or the same) state component, the one with the longest delay is called the **critical path**.

The clock cycle time $T_{\mathrm{c}}$ must satisfy

$$
T_{\mathrm{c}} \ge t_{\mathrm{pcq}} + t_{\mathrm{logic}} + t_{\mathrm{su}} ,
$$
where $t_{\mathrm{pcq}}$ is the **clock-to-Q delay** of the **flip-flop**, $t_{\mathrm{logic}}$ is the delay of the combinational logic on the critical path, and $t_{\mathrm{su}}$ is the **setup time** of the destination flip-flop ([Latches and Flip-Flops](/4.9.6)).

**Example 6.5.1** Suppose the component delays are: $t_{\mathrm{pcq}} = 30\ \mathrm{ps}$, IMEM read $200\ \mathrm{ps}$, register file read $100\ \mathrm{ps}$, immediate generation $50\ \mathrm{ps}$, multiplexer $20\ \mathrm{ps}$, ALU $150\ \mathrm{ps}$, branch comparator $80\ \mathrm{ps}$, DMEM read $200\ \mathrm{ps}$, and the setup time for writing to a state component $t_{\mathrm{su}} = 20\ \mathrm{ps}$; the controller's decoding ($50\ \mathrm{ps}$) runs in parallel with the register file read and is not on the critical path. The longest path of each instruction class is:

| Instruction class | Longest path | Delay |
|---|---|---|
| R-type, I-type arithmetic, `lui`, `auipc` | PC → IMEM → register file → BSel → ALU → WBSel → register file | $30 + 200 + 100 + 20 + 150 + 20 + 20 = 540\ \mathrm{ps}$ |
| `lw` | PC → IMEM → register file → BSel → ALU → DMEM → WBSel → register file | $30 + 200 + 100 + 20 + 150 + 200 + 20 + 20 = 740\ \mathrm{ps}$ |
| `sw` | PC → IMEM → register file → BSel → ALU → DMEM address | $30 + 200 + 100 + 20 + 150 + 20 = 520\ \mathrm{ps}$ |
| branches, `jal` | PC → IMEM → ImmGen → BSel → ALU → PCSel → PC | $30 + 200 + 50 + 20 + 150 + 20 + 20 = 490\ \mathrm{ps}$ |

The other path of a branch (register file → comparator → controller → PCSel) is $30 + 200 + 100 + 80 + 30 + 20 + 20 = 480\ \mathrm{ps}$ (assuming the controller needs $30\ \mathrm{ps}$ to produce PCSel from the comparison result), slightly shorter than the target address computation. The path of `jalr` is close to that of R-type: the ALU result is written to PC, and PC $+ 4$ has long been stable. The critical path is the `lw` path of fetch, register read, address computation, memory read, and write back; the clock cycle must be at least $740\ \mathrm{ps}$, a frequency of about $1.35\ \mathrm{GHz}$.

There is also a **hold time** constraint: the delay of the shortest path must be no less than the hold time of the destination flip-flop, otherwise new data would change the input of the flip-flop too soon after the edge. In the single-cycle processor even the shortest path passes through a memory or the register file, so this is generally not a problem.

### 6.5.2. Performance of the Single-Cycle Processor

The **execution time** of a processor is CPU time $=$ instruction count $\times$ **CPI** $\times$ clock cycle time. The CPI of a single-cycle processor is exactly $1$, but the clock cycle is set by the slowest instruction:

**Example 6.5.2** Suppose the instruction mix of a program is: `lw` $25\%$, `sw` $10\%$, R-type and I-type arithmetic $45\%$, branches $15\%$, and jumps $5\%$. If the clock cycle could vary with the instruction (a purely hypothetical case), the average time per instruction would be

$$
0.25 \times 740 + 0.10 \times 520 + 0.45 \times 540 + 0.15 \times 490 + 0.05 \times 490 = 578\ \mathrm{ps},
$$
whereas the single-cycle processor needs $740\ \mathrm{ps}$ for every instruction, which is slower by a factor of $740 / 578 \approx 1.28$. Executing $10^9$ instructions takes the single-cycle processor $0.74\ \mathrm{s}$.

**Definition 6.5.2 (Single-Cycle Processor)** A processor in which every instruction completes all its execution steps in one clock cycle, with the clock cycle set by the longest instruction path, is called a **single-cycle processor**.

The characteristics of the single-cycle processor can be summarized as follows:

- Advantages: one cycle per instruction, CPI $= 1$; the controller is purely combinational logic and needs no state information; logic design and timing analysis are both simple.
- Disadvantages: the clock cycle must accommodate the instruction with the longest execution time, so most instructions leave components idle in the second part of the cycle; each component can be used only once per cycle and must be duplicated (two memories, a separate adder); the control signals are held for the whole cycle, so component utilization is low. If multiplication, division, or **floating-point operations** were added, the clock cycle would become unacceptably long.

The single-cycle processor is therefore used mainly for teaching, and real processors do not use it: early computers mostly used multicycle, microprogrammed control, and modern processors use pipelines. There are two directions of improvement, both discussed in later chapters: one is to split the execution of an instruction into several shorter cycles so that simple instructions use fewer cycles (the multicycle processor); the other is to overlap the execution of different stages of several instructions (pipelining), keeping CPI close to $1$ while shortening the clock cycle to about the length of one stage.

## Summary

| Topic | Key points |
|---|---|
| Execution stages | IF, ID, EX, MEM, WB; three organizations: single-cycle, multicycle, pipelined |
| Datapath | combinational components (adder, multiplexers, ALU, immediate generator, comparator) + state components (PC, register file, IMEM, DMEM); edge-triggered, reads combinational, writes at the clock edge |
| Building step by step | R-type: register file + ALU; I-type: ImmGen + BSel; `lw`: DMEM + WBSel; `sw`: DataW, ImmSel; branches: comparator + ASel + PCSel; `jal`/`jalr`: WBSel selects PC $+ 4$; U-type: PASS B of the ALU |
| Immediate generator | concatenation of five formats and **sign extension**; the sign bit is always inst[31] |
| Controller | combinational logic; inputs opcode, funct3, inst[30], BrEq, BrLt; outputs PCSel, ImmSel, BrUn, ASel, BSel, ALUSel, MemRW, RegWEn, WBSel; write enables must not be don't-cares |
| Timing | $T_{\mathrm{c}} \ge t_{\mathrm{pcq}} + t_{\mathrm{logic}} + t_{\mathrm{su}}$; the critical path is `lw` |
| Performance | CPI $= 1$, clock cycle set by the slowest instruction; low utilization, which motivates multicycle and pipelined designs |
