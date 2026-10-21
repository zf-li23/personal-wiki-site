---
title: Logic Gates and Their Electrical Characteristics
description: Classification, scale and packaging of integrated circuits; the switch model of the MOS transistor and the structure of the CMOS inverter, NAND, NOR and compound gates; voltage transfer characteristic, logic levels and noise margins, fan-in and fan-out, propagation delay, static and dynamic power; open-drain gates and wired-AND, tri-state gates and buses; TTL as a historical comparison.
source_hash: 83adb9774f99
---

The [previous chapter](/4.9.2) treated a logic gate as an ideal operation: as soon as an input changes, the output changes according to the **truth table**. A real gate is a circuit built from transistors: its output voltage represents $0$ and $1$ only within certain ranges, changes take time, the load it can drive is limited, and it consumes power. This chapter explains how gates are implemented and the external characteristics that a user must care about: voltage levels and noise margins decide whether gates can be cascaded reliably, fan-out and delay decide how fast a circuit can be, and power decides how large a chip can be. These characteristics are the physical origin of races and hazards in [Combinational Logic Circuits](/4.9.4) and of the timing parameters in [Latches and Flip-Flops](/4.9.6).

Today's digital integrated circuits almost all use CMOS technology, and this chapter follows CMOS as its main thread. Bipolar TTL was the mainstream from the 1960s to the 1980s; the 74-series numbering, the 5 V levels and concepts such as "totem-pole output" and "open collector" that it left behind are still in use, and the last section briefly describes it for comparison.

## 3.1. Integrated Circuits

### 3.1.1. Classification and Scale

Fabricating transistors, resistors and interconnects on a single piece of silicon with semiconductor technology gives an integrated circuit (IC). Digital integrated circuits can be classified from several viewpoints:

| Viewpoint | Categories |
|---|---|
| Technology | Bipolar (TTL, ECL); MOS (NMOS, PMOS, CMOS, BiCMOS) |
| Scale of integration | Small-scale SSI (a few gates, such as the quad 2-input **NAND gate** 74HC00), medium-scale MSI (tens to hundreds of gates, such as decoders and counters), large-scale LSI, very-large-scale VLSI (today's processors have tens of billions of transistors) |
| Design style | Standard logic devices (74 series), application-specific integrated circuits (ASICs), programmable devices (FPGAs, see [Programmable Logic and HDL](/4.9.9)) |

In 1965 Moore observed that the number of transistors on a single chip roughly doubled every year, and in 1975 he revised this to doubling every two years; this trend (Moore's law) has lasted for more than half a century. Until the mid-2000s, the supply voltage was scaled down along with the transistors, so the power per unit area stayed constant (Dennard scaling); after that the voltage could hardly be lowered further (the threshold voltage is limited by leakage), power and heat dissipation became the primary constraints of chip design, and processors turned to multiple cores and dedicated accelerators. The names of today's process nodes ("5 nm", "3 nm") no longer correspond to a physical dimension of the transistor but denote the density level of a process generation; the transistor structure has also evolved from the planar MOSFET to the FinFET and the gate-all-around (GAA) transistor, but the logical behavior as a switch is unchanged.

### 3.1.2. Packaging

A chip (die) must be mounted in a package to be used: the package holds and protects the die, connects the pads on the die to the external pins, and helps dissipate heat.

| Package | Features | Typical use |
|---|---|---|
| DIP (dual in-line) | Pin pitch 2.54 mm, inserted into through-holes of the circuit board | 74-series parts for teaching labs, early chips |
| SOIC, TSSOP (small outline) | Surface mount, pins on two sides | Today's 74-series logic devices |
| QFP (quad flat) | Pins on four sides, up to several hundred | Microcontrollers, small FPGAs |
| BGA (ball grid array) | Solder balls arranged in an array on the bottom of the package | Processors, FPGAs, memories |
| CSP, WLCSP (chip-scale package) | Package almost as large as the die | Chips in mobile phones |
| 2.5D / 3D packaging | Several dies (chiplets) interconnected side by side through a silicon interposer, or stacked vertically with through-silicon vias (TSVs) | High-end processors, GPUs and high-bandwidth memory (HBM) |

For example, a 74HC00 in a 14-pin package contains four independent 2-input NAND gates, with pin 14 connected to the supply $V_{\mathrm{CC}}$ and pin 7 to ground. The same part number can come in several packages such as DIP, SOIC and TSSOP, with the same function and pin numbering.

## 3.2. MOS Transistors and the CMOS Inverter

### 3.2.1. The Switch Model of the MOS Transistor

The MOS field-effect transistor (MOSFET) has three terminals: gate (G), source (S) and drain (D). The gate and the channel are separated by an insulating oxide layer, so in steady state the gate draws almost no current. Digital circuits use only its switching behavior:

| Type | Conduction condition | Good at passing | Symbol |
|---|---|---|---|
| nMOS | The gate-source voltage $V_{\mathrm{GS}}$ is above the threshold $V_{\mathrm{tn}} > 0$, that is, the gate is high | A strong $0$ (can pull the output to $0$) | No circle at the gate |
| pMOS | $V_{\mathrm{GS}}$ is below $V_{\mathrm{tp}} < 0$, that is, the gate is low | A strong $1$ (can pull the output to $V_{\mathrm{DD}}$) | Small circle at the gate |

When an nMOS transistor passes a high level, the output can reach at most $V_{\mathrm{DD}} - V_{\mathrm{tn}}$ (a weak $1$); likewise, when a pMOS transistor passes a low level, the output can fall only to $\lvert V_{\mathrm{tp}}\rvert$ (a weak $0$). CMOS gates therefore always connect pMOS transistors to the supply and nMOS transistors to ground.

### 3.2.2. CMOS Structure

**Definition 3.2.1 (CMOS Gate)** A gate in which a pull-up network of pMOS transistors connects the supply $V_{\mathrm{DD}}$ to the output, and a pull-down network of nMOS transistors connects the output to ground, with exactly one of the two networks conducting for any input, is called a complementary MOS (**CMOS**) gate.

![Transistor-level circuits of the CMOS inverter, the 2-input NAND gate and the 2-input NOR gate: pMOS transistors form the pull-up network and nMOS transistors form the pull-down network, and the two are duals of each other](./plots/cmos-gates.py)

The simplest CMOS gate is the inverter (NOT gate): the gates of one pMOS and one nMOS transistor are tied together as the input $A$, and their drains are tied together as the output $Y$. When $A = 0$ the pMOS conducts and the nMOS is off, so $Y$ is pulled up to $V_{\mathrm{DD}}$; when $A = 1$ the opposite happens and $Y$ is pulled to ground. Whether the input is $0$ or $1$, one transistor between the supply and ground is always off, so there is no DC path, and a CMOS gate consumes almost no power in the static state (when the input does not change). This is the fundamental reason that CMOS replaced TTL and NMOS.

### 3.2.3. The Voltage Transfer Characteristic

The curve of the output voltage as a function of the input voltage is called the voltage transfer characteristic (VTC).

![The voltage transfer characteristic of a CMOS inverter (square-law model, VDD = 1.8 V) and the supply current: current flows only when the input is between the two thresholds and both transistors conduct](./plots/inverter-vtc.py)

The curve has three segments: when the input is close to $0$ the output is $V_{\mathrm{DD}}$, when the input is close to $V_{\mathrm{DD}}$ the output is $0$, and in between is a steep transition region where both transistors conduct. The point where the output equals the input, $V_{\mathrm{M}}$, is called the switching threshold; when the two transistors are matched in strength, $V_{\mathrm{M}} \approx V_{\mathrm{DD}}/2$. The two points at which the slope of the curve is $-1$ are denoted $V_{\mathrm{IL}}$ and $V_{\mathrm{IH}}$: when the input is below $V_{\mathrm{IL}}$ or above $V_{\mathrm{IH}}$, small perturbations of the input are attenuated at the output; between the two, perturbations are amplified.

The gain in the transition region is much larger than $1$, which is the physical origin of the "regeneration" of digital circuits ([§1.1.2](/4.9.1#sec-1.1.2)): an input slightly off the standard levels gives an output closer to the standard levels after passing through one gate, so noise does not accumulate stage by stage.

## 3.3. CMOS Logic Gates

### 3.3.1. NAND, NOR and Compound Gates

The structures of the pull-up and pull-down networks are determined by series and parallel connections: switches in series conduct only when all of them conduct (AND), and switches in parallel conduct when any one conducts (OR).

- NAND gate: two nMOS transistors in series and two pMOS transistors in parallel. Only when $A = B = 1$ does the pull-down network conduct and $Y = 0$; otherwise at least one pMOS conducts and $Y = 1$. Hence $Y = \overline{AB}$.
- **NOR gate**: two nMOS transistors in parallel and two pMOS transistors in series, $Y = \overline{A + B}$.

In general, to design a CMOS gate $Y = \overline{G}$: implement $G$ with nMOS transistors (AND corresponds to series and OR to parallel) to get the pull-down network; dualize its series-parallel structure (swap series and parallel) and use pMOS transistors to get the pull-up network. For example, for the AND-OR-INVERT gate $Y = \overline{AB + CD}$, the pull-down network consists of two parallel branches, "$A$ and $B$ in series" and "$C$ and $D$ in series", and the pull-up network consists of two groups in series, "$A$ and $B$ in parallel" and "$C$ and $D$ in parallel", $8$ transistors in all.

Several design points follow:

- The output of a single-stage CMOS gate is always a monotonically decreasing function of the inputs (when an input goes from $0$ to $1$, it can only turn pMOS transistors off and nMOS transistors on). Hence AND and OR gates must be built as a NAND or NOR gate followed by an inverter, which takes two more transistors and one more stage of delay than the NAND or NOR gate.
- A NAND or NOR gate with $n$ inputs needs $2n$ transistors.
- The mobility of electrons in an nMOS channel is about $2$ times that of holes in a pMOS channel, so a pMOS transistor of the same size is weaker. In a NAND gate the series transistors are nMOS, whereas in a NOR gate they are the weaker pMOS, so for the same number of inputs a NAND gate is faster and smaller than a NOR gate, and CMOS designs prefer NAND gates.
- The more transistors in series, the larger the on-resistance and the slower the gate. In practical cell libraries NAND and NOR gates generally have no more than $4$ inputs, and wider AND and OR operations are built with multiple levels of gates.

### 3.3.2. Transmission Gates

Connecting an nMOS and a pMOS transistor in parallel, with their gates driven by the complementary control signals $C$ and $\overline{C}$, gives a transmission gate. When $C = 1$ both transistors conduct, the nMOS passes a strong $0$ and the pMOS passes a strong $1$, so any input level reaches the output without loss; when $C = 0$ both transistors are off and the input is disconnected from the output. A transmission gate is bidirectional, and is often used to build multiplexers and latches, implementing the selection function with fewer transistors.

## 3.4. External Characteristics of Gates

A datasheet describes the external behavior of a gate by a set of parameters, from which the user judges whether gates can be cascaded correctly, how fast the circuit can be, and how large a power supply is needed.

### 3.4.1. Logic Levels and Noise Margins

The datasheet gives four guaranteed values for each gate:

| Parameter | Meaning |
|---|---|
| $V_{\mathrm{OH(min)}}$ | Minimum output high level: when the output is $1$, the voltage is guaranteed to be no lower than this |
| $V_{\mathrm{OL(max)}}$ | Maximum output low level: when the output is $0$, the voltage is guaranteed to be no higher than this |
| $V_{\mathrm{IH(min)}}$ | Minimum input high level: an input voltage no lower than this is guaranteed to be recognized as $1$ |
| $V_{\mathrm{IL(max)}}$ | Maximum input low level: an input voltage no higher than this is guaranteed to be recognized as $0$ |

Gates can be cascaded correctly provided $V_{\mathrm{OH(min)}} > V_{\mathrm{IH(min)}}$ and $V_{\mathrm{OL(max)}} < V_{\mathrm{IL(max)}}$, and the margins by which they hold are the noise allowed to be superimposed on the wire.

**Definition 3.4.1 (Noise Margin)** When a gate drives gates of the same family, the high-level and low-level **noise margins** are

$$
\mathrm{NM_H} = V_{\mathrm{OH(min)}} - V_{\mathrm{IH(min)}},\qquad \mathrm{NM_L} = V_{\mathrm{IL(max)}} - V_{\mathrm{OL(max)}},
$$
that is, the maximum noise voltage that can be superimposed on the signal without causing the next stage to misjudge it.

**Example 3.4.1** Typical datasheet values of several families (in V):

| Family | Supply | $V_{\mathrm{OH(min)}}$ | $V_{\mathrm{OL(max)}}$ | $V_{\mathrm{IH(min)}}$ | $V_{\mathrm{IL(max)}}$ | $\mathrm{NM_H}$ | $\mathrm{NM_L}$ |
|---|---|---|---|---|---|---|---|
| 74 (standard TTL) | 5 | 2.4 | 0.4 | 2.0 | 0.8 | 0.4 | 0.4 |
| 74HC (CMOS) | 4.5 | 4.4 | 0.1 | 3.15 | 1.35 | 1.25 | 1.25 |
| 74HCT (CMOS, TTL-compatible inputs) | 4.5 | 4.4 | 0.1 | 2.0 | 0.8 | 2.4 | 0.7 |

The output values of 74HC are the guaranteed values under light load ($20\,\mu\mathrm{A}$); at a load current of $4\,\mathrm{mA}$, $V_{\mathrm{OH(min)}}$ drops to $3.98$ and $V_{\mathrm{OL(max)}}$ rises to $0.26$, and the noise margins shrink accordingly. The outputs of CMOS can almost reach the supply and ground, so its noise margins are much larger than those of TTL.

When families are mixed, the values must be compared item by item: the $V_{\mathrm{OH(min)}} = 2.4\,\mathrm{V}$ of a TTL output is lower than the $V_{\mathrm{IH(min)}} = 3.15\,\mathrm{V}$ of 74HC, so TTL cannot drive 74HC reliably; 74HCT changes the input thresholds to TTL levels and is designed for exactly this interface. A common problem today is the interface between different supply voltages (for example a $3.3\,\mathrm{V}$ microcontroller and a $1.8\,\mathrm{V}$ sensor), which requires level-shifting devices.

### 3.4.2. Fan-In and Fan-Out

**Definition 3.4.2 (Fan-In and Fan-Out)** The number of inputs of a gate is called its fan-in; the number of inputs of gates of the same kind that the output of a gate can drive while still meeting the level specifications is called its **fan-out**.

Fan-out is limited in two ways:

- DC fan-out: when the output is high it must supply input current to each load, and when the output is low it must sink the input current of each load,

  $$
  N = \min\left(\frac{\lvert I_{\mathrm{OH}}\rvert}{I_{\mathrm{IH}}},\ \frac{I_{\mathrm{OL}}}{\lvert I_{\mathrm{IL}}\rvert}\right).
  $$
  For standard TTL, $I_{\mathrm{OH}} = 0.4\,\mathrm{mA}$, $I_{\mathrm{IH}} = 40\,\mu\mathrm{A}$, $I_{\mathrm{OL}} = 16\,\mathrm{mA}$ and $I_{\mathrm{IL}} = 1.6\,\mathrm{mA}$; both ratios are $10$, so the fan-out is $10$. Beyond the fan-out, the output low level rises and the high level falls, possibly into the forbidden zone, and the whole circuit fails.
- AC fan-out: the input of a CMOS gate is the gate terminal of a MOS transistor, and the DC input current is only leakage (no more than $1\,\mu\mathrm{A}$ for 74HC), so the DC fan-out calculation gives several thousand; but each input is a capacitor of a few pF, and the more loads, the slower the output charges and discharges. The fan-out of a CMOS circuit is therefore determined by the allowed delay rather than by the DC current.

### 3.4.3. Propagation Delay

![Propagation delay of an inverter driving a capacitive load: measured between the 50% points of input and output; pull-up and pull-down strengths differ, so t_PHL and t_PLH are not equal](./plots/propagation-delay.py)

**Definition 3.4.3 (Propagation Delay)** The time from a change at the input to the corresponding change at the output, referenced to the $50\%$ points of the voltage swings: the delay of the output going from high to low is denoted $t_{\mathrm{PHL}}$ and the delay of the output going from low to high is denoted $t_{\mathrm{PLH}}$ (named after the direction of the output change); the **propagation delay** of a gate is the average of the two, $t_{\mathrm{pd}} = (t_{\mathrm{PHL}} + t_{\mathrm{PLH}})/2$.

Another set of parameters is the rise time and fall time: the time for the output to change between $10\%$ and $90\%$ of the swing. Datasheets also give the minimum delay $t_{\mathrm{cd}}$ (contamination delay), the earliest time at which the output starts to change after an input change; the maximum delay determines the maximum speed of a circuit, and the minimum delay is needed when analyzing the hold time of flip-flops ([Latches and Flip-Flops](/4.9.6)).

The source of delay is charging and discharging the load capacitance. Approximating a conducting transistor by a resistance $R$, with load capacitance $C_L$ (the sum of the input capacitance of the next stage and the wire capacitance), the output changes as $\mathrm{e}^{-t/(RC_L)}$, and the time to reach the $50\%$ point is

$$
t_{\mathrm{pd}} \approx \ln 2 \cdot RC_L \approx 0.69\,RC_L .
$$
The delay therefore increases linearly with fan-out (load capacitance). Increasing the transistor size reduces $R$ but also increases the load capacitance it presents to the preceding stage. The total delay of a combinational circuit is the sum of the gate delays along the longest path from input to output, and this path is called the critical path.

**Example 3.4.2 (Ring Oscillator)** Connecting an odd number $N$ of inverters head to tail gives a circuit with no stable state, which oscillates by itself: a transition takes $N t_{\mathrm{pd}}$ to go once around the ring, and the output flips twice in one period, so the oscillation period is $T = 2N t_{\mathrm{pd}}$. Measuring $T$ gives the average delay of a single gate, which is the standard method by which semiconductor manufacturers evaluate process speed. It is not a "perpetual motion machine": the energy of the oscillation comes from the supply, and every flip consumes power in charging and discharging capacitances.

Typical gate delays: about $100\,\mathrm{ns}$ for 4000-series CMOS ($5\,\mathrm{V}$), about $10\,\mathrm{ns}$ for standard TTL and 74HC, and about $4\,\mathrm{ns}$ for 74LVC; these all include the time to drive the chip pins and external loads (tens of pF). A gate inside a chip drives only a load of a few fF, and in advanced processes the delay of one gate is only about $10\,\mathrm{ps}$.

### 3.4.4. Power Dissipation

The power dissipation of a CMOS circuit has three components:

1. Dynamic power: when the output goes from $0$ to $1$, the supply charges the load capacitance $C_L$ through the pull-up network and delivers the energy $C_LV_{\mathrm{DD}}^2$, of which half is stored in the capacitor and half is dissipated in the resistance of the pull-up network; when the output goes from $1$ to $0$, the stored half is dissipated in the pull-down network. Each complete $0 \to 1 \to 0$ transition therefore dissipates $C_LV_{\mathrm{DD}}^2$. If the clock frequency is $f$ and the probability of a $0 \to 1$ transition in each cycle (the activity factor) is $\alpha$, then

   $$
   P_{\mathrm{dyn}} = \alpha\, C_L V_{\mathrm{DD}}^2 f .
   $$
2. Short-circuit power: while the input passes through the transition region, both transistors conduct, and a brief current flows directly from the supply to ground (the right side of the VTC figure); the slower the input edge, the larger this component.
3. Static power: a transistor that is off does not conduct completely: there are subthreshold leakage current and gate leakage current. In advanced processes, leakage power can account for a considerable fraction of the total power.

**Example 3.4.3** Suppose that on average a total equivalent capacitance of $C = 10\,\mathrm{nF}$ flips in each cycle of a chip (the sum of $\alpha C_L$), $V_{\mathrm{DD}} = 0.8\,\mathrm{V}$ and $f = 3\,\mathrm{GHz}$. Then $P_{\mathrm{dyn}} = 10^{-8}\times0.64\times3\times10^9 \approx 19\,\mathrm{W}$. If the voltage drops to $0.7\,\mathrm{V}$, the power falls to $(0.7/0.8)^2 \approx 77\%$ of the original.

Dynamic power is proportional to $V_{\mathrm{DD}}^2$, so lowering the voltage is the most effective way to save energy, but a lower voltage makes the transistors slower. The low-power techniques of modern chips all start from this formula: dynamic voltage and frequency scaling (DVFS) lowers both $V_{\mathrm{DD}}$ and $f$ under light load; clock gating stops idle modules from toggling ($\alpha = 0$); and power gating cuts off the supply of idle modules to eliminate leakage.

## 3.5. Special Output Structures

### 3.5.1. Outputs Cannot Be Connected Directly

The output stage of an ordinary CMOS gate is a push-pull structure: either the pull-up or the pull-down conducts. If the outputs of two gates are tied together and one outputs $1$ while the other outputs $0$, a low-resistance path forms from the supply through two conducting transistors to ground; the current is large, the output level falls into the forbidden zone, and the transistors may be damaged by overheating. This is called bus contention. Computers, however, often need several devices to share one wire (interrupt request lines, data buses), and two special output structures exist for this purpose.

### 3.5.2. Open-Drain Gates and Wired-AND

Removing the pull-up network from the output stage of a CMOS gate, keeping only the pull-down nMOS transistor and bringing out its drain directly, gives an open-drain (OD) gate: it can only pull the output low or leave the output floating. In use, a pull-up resistor $R$ to the supply is connected externally to the output line.

![Two ways of sharing one wire: open-drain outputs with a pull-up resistor form a wired-AND; tri-state buffers hang on a bus with at most one enabled at a time](./plots/open-drain-tristate.py)

When several open-drain outputs are connected to the same wire, the wire is low as long as any pull-down transistor conducts; when all are off, the pull-up resistor pulls the wire high. The logic of the wire is the AND of the gate outputs, called wired-AND: the connection itself performs an AND gate, needs no extra gate, and produces no contention current.

The pull-up resistor value has a lower and an upper limit:

- Lower limit: when only one of the gates outputs low, it has to sink the current through $R$ and the input currents of all loads, which must not exceed $I_{\mathrm{OL(max)}}$, so $R \ge (V_{\mathrm{DD}} - V_{\mathrm{OL(max)}})/(I_{\mathrm{OL(max)}} - \sum I_{\mathrm{IL}})$.
- Upper limit: when all outputs are off, the leakage currents and the load input currents flowing through $R$ cause a voltage drop, and the high level must not fall below $V_{\mathrm{IH(min)}}$; more importantly, the rising edge depends on $R$ charging the capacitance $C$ on the line with time constant $RC$, so the larger $R$ is, the slower the rise.

The rising edge of an open-drain output is therefore much slower than that of a push-pull output, and open-drain is suitable only where speed is not high. Typical applications are: interrupt request lines and reset lines shared by several devices; the I²C bus (both the clock and data lines are open-drain, and any device can pull the line low, which makes arbitration possible); level translation between different supply voltages (the pull-up resistor is connected to the supply of the receiver); and driving loads such as LEDs and relays. The corresponding structure in TTL is called an open-collector (OC) gate.

### 3.5.3. Tri-State Gates

**Definition 3.5.1 (Tri-State Gate)** A gate that, besides outputting $0$ and $1$, can turn off both the pull-up and pull-down networks through an enable signal $\mathit{EN}$ so that the output is in the high-impedance state (denoted $Z$, equivalent to being disconnected from the circuit) is called a **tri-state buffer**.

The function table of a tri-state buffer (active-high enable):

| $\mathit{EN}$ | $A$ | $Y$ |
|---|---|---|
| 0 | × | $Z$ |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

A tri-state buffer keeps the speed of a push-pull output and also allows several outputs to hang on one bus: at any time only one tri-state buffer is enabled and drives the bus, and all the others are in the high-impedance state. When the driver is changed, the old buffer should first go to the high-impedance state and then the new one should be enabled (break before make); otherwise the two briefly drive the bus at the same time and produce a contention current. Connecting two tri-state buffers of opposite directions and using a direction control signal to select which one is enabled gives a bidirectional bus transceiver (such as the 74HC245), which is how the data bus of a traditional processor is interfaced.

In a hardware description language, a tri-state output is written as a conditional assignment of the high-impedance value:

```systemverilog
module tristate_buf (
    input  logic en,
    input  logic a,
    output tri   y
);
    assign y = en ? a : 1'bz;   // high impedance when disabled
endmodule
```

Today, chip interiors and FPGA interiors no longer use tri-state buses but select the driver with a multiplexer ([Combinational Logic Circuits](/4.9.4)): a multiplexer structure has neither contention nor floating lines, and is easier for timing analysis. Tri-state gates are now used mainly at the bidirectional I/O pins of chips.

## 3.6. A Brief Look at TTL

TTL (transistor–transistor logic) is built from bipolar transistors, and the 7400 series introduced by Texas Instruments in the 1960s became the industry standard. The classic TTL NAND gate consists of five transistors:

- the input stage is a multi-emitter transistor; when any input is low, it draws current away from the next stage, which performs the AND function;
- the middle stage is a phase splitter;
- the output stage is a push-pull structure of two transistors stacked one above the other, called a totem-pole output: when the output is high the upper transistor conducts and the lower is off, and when the output is low the reverse holds.

Transistors operate in two states, saturation and cutoff, and leaving saturation requires removing the stored charge in the base region, which limits the speed; later families such as 74LS (low-power Schottky), 74F and 74AS use Schottky diodes to prevent deep saturation and raise the speed. A comparison of TTL and CMOS:

| | Standard TTL (74) | CMOS (74HC and the interior of integrated circuits) |
|---|---|---|
| Supply | $5\,\mathrm{V}$ | $5\,\mathrm{V}$ down to below $1\,\mathrm{V}$ |
| Input | Sources $1.6\,\mathrm{mA}$ when low, which the driving stage must sink | A gate terminal, only leakage current |
| Output levels | High level about $3.4\,\mathrm{V}$, cannot reach the supply | Almost reaches the supply and ground |
| Noise margin | $0.4\,\mathrm{V}$ | About $0.3V_{\mathrm{DD}}$ |
| Static power | About $10\,\mathrm{mW}$ per gate | Close to $0$ (leakage only) |
| Integration density | Low (needs resistors, large transistors) | High (no resistors needed) |

Static power is the decisive difference: a chip made of hundreds of millions of gates could not dissipate its heat at all if each gate consumed milliwatts of static power. CMOS has therefore been the only mainstream technology for digital integrated circuits since the 1980s. Almost all 74-series logic devices on the market today are also CMOS (74HC, 74HCT, 74LVC, 74AUC and so on), merely keeping the numbering and pinout of the TTL era: the 74HC00, like the 7400, is a quad 2-input NAND gate.

## Summary

| Topic | Key points |
|---|---|
| CMOS structure | pMOS pull-up, nMOS pull-down, duals of each other; in a NAND gate the nMOS transistors are in series, in a NOR gate the pMOS transistors are in series; a single-stage gate necessarily inverts |
| Voltage transfer characteristic | Three segments with high gain in the middle; $V_{\mathrm{IL}}$ and $V_{\mathrm{IH}}$ are the points of slope $-1$; high gain makes signals regenerative |
| Noise margin | $\mathrm{NM_H} = V_{\mathrm{OH}} - V_{\mathrm{IH}}$, $\mathrm{NM_L} = V_{\mathrm{IL}} - V_{\mathrm{OL}}$; compare item by item when mixing families |
| Fan-out | Set by DC current for TTL ($10$); set by load capacitance and allowed delay for CMOS |
| Propagation delay | Measured between 50% points; $t_{\mathrm{pd}} \approx 0.69RC_L$, increasing with load; ring oscillator $T = 2Nt_{\mathrm{pd}}$ |
| Power | $P = \alpha C V_{\mathrm{DD}}^2 f$ + short-circuit + leakage; lowering the voltage is the most effective |
| Special outputs | Push-pull outputs cannot be tied together; open-drain with a pull-up resistor gives wired-AND; tri-state gates are used on buses, break before make when switching |
| TTL | Bipolar, totem-pole output, $5\,\mathrm{V}$; replaced by CMOS because of static power, with the 74 numbering still in use |
