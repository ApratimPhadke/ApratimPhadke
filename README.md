<a href="https://komarev.com/ghpvc/?username=gmostofabd">
  <img align="right" src="https://komarev.com/ghpvc/?username=gmostofabd&label=ProfileViews&color=0e75b6&style=flat" alt="Profile visitor" />
</a> 

![MK_51S_Simu_1](https://github.com/user-attachments/assets/cb24ba0b-56c8-432a-b949-bd34c3f8d6af)

<hr/>
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Apratim%20Phadke&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=38&desc=I%20build%20things%20that%20run%20on%20bare%20metal.&descAlignY=60&descSize=18"/>
</div>

<div align="center">
  
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=600&lines=Embedded+Systems+Engineer+%F0%9F%94%A7;VLSI+%2B+RTL+Design+Architect+%E2%9A%A1;RISC-V+Processor+Designer+%F0%9F%A7%A0;Bare-Metal+C+%7C+Embedded+Linux+%F0%9F%90%A7;Silicon+to+Software%2C+Full+Stack+%F0%9F%94%8C)](https://git.io/typing-svg)

</div>

---

<img align="right" alt="Hardware Hacker" width="380" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif"/>

### 🧠 Who Am I?

```yaml
name: Apratim Phadke
based_in: Pune, India 🇮🇳
university: VIIT Pune — B.Tech ENTC
cgpa: 8.36 / 10

i_live_at_the_intersection_of:
  - Silicon & Software
  - RTL & Real Hardware
  - Firmware & Linux Kernel

currently:
  building: RONAN — RISC-V Processor (IEEE paper)
  learning: Advanced Microarchitecture
  leading: IEEE VIIT Student Branch (GM)
  
ask_me_about:
  - STM32 bare-metal wizardry
  - RISC-V processor design
  - GStreamer on embedded Linux
  - Making constrained SoCs perform
```

<br clear="right"/>

---

## ⚡ What Makes Me Different

> Most engineers pick a layer and stay there.
> I own the entire stack — transistors to userspace.

<div align="center">

| 🔬 I've designed | 🛠️ I've shipped | 🔥 I've debugged |
|:---:|:---:|:---:|
| A RISC-V processor from scratch | A bare-metal UART bootloader with zero HAL | A DRM master lock at kernel-space |
| Branch predictor @ 99.89% accuracy | An ELF parser in pure C, no libraries | ARP conflicts on embedded SoCs via tcpdump |
| APB SoC with UART + I2C on FPGA | Real-time telemetry daemons on aarch64 | GStreamer pipelines with no VPU — and won |

</div>

---

## 🚀 Highlight Reel

<details>
<summary><b>⚡ RONAN — Neural-Inspired RISC-V Processor (click to expand)</b></summary>
<br>

```
Not a tutorial. Not a clone. An original architecture.

┌─────────────────────────────────────────────────────────────────┐
│  Metric              │ Baseline   │ Perceptron  │ TAGE+Perc     │
│──────────────────────┼────────────┼─────────────┼───────────────│
│  Branch Accuracy     │ ~50%       │ 99.89% 🔥   │ 95.62%        │
│  IPC                 │ 0.508      │ 0.999  🚀   │ —             │
│  GHR Width           │ —          │ 48-bit      │ 48-bit        │
│  Workloads Validated │ —          │ 5 patterns  │ 8 structured  │
└─────────────────────────────────────────────────────────────────┘

Stack: SystemVerilog · Cocotb · Verilator · Python
Paper: Manuscript in prep → IEEE Conference 2026
```

</details>

<details>
<summary><b>🐧 IFM Electronic — Industry Project (Embedded Linux, aarch64)</b></summary>
<br>

```
Platform: IFM CR1204 HMI · aarch64 Mali400 SoC · Kernel 5.10.127
Challenge: Dual-stream RTSP camera pipeline. No VPU. Weston broken.

What I did:
  ✅ Released DRM master lock manually → routed GStreamer to /dev/fb0
  ✅ Resolved ARP IP conflict via tcpdump → engineered stable pipeline
  ✅ Drove CPU from saturation → 22.6% across 4 ARM cores
  ✅ Built telemetry daemon: /proc/stat + /sys/class/net @ 1s intervals
  ✅ Pandas-validated: ΔCPU = 0.26%, RAM stable at ~343 MB

These numbers became the production deployment parameters.
```

</details>

<details>
<summary><b>🔧 MCU Visualizer — Custom ELF Debug Toolchain</b></summary>
<br>

```c
// What GDB doesn't show you.
// Live firmware introspection. On target. Zero dependencies.

struct elf_inspector {
    section_t  regions[];    // .text / .data / .bss / stack / heap
    reg_file_t register_state;
    insn_t     active_instruction;
    bool       bare_metal;   // Pure C ELF parser. No libraries.
};

// Full Qt GUI. Deployed on a live autonomous ESP32 robot.
```

</details>

<details>
<summary><b>🔌 UART Bootloader — Zero HAL, Pure Registers</b></summary>
<br>

```
STM32F4 · Bare-Metal C · USART1 @ 115200 baud

→ 64-byte framed packets with checksum verification
→ Flash erase + word-aligned write from 0x08004000
→ Validated stack-pointer/reset-vector jump to application
→ 5-second timeout fallback
→ Not a library in sight. Just registers.
```

</details>


## 🛠️ Tech Arsenal

<div align="center">

### Core Languages
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-FF6B35?style=for-the-badge&logoColor=white)
![Verilog](https://img.shields.io/badge/Verilog-E34F26?style=for-the-badge&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Assembly](https://img.shields.io/badge/RISC--V_ASM-007AAC?style=for-the-badge&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)

### Embedded & Hardware
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![ARM](https://img.shields.io/badge/ARM_Cortex--M-0091BD?style=for-the-badge&logo=arm&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=white)
![Linux](https://img.shields.io/badge/Embedded_Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

### VLSI & EDA Tools
![Vivado](https://img.shields.io/badge/Xilinx_Vivado-E31837?style=for-the-badge&logoColor=white)
![OpenROAD](https://img.shields.io/badge/OpenROAD-4A90D9?style=for-the-badge&logoColor=white)
![Yosys](https://img.shields.io/badge/Yosys-00B388?style=for-the-badge&logoColor=white)
![Cadence](https://img.shields.io/badge/Cadence_Virtuoso-E60012?style=for-the-badge&logoColor=white)
![ModelSim](https://img.shields.io/badge/ModelSim-007DB8?style=for-the-badge&logoColor=white)
![GDB](https://img.shields.io/badge/GDB-A42E2B?style=for-the-badge&logoColor=white)

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

```
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

> **Setup:** Connect [WakaTime](https://wakatime.com) to auto-update this block via GitHub Actions using [`waka-readme`](https://github.com/athul/waka-readme).

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

---

## 🎯 2025–2026 Goals

<div align="center">

| Goal | Status |
|:---|:---:|
| 📄 Publish RONAN IEEE paper | 🔄 In Progress |
| 🧠 Tape out RONAN on Sky130 PDK (OpenROAD) | 🔜 Planned |
| 🐧 Upstream a kernel patch (Linux mainline) | 🔜 Planned |
| ⚡ Complete out-of-order execution pipeline | 🔄 In Progress |
| 🏆 Present at a technical conference | 🔜 Planned |
| 🔗 Complete CAN Bus gateway project | ✅ Ongoing |

</div>

---
<p align="center">
  <img src="https://raw.githubusercontent.com/ApratimPhadke/ApratimPhadke/output/github-contribution-grid-snake.svg" />
</p>

## 💬 Random Dev Quote

<div align="center">

[![Readme Quotes](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight)](https://github.com/piyushsuthar/github-readme-quotes)

</div>


## 🤝 Let's Connect

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Apratim_Phadke-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/apratim-phadke-966816223/)
&nbsp;
[![Email](https://img.shields.io/badge/Gmail-apratimphadkeprime@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:apratimphadkeprime@gmail.com)
&nbsp;
[![IEEE](https://img.shields.io/badge/IEEE_VIIT-General_Manager-00629B?style=for-the-badge&logo=ieee&logoColor=white)](https://ieee.org)

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=ApratimPhadke&color=58A6FF&style=for-the-badge&label=PROFILE+VIEWS)

</div>

---

<div align="center">

```
If it runs on bare metal, I've probably broken it — and fixed it at 2 AM.
```

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer&animation=twinkling"/>

</div>
