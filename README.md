
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&display=swap');
  *{box-sizing:border-box;margin:0;padding:0}
  :root{--green:#00d97e;--dim:#00a85c;--bg:#0a0c0f;--bg2:#0f1218;--bg3:#141820;--border:#1e2530;--text:#c9d1d9;--muted:#6e7681;--accent:#58a6ff;--orange:#f0883e;--purple:#bc8cff}
  body{background:var(--bg);color:var(--text);font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.6;padding:0}
  .container{max-width:860px;margin:0 auto;padding:24px 20px}
  .boot-bar{border:1px solid var(--border);border-radius:6px;padding:10px 14px;margin-bottom:24px;background:var(--bg2);overflow:hidden}
  .boot-line{color:var(--green);font-size:11px;white-space:nowrap;opacity:0}
  .boot-line.visible{animation:fadeIn 0.3s forwards}
  @keyframes fadeIn{to{opacity:1}}
  .prompt{color:var(--green);font-weight:700}
  .cursor{display:inline-block;width:8px;height:14px;background:var(--green);animation:blink 1s step-end infinite;vertical-align:text-bottom;margin-left:2px}
  @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
  .section{margin-bottom:28px}
  .cmd-header{color:var(--green);font-size:13px;margin-bottom:12px;display:flex;align-items:center;gap:8px}
  .cmd-header::after{content:'';flex:1;height:1px;background:var(--border)}
  .name-block{text-align:center;padding:28px 0 20px;border-bottom:1px solid var(--border);margin-bottom:24px}
  .name{font-size:32px;font-weight:700;color:#fff;letter-spacing:-0.5px}
  .title-line{color:var(--muted);font-size:12px;margin-top:6px}
  .badge-row{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:14px}
  .badge{padding:4px 10px;border-radius:4px;font-size:11px;border:1px solid}
  .badge-green{border-color:var(--dim);color:var(--green);background:rgba(0,217,126,0.05)}
  .badge-blue{border-color:#1f4068;color:var(--accent);background:rgba(88,166,255,0.05)}
  .badge-orange{border-color:#4a2f10;color:var(--orange);background:rgba(240,136,62,0.05)}
  .badge-purple{border-color:#3d2a5e;color:var(--purple);background:rgba(188,140,255,0.05)}
  .code-block{background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:16px;font-size:12px;line-height:1.8;overflow-x:auto}
  .kw{color:var(--purple)} .type{color:var(--accent)} .str{color:var(--orange)} .num{color:var(--green)} .cmt{color:var(--muted)} .punc{color:var(--text)}
  .skill-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
  .skill-card{background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:14px}
  .skill-card-title{color:var(--muted);font-size:10px;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px}
  .skill-item{display:flex;align-items:center;gap:8px;margin-bottom:6px}
  .skill-name{color:var(--text);font-size:11px;min-width:130px}
  .skill-bar{flex:1;height:3px;background:var(--border);border-radius:2px;overflow:hidden}
  .skill-fill{height:100%;border-radius:2px;width:0;transition:width 1.2s ease}
  .fill-green{background:var(--green)} .fill-blue{background:var(--accent)} .fill-orange{background:var(--orange)}
  .exp-card{background:var(--bg2);border:1px solid var(--border);border-radius:6px;padding:16px;margin-bottom:12px}
  .exp-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;flex-wrap:wrap;gap:8px}
  .exp-role{color:#fff;font-size:13px;font-weight:600}
  .exp-company{color:var(--green);font-size:11px;margin-top:2px}
  .exp-period{color:var(--muted);font-size:11px;border:1px solid var(--border);padding:2px 8px;border-radius:3px}
  .exp-tag-row{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
  .tag{font-size:10px;padding:2px 7px;border-radius:3px;border:1px solid var(--border);color:var(--muted)}
  .exp-bullets{padding-left:14px}
  .exp-bullets li{font-size:12px;color:var(--text);margin-bottom:5px;line-height:1.5}
  .exp-bullets li::marker{color:var(--green)}
  .proj-card{background:var(--bg2);border:1px solid var(--border);border-left:3px solid var(--green);border-radius:6px;padding:16px;margin-bottom:12px}
  .proj-name{color:#fff;font-size:13px;font-weight:600;margin-bottom:4px}
  .proj-sub{color:var(--muted);font-size:11px;margin-bottom:8px}
  .metric-table{width:100%;border-collapse:collapse;margin:10px 0;font-size:11px}
  .metric-table th{color:var(--muted);font-weight:400;text-align:left;padding:3px 8px 3px 0;border-bottom:1px solid var(--border)}
  .metric-table td{padding:3px 8px 3px 0;color:var(--text)}
  .metric-table .highlight{color:var(--green);font-weight:600}
  .footer-box{border:1px solid var(--border);border-radius:6px;padding:14px;text-align:center;background:var(--bg2);margin-top:24px}
  .footer-quote{color:var(--muted);font-size:11px;font-style:italic;margin-bottom:12px}
  .link-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
  .link-btn{padding:6px 14px;border-radius:4px;font-size:11px;font-family:'JetBrains Mono',monospace;cursor:pointer;text-decoration:none;border:1px solid}
  .link-btn-green{border-color:var(--dim);color:var(--green);background:rgba(0,217,126,0.05)}
  .link-btn-blue{border-color:#1f4068;color:var(--accent);background:rgba(88,166,255,0.05)}
  .typing-line{overflow:hidden;white-space:nowrap;border-right:2px solid var(--green)}
  .terminal-anim{color:var(--green);font-size:12px;height:22px;overflow:hidden}
  @media(max-width:600px){.skill-grid{grid-template-columns:1fr}.exp-header{flex-direction:column}}
</style>

<div class="container">
  <div class="boot-bar">
    <div class="boot-line" id="b0">BOOT LOG :: VIIT-ENTC-2027 :: ARM-CORTEX-M → RISCV → LINUX → RTL → GDS</div>
    <div class="boot-line" id="b1">[ CPU: CORTEX-A ] &nbsp;[ MEM: 8.36 CGPA ] &nbsp;[ IRQ: ALWAYS ON ] &nbsp;[ STATUS: ACTIVE ]</div>
    <div class="boot-line" id="b2">Loaded: RTL · Embedded Linux · Processor Arch · FPGA · Bare-Metal C ............. <span style="color:var(--green)">OK</span></div>
    <div class="boot-line" id="b3">IFM Electronic industry project ................................................. <span style="color:var(--green)">COMPLETE</span></div>
    <div class="boot-line" id="b4">RONAN v2 hybrid TAGE+Perceptron 95.62% acc ....................................... <span style="color:var(--green)">PAPER IN PREP</span></div>
    <div class="boot-line" id="b5"><span class="prompt">apratim@viit:~$</span> <span class="cursor"></span></div>
  </div>

  <div class="name-block">
    <div class="name">APRATIM PHADKE</div>
    <div class="title-line">Embedded Systems Engineer &nbsp;·&nbsp; VLSI Designer &nbsp;·&nbsp; Processor Architect</div>
    <div class="title-line" style="margin-top:4px">B.Tech ENTC · VIIT Pune · 2023→2027 &nbsp;|&nbsp; CGPA 8.36 · IEEE GM</div>
    <div class="badge-row">
      <span class="badge badge-green">RTL &amp; VLSI</span>
      <span class="badge badge-blue">Embedded Linux</span>
      <span class="badge badge-orange">Processor Arch</span>
      <span class="badge badge-purple">RISC-V</span>
      <span class="badge badge-green">Bare-Metal C</span>
      <span class="badge badge-blue">FPGA</span>
    </div>
  </div>

  <div class="section">
    <div class="cmd-header"><span class="prompt">&gt;</span> whoami</div>
    <div class="code-block">
<span class="kw">module</span> <span class="type">apratim_phadke</span> <span class="punc">#(</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">parameter</span> INSTITUTION <span class="punc">=</span> <span class="str">"VIIT Pune — B.Tech ENTC — 2023→2027"</span><span class="punc">,</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">parameter</span> CGPA &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="punc">=</span> <span class="num">8.36</span><span class="punc">,</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">parameter</span> DOMAIN &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="punc">=</span> <span class="str">"Embedded Linux | VLSI | RTL | Computer Architecture"</span><br>
<span class="punc">)(</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">input</span> &nbsp;<span class="type">wire</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;curiosity<span class="punc">,</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">input</span> &nbsp;<span class="type">wire</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware_instinct<span class="punc">,</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">output</span> <span class="type">reg</span> <span class="punc">[63:0]</span> production_systems<span class="punc">,</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">output</span> <span class="type">reg</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;papers_in_prep<br>
<span class="punc">);</span><br><br>
<span class="kw">localparam</span> STACK <span class="punc">=</span> <span class="str">"Transistors → RTL → Firmware → Linux Userspace"</span><span class="punc">;</span><br><br>
<span class="kw">always</span> <span class="punc">@(</span><span class="kw">posedge</span> clk<span class="punc">)</span> <span class="kw">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">if</span> <span class="punc">(</span>curiosity <span class="punc">&amp;</span> hardware_instinct<span class="punc">)</span> <span class="kw">begin</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;production_systems <span class="punc">&lt;=</span> build_debug_iterate<span class="punc">();</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;papers_in_prep &nbsp;&nbsp;&nbsp;&nbsp;<span class="punc">&lt;=</span> <span class="num">1'b1</span><span class="punc">;</span> <span class="cmt">// RONAN — VIIT Pune 2026</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">end</span><br>
<span class="kw">end</span><br><br>
<span class="kw">endmodule</span>
    </div>
  </div>

  <div class="section">
    <div class="cmd-header"><span class="prompt">&gt;</span> cat /proc/skills</div>
    <div class="skill-grid" id="skillGrid">
      <div class="skill-card">
        <div class="skill-card-title">RTL &amp; VLSI</div>
        <div class="skill-item"><span class="skill-name">SystemVerilog</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="95"></div></div></div>
        <div class="skill-item"><span class="skill-name">Verilog</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="95"></div></div></div>
        <div class="skill-item"><span class="skill-name">OpenROAD</span><div class="skill-bar"><div class="skill-fill fill-orange" data-w="78"></div></div></div>
        <div class="skill-item"><span class="skill-name">Yosys</span><div class="skill-bar"><div class="skill-fill fill-orange" data-w="80"></div></div></div>
        <div class="skill-item"><span class="skill-name">Xilinx Vivado</span><div class="skill-bar"><div class="skill-fill fill-orange" data-w="80"></div></div></div>
        <div class="skill-item"><span class="skill-name">Magic VLSI / KLayout</span><div class="skill-bar"><div class="skill-fill fill-orange" data-w="75"></div></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-card-title">Embedded &amp; Systems</div>
        <div class="skill-item"><span class="skill-name">C (Bare-Metal)</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="95"></div></div></div>
        <div class="skill-item"><span class="skill-name">STM32 (F1/F4/L0/C0)</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="92"></div></div></div>
        <div class="skill-item"><span class="skill-name">Embedded Linux</span><div class="skill-bar"><div class="skill-fill fill-blue" data-w="82"></div></div></div>
        <div class="skill-item"><span class="skill-name">RISC-V Assembly</span><div class="skill-bar"><div class="skill-fill fill-blue" data-w="80"></div></div></div>
        <div class="skill-item"><span class="skill-name">GDB / Debug</span><div class="skill-bar"><div class="skill-fill fill-blue" data-w="80"></div></div></div>
        <div class="skill-item"><span class="skill-name">Python / TCL</span><div class="skill-bar"><div class="skill-fill fill-blue" data-w="78"></div></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-card-title">Verification</div>
        <div class="skill-item"><span class="skill-name">Cocotb</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="82"></div></div></div>
        <div class="skill-item"><span class="skill-name">Verilator</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="80"></div></div></div>
        <div class="skill-item"><span class="skill-name">GTKWave</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="85"></div></div></div>
        <div class="skill-item"><span class="skill-name">ModelSim</span><div class="skill-bar"><div class="skill-fill fill-orange" data-w="72"></div></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-card-title">Protocols &amp; Comms</div>
        <div class="skill-item"><span class="skill-name">UART / SPI / I2C</span><div class="skill-bar"><div class="skill-fill fill-green" data-w="90"></div></div></div>
        <div class="skill-item"><span class="skill-name">APB / AHB</span><div class="skill-bar"><div class="skill-fill fill-blue" data-w="78"></div></div></div>
        <div class="skill-item"><span class="skill-name">CAN</span><div class="skill-bar"><div class="skill-fill fill-blue" data-w="72"></div></div></div>
        <div class="skill-item"><span class="skill-name">ONVIF / GStreamer</span><div class="skill-bar"><div class="skill-fill fill-orange" data-w="75"></div></div></div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="cmd-header"><span class="prompt">&gt;</span> ls -la ~/experience/</div>
    <div class="exp-card">
      <div class="exp-header">
        <div>
          <div class="exp-role">Embedded Linux Platform Validation &amp; Systems Software</div>
          <div class="exp-company">IFM Electronic &nbsp;·&nbsp; Industry Sponsored Project</div>
        </div>
        <div class="exp-period">2024 – 2025</div>
      </div>
      <div class="exp-tag-row">
        <span class="tag">CODESYS</span><span class="tag">Python</span><span class="tag">Shell</span><span class="tag">ONVIF</span><span class="tag">GDB</span><span class="tag">GStreamer</span><span class="tag">Plotly/Dash</span><span class="tag">aarch64</span>
      </div>
      <ul class="exp-bullets">
        <li>Deployed and profiled a camera streaming stack on a resource-constrained <strong style="color:#fff">ifm CR1204 HMI SoC</strong>, instrumenting CPU utilization, memory footprint, throughput, and sustained FPS across a codec×resolution matrix — results became production deployment parameters</li>
        <li>Designed a closed-loop <strong style="color:#fff">Adaptive Bitrate (ABR) controller</strong> in CODESYS interfacing via ONVIF; modular function blocks for stream management, KPI overlay, and resource monitoring on a constrained runtime</li>
        <li>Executed multi-layer <strong style="color:#fff">hardware-software co-debug</strong> across firmware, CODESYS runtime, and Linux kernel to isolate SoC bottlenecks using GDB and shell diagnostics</li>
        <li>Shipped a <strong style="color:#fff">real-time Plotly/Dash performance dashboard</strong> automating the full validation pipeline end-to-end — surfacing bottlenecks and defining platform performance envelopes</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <div class="cmd-header"><span class="prompt">&gt;</span> ls -la ~/projects/</div>

    <div class="proj-card">
      <div class="proj-name">⚡ RONAN — Neural Network-Inspired Pipelined RISC-V Processor</div>
      <div class="proj-sub">SystemVerilog · Cocotb · Verilator · Python &nbsp;|&nbsp; <span style="color:var(--orange)">Paper in preparation — VIIT Pune 2026</span></div>
      <table class="metric-table">
        <tr><th>Metric</th><th>Baseline</th><th>RONAN (Neural)</th><th>RONAN (Hybrid)</th></tr>
        <tr><td>Branch Pred. Accuracy</td><td>~50%</td><td class="highlight">99.89%</td><td class="highlight">95.62%</td></tr>
        <tr><td>IPC</td><td>0.508</td><td class="highlight">0.999</td><td>—</td></tr>
        <tr><td>Predictor</td><td>None</td><td>Perceptron</td><td>TAGE + Perceptron</td></tr>
        <tr><td>GHR Width</td><td>—</td><td>48-bit</td><td>48-bit</td></tr>
      </table>
      <ul class="exp-bullets">
        <li>Designed a <strong style="color:#fff">quad-core RISC-V processor</strong> with perceptron-based dynamic branch prediction — validated across alternating, pointer-chase, loop-exit, and bimodal workloads</li>
        <li>Implemented a <strong style="color:#fff">hybrid TAGE+Perceptron predictor</strong>: TAGE covers structured patterns, perceptron captures long-history correlations — architecture analogous to branch prediction in production GPU compiler backends</li>
        <li>Built parameterized <strong style="color:#fff">Cocotb/Verilator testbenches</strong> for perceptron table, GHR, and jog-packet unit — full RTL verification methodology from stimulus to scoreboard</li>
      </ul>
    </div>

    <div class="proj-card">
      <div class="proj-name">🔧 MCU Visualizer — Custom ELF-Based Firmware Debug Toolchain</div>
      <div class="proj-sub">C · Qt · Python · Arduino · ESP32</div>
      <ul class="exp-bullets">
        <li>Built an autonomous embedded robot on <strong style="color:#fff">Arduino UNO + ESP32</strong> with real-time motor and sensor control over a custom wireless protocol — full hardware-software stack ownership</li>
        <li>Developed <strong style="color:#fff">MCU Visualizer</strong>: real-time ELF binary parsing to decode active instructions, map memory regions (.text / .data / .bss / stack / heap), and visualize register state on-target — directly applicable to BSP bringup and post-silicon debug</li>
        <li>Implemented the <strong style="color:#fff">ELF parsing engine in bare-metal C</strong> (zero library dependency); migrated full GUI toolchain to C + Qt for live firmware introspection and on-target optimization</li>
      </ul>
    </div>
  </div>

  <div class="section">
    <div class="cmd-header"><span class="prompt">&gt;</span> cat ~/.config/interests</div>
    <div class="code-block">
<span class="punc">[</span><span class="type">current_obsession</span><span class="punc">]</span><br>
focus &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="punc">=</span> <span class="str">RISC-V microarchitecture · TAGE branch predictors · OpenROAD flows</span><br>
deep_curiosity  <span class="punc">=</span> <span class="str">Compiler-hardware co-design · neuromorphic arch · FPGA overlays</span><br><br>
<span class="punc">[</span><span class="type">philosophy</span><span class="punc">]</span><br>
build_style &nbsp;&nbsp;&nbsp;&nbsp;<span class="punc">=</span> <span class="str">"Build it. Break it. Instrument it. Fix it. Document it."</span><br>
what_drives_me  <span class="punc">=</span> <span class="str">The moment simulation waveforms match silicon behaviour</span><br>
mantra &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="punc">=</span> <span class="str">"Hardware is truth. Everything else is abstraction."</span>
    </div>
  </div>

  <div class="footer-box">
    <div class="footer-quote">"If it doesn't run on bare metal, it isn't real yet."</div>
    <div class="link-row">
      <a class="link-btn link-btn-blue" href="https://www.linkedin.com/in/apratim-phadke-966816223/" target="_blank">LinkedIn ↗</a>
      <a class="link-btn link-btn-green" href="mailto:apratimphadkeprime@gmail.com">apratimphadkeprime@gmail.com</a>
    </div>
  </div>
</div>

<script>
const boots = document.querySelectorAll('.boot-line');
boots.forEach((el, i) => {
  setTimeout(() => el.classList.add('visible'), i * 280);
});

function animateBars() {
  document.querySelectorAll('.skill-fill').forEach(el => {
    const w = el.getAttribute('data-w');
    setTimeout(() => { el.style.width = w + '%'; }, 600);
  });
}
const obs = new IntersectionObserver((entries) => {
  entries.forEach(e => { if(e.isIntersecting) { animateBars(); obs.disconnect(); } });
}, { threshold: 0.1 });
const sg = document.getElementById('skillGrid');
if(sg) obs.observe(sg);
</script>
