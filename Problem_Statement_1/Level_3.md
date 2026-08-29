# ⏱️ Level 3 — Real-Time Evolution

[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner%20to%20Intermediate-2ecc71?style=flat-square)](#)
[![Concepts](https://img.shields.io/badge/Concepts-Timed%20Loops%20|%20Screen%20Clearing-0d6efd?style=flat-square)](#)

---

## Background

Levels 1 and 2 print only the final grid after all generations are computed. Level 3 prints each generation as it happens, one frame at a time, with a short delay between frames.

---

## Your Task

| # | Feature | Description |
|---|---|---|
| 1 | **Real-Time Playback** | Print each generation, pause briefly, clear the screen, print the next. |

**Bonus:** Let the user set the delay between frames (in milliseconds) instead of using a fixed delay.

---

## Rules

- Any programming language
- Single program file, runs in your terminal
- No GUI frameworks or third-party libraries
- Using your language's built-in delay function (`sleep`, `Thread.sleep`, `setTimeout`, etc.) is allowed — no multithreading needed
- Because output is printed in real time, plain captured text won't fully show the effect. Include a short screen recording or GIF along with your code.

---

## Concepts You'll Use

| Concept | Description |
|---|---|
| Timed Loops | Pausing between iterations so frames appear at a readable pace |
| Screen Clearing | Clearing the previous frame before printing the next |

**Delay:** `time.sleep(1)` (Python), `std::this_thread::sleep_for(std::chrono::milliseconds(500))` (C++, in `<thread>` but doesn't spawn a thread), `Thread.sleep(1000)` (Java), `await new Promise(r => setTimeout(r, 1000))` (JS).

**Clearing the screen:** most languages let you clear the terminal either through a system command or a short escape sequence — look up what's available for your language and OS.

---

## Feature Specification & Test Case

### Real-Time Playback

Each frame prints a header (generation number, population) followed by the grid, then pauses, clears, and prints the next frame.

<details>
<summary><strong>🧪 Test Case: Blinker (delay = 1s)</strong></summary>
<br>

**Input:**
```
animate
5 5
2
.....
.###.
.....
.....
.....
```

**Frames (each replaces the previous one on screen):**
```
Generation: 0   Population: 3
.....
.###.
.....
.....
.....
```
```
Generation: 1   Population: 3
..#..
..#..
..#..
.....
.....
```
```
Generation: 2   Population: 3
.....
.###.
.....
.....
.....
Simulation complete.
```
</details>

---

## How to Run Your Submission

Add a short comment block at the top of your code (or a separate `RUN.md`) telling us exactly how to run it. Include:

- Language and version used
- Compile command, if your language needs one (e.g. `g++ solution.cpp -o sim`)
- Exact run command (e.g. `python solution.py`, `./sim`)
- Any input file names or arguments your program expects

Example:
```
// Language: C++17
// Compile: g++ level3.cpp -o level3
// Run: ./level3
// Input: enter values directly in terminal when prompted, or pipe a file: ./level3 < input.txt
```

Submissions without clear run instructions may take longer to evaluate.
