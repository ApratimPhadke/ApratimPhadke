<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Apratim%20Phadke&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=38&desc=Embedded%20Systems%20%7C%20RTL%20Design%20%7C%20Embedded%20Linux&descAlignY=60&descSize=18"/>
</div>

<div align="center">
  
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=600&lines=Embedded+Systems+Engineer;RTL+%2B+SoC+Design;RISC-V+Microarchitecture;Bare-Metal+C+%7C+Embedded+Linux;Firmware+to+Hardware+Validation)](https://git.io/typing-svg)

</div>

<!-- <a href="https://komarev.com/ghpvc/?username=gmostofabd">
  <img align="right" src="https://komarev.com/ghpvc/?username=gmostofabd&label=ProfileViews&color=0e75b6&style=flat" alt="Profile visitor" />
</a>  -->

![MK_51S_Simu_1](https://github.com/user-attachments/assets/cb24ba0b-56c8-432a-b949-bd34c3f8d6af)

<hr/>

<img align="right" alt="Hardware Hacker" width="380" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif"/>



### 🧠 About Me

```yaml
name: Apratim Phadke
based_in: Pune, India 🇮🇳
university: VIIT Pune — B.Tech ENTC
cgpa: 8.36 / 10

focus_areas:
  - Embedded Systems
  - RTL & SoC Design
  - RISC-V Microarchitecture
  - Embedded Linux
  - Bare-Metal Firmware

currently:
  building: RONAN — RISC-V Processor Research Project
  learning: Advanced Microarchitecture
  leading: IEEE VIIT Student Branch (GM)

interests:
  - STM32 firmware development
  - RISC-V processor implementation
  - Linux systems on constrained hardware
  - FPGA-based digital design
````

<br clear="right"/>

---

## ⚡ Engineering Focus

<div align="center">

|       🔬 Architecture & RTL       |   🛠️ Firmware & Systems   |      🧪 Debug & Validation      |
| :-------------------------------: | :------------------------: | :-----------------------------: |
|  RISC-V processor implementation  | Bare-metal UART bootloader |    DRM master lock debugging    |
| Branch prediction experimentation |    ELF parser in pure C    | Network debugging using tcpdump |
|     APB-based FPGA SoC design     | Embedded telemetry daemons | GStreamer pipeline optimization |

</div>

---

## 🚀 Highlighted Projects

<details>
<summary><b>⚡ RONAN — RISC-V Processor Research Project</b></summary>
<br>

```text
Custom RISC-V processor implementation focused on branch prediction
and microarchitectural experimentation.

┌─────────────────────────────────────────────────────────────────┐
│  Metric              │ Baseline   │ Perceptron  │ TAGE+Perc     │
│──────────────────────┼────────────┼─────────────┼───────────────│
│  Branch Accuracy     │ ~50%       │ 99.89%      │ 95.62%        │
│  IPC                 │ 0.508      │ 0.999       │ —             │
│  GHR Width           │ —          │ 48-bit      │ 48-bit        │
│  Workloads Validated │ —          │ 5 patterns  │ 8 structured  │
└─────────────────────────────────────────────────────────────────┘

Stack: SystemVerilog · Cocotb · Verilator · Python
Paper: Manuscript in preparation for IEEE Conference 2026
```

</details>

<details>
<summary><b>🐧 IFM Electronic — Embedded Linux Industry Project</b></summary>
<br>

```text
Platform:
IFM CR1204 HMI · aarch64 Mali400 SoC · Linux Kernel 5.10.127

Scope:
Optimization of a dual-stream RTSP camera pipeline on hardware
without dedicated video acceleration support.

Work completed:
  • Resolved DRM master lock issues for framebuffer rendering
  • Investigated ARP IP conflicts using tcpdump
  • Optimized CPU utilization across 4 ARM cores
  • Developed telemetry daemon using /proc and sysfs interfaces
  • Validated runtime performance using pandas-based analysis

Result:
Stable deployment configuration for embedded Linux video pipeline.
```

</details>

<details>
<summary><b>🔧 MCU Visualizer — ELF Firmware Inspection Tool</b></summary>
<br>

```c
// Firmware inspection and debugging utility for embedded targets.

struct elf_inspector {
    section_t  regions[];    
    reg_file_t register_state;
    insn_t     active_instruction;
    bool       bare_metal;
};

// Features:
// - ELF parsing in pure C
// - Memory section inspection
// - Register state visualization
// - Instruction-level analysis
// - Qt-based graphical interface
```

</details>

<details>
<summary><b>🔌 UART Bootloader — STM32 Bare-Metal Implementation</b></summary>
<br>

```text
Platform:
STM32F4 · Bare-Metal C · USART1 @ 115200 baud

Features:
→ 64-byte framed packet communication
→ Checksum verification
→ Flash erase and aligned memory programming
→ Application jump validation
→ Timeout-based recovery mechanism

Implementation:
Direct register-level programming without HAL dependencies.
```

</details>

---

## 🛠️ Tech Arsenal

<div align="center">

### Core Languages

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge\&logo=c\&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge\&logo=cplusplus\&logoColor=white)
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-FF6B35?style=for-the-badge\&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-E34F26?style=for-the-badge\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Assembly](https://img.shields.io/badge/RISC--V_ASM-007AAC?style=for-the-badge\&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?style=for-the-badge\&logo=gnu-bash\&logoColor=white)

### Embedded & Hardware

![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge\&logo=stmicroelectronics\&logoColor=white)
![ARM](https://img.shields.io/badge/ARM_Cortex--M-0091BD?style=for-the-badge\&logo=arm\&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge\&logo=espressif\&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-A22846?style=for-the-badge\&logo=raspberry-pi\&logoColor=white)
![Linux](https://img.shields.io/badge/Embedded_Linux-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)

### VLSI & EDA Tools

![Vivado](https://img.shields.io/badge/Xilinx_Vivado-E31837?style=for-the-badge\&logoColor=white)
![OpenROAD](https://img.shields.io/badge/OpenROAD-4A90D9?style=for-the-badge\&logoColor=white)
![Yosys](https://img.shields.io/badge/Yosys-00B388?style=for-the-badge\&logoColor=white)
![Cadence](https://img.shields.io/badge/Cadence_Virtuoso-E60012?style=for-the-badge\&logoColor=white)
![ModelSim](https://img.shields.io/badge/ModelSim-007DB8?style=for-the-badge\&logoColor=white)
![GDB](https://img.shields.io/badge/GDB-A42E2B?style=for-the-badge\&logoColor=white)

### Protocols

![UART](https://img.shields.io/badge/UART-555?style=for-the-badge)
![SPI](https://img.shields.io/badge/SPI-555?style=for-the-badge)
![I2C](https://img.shields.io/badge/I²C-555?style=for-the-badge)
![CAN](https://img.shields.io/badge/CAN_Bus-555?style=for-the-badge)
![APB](https://img.shields.io/badge/AMBA_APB-555?style=for-the-badge)

</div>

---

## 🧩 Skill Proficiency

<div align="center">

```text
Bare-Metal C         ████████████████████  98%
SystemVerilog/RTL    ██████████████████░░  90%
Embedded Linux       █████████████████░░░  85%
RISC-V Architecture  ████████████████░░░░  80%
Python / Scripting   ██████████████░░░░░░  72%
FPGA Toolchain       █████████████░░░░░░░  67%
```

</div>

---

## 📊 GitHub Stats

<!-- <div align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=ApratimPhadke&show_icons=true&theme=tokyonight&include_all_commits=true&count_private=true&hide_border=true"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ApratimPhadke&layout=compact&langs_count=8&theme=tokyonight&hide_border=true"/>
</div> -->

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=ApratimPhadke&theme=tokyonight&hide_border=true" alt="streak"/>
</div>

---

## 📅 Weekly Dev Breakdown

<!--START_SECTION:waka-->

```text
C              ██████████████░░░░░  72.4%
SystemVerilog  ████░░░░░░░░░░░░░░░  18.9%
Python         █░░░░░░░░░░░░░░░░░░   5.3%
Shell          ░░░░░░░░░░░░░░░░░░░   2.1%
Other          ░░░░░░░░░░░░░░░░░░░   1.3%
```

<!--END_SECTION:waka-->

---

## 🏆 Trophy Case

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=ApratimPhadke&theme=tokyonight&no-frame=true&no-bg=true&margin-w=4&row=1"/>
</div>

---

## 📈 Activity Graph

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=ApratimPhadke&theme=tokyo-night&hide_border=true&area=true" width="100%"/>
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/ApratimPhadke/ApratimPhadke/output/github-contribution-grid-snake.svg" />
</p>

<!--## 💬 Random Dev Quote

<div align="center">

[![Readme Quotes](https://quotes-github-readme.vercel.app/api?type=horizontal\&theme=tokyonight)](https://github.com/piyushsuthar/github-readme-quotes)

</div>-->
## 💬 Random Dev Quote

<div align="center">

[![Readme Quotes](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight&cachebuster=143596)](https://github.com/piyushsuthar/github-readme-quotes)

</div>

---

## 🤝 Let's Connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Apratim_Phadke-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/apratim-phadke-966816223/)
 
[![Email](https://img.shields.io/badge/Gmail-apratimphadkeprime@gmail.com-EA4335?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:apratimphadkeprime@gmail.com)
 
[![IEEE](https://img.shields.io/badge/IEEE_VIIT-General_Manager-00629B?style=for-the-badge\&logo=ieee\&logoColor=white)](https://ieee.org)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=ApratimPhadke\&color=58A6FF\&style=for-the-badge\&label=PROFILE+VIEWS)

</div>

---

<div align="center">

Focused on low-level systems, hardware-software integration,
and architecture-driven embedded development.


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&animation=twinkling"/>

</div>
```
