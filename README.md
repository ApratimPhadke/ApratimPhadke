<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0D0D0D&height=4&section=header"/>

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║  BOOT LOG :: VIIT-ENTC-2027 :: ARM-CORTEX-M → RISCV → LINUX → RTL → GDS       ║
║  [ CPU: CORTEX-A ]  [ MEM: 8.36 CGPA ]  [ IRQ: ALWAYS ON ]  [ STATUS: ACTIVE ] ║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

# `APRATIM PHADKE`
### Embedded Systems Engineer · VLSI Designer · Processor Architect

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=18&duration=2500&pause=800&color=00FF88&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=60&lines=%24+probe+--target+apratim+--depth+full;%3E+RTL+%7C+Embedded+Linux+%7C+Processor+Arch+%7C+FPGA+%7C+Bare-Metal+C)](https://git.io/typing-svg)

<br>

[![LinkedIn](https://img.shields.io/badge/─────────────────────────────────────────────-0D0D0D?style=for-the-badge)]()

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Apratim_Phadke-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/apratim-phadke-966816223/)
[![Email](https://img.shields.io/badge/Email-apratimphadkeprime%40gmail.com-EA4335?style=flat-square&logo=gmail)](mailto:apratimphadkeprime@gmail.com)
[![IEEE](https://img.shields.io/badge/IEEE-General_Manager_VIIT-00629B?style=flat-square&logo=ieee)](https://ieee.org)

</div>

---

## `> whoami`

```verilog
module apratim_phadke #(
    parameter INSTITUTION = "VIIT Pune — B.Tech ENTC — 2023→2027",
    parameter CGPA        = 8.36,   // Till 5th Sem
    parameter ROLE        = "IEEE VIIT Student Branch — General Manager",
    parameter DOMAIN      = "Embedded Linux | VLSI | RTL | Computer Architecture"
)(
    input  wire        curiosity,
    input  wire        hardware_instinct,
    output reg  [63:0] production_systems,
    output reg         papers_in_prep
);

localparam STACK = "Transistors → RTL → Firmware → Linux Userspace";

always @(posedge clk) begin
    if (curiosity & hardware_instinct) begin
        production_systems <= build_debug_iterate();
        papers_in_prep     <= 1'b1;            // RONAN — VIIT Pune 2026
    end
end

endmodule
```

I live at the intersection of **silicon and software** — equally comfortable writing SystemVerilog that hits timing closure and debugging a kernel-layer SoC bottleneck with GDB. I care about the full stack: from register-level bare-metal C on ARM Cortex-M, through embedded Linux user/kernel space, up to RTL design and physical implementation with OpenROAD + Sky130. Engineering isn't a career path to me — it's how I think.

---

## `> cat /proc/skills`

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TECHNICAL CAPABILITY REGISTER                       │
├──────────────────────────────────┬──────────────────────────────────────────┤
│  DOMAIN                          │  STACK                                   │
├──────────────────────────────────┼──────────────────────────────────────────┤
│  RTL & HDL                       │  SystemVerilog · Verilog · VHDL          │
│  EDA / Physical Design           │  OpenROAD · Yosys · Magic · KLayout      │
│  FPGA                            │  Xilinx Vivado · Quartus · Vicharak      │
│  Embedded Linux                  │  User-space · Kernel-space · GDB · GStr  │
│  Bare-Metal Firmware             │  STM32 (F1/F4/L0/C0) · ARM Cortex-M     │
│  Processor Arch                  │  RISC-V ISA · Pipeline · Branch Pred.    │
│  Programming                     │  C · C++ · Python · Assembly · TCL       │
│  Verification                    │  Cocotb · Verilator · GTKWave            │
│  Protocols                       │  UART · SPI · I2C · APB · CAN · ONVIF   │
│  Build & Debug                   │  GDB · GDB · Make · Linker Scripts · ELF │
│  Simulation                      │  MATLAB/Simulink · Simscape · ModelSim   │
└──────────────────────────────────┴──────────────────────────────────────────┘
```

</div>

### Hardware Arsenal

**RTL & VLSI**
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-★★★★★-FF6B35?style=flat-square)
![Verilog](https://img.shields.io/badge/Verilog-★★★★★-FF6B35?style=flat-square)
![OpenROAD](https://img.shields.io/badge/OpenROAD-★★★★☆-FF9800?style=flat-square)
![Yosys](https://img.shields.io/badge/Yosys-★★★★☆-FF9800?style=flat-square)
![Magic VLSI](https://img.shields.io/badge/Magic_VLSI-★★★★☆-FF9800?style=flat-square)
![Xilinx Vivado](https://img.shields.io/badge/Vivado-★★★★☆-E31837?style=flat-square)

**Embedded & Systems**
![C](https://img.shields.io/badge/C_Bare_Metal-★★★★★-00D9FF?style=flat-square)
![STM32](https://img.shields.io/badge/STM32-★★★★★-03234B?style=flat-square)
![Embedded Linux](https://img.shields.io/badge/Embedded_Linux-★★★★☆-FCC624?style=flat-square)
![GDB](https://img.shields.io/badge/GDB-★★★★☆-A31515?style=flat-square)
![Python](https://img.shields.io/badge/Python-★★★★☆-3776AB?style=flat-square)
![RISC-V](https://img.shields.io/badge/RISC--V_Assembly-★★★★☆-283272?style=flat-square)

---

## `> ls -la ~/experience/`

### 🏭 Industry Sponsored Project — IFM Electronic
**`Embedded Linux Platform Validation & Systems Software`**
`CODESYS · Python · Shell Scripting · ONVIF · GDB · GStreamer · Plotly/Dash`

```
[PLATFORM]  ifm CR1204 HMI — aarch64 — resource-constrained embedded Linux SoC
[MISSION]   Define production operating envelope via systematic KPI profiling
```

- Deployed and profiled a camera streaming stack, instrumenting **CPU utilization, memory footprint, data throughput, and sustained FPS** across a codec×resolution matrix — results became production deployment parameters
- Designed a closed-loop **Adaptive Bitrate (ABR) controller** in CODESYS, interfacing via ONVIF protocol; modular function blocks for stream management, KPI overlay, and resource monitoring on a constrained runtime
- Multi-layer **hardware-software co-debug** across firmware, CODESYS runtime, and Linux kernel to isolate SoC bottlenecks using GDB and shell diagnostics
- Automated the full validation pipeline end-to-end; shipped a **real-time Plotly/Dash performance dashboard** to surface bottlenecks and define platform performance envelopes

---

## `> ls -la ~/projects/`

### ⚡ RONAN — Neural Network-Inspired Pipelined RISC-V Processor
`SystemVerilog · Cocotb · Verilator · Python`

```
 METRIC              BASELINE          RONAN (Neural)     RONAN (Hybrid)
 ─────────────────────────────────────────────────────────────────────────
 Branch Pred. Acc.   Static / ~50%     99.89%             95.62% post-warmup
 IPC                 0.508             0.999              —
 Predictor           None              Perceptron         TAGE(40.1%) + Perceptron(59.9%)
 GHR Width           —                 48-bit             48-bit
 Workloads           —                 5 patterns         8 structured
```

- Designed a **quad-core RISC-V processor** in SystemVerilog with perceptron-based dynamic branch prediction — validated across alternating, pointer-chase, loop-exit, and bimodal workloads
- Implemented a **hybrid TAGE+Perceptron predictor**: TAGE covers structured patterns, perceptron captures long-history correlations — architecture analogous to branch prediction units in production GPU compiler backends
- Built **parameterized Cocotb/Verilator testbenches** for perceptron table, GHR, and jog-packet unit — full RTL verification methodology from stimulus to scoreboard

> 📄 *A. Phadke et al., "RONAN: A Neural Network-Inspired Pipelined RISC-V Processor with Perceptron-Based Branch Prediction," manuscript in preparation, VIIT Pune, 2026.*

---

### 🔧 MCU Visualizer — Custom ELF-Based Firmware Debug Toolchain
`C · Qt · Python · Arduino · ESP32`

```c
// What GDB doesn't show you — live firmware introspection, on-target
struct elf_inspector {
    section_t  regions[];    // .text / .data / .bss / stack / heap
    reg_file_t register_state;
    insn_t     active_instruction;
    bool       bare_metal;   // No library dependency. Pure C ELF parser.
};
```

- Built an autonomous embedded robot on **Arduino UNO + ESP32** with real-time motor and sensor control over a custom wireless communication protocol — full hardware-software stack ownership
- Developed **MCU Visualizer**: real-time ELF binary parsing to decode active instructions, map memory regions, and visualize register state on-target — directly applicable to BSP bringup and post-silicon debug
- Implemented the **ELF parsing engine in bare-metal C** (zero library dependency); migrated full GUI toolchain to **C + Qt** for live firmware introspection, memory analysis, and on-target optimization

---

## `> cat ~/publications.bib`

```bibtex
@article{phadke2026ronan,
  author    = {Phadke, Apratim and others},
  title     = {RONAN: A Neural Network-Inspired Pipelined RISC-V Processor
               with Perceptron-Based Branch Prediction},
  journal   = {Manuscript in Preparation},
  year      = {2026},
  institute = {VIIT Pune},
  status    = {in-prep}
}
```

---

## `> cat ~/certifications.txt`

```
[2025]  Introduction to Microprocessors — ARM
[2025]  Using Git for Distributed Development — The Linux Foundation
```

---

## `> cat ~/interests.conf`

```ini
[hardware]
passion         = "Understanding every abstraction layer — transistor to OS"
current_obsess  = RISC-V microarchitecture, TAGE branch predictors, OpenROAD flows
deep_curiosity  = Compiler-hardware co-design, neuromorphic architectures, FPGA overlays

[software]
approach        = "If I can't debug it at the register level, I don't trust it"
tools_of_choice = GDB, Verilator, bare-metal C, shell scripting, linker scripts

[philosophy]
build_style     = "Build it. Break it. Instrument it. Fix it. Document it."
what_drives_me  = The moment simulation waveforms match silicon behaviour
mantra          = "Hardware is truth. Everything else is abstraction."
```

---

## `> iostat github`

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=ApratimPhadke&show_icons=true&theme=chartreuse-dark&hide_border=true&include_all_commits=true&count_private=true&custom_title=Commit+Register" />
<img width="49%" src="https://github-readme-streak-stats.herokuapp.com/?user=ApratimPhadke&theme=chartreuse-dark&hide_border=true&fire=FF6B35&ring=00FF88&currStreakLabel=00FF88" />

<img width="98%" src="https://github-readme-activity-graph.vercel.app/graph?username=ApratimPhadke&theme=chartreuse-dark&hide_border=true&area=true&custom_title=Activity+Trace" />

</div>

---

## `> dmesg | tail`

```
[  0.000001] Apratim Phadke initialised — VIIT Pune, ENTC
[  0.000042] Loaded: Computer Architecture, ISA Design, Compiler Infrastructure
[  0.000089] Loaded: Processor Microarchitecture, Systems Programming
[  0.000134] Loaded: Embedded Linux (user + kernel), FPGA, Bare-Metal STM32
[  0.000201] Loaded: RTL Design, Physical Implementation, OpenROAD, Sky130 PDK
[  0.000267] IFM Electronic — industry project — platform validation COMPLETE
[  0.000334] RONAN v2 — hybrid TAGE+Perceptron — 95.62% acc — paper in prep
[  0.000401] MCU Visualizer — ELF parser — bare-metal C — Qt GUI — shipped
[  0.000468] IEEE VIIT GM — ICBDS 2024 coordinated — workshops delivered
[  0.000512] STATUS: kernel panic? No. Actively building. IRQ pending.
```

---

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════╗
║         "If it doesn't run on bare metal, it isn't real yet."           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/apratim-phadke-966816223/)
[![Email](https://img.shields.io/badge/Email-Reach_Out-EA4335?style=for-the-badge&logo=gmail)](mailto:apratimphadkeprime@gmail.com)

[![Profile Views](https://komarev.com/ghpvc/?username=ApratimPhadke&color=00FF88&style=flat-square&label=profile+probes)](https://github.com/ApratimPhadke)

<img src="https://capsule-render.vercel.app/api?type=rect&color=0D0D0D&height=4&section=footer"/>

</div>
