---
title: Instruction Sets
description: "The role of instructions and the instruction set, and its design requirements; functional classes of instructions; number of operands and the classification of ISAs (stack, accumulator, register-memory, load-store); instruction length, fixed- and variable-length instructions; opcodes and opcode expansion (the prefix-code condition); the x86 instruction format; addressing modes: immediate, register, direct, indirect, register indirect, indexed, base, PC-relative and stack addressing; the history, characteristics and performance comparison of CISC and RISC."
source_hash: f710248e6a97
---

The previous chapter made the **instruction set architecture** the interface between software and hardware. This chapter discusses the general questions that arise in designing this interface, not tied to any one processor: which instructions a computer needs; how an instruction is represented as a string of bits, that is, the instruction format and the encoding of opcodes; how an instruction indicates where its data are, that is, the addressing modes; and the two opposing design philosophies in history, complex **instruction sets** (CISC) and reduced instruction sets (RISC). The examples in this chapter come mainly from x86 and RISC-V, two very different **instruction sets**. The next chapter, [4.10.3](/4.10.3), teaches RISC-V in full, and [4.10.6](/4.10.6) then shows from the hardware side how a regular instruction format simplifies processor design.

## 2.1. Basic Concepts of the Instruction Set

### 2.1.1. Instructions and the Instruction Set

**Definition 2.1.1 (Instruction)** A command that the processor can directly recognize and execute, directing the hardware to perform one basic operation, is called an **instruction**. An instruction is a string of bits that must specify the operation to be performed, together with the object of the operation (the operands) or where they are located.

The set of all the instructions of a computer, together with the **registers**, data types and addressing modes they use, is its **instruction set architecture**. From the viewpoint of the layered structure ([4.10.1](/4.10.1#sec-1.3.1)), the instruction set lies at the boundary between hardware and software: the hardware must implement the function of every instruction and handle the transition between instructions, and software (**compilers**, the operating system and all applications) is ultimately represented as sequences of instructions. Once an instruction set is fixed it is therefore very hard to change: changing it would mean recompiling, or even rewriting, all existing software.

Four goals are usually pursued in designing an instruction set:

| Requirement | Meaning |
|---|---|
| Completeness | The instructions are functionally complete: any computable task can be programmed with them, and common operations are convenient to write |
| Regularity | The instruction format is simple and uniform and instructions of the same kind behave consistently, which eases hardware decoding and compiler code generation |
| Efficiency | Programs occupy little storage and run fast |
| Compatibility | New machines of the same family can run the software of older machines |

These goals conflict: a regular fixed-length format often makes programs longer, and compatibility with old instructions makes the instruction set ever more cluttered. To remain compatible with the 8086 of 1978, x86 still keeps the instructions and encodings of that time, which is the main reason for its complex format (Section 2.2.3).

### 2.1.2. Functional Classes of Instructions

A computer consists of the arithmetic unit, the control unit, the memory and the input/output devices ([4.10.1](/4.10.1#sec-1.2.1)), and the instruction set must provide instructions for using each component:

| Class | Function | x86 examples | RISC-V examples |
|---|---|---|---|
| Arithmetic | Add, subtract, multiply, divide, negate | `ADD`, `SUB`, `IMUL`, `IDIV`, `NEG`, `INC` | `add`, `sub`, `addi`, `mul`, `div` |
| Logic | AND, OR, NOT, **exclusive OR** | `AND`, `OR`, `NOT`, `XOR` | `and`, `or`, `xori` |
| Shift | Logical, arithmetic and circular shifts | `SHL`, `SAR`, `ROL` | `sll`, `srl`, `sra` (rotates are in the B extension) |
| Data transfer | Between registers, and between registers and memory | `MOV`, `XCHG`, `LEA`, `CMOVcc` | `lw`, `sw`, `lb`, `sb` |
| Comparison and condition | Compare and set condition codes or a result | `CMP`, `TEST` | `slt`, `sltu` |
| Control transfer | Unconditional jump, conditional branch | `JMP`, `Jcc`, `LOOP` | `jal`, `beq`, `blt` |
| Subroutine | Call and return | `CALL`, `RET` | `jal`, `jalr` |
| Stack operation | Push, pop | `PUSH`, `POP` | None; implemented with `addi sp` and load/store |
| Input/output | Exchange data with device interfaces | `IN`, `OUT` | None; device registers are mapped to memory addresses and accessed with load/store |
| System and other | System calls, interrupts, privileged operations, no-ops, synchronization | `INT`, `SYSCALL`, `HLT`, `NOP` | `ecall`, `ebreak`, `mret`, `fence`, `csrrw` |

There are two architectural schemes for input and output. x86 has a separate port address space and dedicated `IN`/`OUT` instructions (port-mapped I/O); most RISC machines place device registers in the memory address space and access them with ordinary memory-access instructions (memory-mapped I/O), so no dedicated instructions are needed, as later chapters on input and output discuss in detail. Another difference is conditional branching: x86 first sets the condition codes in the flags register with an instruction such as `CMP`, and then `Jcc` branches on the condition codes; RISC-V has no condition codes, and comparison and branching are done in one instruction ([4.10.3](/4.10.3#sec-3.5.1)).

### 2.1.3. Number of Operands and Classification of Instruction Sets

**Definition 2.1.2 (Opcode and Address Field)** The field of an instruction that specifies the operation to be performed is called the **opcode**; the fields that specify the operands or their locations are called address fields. By the number of address fields, instructions are classified as zero-address, one-address, two-address, three-address instructions and so on.

Operands may come from three places: registers inside the processor, locations in memory, and registers in the interface of an input/output device. How many operands an instruction gives explicitly, and how many of them may be memory operands, determines the basic type of an instruction set. Take the computation of `C = A + B` (with `A`, `B` and `C` all in memory) as an example:

| Type | Operands of arithmetic instructions | Code | Representatives |
|---|---|---|---|
| Stack | Implicit at the top of the stack (zero-address) | `push A`<br/>`push B`<br/>`add`<br/>`pop C` | Burroughs B5000, x87 floating point, JVM, WebAssembly |
| Accumulator | One implicit in the accumulator (one-address) | `load A`<br/>`add B`<br/>`store C` | EDSAC, early microprocessors |
| Register-memory | A register and a memory location (two-address) | `load R1, A`<br/>`add R1, B`<br/>`store R1, C` | IBM 360, x86 |
| Load-store | Registers only (three-address) | `load R1, A`<br/>`load R2, B`<br/>`add R3, R1, R2`<br/>`store R3, C` | RISC-V, ARM, **MIPS** |

The load-store type is also called the register-register type: only load and store instructions access memory, and the operands of arithmetic instructions are all in registers. It has the longest code, but every instruction is simple, the format is regular, the **execution time** is predictable, and since registers are much faster than memory, the compiler can keep frequently used variables in registers. Almost all instruction sets designed after 1980 are of the load-store type. The stack type has the most compact code and is therefore still used as the **bytecode** of virtual machines (JVM, WebAssembly, CPython), which an **interpreter** or a just-in-time compiler translates into real machine instructions.

## 2.2. Instruction Formats

### 2.2.1. Instruction Length

**Definition 2.2.1 (Instruction Length and Word Size)** The complete binary representation of an instruction is called an instruction word, and the number of bits it contains is called the **instruction length**; the number of bits of binary data a computer can process directly at one time (usually the width of the general-purpose registers) is called the **word size**. The scheme that allocates the bits of the instruction word to the opcode and the address fields is called the **instruction format**.

The instruction length is usually a whole number of bytes, and may be shorter than, equal to or longer than the word size. According to whether all instructions have the same length, there are two kinds:

- Fixed-length instructions: all instructions have the same length. Fetching and decoding are simple, the address of the next instruction is easy to compute, and pipelining is easy; the drawback is that simple instructions occupy the same space, so programs are longer. For example, all base RISC-V instructions are 32 bits, and so are those of ARM's AArch64.
- Variable-length instructions: the length varies with the operation and the addressing mode. Programs are compact, but fetching and decoding are complex: without decoding the previous instruction, one does not know where the next begins. x86 instructions are 1 to 15 bytes long, and the PDP-11 has three lengths, 16, 32 and 48 bits.

A compromise is to use only a few lengths: the C extension of RISC-V adds 16-bit compressed instructions mixed with 32-bit ones ([4.10.3](/4.10.3#sec-3.8.8)), and ARM's Thumb-2 likewise mixes 16-bit and 32-bit instructions.

### 2.2.2. Opcode Encoding and Expansion

Opcodes can be organized in several ways:

- Fixed-length opcodes: a fixed number of bits at a fixed position in the instruction word represent the opcode, so decoding is simple and fast. For example, the opcode of the IBM 360 is always the first byte. A $k$-bit opcode can represent at most $2^k$ operations.
- Expanded opcodes: the length of the opcode varies with the number of address fields. Instructions that need fewer address fields can use the freed bits as an extension of the opcode. More instructions can then be represented without lengthening the instruction word, at the cost of somewhat more complex decoding.
- Interleaved opcode and address fields: the opcode is divided into a main opcode and an auxiliary opcode, and the auxiliary opcode is placed between address fields, as in the DJS-130 (NOVA). The `opcode` plus `funct3` and `funct7` of RISC-V follow the same idea ([4.10.3](/4.10.3#sec-3.8.1)).

**Example 2.2.1** A machine has a 16-bit instruction word consisting of a 4-bit basic opcode and three 4-bit address fields. If all instructions were three-address, a 4-bit opcode could represent only 16 instructions. To have 15 each of three-address, two-address and one-address instructions and 16 zero-address instructions, the opcode can be expanded as follows:

| Instruction type | Count | Opcode | Address fields |
|---|---|---|---|
| Three-address | 15 | `0000`–`1110` | Three 4-bit fields |
| Two-address | 15 | `1111 0000`–`1111 1110` | Two 4-bit fields |
| One-address | 15 | `1111 1111 0000`–`1111 1111 1110` | One 4-bit field |
| Zero-address | 16 | `1111 1111 1111 0000`–`1111 1111 1111 1111` | None |

At each level one code (`1111`) is reserved as the flag of expansion. More than one code may also be reserved: for example, if the three-address instructions use only the 14 codes `0000`–`1101`, leaving `1110` and `1111`, the two-address instructions have $2 \times 16 = 32$ opcodes available, of which 30 are taken (`1110 0000`–`1111 1101`), leaving `1111 1110` and `1111 1111`; the one-address instructions then have 32 available, of which 31 are taken (`1111 1110 0000`–`1111 1111 1110`); finally `1111 1111 1111` followed by 4 bits gives 16 zero-address instructions.

The rule of expansion is that no short opcode may be a prefix of a long one; otherwise the **decoder** cannot tell which bits to treat as the opcode. In other words, the set of all opcodes forms a **prefix code** ([4.3.5](/4.3.5)). This gives a criterion for whether an expansion is possible.

**Proposition 2.2.1** In the format of Example 2.2.1, there is an opcode expansion scheme that accommodates $N_3$ three-address, $N_2$ two-address, $N_1$ one-address and $N_0$ zero-address instructions if and only if

$$
N_3 \cdot 2^{12} + N_2 \cdot 2^{8} + N_1 \cdot 2^{4} + N_0 \le 2^{16}.
$$

**Proof** Necessity: an opcode of length $\ell$ is followed by $16 - \ell$ address bits, and occupies all the $2^{16-\ell}$ instruction words that have it as a prefix. No opcode is a prefix of another, so different opcodes occupy disjoint sets of instruction words, and the total does not exceed $2^{16}$. Sufficiency: allocate opcodes from short to long. First assign the 4-bit codes $0, 1, \dots, N_3 - 1$ to the three-address instructions; each of the remaining $16 - N_3$ 4-bit codes is extended by 4 bits, giving $(16 - N_3) \cdot 16$ 8-bit codes, from which $N_2$ are taken for the two-address instructions; continue in this way. The number of codes finally available for zero-address instructions is $((16 - N_3) \cdot 16 - N_2) \cdot 16 - N_1) \cdot 16 = 2^{16} - N_3 2^{12} - N_2 2^8 - N_1 2^4$, and the inequality says precisely that this is not less than $N_0$; it also guarantees that the remainder at each intermediate step is nonnegative. $\square$

This is exactly the Kraft inequality $\sum_i 2^{-\ell_i} \le 1$ for prefix codes, multiplied by $2^{16}$. Both schemes of Example 2.2.1 attain equality: $15 \cdot 4096 + 15 \cdot 256 + 15 \cdot 16 + 16 = 65536$ and $14 \cdot 4096 + 30 \cdot 256 + 31 \cdot 16 + 16 = 65536$, so the code space is used up entirely. If we require 15 three-address and 15 two-address instructions and no zero-address instructions, there can be at most $(65536 - 61440 - 3840)/16 = 16$ one-address instructions.

From the viewpoint of information theory, frequently used instructions should have short opcodes (similar to **Huffman coding**) to shorten programs, but this makes the opcode lengths very varied and decoding slower. Real instruction sets use only a few opcode lengths, a compromise between decoding speed and code density.

### 2.2.3. Two Examples of Instruction Formats

x86 is a typical variable-length format. An x86-64 instruction consists of the following parts in order, all of which except the opcode may be omitted:

| Part | Length | Purpose |
|---|---|---|
| Prefixes | 0–4 bytes (plus REX, VEX, EVEX and other prefixes) | Repetition, segment override, changing the length of operands or addresses; extending register numbers, vector length |
| Opcode | 1–3 bytes | The operation, sometimes also implying the operand size or a register number |
| ModR/M | 0–1 byte | The `Mod` and `R/M` fields indicate whether the operand is in a register or in memory and which addressing mode is used; the `Reg/Opcode` field is a register number or a 3-bit auxiliary opcode |
| SIB | 0–1 byte | For scaled indexed addressing, gives the scale factor (Scale), the index register (Index) and the base register (Base) |
| Displacement | 0, 1, 2 or 4 bytes | The constant part of the address |
| Immediate | 0, 1, 2 or 4 bytes (8 bytes for a few instructions) | The operand itself |

The total length of an instruction does not exceed 15 bytes; beyond that an illegal-instruction exception is raised. For example, the breakpoint instruction `int3` is the single byte `CC`; `mov eax, [rbx + rcx*4 + 8]` is encoded as `8B 44 8B 08` (opcode, ModR/M, SIB, 8-bit displacement); and `mov rax, 0x1122334455667788` needs 10 bytes (REX prefix, opcode and an 8-byte immediate). Depending on how one counts, x86 has from one thousand to over three thousand instructions, and the manual runs to more than five thousand pages.

RISC-V is a typical fixed-length format: the base instructions are all 32 bits, there are only six formats, R, I, S, B, U and J, the opcode is always in the lowest 7 bits, and the numbers of the source and destination registers are in the same positions in all formats. The processor can therefore read the registers while decoding, without knowing which instruction it is. The next chapter ([4.10.3](/4.10.3#sec-3.8)) gives the detailed definitions of the formats and examples of encoding.

## 2.3. Addressing Modes

**Definition 2.3.1 (Addressing Mode)** The method of determining the address of the operands of the current instruction and the address of the next instruction to execute is called the **addressing mode**. The address given in the instruction is called the formal address, and the actual address in memory of an operand computed according to the addressing mode is called the **effective address** (EA).

Addressing modes fall into two kinds, instruction addressing and operand addressing.

### 2.3.1. Instruction Addressing

The address of an instruction is given by the **PC**. In sequential execution the PC automatically increases by the length of the current instruction (4 for fixed-length 32-bit instructions). For a branch, the target address can be given in several ways: an absolute address given directly in the instruction; an offset relative to the current PC (PC-relative addressing, see below); or a register (register indirect branching, used for function returns, function pointers and `switch` jump tables). Conditional branches in modern instruction sets almost all use PC-relative addressing, because the targets of loops and branches are usually nearby, so the offset can be represented with few bits.

### 2.3.2. Operand Addressing

Let $A$ be the formal address (or constant) in the instruction, $R[r]$ the content of register number $r$, and $M[x]$ the content of the memory location at address $x$.

**Definition 2.3.2 (Basic Addressing Modes)** The common operand addressing modes are as follows.

- **Immediate addressing**: the operand is the constant $A$ given in the instruction.
- **Register addressing**: the operand is in the register specified by the instruction, namely $R[r]$.
- **Direct addressing**: the instruction gives the effective address of the operand, $\mathrm{EA} = A$, and the operand is $M[A]$.
- **Indirect addressing**: the instruction gives the address of the memory location that holds the effective address, $\mathrm{EA} = M[A]$.
- **Register indirect addressing**: the effective address is in a register, $\mathrm{EA} = R[r]$.
- **Indexed addressing**: the effective address is the content of the index register plus the formal address in the instruction, $\mathrm{EA} = R[\text{index}] + A$; what changes while the program runs is the index register.
- **Base addressing**: the effective address is the content of the base register plus the displacement in the instruction, $\mathrm{EA} = R[\text{base}] + D$; the base register gives the start of a block of memory and the displacement gives the position within the block.
- **PC-relative addressing**: the effective address is the value of the **program counter** plus the displacement in the instruction, $\mathrm{EA} = \mathrm{PC} + D$, where the displacement is in **two's complement** and may be positive or negative.
- **Stack addressing**: the operand is at the top of the stack, its address is given implicitly by the stack pointer SP, and SP is modified automatically as the access is made.

The modes are compared below. "Memory accesses" is the number of times memory must be accessed to obtain the operand (not counting the instruction fetch).

| Addressing mode | Operand | Memory accesses | Use | Counterpart in a C program |
|---|---|---|---|---|
| Immediate | $A$ | 0 | Constants | `x + 5` |
| Register | $R[r]$ | 0 | Frequently used variables | A **local variable** kept in a register |
| Direct | $M[A]$ | 1 | Data at a fixed address | A **global variable** (address fixed at link time) |
| Indirect | $M[M[A]]$ | 2 | Pointer kept in memory | `*p` for a global pointer `p` |
| Register indirect | $M[R[r]]$ | 1 | Pointer kept in a register | `*p` |
| Indexed | $M[R[\text{index}] + A]$ | 1 | Accessing an **array** in sequence | Global array `a[i]`, where $A$ is the address of `a` |
| Base | $M[R[\text{base}] + D]$ | 1 | Accessing data within a region | Structure member `p->f`; local variables on the stack |
| PC-relative | $M[\mathrm{PC} + D]$ or branch target $\mathrm{PC} + D$ | 1 or 0 | Branches; position-independent code | Jumps of `if` and loops |
| Stack | $M[\mathrm{SP}]$ | 1 | Subroutine calls, expression evaluation | The **stack frame** of a function |

Several remarks:

1. Immediate addressing obtains the operand when the instruction is fetched and is the fastest, but the number of bits of the constant is limited by the instruction format; larger constants must be assembled from several instructions or placed in memory.
2. The address field of direct addressing must hold an entire memory address, which is impossible in a 32-bit fixed-length instruction, so RISC instruction sets have no direct addressing. Indirect addressing needs an extra memory access, and modern instruction sets no longer provide it; a load fetches the pointer first instead.
3. Indexed and base addressing are both "register plus constant" in form; the difference is which part varies. In indexed addressing the constant (the start of an array) is fixed and the register (the subscript) varies; in base addressing the register (the start of a region) is fixed and the constant (the offset within the region) varies. Early machines used base registers to implement program relocation: the operating system could load a program anywhere in memory simply by setting the base register. In the English literature the two are often called displacement addressing together.
4. PC-relative addressing means that when a piece of code is moved as a whole to another address, the relative addresses in it need not be modified. This is the basis of the *position-independent code* that dynamic libraries require ([4.2.2](/4.2.2)).
5. The direction in which the stack grows and when SP is modified are specified by the instruction set. If the stack grows toward lower addresses and SP points to the top element, then with word addressing a push is $\mathrm{SP} - 1 \to \mathrm{SP}$ followed by writing $M[\mathrm{SP}]$, and a pop is reading $M[\mathrm{SP}]$ followed by $\mathrm{SP} + 1 \to \mathrm{SP}$; with byte addressing and a 4-byte word, add and subtract 4 instead.

There are also several composite modes: the PDP-11 and ARM provide auto-increment and auto-decrement addressing (the register is modified automatically after the access, which suits sequential access to arrays and the implementation of stacks); x86 provides scaled indexed addressing, whose effective address is

$$
\mathrm{EA} = R[\text{base}] + R[\text{index}] \times S + D, \qquad S \in \{1, 2, 4, 8\},
$$
where every part may be omitted, giving combinations such as direct, base, base plus displacement and scaled index plus displacement; x86-64 also adds addressing relative to the instruction pointer, `[rip + D]`.

### 2.3.3. Comparing the Two Styles

For the same array access `return a[i + 2];` (with `a` an `int *`), the compiled output of x86-64 and RISC-V (RV64) (GCC, `-O2`) is:

```asm
# x86-64: one instruction, base + index*4 + 8
mov  eax, DWORD PTR [rdi + rsi*4 + 8]
ret

# RISC-V RV64: address arithmetic is done by ordinary instructions
addi a1, a1, 2       # i + 2
slli a1, a1, 2       # (i + 2) * 4
add  a1, a0, a1      # a + (i + 2) * 4
lw   a0, 0(a1)       # load a[i + 2]
ret
```

RISC-V has only four addressing modes: immediate, register, base ("register plus a 12-bit displacement", used by load, store and `jalr`) and PC-relative (used by conditional branches, `jal` and `auipc`). All the others are composed from these: register indirect addressing is base addressing with displacement 0, and indexed addressing first computes the address with `slli` and `add`. There are more instructions, but each does only one simple thing, so the hardware can make them very fast, which is the subject of the next section.

## 2.4. CISC and RISC

### 2.4.1. History

In the 1960s and 1970s memory was expensive and slow, programming was mostly in **assembly language**, and compiler technology was immature. The designers' idea was to make instructions as powerful as possible: one instruction would perform a statement of a **high-level language**, or even a function, to shorten programs and narrow the "semantic gap". The means of implementing these complex instructions was the microprogrammed control introduced by the IBM 360: each machine instruction is interpreted by a microprogram in a control store, so adding instructions only requires adding microprograms (discussed in detail in later chapters on the control unit). The DEC VAX (1977) was the peak of this approach, with more than three hundred instructions, a dozen or so addressing modes, and even instructions for evaluating polynomials and manipulating queues.

In the late 1970s two changes shook this approach. The first was that Unix showed that even an operating system could be written in a high-level language, so the key question changed from "which instructions will assembly programmers use" to "which instructions will the compiler generate". The second was that measurements showed that complex instructions were rarely used: when IBM's John Cocke and colleagues made an experimental compiler generate only the simple register-register operations and load/store instructions of the IBM 360, programs became faster by up to a factor of three; measurements of the VAX found that 20% of the instructions used 60% of the microcode but accounted for only 0.2% of the **execution time**.

The opposite design thus appeared: the IBM 801 (Cocke, 1975–1980), Berkeley's RISC I (Patterson and Séquin, 1980–1982) and Stanford's MIPS (Hennessy, from 1981). They kept only simple, commonly used instructions, implemented them with hardwired logic rather than microprograms, and made them easy to pipeline. Commercial RISC processors such as SPARC, MIPS, PowerPC and ARM followed; Hennessy and Patterson received the 2017 Turing Award for this work.

### 2.4.2. Two Design Philosophies

**Definition 2.4.1 (CISC and RISC)** An instruction set that aims to shorten programs and reduce the instruction count with rich, powerful instructions and diverse addressing modes is called a **complex instruction set computer** (CISC); an instruction set that aims at a small number of simple instructions with a regular format that are easy to pipeline, and that accesses memory only with load/store instructions, is called a **reduced instruction set computer** (RISC).

| | CISC (e.g., x86, VAX) | RISC (e.g., RISC-V, ARM, MIPS) |
|---|---|---|
| Number of instructions | Many, including functionally complex ones | Few, only the common simple ones |
| Instruction length | Variable | Fixed (or a few lengths) |
| Instruction formats | Many and complex | Few and regular, with fields at fixed positions |
| Addressing modes | Many | Few, mainly "register plus displacement" |
| Memory access | Arithmetic instructions can access memory directly | Only load/store access memory (load-store type) |
| General-purpose registers | Fewer (x86-32 has only 8) | More (usually 32) |
| Cycles per instruction | Many and variable | Few and fairly uniform |
| Control unit | Mostly microprogrammed | Hardwired |
| Design emphasis | Complex functions in hardware | Compiler optimization; hardware does simple things well |

The "reduced" in RISC does not mean that fewer instructions are always better, but reflects several design principles: simplicity favors regularity (uniform formats, fixed field positions); smaller is faster (not too many registers, and 32 is a common compromise); make the common case fast (the most common cases, constants and relative branches, take the shortest path); and good design demands good compromises (for example, RISC-V has several formats to accommodate larger immediates, [4.10.3](/4.10.3#sec-3.8)).

### 2.4.3. Comparison by the Performance Equation

The trade-off between CISC and RISC can be explained quantitatively by the performance equation (1.1) ([4.10.1](/4.10.1#sec-1.4.2)):

$$
\frac{\text{Time}}{\text{Program}} = \frac{\text{Instructions}}{\text{Program}} \times \frac{\text{Clock cycles}}{\text{Instruction}} \times \frac{\text{Time}}{\text{Clock cycle}}.
$$

CISC reduces the first factor, and RISC lowers the second and third. Engineers at DEC compared the VAX and MIPS in similar technology and found that the VAX executed about 75% as many instructions as MIPS for a program, but its average number of cycles per instruction was five to six times that of MIPS. The two had similar **clock rates**, so

$$
\frac{T_{\mathrm{VAX}}}{T_{\mathrm{MIPS}}} \approx 0.75 \times 5.5 \approx 4,
$$
and the RISC processor was about 4 times as fast.

**Example 2.4.1** A program needs $10^9$ instructions on a RISC machine, with a **CPI** of 1.2 and a clock rate of 2 GHz; on a CISC machine it needs only $0.6 \times 10^9$ instructions, with a CPI of 3.0 and a clock rate of 2.5 GHz. By Eq. (1.1), the RISC machine takes $10^9 \times 1.2 / (2 \times 10^9) = 0.6\ \mathrm{s}$ and the CISC machine takes $0.6 \times 10^9 \times 3.0 / (2.5 \times 10^9) = 0.72\ \mathrm{s}$. The CISC machine has 40% fewer instructions and a 25% higher clock rate, yet is still 20% slower.

### 2.4.4. The Landscape Today

The CISC–RISC debate gradually lost its original meaning after the 1990s. Beginning with the Pentium Pro (1995), Intel processors decode x86 instructions internally into RISC-like micro-operations (micro-ops) and execute them with RISC techniques such as pipelining and out-of-order execution; the complexity of x86 is confined to the decoder, and as transistor counts grew its share of the cost became ever smaller. On the other hand, RISC instruction sets have gradually added instructions for multiplication and division, floating point, vectors, atomic operations and cryptography. Today the competition among instruction sets lies more in software ecosystem, licensing model and energy efficiency:

| Instruction set | Type | Main areas |
|---|---|---|
| x86-64 | CISC | Personal computers, servers |
| ARMv8-A / ARMv9-A (AArch64) | RISC | Phones, tablets, Apple's Macs, some servers |
| RISC-V | RISC | Embedded systems, microcontrollers, accelerators; entering servers and personal computers |
| MIPS, SPARC, PowerPC | RISC | Widely used in the past; MIPS (the company) turned to RISC-V in 2021 |

Both x86 and ARM are proprietary: using ARM requires a license fee, and x86 is essentially not licensed to others. RISC-V is an open standard that anyone may implement for free, which makes it the first choice for teaching, research and custom processors, and the labs of this course are based on it too.

## Summary

- An instruction is a command that the processor executes directly, and the **instruction set architecture** is the interface between software and hardware, which should be complete, regular, efficient and compatible. By function, instructions divide into arithmetic, shift, data transfer, control transfer, subroutine, input/output and system instructions.
- By the source of the operands of arithmetic instructions, instruction sets divide into stack, accumulator, register-memory and load-store types; almost all modern instruction sets are of the load-store type.
- The instruction format specifies how bits are allocated to the opcode and the address fields. Fixed-length instructions ease decoding and pipelining, and variable-length instructions give compact code. Opcode expansion extends the opcode with the bits freed by instructions with fewer address fields; all opcodes must form a **prefix code**, and the necessary and sufficient condition for feasibility is the Kraft inequality.
- Addressing modes give the address of an operand or of the next instruction: immediate, register, direct, indirect, register indirect, indexed, base, PC-relative and stack. RISC-V uses only four: immediate, register, base and PC-relative.
- CISC uses complex instructions to reduce the instruction count, while RISC uses simple, regular instructions to lower the CPI and the **clock cycle time**; in similar technology RISC is about 4 times as fast. Today x86 internally decodes instructions into RISC-like micro-operations, and the competition among instruction sets lies mainly in ecosystem and licensing; RISC-V is an open RISC standard.
