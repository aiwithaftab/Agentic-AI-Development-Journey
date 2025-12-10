# 🚀 AI Agents Journey — Daily Code & Learning Log

<p align="center">
  <img src="assets/agent-journey.svg" alt="AI Agent Journey Animation" width="720" />
</p>

> *Daily practice, experiments, and small wins — one commit at a time.*

---

## 🔍 About this repo
This repo documents my **daily journey building AI Agents & agentic systems** using **Generative AI, Python, and practical infra**. Every day I upload a folder named `day-YYYY-MM-DD` containing code, notes, datasets, and short demos.

This README is designed to be visually attractive on GitHub using a lightweight animated SVG (no external JS). Save the SVG in `/assets/agent-journey.svg` to see the animation.

---

## 🗂️ Recommended repo structure
```
/ (root)
├─ assets/
│  └─ agent-journey.svg      # animated header (save from below)
├─ day-2025-12-01/
│  ├─ code.ipynb
│  ├─ main.py
│  └─ notes.md
├─ day-2025-12-02/
│  └─ ...
├─ README.md
└─ LICENSE
```

---

## 🛠️ How to use this README
1. **Copy** the SVG content (provided below) into `assets/agent-journey.svg` in your repo.
2. Keep updating the `day-YYYY-MM-DD` folders — one commit per day if possible.
3. Use this README as the project landing page, update the short summary at the top of the README weekly.

---

## ✨ Features included
- Animated SVG header showing a rocket (agent) traveling through milestones.
- Progress trackers and badges (manually update milestones).
- Clear daily folder layout for recruiters and collaborators.

---

## 🧭 Suggested commit message format
Use consistent commit messages to show cadence:
```
Daily: day-2025-12-10 — experimented with action planning + tool-call stub
```

---

## 📦 Animated SVG (save as `assets/agent-journey.svg`)

> Copy everything between the fenced block and save as `assets/agent-journey.svg`.

```svg
<!-- Agent Journey Animated SVG
     Save this file as assets/agent-journey.svg in your repo. It uses pure SVG animation (SMIL + CSS) and will render on GitHub.
-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420">
  <defs>
    <linearGradient id="bg" x1="0" x2="1">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#0b1220" />
    </linearGradient>
    <linearGradient id="horizon" x1="0" x2="1">
      <stop offset="0%" stop-color="#0b1220" stop-opacity="0.0"/>
      <stop offset="100%" stop-color="#0b1220" stop-opacity="0.6"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <style type="text/css"><![CDATA[
      .small { font: 16px 'Segoe UI', Roboto, Arial; fill: #cbd5e1; }
      .title { font: 34px 'Segoe UI', Roboto, Arial; fill: #fff; font-weight:700; }
      .muted { fill: #94a3b8; font-size:14px; }
      .pulse { animation: pulse 2s infinite; }
      @keyframes pulse {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.06); opacity: 1; }
        100% { transform: scale(1); opacity: 0.9; }
      }
      /* progress dots */
      .dot { transition: transform 0.3s ease; }
      .dot:hover { transform: scale(1.25); }
    ]]></style>
  </defs>

  <!-- Background -->
  <rect width="1200" height="420" fill="url(#bg)"/>
  <rect y="320" width="1200" height="100" fill="url(#horizon)" />

  <!-- Stars -->
  <g id="stars">
    <!-- multiple small stars using circles with slight flicker -->
    <circle cx="110" cy="60" r="1.8" fill="#fff" opacity="0.9">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="3.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="210" cy="40" r="1.6" fill="#fff" opacity="0.8">
      <animate attributeName="opacity" values="1;0.3;1" dur="4.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="380" cy="80" r="1.2" fill="#fff" opacity="0.7">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="960" cy="50" r="1.5" fill="#fff" opacity="0.9">
      <animate attributeName="opacity" values="1;0.2;1" dur="3.2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Title block -->
  <g transform="translate(40,40)">
    <text class="title">AI Agents Journey</text>
    <text class="small" y="36">Agentic AI • Generative AI • Python • Daily Practice</text>
  </g>

  <!-- Rocket / Agent (animated) -->
  <g id="rocket" transform="translate(120,250)">
    <!-- shadow -->
    <ellipse cx="40" cy="110" rx="70" ry="14" fill="#020617" opacity="0.35" />

    <!-- rocket body -->
    <g filter="url(#glow)">
      <g transform="translate(0, -60)">
        <rect x="18" y="10" rx="12" ry="12" width="44" height="72" fill="#e11d48" />
        <circle cx="40" cy="36" r="12" fill="#fff" />
        <rect x="14" y="60" width="52" height="10" rx="6" fill="#111827"/>
      </g>

      <!-- flame -->
      <g transform="translate(30,86)">
        <path d="M0,0 C8,12 24,12 32,0 C24,18 8,18 0,0 Z" fill="#ffb11f" opacity="0.95">
          <animate attributeName="transform" values="scale(1);scale(0.9);scale(1)" dur="0.6s" repeatCount="indefinite"/>
        </path>
      </g>
    </g>

    <!-- rocket trajectory animation (moves along x) -->
    <animateTransform attributeName="transform" attributeType="XML" type="translate"
                      values="120,250; 440,90; 760,170; 1020,40"
                      keyTimes="0;0.35;0.7;1" dur="12s" repeatCount="indefinite"/>
  </g>

  <!-- Timeline / milestones -->
  <g transform="translate(90,330)">
    <!-- baseline -->
    <line x1="0" y1="0" x2="1020" y2="0" stroke="#334155" stroke-width="3" stroke-linecap="round" />

    <!-- milestone dots and labels -->
    <g transform="translate(0, -18)">
      <!-- Day 1 -->
      <g transform="translate(0,0)">
        <circle class="dot" cx="30" cy="-2" r="10" fill="#06b6d4" />
        <text class="muted" x="-8" y="24">Day 1</text>
      </g>

      <!-- Day 15 -->
      <g transform="translate(240,0)">
        <circle class="dot" cx="30" cy="-2" r="10" fill="#60a5fa" />
        <text class="muted" x="-6" y="24">Day 15</text>
      </g>

      <!-- Day 30 -->
      <g transform="translate(520,0)">
        <circle class="dot" cx="30" cy="-2" r="10" fill="#a78bfa" />
        <text class="muted" x="-8" y="24">Day 30</text>
      </g>

      <!-- Day 90 -->
      <g transform="translate(840,0)">
        <circle class="dot" cx="30" cy="-2" r="10" fill="#34d399" />
        <text class="muted" x="-10" y="24">Day 90</text>
      </g>
    </g>

    <!-- moving progress indicator that follows the rocket -->
    <g id="progress" transform="translate(0,-16)">
      <circle cx="30" cy="-2" r="8" fill="#fff" opacity="0.95">
        <animate attributeName="cx" values="30;270;550;870" keyTimes="0;0.35;0.7;1" dur="12s" repeatCount="indefinite" />
      </circle>
    </g>
  </g>

  <!-- Left panel with quick stats -->
  <g transform="translate(40,200)">
    <rect x="0" y="0" rx="10" ry="10" width="420" height="120" fill="#071033" opacity="0.6" />
    <text class="muted" x="20" y="28">📅 Streak</text>
    <text class="small" x="20" y="52">Commits: <tspan fill="#fff">42</tspan></text>
    <text class="muted" x="186" y="28">🏷️ Focus</text>
    <text class="small" x="186" y="52">Agent loops, Tooling, Infra</text>
    <text class="muted" x="20" y="90">🧾 Latest</text>
    <text class="small" x="20" y="112">Day-2025-12-09 — action plan + tool-calls</text>
  </g>

  <!-- footer small note -->
  <g transform="translate(40,390)">
    <text class="muted">Made with ❤️ — Save the SVG to <tspan fill="#fff">assets/agent-journey.svg</tspan> to render animation</text>
  </g>
</svg>
```

---

## 🧩 Customize the SVG
- Edit text lines in the SVG to show your real progress numbers and latest day.
- You can change milestone colors by modifying the `fill` values for the dots.
- If GitHub doesn't animate the SVG in the README preview, open the raw file or view it directly in the repo (some browsers / viewers may limit SMIL support). A GIF fallback can be added if needed.

---

## 📣 Final tips
- Commit daily and keep commit messages consistent — recruiters love cadence.
- Add a short 1–2 line blurb at the top of each day folder describing the day's learning.
- Pin this repo to your GitHub profile and link it on LinkedIn.

---

If you want, I can also:
- Generate a GIF fallback for platforms that don’t animate SVG SMIL.
- Create a compact badge you can show in the README header with live stats (requires GitHub Actions).

Happy building — keep the daily momentum! 🌟
